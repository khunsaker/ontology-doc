#!/usr/bin/env python3

import argparse
import os
import subprocess
from pathlib import Path

from jinja2 import Template
from neo4j import GraphDatabase


def get_neo4j_config():
    """Get Neo4j connection config from environment."""
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD")
    database = os.getenv("NEO4J_DB", "Shark2")
    if not password:
        raise SystemExit("Missing required environment variable: NEO4J_PASSWORD")
    return {"uri": uri, "user": user, "password": password, "database": database}


def query_db_statistics(driver, database: str):
    """Query Neo4j for database statistics."""
    stats = {}
    with driver.session(database=database) as session:
        # Total nodes
        result = session.run("MATCH (n) RETURN count(n) AS cnt")
        stats["nodes"] = result.single()["cnt"]

        # Total relationships
        result = session.run("MATCH ()-[r]->() RETURN count(r) AS cnt")
        stats["relationships"] = result.single()["cnt"]

        # Total labels
        result = session.run("CALL db.labels() YIELD label RETURN count(label) AS cnt")
        stats["labels"] = result.single()["cnt"]

        # Total property keys
        result = session.run("CALL db.propertyKeys() YIELD propertyKey RETURN count(propertyKey) AS cnt")
        stats["properties"] = result.single()["cnt"]

    return stats


def render_title_template(template_path: Path, stats: dict) -> str:
    """Render the title page Jinja2 template with database stats."""
    template_content = template_path.read_text(encoding="utf-8")
    template = Template(template_content)
    # Format numbers with thousands separator
    formatted_stats = {k: f"{v:,}" for k, v in stats.items()}
    return template.render(stats=formatted_stats)


def read_levels_file(path: Path):
    levels = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        levels.append(s)
    return levels


def run(cmd, cwd=None):
    print("+ " + " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--levels-file", default="levels.txt",
                    help="File with one level label per line (default: levels.txt)")
    ap.add_argument("--levels", nargs="*", default=None,
                    help="Optional explicit list of level labels (overrides --levels-file)")

    ap.add_argument("--out-dir", default="cards", help="Where to write markdown cards (default: cards)")
    ap.add_argument("--json-dir", default="export/json", help="Where to write json exports (default: export/json)")
    ap.add_argument("--assembled-md", default="ontology_cards.md",
                    help="Assembled markdown output file (default: ontology_cards.md)")

    ap.add_argument("--build-pdf", action="store_true",
                    help="If set, run pandoc to build a PDF after assembly")
    ap.add_argument("--pdf-out", default="Shark2_Data_Model.pdf",
                    help="PDF output filename (default: Shark2_Data_Model.pdf)")

    args = ap.parse_args()

    root = Path(".").resolve()
    out_dir = root / args.out_dir
    json_dir = root / args.json_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    json_dir.mkdir(parents=True, exist_ok=True)

    if args.levels is not None and len(args.levels) > 0:
        levels = args.levels
    else:
        levels_path = root / args.levels_file
        if not levels_path.exists():
            raise SystemExit(
                f"levels file not found: {levels_path}\n"
                f"Create it (one label per line) or pass --levels Category Kind ..."
            )
        levels = read_levels_file(levels_path)

    if not levels:
        raise SystemExit("No levels provided. Add labels to levels.txt or pass --levels ...")

    assembled_path = root / args.assembled_md

    # Generate each level
    rendered_files = []
    for lvl in levels:
        json_path = json_dir / f"{lvl}.json"
        md_path = out_dir / f"{lvl}.md"

        # 1) Export JSON
        run(["python3", "export_level.py", "--level-label", lvl, "--out", str(json_path)], cwd=str(root))

        # 2) Render Markdown card
        run(["python3", "render_one.py", "--in", str(json_path), "--out", str(md_path)], cwd=str(root))

        rendered_files.append(md_path)

    # 3) Generate diagrams (requires JSON exports)
    diagrams_script = root / "generate_diagrams.py"
    if diagrams_script.exists():
        run(["python3", "generate_diagrams.py"], cwd=str(root))

    # 4) Query database statistics for title page
    cfg = get_neo4j_config()
    with GraphDatabase.driver(cfg["uri"], auth=(cfg["user"], cfg["password"])) as driver:
        db_stats = query_db_statistics(driver, cfg["database"])
    print(f"Database stats ({cfg['database']}): {db_stats}")

    # 5) Assemble
    title_template_path = root / "templates" / "title.md.j2"
    diagrams_path = root / "templates" / "diagrams.md"
    with assembled_path.open("w", encoding="utf-8") as out:
        # Prepend title page (rendered from Jinja2 template)
        if title_template_path.exists():
            rendered_title = render_title_template(title_template_path, db_stats)
            out.write(rendered_title.rstrip() + "\n\n")
        # Include diagrams section if it exists
        if diagrams_path.exists():
            out.write(diagrams_path.read_text(encoding="utf-8").rstrip() + "\n\n")
        for p in rendered_files:
            out.write(p.read_text(encoding="utf-8").rstrip() + "\n\n")

    print(f"Wrote {assembled_path}")

    # 6) Optional PDF build
    if args.build_pdf:
        run([
            "pandoc",
            str(assembled_path),
            "-o",
            args.pdf_out,
            "--pdf-engine=xelatex",
            "-V", "header-includes=\\usepackage{graphicx}"
        ], cwd=str(root))
        print(f"Wrote {root / args.pdf_out}")


if __name__ == "__main__":
    main()
