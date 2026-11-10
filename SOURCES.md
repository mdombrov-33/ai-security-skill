# Sources

The skill combines published guidance with original review workflows and tests. References cite the sources relevant to their topic.

| Source | Used for |
|---|---|
| [OWASP Top 10 for LLM Applications, 2025](https://genai.owasp.org/llm-top-10/) | Prompt injection, sensitive data, supply chains, output handling, excessive agency, retrieval and resource consumption. |
| [OWASP Top 10 for Agentic Applications, 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and [Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) | Background on persistent state, delegated authority and agent actions. |
| [OWASP GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/) | Evaluating model behavior, application implementation, infrastructure and runtime. |
| [MCP Authorization, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) and [Security Best Practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) | Transport-specific authorization, token audiences, sessions, confused deputies and local-server risks. |
| Lakera's [Prompt Injection Attacks Handbook](https://www.lakera.ai/ai-security-guides/prompt-injection-attacks-handbook) and [Securing AI Agents](https://www.lakera.ai/ai-security-guides/securing-ai-agents) | Practitioner perspectives on attack patterns and input, memory, retrieval and tool misuse. |

Source pages checked November 9–10, 2026. The agentic publications provide background, not a verified clause-by-clause mapping. Practitioner material does not establish independent product comparisons or this skill's effectiveness.

The workflows, inspection sequences and synthetic fixtures are original project work. Protocol requirements are distinguished from application recommendations; check the version deployed by the system under review.

The package follows the [Agent Skills specification](https://agentskills.io/specification) and installs through the [Skills CLI](https://github.com/vercel-labs/skills).

Linked publications retain their own licenses. Source PDFs and third-party datasets are not bundled. No affiliation or endorsement is implied.
