# AI Prompt Workflow

## Purpose

Coordinate Codex and ChatGPT prompts so each AI system is used for the part of the workflow it handles best.

## When to Use

Use this skill when creating prompts for data migration, rule generation, GH cell creation, building style breakdown, visual debugging, or portfolio storytelling.

## Inputs

- Current workflow stage
- Available data
- GH errors or visual symptoms
- Desired output format
- Human validation notes

## Outputs

- Codex prompt
- ChatGPT prompt
- Debug prompt
- Documentation prompt
- Portfolio storytelling prompt

## Procedure

1. Decide whether the task is data/code/documentation or visual/style/generator reasoning.
2. Use Codex for structured data, validators, schemas, first-pass GH cells, and docs.
3. Use ChatGPT for style breakdown, GH connection explanations, building generator logic, and visual debugging.
4. Always include expected inputs, expected outputs, and failure symptoms in prompts.
5. Ask for summary JSON and panel summary behavior when requesting GH code.
6. Ask for separate outputs instead of a single `all_breps` preview.
7. Record the prompt and the outcome in a workflow ledger.

## Codex Role

Codex creates productized artifacts, checks consistency, and updates files. It is strongest when the task has explicit structure.

## ChatGPT Role

ChatGPT expands design logic, style reasoning, visual diagnosis, and generator iteration prompts.

## Human Validation

The human designer decides whether the AI answer matches the model seen in Rhino/GH and whether another prompt iteration is needed.

## Common Failures

- Asking Codex to judge visual quality it cannot see reliably.
- Asking ChatGPT for code without giving GH input/output names.
- Forgetting to ask for `summary` and `warnings`.
- Combining city-scale and building facade tasks in one prompt.

## Recovery Strategy

- Rewrite prompts with stage, inputs, outputs, constraints, and validation criteria.
- Split city massing prompts from building generator prompts.
- Include symptoms such as "height points exist but no massing breps" or "output count mismatch".
- Include preview instructions: separate Custom Preview outputs and avoid direct `all_breps` preview.

## Deliverables

- Prompt files
- Prompt usage notes
- Workflow ledger entry
- Human validation note

