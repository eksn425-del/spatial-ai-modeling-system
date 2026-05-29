# Spatial AI Modeling System

Human-in-the-loop Workflow for Space Product Prototyping and Generative Modeling

## Current Status

- v0.1 system release is ready for GitHub initialization
- Product skeleton completed
- Skills system completed
- Schemas / templates / validators completed
- Minimal examples included
- Real Rhino/GH screenshots, demo GIF, and portfolio board still need to be added

空间 AI 建模系统：面向空间产品原型与生成式建模的人机协同工作流

## What is this system

Spatial AI Modeling System is a productized skills and workflow framework for AI-assisted spatial modeling. It translates site data, parcel IDs, spatial rules, design intent, Grasshopper Python cells, building generator patterns, validation steps, and portfolio packaging into a reusable system.

This is not a fully autonomous architecture generator. It is a human-in-the-loop spatial modeling workflow for people who want to turn messy spatial design processes into clear data structures, modular GH Python components, testable generators, and documented case studies.

空间 AI 建模系统是一个产品化的 skills 与 workflow 项目骨架，用于把场地数据、空间规则、地块编号、设计意图、GH Python 电池组、建筑生成器、Rhino/GH 验证和 GitHub 展示整理成可复用流程。

它不是全自动建筑生成器，而是一个人机协同的空间建模工作流。

## Why it exists

AI can help spatial designers move faster, but it often fails when geometry, style, facade logic, and Grasshopper connections become too complex. A single oversized GH component can become unstable, outputs can mismatch, preview and bake can become confusing, and generated building envelopes can look visually wrong even when the code runs.

This system exists to make the workflow explicit:

- Use data and JSON rules to control spatial intent.
- Use small GH Python cells instead of one large city-scale component.
- Separate city massing from individual building facade generation.
- Require summary JSON and panel summaries for every major step.
- Validate geometry in Rhino/GH with human judgment before treating output as successful.
- Package the final process as a product, not as a hidden one-off experiment.

## Who it is for

- Architecture and urban design students who want a structured AI-assisted modeling workflow.
- Spatial product designers who prototype spatial systems, layouts, and generators.
- AI modeling learners who want to understand where AI helps and where it fails.
- Rhino, Grasshopper, GH Python, and RhinoCommon users who need repeatable component patterns.

## Workflow overview

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

## Repository Map

- [docs/](docs/) contains system principles, limitations, and release planning.
- [skills/](skills/) contains the reusable workflow skills.
- [examples/minimal_site_project/](examples/minimal_site_project/) contains fictional sample data and a GH Python cell.

## Core skills

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

## Tech stack

- JSON for spatial data and rule definitions
- Python for validation scripts and reusable templates
- GH Python for Grasshopper component logic
- RhinoCommon for geometry construction inside Rhino/GH
- Rhino and Grasshopper for preview, iteration, and baking
- Codex for data migration, rule organization, first-pass GH cells, validators, docs, and packaging
- ChatGPT for building style breakdown, generator logic, GH wiring strategy, and visual debugging prompts
- GitHub for productized presentation and versioned workflow documentation

## Human-in-the-loop principle

The system assumes that AI output is a draft, not a final model. Codex is strong at structured data, code scaffolding, schema thinking, and documentation. ChatGPT is useful for style decomposition, generator logic, and explaining GH connections. Rhino/GH and human judgment are still required for spatial quality, visual coherence, facade behavior, preview control, and final model acceptance.

Every major modeling step should produce:

- Separate geometry outputs that can be independently previewed.
- A panel summary.
- A JSON summary with status, geometry counts, parameters, and warnings.
- A human validation note before the result is considered usable.

## What this system is not

- Not a fully autonomous architecture generator.
- Not a backup of old architecture projects.
- Not a collection of finished building designs.
- Not a promise that AI can judge visual quality reliably.
- Not one giant GH component controlling an entire city.
- Not a replacement for Rhino/GH validation, design judgment, or iteration.

## Future roadmap

- Web UI for rule editing and workflow tracking.
- Visual parameter editor for parcels, heights, groups, and generator parameters.
- Automatic GH cell generator from schema definitions.
- Rendering and image export workflow.
- Model QA system for geometry counts, missing breps, preview state, and output mismatches.
- Case-study packaging format for internships, portfolios, and product demos.
