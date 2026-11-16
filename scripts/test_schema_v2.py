"""Offline tests for the schema v2 helpers, migration and validator rules."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import catalog_schema as cs  # noqa: E402
import migrate_v2 as mig  # noqa: E402
import validate as val  # noqa: E402


class Maps(unittest.TestCase):
    def test_tasks(self):
        cases = {"tumor segmentation": "segmentation", "report generation": "report-generation",
                 "visual question answering": "vqa", "survival prediction": "outcome-prediction",
                 "coronary calcium scoring": "quantification", "image-text retrieval": "retrieval",
                 "accelerated MRI": "reconstruction", "hosting": None, "multimodal oncology research": None,
                 "Segmentation": "segmentation", "foundation model pretraining": "pretraining"}
        for k, v in cases.items():
            self.assertEqual(cs.map_task(k), v, k)

    def test_formats(self):
        cases = {"DICOM": ("DICOM", None), "DICOM-SEG": (None, "DICOM-SEG"), "DICOM RTSTRUCT": (None, "DICOM RTSTRUCT"),
                 "NIfTI (OAIZIB-CM mirror)": ("NIfTI", None), "JPG": ("JPEG", None), "HDF5 (k-space)": ("raw-data", None),
                 "MHD/RAW": ("MHA", None), "CSV": (None, "CSV"), "derived": (None, None), "BIDS": ("NIfTI", None),
                 "NPZ": ("NumPy", None), "PET list-mode (raw)": ("raw-data", None), "DICOM-CT-PD": ("raw-data", None)}
        for k, v in cases.items():
            self.assertEqual(cs.map_format(k), v, k)

    def test_licenses(self):
        cases = {"CC BY 4.0": ("CC-BY", "allowed"), "CC BY-NC-SA 4.0": ("CC-BY-NC-SA", "prohibited"),
                 "cc-by-nc-4.0": ("CC-BY-NC", "prohibited"), "CC BY-NC-ND 4.0": ("CC-BY-NC-ND", "prohibited"),
                 "CC0 1.0": ("CC0", "allowed"), "PhysioNet Credentialed Health Data License 1.5.0":
                 ("PhysioNet-credentialed", "unclear"), "NIH Controlled Data Access Policy": ("NIH-controlled", "unclear"),
                 "MIT": ("software-license", "allowed"), None: ("unknown", "unclear"),
                 "Stanford research-use agreement (non-commercial)": ("custom-DUA", "prohibited")}
        for k, v in cases.items():
            self.assertEqual(cs.map_license(k), v, k)
            self.assertIn(v[0], cs.V["license_id"])

    def test_vocab_consistency(self):
        self.assertEqual(len(cs.PROTOCOLS), len(set(cs.PROTOCOLS)))
        self.assertTrue(set(val.REGIONS) >= {"Phantom", "Multi"})
        self.assertIn("includes-animal", cs.V["tags"])


class Migration(unittest.TestCase):
    def test_seed_keeps_v1_valid(self):
        cat = json.loads((cs.ROOT / "data" / "datasets.json").read_text())
        seeded = [mig.seed(json.loads(json.dumps(e))) for e in cat]
        self.assertEqual(val.validate(seeded), [])          # seeding never breaks a v1 entry
        self.assertTrue(all("license_id" in e for e in seeded if e.get("type") != "repository"))

    def test_finalize_ignores_v1_and_orders_v2(self):
        e = {"id": "a", "format": ["DICOM"]}
        self.assertEqual(mig.finalize(dict(e)), e)
        v2 = {"subjects": ["human"], "id": "a", "tasks": ["Tumor segmentation", "hosting"], "tags": ["pediatric", "genetics"],
              "label_types": ["report"], "image_format": ["PNG"], "n_images": 0, "name": "A"}
        f = mig.finalize(v2)
        self.assertEqual(list(f)[:3], ["id", "name", "subjects"])
        self.assertEqual((f["tasks"], f["tags"], f["paired_text"], f["raw_image"]),
                         (["segmentation"], ["genetics"], True, False))
        self.assertNotIn("n_images", f)
        self.assertEqual(mig.finalize(dict(v2, regions=["Multi", "Chest"]))["regions"], ["Chest"])
        self.assertEqual(mig.finalize(dict(v2, regions=["Multi"]))["regions"], ["Multi"])


class Validator(unittest.TestCase):
    def good(self, **over):
        e = {"id": "a", "name": "A", "type": "dataset", "review": "curated", "subjects": ["human"],
             "regions": ["Chest"], "organs": ["lung"], "modality": ["CT"], "protocols": ["CT:low-dose"],
             "image_format": ["DICOM"], "preprocessing": ["native"], "label_types": ["image-level-class"],
             "condition_groups": ["neoplasm"], "conditions": ["lung cancer"], "tasks": ["classification"],
             "license_id": "CC-BY", "commercial_use": "allowed", "access": "open", "url": "https://x.org",
             "description": "d"}
        e.update(over)
        return mig.finalize(e)

    def test_good_entry(self):
        self.assertEqual(val.validate([self.good()]), [])

    def test_rules(self):
        bad = {
            "animal": self.good(subjects=["animal"]),
            "protocol": self.good(protocols=["MRI:T9"]),
            "modality": self.good(modality=["Ultrasound"]),
            "conditions": dict(self.good(), conditions=["Lung Cancer"]),   # finalize would lowercase it
            "derived": dict(self.good(), raw_image=False),
            "v1 field": dict(self.good(), format=["DICOM"]),
            "note": self.good(details={"related": [{"name": "B", "relation": "derived-from"}]}),
            "related id": self.good(details={"related": [{"id": "zzz", "relation": "overlaps"}]}),
            "verified": self.good(review="human-verified"),
            "future": self.good(details={"release_date": "2999-01-01"}),
        }
        for name, e in bad.items():
            self.assertTrue(val.validate([e]), name)

    def test_require_v2(self):
        self.assertTrue(val.validate([{"id": "v1", "type": "dataset"}], require_v2=True))


if __name__ == "__main__":
    unittest.main()
