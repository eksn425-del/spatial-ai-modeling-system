"""Validate height rule JSON data.

Usage:
    python validate_height_rules.py path/to/height_rules.json
"""

import json
import sys


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(data):
    rules = data if isinstance(data, list) else data.get("height_rules", [])
    errors = []
    warnings = []

    if not isinstance(rules, list) or not rules:
        errors.append("Height rules must be a non-empty list.")
        return errors, warnings

    required = ["parcel_id", "max_height", "min_height", "allow_tower", "allow_podium"]

    for index, rule in enumerate(rules):
        prefix = "height_rules[%d]" % index
        if not isinstance(rule, dict):
            errors.append("%s must be an object." % prefix)
            continue

        for field in required:
            if field not in rule:
                errors.append("%s is missing %s." % (prefix, field))

        max_height = rule.get("max_height")
        min_height = rule.get("min_height")
        if max_height is not None and not isinstance(max_height, (int, float)):
            errors.append("%s.max_height must be numeric." % prefix)
        if min_height is not None and not isinstance(min_height, (int, float)):
            errors.append("%s.min_height must be numeric." % prefix)
        if isinstance(max_height, (int, float)) and isinstance(min_height, (int, float)):
            if min_height > max_height:
                errors.append("%s.min_height cannot exceed max_height." % prefix)

        if "allow_tower" in rule and not isinstance(rule["allow_tower"], bool):
            errors.append("%s.allow_tower must be true or false." % prefix)
        if "allow_podium" in rule and not isinstance(rule["allow_podium"], bool):
            errors.append("%s.allow_podium must be true or false." % prefix)

        if rule.get("allow_tower") is False and rule.get("max_height", 0) > 80:
            warnings.append("%s has high max_height but allow_tower is false." % prefix)

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_height_rules.py path/to/height_rules.json")
        return 2

    data = load_json(sys.argv[1])
    errors, warnings = validate(data)

    print("height_rules validation")
    print("errors:", len(errors))
    for item in errors:
        print("ERROR:", item)
    print("warnings:", len(warnings))
    for item in warnings:
        print("WARNING:", item)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

