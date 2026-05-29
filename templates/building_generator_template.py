"""
Building Generator Template

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
    summary

Preview notes:
    - Connect glass_core, facade_lines, podium_breps, and roof_breps to separate Custom Preview components.
    - Keep all_breps for collection or bake review, not as the only Preview source.
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


def get_value(name, fallback):
    value = globals().get(name, fallback)
    try:
        return float(value)
    except Exception:
        warnings.append("%s was invalid; fallback used." % name)
        return float(fallback)


def get_point():
    if rg is None:
        return None
    candidate = globals().get("pt", None)
    if isinstance(candidate, rg.Point3d):
        return candidate
    warnings.append("pt was missing or invalid; WorldXY origin used.")
    return rg.Point3d(0, 0, 0)


def parse_style_parameters():
    raw = globals().get("style_parameters", {})
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip():
        try:
            return json.loads(raw)
        except Exception:
            warnings.append("style_parameters was not valid JSON; defaults used.")
    return {}


def create_box(origin, size_x, size_y, size_z):
    plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
    box = rg.Box(
        plane,
        rg.Interval(-size_x / 2.0, size_x / 2.0),
        rg.Interval(-size_y / 2.0, size_y / 2.0),
        rg.Interval(0, size_z)
    )
    return box.ToBrep()


try:
    style = parse_style_parameters()
    base_pt = get_point()
    h = get_value("height", 60)
    floors = max(1, int(get_value("floor_count", 18)))
    w = get_value("width", 18)
    d = get_value("depth", 18)
    podium_height = float(style.get("podium_height", min(12, h * 0.2)))
    facade_step = max(1, int(style.get("facade_step", 3)))

    if rg is None:
        warnings.append("Rhino.Geometry is unavailable. No geometry generated.")
    else:
        core = create_box(base_pt, w, d, h)
        glass_core.append(core)
        all_breps.append(core)

        podium = create_box(base_pt, w * 1.4, d * 1.3, podium_height)
        podium_breps.append(podium)
        all_breps.append(podium)

        floor_height = h / float(floors)
        for i in range(0, floors + 1, facade_step):
            z = i * floor_height
            x0 = base_pt.X - w / 2.0
            x1 = base_pt.X + w / 2.0
            y0 = base_pt.Y - d / 2.0
            y1 = base_pt.Y + d / 2.0
            facade_lines.append(rg.Line(rg.Point3d(x0, y0, z), rg.Point3d(x1, y0, z)).ToNurbsCurve())
            facade_lines.append(rg.Line(rg.Point3d(x1, y0, z), rg.Point3d(x1, y1, z)).ToNurbsCurve())
            facade_lines.append(rg.Line(rg.Point3d(x1, y1, z), rg.Point3d(x0, y1, z)).ToNurbsCurve())
            facade_lines.append(rg.Line(rg.Point3d(x0, y1, z), rg.Point3d(x0, y0, z)).ToNurbsCurve())

        roof_origin = rg.Point3d(base_pt.X, base_pt.Y, base_pt.Z + h)
        roof = create_box(roof_origin, w * 0.85, d * 0.85, max(1.0, floor_height * 0.3))
        roof_breps.append(roof)
        all_breps.append(roof)

    geometry_counts = {
        "glass_core": len(glass_core),
        "facade_lines": len(facade_lines),
        "podium_breps": len(podium_breps),
        "roof_breps": len(roof_breps),
        "all_breps": len(all_breps)
    }

    summary = json.dumps({
        "stage": "building_generator_template",
        "status": "success",
        "geometry_counts": geometry_counts,
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
        "stage": "building_generator_template",
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

