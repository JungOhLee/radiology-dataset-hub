"""Offline tests for scripts/enrich_entries.py (schema v2; no network, no SDK)."""
import json
import pathlib
import sys
import types
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import enrich_entries as en  # noqa: E402
import migrate_v2 as mig  # noqa: E402

TODAY = "2026-11-16"
NOPH = {"type": "not-a-phantom", "anthropomorphic": False, "body_part": "", "model": "", "purpose": ""}


def v1(**over):
    """A seeded v1 entry, as the enrichment pass sees it."""
    e = {"id": "x-set", "name": "X Set", "full_name": None, "type": "dataset", "regions": ["Multi"],
         "anatomy": "brain", "modality": ["MRI"], "year": 2024, "format": ["NIfTI", "CSV"], "raw_image": True,
         "size": "10 scans", "paired_text": True, "paired_text_detail": "clinical CSV", "multi_sequence": True,
         "multi_sequence_detail": "T1, T2", "segmentation": True, "segmentation_detail": "tumour masks",
         "other_labels": ["IDH status"], "tasks": ["tumor segmentation", "hosting"], "license": "CC BY 4.0",
         "access": "open", "host": "Zenodo", "url": "https://zenodo.org/records/1", "description": "Ten scans.",
         "tags": ["longitudinal", "pediatric"]}
    e.update(over)
    return mig.seed(e, {"x-set"})


def res(**over):
    o = {"subjects": ["human"], "other_modalities": [], "protocols": ["MRI:T1w", "MRI:T2w"], "protocol_note": "",
         "field_strength": ["3T"], "conditions": ["Glioma"], "condition_groups": ["neoplasm"],
         "population": ["pediatric"], "setting": ["diagnostic"], "organs": ["brain"], "label_types": ["mask", "molecular"],
         "image_format": ["NIfTI"], "label_format": ["CSV"], "preprocessing": ["skull-stripped-defaced"],
         "images_included": True, "n_subjects": 10, "n_studies": 0, "n_images": 0, "tasks": ["classification"],
         "tags": ["radiogenomics"], "license_id": "CC-BY", "commercial_use": "allowed", "phantom": dict(NOPH),
         "regions": ["Neuro"], "sources": [], "reason": "official page"}
    o.update(over)
    return o


class Apply(unittest.TestCase):
    ids = {"x-set", "lidc-idri"}

    def test_converts_to_valid_v2(self):
        e, ch = en.apply_v2(v1(), res(), self.ids, TODAY)
        self.assertEqual(ch[0], "v2")
        for k in ("format", "multi_sequence_detail", "other_labels"):
            self.assertNotIn(k, e)
        self.assertEqual(e["protocol_note"], "T1, T2")                 # moved, not lost
        self.assertIn("IDH status", e["details"]["label_schema"])     # other_labels merged
        self.assertEqual(e["regions"], ["Neuro"])                       # ["Multi"] replaced
        self.assertEqual(e["tasks"], ["segmentation", "classification"])
        self.assertEqual(e["tags"], ["longitudinal", "radiogenomics"])  # pediatric -> population, dropped as tag
        self.assertEqual((e["raw_image"], e["paired_text"], e["segmentation"], e["longitudinal"]),
                         (False, False, True, True))                    # derived: skull-stripped is not raw
        self.assertEqual((e["review"], e["enriched"]), ("curated", TODAY))
        self.assertEqual(en.val.entry_errors(e, self.ids), [])

    def test_animal_only_removed_mixed_tagged(self):
        self.assertEqual(en.apply_v2(v1(), res(subjects=["animal"]), self.ids, TODAY), (None, ["removed: animal"]))
        e, ch = en.apply_v2(v1(), res(subjects=["human", "animal"]), self.ids, TODAY)
        self.assertEqual(e["subjects"], ["human"])
        self.assertIn("includes-animal", e["tags"])

    def test_no_subjects_keeps_v1(self):
        old = v1()
        e, ch = en.apply_v2(old, res(subjects=[]), self.ids, TODAY)
        self.assertIs(e, old)
        self.assertEqual(ch, ["no-subjects"])

    def test_geometric_phantom(self):
        ph = {"type": "physical", "anthropomorphic": False, "body_part": "none-geometric",
              "model": "Catphan 600", "purpose": "CT image quality"}
        e, ch = en.apply_v2(v1(modality=["CT"]), res(subjects=["phantom"], phantom=ph, organs=["none-geometric"],
                                                     protocols=["CT:non-contrast"], condition_groups=["not-applicable"],
                                                     population=[], conditions=[]), self.ids, TODAY)
        self.assertEqual(e["phantom"]["model"], "Catphan 600")
        self.assertEqual(e["regions"], ["Phantom"])
        self.assertEqual(en.val.entry_errors(e, self.ids), [])

    def test_sources_with_process_and_note(self):
        base = v1(details={"related": [{"id": "lidc-idri", "name": "LIDC-IDRI", "relation": "derived-from"}]})
        out = res(sources=[{"id": "lidc-idri", "name": "LIDC-IDRI", "process": ["reformatted-resized"], "note": "crops"},
                           {"id": "not-in-catalog", "name": "NLST", "process": ["subset"], "note": ""}])
        e, ch = en.apply_v2(base, out, self.ids, TODAY)
        rel = e["details"]["related"]
        self.assertEqual(rel[0], {"id": "lidc-idri", "name": "LIDC-IDRI", "relation": "derived-from",
                                  "note": "crops", "process": ["reformatted-resized"]})   # note filled in place
        self.assertEqual(rel[1], {"name": "NLST", "relation": "derived-from", "process": ["subset"], "note": "subset"})
        self.assertIn("sources +1", ch)
        self.assertEqual(en.val.entry_errors(e, self.ids), [])


