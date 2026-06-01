# AI Product Flow Diagram

This diagram explains the Spatial AI Modeling System as an Agent-assisted urban modeling workflow.

```mermaid
flowchart LR
    A["Designer Need<br/>turn messy urban design rules into reusable modeling workflow"] --> B["Input<br/>site boundary<br/>parcel IDs<br/>height rules<br/>design intent"]
    B --> C["Rule Structuring<br/>JSON schemas<br/>input-output contract<br/>validation checklist"]
    C --> D["Agent Workflow<br/>task decomposition<br/>GH Python draft generation<br/>prompt traceability"]
    D --> E["Rhino / Grasshopper Execution<br/>modular cells<br/>separate previews<br/>summary JSON"]
    E --> F["Output<br/>massing candidates<br/>building generator patterns<br/>warnings and counts<br/>case-study package"]
    F --> G["Human Validation<br/>geometry count check<br/>height rule check<br/>spatial quality review"]
    G --> H["Feedback Loop<br/>fix rules<br/>patch GH cells<br/>rerun validators<br/>document lessons"]
    H --> C
```

## Product Manager Reading

- **User problem:** Urban modeling workflows are difficult to reproduce, debug, and explain.
- **Agent role:** Help structure rules, generate modular GH Python cells, and produce validation artifacts.
- **Output value:** A reusable workflow system rather than a one-off model.
- **Validation:** Human review in Rhino/GH decides whether geometry is usable.
