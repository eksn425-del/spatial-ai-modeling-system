# Spatial AI Modeling System

Human-in-the-loop Workflow for Space Product Prototyping and Generative Modeling

## 中文项目简介

**Spatial AI Modeling System｜空间 AI 建模系统** 是一个面向 Rhino / Grasshopper / GHPython 的 AI 辅助空间建模工作流系统。它把场地数据、地块规则、设计意图、GH Python 电池组、生成器模板、验证脚本和作品集包装，整理成可复用的 skills + workflow 项目。

这个项目不是全自动建筑生成器，而是 **human-in-the-loop spatial modeling workflow**：AI 负责数据整理、规则结构、代码模板和文档化；设计者负责 Rhino/GH 预览、几何判断、视觉质量和最终取舍。

**项目关键词：** Agent-assisted Workflow、AI Coding、Vibe Coding、Rhino / Grasshopper、空间智能工具系统。

## Current Status

- v0.1 system release is published as a public GitHub-ready workflow prototype
- Product skeleton completed
- Skills system completed
- Schemas / templates / validators completed
- Minimal examples included
- Real Rhino/GH screenshots, demo GIF, and portfolio board still need to be added

## What Is This System

Spatial AI Modeling System is a productized skills and workflow framework for AI-assisted spatial modeling. It translates site data, parcel IDs, spatial rules, design intent, Grasshopper Python cells, building generator patterns, validation steps, and portfolio packaging into a reusable system.

This is not a fully autonomous architecture generator. It is a human-in-the-loop spatial modeling workflow for people who want to turn messy spatial design processes into clear data structures, modular GH Python components, testable generators, and documented case studies.

In product terms, it is an **Agent-assisted urban modeling workflow**: AI helps organize rules, generate modular code, and create validation artifacts, while the designer remains responsible for spatial judgment, Rhino/GH verification, and final model acceptance.

中文定位：这是一个面向 Rhino / Grasshopper / GHPython 的空间 AI 建模工作流系统。它不是自动城市设计生成器，而是把城市设计任务拆成数据输入、规则结构、Agent 辅助建模、几何验证和人工复核的产品流程。

## Product Logic

```text
site boundary + parcel data + height rules + design intent
-> structured JSON rules
-> Agent-assisted GH Python cell generation
-> Rhino/GH preview and summary JSON
-> human validation of geometry counts, heights, and spatial quality
-> documented workflow case for GitHub / portfolio review
```

The product value is not "AI replaces the designer." The value is that AI turns a messy urban modeling task into a repeatable workflow that can be checked, debugged, reused, and explained.

## Why It Exists

AI can help spatial designers move faster, but it often fails when geometry, style, facade logic, and Grasshopper connections become too complex. A single oversized GH component can become unstable, outputs can mismatch, preview and bake can become confusing, and generated building envelopes can look visually wrong even when the code runs.

This system exists to make the workflow explicit:

- Use data and JSON rules to control spatial intent.
- Use small GH Python cells instead of one large city-scale component.
- Separate city massing from individual building facade generation.
- Require summary JSON and panel summaries for every major step.
- Validate geometry in Rhino/GH with human judgment before treating output as successful.
- Package the final process as a product, not as a hidden one-off experiment.

## Who It Is For

- Architecture and urban design students who want a structured AI-assisted modeling workflow.
- Spatial product designers who prototype spatial systems, layouts, and generators.
- AI modeling learners who want to understand where AI helps and where it fails.
- Rhino, Grasshopper, GH Python, and RhinoCommon users who need repeatable component patterns.

## Workflow Overview

1. Define spatial intent and project scope.
2. Prepare site data, parcel IDs, boundaries, roads, and notes.
3. Convert intent into JSON rule systems.
4. Generate modular GH Python cells with clear inputs and outputs.
5. Preview each output separately in Rhino/GH.
6. Validate geometry, counts, height rules, and design quality manually.
7. Use ChatGPT for complex building style breakdowns, generator logic, and GH connection reasoning.
8. Iterate in Rhino/GH until the model is stable enough to document.
9. Package the process as GitHub documentation, prompts, templates, examples, and portfolio material.

