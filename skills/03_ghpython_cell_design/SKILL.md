# GH Python Cell Design

## Purpose

Design reliable GH Python cells that are small, inspectable, and easy to debug in Grasshopper.

## When to Use

Use this skill whenever creating or revising a Grasshopper Python component for site data, parcel previews, massing, labels, validation, or generator output.

## Inputs

- JSON strings or file paths
- GH input parameters
- RhinoCommon geometry requirements
- Expected output port names
- Validation requirements

## Outputs

- GH Python cell script
- Separate geometry outputs
- `summary` JSON string
- `warnings`
- Panel-readable status text

## Procedure

1. Define inputs and outputs before writing geometry logic.
2. Keep one cell responsible for one narrow task.
3. Do not build one large GH component that controls the whole city.
4. Use `try/except` to keep failures visible in `summary` and `warnings`.
5. Count generated geometry by output type.
6. Output summary JSON every time, even on failure.
7. Keep output variable names exactly aligned with GH output ports.
8. Make each output previewable separately through Custom Preview.
9. Avoid connecting `all_breps` directly to Preview as the only visual check.

## Codex Role

Codex is useful for first-pass GH Python code, JSON parsing, output naming, warning structures, and documentation comments.

Codex should not be trusted to judge whether the Rhino viewport result is visually successful.

## ChatGPT Role

ChatGPT can help describe GH wiring, explain how outputs should connect to Custom Preview, and reason about generator logic when components become style-specific.

## Human Validation

The human designer checks the component in Grasshopper, confirms each output port has the expected type and count, and previews each output separately.

## Common Failures

- `summary` is null because the exception path did not assign it.
- GH output count does not match Python variable names.
- Only height points are generated because the massing function is not called or breps are never appended.
- `all_breps` hides which output failed.
- Default Python Preview creates duplicate or confusing visual output.

## Recovery Strategy

- Initialize every output variable at the top of the script.
- Compare GH output ports with final Python variable names.
- Add `geometry_counts` to summary JSON.
- When only height points appear, inspect output variables, generation functions, and data mapping.
- Turn off Python component default Preview and preview each output with Custom Preview.

## Deliverables

- GH Python cell script
- Input/output table
- Summary JSON pattern
- Preview connection note
- Debug checklist

