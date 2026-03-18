# Security Threat Checklist (Architecture Skills)

Use this to populate the Security Architecture threat table with concrete items.

## Core threat categories to cover (8+)
1) **Broken authn**: weak password reset, token leakage, missing MFA option
2) **Broken authz**: IDOR, missing ownership checks, role escalation
3) **Injection**: SQL/NoSQL injection, command injection via tool inputs
4) **XSS/CSRF**: web client risks, cookie/session misconfiguration
5) **Secrets exposure**: leaked keys in logs/repos, weak rotation, over-privileged secrets
6) **API abuse**: rate-limit bypass, scraping, enumeration, brute force
7) **Data leakage**: PII in logs, over-broad analytics, insecure object storage buckets
8) **Supply chain**: vulnerable dependencies, CI compromise
9) **AI-specific** (if AI-centric): prompt injection, tool abuse, data exfiltration via tools, jailbreaks

## Mitigation checklist
- Auth:
  - OIDC/OAuth2, short-lived access tokens, refresh token rotation
  - centralized auth middleware + per-endpoint authorization rules
- Input validation:
  - schema validation for every request and tool input
  - allowlists for tool parameters
- Secrets:
  - managed secret store, rotation schedule, least privilege IAM
- Logging:
  - PII redaction, access control to logs, retention policy
- Abuse controls:
  - rate limiting per user/IP, WAF rules, bot detection (if needed)
- AI controls:
  - tool allowlists, sandboxing, policy checks before executing tools
  - safe browsing / URL allowlists if the agent fetches content

