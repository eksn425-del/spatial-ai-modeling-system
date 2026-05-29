# Grasshopper Cell Hierarchy

Large GH Python components are difficult to debug because data loading, rule mapping, massing, facade generation, preview, and summary logic become tangled.

## Recommended hierarchy

1. Data loader cell
2. Parcel preview cell
3. Rule mapping cell
4. City massing cell
5. Building generator cell
6. Validation summary cell
7. Export or bake preparation cell

## Rules

- Do not use one large GH component to control an entire city.
- Keep city massing separate from individual building facade generation.
- Keep `summary` output in every major cell.
- Output JSON summaries so the workflow can be inspected outside Rhino/GH.
- Keep geometry outputs separate for Custom Preview.
- Do not connect `all_breps` directly to Preview as the only inspection method.

## Debug advantage

When a component fails, small cells make it easier to answer:

- Is the data valid?
- Are IDs mapped correctly?
- Did the generation function run?
- Were breps appended to the right output?
- Is the issue code logic or GH Preview wiring?

