"""
Single tower generator example.

Inputs:
    pt
    height
    floor_count
    width
    depth
    style_parameters

Outputs:
    glass_core
    facade_lines
    podium_breps
    roof_breps
    all_breps
    warnings
    summary

This is a simple interface example, not a finished building design.
"""

import json

try:
    import Rhino.Geometry as rg
except Exception:
    rg = None


glass_core = []
facade_lines = []
podium_breps = []
roof_breps = []
all_breps = []
warnings = []
summary = ""


def to_number(name, fallback):
    value = globals().get(name, fallback)
    try:
        return float(value)
    except Exception:
        warnings.append("%s invalid; fallback used." % name)
        return float(fallback)


def parse_style():
    raw = globals().get("style_parameters", {})
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip():
        try:
            return json.loads(raw)
        except Exception:
            warnings.append("style_parameters invalid JSON; defaults used.")
    return {}


def base_point():
    value = globals().get("pt", None)
    if rg is not None and isinstance(value, rg.Point3d):
        return value
    warnings.append("pt missing or invalid; origin used.")
    return rg.Point3d(0, 0, 0)


def make_box(origin, width, depth, height):
    plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
    box = rg.Box(
        plane,
        rg.Interval(-width / 2.0, width / 2.0),
        rg.Interval(-depth / 2.0, depth / 2.0),
        rg.Interval(0, height)
    )
    return box.ToBrep()


try:
    h = to_number("height", 72)
    floors = max(1, int(to_number("floor_count", 24)))
    w = to_number("width", 18)
    d = to_number("depth", 16)
    style = parse_style()

    if rg is None:
        warnings.append("Rhino.Geometry unavailable. Run inside Rhino/GH for geometry.")
    else:
        origin = base_point()
        podium_height = float(style.get("podium_height", min(10, h * 0.18)))
        facade_step = max(1, int(style.get("facade_step", 3)))
        roof_height = float(style.get("roof_height", 2))

        core = make_box(origin, w, d, h)
        glass_core.append(core)
        all_breps.append(core)

        podium = make_box(origin, w * 1.35, d * 1.35, podium_height)
        podium_breps.append(podium)
        all_breps.append(podium)

        floor_height = h / float(floors)
        for floor_index in range(0, floors + 1, facade_step):
            z = origin.Z + floor_index * floor_height
            facade_lines.append(rg.Line(rg.Point3d(origin.X - w / 2.0, origin.Y - d / 2.0, z), rg.Point3d(origin.X + w / 2.0, origin.Y - d / 2.0, z)).ToNurbsCurve())
            facade_lines.append(rg.Line(rg.Point3d(origin.X + w / 2.0, origin.Y - d / 2.0, z), rg.Point3d(origin.X + w / 2.0, origin.Y + d / 2.0, z)).ToNurbsCurve())

        roof_origin = rg.Point3d(origin.X, origin.Y, origin.Z + h)
        roof = make_box(roof_origin, w * 0.8, d * 0.8, roof_height)
        roof_breps.append(roof)
        all_breps.append(roof)

    summary = json.dumps({
        "stage": "single_tower_generator",
        "status": "success",
        "geometry_counts": {
            "glass_core": len(glass_core),
            "facade_lines": len(facade_lines),
            "podium_breps": len(podium_breps),
            "roof_breps": len(roof_breps),
            "all_breps": len(all_breps)
        },
        "parameters": {
            "height": h,
            "floor_count": floors,
            "width": w,
            "depth": d,
            "style_parameters": style
        },
        "warnings": warnings
    }, ensure_ascii=False, indent=2)

except Exception as exc:
    warnings.append(str(exc))
    summary = json.dumps({
        "stage": "single_tower_generator",
        "status": "failed",
        "geometry_counts": {
            "glass_core": len(glass_core),
            "facade_lines": len(facade_lines),
            "podium_breps": len(podium_breps),
            "roof_breps": len(roof_breps),
            "all_breps": len(all_breps)
        },
        "parameters": {},
        "warnings": warnings
    }, ensure_ascii=False, indent=2)

