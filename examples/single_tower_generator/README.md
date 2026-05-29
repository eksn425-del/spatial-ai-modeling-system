# Single Tower Generator

This fictional example demonstrates the expected input and output structure for an individual building generator.

It is not a finished architecture proposal. Use it as a scaffold for testing GH output ports, Custom Preview routing, summary JSON, and visual validation.

## Required inputs

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

## Preview setup

Preview `glass_core`, `facade_lines`, `podium_breps`, and `roof_breps` separately. Do not rely on `all_breps` alone. Keep `summary` connected to a Panel.

## Human validation

Check whether the core, facade lines, podium, and roof appear connected and visually coherent in Rhino/GH before reusing this generator on multiple parcels.

