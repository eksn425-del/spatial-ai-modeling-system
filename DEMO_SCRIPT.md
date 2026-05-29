# Demo Script

60-second demo video script for GitHub v0.1.

## 0-10s: System README and workflow map

Visual:

- Show `README.md` title: `Spatial AI Modeling System`.
- Show the subtitle.
- Scroll briefly to the human-in-the-loop principle.
- Show `WORKFLOW_MAP.md` Mermaid diagram.

Voiceover:

"This is the Spatial AI Modeling System, a human-in-the-loop workflow for space product prototyping and generative modeling. It is not a fully autonomous architecture generator. It turns spatial intent, data, rules, GH Python cells, validation, and portfolio packaging into a reusable system."

Materials needed:

- README screen capture
- Workflow map screen capture

## 10-20s: Sample data and schema

Visual:

- Open `examples/minimal_site_project/data/parcels.sample.json`.
- Show parcel IDs: `B-01`, `B-02`, `D-01`, `D-02`, `F-01`.
- Open `schemas/parcel.schema.json` or `schemas/height_rules.schema.json`.

Voiceover:

"The workflow starts from clean sample data. Parcels, boundaries, centroids, spatial rules, and height rules are described in JSON so the modeling process can be checked before geometry is generated."

Materials needed:

- Sample JSON screen capture
- Schema screen capture

## 20-35s: GH Python cell template and summary JSON

Visual:

- Open `examples/minimal_site_project/gh_cells/example_gh_cell.py`.
- Highlight input/output names.
- Show `templates/ghpython_cell_template.py`.
- Show a summary JSON example with `status`, `geometry_counts`, `parameters`, and `warnings`.

Voiceover:

"Each GH Python cell is small and inspectable. It has clear inputs, separate outputs, warnings, and a summary JSON panel. This makes debugging easier when geometry is missing or output counts do not match."

Materials needed:

- GH Python code capture
- Summary JSON capture

## 35-50s: Rhino/GH preview screenshot placeholder

Visual:

- Show placeholder images or slides for:
  - Grasshopper Python component wiring
  - separate Custom Preview outputs
  - Rhino viewport preview
  - summary Panel

Voiceover:

"The key step happens in Rhino and Grasshopper. Each output should be previewed separately with Custom Preview, and the designer validates whether the geometry is correct before baking or documenting the result."

Materials needed:

- Grasshopper wiring screenshot
- Rhino viewport screenshot
- Custom Preview output screenshot
- Summary Panel screenshot

## 50-60s: Building generator and GitHub packaging

Visual:

- Open `examples/single_tower_generator/generator.py`.
- Show outputs: `glass_core`, `facade_lines`, `podium_breps`, `roof_breps`, `all_breps`, `summary`.
- Show `portfolio_summary/resume_bullets.md`.
- End on GitHub repository view.

Voiceover:

"The system also includes building generator patterns, prompt workflows, validators, and portfolio packaging. The result is not just a model, but a reusable AI-assisted spatial modeling workflow that can be shared on GitHub."

Materials needed:

- Building generator code capture
- Portfolio summary capture
- GitHub repo screen capture

