"""Validate site-level JSON data.

Usage:
    python validate_site_data.py path/to/site_data.json
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


def validate(data):
    errors = []
    warnings = []

    boundary = data.get("site_boundary")
    if not isinstance(boundary, list) or len(boundary) < 3:
        errors.append("site_boundary must contain at least three points.")
    elif not all(is_point(point) for point in boundary):
        errors.append("site_boundary contains invalid points.")

    parcels = data.get("parcels")
    if not isinstance(parcels, list) or not parcels:
        errors.append("parcels must be a non-empty list.")

    roads = data.get("roads")
    if not isinstance(roads, list):
        errors.append("roads field must exist and be a list.")
    else:
        for index, road in enumerate(roads):
            if not isinstance(road, dict):
                errors.append("roads[%d] must be an object." % index)
                continue
            if "road_id" not in road:
                errors.append("roads[%d] is missing road_id." % index)
            if "points" not in road:
                errors.append("roads[%d] is missing points." % index)
            elif not isinstance(road["points"], list) or len(road["points"]) < 2:
                errors.append("roads[%d].points must contain at least two points." % index)
            elif not all(is_point(point) for point in road["points"]):
                errors.append("roads[%d].points contains invalid points." % index)

    if not data.get("coordinate_system"):
        warnings.append("coordinate_system is missing or empty.")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_site_data.py path/to/site_data.json")
        return 2

    data = load_json(sys.argv[1])
    errors, warnings = validate(data)

    print("site_data validation")
    print("errors:", len(errors))
    for item in errors:
        print("ERROR:", item)
    print("warnings:", len(warnings))
    for item in warnings:
        print("WARNING:", item)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

