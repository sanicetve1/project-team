# Infrastructure & Resilience Defaults (Architecture Skills)

Use these defaults to avoid hand-wavy infra/resilience sections.

## Deployment topology checklist
- Edge: CDN/WAF (if public), API gateway/ingress
- Compute: container runtime or serverless
- Data: primary DB, cache, object storage, vector store (if any)
- Async: queue/broker (if any)
- Observability: logs/metrics/traces sink

## Default timeouts/retries (override per integration)
Use explicit numbers in the architecture doc:
- **Internal API calls**: timeout 2s, retries 2 (jittered), circuit breaker on
- **External API calls**: timeout 4–8s, retries 2 for GET only; POST requires idempotency
- **LLM calls**: timeout 20–60s depending on streaming; retries 1 with backoff; fallback model
- **DB queries**: statement timeout 2–5s for OLTP paths; background jobs can be higher

## Circuit breaker defaults
- open after: 50% failures over 20 requests (or similar)
- half-open: 1 request per 10s
- close after: 10 consecutive successes

## Scaling knobs checklist
- API tier: HPA on CPU + request rate
- Workers: scale on queue depth or tool-call backlog
- DB: connection pooling, read replicas only when needed
- Cache: size + eviction policy + key TTLs

## Backup/restore checklist
- RPO:
- RTO:
- PITR enabled:
- restore tests cadence:

## Release/rollback checklist
- blue/green or canary:
- feature flags:
- DB migration strategy (expand/contract):

