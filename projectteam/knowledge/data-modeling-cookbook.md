# Data Modeling Cookbook (Architecture Skills)

Use this to make `## 7. Data Architecture` concrete and implementation-oriented.

## Entity schema rules
- Name entities using domain nouns in `PascalCase` (e.g., `TravelGoal`, `Itinerary`, `Payment`).
- For each top entity provide:
  - Primary key (PK) type (e.g., `uuid` / `bigint`) and name
  - Core fields (5-10 key fields) with data types
  - Uniqueness constraints (e.g., unique email per tenant)
  - Ownership (which module/service owns writes)
- Prefer explicit timestamps:
  - `created_at`, `updated_at`
  - For auditability: `deleted_at` (soft delete) or `archived_at`

## Relationship rules
- Describe cardinalities explicitly:
  - `User 1:N TravelGoal`
  - `TravelGoal 1:N Itinerary`
  - `Itinerary 1:N Activity`
- For relationships, define:
  - Foreign key fields
  - Cascade behavior (usually restrict; avoid cascades for safety)
  - Indexes supporting common queries (e.g., `(user_id, start_date)` for feed)

## Data lifecycle and retention
- For each entity state what happens on:
  - Create (source module)
  - Update (idempotent keys if relevant)
  - Archive/delete policy
- If the system stores AI artifacts:
  - Keep prompt/response logs short-lived by default
  - Store embeddings in vector store with a stable embedding-key and metadata pointers

## Validation and constraints
- Validation: application-level schema validation + database constraints.
- Use:
  - NOT NULL where appropriate
  - CHECK constraints for bounded numeric ranges
  - Foreign keys for referential integrity

## Migration strategy defaults
- Schema evolution pattern:
  - Backward compatible migrations first (expand, then write, then contract)
  - Use safe defaults for large tables (batching, lock timeouts, online index creation)
- For AI/vector stores:
  - Version embeddings with `embedding_model_version`
  - Rebuild embeddings asynchronously when model changes

