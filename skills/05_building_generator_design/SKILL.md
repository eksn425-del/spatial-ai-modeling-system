# Building Generator Design

## Purpose

Design individual building generator patterns that are separate from city-scale massing and can be iterated visually in Rhino/GH.

## When to Use

Use this skill when creating a single tower, podium, facade, roof, or building-family generator.

## Inputs

- Anchor point `pt`
- Height
- Floor count
- Width
- Depth
- Style parameters
- Parcel or massing envelope reference
- Human visual goals

## Outputs

- `glass_core`
- `facade_lines`
- `podium_breps`
- `roof_breps`
- `all_breps`
- `summary`
- Warnings

## Procedure

1. Start from one building prototype, not the whole city.
2. Define base dimensions and floors.
3. Generate core mass first.
4. Add podium, facade lines, skin curves, and roof as separate outputs.
5. Keep `all_breps` as a convenience collection only.
6. Preview each output separately.
7. Use summary JSON to record parameters, geometry counts, and warnings.
8. Iterate visually in Rhino/GH before reusing the generator on many parcels.

## Codex Role

Codex can create generator scaffolds, parameter validation, simple geometry patterns, and summary outputs.

Codex is not reliable for judging complex Rhino/GH visual results, especially flowing skins, Zaha-like surfaces, or tower facade coherence.

## ChatGPT Role

ChatGPT helps break down building styles, facade rhythms, GH input/output logic, and generator code strategy. Complex architectural skins need ChatGPT-assisted reasoning plus human validation.

## Human Validation

The human designer checks whether the building reads correctly from multiple Rhino views, whether facade lines attach to the mass, and whether podium and roof transitions are believable.

## Common Failures

- Facade lines float away from the core.
- Roof and podium look abrupt or unrelated.
- Skin logic produces visual noise even when no code error appears.
- `all_breps` is previewed without checking the individual outputs.
- Output counts do not match GH ports.

## Recovery Strategy

- Preview `glass_core`, `facade_lines`, `podium_breps`, and `roof_breps` separately.
- Use simple geometry before adding style effects.
- Check output variable names against GH output ports.
- Add warnings when style parameters are out of range.
- Turn off Python component default Preview when using Custom Preview materials.

## Deliverables

- Building generator script
- Parameter sample JSON
- Output preview guide
- Summary JSON
- Human visual validation note

