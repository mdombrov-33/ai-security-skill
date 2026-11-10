# AI Security

**Review and harden LLM apps, RAG pipelines and tool-using agents with your coding agent.**

An installable skill that follows untrusted input through your application: what reaches the model, what tools it can call, what survives in memory, and what its output can do. It directs the agent to inspect the code, trace reachable failures, and propose fixes with tests.

## Install

Run this from the project you want to work on:

```sh
npx skills@latest add mdombrov-33/ai-security-skill
```

Choose your agent and **project** installation in the terminal. Requires Node.js 22.20+. No repository clone or separate `npm install` needed.

Then ask:

```text
Use ai-security to review this project for AI security issues.
```

In Codex, you can also invoke it explicitly with `$ai-security`.

## What you can ask it to do

| Task | Example request | Expected output |
|---|---|---|
| **Review** | “Review this RAG service for cross-tenant data leaks.” | Findings with code locations, attack paths, impact and verification steps. |
| **Design** | “Threat-model an assistant that can issue refunds.” | Data and permission flows, enforcement points and acceptance tests. |
| **Fix** | “Fix this memory-poisoning issue and test the change.” | A scoped implementation, a regression test and a check that legitimate behavior still works. |
| **Test** | “Build adversarial tests for this MCP integration.” | Cases with attacker capabilities, observable failures and benign controls. |

Use it on an existing repository, a proposed architecture, a focused change or an incident trace. A narrow request follows the affected path; a broad review checks each applicable surface.

## What it looks for

| Surface | Questions the skill directs the agent to investigate |
|---|---|
| **Prompt injection** | Can documents, tool results or other untrusted content redirect the task? What consequences can follow? |
| **RAG and private data** | Are permissions checked before data reaches the model, including through caches, rerankers and fallbacks? |
| **Memory and summaries** | Can untrusted content become policy? Do tenant boundaries and source revocation survive repeated summarization? |
| **Tools and approvals** | Is the exact action authorized for this user and resource? Can arguments change after approval? |
| **MCP** | Are tokens bound to the intended audience, sessions isolated and tool descriptions treated as untrusted? |
| **Code and output** | Can generated commands, HTML, URLs or file paths escape their intended boundaries? |
| **Supply chain** | Can a changed package, model, skill or tool manifest introduce new authority or executable behavior? |
| **Runtime and recovery** | Do budgets cover retries and delegated work? Can cancellation stop a pending action and recovery clear poisoned state? |

For example, filtering citations **after** generation does not prevent unauthorized documents from entering the model request. The review should identify where access is actually enforced and test what reaches that boundary.

Findings must distinguish observed defects from hypotheses and missing evidence. Existing controls matter; an undocumented control is not automatically an absent one.

## Small context, focused guidance

One skill, four workflows and eight topic references. The [entrypoint](skills/ai-security/SKILL.md) directs the agent to read the workflow and topics relevant to the task.

The installed skill contains instructions and reference material. It has no executable hooks, API keys or required hosted service. Development fixtures stay outside the installed directory.

## Sources

Built from OWASP's LLM and agentic security guidance, the MCP specification, research and practitioner publications. The [bibliography](SOURCES.md) lists 32 publications, their editions and contributions, plus protocol references and further reading.

Recommendations distinguish protocol requirements from project guidance. The skill organizes that material around engineering decisions rather than asking the agent to load the entire bibliography.

[Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)

