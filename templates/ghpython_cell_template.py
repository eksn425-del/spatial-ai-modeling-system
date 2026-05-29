"""
GH Python Cell Template

Inputs:
    input_json: str
        JSON string or small configuration payload from Grasshopper.
    scale: float
        Optional scale factor for placeholder geometry.

Outputs:
    preview_curves
    preview_points
    preview_breps
    all_breps
    warnings
    summary

Grasshopper notes:
    - Keep output names exactly aligned with GH output ports.
    - Connect each preview output to its own Custom Preview.
    - Do not use all_breps as the only Preview connection.
    - Keep a Panel connected to summary.
"""

import json

try:
    import Rhino.Geometry as rg
except Exception:
    rg = None


preview_curves = []
preview_points = []
preview_breps = []
all_breps = []
warnings = []
summary = ""


def safe_number(value, fallback):
    try:
        return float(value)
    except Exception:
        warnings.append("Invalid number value; fallback used.")
        return fallback


def make_placeholder_geometry(config):
    geometry_counts = {
        "preview_curves": 0,
        "preview_points": 0,
        "preview_breps": 0,
        "all_breps": 0
    }

    if rg is None:
        warnings.append("Rhino.Geometry is unavailable. Placeholder counts only.")
        return geometry_counts

    local_scale = safe_number(config.get("scale", scale if "scale" in globals() else 1.0), 1.0)

    p0 = rg.Point3d(0, 0, 0)
    p1 = rg.Point3d(10 * local_scale, 0, 0)
    p2 = rg.Point3d(10 * local_scale, 10 * local_scale, 0)
    p3 = rg.Point3d(0, 10 * local_scale, 0)

    polyline = rg.Polyline([p0, p1, p2, p3, p0])
    curve = polyline.ToNurbsCurve()
    preview_curves.append(curve)
    preview_points.extend([p0, p1, p2, p3])

    height = safe_number(config.get("height", 20), 20)
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, 10 * local_scale), rg.Interval(0, 10 * local_scale), rg.Interval(0, height))
    brep = box.ToBrep()
    preview_breps.append(brep)
    all_breps.append(brep)

    geometry_counts["preview_curves"] = len(preview_curves)
    geometry_counts["preview_points"] = len(preview_points)
    geometry_counts["preview_breps"] = len(preview_breps)
    geometry_counts["all_breps"] = len(all_breps)
    return geometry_counts


try:
    raw_input = input_json if "input_json" in globals() and input_json else "{}"
    config = json.loads(raw_input)
    geometry_counts = make_placeholder_geometry(config)

    summary_data = {
        "stage": "ghpython_cell_template",
        "status": "success",
        "geometry_counts": geometry_counts,
        "parameters": config,
        "warnings": warnings
    }
    summary = json.dumps(summary_data, ensure_ascii=False, indent=2)

except Exception as exc:
    warnings.append(str(exc))
    summary_data = {
        "stage": "ghpython_cell_template",
        "status": "failed",
        "geometry_counts": {
            "preview_curves": len(preview_curves),
            "preview_points": len(preview_points),
            "preview_breps": len(preview_breps),
            "all_breps": len(all_breps)
        },
        "parameters": {},
        "warnings": warnings
    }
    summary = json.dumps(summary_data, ensure_ascii=False, indent=2)

