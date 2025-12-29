#!/usr/bin/env python3

import json
import argparse
from pathlib import Path
from collections import defaultdict

from jinja2 import Environment, FileSystemLoader, select_autoescape


# Only these levels keep Shark_Name as the displayed node identity.
NAMED_LEVELS = {"Hub", "Category", "Kind", "Family"}

# Labels we never want to use as the collapsed display label.
# (We do NOT validate labels; we just avoid using these for display.)
NEVER_COLLAPSE_TO = {"SharkNode", "AirSystem", "_Bloom_Perspective_"}


def sort_labels(labels):
    """Deterministic label ordering and basic cleanup."""
    out = []
    for x in (labels or []):
        if x is None:
            continue
        s = str(x).strip()
        if not s:
            continue
        out.append(s)
    return sorted(out)


def pick_level_label(labels):
    """
    Choose a single representative label for a node when collapsing.

    Rules:
      1) If any core level label present, return it (Hub/Category/Kind/Family).
      2) Otherwise return first match in SECONDARY_PRIORITY.
      3) Otherwise return first non-NEVER_COLLAPSE_TO label alphabetically.
      4) Fallback: 'Unknown'
    """
    label_set = set(labels or [])

    # 1) Core levels
    for core in ["Hub", "Category", "Kind", "Family"]:
        if core in label_set:
            return core

    # 2) Secondary priority list (NO underscore labels, NO AirSystem)
    SECONDARY_PRIORITY = [
        # Air chain (preferred collapsed labels)
        "AirType",
        "AirSubType",
        "AirVariant",
        "AirSubVariant",
        "AirModel",
        "AirSubModel",
        "AirInstance",

        # Maritime chain (preferred collapsed labels)
        "ShipType",
        "ShipSubType",
        "ShipVariant",
        "ShipClass",
        "ShipSubClass",
        "ShipInstance",

        # Other chains
        "Place",
        "Organization",
        "Weapon",

        # Common geo levels (if used in your ontology)
        "Continent",
        "Country",
        "Region",
        "City",
    ]
    for lab in SECONDARY_PRIORITY:
        if lab in label_set:
            return lab

    # 3) Fallback: first label alphabetically excluding banned labels
    candidates = sorted([l for l in label_set if l not in NEVER_COLLAPSE_TO])
    return candidates[0] if candidates else "Unknown"


def display_node(shark_name, labels):
    """
    If node is in a named level, display Shark_Name.
    Otherwise collapse to a chosen level label.
    """
    label_set = set(labels or [])
    if any(lvl in label_set for lvl in NAMED_LEVELS):
        return str(shark_name)
    return pick_level_label(labels)


def aggregate_relationships(raw_rels):
    """
    Collapse raw relationship rows into unique DISPLAYED relationships and count them.

    Counting key:
      (from_display, rel_type, to_display)

    We keep representative source/target label strings (first-seen) for display,
    but they do NOT affect grouping/counting.
    """
    counts = defaultdict(int)
    exemplar = {}

    for r in raw_rels or []:
        src_labels = sort_labels(r.get("source_labels"))
        tgt_labels = sort_labels(r.get("target_labels"))

        from_disp = display_node(r.get("from_name"), src_labels)
        to_disp = display_node(r.get("to_name"), tgt_labels)
        rel_type = r.get("rel_type")

        key = (from_disp, rel_type, to_disp)
        counts[key] += 1

        if key not in exemplar:
            exemplar[key] = {
                "from_display": from_disp,
                "rel_type": rel_type,
                "to_display": to_disp,
                "source_labels_str": ", ".join(src_labels),
                "target_labels_str": ", ".join(tgt_labels),
            }

    out = []
    for key, c in counts.items():
        row = dict(exemplar[key])
        row["count"] = c
        out.append(row)

    out.sort(key=lambda x: (
        x.get("from_display") or "",
        x.get("rel_type") or "",
        x.get("to_display") or "",
        x.get("source_labels_str") or "",
        x.get("target_labels_str") or "",
    ))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", required=True, help="Input JSON (e.g., export/json/Category.json)")
    ap.add_argument("--out", dest="outfile", required=True, help="Output MD (e.g., cards/Category.md)")
    ap.add_argument("--template", default="semantic_card.md.j2", help="Template filename in templates/")
    args = ap.parse_args()

    in_path = Path(args.infile)
    out_path = Path(args.outfile)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    data = json.loads(in_path.read_text(encoding="utf-8"))
    card = data["card"]

    # Documentation requirement: Shark_Name is required
    for p in card.get("properties", []):
        if p.get("name") == "Shark_Name":
            p["required"] = True
            if p.get("type") in (None, "", "unknown"):
                p["type"] = "string"

    # Aggregate relationships for rendering
    rels = card.get("relationships", {})
    card["relationships_agg"] = {
        "incoming": aggregate_relationships(rels.get("incoming", [])),
        "outgoing": aggregate_relationships(rels.get("outgoing", [])),
    }

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(enabled_extensions=()),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(args.template)
    rendered = template.render(card=card)

    out_path.write_text(rendered, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()


