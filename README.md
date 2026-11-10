# AI Security

An agent skill for reviewing, designing and securing AI applications. Covers prompt injection, RAG, memory, tool permissions, MCP, code execution and data leaks. Loads detailed guidance only when the task needs it.

## Install

Run this from the project where you want to use the skill:

```sh
npx skills@latest add YOUR_GITHUB_OWNER/ai-security-skill
```

Choose your agent and **project** installation in the terminal. Requires Node.js 22.20+. You do not need to clone this repository or run `npm install` first.

The repository address above is a placeholder until publication.

Then ask your agent:

```text
Use ai-security to review this project for AI security issues.
```

## Sources

Based on OWASP's LLM and agentic security guidance, the MCP specification, and published practitioner research. See [sources and attribution](SOURCES.md) for links and editions.
