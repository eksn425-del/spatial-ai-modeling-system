"""
Minimal GH Python cell example.

Inputs:
    parcels_json: JSON string containing parcel records.
    height_rules_json: JSON string containing height rules.

Outputs:
    parcel_curves
    height_points
    massing_breps
    warnings
    summary

This example is intentionally simple. It demonstrates data-to-output structure,
not a finished design.
"""

import json

try:
    import Rhino.Geometry as rg
except Exception:
    rg = None


parcel_curves = []
height_points = []
massing_breps = []
warnings = []
summary = ""


def point_from_list(values):
    z = values[2] if len(values) > 2 else 0
    return rg.Point3d(values[0], values[1], z)


def make_curve(points):
    rhino_points = [point_from_list(point) for point in points]
    if rhino_points[0] != rhino_points[-1]:
        rhino_points.append(rhino_points[0])
    return rg.Polyline(rhino_points).ToNurbsCurve()


def make_box_from_boundary(points, height):
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(min(xs), max(xs)),
        rg.Interval(min(ys), max(ys)),
        rg.Interval(0, height)
    )
    return box.ToBrep()


try:
    parcels = json.loads(parcels_json if "parcels_json" in globals() and parcels_json else "[]")
    height_rules = json.loads(height_rules_json if "height_rules_json" in globals() and height_rules_json else "[]")
    height_by_id = {rule["parcel_id"]: rule for rule in height_rules if "parcel_id" in rule}

    if rg is None:
        warnings.append("Rhino.Geometry unavailable. Run inside Rhino/GH for geometry.")
    else:
        for parcel in parcels:
            parcel_id = parcel.get("parcel_id", "unknown")
            boundary = parcel.get("boundary_points", [])
            centroid = parcel.get("centroid", [0, 0, 0])
            rule = height_by_id.get(parcel_id)

            if not boundary or len(boundary) < 3:
                warnings.append("Parcel %s has invalid boundary." % parcel_id)
                continue

            parcel_curves.append(make_curve(boundary))

            if not rule:
                warnings.append("Parcel %s has no height rule." % parcel_id)
                continue

            max_height = float(rule.get("max_height", 0))
            height_points.append(point_from_list([centroid[0], centroid[1], max_height]))

            if max_height > 0 and (rule.get("allow_tower") or rule.get("allow_podium")):
                massing_breps.append(make_box_from_boundary(boundary, max_height))

    summary = json.dumps({
        "stage": "minimal_site_project.example_gh_cell",
        "status": "success",
        "geometry_counts": {
            "parcel_curves": len(parcel_curves),
            "height_points": len(height_points),
            "massing_breps": len(massing_breps)
        },
        "parameters": {
            "parcel_count": len(parcels),
            "height_rule_count": len(height_rules)
        },
        "warnings": warnings
    }, ensure_ascii=False, indent=2)

except Exception as exc:
    warnings.append(str(exc))
    summary = json.dumps({
        "stage": "minimal_site_project.example_gh_cell",
        "status": "failed",
        "geometry_counts": {
            "parcel_curves": len(parcel_curves),
            "height_points": len(height_points),
            "massing_breps": len(massing_breps)
        },
        "parameters": {},
        "warnings": warnings
    }, ensure_ascii=False, indent=2)

