# Codex Prompt: Rule System Generation

You are generating a JSON rule system for the Spatial AI Modeling System.

## Task

Convert design intent and parcel IDs into:

- `spatial_rules.json`
- `height_rules.json`
- `building_groups.json`

## Requirements

- Keep city-scale rules separate from individual building facade rules.
- Include hierarchy, open space, mobility, and landscape rules.
- Include `max_height`, `min_height`, `allow_tower`, `allow_podium`, and `hierarchy_level`.
- Check duplicate parcel IDs across building groups.
- Output warnings for unclassified parcel IDs.

## Output

Return:

- JSON rule files
- Duplicate ID report
- Unclassified TODO list
- Human validation questions

