# ChatGPT Prompt: Building Style Breakdown

Help break down a building style into generator logic that can be tested in Rhino/Grasshopper.

## Inputs

- Target style or reference description:
- Building type:
- Height:
- Floor count:
- Width:
- Depth:
- Desired facade behavior:

## Please produce

- Main massing rules
- Core geometry
- Podium logic
- Facade line logic
- Roof logic
- Style parameters
- Outputs that should be previewed separately

## Constraints

- Do not merge city massing and individual building facade generation.
- Assume the first generator is a prototype, not a final architecture design.
- Include human validation checks for visual quality.

## Output format

Return:

- Generator strategy
- Parameter table
- GH output list
- Visual risks
- Rhino/GH validation checklist

