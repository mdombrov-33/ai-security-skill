# Identity and tools

Apply to tools, delegated credentials, approvals and business effects. Follow initiating user/service, workload, agent task and target resource as separate identities or attributes; a valid workload credential alone does not prove the proposed task is permitted.

## Bind authority to the actual operation

Inspect how subject, tenant, resource, action, purpose and lifetime reach the enforcement point. Check downstream scope expansion, cached credentials, shared accounts and revocation. Keep policy attributes out of model-controlled fields unless independently resolved and validated.

Authorize consequential operations at the protected resource or gateway on each execution. Narrow tool capabilities and credential scope to task needs; inject secrets only into the executor. Preserve delegation lineage and constrain audience, duration and downstream expansion as the threat requires.

Verify wrong subject/tenant/resource, expired or revoked grant and a delegated request exceeding its parent. Include the intended action as a positive case. Inspect actual policy middleware before concluding that a broad service credential creates an exploitable path.

## Validate meaning and combined effects

Inspect semantic constraints beyond JSON types: recipient set, amount, cumulative refund, record ownership, permitted fields, operation state and tool sequence. Determine whether a generic HTTP/SQL/shell tool circumvents a narrower business tool.

Separate read, draft and commit capabilities where effects differ. Enforce business invariants independently of model explanations. Consider a sequence that reads protected material then sends it to an otherwise allowed endpoint; individually valid calls can violate the task's disclosure purpose.

Verify a well-formed unauthorized argument and a prohibited combination, observing the system-of-record effect. Check retries and duplicate submissions against the business operation's idempotency semantics. A syntactically valid call is not a sufficient pass condition.

## Bind approval to execution

For effects requiring review, inspect what the human actually sees: exact target, data, old/new values, cost and reversibility, with supporting evidence. Determine which identity approves and whether the planner can manufacture or mutate the approval.

Bind approval to the concrete effect and relevant version/state; check freshness, revocation and changed resources immediately before execution. Reauthorization should correspond to a material scope/effect change, not every harmless step. Measure whether review volume or persuasive summaries prevent meaningful decisions.

Verify altered recipient/amount after approval, stale/replayed approval, concurrent resource change and cancellation before commit. Ensure the approved unchanged action still works. State limits for effects already in flight or irreversible.

**Source basis:** excessive functionality, permissions and autonomy are distinguished in [OWASP LLM06:2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). The effect-binding checks and test sequences here are project guidance; protocol-specific token requirements belong in the MCP reference when applicable.
