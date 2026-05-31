# Validation Metrics

## Purpose

These metrics help explain whether an Agent-assisted modeling output is usable. They also protect the project from overclaiming that AI can judge final design quality automatically.

## Data Validation Metrics

| Metric | Meaning |
| --- | --- |
| Parcel ID coverage | Whether all expected parcel IDs exist in the data |
| Height rule coverage | Whether each buildable parcel has a height rule |
| Boundary validity | Whether parcel/site boundaries have enough points |
| Coordinate consistency | Whether inputs use the same local coordinate system |
| Missing rule count | Number of parcels without usable rules |

## Geometry Validation Metrics

| Metric | Meaning |
| --- | --- |
| Parcel curve count | Should match valid parcel count |
| Massing brep count | Should match parcels allowed to generate massing |
| Height point count | Should match height-rule coverage |
| Warning count | Indicates missing or inconsistent data |
| Preview stability | Whether GH previews without empty or duplicated outputs |

## Workflow Validation Metrics

| Metric | Meaning |
| --- | --- |
| Step reproducibility | Whether another user can follow the documented workflow |
| Prompt traceability | Whether Agent prompts map to actual workflow steps |
| Human review coverage | Whether every major output has a manual check |
| Failure recovery | Whether the repo explains what to do when geometry fails |

## Portfolio Evidence Checklist

For a stronger visual release, collect:

- Rhino viewport before/after screenshot
- Grasshopper canvas screenshot
- Custom Preview screenshot
- summary Panel screenshot
- exported massing image
- one GIF showing parameter change or workflow run
- annotated board explaining input, Agent step, output, validation

## Interview Framing

The key claim is:

```text
I did not just ask AI to make a model. I designed validation metrics so AI-generated modeling steps could be checked by data coverage, geometry outputs, warnings, and human spatial review.
```
