# Memory and compaction

Apply to conversation summaries, checkpoints, preference stores, long-term memory, shared knowledge and feedback written for later use. Treat a memory write as a state-changing operation with its own authority.

## Control promotion and reads

Identify memory classes: raw observation, user assertion, model inference, preference and independently verified fact/policy. Trace authorized writers, readers, tenant/task scope, provenance and expiry. Check whether model output is automatically stored at a higher trust level or reused across subjects.

Keep derived summaries distinguishable from authoritative records. Enforce write/read policy in storage or its service. Attach source references, transformation/version, sensitivity and lifetime appropriate to the class. Identity, permission, financial and policy facts require an authorized source beyond a model's assertion that they are verified.

Verify unauthorized high-trust writes, cross-user reads and self-output reingestion. A legitimate preference update should still work while a preference claiming new permissions cannot create authority. Test subsequent tasks, not only the turn that wrote the value.

## Preserve constraints during compaction

Compare original and reduced state for task/resource scope, denied actions, tenant identity, expiry, untrusted-source labels, unresolved claims and evidence references. Check truncation and repeated summarization, including a handoff where the recipient lacks the original context.

Store enforceable authorization separately from summaries and revalidate at action time. A fluent summary is insufficient evidence that a grant survived correctly. Preserve source lineage so a claim copied through multiple agents does not become independent corroboration.

Verify a summary that omits an explicit denial, broadens recipients or upgrades an untrusted quote. Observe the continuation's requested and actual effects. Test that externally retained policy still blocks the action even if the summary is wrong. Label text-comparison evidence separately from downstream authorization evidence.

## Make poisoned state recoverable

Find how operators identify entries influencing an action and their derived caches, vectors, summaries and downstream artifacts. Inspect expiry, retention, deletion, quarantine, snapshots and rebuild paths. A raw-source deletion may leave a live derived instruction.

Exercise a synthetic poisoned entry: identify consumers, quarantine influence, rebuild from an authorized source and rerun the triggering task. Preserve forensic evidence with appropriate access and retention instead of deleting every trace. State effects that cannot be reversed.

**Sources:** [OWASP's Agentic Top 10, 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) provides background on agentic risks. The lineage checks, compaction comparisons and recovery tests here are project recommendations, supported by local regression tests, not a clause-level mapping to that framework.
