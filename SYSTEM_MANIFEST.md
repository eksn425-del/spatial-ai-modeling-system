# System Manifest

## System purpose

Spatial AI Modeling System organizes AI-assisted spatial modeling into clear layers. Each layer has its own responsibility, inputs, outputs, validation method, and failure mode.

## Data Layer

The Data Layer stores normalized site information.

Typical content:

- Site boundary
- Roads
- Parcel IDs
- Parcel boundaries
- Centroids
- Coordinate system notes

Primary files:

- `schemas/site_data.schema.json`
- `schemas/parcel.schema.json`
- `examples/minimal_site_project/data/parcels.sample.json`

## Rule Layer

The Rule Layer translates design intent into structured JSON.

Typical content:

- Hierarchy rules
- Height limits
- Tower and podium permission
- Open space rules
- Mobility rules
- Landscape rules
- Building group classifications

Primary files:

- `schemas/spatial_rules.schema.json`
- `schemas/height_rules.schema.json`
- `schemas/building_groups.schema.json`

## GH Cell Layer

The GH Cell Layer defines modular Grasshopper Python components. Each component should have narrow responsibility, clear inputs, clear outputs, warning messages, and summary JSON.

Rules:

- Do not control the entire city with one large GH component.
- Do not connect `all_breps` directly to Preview as the only visual output.
- Every output should be able to use Custom Preview separately.
- Every component should output a panel-readable summary.

Primary files:

- `templates/ghpython_cell_template.py`
- `schemas/gh_cell_io.schema.json`

## Generator Layer

The Generator Layer focuses on reusable geometry generators. City massing and individual building generators are separated.

Rules:

- City massing handles parcels, groups, height rules, and envelope-level geometry.
- Building generators handle one prototype or one building family at a time.
- Complex facade systems need ChatGPT-assisted logic and human visual validation.

Primary files:

- `templates/building_generator_template.py`
- `schemas/building_generator.schema.json`
- `examples/single_tower_generator/generator.py`

## Validation Layer

The Validation Layer checks data integrity, geometry counts, output consistency, and Rhino/GH preview behavior.

Typical checks:

- Missing parcel IDs
- Invalid boundaries
- Height rule mismatch
- Duplicate group IDs
- Output count mismatch
- Null summary output
- Preview/Bake confusion

Primary files:

- `validators/`
- `checklists/`

## AI Collaboration Layer

The AI Collaboration Layer defines which AI system should handle which task.

Codex is suitable for:

- Data migration
- Rule organization
- Validation scripts
- First-pass GH Python cells
- Documentation
- GitHub packaging

ChatGPT is suitable for:

- Building style breakdown
- GH wiring explanation
- Building generator logic
- Visual debugging prompts
- Portfolio storytelling

Human validation is required for:

- Visual quality
- Facade coherence
- Rhino/GH preview checks
- Bake decisions
- Final design acceptance

## Portfolio Layer

The Portfolio Layer explains the system as an AI-assisted spatial modeling workflow. It avoids claiming that AI automatically designs buildings.

Primary files:

- `portfolio_summary/project_one_page.md`
- `portfolio_summary/resume_bullets.md`
- `portfolio_summary/application_statement.md`

