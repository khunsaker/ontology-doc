#!/usr/bin/env python3

import os
import json
from datetime import datetime, timezone
from neo4j import GraphDatabase


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sanitize_label(label: str) -> str:
    import re
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", label):
        raise SystemExit(f"Invalid label name: {label}")
    return label


def fetch_all(tx, query: str):
    return [r.data() for r in tx.run(query)]


def rel_type_exists(session, rel_type: str) -> bool:
    """
    Return True iff the relationship type exists in the database.
    Uses db.relationshipTypes() to avoid warnings from pattern-matching on
    non-existent relationship types.
    """
    try:
        rec = session.run(
            """
            CALL db.relationshipTypes() YIELD relationshipType
            WHERE relationshipType = $t
            RETURN count(*) > 0 AS exists
            """,
            t=rel_type,
        ).single()
        return bool(rec and rec.get("exists"))
    except Exception:
        # If procedures are unavailable/restricted, fail closed (skip parent grouping).
        return False


def norm_relationship_rows(rows):
    out = []
    for r in rows or []:
        out.append(
            {
                "from_name": r.get("from_name"),
                "rel_type": r.get("rel_type"),
                "to_name": r.get("to_name"),
                "source_labels": sorted(r.get("source_labels") or []),
                "target_labels": sorted(r.get("target_labels") or []),
            }
        )
    return out


def export_level(cfg: dict, level_label: str) -> dict:
    level_label = sanitize_label(level_label)

    # ----------------------------
    # Cypher Queries
    # ----------------------------

    q_grouping = f"""
    MATCH (n:`{level_label}`)
    WITH collect(DISTINCT labels(n)) AS lbls
    UNWIND lbls AS l
    UNWIND l AS lbl
    RETURN collect(DISTINCT lbl) AS grouping
    """

    q_nodes = f"""
    MATCH (n:`{level_label}`)
    WHERE n.Shark_Name IS NOT NULL AND trim(toString(n.Shark_Name)) <> ''
    RETURN collect(DISTINCT n.Shark_Name) AS node_names
    """

    q_props = f"""
    MATCH (n:`{level_label}`)
    WITH collect(DISTINCT keys(n)) AS key_sets
    UNWIND key_sets AS ks
    UNWIND ks AS k
    RETURN collect(DISTINCT k) AS props
    """

    q_incoming = f"""
    MATCH (src)-[r]->(tgt:`{level_label}`)
    WHERE src.Shark_Name IS NOT NULL AND tgt.Shark_Name IS NOT NULL
    RETURN
      src.Shark_Name AS from_name,
      type(r) AS rel_type,
      tgt.Shark_Name AS to_name,
      labels(src) AS source_labels,
      labels(tgt) AS target_labels
    ORDER BY from_name, rel_type, to_name
    """

    q_outgoing = f"""
    MATCH (src:`{level_label}`)-[r]->(tgt)
    WHERE src.Shark_Name IS NOT NULL AND tgt.Shark_Name IS NOT NULL
    RETURN
      src.Shark_Name AS from_name,
      type(r) AS rel_type,
      tgt.Shark_Name AS to_name,
      labels(src) AS source_labels,
      labels(tgt) AS target_labels
    ORDER BY from_name, rel_type, to_name
    """

    # Parent grouping assumes: (p)-[:<LevelLabel>]->(n:<LevelLabel>)
    # We only execute this if the relationship type exists (to avoid warnings).
    q_parent_groups = f"""
    MATCH (p)-[:`{level_label}`]->(n:`{level_label}`)
    WHERE p.Shark_Name IS NOT NULL AND trim(toString(p.Shark_Name)) <> ''
      AND n.Shark_Name IS NOT NULL AND trim(toString(n.Shark_Name)) <> ''
    RETURN
      p.Shark_Name AS parent_name,
      collect(DISTINCT n.Shark_Name) AS child_names
    ORDER BY parent_name
    """

    # ----------------------------
    # Execute queries
    # ----------------------------
    with GraphDatabase.driver(cfg["uri"], auth=(cfg["user"], cfg["password"])) as driver:
        with driver.session(database=cfg["database"]) as session:
            grouping_rows = session.execute_read(lambda tx: fetch_all(tx, q_grouping))
            nodes_rows = session.execute_read(lambda tx: fetch_all(tx, q_nodes))
            props_rows = session.execute_read(lambda tx: fetch_all(tx, q_props))

            # Hub: only outgoing relationships (per your ontology); skip incoming query.
            incoming_rows = []
            if level_label != "Hub":
                incoming_rows = session.execute_read(lambda tx: fetch_all(tx, q_incoming))

            outgoing_rows = session.execute_read(lambda tx: fetch_all(tx, q_outgoing))

            parent_groups_rows = []
            if rel_type_exists(session, level_label):
                parent_groups_rows = session.execute_read(lambda tx: fetch_all(tx, q_parent_groups))

    # ----------------------------
    # Normalize data
    # ----------------------------
    grouping_labels = []
    if grouping_rows and "grouping" in grouping_rows[0]:
        grouping_labels = sorted(set(grouping_rows[0]["grouping"] or []))

    node_names = []
    if nodes_rows and "node_names" in nodes_rows[0]:
        node_names = sorted(set(nodes_rows[0]["node_names"] or []))

    total_nodes = len(node_names)

    properties = []
    if props_rows and "props" in props_rows[0]:
        properties = sorted(set(props_rows[0]["props"] or []))

    def group_heading(parent: str) -> str:
        # Your examples for Kind level:
        # Aircraft Kind, Organization Kind, Place Kind, Ships Kind, Weapon Kind
        if level_label == "Kind":
            if parent == "Ship":
                return "Ships Kind"
            if parent == "Aircraft":
                return "Aircraft Kind"
            if parent == "Organization":
                return "Organization Kind"
            if parent == "Place":
                return "Place Kind"
            if parent == "Weapon":
                return "Weapon Kind"

        # Category example: Hub (Parent)
        if level_label == "Category" and parent == "Hub":
            return "Hub (Parent)"

        return f"{parent} {level_label}"

    parent_groups = []
    if parent_groups_rows:
        for row in parent_groups_rows:
            parent = row.get("parent_name")
            kids = sorted(set(row.get("child_names") or []))
            if parent:
                parent_groups.append(
                    {
                        "parent": parent,
                        "heading": group_heading(parent),
                        "nodes": kids,
                    }
                )

    # IMPORTANT: We do NOT force Hub into parent_groups.
    # For Hub, the template should render using node_names (Nodes (Shark_Name)).

    # ----------------------------
    # Final payload
    # ----------------------------
    return {
        "level": level_label,
        "level_label": level_label,
        "card": {
            "title": f"{level_label} Level",
            "parent_groups": parent_groups,
            "labels": {"grouping": grouping_labels},
            "node_names": node_names,
            "total_nodes": total_nodes,
            "properties": [{"name": p, "type": "unknown", "required": False} for p in properties],
            "relationships": {
                "incoming": norm_relationship_rows(incoming_rows),
                "outgoing": norm_relationship_rows(outgoing_rows),
            },
        },
        "meta": {
            "db": cfg["database"],
            "generated_utc": now_utc(),
            "exporter_version": "0.1",
        },
    }


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--level-label", required=True)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    cfg = {
        "uri": os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687"),
        "user": os.getenv("NEO4J_USER", "neo4j"),
        "password": require_env("NEO4J_PASSWORD"),
        "database": os.getenv("NEO4J_DB", "Shark2"),
    }

    output_path = args.out or f"export/json/{args.level_label}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    data = export_level(cfg, args.level_label)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
