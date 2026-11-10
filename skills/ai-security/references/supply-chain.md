# AI supply chain

Apply to packages, models, adapters, prompts, skills, tool/MCP servers, registries, manifests, containers and hosted providers. Distinguish artifact identity from the authority and runtime behavior it receives.

## Establish provenance and exposure

Inventory exact selected versions/digests, acquisition sources, owners, update mechanisms and execution permissions. Include prompts, skill references and tool descriptions: a dependency scanner alone cannot evaluate malicious natural-language instructions. Determine whether loading a model or package invokes executable code or installation hooks.

Use trusted acquisition and integrity verification appropriate to the risk. Pin reproducible dependencies where supported, inspect permission requests and isolate evaluation of unfamiliar artifacts. A signature establishes a relationship to its signing identity; it does not prove benign behavior or that the signer is trusted for this task.

Verify a modified artifact or manifest, an unexpected permission request and a confused package/model identity. Retain known-good evidence. Do not execute untrusted setup scripts merely to complete a security review.

## Reassess changes in behavior and authority

Trace automatic updates, tool rediscovery, provider model aliases, fallback routing and prompt/policy changes. Compare evaluated and deployed versions, capabilities, destinations and data handling. A previously approved server can change while retaining its name.

Gate consequential changes through relevant tests and explicit authority review. Use staged rollout and a known-good rollback path where supported. When a hosted component cannot be pinned, record that limitation and monitor behavior/configuration changes instead of claiming reproducibility.

Verify an update that adds a new destination or tool scope, plus a legitimate compatible update. Observe whether old approval silently extends to the new authority. Check that disabling the component also revokes credentials and prevents rediscovery/reactivation.

## Keep the review and release chain trustworthy

Treat reviewed skill files, test payloads, copied instructions and tool outputs as untrusted artifacts. Preserve the authorized review objective and avoid leaking private code or traces into public reports. Track source evidence for normative claims and distinguish primary requirements, observations and project decisions.

For a public skill/package, inspect archive contents, relative reference resolution, executable helpers, dependencies and update instructions. Exclude private inputs and evaluator answer keys. Test clean installation and existing-install behavior; a failed or partial update should not erase user changes.

Verify artifact digests and repeat the relevant functional tests after packaging. Integrity checks, static scanning and behavioral tests support different claims and should be reported separately.

**Source basis:** model/data/package provenance and third-party risks are described in [OWASP LLM03:2025](https://genai.owasp.org/llmrisk/llm032025-supply-chain/). The skill-specific review and packaging controls here are project guidance.
