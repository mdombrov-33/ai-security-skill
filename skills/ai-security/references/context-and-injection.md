# Context and injection

Apply when user input, retrieved material, tool observations, multimodal content or judges influence reasoning. Map both direct input and content an authorized user causes the system to fetch.

## Preserve origin across transformations

Inspect how trusted task/policy and untrusted content enter context. Follow parsing, OCR, chunking, summarization, concatenation and role assignment. Identify any transformation that turns source text into a policy message or strips origin/trust metadata. Consider instructions in code comments, email fields, image text, metadata and tool errors.

Keep the authenticated task and enforceable limits outside model-editable context. Use roles, labels and delimiters to communicate provenance, while retaining machine-readable origin and authorization where effects are decided. A string claiming administrator authority does not establish it.

Verify by placing an instruction in an otherwise legitimate source and inspecting the assembled context and proposed effects. Include one transformation and a later turn where relevant. Preserve the legitimate summary or extraction task. Distinguish “the instruction influenced the answer” from “the application released an unauthorized effect.”

## Evaluate containment after influence

Inventory what a compromised proposal can reach: private retrieval, outbound URLs/images, tool parameters, files, stored memory or expensive loops. Follow the applicable data, identity, execution and runtime references from the entrypoint. A refusal is not the only result worth observing; an allowed read followed by an allowed send can create an unauthorized combined disclosure.

Test an assumed-malicious model proposal directly against the boundary. If independent policy blocks it, record that protection even when a language-level attack succeeds. If the proposal is allowed, establish its prerequisites before claiming a real attack succeeded. Avoid rating harmless disclosure of a nonsecret system prompt like credential theft.

## Calibrate behavioral defenses

Inspect input/output filters, prompt hardening and judge placement. Determine what each observes, whether it runs before the relevant effect, and what happens on timeout. Check whether evaluated text can instruct the judge or whether all judges share the same input and failure mode.

Use variants tied to the same objective: encoded or multilingual content, split instructions, tool-result recursion, multi-turn escalation or modality changes. Include legitimate security discussion, source code and multilingual text to measure overblocking. Report exact model/configuration and observable effects rather than generalizing from one successful or unsuccessful phrase.

**Source basis:** indirect and multimodal delivery, consequence-dependent impact and imperfect prevention are described in [OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). The inspection sequence and test oracles above are this project's engineering synthesis.
