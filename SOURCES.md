# Sources

The bibliography behind the skill's security guidance, including background on evaluation, governance and procurement. Topic references cite the sources relevant to their recommendations; this list is not a claim of complete framework coverage.

## OWASP publications

| Publication | Edition | Contribution |
|---|---|---|
| [Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | 2025 | Application risks: injection, disclosure, output handling, agency, retrieval, supply chains and consumption. |
| [Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 2026 | Agent-specific risks, identity, memory, tools, delegation and cascading effects. |
| [Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) | 1.1, December 2025 | Threat taxonomy, reference architecture and mitigation playbooks. |
| [Securing Agentic Applications Guide](https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/) | 1.0, July 2025 | Architecture, capabilities and controls across design, development and operations. |
| [A Practical Guide for Secure MCP Server Development](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/) | 1.0, February 2026 | Authorization, sessions, tool interfaces, validation and deployment hardening. |
| [GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/) | 1.0, January 2025 | Engagement scope, test layers, methodology, reporting and metrics. |
| [State of Agentic AI Security and Governance](https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/) | 2.01, June 2026 | Agent identity, autonomy, adoption, governance and deployment evidence. |
| [AI Security Solutions Landscape for AI and Agentic Red Teaming](https://genai.owasp.org/resource/ai-security-solutions-landscape-for-ai-and-agentic-red-teaming-q2-2026/) | Q2 2026 | Evaluation capabilities and tool categories; a dated landscape, not a product recommendation. |
| [AI Security Solutions Landscape for Agentic AI](https://genai.owasp.org/resource/ai-security-solutions-landscape-for-agentic-ai-q2-2026/) | Q2 2026 | Security capabilities across the agent lifecycle. |
| [GenAI Security Project Consolidated Roadmap](https://genai.owasp.org/roadmap/) | Q1 2026 snapshot | Relationships between community workstreams. Planned work is not a security requirement; the linked page tracks subsequent roadmaps. |

## Research and training

| Publication | Author / edition | Contribution |
|---|---|---|
| [MAESTRO: Multi-Agent Evaluation Suite for Testing, Reliability, and Observability](https://arxiv.org/abs/2601.00481) | Tie Ma et al., January 2026 | Reproducibility, execution traces, failure analysis and resource measurements in multi-agent systems. This is the evaluation suite, not the CSA threat-modeling framework with the same name. |
| Certified LLM Security Expert (CLLMSE): Official Study Handbook | Joas A. Santos, version 1.0 | Attack families, privacy, identity, agent architecture, lifecycle security and defense. |
| Certified LLM Security Professional (CLLMSP): Official Study Guide & Reference Handbook | Red Team Leaders, version 1.0, 2026 | LLM foundations, application security, MCP, testing, deployment and governance. |

The handbooks are training material, not standards. Titles without links are retained for attribution where a stable publication URL has not been verified.

## Lakera practitioner guides and reports

| Publication | Contribution |
|---|---|
| [Prompt Injection Attacks Handbook](https://www.lakera.ai/ai-security-guides/prompt-injection-attacks-handbook) | Direct and indirect delivery, evasion, layered defenses and evaluation material. |
| [Understanding Prompt Attacks: A Tactical Guide](https://www.lakera.ai/ai-security-guides/understanding-prompt-attacks-a-tactical-guide) | Attack anatomy, conflicting instructions, objectives and severity. |
| [Prompt Attacks: What They Are and What They're Not](https://www.lakera.ai/ai-security-guides/prompt-attacks-what-they-are-and-what-theyre-not) | Distinguishing instruction manipulation from harmful content. |
| [How to Craft Secure System Prompts for LLM & GenAI Applications](https://www.lakera.ai/ai-security-guides/crafting-secure-system-prompts-for-llm-and-genai-applications) | Prompt design as one defensive layer; application authorization remains separate. |
| [Securing AI Agents in Production: A Practical Guide](https://www.lakera.ai/ai-security-guides/securing-ai-agents) | Planner/executor separation, least privilege, context, memory, tools and observability. |
| Agentic AI Security: The Enterprise Playbook | Workforce AI, applications, agents and consistent policy across their data and action paths. |
| [LLM Security Playbook](https://www.lakera.ai/ai-security-guides/llm-security-playbook), version 2 | Early practitioner taxonomy, leakage, downstream actions, monitoring and datasets. |
| [AI Security Guide](https://lakera-marketing-public.s3.eu-west-1.amazonaws.com/Lakera_AI_Security_Guide_2024.pdf), 2024 | Foundational risk, controls, secure lifecycle and organizational practice. |
| AI Security for Product Teams Handbook | Security across product development, ownership, evaluation and user communication. |
| Real World LLM Exploits, January 2024 | Case studies involving unsafe HTML, indirect injection, poisoned data and image-based exfiltration. |
| [Q4 2025 AI Agent Security Trends](https://www.lakera.ai/ai-security-guides/q4-2025-ai-agent-security-trends) | Vendor observations of leakage, reconnaissance, script injection and attacker behavior. |
| AI Red Teaming: Insights from the World's Largest Red Team | Scenario development, manual and automated testing, and recording results. |
| Building AI Security Awareness Through Red Teaming with Gandalf | Guardrail bypasses, layered controls and the limits of defensive assumptions. |
| [Decoding OWASP Large Language Model Security Verification Standard (LLMSVS)](https://www.lakera.ai/ai-security-guides/decoding-owasp-large-language-model-security-verification-standard-llmsvs) | Orientation to verification requirements, assurance levels and self-assessment. |
| The AI Risk Map | Connections among threat taxonomies, controls, governance and lifecycle responsibilities. |
| [Navigating AI Governance: EU AI Act vs. White House's AI Bill of Rights](https://www.lakera.ai/ai-security-guides/navigating-ai-governance-eu-ai-act-vs-white-houses-ai-bill-of-rights) | Historical governance comparison; not a source for current legal requirements. |
| How to Choose the Best GenAI Security Solution: Key Factors to Consider | Coverage, integration, privacy, performance and supplier evaluation questions. |
| Build vs. Buy Guide | Cost, maintenance, expertise, deployment time and coverage tradeoffs. |
| LLM Security Solution Evaluation Checklist, version 2 | Model support, testing, data handling, monitoring and integration questions. |

These are practitioner and vendor publications. Their examples inform engineering judgment; product claims and telemetry are not independent benchmarks. Linked landing pages may offer a different edition from the one named here.

## Protocol and packaging references

- [MCP Authorization, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) and [Security Best Practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices): transport-specific authorization, token audiences, sessions and confused deputies. Check the revision deployed by the target system.
- [Agent Skills specification](https://agentskills.io/specification): skill format and supporting resources.
- [Skills CLI](https://github.com/vercel-labs/skills): discovery and installation.

## Further reading

For deeper investigation beyond the bibliography above:

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): organizational AI risk management and links to the Generative AI Profile.
- [MITRE ATLAS](https://atlas.mitre.org/): adversarial tactics and techniques against AI systems.
- [OWASP LLMSVS](https://owasp.github.io/www-project-llm-verification-standard/LLMSVS-v2.0-en.html): primary verification requirements, rather than a vendor's summary.
- [Not what you've signed up for](https://arxiv.org/abs/2302.12173), Greshake et al., 2023: research on indirect prompt injection in integrated applications.
- [Simon Willison on prompt injection](https://simonwillison.net/tags/prompt-injection/) and [Johann Rehberger's Embrace The Red](https://embracethered.com/blog/): ongoing analysis and exploit research.

## Attribution and maintenance

Publication identities and available links checked November 10, 2026. Editions are preserved rather than silently treating a newer web page as the same document. Links do not imply clause-level verification or endorsement.

The skill's workflows, inspection sequences and synthetic tests are original project work. Source publications retain their own licenses; PDFs and third-party datasets are not bundled. When adding guidance, cite the primary source near the recommendation and distinguish its requirements from project recommendations.
