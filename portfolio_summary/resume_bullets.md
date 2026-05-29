# 空间 AI 建模系统｜AI-assisted Spatial Modeling Workflow

- 构建了一个面向空间产品原型与生成式建模的人机协同工作流，将场地数据、地块编号、空间规则、GH Python 电池组、建筑生成器、Rhino/GH 验证和 GitHub 展示组织成可复用系统。
- 使用 Python / RhinoCommon / Grasshopper Python 设计模块化建模模板，避免单一大型 GH 电池组控制整个城市，提高数据映射、输出检查和调试效率。
- 建立 JSON rule system，用于表达地块分级、限高、塔楼/裙房许可、开放空间和交通景观规则。
- 使用 Codex 进行城市尺度数据整理、规则迁移、初版 GH cells、validators 和文档化；使用 ChatGPT 辅助建筑生成器逻辑、风格拆解和视觉调试提示。
- 在 Rhino/GH 中进行人工验证和参数调试，重点检查输出数量、summary JSON、Custom Preview、Preview/Bake 状态和复杂表皮视觉质量。
- 将项目包装为 GitHub product skeleton，包含 skills、schemas、templates、prompts、validators、checklists、docs 和 portfolio summary。

# Spatial AI Modeling System | Human-in-the-loop Design Automation Workflow

- Built a human-in-the-loop spatial modeling workflow that organizes site data, parcel IDs, spatial rules, GH Python cells, building generators, Rhino/GH validation, and GitHub packaging into a reusable product system.
- Designed modular Python / RhinoCommon / Grasshopper Python templates to avoid one oversized GH component controlling an entire city and to improve data mapping, output inspection, and debugging.
- Developed a JSON rule system for parcel hierarchy, height limits, tower/podium permissions, open space logic, mobility rules, and landscape strategy.
- Used Codex for city-scale data organization, rule migration, first-pass GH cells, validators, and documentation; used ChatGPT for building generator logic, style breakdown, and visual debugging prompts.
- Validated outputs in Rhino/GH through human review, checking output counts, summary JSON, Custom Preview routing, Preview/Bake behavior, and complex facade quality.
- Packaged the project as a GitHub-ready product skeleton with skills, schemas, templates, prompts, validators, checklists, docs, and portfolio summaries.

