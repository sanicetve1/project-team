# Architecture Assembly Rubric (Architecture Skills)

Use this to make the assembler and reviewer outputs consistent and template-compliant.

## Template fidelity rules (HARD)
- Preserve all `##` sections and headings/subheadings exactly as in the template.
- Do not remove template tables; keep their header rows unchanged.
- If a specialist spec conflicts, choose the most internally consistent set and record the assumption in the relevant section.

## Required artifacts (HARD)
- `## 4. Application Architecture`
  - Component Diagram mermaid block present and syntactically valid.
- `## 8. API and Integration Architecture`
  - Endpoint catalog table present with header + separator rows.
- `## 9. Security Architecture`
  - Threat table present with header + separator rows and >= 8 threats.
- `## 10. Infrastructure Architecture`
  - Deployment Diagram mermaid block present and syntactically valid.
  - Resilience defaults table present with header + separator rows.
- `## 11. Observability Architecture`
  - SLI/SLO table present with header + separator rows and >= 6 rows.
- `## 12. Quality Attributes and Architecture Decisions`
  - ADR table present with header + separator rows and >= 6 rows.

## Output formatting rules (HARD)
- The response must be raw markdown, not wrapped in a top-level ``` or ```markdown fence.
- The only allowed fenced blocks are:
  - Mermaid blocks (```mermaid ... ```).
  - No other ``` fences anywhere.

## Consistency checks
- Auth model consistency: API endpoint auth expectations match the security enforcement points.
- Data consistency: entities/relationships match the API resources and storage decisions.
- Diagram consistency: nodes/edges match the described components and tiers.

