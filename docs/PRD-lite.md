# PRD-lite: Spatial AI Modeling System

## Product Goal

Build a reusable Agent-assisted urban modeling workflow that helps designers convert site information, parcel rules, and design intent into modular Rhino/Grasshopper modeling components with explicit validation checkpoints.

## Target Users

- Urban design students building complex Rhino/GH models.
- Spatial product designers prototyping rule-based layouts.
- Architecture technology learners exploring AI-assisted modeling.
- Design teams that need a repeatable workflow for site data, rules, geometry outputs, and documentation.

## Problem Statement

AI tools can generate code quickly, but spatial modeling often fails when rules, geometry, Grasshopper wiring, and visual judgment are mixed into one large black-box component. The result may run but still be spatially wrong, hard to debug, or impossible to explain.

This system solves that by separating the workflow into data preparation, rule definition, modular GH Python cells, Rhino/GH preview, validation summaries, and human review.

## Core User Story

As a designer, I want to turn parcel IDs, height limits, mobility rules, and design intent into small GH Python cells and validation outputs, so that I can iterate urban massing models with AI assistance while still controlling design quality.

## MVP Scope

Included in v0.1:

- Skill-based workflow system.
- JSON schemas for site data, parcels, building groups, and height rules.
- Minimal sample project.
- GH Python cell template.
- Python validators.
- Prompt templates for Codex and ChatGPT.
- Human-in-the-loop validation checklists.
- Sanitized Maluan TOD workflow case study.

Out of scope for v0.1:

- Finished Rhino/GH project file.
- Public release of raw urban-design project files.
- Autonomous full-city design generation.
- Visual dashboard.
- Automatic model quality judgment.

## Product Flow

1. Designer defines spatial intent and project scope.
2. Site data is converted into structured JSON.
3. Height rules, parcel hierarchy, mobility logic, and building-group rules are validated.
4. Agent generates small GH Python cells from the structured inputs.
5. Designer previews each geometry output in Rhino/GH.
6. System writes summary JSON and panel summaries.
7. Designer checks geometry count, height compliance, preview/bake state, and visual quality.
8. Workflow is documented as a case study and reusable skill package.

## Success Criteria

- A new user can understand the workflow without seeing private project files.
- Sample data can be validated with bundled validators.
- GH Python cells have clear inputs, outputs, warnings, and summary JSON.
- The case study explains what AI did, what the human validated, and what remains manual.
- The repository can support internship and portfolio discussion as an AI Native workflow project.

## Risks and Limits

- AI-generated code may be syntactically valid but spatially poor.
- Rhino/GH validation is still required.
- Visual quality and facade logic cannot be fully judged by the current system.
- Real project screenshots and GIFs are still needed for a stronger visual release.

## Next Product Upgrade

The next version should add real Rhino/GH screenshots, a workflow GIF, a completed output board, and a small visual QA report showing before/after debugging states.
