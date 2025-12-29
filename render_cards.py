import json
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

EXPORT_DIR = Path("export/json")
CARDS_DIR = Path("cards")
TEMPLATE_DIR = Path("templates")
TEMPLATE_NAME = "semantic_card.md.j2"

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def normalize_card(card: dict) -> dict:
    # Make output deterministic even if inputs vary slightly.
    card = dict(card)

    props = card.get("properties") or []
    # Ensure stable ordering by property name
    props = sorted(props, key=lambda p: (p.get("name", ""), p.get("type", "")))
    card["properties"] = props

    rel = card.get("relationships") or {}
    incoming = rel.get("incoming") or []
    outgoing = rel.get("outgoing") or []

    # Normalize label arrays and sort deterministically
    for r in incoming:
        r["source_labels"] = sorted(r.get("source_labels") or [])
    for r in outgoing:
        r["target_labels"] = sorted(r.get("target_labels") or [])

    incoming = sorted(incoming, key=lambda r: (r.get("type", ""), ",".join(r.get("source_labels") or [])))
    outgoing = sorted(outgoing, key=lambda r: (r.get("type", ""), ",".join(r.get("target_labels") or [])))

    card["relationships"] = {"incoming": incoming, "outgoing": outgoing}
    return card

def main():
    if not EXPORT_DIR.exists():
        raise SystemExit(f"Missing {EXPORT_DIR}. Run exports first.")

    CARDS_DIR.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)
    template = env.get_template(TEMPLATE_NAME)

    json_files = sorted(EXPORT_DIR.glob("*.json"))
    if not json_files:
        raise SystemExit(f"No JSON files found in {EXPORT_DIR}.")

    rendered = 0
    for jf in json_files:
        card = normalize_card(load_json(jf))

        label = card.get("label")
        if not label:
            print(f"Skipping {jf.name}: missing 'label'")
            continue

        md = template.render(**card).rstrip() + "\n"
        out_path = CARDS_DIR / f"{label}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")
        rendered += 1

    print(f"Rendered {rendered} card(s).")

if __name__ == "__main__":
    main()
