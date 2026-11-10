# Retrieval and data

Apply when the system handles private records, retrieval, vectors, caches or provider routing. Trace bytes before the model and after the answer, including intermediate rerankers, logs and derivatives.

## Authorize before exposure

Locate the authenticated principal and trusted tenant/purpose attributes. Follow query construction through candidate selection, reranking, content loading and model requests. Check that user/model-controlled metadata cannot choose a privileged tenant. Inspect caches, conversation reuse, direct document lookup and reference resolution for alternate paths.

Enforce record/chunk access in the data service before unauthorized content reaches a model or another external processor. Output filtering cannot retract exposure that already occurred. Cache scoping must reflect authorization, and permission changes need invalidation or current rechecks.

Verify with distinct synthetic tenant markers. Inspect model/reranker inputs as well as final output for direct and semantic queries, cache hits and access revoked mid-session. The permitted principal must still retrieve their own records. A shared service credential is not by itself proof of a leak if resource policy independently enforces the correct principal.

## Preserve source integrity

Inspect ingestion writers, parser isolation, origin identity, document/chunk metadata, version and promotion rules. Establish who can change retrievable evidence or ranking. Consider poisoned duplicates, stale documents and metadata tampering. Embeddings retain sensitive information; they are not an anonymization boundary.

Require attributable authorized writes and carry source identity and access labels through extraction and chunking. Stage/quarantine consequential updates according to their risk. A citation should resolve to an authorized passage that supports the claim; a real URL alone is insufficient.

Verify an unauthorized write and an authorized source with malicious content separately. Check stale/deleted source behavior and a citation that does not support the generated conclusion. Preserve legitimate contradictory evidence rather than hiding it through an oversimplified allowlist.

## Account for every disclosure destination

Map model providers, fallbacks, telemetry, errors, exports, caches and derived state. Compare actual data sent with approved purpose, retention and destination constraints. Keep secret material in the executor that needs it rather than in context; minimize unrelated personal data.

Check provider and region changes against current configuration/evidence. Verify removal across controlled source, vector, cache and memory paths; distinguish implemented deletion from a provider's contractual promise. Record uncertainty when provider behavior cannot be inspected.

**Source basis:** access restrictions and contextual sensitive-data risk appear in [OWASP LLM02:2025](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/); vector access, cross-context leakage and poisoning appear in [OWASP LLM08:2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/). Specific cache, revocation and input-boundary tests here are project guidance.
