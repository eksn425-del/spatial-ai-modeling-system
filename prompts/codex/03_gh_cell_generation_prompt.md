# Codex Prompt: GH Cell Generation

You are generating a GH Python cell for a human-in-the-loop spatial modeling workflow.

## Task

Create a small GH Python component, not one large component controlling the whole city.

## Requirements

- Define input and output ports before writing geometry logic.
- Include `try/except`.
- Initialize all output variables.
- Include `warnings`.
- Include `summary` as JSON with `stage`, `status`, `geometry_counts`, `parameters`, and `warnings`.
- Include a panel-readable summary.
- Keep city massing separate from individual building facade generation.
- Do not connect `all_breps` directly to Preview as the only visual check.
- Each output must be separately previewable with Custom Preview.

## Debug rules

- If only height points appear and no massing breps appear, check output variables, generation functions, and data mapping.
- If output count mismatches occur, check GH output ports and Python variable names.
- If Preview/Bake is confusing, turn off Python component default Preview and preview each output separately.

## Output

Return:

- GH Python code
- Input/output notes
- Preview connection notes
- Expected summary JSON example

