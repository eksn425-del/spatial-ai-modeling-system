# Master Skill

## Purpose

Orchestrate the full Spatial AI Modeling System from spatial intent to GitHub-ready workflow packaging. This skill keeps the system from becoming a one-off architecture experiment by enforcing data layers, rule layers, modular GH cells, validation, and documentation.

## When to Use

Use this skill when starting a new spatial AI modeling project, reorganizing a messy Rhino/GH workflow, or turning a modeling experiment into a reusable productized system.

## Inputs

- Project intent
- Site data or data description
- Parcel IDs
- Spatial rules
- Height or hierarchy rules
- Rhino/GH validation notes
- Screenshots or demo notes when available

## Outputs

- Project structure
- Workflow ledger
- Modular skill plan
- Product documentation
- Validation checklist
- GitHub packaging plan

## Procedure

1. Define the project as a spatial AI modeling workflow, not as a finished building design.
2. Separate data, rules, GH cells, generators, validation, prompts, and portfolio packaging.
3. Avoid one large GH component controlling the entire city. Split the workflow into small cells that can be previewed and debugged independently.
4. Separate city massing from individual building facade or skin generation.
5. Require every modeling cell to output a panel summary and a machine-readable summary JSON.
6. Require every geometry output to be previewable through its own Custom Preview.
7. Treat `all_breps` as a collection or bake candidate, not as the only Preview output.
8. Document failed attempts, recovery logic, and human decisions.

## Codex Role

Codex is responsible for data migration, rule organization, schema creation, validators, first-pass GH Python cells, documentation, checklists, and GitHub packaging.

Codex should not claim reliable judgment over complex Rhino/GH visual quality. If the model runs but looks wrong, the output still needs human validation.

## ChatGPT Role

ChatGPT is used for building style breakdowns, facade logic, GH connection reasoning, generator parameter design, visual debugging prompts, and portfolio storytelling.

Complex building skins, flowing tower logic, and style-specific facade systems should be handled with ChatGPT plus manual Rhino/GH validation.

## Human Validation

The human designer validates:

- Whether the spatial intent is represented correctly.
- Whether parcel groups and height rules are meaningful.
- Whether the Rhino/GH preview is visually coherent.
- Whether building facades, roofs, podiums, and skins are acceptable.
- Whether outputs should be baked, rejected, or iterated.

## Common Failures

- One oversized GH component becomes impossible to debug.
- City massing and building facade logic are mixed together.
- Panel summary is missing or `summary` is null.
- Only height points appear but no massing breps are generated.
- Output quantity does not match GH output ports.
- `all_breps` is connected directly to Preview and hides which part failed.
- Python component default Preview conflicts with Custom Preview.

## Recovery Strategy

- Split large components into site, parcel, rule, massing, generator, and validation cells.
- Check output variable names against GH output ports.
- Check generation functions and data mapping when height points exist but massing is missing.
- Add summary JSON with `status`, `geometry_counts`, `parameters`, and `warnings`.
- Turn off Python component default Preview when visual output becomes confusing.
- Preview roads, parcel curves, towers, podiums, facade lines, roofs, and warnings separately.

## Deliverables

- Productized workflow map
- Skill folder structure
- Schemas and templates
- Validators and checklists
- Prompt library
- Portfolio and GitHub packaging materials

