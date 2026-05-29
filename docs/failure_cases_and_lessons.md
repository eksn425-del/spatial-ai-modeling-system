# Failure Cases and Lessons

This document records real workflow lessons that shaped the Spatial AI Modeling System.

## One-shot full city generation failed

Trying to generate all city buildings, facade systems, roofs, and visual logic in one step made the GH output unstable and hard to debug.

Lesson: split the workflow into data, rules, city massing, building generators, and validation.

## Only height points appeared, no massing

The viewport showed height points but no building volumes.

Likely causes:

- Brep generation function was not called.
- Breps were created but not appended to the output list.
- Parcel-to-height data mapping failed.
- Output variable did not match the GH port name.

Lesson: inspect output variables, generation functions, and data mapping before assuming the geometry algorithm is wrong.

## A2 summary null

A summary panel showed null, which made debugging harder.

Likely causes:

- `summary` was not initialized.
- Exception path did not assign summary.
- Output port name did not match the Python variable.

Lesson: every GH cell must produce summary JSON in both success and failure states.

## Output quantity mismatch

The number of generated items did not match expected parcels or floors.

Likely causes:

- GH output ports and Python variables were inconsistent.
- A filtered parcel list removed items silently.
- A loop skipped failed IDs without warning.

Lesson: use `geometry_counts` and warnings for skipped IDs.

## Building facade floated away

Facade curves or skin elements appeared detached from the tower core.

Likely causes:

- Wrong base point.
- Z values did not match floor heights.
- Offset direction or local plane was wrong.

Lesson: preview core, facade lines, podium, and roof separately before combining.

## Roof and podium felt abrupt

The generator created roof and base elements, but they did not look connected to the mass.

Lesson: building generators need style logic, not only geometry output. Use ChatGPT for style breakdown and human validation for visual coherence.

## Preview / Bake confusion

Geometry appeared duplicated or unclear in the viewport.

Likely causes:

- Python component default Preview was still on.
- Multiple outputs were merged into one preview material.
- `all_breps` hid which geometry category failed.

Lesson: turn off Python component default Preview and route each output to its own Custom Preview.

