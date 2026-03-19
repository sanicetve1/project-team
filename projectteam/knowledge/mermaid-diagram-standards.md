# Mermaid Diagram Standards (Architecture Skills)

Use this to enforce syntactically-correct Mermaid output for component/deployment diagrams.

## Code fence rules
- Use Mermaid code fences exactly:
  - Start: ````mermaid
    ```mermaid
    ```
  - End: a plain closing fence ````` (no language tag)
- Never put any prose inside a Mermaid block; only node/edge declarations.

## Diagram type rules
- Component Diagram: use `graph TD;` or `flowchart TD;`
- Deployment Diagram: use `graph TD;` or `graph LR;`
- Keep it to ONE `graph` definition per Mermaid block.

## Node/edge syntax rules
- Node IDs (left side like `A`, `API`, `DB`) must be simple: `[A-Za-z0-9_]+` (no spaces or hyphens).
- Node labels (inside `[]`, `()`, etc.) can contain spaces.
- Common shapes:
  - Rectangle: `A[Label]`
  - Rounded: `A(Label)`
  - Stadium: `A((Queue))` (use consistently for DB/vector/queues if you want)
  - Subgraph (optional): `subgraph Name ... end`
- Edges:
  - `A --> B`
  - `A -->|HTTPS| B` (use quotes only if needed)

## Quick validity checklist
- Every node referenced in an edge is declared once.
- Mermaid block opens and closes properly (no missing closing fence).
- No markdown backticks appear inside the Mermaid block.

