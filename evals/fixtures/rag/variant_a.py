"""Document assistant implementation A."""


class Service:
    def __init__(self, store):
        self.store = store
        self.memory = {}

    def answer(self, principal, query, model):
        candidates = self.store.search(query)
        messages = [{"role": "system", "content": "Summarize the user's documents."}]
        if principal.user in self.memory:
            messages.append({"role": "system", "content": self.memory[principal.user]})
        messages.append({"role": "user", "content": query})
        messages.extend({"role": "user", "content": d.text} for d in candidates)
        result = model(messages)
        permitted = {
            d.id for d in candidates
            if d.tenant == principal.tenant and principal.user in d.readers
        }
        if result.get("summary"):
            self.memory[principal.user] = result["summary"]
        return {
            "html": result["text"],
            "citations": [c for c in result.get("citations", []) if c in permitted],
        }
