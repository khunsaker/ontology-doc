#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path


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
    ap.add_argument("--pdf-out", default="ontology_cards.pdf",
                    help="PDF output filename (default: ontology_cards.pdf)")

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

    # 3) Assemble
    title_path = root / "templates" / "title.md"
    with assembled_path.open("w", encoding="utf-8") as out:
        # Prepend title page if it exists
        if title_path.exists():
            out.write(title_path.read_text(encoding="utf-8").rstrip() + "\n\n")
        for p in rendered_files:
            out.write(p.read_text(encoding="utf-8").rstrip() + "\n\n")

    print(f"Wrote {assembled_path}")

    # 4) Optional PDF build
    if args.build_pdf:
        run([
            "pandoc",
            str(assembled_path),
            "-o",
            args.pdf_out,
            "--pdf-engine=xelatex"
        ], cwd=str(root))
        print(f"Wrote {root / args.pdf_out}")


if __name__ == "__main__":
    main()
