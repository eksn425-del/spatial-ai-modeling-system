# Workflow Map

```mermaid
flowchart TD
    A["Spatial Intent"] --> B["Site Data"]
    B --> C["JSON Rules"]
    C --> D["Codex GH Cell Generation"]
    D --> E["Rhino/GH Preview"]
    E --> F["Human Validation"]
    F --> G["ChatGPT Building Generator"]
    G --> H["Rhino/GH Iteration"]
    H --> I["Productized Skills System"]
    I --> J["GitHub / Portfolio Release"]

    F --> K["Debug Notes"]
    K --> D
    K --> G

    E --> L["Panel Summary + Summary JSON"]
    L --> F
```

## Reading the map

The workflow starts with spatial intent, not with code. Data and rules make the intent explicit. Codex can then generate first-pass GH Python cells, but Rhino/GH preview and human validation decide whether the output is usable. Complex building generators are treated as a separate loop because facade logic and visual quality require a different level of judgment.

