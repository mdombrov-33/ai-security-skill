# Design defensible AI capabilities

## Bound the capability

Translate the user's intended task into acceptable data access and effects. Capture identities, resources, data classes, tenant boundaries, persistence, autonomous duration, budget and irreversible actions. Infer what the artifacts establish; list missing decisions without demanding a questionnaire before useful design work.

Choose the least autonomous shape that delivers the requested behavior. An advisory response, a draft and a committed transaction require different authority. Keep the model's ability to interpret information separate from its ability to authorize effects.

## Draw the two flows

Map sources → parsing → context/retrieval/memory → model → downstream interpreters and outputs. Mark trust transitions and stored derivatives. Separately map initiating subject → workload/agent → delegated capability → protected resource. Identify where user intent is preserved, where authorization is checked, and how a delegation expires or is revoked.

For each consequential effect, specify:

- The exact allowed operation, resource and parameter constraints.
- The independent enforcement point and source of policy attributes.
- How approved inputs are bound to execution and rechecked against current state.
- Credential scope, execution isolation and cumulative resource limits.
- Failure behavior, observable evidence and recovery limitations.

Use the applicable domain references for detailed decisions. Treat model-based detection as a behavioral layer with measurable false positives and bypasses. Avoid making one model the sole authority over another model's effects.

## Test the design against abuse

Construct attack chains from actual exposed content and capabilities. Assume a model proposal has been influenced; determine what independent controls still hold. Include indirect input, a valid-looking unauthorized tool argument, compromised persistent state, a failed/retried operation and a cancellation/revocation race where applicable.

For every requirement, name an observable check and a legitimate task that must still succeed. Prefer “tenant B's bytes never enter tenant A's model request” over “prevent leakage.” Include response/recovery for risks that cannot be eliminated.

Finish with design choices, alternatives where material, testable requirements, residual risks and the unresolved facts that affect feasibility. The design is complete when each consequential effect has a control owner, enforcement point, failure behavior and acceptance check. Framework labels can explain coverage afterward; they do not replace the system-specific argument.
