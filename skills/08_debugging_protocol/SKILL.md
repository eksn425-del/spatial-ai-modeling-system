# Debugging Protocol

## Purpose

Provide a structured recovery process for AI-generated GH Python cells and building generators when geometry output is missing, unstable, or visually wrong.

## When to Use

Use this skill whenever Grasshopper output is null, counts are wrong, preview is confusing, or geometry appears but fails visually.

## Inputs

- Error messages
- GH output names
- Python output variables
- Summary JSON
- Warnings
- Human viewport observations

## Outputs

- Debug diagnosis
- Patch plan
- Updated component
- Validation notes
- Next prompt for Codex or ChatGPT

## Procedure

1. Check whether the component produced a panel summary.
2. Check whether `summary` is valid JSON or null.
3. Check whether every GH output port has a matching Python variable.
4. Check whether geometry generation functions are actually called.
5. Check whether generated geometry is appended to the correct output list.
6. Check data mapping from parcel ID to rule, height, or generator parameter.
7. Preview each output separately.
8. Turn off Python component default Preview when Custom Preview is used.
9. Document the failure and recovery in the workflow ledger.

## Codex Role

Codex can patch output variables, exception handling, data mapping, validators, and summary JSON. It can also create a narrower repro cell.

## ChatGPT Role

ChatGPT can reason about visual symptoms and generator logic, especially for facade systems, tower skins, roof transitions, and podium massing.

## Human Validation

The human designer confirms the fix in Rhino/GH and decides whether the result is good enough to keep.

## Common Failures

- Only height points appear but no massing.
- Output count mismatch between GH ports and Python variables.
- Summary panel shows null.
- Preview/Bake confusion hides duplicate geometry.
- Facade skin floats or does not attach to the core.
- Building generator produces roof and podium elements that look abrupt.

## Recovery Strategy

- For height points without massing: inspect output variables, generation functions, and data mapping.
- For output mismatch: compare GH ports and Python variables exactly.
- For summary null: initialize `summary` and assign it in success and failure branches.
- For Preview/Bake confusion: disable default Preview and use one Custom Preview per output.
- For visual facade failure: simplify geometry, isolate one facade rule, and use ChatGPT plus human validation.

## Deliverables

- Debug report
- Updated script
- Summary JSON sample
- Validation note
- Follow-up prompt

