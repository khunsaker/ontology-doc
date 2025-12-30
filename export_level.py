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
# Generalization logic + exceptions
# -----------------------------------------------------------------------------

LEVEL_ORDER = ["Hub", "Category", "Kind", "Family", "Type", "Class", "Instance"]

NOISE_LABELS = {
    "Object", "People", "Person", "SharkNode", "System",
    "__MigrationNode__", "__MigrationRelationship__"
}

# Canonical display names (tune freely)
CANONICAL_DISPLAY = {
    # Air specificity (keep exact strings as requested)
    "AirType": "AirType",
    "AirSubType": "AirSubType",
    "AirVariant": "AirVariant",
    "AirSubVariant": "AirSubVariant",
    "AirModel": "AirModel",
    "AirSubModel": "AirSubModel",
    "AirInstance": "AirInstance",

    # Ship specificity
    "ShipType": "ShipType",
    "ShipSubType": "ShipSubType",
    "ShipClass": "ShipClass",
    "ShipSubClass": "ShipSubClass",
    "ShipInstance": "ShipInstance",

    # Other common endpoints
    "ArmedForces": "ArmedForces",
    "Company": "Company",
    "Manufacturer": "Company",  # treat as synonym unless you want distinct
    "Organization": "Organization",
    "Place": "Place",
    "Country": "Country",

    # Broad labels (allowed but de-prioritized)
    "AirSystem": "AirSystem",
    "AirVehicle": "AirVehicle",
    "SeaVessel": "SeaVessel",

    # Family overrides requested
    "WeaponType": "WeaponType",
}

# Prefer most-specific Air label if present (most specific first)
AIR_SPECIFIC_PRIORITY = [
    "AirInstance",
    "AirSubModel",
    "AirModel",
    "AirSubVariant",
    "AirVariant",
    "AirSubType",
    "AirType",
]

# Prefer most-specific Ship label if present (most specific first)
SHIP_SPECIFIC_PRIORITY = [
    "ShipInstance",
    "ShipSubClass",
    "ShipClass",
    "ShipSubType",
    "ShipType",
]

# General label priority fallback (after domain-specific specificity checks)
LEVEL_LABEL_PRIORITY = [
    "Hub", "Category", "Kind", "Family",
    "WeaponType",
    "Company", "Manufacturer",
    "ArmedForces",
    "Organization",
    "Country",
    "Place",
    # Broad/utility labels last
    "AirSystem",
    "AirVehicle",
    "SeaVessel",
]

# Levels that should render relationships in generalized mode even if nodes are listed.
GENERALIZE_RELS_LEVELS = {"Family"}

# Family-level relationship-specific target overrides
REL_TARGET_OVERRIDES = {
    # Requested:
    "Weapon_Type": "WeaponType",
    "Derivative": "AirType",
}

# Kind-level collapse: Nation => Country
KIND_COLLAPSE_REL_TYPES = {"Nation"}
KIND_COLLAPSE_TARGET = {"Nation": "Country"}


def _safe_level_index(level_label: str) -> int:
    try:
        return LEVEL_ORDER.index(level_label)
    except ValueError:
        return 10_000


def is_deep_level(level_label: str) -> bool:
    return _safe_level_index(level_label) > _safe_level_index("Family")


def pick_level_display(labels: List[str]) -> str:
    """
    Generalized endpoint selection.

    - If Air hierarchy labels exist, choose the MOST SPECIFIC Air* label.
    - If Ship hierarchy labels exist, choose the MOST SPECIFIC Ship* label.
    - Otherwise choose by LEVEL_LABEL_PRIORITY.
    - Otherwise fallback to any remaining label.
    """
    s = set(labels or []) - NOISE_LABELS

    for key in AIR_SPECIFIC_PRIORITY:
        if key in s:
            return CANONICAL_DISPLAY.get(key, key)

    for key in SHIP_SPECIFIC_PRIORITY:
        if key in s:
            return CANONICAL_DISPLAY.get(key, key)

    for key in LEVEL_LABEL_PRIORITY:
        if key in s:
            return CANONICAL_DISPLAY.get(key, key)

    for lbl in sorted(s):
        return CANONICAL_DISPLAY.get(lbl, lbl)

    return "Node"


