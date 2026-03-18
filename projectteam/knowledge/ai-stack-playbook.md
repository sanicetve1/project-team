# AI Stack Playbook (Architecture Skills)

Use this as a checklist to make AI/LLM architecture decisions concrete and implementable.

## 1) Choose the LLM provider + model
- **Primary provider**:
- **Primary model**:
- **Fallback model**:
- **Reasoning**: latency, cost, reliability, regional availability, tool-calling support.

## 2) Orchestration strategy (pick one and commit)
- **Option A: Direct SDK + custom orchestration**
  - Use when flows are simple and you want minimal dependencies.
  - Required outputs: prompt templates, tool schema definitions, routing logic, retry/fallback policy.
- **Option B: LangChain**
  - Use when you want a mature tool abstraction layer and patterns for RAG/tools.
  - Required outputs: tool registry, prompt hub strategy, callbacks/telemetry hooks.
- **Option C: LlamaIndex**
  - Use when RAG/indexing is the core of the product.
  - Required outputs: index strategy, chunking, retrieval pipeline, evaluation harness.

## 3) RAG decision (only if needed)
RAG is not mandatory. Use it if:
- you must ground answers in company/product documents
- you need long-term memory over user or domain data
- you need citations or traceability

If using RAG, specify:
- **What is indexed**:
- **Chunking strategy**:
- **Metadata**:
- **Retrieval**: top-k, filters, re-ranking
- **Freshness**: update schedule, invalidation
- **Evaluation**: offline set + online monitoring

## 4) Tool calling strategy
Define:
- **Tool catalog**: tool name → purpose → external API → auth method → rate limit → timeout/retry
- **Validation**: schema validation on tool inputs/outputs
- **Idempotency**: for tools that create/update external state
- **Safety**: allowlist tools; denylist parameters; PII redaction rules

## 5) AI safety + governance (must be explicit)
- **Prompt/response logging**: what is stored, retention, PII handling, access control
- **Moderation**: where filters run (pre/post), how violations are handled
- **Cost controls**: per-user budgets, per-request caps, caching policy
- **Latency controls**: streaming, timeouts, fallback behavior

## 6) Observability for AI
Log and measure:
- prompt template version
- model name/version
- tool calls (name, latency, success/failure)
- token usage/cost estimate
- retrieval metrics (hit rate, top-k overlap) if RAG

