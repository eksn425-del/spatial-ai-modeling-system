# Site Data Preparation

## Purpose

Prepare spatial data so downstream rules, GH Python cells, and generators receive stable inputs instead of ambiguous notes or mixed-format tables.

## When to Use

Use this skill before generating any GH cell or massing model. It is especially important when site boundaries, roads, parcel IDs, and height rules come from different sources.

## Inputs

- Site boundary points
- Road centerlines or road descriptions
- Parcel IDs
- Parcel boundary points
- Parcel centroids
- Coordinate system notes
- Human notes about missing or uncertain data

## Outputs

- Validated site data JSON
- Validated parcel JSON
- Data preflight notes
- Warnings about missing IDs, missing centroids, or weak boundaries

## Procedure

1. Assign a stable `site_id`.
2. Store `site_boundary` as ordered points.
3. Store roads as named or typed path objects.
4. Store parcels as records with `parcel_id`, `boundary_points`, `centroid`, `parcel_type`, and `notes`.
5. Keep coordinate system notes visible even if the current prototype uses local coordinates.
6. Run validators before GH generation.
7. Do not infer missing geometry silently. Put uncertainty in `notes` or `warnings`.

## Codex Role

Codex can clean field names, normalize JSON, detect missing required fields, and create validators. Codex is well suited for data migration and structured preflight checks.

## ChatGPT Role

ChatGPT can help interpret vague site intent, naming logic, or how parcel categories should support design goals.

## Human Validation

The human designer confirms whether parcel IDs, boundaries, roads, and centroids match the intended site logic. Human review is required before GH cells are generated from the data.

## Common Failures

- Parcel ID spelling differs between data files and height rules.
- Boundary points are unordered.
- Road data exists as notes but not as structured records.
- Coordinate system assumptions are missing.
- A site looks correct in code but appears shifted or flipped in Rhino/GH.

## Recovery Strategy

- Compare parcel IDs across all JSON files.
- Add notes for every uncertain boundary or road.
- Test a minimal GH preview for only site boundary, roads, and parcel labels before adding massing.
- If output quantities do not match expected parcel counts, check data mapping before editing geometry logic.

## Deliverables

- `site_data.json`
- `parcels.json`
- Data preflight checklist
- Validator output
- Human-approved data note

