# Data Preflight Checklist

- Confirm `site_id` exists.
- Confirm `site_boundary` has at least three ordered points.
- Confirm all parcels have `parcel_id`.
- Confirm all parcels have `boundary_points`.
- Confirm all parcels have `centroid`.
- Confirm roads field exists, even if empty.
- Confirm coordinate system notes are present.
- Confirm parcel IDs match across parcels, height rules, and building groups.
- Confirm missing or uncertain geometry is recorded in notes.
- Run validators before GH cell generation.

