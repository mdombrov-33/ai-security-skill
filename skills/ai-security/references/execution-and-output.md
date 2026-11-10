# Execution and output

Apply wherever model-influenced values reach an interpreter, filesystem, network, browser or generated artifact. Follow actual sinks, including client rendering that causes network activity without a tool call.

## Constrain the interpreter

Inspect shell construction, subprocess arguments, SQL, templates, deserialization, evaluators, paths and URL fetchers. Prefer typed/parameterized APIs and semantic allowlists suited to the operation. Shell avoidance alone does not prevent dangerous program arguments; SQL parameters do not authorize selected records.

For paths, inspect canonical resolution, symlinks, special files and races against the permitted workspace. For URLs, inspect scheme, host, port, resolved IP and every redirect; hostname string matching alone may allow internal destinations. Keep resource authorization separate from safe parsing.

Verify a model-derived input that tries to escape each relevant sink and a legitimate value that must work. Observe executed arguments, resolved path/destination or database effect. Avoid declaring exploitability from a dangerous function name without its reachable inputs and surrounding controls.

## Isolate generated computation

Inspect the executor's effective filesystem, environment, credentials, user privileges, network/DNS, metadata access and resource limits. A disposable worktree does not isolate host secrets; a container's strength depends on configuration, mounts and runtime boundary.

Separate proposal generation from execution. Choose isolation proportionate to hostile code: task-scoped writable storage, minimal privileges, bounded resources/lifetime, constrained egress and credentials issued only where required. Keep enforcement and essential telemetry outside the code's control.

Verify controlled reads/writes outside scope, an unauthorized destination, resource exhaustion and persistence after termination. Use safe fixtures or approved sandbox tests; a shell smoke test is not proof against all escapes. Capture actual configuration and residual host assumptions.

## Render and export safely

Inspect how model output becomes HTML, Markdown, email, links, spreadsheets, downloads or documents. Encode/sanitize for the actual destination. Active content and remote images can disclose data or impersonate trusted UI; a CSP or image proxy must be checked for its actual restrictions and data flow.

Verify a synthetic canary in a remote-image URL, active HTML, unsafe protocol and spreadsheet formula where supported. Observe renderer/network behavior, not only displayed text. Plain-text rendering can be a useful constrained option when rich content is unnecessary; maintain required legitimate formatting with a tested sanitizer when it is needed.

**Source basis:** downstream interpreter risks and context-specific output handling are described in [OWASP LLM05:2025](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/). Sandbox selection, race checks and fixture oracles here are project engineering decisions.
