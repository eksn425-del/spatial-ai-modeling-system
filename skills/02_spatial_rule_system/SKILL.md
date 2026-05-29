# Spatial Rule System

## Purpose

Convert design intent into JSON rules that can be inspected, validated, and used by GH Python cells.

## When to Use

Use this skill after site data is prepared and before city massing or generator logic is created.

## Inputs

- Design intent
- Parcel classifications
- Height requirements
- Tower and podium permissions
- Mobility strategy
- Open space strategy
- Landscape strategy

## Outputs

- `spatial_rules.json`
- `height_rules.json`
- `building_groups.json`
- Rule summary JSON
- Warnings about unclear or conflicting rules

## Procedure

1. Write the design intent as plain text first.
2. Convert intent into hierarchy, open space, mobility, and landscape rules.
3. Classify parcel IDs into primary, secondary, tertiary, open space, and special groups.
4. Assign height rules by parcel ID.
5. Keep tower and podium permissions explicit.
6. Validate duplicate group IDs and missing classifications.
7. Keep rules separate from GH geometry code.

## Codex Role

Codex can translate written rules into structured JSON, find duplicate IDs, check missing fields, and generate validation scripts.

## ChatGPT Role

ChatGPT can help refine design language into clearer spatial strategies, but it should not be the final authority on whether a rule fits the site.

## Human Validation

The human designer decides whether the rule system reflects the intended spatial hierarchy and design narrative.

## Common Failures

- A parcel appears in more than one building group.
- Height rules exist for IDs that do not exist in parcel data.
- The rule file describes design ambition but does not include usable fields.
- City massing and building facade logic are mixed into one rule file.

## Recovery Strategy

- Keep rules readable and shallow instead of over-nesting.
- Validate IDs before generating geometry.
- Separate city-level rules from building-style parameters.
- Use summary JSON to report rule counts, missing IDs, duplicate IDs, and warnings.

## Deliverables

- Rule JSON files
- Rule validation report
- Human-approved rule summary
- Notes for GH cell generation

