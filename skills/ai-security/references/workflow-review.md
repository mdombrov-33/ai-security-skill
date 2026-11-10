# Review an AI system

## Scope and map

Establish whether the request concerns a diff, component, architecture or deployed system. Record the version and accessible evidence. Trace callers and downstream sinks of a focused change; explain any boundaries outside the review. For a broad review, use the entrypoint's surface inventory and account for unknown deployment behavior.

Identify the initiating subject and allowed objective. Follow representative input through context assembly, retrieval/memory, model proposal, authorization, tool execution, rendering and stored state. Record the authority actually exercised, including shared accounts, retries and fallback routes. Diagram data and authority separately when they diverge.

## Investigate consequential paths

For each applicable boundary, form a causal hypothesis with a concrete attacker capability and possible harm. Find the controlling implementation and its callers. Check whether the apparent protection acts before exposure/effect, applies on alternate paths, and is independent of the model it constrains.

Verify guard placement through code and scoped local tests when authorized. Use synthetic markers and sinks. Distinguish a proven control bypass from a stochastic claim that a particular model will select it. An assumed-malicious model output is useful for testing the application's containment; label that assumption.

Check secure alternatives before reporting: middleware, row-level policy, deployment network restrictions and execution gateways may supply controls outside the first file inspected. Lack of access to those artifacts creates an evidence gap. A concrete request path that bypasses them creates a finding.

## Prioritize and report

Rank reachable confidentiality, integrity, availability and authority failures ahead of hypothetical weaknesses. Capture prerequisites, tenant/resource scope, persistence, propagation and reversibility. Treat severity and confidence independently; label uncertain exploitability rather than asserting it.

For each finding, provide its location, causal path, impact, owning enforcement point and a verification method. Include important existing controls and explain why they are insufficient. Consolidate symptoms sharing one root failure while retaining distinct affected paths.

Finish with coverage and untested assumptions. A negative finding applies only to the inspected scope. A review is complete when every applicable surface is inspected or explicitly unresolved, and every claimed issue has supporting evidence and an actionable correction. Do not convert a review into edits unless the user requested implementation.
