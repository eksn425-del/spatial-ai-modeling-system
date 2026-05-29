"""Validate building group classification JSON data.

Usage:
    python validate_building_groups.py path/to/building_groups.json [path/to/parcels.json]
"""

import json
import sys


GROUP_FIELDS = [
    "primary_core_ids",
    "secondary_tod_ids",
    "tertiary_living_ids",
    "open_space_ids",
    "special_ids"
]


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_parcel_ids(data):
    parcels = data if isinstance(data, list) else data.get("parcels", [])
    ids = []
    for item in parcels:
        if isinstance(item, dict) and item.get("parcel_id"):
            ids.append(item["parcel_id"])
        elif isinstance(item, str):
            ids.append(item)
    return ids


def validate(groups, known_parcel_ids=None):
    errors = []
    warnings = []
    id_to_groups = {}

    if isinstance(groups, dict) and "building_groups" in groups:
        groups = groups["building_groups"]

    for field in GROUP_FIELDS:
        values = groups.get(field)
        if not isinstance(values, list):
            errors.append("%s must be a list." % field)
            continue
        for parcel_id in values:
            if not isinstance(parcel_id, str):
                errors.append("%s contains a non-string ID." % field)
                continue
            id_to_groups.setdefault(parcel_id, []).append(field)

    duplicate_ids = sorted([parcel_id for parcel_id, fields in id_to_groups.items() if len(fields) > 1])
    for parcel_id in duplicate_ids:
        errors.append("Duplicate ID %s appears in: %s" % (parcel_id, ", ".join(id_to_groups[parcel_id])))

    if known_parcel_ids:
        classified = set(id_to_groups.keys())
        known = set(known_parcel_ids)
        unclassified = sorted(known - classified)
        unknown = sorted(classified - known)

        if unclassified:
            warnings.append("Unclassified TODO IDs: %s" % ", ".join(unclassified))
        if unknown:
            warnings.append("Group IDs not found in parcel data: %s" % ", ".join(unknown))

    return errors, warnings, duplicate_ids


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python validate_building_groups.py path/to/building_groups.json [path/to/parcels.json]")
        return 2

    groups = load_json(sys.argv[1])
    known_ids = extract_parcel_ids(load_json(sys.argv[2])) if len(sys.argv) == 3 else None
    errors, warnings, duplicate_ids = validate(groups, known_ids)

    print("building_groups validation")
    print("duplicate_ids:", duplicate_ids)
    print("errors:", len(errors))
    for item in errors:
        print("ERROR:", item)
    print("warnings:", len(warnings))
    for item in warnings:
        print("WARNING:", item)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
