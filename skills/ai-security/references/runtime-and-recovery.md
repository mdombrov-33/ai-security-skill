# Runtime and recovery

Apply to autonomous loops, queues, retries, budgets, deployments, telemetry, cancellation and persistent effects. Inspect the running topology where accessible; source-level intent alone does not prove deployed enforcement.

## Bound cumulative work

Inspect per-user/tenant/task and global accounting for tokens, model/tool calls, retries, elapsed time, spend, memory writes and fan-out. Check admission before expensive work and accounting across fallback models, concurrency and delegated jobs. Per-call limits can coexist with an unbounded task.

Use finite limits appropriate to the task, reserve capacity before dispatch where races matter, and define failure behavior when accounting is unavailable. Apply backpressure, bounded retry and circuit breaking to prevent amplification. Preserve legitimate progress and state the behavior when a limit is exhausted.

Verify repeated equivalent failure, concurrent work and a costly fallback with small local limits. Observe cumulative effects and termination. A billing alert detects spend; it does not by itself enforce a cap.

## Make stop and revocation effective

Trace cancellation from user/operator to queued work, executors, retries and external commits. Determine what can already be in flight and which effects cannot be undone. Check that a stopped planner cannot leave active tools or credentials continuing independently.

Enforce cancellation/current authorization at execution boundaries; revoke relevant grants and prevent redispatch as required. Keep management controls independent of the model being stopped. Combine this with effect/approval binding from the identity/tools reference.

Verify cancel-before-dispatch, cancel-before-commit, repeated delivery and stale-worker completion. Record observed stop latency and unavoidable in-flight effects. A UI showing “cancelled” is not proof that the system of record remained unchanged.

## Preserve evidence and recover derived state

Inspect correlation of task, principal, source IDs, model/policy/tool versions, authorization decisions, approvals, effect results and memory lineage. Collect sufficient evidence outside the agent's control while minimizing prompt/secret retention. Raw prompt logging can create a new sensitive-data store and still miss the reason an effect was authorized.

For an incident, separate known events from inferred causality. Trace source influence into memory, summaries, caches, vectors and downstream artifacts. Prefer proportionate containment, credential/delegation revocation, quarantine and restoration from known-good state. Capture needed forensic evidence before destructive cleanup.

Verify a synthetic poisoned-state recovery and a version rollback, then rerun both the trigger and legitimate task. Confirm retired components lose credentials, registrations and scheduled work. Mark forensic/production actions outside current permission as proposed, while completing available analysis.

**Source basis:** financial and service impact from uncontrolled inference is covered by [OWASP LLM10:2025](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/). Cancellation races, correlation fields and recovery procedures here are project-authored system controls; they are not a complete incident-response or compliance standard.
