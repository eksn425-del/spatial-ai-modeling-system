# Component Note

## Component Name

`...`

## Purpose

Describe the narrow responsibility of this GH Python cell.

## Inputs

- `input_name`: expected type and meaning

## Outputs

- `output_name`: expected type and preview behavior

## Preview Setup

- Connect each geometry output to its own Custom Preview.
- Keep a Panel connected to `summary`.
- Do not use `all_breps` as the only visual check.
- Turn off Python component default Preview if it conflicts with Custom Preview.

## Summary JSON

Expected fields:

- `stage`
- `status`
- `geometry_counts`
- `parameters`
- `warnings`

## Known Risks

- Output port mismatch
- Null summary
- Missing breps
- Preview/Bake confusion

## Human Validation

Describe what must be checked in Rhino/GH before this component is accepted.

