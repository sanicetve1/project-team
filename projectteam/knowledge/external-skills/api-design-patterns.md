# API Design Patterns (Imported Skill Notes)

Source: `D:\Projects\everything-claude-code\skills\api-design\SKILL.md`

Use this to produce meticulous, consistent REST APIs.

## URL / resource conventions
- Resources are **nouns**, **plural**, **lowercase**, **kebab-case**.
- Prefer nested resources to express ownership (sparingly).
- Avoid verbs in URLs; use sub-actions only when not CRUD.

## HTTP methods and status codes
- **GET** safe + idempotent (read)
- **POST** create/trigger (non-idempotent unless idempotency key)
- **PUT** full replace (idempotent)
- **PATCH** partial update (make idempotent if needed)
- **DELETE** idempotent delete

Status codes:
- 200 OK, 201 Created (+ Location), 204 No Content
- 400 bad request, 401 unauthorized, 403 forbidden, 404 not found, 409 conflict, 422 semantic invalid, 429 rate limit
- 500/502/503 server/upstream

## Response envelope
Prefer a stable envelope (esp. public/partner APIs):
- Success: `{ "data": <T>, "meta"?: ..., "links"?: ... }`
- Error: `{ "error": { "code": "...", "message": "...", "details"?: ... } }`

## Error schema (field-level details)
Use a single error schema across services. Include correlation ID for support.

## Pagination
- Use cursor pagination for large datasets where possible.
- If offset pagination is used, document limitations and ordering.

## Filtering/sorting
- Use query parameters for filtering.
- Use a single `sort=` param (e.g. `sort=-created_at`).

## Rate limiting
- Document limit type (per-IP/per-user/per-token) and responses (429 + retry-after).

## Idempotency
For POST endpoints that create state:
- Require `Idempotency-Key`
- Store key + request hash + response for TTL
- Return the same result for retries

