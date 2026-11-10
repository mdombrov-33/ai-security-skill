# Evaluating the skill

The initial executable target is the synthetic RAG fixture. `tests/test_rag_fixture.py` verifies the fixture's actual boundaries; it does not grade an agent or model. Task cases are in `cases/`, and answer keys are isolated in `rubrics/`.

## Run a behavioral review

1. Copy `fixtures/rag/common.py`, its README and exactly one selected variant into a new temporary directory. Name the variant `service.py`. Do not expose tests, other variants or the rubric to the tested agent.
2. Start a fresh session with scoped local read/execution tools. Supply the request in `cases/rag-review.json`; for the skill condition, include the installed skill path and ask it to use that skill. Withhold `suggested_references` as well as the rubric so routing is exercised.
3. Capture the report and observable tool activity. Record loaded references, host/model identifiers, settings available, permissions, fixture digest, trial count, tokens and elapsed time. Unknown fields should be explicitly unknown.
4. Grade afterward using the rubric. Confirm code locations and effects, count missed/false findings and scope violations, and distinguish actual observed output from proposed tests.
5. Repeat with the other variant and without the skill, keeping permissions/model/task constant. Reset state each trial. Keep local outputs in ignored `local-results/` until sanitized for publication.

Repeat trials before comparing conditions. Add held-out cases before drawing conclusions about generalization; this fixture was used during development.

## Evaluate the skill separately from the target

The fake model deliberately returns chosen outputs or echoes its input. That tests what application controls do if model intent is compromised; it does not estimate real-model prompt-injection success. Judge application evidence and the reviewing agent's conduct separately.

Use deterministic probes for exposure, rendering, state, tools and resource limits. Human-review severity, causal reasoning, remediation fit and uncertainty. An LLM judge may assist, but should not be the only oracle for critical results.

## Observed development results

On November 9, 2026, two fresh agent sessions reviewed separate variants with the skill and without access to the rubric. The vulnerable-variant review identified the five seeded defects. The protected-variant review found an additional defect: summarizing an existing summary dropped its earlier source dependencies. Revoking access to an earlier source therefore failed to prevent its content from being replayed.

A regression test reproduced the failure. The fix retains dependencies from the prior summary whenever that summary is supplied to the model. The same reviewer retested the fix, confirming both revocation and legitimate summary reuse. Run `npm test` to exercise the seven deterministic fixture tests, including `test_revocation_survives_repeated_summarization`.

These were development smoke tests, not a controlled model comparison. There was one initial review per variant, no no-skill baseline, and no recorded model/configuration manifest. The entrypoint was subsequently shortened; the revised wording has not received a fresh behavioral evaluation. The tests establish fixture behavior, not a prompt-injection prevention rate or skill reliability score.

On November 10, Skills CLI 1.7.6 discovered the skill and displayed its interactive agent picker. A separate project-scoped copy installation for Codex completed in a temporary directory; all 14 installed files matched the source. Local Markdown links were also checked. This verifies packaging and installation, not automatic invocation or model behavior inside an installed host.

## Evidence to collect next

Publish raw counts and configuration, with honest limits. Track consequential defects found and missed, unsupported high-severity findings, benign task preservation, reference selection, instruction-token cost and out-of-scope reviewer actions. Investigate every critical miss or unauthorized effect rather than hiding it in an aggregate score.

Automatic discovery and installed-host behavior require their own tests. Static metadata validation and explicit invocation do not prove either.
