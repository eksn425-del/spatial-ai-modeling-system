# Building Generator Checklist

- Generator is tested on one building prototype first.
- City massing and building facade logic are separate.
- Inputs include `pt`, `height`, `floor_count`, `width`, `depth`, and `style_parameters`.
- Outputs include `glass_core`, `facade_lines`, `podium_breps`, `roof_breps`, `all_breps`, `warnings`, and `summary`.
- `glass_core` appears before facade logic is judged.
- Facade lines attach to the mass.
- Podium connects visually to the core.
- Roof does not appear abrupt unless intentionally designed.
- Each output is previewed separately.
- Summary JSON reports geometry counts.
- Human validation happens before reusing the generator across many parcels.

