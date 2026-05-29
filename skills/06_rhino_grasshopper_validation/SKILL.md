# Rhino Grasshopper Validation

## Purpose

Validate AI-generated GH Python components and building generators inside Rhino/GH before considering them successful.

## When to Use

Use this skill after every GH cell or generator update, especially when the code runs but the viewport result is unclear.

## Inputs

- GH component outputs
- Rhino viewport observation
- Panel summary
- Summary JSON
- Warnings
- Screenshots when available

## Outputs

- Validation status
- Preview notes
- Bake readiness decision
- Debug tasks
- Human acceptance or rejection note

## Procedure

1. Confirm the Python component has a panel summary.
2. Confirm summary JSON is not null.
3. Check output counts in `geometry_counts`.
4. Preview each output separately with Custom Preview.
5. Turn off Python component default Preview if duplicate previews create confusion.
6. Do not judge success only by `all_breps`.
7. Check missing breps, floating facade lines, abrupt roofs, and mismatched heights.
8. Bake only validated outputs.

## Codex Role

Codex can interpret warnings, patch code, add summary fields, and explain likely causes of missing output. Codex cannot reliably decide whether a complex Rhino/GH visual result is architecturally convincing.

## ChatGPT Role

ChatGPT can help interpret visual debugging descriptions and propose generator-level changes, especially for complex building skin and facade logic.

## Human Validation

The human designer is the final judge of viewport quality, geometry acceptance, preview material setup, and bake decisions.

## Common Failures

- A2 or another summary panel is null.
- Preview shows height points but no building mass.
- Preview/Bake is confusing because default Preview and Custom Preview overlap.
- Output counts differ from expected parcel or floor counts.
- Facade or roof pieces are generated but visually disconnected.

## Recovery Strategy

- Check whether `summary` is assigned in both success and exception paths.
- Check output variables, generation functions, and data mapping when only height points appear.
- Compare GH output ports with Python variable names.
- Disable default Preview on the Python component.
- Route every major output to a separate Custom Preview with distinct material.

## Deliverables

- Validation checklist result
- Screenshot notes or viewport notes
- Accepted outputs list
- Rejected outputs list
- Next debug prompt

