# Product Manifest

## Product name

Spatial AI Modeling System

空间 AI 建模系统

## Product positioning

Spatial AI Modeling System is a reusable workflow product for AI-assisted spatial modeling. It converts a complex spatial design process into productized modules: data, rules, GH cells, generators, validation, prompts, and GitHub packaging.

This project should be understood as a workflow system and skill library, not as a traditional architecture portfolio project.

## Target users

- Architecture and urban design students
- Spatial product designers
- AI modeling learners
- Rhino and Grasshopper users

## User problem

Spatial design modeling is difficult to reproduce because data, rules, code, and visual judgment are often mixed together in one fragile process.

Common pain points:

- Site data, parcel IDs, road information, and height limits are hard to normalize.
- AI-generated geometry is often unstable or visually uncontrolled.
- GH Python components can become too large and hard to debug.
- Data and model outputs lack a standard workflow.
- Complex facade or tower skin generation may run but still fail visually.
- Preview and bake states in Rhino/GH can become confusing when all outputs are merged.

## Product value

The system decomposes spatial design automation into:

- Data preparation
- JSON rule systems
- GH Python cell patterns
- City massing generators
- Individual building generator patterns
- Rhino/GH validation protocols
- AI prompt workflows
- GitHub and portfolio packaging

The value is not that AI replaces the designer. The value is that AI-assisted modeling becomes structured, inspectable, reusable, and explainable.

## Core features

1. Data-to-model workflow
2. JSON rule system
3. GH Python cell pattern
4. Building generator pattern
5. Rhino/GH validation protocol
6. AI prompt library
7. GitHub portfolio packaging

## Product principles

- Separate city-scale massing from individual building facade generation.
- Avoid one large GH component controlling an entire city.
- Require panel summaries and JSON summaries.
- Keep output variables aligned with GH output ports.
- Preview each geometry output independently through Custom Preview.
- Treat AI output as a draft that must be validated in Rhino/GH.
- Document both success and failure cases.

## Future product direction

- Web UI for spatial rule authoring
- Visual parameter editor
- Automatic GH cell generator
- Rendering export workflow
- Model QA system
- Versioned case-study builder
- Prompt-to-schema assistant
- Rhino/GH validation dashboard