## Quick Start

Start here:

[QUICK_START.md](QUICK_START.md)

The quick start walks through the minimal sample data, validators, GH Python cell, summary Panel, and Custom Preview checks.

## Case Study

See the sanitized workflow demo:

[case_studies/maluan_tod_workflow_demo/](case_studies/maluan_tod_workflow_demo/)

This case study demonstrates how the system can be applied to a real AI-assisted spatial modeling workflow, without exposing raw project assets.

Real Rhino/GH screenshots and demo GIF will be added in a later visual release.

## Product Documents

- [PRD-lite](docs/PRD-lite.md)
- [AI product flow diagram](docs/AI_PRODUCT_FLOW_DIAGRAM.md)
- [Agent workflow case](docs/AGENT_WORKFLOW_CASE.md)
- [Input / output contract](docs/INPUT_OUTPUT_CONTRACT.md)
- [Validation metrics](docs/VALIDATION_METRICS.md)
- [Interview talking points](docs/INTERVIEW_TALKING_POINTS.md)

## Repository Map

- [docs/](docs/) contains system principles, limitations, and release planning.
- [skills/](skills/) contains the reusable workflow skills.
- [examples/minimal_site_project/](examples/minimal_site_project/) contains fictional sample data and a GH Python cell.
- [中文产品定位说明](docs/PRODUCT_POSITIONING_CN.md)
- [schemas/](schemas/) contains JSON contracts for data and rules.
- [validators/](validators/) contains Python scripts for preflight checks.
- [prompts/](prompts/) contains prompt workflows for Codex and ChatGPT.
- [case_studies/](case_studies/) contains public-safe workflow demos.

## Core Skills

- Master system orchestration
- Site data preparation
- Spatial rule system design
- GH Python cell design
- City massing generation
- Building generator design
- Rhino/Grasshopper validation
- AI prompt workflow
- Debugging protocol
- GitHub product packaging

## Tech Stack

- JSON for spatial data and rule definitions
- Python for validation scripts and reusable templates
- GH Python for Grasshopper component logic
- RhinoCommon for geometry construction inside Rhino/GH
- Rhino and Grasshopper for preview, iteration, and baking
- Codex for data migration, rule organization, first-pass GH cells, validators, docs, and packaging
- ChatGPT for building style breakdown, generator logic, GH wiring strategy, and visual debugging prompts
- GitHub for productized presentation and versioned workflow documentation

## Human-in-the-loop Principle

The system assumes that AI output is a draft, not a final model. Codex is strong at structured data, code scaffolding, schema thinking, and documentation. ChatGPT is useful for style decomposition, generator logic, and explaining GH connections. Rhino/GH and human judgment are still required for spatial quality, visual coherence, facade behavior, preview control, and final model acceptance.

Every major modeling step should produce:

- Separate geometry outputs that can be independently previewed.
- A panel summary.
- A JSON summary with status, geometry counts, parameters, and warnings.
- A human validation note before the result is considered usable.

## What This System Is Not

- Not a fully autonomous architecture generator.
- Not a backup of old architecture projects.
- Not a collection of finished building designs.
- Not a promise that AI can judge visual quality reliably.
- Not one giant GH component controlling an entire city.
- Not a replacement for Rhino/GH validation, design judgment, or iteration.

## Future Roadmap

- Web UI for rule editing and workflow tracking.
- Visual parameter editor for parcels, heights, groups, and generator parameters.
- Automatic GH cell generator from schema definitions.
- Rendering and image export workflow.
- Model QA system for geometry counts, missing breps, preview state, and output mismatches.
- Case-study packaging format for internships, portfolios, and product demos.
