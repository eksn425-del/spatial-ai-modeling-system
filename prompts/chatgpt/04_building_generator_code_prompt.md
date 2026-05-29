# ChatGPT Prompt: Building Generator Code

Help me write or revise a GH Python building generator.

## Inputs

- `pt`
- `height`
- `floor_count`
- `width`
- `depth`
- `style_parameters`

## Required outputs

- `glass_core`
- `facade_lines`
- `podium_breps`
- `roof_breps`
- `all_breps`
- `warnings`
- `summary`

## Requirements

- Include try/except.
- Include summary JSON.
- Include geometry counts.
- Keep each geometry output separate.
- Do not rely on `all_breps` as the only preview.
- Add warnings for invalid parameters.

## Debug cases to handle

- Facade lines floating away from the core.
- Roof and podium looking abrupt.
- Output variables not matching GH ports.
- Code runs but visual quality is weak.

## Output format

Return GH Python code plus a short GH connection note.

