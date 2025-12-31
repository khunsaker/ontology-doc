# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python pipeline for generating data model documentation from a Neo4j graph database (Shark2 Knowledge Base). Exports hierarchical data cards for entities like Aircraft, Ships, Organizations, Weapons, and Places as Markdown and PDF, with auto-generated Graphviz diagrams showing the data model structure.

## Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Full pipeline (export + render all levels + assemble)
python3 render_all.py

# Full pipeline with PDF generation
python3 render_all.py --build-pdf

# Export single level to JSON
python3 export_level.py --level-label Category --out export/json/Category.json

# Render JSON to Markdown
python3 render_one.py --in export/json/Category.json --out cards/Category.md
```

## Architecture

**Pipeline flow:** `export_level.py` → `render_one.py` → `generate_diagrams.py` → `render_all.py`

1. **export_level.py**: Queries Neo4j for data model level, normalizes relationships, outputs JSON
2. **render_one.py**: Converts JSON to Markdown using Jinja2 templates
3. **generate_diagrams.py**: Creates Graphviz diagrams from JSON exports (overview, air domain, ship domain)
4. **render_all.py**: Orchestrates full pipeline, queries DB stats, assembles final output with diagrams

**Key files:**
- `levels.txt` - Ordered list of data model levels to export (Hub, Category, Kind, Family, AirType→AirInstance, ShipType→ShipInstance)
- `templates/semantic_card.md.j2` - Jinja2 template controlling card appearance
- `templates/title.md.j2` - Title page template with dynamic database statistics
- `templates/diagrams.md` - LaTeX template embedding generated diagram PDFs
- `.env` - Neo4j credentials (required for database connection)

**Generated diagrams** (in `diagrams/`):
- `overview.pdf` - High-level structure: Hub → Category → Kind → Family
- `air_domain.pdf` - Aircraft hierarchy: AirType → AirInstance chain
- `ship_domain.pdf` - Ship hierarchy: ShipType → ShipInstance chain

## Key Concepts

**Two rendering modes:**
- **Named levels** (Hub, Category, Kind, Family): Display individual node names and relationships
- **Deep levels** (Type→Instance hierarchies): Collapse to representative labels with relationship counts

**Relationship aggregation** (`build_outgoing_generalized()`):
- Collapses detailed relationships into generalized patterns
- Priority-based label selection prefers domain-specific labels (AirInstance > AirModel > AirType)
- Falls back to general labels (Hub > Category > Kind > Family)

**Label canonicalization** (`pick_level_display()`):
- Filters noise labels: Object, Person, SharkNode, _Bloom_Perspective_
- Maps to canonical display names via `CANONICAL_DISPLAY` dict

## Configuration Constants

In `export_level.py`:
- `LEVEL_ORDER` - Hierarchy depth ordering
- `CANONICAL_DISPLAY` - Label name mappings
- `GENERALIZE_RELS_LEVELS` - Levels using aggregated relationship display
- `REL_TARGET_OVERRIDES` - Special relationship target mappings

In `render_one.py`:
- `NAMED_LEVELS` - Levels that display node names (vs collapsed labels)
- `NEVER_COLLAPSE_TO` - Labels to avoid when collapsing

## Dependencies

- `neo4j` - Graph database driver
- `jinja2` - Template engine
- `graphviz` - Diagram generation (`sudo apt install graphviz`)
- `pandoc` + `xelatex` - PDF generation

## Notes

- Generated files (`cards/`, `export/json/`, `diagrams/`, `*.md`, `*.pdf`) are git-ignored
- Requires active Neo4j connection with Shark2 database for exports
- Default PDF output: `Shark2_Data_Model.pdf`
- Title page displays live database statistics (nodes, relationships, labels, properties)
- Diagrams are dynamically generated from JSON exports using Graphviz DOT format
- Modify `templates/semantic_card.md.j2` to change documentation card formatting
- Modify `templates/title.md.j2` to change title page layout or statistics
- Modify `generate_diagrams.py` to change diagram structure or styling
