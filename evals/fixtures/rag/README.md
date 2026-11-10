# Synthetic document assistant

The assistant summarizes documents for authenticated tenant users. Compare the supplied implementation under the requested scope; each variant has the same `Service.answer(principal, query, model)` interface.

The caller is an already-authenticated gateway that constructs an immutable `Principal`. Users cannot choose another tenant or identity at that gateway. `Document.readers` and `Document.tenant` are authoritative source ACLs maintained outside the assistant. The source store is local, and tests can revoke an ACL between calls.

The model callable receives a message list and returns `text`, optional `summary`, and `citations`. In production, the returned `html` field is inserted into a browser container with `innerHTML`. This fixture does not launch a browser. Documents and model outputs are untrusted.

The supplied fake model is an assumed-compromise boundary probe, not a model simulator or an attack-success-rate benchmark. It can expose all of the messages it receives and return chosen content. All markers and identities are synthetic. There are no network calls, real secrets, external tools or paid APIs.

Persistent state is the service's in-memory `memory` dictionary, which survives consecutive `answer` calls on that instance. The implementation and source records are the review artifacts; evaluator rubrics and tests are deliberately stored elsewhere.
