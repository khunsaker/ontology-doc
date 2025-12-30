#!/usr/bin/env python3

import os
import json
from datetime import datetime, timezone
from neo4j import GraphDatabase


def require_env(name):
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sanitize_label(label):
    import re
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", label):
        raise SystemExit(f"Invalid label name: {label}")
    return label


def fetch_all(tx, query):
    return [r.data() for r in tx.run(query)]


def export_level(cfg, level_label):
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
    with GraphDatabase.driver(
        cfg["uri"], auth=(cfg["user"], cfg["password"])
    ) as driver:
        with driver.session(database=cfg["database"]) as session:
            grouping = session.execute_read(lambda tx: fetch_all(tx, q_grouping))
            nodes = session.execute_read(lambda tx: fetch_all(tx, q_nodes))
            props = session.execute_read(lambda tx: fetch_all(tx, q_props))
            incoming = session.execute_read(lambda tx: fetch_all(tx, q_incoming))
            outgoing = session.execute_read(lambda tx: fetch_all(tx, q_outgoing))
            parent_groups_rows = session.execute_read(lambda tx: fetch_all(tx, q_parent_groups))


    # ----------------------------
    # Normalize data
    # ----------------------------
    grouping_labels = sorted(set(grouping[0]["grouping"])) if grouping else []

    node_names = []
    if nodes and "node_names" in nodes[0]:
        node_names = sorted(set(nodes[0]["node_names"]))

    properties = sorted(set(props[0]["props"])) if props else []

    def group_heading(parent):
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
            parent = row["parent_name"]
            kids = sorted(set(row.get("child_names") or []))
            parent_groups.append({
                "parent": parent,
                "heading": group_heading(parent),
                "nodes": kids
            })


    def norm(rows):
        return [
            {
                "from_name": r["from_name"],
                "rel_type": r["rel_type"],
                "to_name": r["to_name"],
                "source_labels": sorted(r["source_labels"]),
                "target_labels": sorted(r["target_labels"]),
            }
            for r in rows
        ]

    # ----------------------------
    # Final payload
    # ----------------------------
    return {
        "level": level_label,
        "level_label": level_label,
        "card": {
            "title": f"{level_label} Level",
	    "parent_groups": parent_groups,
            "labels": {
                "grouping": grouping_labels
            },
            "node_names": node_names,
            "properties": [
                {"name": p, "type": "unknown", "required": False}
                for p in properties
            ],
            "relationships": {
                "incoming": norm(incoming),
                "outgoing": norm(outgoing),
            }
        },
        "meta": {
            "db": cfg["database"],
            "generated_utc": now_utc(),
            "exporter_version": "0.1"
        }
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
