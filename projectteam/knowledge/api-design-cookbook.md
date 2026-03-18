# API Design Cookbook (Architecture Skills)

Use these conventions to keep API sections concrete and consistent.

## API conventions
- **Base path**: `/api/v1`
- **Resource naming**: nouns, plural, lower-case (`/users`, `/itineraries`)
- **HTTP methods**: GET=read, POST=create, PUT=replace, PATCH=partial update, DELETE=delete
- **Versioning**: URL versioning (`/v1`) + explicit deprecation policy

## Error model (standard shape)
Use a single JSON error schema across services:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": { "any": "json" },
    "correlationId": "string"
  }
}
```

Map errors:
- 400 validation error
- 401 unauthenticated
- 403 unauthorized
- 404 not found
- 409 conflict (idempotency/key collisions)
- 422 semantic/business rule failure
- 429 rate limit
- 500/503 server/downstream failure

## Idempotency
For POST endpoints that create state:
- Require `Idempotency-Key` header
- Store key + request hash + response for TTL
- Return same result for repeats

## Pagination
Prefer cursor pagination:
- Request: `?cursor=<token>&limit=50`
- Response: `{ "items": [...], "nextCursor": "<token>" }`

## Authn/Authz in APIs
- Include `Authorization: Bearer <jwt>`
- Define scopes/roles per endpoint in the endpoint catalog table
- Specify where enforcement happens (gateway vs service middleware)

## Timeouts/retries for outbound HTTP calls
- Always define timeouts for downstream calls
- Prefer retries only for safe idempotent operations (GET) or POST with idempotency keys

