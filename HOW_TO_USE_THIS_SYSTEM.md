# How to Use This System

This guide describes the minimum executable workflow for a new spatial AI modeling project.

## Step 1: Prepare spatial data

Input:

- Site boundary
- Parcel IDs
- Parcel boundary points
- Roads
- Coordinate system notes

Output:

- Clean JSON files for site data and parcel data
- A short data preflight note

Codex role:

- Convert messy tables or notes into structured JSON.
- Check missing IDs, invalid boundaries, and inconsistent field names.

ChatGPT role:

- Help clarify spatial intent if the data implies several possible design directions.

Human validation:

- Confirm the site boundary, parcel IDs, and road logic match the actual design context.

## Step 2: Define rules

Input:

- Design intent
- Parcel types
- Height limits
- Open space goals
- Mobility and landscape logic

Output:

- `spatial_rules.json`
- `height_rules.json`
- `building_groups.json`

Codex role:

- Translate written rules into structured JSON.
- Keep field names consistent with schemas.

ChatGPT role:

- Help turn design concepts into clearer hierarchy, landscape, and mobility logic.

Human validation:

- Decide whether rules actually match the desired spatial strategy.

## Step 3: Generate GH cells

Input:

- Site data JSON
- Parcel JSON
- Spatial rules JSON
- Height rules JSON

Output:

- Small GH Python cell scripts
- Separate outputs for parcels, roads, massing, labels, warnings, and summary

Codex role:

- Generate first-pass GH Python cells.
- Keep inputs and outputs aligned with GH ports.
- Add try/except, geometry counts, warnings, and summary JSON.

ChatGPT role:

- Help explain how to connect component inputs and outputs inside Grasshopper.

Human validation:

- Confirm every output can be previewed separately with Custom Preview.

## Step 4: Preview in Rhino/GH

Input:

- GH Python cell
- Grasshopper input panels
- JSON strings or file paths

Output:

- Rhino/GH preview of boundaries, roads, parcel labels, and massing envelopes
- Panel summary

Codex role:

- Debug code-level errors and missing variables.

ChatGPT role:

- Suggest GH wiring structure and preview separation.

Human validation:

- Check visual correctness in Rhino.
- Do not rely only on `all_breps`.
- Turn off Python component default Preview when it causes confusion.

## Step 5: Debug geometry

Input:

- Error messages
- Null outputs
- Missing breps
- Mismatched counts
- Screenshots or user observations

Output:

- Updated GH cell or generator
- Debug notes
- Updated summary JSON

Codex role:

- Inspect output variable names, generation functions, data mapping, and exception paths.

ChatGPT role:

- Help reason about visual symptoms such as floating facade lines, abrupt roofs, or disconnected podiums.

Human validation:

- Re-preview each output separately and confirm the issue is actually resolved.

## Step 6: Generate individual building prototypes

Input:

- One parcel or one building anchor point
- Height, floor count, width, depth
- Style parameters
- Generator requirements

Output:

- Building generator script
- Glass core, facade lines, podium breps, roof breps, all_breps, and summary outputs

Codex role:

- Create safe generator scaffolds, validation helpers, and summary outputs.

ChatGPT role:

- Develop complex facade logic, style decomposition, and GH connection reasoning.

Human validation:

- Decide whether the building looks coherent from multiple views in Rhino/GH.

## Step 7: Validate and bake

Input:

- Previewed geometry
- Summary JSON
- Warnings
- Rhino/GH checklist

Output:

- Validated geometry
- Bake-ready outputs
- Notes about what was accepted or rejected

Codex role:

- Help produce validation scripts, checklists, and release notes.

ChatGPT role:

- Help turn visual debugging observations into next iteration prompts.

Human validation:

- Bake only outputs that are visually and structurally acceptable.

## Step 8: Package as GitHub project

Input:

- Stable workflow
- Templates
- Prompts
- Screenshots
- Demo notes

Output:

- GitHub-ready documentation
- Product README
- Portfolio summary
- Resume bullets

Codex role:

- Organize files, write docs, produce manifests, and keep the project explainable.

ChatGPT role:

- Help refine storytelling, case study framing, and application language.

Human validation:

- Add screenshots, demo images, and real Rhino/GH proof before publishing.

