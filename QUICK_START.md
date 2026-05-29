# Quick Start

10-minute start guide for the Spatial AI Modeling System.

空间 AI 建模系统 10 分钟快速上手指南。

## Before you start

This system does not automatically finish a design. It is a human-in-the-loop workflow. AI helps prepare data, rules, GH Python cells, templates, validators, and documentation; the designer still validates geometry and visual quality in Rhino/Grasshopper.

这个系统不是自动完成设计的工具，而是一个 human-in-the-loop 工作流。AI 负责数据、规则、GH Python 电池组、模板、验证脚本和文档；设计者仍然需要在 Rhino/Grasshopper 中判断几何输出和视觉质量。

## 1. Read the README

Open `README.md` first.

先打开 `README.md`，理解系统定位：这是空间 AI 建模系统，不是全自动建筑生成器。

## 2. Open the minimal example

Go to:

`examples/minimal_site_project`

进入最小示例项目：

`examples/minimal_site_project`

## 3. Check the sample JSON

Review:

- `data/site_data.sample.json`
- `data/parcels.sample.json`
- `data/spatial_rules.sample.json`
- `data/height_rules.sample.json`

检查示例数据是否能看懂：地块 ID、边界点、中心点、空间规则和限高规则。

## 4. Run validators

From the repository root, run:

```bash
python validators/validate_site_data.py examples/minimal_site_project/data/site_data.sample.json
python validators/validate_parcel_data.py examples/minimal_site_project/data/parcels.sample.json
python validators/validate_height_rules.py examples/minimal_site_project/data/height_rules.sample.json
python validators/validate_building_groups.py examples/minimal_site_project/data/spatial_rules.sample.json examples/minimal_site_project/data/parcels.sample.json
```

Expected result:

- `errors: 0`
- no duplicate parcel IDs

预期结果：

- `errors: 0`
- 没有重复地块编号

## 5. Open the GH Python cell

Open:

`examples/minimal_site_project/gh_cells/example_gh_cell.py`

打开 GH Python 示例电池组代码。

## 6. Copy code into Grasshopper Python

In Grasshopper:

1. Add a Python component.
2. Create inputs named `parcels_json` and `height_rules_json`.
3. Create outputs named `parcel_curves`, `height_points`, `massing_breps`, `warnings`, and `summary`.
4. Copy the code from `example_gh_cell.py` into the component.

在 Grasshopper 中添加 Python 组件，并保持输入输出端口名称一致。

## 7. Connect inputs and outputs

Use Panels or file-reading logic to provide the sample JSON content.

Suggested output wiring:

- `parcel_curves` -> Custom Preview
- `height_points` -> Custom Preview
- `massing_breps` -> Custom Preview
- `warnings` -> Panel
- `summary` -> Panel

建议每个几何输出都单独连接 Custom Preview，不要只看一个合并输出。

## 8. Check the summary Panel

The `summary` output should show JSON with:

- `stage`
- `status`
- `geometry_counts`
- `parameters`
- `warnings`

如果 `summary` 是 null，先检查 Python 输出变量名和 GH 输出端口是否一致。

## 9. Preview outputs separately

Use separate materials or colors for:

- parcel curves
- height points
- massing breps

分别预览每个输出。不要把所有内容混在一起判断，否则很难发现是数据、生成函数还是 Preview 设置出了问题。

## 10. Screenshot and record results

Capture:

- Rhino viewport preview
- Grasshopper component wiring
- summary Panel
- any warnings

截图并记录结果。这个步骤是系统的一部分，因为 human validation 决定输出是否真正可用。
