# Evaluate security behavior

## Specify the experiment

Determine whether the user wants a plan, fixtures or execution. For execution, establish the authorized target, test accounts/data, allowed effects, request/spend limits, stop conditions and evidence handling. Reuse authorization already provided. Prepare local simulations for effects outside that permission.

Define each case as an attacker capability, delivery path, invariant, observable failure and legitimate task. Distinguish model manipulation from application harm: a model may follow an instruction while a tool gateway correctly blocks its effect. Conversely, a polite answer may accompany a leaked model request, external image fetch or poisoned memory write.

## Cover the actual boundaries

Select cases from the relevant domains and accessible architecture. Include direct and indirect content, tool observations and persistent state where present. Add conventional parser/renderer, identity and execution checks alongside semantic attacks.

Use benign controls, secure variants and representative languages/modalities. Vary attack delivery or semantics rather than only one blocked string. Include delayed activation and repeat tasks when testing persistence. Keep model-based judges isolated from evaluated content and calibrate them against deterministic evidence and human labels.

For containment testing, inject an assumed-malicious proposal directly into the application boundary. Label this as an assumed-compromise test; it does not measure the probability a live model produces the proposal. Use repeated model trials separately when that probability matters.

## Execute and retain evidence

Reset fixture state between trials. Record system, model, prompt/policy, tools, data snapshot, available decoding settings, trial counts, observed boundary events and outcomes. Use synthetic canaries and controlled sinks; minimize sensitive trace data. Stop when an authorized limit is reached or an unexpected external effect occurs, preserving the evidence needed to investigate.

Compute results using explicit denominators and consequence-specific success criteria. Report benign task success and false positives alongside attack success. Small samples and passing scanners support bounded conclusions; avoid converting them into claims of universal security.

Finish with results actually observed, unexecuted cases, limitations and retest priorities. Confirmed failures should yield a minimal regression, a nearby variant, a benign control and a check at the owning deterministic boundary. A plan is complete when someone can execute it without inventing its scope, effect oracle or stop conditions.
