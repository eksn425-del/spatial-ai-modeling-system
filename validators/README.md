# Validators

These scripts perform lightweight checks for JSON data used by the Spatial AI Modeling System. They use only the Python standard library.

## Scripts

- `validate_site_data.py`: checks `site_boundary`, `parcels`, and `roads`.
- `validate_parcel_data.py`: checks `parcel_id`, `centroid`, and `boundary_points`.
- `validate_height_rules.py`: checks `max_height`, `min_height`, `allow_tower`, and `allow_podium`.
- `validate_building_groups.py`: checks duplicate IDs across primary, secondary, tertiary, open space, and special groups. If parcel data is provided, it also prints unclassified TODO IDs.

## Example

```bash
python validators/validate_parcel_data.py examples/minimal_site_project/data/parcels.sample.json
python validators/validate_building_groups.py examples/minimal_site_project/data/spatial_rules.sample.json examples/minimal_site_project/data/parcels.sample.json
```

## Validation principle

Validators do not prove that a Rhino/GH model is visually successful. They only reduce data mistakes before geometry generation. Human validation in Rhino/GH is still required.

