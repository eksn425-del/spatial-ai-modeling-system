# Codex Prompt: Site Data Migration

You are helping build a Spatial AI Modeling System. Convert the provided site notes into clean JSON for a spatial modeling workflow.

## Context

This is not a traditional architecture portfolio backup. It is a human-in-the-loop workflow for space product prototyping and generative modeling.

## Task

Create or update:

- `site_data.json`
- `parcels.json`
- data preflight notes

## Requirements

- Preserve parcel IDs exactly.
- Include `site_id`, `site_boundary`, `roads`, `parcels`, `coordinate_system`, and `notes`.
- Each parcel should include `parcel_id`, `boundary_points`, `centroid`, `parcel_type`, and `notes`.
- Do not invent missing geometry silently. Add warnings or notes.
- Do not read or copy old project assets such as DWG, DXF, 3DM, GH, images, PDFs, or Word files.

## Output

Return:

- Updated JSON
- Missing fields
- Data warnings
- Suggested next validation step

