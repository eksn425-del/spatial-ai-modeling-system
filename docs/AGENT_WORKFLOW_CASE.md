# Agent Workflow Case: Maluan TOD

## Case Positioning

The Maluan TOD case is a workflow case, not a public release of the original urban-design project. It demonstrates how a TOD modeling task can be decomposed into structured inputs, Agent-assisted generation, Rhino/GH validation, and human design judgment.

## Core Question

How can a complex urban design modeling task be converted into a repeatable Agent-assisted workflow instead of a one-off Rhino/Grasshopper file?

## Workflow Loop

```text
Planning intent
-> parcel and height rules
-> JSON rule system
-> GH Python cell generation
-> Rhino/GH preview
-> validation report
-> manual design iteration
-> reusable skill documentation
```

## What the Agent Does

Codex is used for:

- transforming messy design notes into structured schemas
- drafting JSON rule formats
- generating first-pass GH Python cell templates
- writing validators
- creating documentation, checklists, and release materials
- organizing workflow evidence for GitHub

ChatGPT is used for:

- building-type and style breakdown
- facade generator reasoning
- GH wiring explanation
- visual debugging prompts
- portfolio storytelling

## What the Human Designer Does

The designer remains responsible for:

- deciding design intent and spatial hierarchy
- checking whether rules match the actual planning logic
- previewing geometry in Rhino/GH
- judging skyline, density, open-space quality, and massing composition
- fixing GH wiring issues
- deciding whether an output is spatially acceptable

## Input Evidence

The public repository uses sanitized sample inputs:

- `examples/minimal_site_project/data/site_data.sample.json`
- `examples/minimal_site_project/data/parcels.sample.json`
- `examples/minimal_site_project/data/height_rules.sample.json`
- `examples/minimal_site_project/data/spatial_rules.sample.json`

The real project data remains private.

## Output Evidence

The current v0.1 release can show:

- schema-driven data contracts
- validators
- GH Python cell structure
- workflow map
- case study documentation
- prompt workflow
- validation checklists

The visual release still needs:

- Rhino viewport screenshots
- Grasshopper canvas screenshot
- summary panel screenshot
- generated massing GIF
- portfolio board

## Why This Counts as an AI Product Workflow

The project does not claim that AI automatically designs a city. Its product claim is narrower and stronger:

```text
AI assists the modeling workflow by turning spatial rules into modular code, validation artifacts, and repeatable modeling steps, while humans validate spatial quality in Rhino/GH.
```

## Interview Summary

In the Maluan TOD workflow, I used AI as an Agent-assisted modeling partner rather than a design replacement. I structured site data and planning rules into JSON, used Codex to generate modular GH Python cells and validators, then relied on Rhino/GH preview and human design judgment to check whether the outputs were spatially usable.
