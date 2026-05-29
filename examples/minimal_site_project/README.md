# Minimal Site Project

This fictional sample demonstrates the smallest data-to-GH-cell workflow in the Spatial AI Modeling System.

## Files

- `data/site_data.sample.json`: fictional site boundary, roads, parcel references, and coordinate notes.
- `data/parcels.sample.json`: five fictional parcels: B-01, B-02, D-01, D-02, F-01.
- `data/spatial_rules.sample.json`: minimal design intent, rule categories, and embedded building groups.
- `data/height_rules.sample.json`: height and tower/podium permissions.
- `gh_cells/example_gh_cell.py`: GH Python example that outputs parcel curves, height points, massing breps, warnings, and summary JSON.

## Grasshopper use

1. Add a Python component.
2. Add inputs named `parcels_json` and `height_rules_json`.
3. Add outputs named `parcel_curves`, `height_points`, `massing_breps`, `warnings`, and `summary`.
4. Paste the Python code from `gh_cells/example_gh_cell.py`.
5. Connect panels containing the JSON sample content.
6. Connect each geometry output to its own Custom Preview.
7. Connect `summary` to a Panel.

## Validation notes

- If height points appear but no massing breps appear, check height rules, generation functions, and output variables.
- If output counts are wrong, check GH output ports and Python variable names.
- If Preview/Bake looks confusing, turn off Python component default Preview.
