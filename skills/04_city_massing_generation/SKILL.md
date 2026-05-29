# City Massing Generation

## Purpose

Generate city-scale spatial massing from parcel data and rules while keeping building-level facade generation separate.

## When to Use

Use this skill after site data, parcel data, building groups, and height rules have been validated.

## Inputs

- Parcel boundaries
- Parcel centroids
- Building group classifications
- Height rules
- Open space rules
- Design hierarchy notes

## Outputs

- Tower envelope breps
- Podium envelope breps
- Open space curves or surfaces
- Road and parcel preview geometry
- Labels
- Summary JSON
- Warnings

## Procedure

1. Load parcels and height rules.
2. Match every height rule to a parcel ID.
3. Generate basic city massing envelopes only.
4. Keep facade, skin, roof articulation, and detailed tower style out of this cell.
5. Output towers, podiums, open spaces, labels, and warnings separately.
6. Add geometry counts for each output group.
7. Preview every group independently before combining.

## Codex Role

Codex can generate city-scale data handling, massing scaffolds, height-rule mapping, and summary JSON. Codex is strong at this layer because it is mostly structured data and repeatable geometry logic.

## ChatGPT Role

ChatGPT can help translate design hierarchy into more legible massing concepts, but the final visual judgment must happen in Rhino/GH.

## Human Validation

The human designer confirms whether the massing hierarchy, open space distribution, and height logic make spatial sense.

## Common Failures

- Attempting to generate all city buildings, facades, skins, and roofs in one component.
- Only height points appear because extrusion or brep generation did not run.
- Some parcels produce massing and others silently fail due to ID mismatch.
- The preview looks dense because every brep is merged into `all_breps`.

## Recovery Strategy

- Separate city massing from individual building generator work.
- Start with parcel curves and labels, then add podiums, then towers.
- If height points exist but no breps appear, check output variables, generation functions, and parcel-to-height data mapping.
- Use Custom Preview for towers, podiums, open spaces, and labels separately.
- Record failed parcel IDs in warnings.

## Deliverables

- City massing GH cell
- Height-rule mapping report
- Separate preview outputs
- Summary JSON
- Human validation note

