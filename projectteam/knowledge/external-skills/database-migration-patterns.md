# Database Migration Patterns (Imported Skill Notes)

Source: `D:\Projects\everything-claude-code\skills\database-migrations\SKILL.md`

Use this to make Data/Infra sections safe for production evolution.

## Core principles
1) Every change is a migration (no manual prod edits).
2) Migrations are immutable once deployed.
3) Prefer forward-fix migrations over rollbacks in prod.
4) Separate schema migrations (DDL) from data backfills (DML).
5) Test migrations against realistic data volumes.

## Safety checklist
- New columns: nullable or have safe defaults.
- Avoid full table rewrites / long locks.
- Create indexes concurrently where supported.
- Document a rollback/forward-fix plan.
- Use batching for large data backfills.

## Zero-downtime schema changes (expand/contract)
- Add new column/table (expand)
- Backfill in batches (data migration)
- Deploy code reading/writing both
- Switch reads to new
- Stop writes to old
- Drop old (contract)

## PostgreSQL notes
- Avoid `NOT NULL` without defaults on large existing tables.
- Use concurrent index creation when needed (tooling must support it).

