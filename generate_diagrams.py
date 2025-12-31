#!/usr/bin/env python3
"""Generate Graphviz diagrams from ontology JSON exports."""

import json
import subprocess
from pathlib import Path


def load_json(path: Path) -> dict:
    """Load JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


def sanitize_id(name: str) -> str:
    """Convert name to valid Graphviz node ID."""
    return name.replace(" ", "_").replace("-", "_").replace("/", "_")


def generate_overview_dot(json_dir: Path) -> str:
    """Generate DOT for high-level overview (Hub → Category → Kind → Family)."""

    hub = load_json(json_dir / "Hub.json")
    category = load_json(json_dir / "Category.json")
    kind = load_json(json_dir / "Kind.json")
    family = load_json(json_dir / "Family.json")

    lines = [
        'digraph overview {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica"];',
        '    edge [fontname="Helvetica", fontsize=9];',
        '',
        '    // Level labels on the left',
        '    node [shape=plaintext, style="", fillcolor=none, fontsize=14, fontname="Helvetica Bold"];',
        '    label_hub [label="Hub"];',
        '    label_category [label="Category"];',
        '    label_kind [label="Kind"];',
        '    label_family [label="Family"];',
        '    { rank=same; label_hub; }',
        '    { rank=same; label_category; }',
        '    { rank=same; label_kind; }',
        '    { rank=same; label_family; }',
        '    label_hub -> label_category -> label_kind -> label_family [style=invis];',
        '',
        '    // Reset node style for data nodes',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=12];',
        '',
        '    // Hub level',
    ]

    # Add hub node
    hub_name = hub["card"]["node_names"][0]
    lines.append(f'    {sanitize_id(hub_name)} [label="{hub_name}", fillcolor="#4a90d9", fontcolor=white];')
    lines.append(f'    {{ rank=same; label_hub; {sanitize_id(hub_name)}; }}')
    lines.append('')

    # Category level
    lines.append('    // Category level')
    categories = category["card"]["node_names"]
    cat_ids = []
    for cat in categories:
        cat_id = sanitize_id(cat)
        cat_ids.append(cat_id)
        lines.append(f'    {cat_id} [label="{cat}", fillcolor="#5cb85c", fontcolor=white];')
    lines.append(f'    {{ rank=same; label_category; {"; ".join(cat_ids)}; }}')
    lines.append('')

    # Hub → Category edges with label
    for rel in hub["card"]["relationships"]["outgoing"]:
        from_id = sanitize_id(rel["from_name"])
        to_id = sanitize_id(rel["to_name"])
        lines.append(f'    {from_id} -> {to_id} [label="Category"];')
    lines.append('')

    # Kind level - group by parent
    lines.append('    // Kind level')

    # Define groups to collapse into a single node: {parent: (collapsed_label, node_count)}
    collapse_groups = {}
    kind_ids = []
    for group in kind["card"]["parent_groups"]:
        if group["parent"] == "Place":
            # Collapse Place kinds (continents) into single node
            collapse_groups["Place"] = ("Continents", len(group["nodes"]))
        else:
            for node in group["nodes"]:
                node_id = sanitize_id(node)
                kind_ids.append(node_id)
                lines.append(f'    {node_id} [label="{node}", fillcolor="#f0ad4e", fontcolor=white];')

    # Add collapsed group nodes
    for parent, (label, count) in collapse_groups.items():
        node_id = sanitize_id(label)
        kind_ids.append(node_id)
        lines.append(f'    {node_id} [label="{label}\\n({count})", fillcolor="#f0ad4e", fontcolor=white];')

    lines.append(f'    {{ rank=same; label_kind; {"; ".join(kind_ids)}; }}')
    lines.append('')

    # Category → Kind edges with label
    for rel in category["card"]["relationships"]["outgoing"]:
        from_id = sanitize_id(rel["from_name"])
        to_name = rel["to_name"]

        # Check if this edge should point to a collapsed group
        if rel["from_name"] in collapse_groups:
            to_id = sanitize_id(collapse_groups[rel["from_name"]][0])
            # Only add edge once for collapsed groups
            edge = f'    {from_id} -> {to_id} [label="Kind"];'
            if edge not in lines:
                lines.append(edge)
        else:
            to_id = sanitize_id(to_name)
            lines.append(f'    {from_id} -> {to_id} [label="Kind"];')

    lines.append('')

    # Family level - collapsed by parent category
    lines.append('    // Family level')

    # Group families by their parent category (Aircraft, Ship, Weapon, Organization, Place)
    family_by_category = {}
    # Initialize all categories with 0
    for cat in categories:
        family_by_category[cat] = 0

    for group in family["card"]["parent_groups"]:
        parent = group["parent"]
        count = len(group["nodes"])
        # Map parent Kind to its Category
        for kg in kind["card"]["parent_groups"]:
            if parent in kg["nodes"]:
                cat = kg["parent"]
                family_by_category[cat] += count
                break

    # Add collapsed family nodes per category
    family_ids = []
    for cat, count in family_by_category.items():
        node_id = f"Family_{sanitize_id(cat)}"
        family_ids.append(node_id)
        if count > 0:
            lines.append(f'    {node_id} [label="{cat} Families\\n({count})", fillcolor="#d9534f", fontcolor=white];')
        else:
            lines.append(f'    {node_id} [label="{cat} Families\\n(N/A)", fillcolor="#d9534f", fontcolor=white];')

    lines.append(f'    {{ rank=same; label_family; {"; ".join(family_ids)}; }}')
    lines.append('')

    # Kind → Family edges (generalized) with label
    added_family_edges = set()
    for kg in kind["card"]["parent_groups"]:
        cat = kg["parent"]
        for kind_node in kg["nodes"]:
            # Use collapsed group name for Place (Continents)
            if cat == "Place":
                from_id = "Continents"
            else:
                from_id = sanitize_id(kind_node)
            to_id = f"Family_{sanitize_id(cat)}"
            edge = f'    {from_id} -> {to_id} [label="Family"];'
            if edge not in added_family_edges:
                added_family_edges.add(edge)
                lines.append(edge)

    lines.append('}')
    return '\n'.join(lines)


def generate_air_domain_dot(json_dir: Path) -> str:
    """Generate DOT for Air domain hierarchy."""

    # Define the air hierarchy levels (excluding AirInstance which has special connections)
    air_chain = ["AirType", "AirSubType", "AirVariant", "AirSubVariant", "AirModel", "AirSubModel"]

    colors = {
        "AirType": "#4a90d9",
        "AirSubType": "#5cb85c",
        "AirVariant": "#f0ad4e",
        "AirSubVariant": "#d9534f",
        "AirModel": "#9b59b6",
        "AirSubModel": "#3498db",
        "AirInstance": "#1abc9c"
    }

    lines = [
        'digraph air_domain {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontcolor=white];',
        '    edge [fontname="Helvetica", fontsize=9];',
        '',
        '    // Air Domain Hierarchy',
        '    label="Air Domain Hierarchy";',
        '    labelloc=t;',
        '    fontsize=16;',
        '    fontname="Helvetica Bold";',
        '',
    ]

    # Add nodes for the chain
    for level in air_chain:
        json_path = json_dir / f"{level}.json"
        if json_path.exists():
            data = load_json(json_path)
            count = data["card"]["total_nodes"]
            label = f"{level}\\n({count} nodes)"
            lines.append(f'    {level} [label="{label}", fillcolor="{colors[level]}"];')

    # Add AirInstance node
    json_path = json_dir / "AirInstance.json"
    if json_path.exists():
        data = load_json(json_path)
        count = data["card"]["total_nodes"]
        label = f"AirInstance\\n({count} nodes)"
        lines.append(f'    AirInstance [label="{label}", fillcolor="{colors["AirInstance"]}"];')

    lines.append('')

    # Chain connections (Derivative relationships)
    chain_rels = [
        ("AirType", "AirSubType", "SubType"),
        ("AirSubType", "AirVariant", "Variant"),
        ("AirVariant", "AirSubVariant", "SubVariant"),
        ("AirSubVariant", "AirModel", "Model"),
        ("AirModel", "AirSubModel", "SubModel"),
    ]
    for from_node, to_node, rel in chain_rels:
        lines.append(f'    {from_node} -> {to_node} [label="{rel}"];')

    lines.append('')

    # Instance relationships - all levels can connect to AirInstance
    lines.append('    // Instance relationships')
    for level in air_chain:
        lines.append(f'    {level} -> AirInstance [label="Instance"];')

    lines.append('}')
    return '\n'.join(lines)


def generate_ship_domain_dot(json_dir: Path) -> str:
    """Generate DOT for Ship domain hierarchy."""

    ship_levels = ["ShipType", "ShipSubType", "ShipClass", "ShipSubClass", "ShipInstance"]

    colors = {
        "ShipType": "#2c3e50",
        "ShipSubType": "#34495e",
        "ShipClass": "#7f8c8d",
        "ShipSubClass": "#95a5a6",
        "ShipInstance": "#16a085"
    }

    lines = [
        'digraph ship_domain {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontcolor=white];',
        '    edge [fontname="Helvetica", fontsize=9];',
        '',
        '    // Ship Domain Hierarchy',
        '    label="Ship Domain Hierarchy";',
        '    labelloc=t;',
        '    fontsize=16;',
        '    fontname="Helvetica Bold";',
        '',
    ]

    # Add nodes for each level with counts
    for level in ship_levels:
        json_path = json_dir / f"{level}.json"
        if json_path.exists():
            data = load_json(json_path)
            count = data["card"]["total_nodes"]
            label = f"{level}\\n({count} nodes)"
            lines.append(f'    {level} [label="{label}", fillcolor="{colors[level]}"];')

    lines.append('')

    # Standard chain connections
    lines.append('    // Standard chain')
    lines.append('    ShipType -> ShipSubType [label="SubType"];')
    lines.append('    ShipClass -> ShipSubClass [label="SubClass"];')

    lines.append('')

    # Class relationships - both ShipType and ShipSubType can connect to ShipClass
    lines.append('    // Class relationships')
    lines.append('    ShipType -> ShipClass [label="Class"];')
    lines.append('    ShipSubType -> ShipClass [label="Class"];')

    lines.append('')

    # Instance relationships - both ShipClass and ShipSubClass can connect to ShipInstance
    lines.append('    // Instance relationships')
    lines.append('    ShipClass -> ShipInstance [label="Instance", constraint=false];')
    lines.append('    ShipSubClass -> ShipInstance [label="Instance"];')

    lines.append('}')
    return '\n'.join(lines)


def render_dot_to_pdf(dot_path: Path, pdf_path: Path):
    """Render DOT file to PDF using Graphviz."""
    subprocess.check_call(["dot", "-Tpdf", str(dot_path), "-o", str(pdf_path)])


def main():
    root = Path(__file__).parent.resolve()
    json_dir = root / "export" / "json"
    diagrams_dir = root / "diagrams"
    diagrams_dir.mkdir(exist_ok=True)

    # Generate overview diagram
    print("Generating overview diagram...")
    overview_dot = generate_overview_dot(json_dir)
    overview_dot_path = diagrams_dir / "overview.dot"
    overview_dot_path.write_text(overview_dot, encoding="utf-8")
    render_dot_to_pdf(overview_dot_path, diagrams_dir / "overview.pdf")
    print(f"  Wrote {diagrams_dir / 'overview.pdf'}")

    # Generate air domain diagram
    print("Generating air domain diagram...")
    air_dot = generate_air_domain_dot(json_dir)
    air_dot_path = diagrams_dir / "air_domain.dot"
    air_dot_path.write_text(air_dot, encoding="utf-8")
    render_dot_to_pdf(air_dot_path, diagrams_dir / "air_domain.pdf")
    print(f"  Wrote {diagrams_dir / 'air_domain.pdf'}")

    # Generate ship domain diagram
    print("Generating ship domain diagram...")
    ship_dot = generate_ship_domain_dot(json_dir)
    ship_dot_path = diagrams_dir / "ship_domain.dot"
    ship_dot_path.write_text(ship_dot, encoding="utf-8")
    render_dot_to_pdf(ship_dot_path, diagrams_dir / "ship_domain.pdf")
    print(f"  Wrote {diagrams_dir / 'ship_domain.pdf'}")

    print("Done!")


if __name__ == "__main__":
    main()