def build_outgoing_generalized(
    outgoing_norm: List[Dict[str, Any]],
    *,
    level_label: str,
) -> List[Dict[str, Any]]:
    """
    Build generalized unique outgoing rel patterns with counts.

    Supports:
      - Family-level relationship target overrides (REL_TARGET_OVERRIDES)
      - Air/Ship specificity via pick_level_display()
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

        # Family overrides requested
        if level_label == "Family" and rel_type in REL_TARGET_OVERRIDES:
            to_level = REL_TARGET_OVERRIDES[rel_type]

        counter[(from_level, rel_type, to_level)] += 1

    out = [
        {"from_level": k[0], "rel_type": k[1], "to_level": k[2], "count": v}
        for k, v in counter.items()
    ]
    out.sort(key=lambda x: (-x["count"], x["from_level"], x["rel_type"], x["to_level"]))
    return out


def export_level(cfg: dict, level_label: str) -> dict:
    level_label = sanitize_label(level_label)

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

    # Outgoing only
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

    with GraphDatabase.driver(cfg["uri"], auth=(cfg["user"], cfg["password"])) as driver:
        with driver.session(database=cfg["database"]) as session:
            grouping_rows = session.execute_read(lambda tx: fetch_all(tx, q_grouping))
            nodes_rows = session.execute_read(lambda tx: fetch_all(tx, q_nodes))
            props_rows = session.execute_read(lambda tx: fetch_all(tx, q_props))
            outgoing_rows = session.execute_read(lambda tx: fetch_all(tx, q_outgoing))

            parent_groups_rows = []
            if rel_type_exists(session, level_label):
                parent_groups_rows = session.execute_read(lambda tx: fetch_all(tx, q_parent_groups))

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
                    {"parent": parent, "heading": group_heading(parent), "nodes": kids}
                )

    outgoing_norm = norm_relationship_rows(outgoing_rows)

    # Kind-level: collapse Nation spam to (X)-[Nation]->(Country) with counts
    outgoing_generalized_exceptions: List[Dict[str, Any]] = []
    if level_label == "Kind":
        keep: List[Dict[str, Any]] = []
        collapsed_counter: Counter[Tuple[str, str]] = Counter()  # (from_name, rel_type) -> count

        for r in outgoing_norm:
            rt = (r.get("rel_type") or "").strip()
            if rt in KIND_COLLAPSE_REL_TYPES:
                fn = r.get("from_name") or "Node"
                collapsed_counter[(fn, rt)] += 1
            else:
                keep.append(r)

        outgoing_norm = keep

        for (from_name, rt), cnt in collapsed_counter.items():
            outgoing_generalized_exceptions.append(
                {
                    "from_level": from_name,  # show the Kind node (e.g., National)
                    "rel_type": rt,
                    "to_level": KIND_COLLAPSE_TARGET.get(rt, "Node"),
                    "count": cnt,
                }
            )

        outgoing_generalized_exceptions.sort(
            key=lambda x: (-x["count"], x["from_level"], x["rel_type"], x["to_level"])
        )

    outgoing_generalized = build_outgoing_generalized(outgoing_norm, level_label=level_label)

    deep = is_deep_level(level_label)
    show_node_list = (not deep)

    # For deep levels: suppress explicit node listings
    if deep:
        node_names_for_card = []
        parent_groups_for_card = []
    else:
        node_names_for_card = node_names
        parent_groups_for_card = parent_groups

    relationships_mode = (
        "generalized"
        if (deep or level_label in GENERALIZE_RELS_LEVELS)
        else "detailed"
    )

    return {
        "level": level_label,
        "level_label": level_label,
        "card": {
            "title": f"{level_label} Level",
            "show_node_list": show_node_list,
            "relationships_mode": relationships_mode,
            "parent_groups": parent_groups_for_card,
            "labels": {"grouping": grouping_labels},
            "node_names": node_names_for_card,
            "total_nodes": total_nodes,
            "properties": [{"name": p, "type": "unknown", "required": False} for p in properties],
            "relationships": {
                "outgoing": outgoing_norm,
                "outgoing_generalized": outgoing_generalized,
                "outgoing_generalized_exceptions": outgoing_generalized_exceptions,
            },
        },
        "meta": {
            "db": cfg["database"],
            "generated_utc": now_utc(),
            "exporter_version": "0.4",
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
