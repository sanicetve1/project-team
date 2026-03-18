# Security Review Checklist (Imported Skill Notes)

Source: `D:\Projects\everything-claude-code\skills\security-review\SKILL.md`

Use this to make Security sections detailed and actionable.

## Secrets management
- No hardcoded keys/tokens/passwords.
- Secrets come from env/secrets manager.
- Validate secrets exist at startup.
- `.env*` ignored; no secrets in git history.

## Input validation
- Validate every request with schemas (server-side).
- Validate file uploads (size/type/extension).
- Use allowlists where possible.
- Error messages must not leak sensitive data.

## SQL injection prevention
- Parameterized queries only.
- ORM/query builder used safely (no string concatenation).

## Authentication & authorization
- Prefer httpOnly cookies for web tokens.
- Explicit per-endpoint authorization checks.
- Ownership checks (avoid IDOR).
- Session/token lifetimes and rotation documented.

## XSS/CSRF
- Sanitize user-provided HTML.
- Use CSP.
- CSRF protections for cookie-based auth.

## Logging
- PII redaction rules.
- Access control for logs.
- Correlation IDs for incident response.

