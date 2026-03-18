# Knowledge Pack

These documents are curated “skills” for the architecture and review agents.

How they are used:
- The Architect and Architect Reviewer tasks are instructed to read these files via `FileReadTool` before producing the architecture document.
- The content is designed to be copied into the output as concrete defaults, checklists, and tables (not generic prose).

Files:
- `ai-stack-playbook.md`: LLM/RAG/tooling choices and defaults
- `api-design-cookbook.md`: API conventions, error model, idempotency, pagination
- `infra-resilience-defaults.md`: timeouts/retries/circuit breakers, scaling, deployment defaults
- `security-threat-checklist.md`: threat categories and mitigations to cover in the doc

