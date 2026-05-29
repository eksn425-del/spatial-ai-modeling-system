# ChatGPT Prompt: Visual Debugging

Help diagnose a Rhino/Grasshopper visual failure from human observations.

## Observed issue

Describe what appears in the Rhino viewport:

- Missing breps:
- Only height points:
- Floating facade:
- Abrupt roof or podium:
- Preview/Bake confusion:
- Output mismatch:

## Component context

- Input parameters:
- Output ports:
- Summary JSON:
- Warnings:

## Please diagnose

- Most likely code cause
- Most likely GH wiring cause
- Most likely parameter cause
- What to preview separately
- What to ask Codex to patch

## Constraints

- Do not claim the model is correct without human viewport validation.
- Keep city massing and single building generator debugging separate.

## Output format

Return:

- Diagnosis
- Immediate GH checks
- Code patch request
- Human validation step

