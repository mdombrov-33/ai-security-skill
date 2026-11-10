# Harden an existing boundary

## Establish the failure

Inspect the target implementation, caller, effect and existing controls. Reproduce the issue with synthetic data when possible. If evidence supports only a hypothesis, say so and choose a check that distinguishes it from an already-protected path. Keep unrelated user changes intact.

Write the intended invariant and a legitimate use case before changing behavior. The invariant must describe data access, authority, persistence, resource use or a downstream effect rather than a particular payload phrase.

## Change the owning control

Prefer a focused correction where the boundary is enforced: authorized retrieval, resource-level policy, a narrow tool, a safe interpreter API, an independent execution gate, isolated state, or cumulative accounting. Read the relevant domains. Adding an instruction or detector alone does not repair missing application authorization.

Inspect related paths such as caches, rerankers, fallback providers, retries, background workers and callbacks. Fix paths inside the authorized scope; describe connected risks outside it. Use existing project conventions and infrastructure when they implement the required invariant. Avoid adding enterprise machinery to a small system without a demonstrated need.

## Verify both sides

Run a regression that would fail for the original defect and pass for the correction. Observe the actual boundary: model inputs, denied tool calls, scoped records, rendered content, state transitions or resource counters. Include nearby variants where the defect class warrants them, such as changed recipient, expired approval, cache hit, symlink or replay.

Run a benign case proving the legitimate task remains possible. Check expected failure behavior and error handling; a failing policy service must not silently release the previously blocked effect. Reuse the repository's required checks and relevant tests instead of repeatedly running unrelated suites.

## Complete the change

Report the changed behavior, why the control belongs there, executed validation and its result. Mark unrun production, provider or environment checks explicitly. State remaining exposure and deployment/migration requirements when material.

Completion means the identified invariant is enforced on the scoped paths and verification supports that claim. Preserve the user's existing authorization for implementation and local checks; ask only at a concrete action outside that scope. Do not infer permission to deploy, publish, message others or run live attacks from a request to fix local code.
