#!/usr/bin/env python3

import os
import json
from datetime import datetime, timezone
from collections import Counter
from typing import Any, Dict, List, Tuple

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


# -----------------------------------------------------------------------------
# Generalization logic
# -----------------------------------------------------------------------------

# Ontology ladder. Unknown levels are treated as "deep" to prevent explosion.
LEVEL_ORDER = ["Hub", "Category", "Kind", "Family", "Type", "Class", "Instance"]

# Labels that are documentation noise and should not drive generalization.
NOISE_LABELS = {
    "Object", "People", "Person", "SharkNode", "System",
    "__MigrationNode__", "__MigrationRelationship__"
}

# Canonical display names (tune as desired). Manufacturer is treated as Company.
CANONICAL_DISPLAY = {
    "AirType": "Air Type",
    "AirSystem": "Air System",
    "AirVehicle": "Air Vehicle",
    "ArmedForces": "Armed Forces",
    "Company": "Company",
    "Manufacturer": "Company",
    "Organization": "Organization",
    "Place": "Place",
    "Weapon": "Weapon",
    "Ship": "Ship",
}

# Priority: first match wins after removing NOISE_LABELS.
LEVEL_LABEL_PRIORITY = [
    "Hub", "Category", "Kind", "Family",
    "AirType",
    "Type", "Class", "Instance",
    "Company", "Manufacturer",
    "ArmedForces",
    "Organization",
    "Place",
    "Weapon",
    "Ship",
    "AirSystem",
    "AirVehicle",
]


def _safe_level_index(level_label: str) -> int:
    try:
        return LEVEL_ORDER.index(level_label)
    except ValueError:
        return 10_000


def is_deep_level(level_label: str) -> bool:
    """Deep = strictly below Family in the ontology ladder."""
    return _safe_level_index(level_label) > _safe_level_index("Family")


def pick_level_display(labels: List[str]) -> str:
    """
    Choose a stable generalized endpoint label from a node's label set,
    ignoring noise labels. Uses a priority list, then falls back.
    """
    s = set(labels or [])
    s = s - NOISE_LABELS

    for key in LEVEL_LABEL_PRIORITY:
        if key in s:
            return CANONICAL_DISPLAY.get(key, key)

    # Fallback: any remaining label (stable)
    for lbl in sorted(s):
        return CANONICAL_DISPLAY.get(lbl, lbl)

    return "Node"


def build_outgoing_generalized(outgoing_norm: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Build generalized unique outgoing rel patterns with counts, from the
    normalized outgoing relationship rows.

    Safer behavior:
      - treats rel_type as invalid if blank/whitespace
      - tolerates missing/empty labels without throwing
      - produces stable output ordering
    """
    counter: Counter[Tuple[str, str, str]] = Counter()

    for r in outgoing_norm or []:
        rel_type = r.get("rel_type")
        if rel_type is None:
            continue
        rel_type = str(rel_type).strip()
        if rel_type == "":
            continue

        src_labels = r.get("source_labels") or []
        tgt_labels = r.get("target_labels") or []

        from_level = pick_level_display(src_labels)
        to_level = pick_level_display(tgt_labels)

        counter[(from_level, rel_type, to_level)] += 1

    out = [
        {"from_level": k[0], "rel_type": k[1], "to_level": k[2], "count": v}
        for k, v in counter.items()
    ]

    # Sort: most represented first, then stable alpha
    out.sort(key=lambda x: (-x["count"], x["from_level"], x["rel_type"], x["to_level"]))
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

    # Outgoing only (Incoming intentionally removed to prevent duplication)
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

    outgoing_norm = norm_relationship_rows(outgoing_rows)
    outgoing_generalized = build_outgoing_generalized(outgoing_norm)

    deep = is_deep_level(level_label)
    show_node_list = (not deep)

    if deep:
        node_names_for_card = []
        parent_groups_for_card = []
    else:
        node_names_for_card = node_names
        parent_groups_for_card = parent_groups

    return {
        "level": level_label,
        "level_label": level_label,
        "card": {
            "title": f"{level_label} Level",
            "show_node_list": show_node_list,
            "parent_groups": parent_groups_for_card,
            "labels": {"grouping": grouping_labels},
            "node_names": node_names_for_card,
            "total_nodes": total_nodes,
            "properties": [{"name": p, "type": "unknown", "required": False} for p in properties],
            "relationships": {
                "outgoing": outgoing_norm,
                "outgoing_generalized": outgoing_generalized,
            },
        },
        "meta": {
            "db": cfg["database"],
            "generated_utc": now_utc(),
            "exporter_version": "0.3",
        },
    }


def main() -> None:
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
