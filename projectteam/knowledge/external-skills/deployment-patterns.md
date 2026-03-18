# Deployment Patterns (Imported Skill Notes)

Source: `D:\Projects\everything-claude-code\skills\deployment-patterns\SKILL.md`

Use this to make Infrastructure/Deployment sections production-grade and specific.

## Deployment strategies (pick one and document)
- **Rolling (default)**: gradual replace; requires backward-compatible DB/API changes.
- **Blue/Green**: instant cutover; easiest rollback; costs 2x infra during deploy.
- **Canary**: small traffic first; requires metrics + traffic splitting; best for high-risk changes.

## Docker best practices
- Pin image versions (no `:latest`).
- Multi-stage builds to shrink images.
- Run as non-root user.
- `.dockerignore` to avoid sending `node_modules`, `.git`, etc.
- Add `HEALTHCHECK`.
- Secrets are injected (env/secrets manager), never baked into images.

## Health checks
Document:
- liveness endpoint (process alive)
- readiness endpoint (dependencies ready)
- dependency checks (DB connectivity optional for liveness; required for readiness)

## CI/CD checklist
At minimum:
- lint + typecheck + tests on PR
- build artifact
- security scanning (dependencies + container image)
- deploy gated by environment approvals
- rollback strategy defined

## Backward-compatible release patterns
- DB migrations use **expand/contract**.
- Feature flags for behavior changes.
- Avoid breaking API contracts during a rolling deploy.

