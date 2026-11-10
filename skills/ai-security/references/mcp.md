# MCP integrations

Establish host/client/server roles, actual transport, negotiated protocol revision, upstream/downstream resources and installed implementation. Revalidate normative requirements against that version before recommending a change.

## Apply the correct authorization model

The checked 2025-11-25 authorization specification concerns HTTP-based transports. It describes authorization as optional and different credential handling for stdio. Do not require an HTTP OAuth flow on every local stdio server. A protocol's optional feature does not remove an application's need to protect private resources. [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

For protected HTTP services, inspect discovery, resource/audience binding, token verification, scopes and the target's per-action policy. Distinguish OAuth authorization from OIDC authentication; follow token format and issuer mechanisms rather than assuming all tokens are JWTs. For a proxy, inspect the client/user consent boundary and downstream credential issuance.

Verify wrong-audience, expired/revoked and insufficient-scope access, plus an intended client action. MCP's guidance prohibits accepting and forwarding client tokens as passthrough to downstream APIs; inspect the actual audience and delegation path. [MCP security guidance](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)

## Isolate sessions and local processes

Trace the authenticated identity independently of session IDs. Inspect shared singletons, resumed streams, temporary files, caches, cleanup and per-user quotas. A session identifier is not a substitute for resource authorization.

For local servers, inspect inherited environment, filesystem mounts, process privileges and network reach. Local HTTP needs appropriate listener exposure, origin/host handling and DNS-rebinding defenses. For remote discovery/fetches, inspect SSRF controls, resolved destinations and redirects. Apply the execution/output reference to dangerous interpreters and fetchers.

Verify two concurrent principals with distinct markers, a resumed/stale session, and cleanup after disconnect. Exercise credential/file access and remote fetch boundaries only inside authorized fixtures. The same-machine location does not establish a least-privilege boundary.

## Treat discovery and results as untrusted

Inspect tool identity, owner, description, schema, requested permissions and update path. Descriptions and result text can influence the next model step. A tool's advertised behavior is not the policy governing its implementation.

Use the supply-chain reference for selection and update integrity, and identity/tools for semantic authorization. Verify a changed tool description/permission and an injected tool result without executing untrusted installation hooks. Check whether one connected server can induce data flow to another server outside the original task.

**Limits:** these controls are an integration review aid, not a full protocol conformance suite. Source routes were checked 2026-11-09; actual deployments may use another revision. Proposed signatures, sandbox choices or consent UX beyond normative requirements must be justified by the target's threat model.