class Run(unittest.TestCase):
    def factory(self, outs):
        outs = list(outs)

        def create(**kw):
            u = types.SimpleNamespace(input_tokens=5000, output_tokens=500, cache_read_input_tokens=0,
                                      cache_creation_input_tokens=0)
            return types.SimpleNamespace(stop_reason="end_turn", usage=u,
                                         content=[types.SimpleNamespace(type="text", text=json.dumps(outs.pop(0)))])
        return lambda: types.SimpleNamespace(beta=types.SimpleNamespace(messages=types.SimpleNamespace(create=create)))

    def test_removal_conversion_and_invalid(self):
        cat = [v1(id="mouse-mri", name="Mouse MRI", url="https://example.org/m"), v1(), v1(id="bad")]
        triage = {"decisions": [{"name": "MOUSE-MRI", "decision": "added",
                                 "reason": "catalog id mouse-mri (auto-added): TCIA collection"}]}
        results, spent = en.run(cat, triage, ["mouse-mri", "x-set", "bad"], 10, 10, client_factory=self.factory(
            [res(subjects=["animal"]), res(), res(organs=[])]), get=lambda u, headers=None: ("text/html", "x"),
            today=TODAY, log=lambda *_: None)
        self.assertEqual([r["status"] for r in results], ["removed", "v2", "invalid"])
        self.assertEqual([e["id"] for e in cat], ["x-set", "bad"])
        self.assertIn("subjects", cat[0])
        self.assertNotIn("subjects", cat[1])                # invalid patch -> kept as v1
        self.assertEqual(triage["decisions"][0]["decision"], "rejected")
        body = en.summary(results, spent, 3, TODAY, 10)
        self.assertIn("Removed — animal / preclinical subjects (1)", body)
        self.assertIn("Not converted", body)

    def test_budget_stop(self):
        cat = [v1(id=f"s{i}") for i in range(4)]
        res_, _ = en.run(cat, {"decisions": []}, [e["id"] for e in cat], 10, 0.01,
                         client_factory=self.factory([res()] * 4), get=lambda u, headers=None: ("text/html", "x"),
                         today=TODAY, log=lambda *_: None)
        self.assertEqual(len(res_), 1)

    def test_schema_has_no_union(self):
        self.assertEqual(json.dumps(en.schema()).count('"anyOf"'), 0)


if __name__ == "__main__":
    unittest.main()
