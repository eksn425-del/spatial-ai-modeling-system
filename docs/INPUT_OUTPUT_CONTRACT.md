# Input / Output Contract

## Purpose

This contract explains what the system expects as input, what it can produce as output, and where human validation is required.

## Input Types

| Input | Format | Role |
| --- | --- | --- |
| Site boundary | JSON points / Rhino curve | Defines modeling area |
| Roads | JSON polylines | Supports access and spatial hierarchy |
| Parcels | JSON records | Defines buildable units |
| Height rules | JSON records | Controls massing limits |
| Spatial rules | JSON records | Captures design intent and constraints |
| Building groups | JSON records | Organizes tower, podium, open space, and special zones |
| Human notes | Markdown / prompt text | Captures judgment that cannot be automated |

## Agent Processing

The Agent can help with:

- converting design notes into JSON structures
- checking schema consistency
- generating GH Python cell drafts
- writing validators
- producing summary JSON templates
- creating documentation and case-study materials

The Agent should not be trusted alone for:

- final geometry quality
- exact design correctness
- facade visual quality
- planning-law compliance
- final portfolio rendering selection

## Output Types

| Output | Format | Use |
| --- | --- | --- |
| Parcel curves | Rhino geometry | Preview parcel mapping |
| Height points | Rhino geometry | Check rule-to-geometry mapping |
| Massing breps | Rhino geometry | Preview city massing |
| Warning list | Text / panel | Flag missing or inconsistent inputs |
| Summary JSON | JSON | Record counts, parameters, status, and warnings |
| Validation report | Markdown / JSON | Explain whether the output is usable |
| Case study | Markdown | Package the workflow for GitHub and portfolio review |

## Minimum Valid Output

Every GH Python cell should produce:

- separate geometry outputs
- a `warnings` output
- a `summary` output
- stable behavior when input is missing
- clear failure notes instead of silent errors

## Human Acceptance Criteria

An output is considered usable only after the designer checks:

- parcel count matches expected count
- height rules are applied to the correct IDs
- building groups map to correct zones
- open spaces remain unbuilt
- preview colors and bake states are readable
- geometry is not duplicated, missing, or wildly scaled
- the result supports the intended design story

## Product Interpretation

This system is a workflow product. Its value is not only the geometry output, but the traceable chain from input rules to generated cells, validation reports, and human acceptance.
