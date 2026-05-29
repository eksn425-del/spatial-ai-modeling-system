# GH Component Checklist

- Component has a narrow responsibility.
- Inputs are named before code is written.
- Outputs are named before code is written.
- Python variables match GH output ports exactly.
- Every output variable is initialized.
- `try/except` exists.
- `warnings` output exists.
- `summary` output exists and is valid JSON.
- `geometry_counts` exists inside summary.
- Panel is connected to `summary`.
- Each geometry output can be connected to a separate Custom Preview.
- `all_breps` is not the only preview path.
- Python component default Preview is disabled when it conflicts with Custom Preview.

