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

    lines = [
        'digraph overview {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica"];',
        '    edge [fontname="Helvetica", fontsize=10];',
        '',
        '    // Hub level',
        '    subgraph cluster_hub {',
        '        label="Hub";',
        '        style=dashed;',
        '        bgcolor="#f0f8ff";',
    ]

    # Add hub node
    hub_name = hub["card"]["node_names"][0]
    lines.append(f'        {sanitize_id(hub_name)} [label="{hub_name}", fillcolor="#4a90d9", fontcolor=white];')
    lines.append('    }')
    lines.append('')

    # Category level
    lines.append('    // Category level')
    lines.append('    subgraph cluster_category {')
    lines.append('        label="Category";')
    lines.append('        style=dashed;')
    lines.append('        bgcolor="#f0fff0";')

    categories = category["card"]["node_names"]
    for cat in categories:
        lines.append(f'        {sanitize_id(cat)} [label="{cat}", fillcolor="#5cb85c", fontcolor=white];')
    lines.append('    }')
    lines.append('')

    # Hub → Category edges
    for rel in hub["card"]["relationships"]["outgoing"]:
        from_id = sanitize_id(rel["from_name"])
        to_id = sanitize_id(rel["to_name"])
        lines.append(f'    {from_id} -> {to_id};')
    lines.append('')

    # Kind level - group by parent
    lines.append('    // Kind level')
    lines.append('    subgraph cluster_kind {')
    lines.append('        label="Kind";')
    lines.append('        style=dashed;')
    lines.append('        bgcolor="#fffaf0";')

    for group in kind["card"]["parent_groups"]:
        parent = group["parent"]
        # Only show Aircraft and Ship kinds for clarity
        if parent in ["Aircraft", "Ship"]:
            for node in group["nodes"]:
                lines.append(f'        {sanitize_id(node)} [label="{node}", fillcolor="#f0ad4e", fontcolor=white];')
    lines.append('    }')
    lines.append('')

    # Category → Kind edges (only Aircraft and Ship)
    for rel in category["card"]["relationships"]["outgoing"]:
        if rel["from_name"] in ["Aircraft", "Ship"]:
            from_id = sanitize_id(rel["from_name"])
            to_id = sanitize_id(rel["to_name"])
            lines.append(f'    {from_id} -> {to_id};')

    lines.append('}')
    return '\n'.join(lines)


def generate_air_domain_dot(json_dir: Path) -> str:
    """Generate DOT for Air domain hierarchy."""

    # Define the air hierarchy levels
    air_levels = ["AirType", "AirSubType", "AirVariant", "AirSubVariant",
                  "AirModel", "AirSubModel", "AirInstance"]

    colors = ["#4a90d9", "#5cb85c", "#f0ad4e", "#d9534f", "#9b59b6", "#3498db", "#1abc9c"]

    lines = [
        'digraph air_domain {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontcolor=white];',
        '    edge [fontname="Helvetica"];',
        '',
        '    // Air Domain Hierarchy',
        '    label="Air Domain Hierarchy";',
        '    labelloc=t;',
        '    fontsize=16;',
        '    fontname="Helvetica Bold";',
        '',
    ]

    # Add nodes for each level with counts
    prev_level = None
    for i, level in enumerate(air_levels):
        json_path = json_dir / f"{level}.json"
        if json_path.exists():
            data = load_json(json_path)
            count = data["card"]["total_nodes"]
            label = f"{level}\\n({count} nodes)"
            lines.append(f'    {level} [label="{label}", fillcolor="{colors[i % len(colors)]}"];')

            if prev_level:
                lines.append(f'    {prev_level} -> {level};')
            prev_level = level

    lines.append('}')
    return '\n'.join(lines)


def generate_ship_domain_dot(json_dir: Path) -> str:
    """Generate DOT for Ship domain hierarchy."""

    # Define the ship hierarchy levels
    ship_levels = ["ShipType", "ShipSubType", "ShipClass", "ShipSubClass", "ShipInstance"]

    colors = ["#2c3e50", "#34495e", "#7f8c8d", "#95a5a6", "#bdc3c7"]

    lines = [
        'digraph ship_domain {',
        '    rankdir=TB;',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontcolor=white];',
        '    edge [fontname="Helvetica"];',
        '',
        '    // Ship Domain Hierarchy',
        '    label="Ship Domain Hierarchy";',
        '    labelloc=t;',
        '    fontsize=16;',
        '    fontname="Helvetica Bold";',
        '',
    ]

    # Add nodes for each level with counts
    prev_level = None
    for i, level in enumerate(ship_levels):
        json_path = json_dir / f"{level}.json"
        if json_path.exists():
            data = load_json(json_path)
            count = data["card"]["total_nodes"]
            label = f"{level}\\n({count} nodes)"
            lines.append(f'    {level} [label="{label}", fillcolor="{colors[i % len(colors)]}"];')

            if prev_level:
                lines.append(f'    {prev_level} -> {level};')
            prev_level = level

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
