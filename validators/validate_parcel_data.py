"""Validate parcel JSON data.

Usage:
    python validate_parcel_data.py path/to/parcels.json
"""

import json
import sys


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def is_point(value):
    return (
        isinstance(value, list)
        and 2 <= len(value) <= 3
        and all(isinstance(item, (int, float)) for item in value)
    )


def validate_parcel(parcel, index):
    errors = []
    prefix = "parcel[%d]" % index

    if not isinstance(parcel, dict):
        return ["%s must be an object." % prefix]

    if not parcel.get("parcel_id"):
        errors.append("%s is missing parcel_id." % prefix)

    centroid = parcel.get("centroid")
    if not is_point(centroid):
        errors.append("%s.centroid must be a 2D or 3D point." % prefix)

    boundary = parcel.get("boundary_points")
    if not isinstance(boundary, list) or len(boundary) < 3:
        errors.append("%s.boundary_points must contain at least three points." % prefix)
    elif not all(is_point(point) for point in boundary):
        errors.append("%s.boundary_points contains invalid points." % prefix)

    return errors


def validate(data):
    parcels = data if isinstance(data, list) else data.get("parcels", [])
    errors = []
    warnings = []
    seen = set()

    if not parcels:
        errors.append("No parcels found.")
        return errors, warnings

    for index, parcel in enumerate(parcels):
        errors.extend(validate_parcel(parcel, index))
        parcel_id = parcel.get("parcel_id") if isinstance(parcel, dict) else None
        if parcel_id:
            if parcel_id in seen:
                errors.append("Duplicate parcel_id: %s" % parcel_id)
            seen.add(parcel_id)

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_parcel_data.py path/to/parcels.json")
        return 2

    data = load_json(sys.argv[1])
    errors, warnings = validate(data)

    print("parcel_data validation")
    print("errors:", len(errors))
    for item in errors:
        print("ERROR:", item)
    print("warnings:", len(warnings))
    for item in warnings:
        print("WARNING:", item)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

