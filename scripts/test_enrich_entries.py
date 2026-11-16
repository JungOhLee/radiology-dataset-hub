"""Offline tests for scripts/enrich_entries.py (no network, no SDK)."""
import json
import pathlib
import sys
import types
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import enrich_entries as en  # noqa: E402

TODAY = "2026-11-15"
NOPH = {"type": "not-a-phantom", "body_part": "", "model": "", "purpose": ""}


def ent(**over):
    e = {"id": "x-set", "name": "X Set", "full_name": None, "type": "dataset", "regions": ["Chest"],
         "anatomy": "", "modality": ["CT"], "year": 2024, "format": ["DICOM"], "raw_image": True,
         "size": "10 scans", "paired_text": False, "paired_text_detail": None, "multi_sequence": True,
         "multi_sequence_detail": None, "segmentation": False, "segmentation_detail": None,
         "other_labels": [], "tasks": ["classification"], "license": "CC BY 4.0", "access": "open",
         "host": "Zenodo", "url": "https://zenodo.org/records/1", "description": "Ten scans."}
    e.update(over)
    return e


def res(**over):
    o = {"subjects": "human", "phantom": dict(NOPH), "derived": False, "sources": [], "vqa": False,
         "anatomy": "", "sequences": "", "reason": "official page"}
    o.update(over)
    return o


class Patch(unittest.TestCase):
    ids = {"x-set", "lidc-idri"}

    def test_animal_removed(self):
        self.assertEqual(en.patch(ent(), res(subjects="animal"), self.ids), (None, ["removed: animal"]))

    def test_phantom_fills_details_tag_and_anatomy(self):
        ph = {"type": "physical", "body_part": "chest", "model": "Lungman", "purpose": "radiomics"}
        e, ch = en.patch(ent(), res(subjects="phantom-or-simulation", phantom=ph), self.ids)
        self.assertEqual(e["details"]["phantom"], ph)
        self.assertIn("phantom", e["tags"])
        self.assertEqual(e["anatomy"], "chest")
        self.assertEqual(en.val.validate([e]), [])

    def test_existing_values_are_not_overwritten(self):
        old = {"type": "digital", "body_part": "breast"}
        e, ch = en.patch(ent(anatomy="lung", multi_sequence_detail="arterial, venous", details={"phantom": old}),
                         res(phantom={"type": "physical", "body_part": "chest", "model": "", "purpose": ""},
                             anatomy="thorax", sequences="T1, T2"), self.ids)
        self.assertEqual((e["details"]["phantom"], e["anatomy"], e["multi_sequence_detail"]),
                         (old, "lung", "arterial, venous"))
        self.assertEqual(ch, [])

    def test_derived_sources_merge_without_duplicates(self):
        base = ent(details={"related": [{"id": "lidc-idri", "name": "LIDC-IDRI", "relation": "derived-from"}]})
        out = res(derived=True, sources=[{"id": "lidc-idri", "name": "LIDC-IDRI", "note": "crops"},
                                         {"id": "not-in-catalog", "name": "NLST", "note": "2D slices"},
                                         {"id": "", "name": "nlst", "note": "dup by name"}])
        e, ch = en.patch(base, out, self.ids)
        rel = e["details"]["related"]
        self.assertEqual(len(rel), 2)
        self.assertEqual(rel[1], {"name": "NLST", "relation": "derived-from", "note": "2D slices"})  # unknown id dropped
        self.assertIn("derived", e["tags"])
        self.assertIn("sources +1", ch)
        self.assertEqual(en.val.validate([e]), [])

    def test_vqa_and_sequences(self):
        e, ch = en.patch(ent(), res(vqa=True, sequences="T1, T2, FLAIR", anatomy="brain"), self.ids)
        self.assertIn("vqa", e["tags"])
        self.assertIn("vqa", e["tasks"])
        self.assertEqual((e["multi_sequence_detail"], e["anatomy"]), ("T1, T2, FLAIR", "brain"))
        e, _ = en.patch(ent(multi_sequence=False), res(sequences="T1"), self.ids)
        self.assertIsNone(e["multi_sequence_detail"])   # not multi-sequence: leave it


class Run(unittest.TestCase):
    def factory(self, outs):
        outs = list(outs)

        def create(**kw):
            u = types.SimpleNamespace(input_tokens=5000, output_tokens=500, cache_read_input_tokens=0,
                                      cache_creation_input_tokens=0)
            return types.SimpleNamespace(stop_reason="end_turn", usage=u,
                                         content=[types.SimpleNamespace(type="text", text=json.dumps(outs.pop(0)))])
        return lambda: types.SimpleNamespace(beta=types.SimpleNamespace(messages=types.SimpleNamespace(create=create)))

    def test_removal_rewrites_triage_and_catalog(self):
        cat = [ent(id="mouse-mri", name="Mouse MRI", url="https://example.org/m"), ent()]
        triage = {"decisions": [{"name": "MOUSE-MRI", "decision": "added",
                                 "reason": "catalog id mouse-mri (auto-added): TCIA collection"}]}
        res_, spent = en.run(cat, triage, ["mouse-mri", "x-set"], 10, 10, client_factory=self.factory(
            [res(subjects="animal"), res(anatomy="lung")]), get=lambda u, headers=None: ("text/html", "x"),
            today=TODAY, log=lambda *_: None)
        self.assertEqual([e["id"] for e in cat], ["x-set"])
        self.assertEqual(cat[0]["anatomy"], "lung")
        self.assertEqual(triage["decisions"][0]["decision"], "rejected")
        self.assertEqual(triage["decisions"][-1]["url"], "https://example.org/m")
        self.assertEqual([r["status"] for r in res_], ["removed", "enriched"])
        body = en.summary(res_, spent, 2, TODAY, 10)
        self.assertIn("Removed — animal / preclinical subjects (1)", body)

    def test_budget_stop(self):
        cat = [ent(id=f"s{i}") for i in range(4)]
        res_, _ = en.run(cat, {"decisions": []}, [e["id"] for e in cat], 10, 0.01,
                         client_factory=self.factory([res()] * 4), get=lambda u, headers=None: ("text/html", "x"),
                         today=TODAY, log=lambda *_: None)
        self.assertEqual(len(res_), 1)

    def test_schema_has_one_union_at_most(self):
        self.assertEqual(json.dumps(en.schema()).count('"anyOf"'), 0)


if __name__ == "__main__":
    unittest.main()
