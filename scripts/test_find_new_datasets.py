#!/usr/bin/env python3
"""Offline tests for find_new_datasets.py (no network: every API call is mocked).

Run: python3 -m unittest discover -s scripts -p 'test_*.py'
Centred on the Merlin Plus miss: a follow-up release by a catalog publisher
(AbdomenAtlas / MrGiovanni) with a non-generic repo name, which the id-substring
Hugging Face search could never surface.
"""
import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import find_new_datasets as f  # noqa: E402

CATALOG = json.loads(f.DATA.read_text())
# the catalog as it was when Merlin Plus was missed
BEFORE = [d for d in CATALOG if d["id"] != "merlin-plus"]
MERLIN_PLUS_HF = "AbdomenAtlas/MerlinPlus"


def fixture_get_json(url, timeout=25, headers=None, data=None):
    recent, old = f.days_ago(30), f.days_ago(900)
    if "huggingface.co/api/datasets?author=AbdomenAtlas&" in url:
        return [
            {"id": MERLIN_PLUS_HF, "createdAt": recent + "T00:00:00.000Z", "downloads": 3, "likes": 1,
             "tags": ["medical", "task_categories:image-segmentation"],
             "description": "Merlin Plus: per-voxel tumor and organ masks for 25,494 abdominal CT scans."},
            # catalog entry (by URL slug) -> known
            {"id": "AbdomenAtlas/AbdomenAtlas1.0Mini", "createdAt": recent, "tags": [],
             "description": "abdominal CT organ segmentation"},
            # only an auto tag says "segmentation": not radiology -> skipped
            {"id": "AbdomenAtlas/StreetScenes", "createdAt": recent,
             "tags": ["task_categories:image-segmentation"], "description": "Urban street scene images."},
            # older than the publisher lookback -> skipped
            {"id": "AbdomenAtlas/OldCTRelease", "createdAt": old, "tags": [],
             "description": "abdominal CT dataset"},
        ]
    if url.startswith(f.GH_API + "/users/MrGiovanni/repos"):
        return [
            {"name": "MerlinPlus", "full_name": "MrGiovanni/MerlinPlus",
             "html_url": "https://github.com/MrGiovanni/MerlinPlus", "created_at": recent + "T00:00:00Z",
             "stargazers_count": 40, "topics": [],
             "description": "[MICCAI 2026] Merlin Plus is the first large-scale public CT dataset with "
                            "radiologist-created tumor masks across 9 organs"},
            # model repo that only *uses* data
            {"name": "CheXThing", "full_name": "MrGiovanni/CheXThing", "html_url": "https://github.com/MrGiovanni/CheXThing",
             "created_at": recent, "topics": [],
             "description": "A generative model trained on a large corpus of chest X-rays"},
            # code-only repo: relevant words but not a dataset release
            {"name": "SomeNet", "full_name": "MrGiovanni/SomeNet", "html_url": "https://github.com/MrGiovanni/SomeNet",
             "created_at": recent, "description": "Official code for CT tumor detection", "topics": []},
            {"name": "ForkedCT", "full_name": "MrGiovanni/ForkedCT", "fork": True,
             "html_url": "https://github.com/MrGiovanni/ForkedCT", "created_at": recent,
             "description": "CT dataset fork", "topics": []},
        ]
    raise OSError("offline test: " + url)


def run_main(catalog, prev_text=None):
    with tempfile.TemporaryDirectory() as tmp:
        data = pathlib.Path(tmp) / "datasets.json"
        data.write_text(json.dumps(catalog))
        argv = ["find_new_datasets.py"]
        if prev_text is not None:
            prev = pathlib.Path(tmp) / "prev.md"
            prev.write_text(prev_text)
            argv += ["--prev", str(prev)]
        out = io.StringIO()
        with mock.patch.object(f, "DATA", data), mock.patch.object(f, "get_json", fixture_get_json), \
                mock.patch.object(sys, "argv", argv), mock.patch.dict(os.environ, {}, clear=False), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            f.main()
        return out.getvalue()


def priority_section(report):
    start = report.index("## ⭐ Priority")
    nxt = report.find("\n## ", start + 1)
    return report[start:nxt if nxt != -1 else len(report)]


class NormAndClassify(unittest.TestCase):
    def setUp(self):
        self.names, self.slugs, self.short, self.display, self.cover = f.load_known(BEFORE)

    def cls(self, name):
        return f.classify(f.norm(name), self.names, self.slugs, self.short, self.cover)

    def test_plus_is_spelled_out(self):
        self.assertEqual(f.norm("Merlin+"), f.norm("MerlinPlus"))
        self.assertEqual(f.norm("Merlin Plus"), "merlinplus")
        self.assertNotEqual(f.norm("Merlin+"), f.norm("Merlin"))

    def test_merlin_plus_is_a_derivative_of_merlin(self):
        for name in ("Merlin+", "MerlinPlus", "Merlin Plus", "Merlin-Plus"):
            status, base = self.cls(name)
            self.assertEqual(status, "derivative", name)
            self.assertEqual(self.display[base], "Merlin")

    def test_merlin_itself_is_known(self):
        self.assertEqual(f.classify("merlin", self.names, self.slugs, self.short)[0], "known")

    def test_extension_of_long_name_not_swallowed_as_mirror(self):
        # before: any superstring of an 8+ char catalog name was suppressed as a reupload
        status, base = self.cls("TotalSegmentator v3")
        self.assertEqual(status, "derivative")

    def test_editions_the_catalog_covers_are_known(self):
        # VerSe entry: "(2019 & 2020)"; LiTS entry: "(LiTS17)", 2017
        for name in ("VerSe'20", "VerSe`19", "LiTS17", "LiTS 2017"):
            self.assertEqual(self.cls(name), ("known", None), name)

    def test_residue_cannot_continue_a_number(self):
        # "HVSMR 2024" is not catalog "HVSMR-2.0" (key hvsmr20) + "24"
        self.assertNotEqual(self.cls("HVSMR 2024")[1], "hvsmr20")

    def test_longest_base_wins(self):
        names = {"totalsegmentator", "totalsegmentatormri"}
        status, base = f.classify("totalsegmentatormriv2", names, set(), {"totalsegmentator"})
        self.assertEqual((status, base), ("derivative", "totalsegmentatormri"))

    def test_mirrors_still_suppressed(self):
        names = {"totalsegmentator"}
        self.assertEqual(f.classify("totalsegmentatordatasetmirror", names, set(), names)[0], "known")

    def test_reformatted_copies_are_mirrors(self):
        # seen as "-Lite" rows in the ⭐ Priority section of the first live dry run
        for name in ("AMOS22-Lite", "VerSe-Lite", "PI-CAI-Lite", "MAMA-MIA-Lite", "LNQ2023-Lite",
                     "HNTSMRG24-Lite",          # 2-digit year: catalog "HNTS-MRG 2024"
                     "AbdomenAtlas1.1Mini", "PI-CAI_preprocessed_nifti"):
            self.assertEqual(self.cls(name), ("known", None), name)

    def test_derivative_with_packaging_word_still_flagged(self):
        # pre-merge review: "COVIDx CXR-4" was flagged but "COVIDx CXR-4 Dataset" was
        # swallowed by the substring mirror rule; Kaggle/Zenodo titles often end so
        self.assertEqual(self.cls("TotalSegmentator v3 Dataset"), ("derivative", "totalsegmentator"))
        for name in ("COVIDx CXR-4 Dataset", "CancerVerse-v2-Dataset", "OmniMedVQA-V2-Data",
                     "Merlin v2 Dataset"):
            self.assertEqual(self.cls(name)[0], "derivative", name)
        self.assertEqual(self.cls("AMOS22-Lite"), ("known", None))     # plain copies stay mirrors

    def test_copy_of_uncatalogued_base_still_surfaces(self):
        self.assertEqual(self.cls("AFIDs-Lite"), (None, None))   # AFIDs itself isn't catalogued
        self.assertEqual(self.cls("MSD-Lite"), (None, None))     # base "msd" too short to trust

    def test_unrelated_is_new(self):
        self.assertEqual(f.classify("somebrandnewctcohort", self.names, self.slugs, self.short), (None, None))


class Relevance(unittest.TestCase):
    def test_stems_match_whole_words(self):
        # the \b...\b wrapper used to stop stems like "radiolog" matching "radiology"
        for text in ("radiology reports", "Mammography screening", "renal tumors", "pancreatic cancer",
                     "computed tomography", "medical-imaging"):
            self.assertTrue(f.relevant(text), text)

    def test_exclude_unless_in_scope_modality(self):
        self.assertFalse(f.relevant("100,000 histological images of human colorectal cancer"))
        self.assertTrue(f.relevant("CT scans of histologically confirmed lung nodules"))

    def test_claims_dataset(self):
        yes = [("MerlinPlus", "[MICCAI 2026] Merlin Plus is the first large-scale public CT dataset with "
                              "radiologist-created tumor masks across 9 organs"),
               ("BreastMammo", "BreastMammo and DenseMammo: Benchmarks for Mammography Domain Generalization"),
               ("Dataset_GBC_CT", "Gallbladder cancer CT scans")]
        no = [("CheXThing", "A generative model trained on a large corpus of chest X-rays"),
              ("CycleMED", "CycleGAN framework for CT/MRI translation with a custom dataset loader"),
              ("newmajor", "Alzheimer's disease detection using MRI datasets"),
              ("SomeNet", "Official code for CT tumor detection")]
        for name, desc in yes:
            self.assertTrue(f.claims_dataset(name, desc), name)
        for name, desc in no:
            self.assertFalse(f.claims_dataset(name, desc), name)

    def test_publisher_rows_need_imaging_terms(self):
        self.assertFalse(f.imaging("org/StreetScenes", "Urban street scene segmentation"))
        self.assertTrue(f.imaging("AbdomenAtlas/MerlinPlus", "tumor masks for abdominal CT"))


class SourceQueries(unittest.TestCase):
    def test_github_search_has_no_bare_pet_query(self):
        urls = []

        def fake(url, timeout=25, headers=None, data=None):
            urls.append(f.urllib.parse.unquote(url))
            return {"items": []}
        with mock.patch.object(f, "get_json", fake):
            f.github_search("2026-01-01")
        self.assertTrue(urls)
        self.assertFalse([u for u in urls if "q=PET dataset" in u])   # finds pet-animal datasets
        self.assertTrue([u for u in urls if "q=PET CT dataset" in u])

    def test_hf_tag_hits_need_higher_floor(self):
        def fake(url, timeout=25, headers=None, data=None):
            if "search=radiology" in url:
                return [{"id": "a/IdHit-CT", "downloads": 100, "likes": 0, "tags": []}]
            if "filter=radiology" in url:
                return [{"id": "b/TagLowPop-CT", "downloads": 100, "likes": 0, "tags": []},
                        {"id": "c/TagPopular-CT", "downloads": 500, "likes": 0, "tags": []}]
            return []
        with mock.patch.object(f, "get_json", fake), mock.patch.object(f, "_hf_token_ok", False):
            names = [c["name"] for c in f.huggingface(100)]
        self.assertEqual(names, ["IdHit-CT", "TagPopular-CT"])


class HfToken(unittest.TestCase):
    def test_rejected_token_falls_back_to_anonymous(self):
        calls = []

        def fake(url, timeout=25, headers=None, data=None):
            calls.append(bool(headers))
            if headers:
                raise f.urllib.error.HTTPError(url, 401, "Unauthorized", {}, None)
            return [{"id": "x"}]
        with mock.patch.object(f, "get_json", fake), mock.patch.object(f, "_hf_token_ok", True), \
                mock.patch.dict(os.environ, {"HF_TOKEN": "hf_revoked"}), \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(f.hf_get("u1"), [{"id": "x"}])
            self.assertEqual(f.hf_get("u2"), [{"id": "x"}])
        self.assertEqual(calls, [True, False, False])   # token tried once, then anonymous


class Publishers(unittest.TestCase):
    def test_catalog_publishers_include_merlin_plus_publishers(self):
        hf, gh = f.catalog_publishers(BEFORE)
        self.assertIn("AbdomenAtlas", hf)     # AbdomenAtlas 1.0 is on HF under this org
        self.assertIn("MrGiovanni", gh)       # AbdomenAtlas 1.1 / 3.0, PanTS on GitHub
        self.assertIn("stanfordmimi", hf)     # Merlin's own publisher (extra)
        hf_now, gh_now = f.catalog_publishers(CATALOG)
        self.assertIn("BodyMaps", hf_now)     # CancerVerse
        self.assertIn("BodyMaps", gh_now)     # AbdomenAtlas 2.0
        self.assertNotIn("datasets", [a.lower() for a in hf])


class EndToEnd(unittest.TestCase):
    def test_merlin_plus_surfaces_once_in_priority(self):
        report = run_main(BEFORE)
        pri = priority_section(report)
        self.assertIn(f"[MerlinPlus](https://huggingface.co/datasets/{MERLIN_PLUS_HF})", pri)
        self.assertIn("extends **Merlin**", pri)
        self.assertEqual(report.count("[MerlinPlus]("), 1)   # HF + GitHub deduped
        self.assertNotIn("OldCTRelease", report)
        self.assertNotIn("StreetScenes", report)
        self.assertNotIn("CheXThing", report)
        self.assertNotIn("SomeNet", report)
        self.assertNotIn("ForkedCT", report)
        self.assertNotIn("AbdomenAtlas1.0Mini", report)

    def test_not_reported_once_in_catalog(self):
        cat = BEFORE + [{"id": "merlin-plus", "name": "Merlin Plus", "full_name": None,
                         "url": "https://huggingface.co/datasets/" + MERLIN_PLUS_HF}]
        self.assertNotIn("MerlinPlus", run_main(cat))

    def test_real_catalog_knows_merlin_plus(self):
        if not any(d["id"] == "merlin-plus" for d in CATALOG):
            self.skipTest("merlin-plus not in catalog yet")
        self.assertNotIn("MerlinPlus", run_main(CATALOG))

    def test_new_candidate_marked_fresh(self):
        cat = BEFORE + [{"id": "merlin-plus", "name": "Merlin Plus", "full_name": None,
                         "url": "https://huggingface.co/datasets/" + MERLIN_PLUS_HF}]
        first = run_main(cat, prev_text="")
        self.assertNotIn("MerlinPlus", first)
        again = run_main(BEFORE, prev_text=first)
        self.assertIn(f"- 🆕 [MerlinPlus](https://huggingface.co/datasets/{MERLIN_PLUS_HF})", again)
        self.assertIn("_1 candidate(s) marked 🆕", again)

    def test_fresh_on_second_run_only_for_new(self):
        first = run_main(BEFORE, prev_text="")
        self.assertNotIn("- 🆕", first)                    # no previous report -> nothing flagged
        again = run_main(BEFORE, prev_text=first)
        self.assertNotIn("- 🆕", again)                    # nothing new since
        self.assertIn("_0 candidate(s) marked 🆕", again)


def cands(n, prefix="Candidate"):
    return [{"name": f"{prefix} {i:05d} CT", "url": f"https://example.org/{prefix}/{i}", "source": "Zenodo"}
            for i in range(n)]


KNOWN_EMPTY = (set(), set(), set(), {}, {})


class SeenState(unittest.TestCase):
    def roundtrip(self, report):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as t:
            t.write(report)
        try:
            return f.load_prev_seen(t.name)
        finally:
            os.unlink(t.name)

    def week(self, candidates, prev):
        new = f.select_new(candidates, KNOWN_EMPTY, set(prev))
        report = f.build_report(new, [], prev)
        return new, report, self.roundtrip(report)

    def test_first_run_baselines_everything(self):
        new, report, seen = self.week(cands(200), [])
        self.assertIn("…and 150 more", report)             # only 50 rows visible
        self.assertEqual(len(seen), 200)                    # no previous report: all baseline

    def test_backlog_of_cut_new_rows_drains(self):
        _, _, prev = self.week(cands(3, "Old"), [])        # an earlier report exists
        shown_ever, fresh_counts = set(), []
        for _ in range(5):
            new, report, prev = self.week(cands(3, "Old") + cands(200), prev)
            fresh_counts.append(sum(c["fresh"] for c in new))
            shown_ever |= {c["name"] for c in new if f"[{c['name']}](" in report}
        # 200 new rows, 50 visible per week: each is shown once, flagged 🆕 until then
        self.assertEqual(fresh_counts, [200, 150, 100, 50, 0])
        self.assertTrue({c["name"] for c in cands(200)} <= shown_ever)

    def test_only_genuinely_new_rows_fresh(self):
        _, _, prev = self.week(cands(40), [])
        _, _, prev = self.week(cands(40), prev)
        new, _, _ = self.week(cands(40) + cands(1, "Brand new"), prev)
        self.assertEqual([c["name"] for c in new if c["fresh"]], ["Brand new 00000 CT"])

    def test_priority_rows_not_cut_by_source_cap(self):
        rows = [{"name": f"Release {i:03d} CT", "url": f"https://x/{i}", "source": "HuggingFace",
                 "publisher": "Org"} for i in range(80)]
        report = f.build_report(f.select_new(rows, KNOWN_EMPTY, set()), [], [])
        self.assertNotIn("more priority candidates not shown", report)

    def test_legacy_report_without_hidden_list(self):
        legacy = "## Zenodo (1)\n\n- [Old One](https://zenodo.org/records/1)\n"
        prev = set(self.roundtrip(legacy))
        new = f.select_new([{"name": "Old One", "url": "u", "source": "Zenodo"},
                            {"name": "Fresh One", "url": "u", "source": "Zenodo"}], KNOWN_EMPTY, prev)
        self.assertEqual([c["fresh"] for c in new], [False, True])

    def test_previously_seen_keys_are_carried(self):
        report1 = f.build_report(f.select_new(cands(3), KNOWN_EMPTY, set()), [], [])
        prev = self.roundtrip(report1)
        # week 2: that source failed (no candidates) -> its keys must survive for week 3
        report2 = f.build_report([], [], prev)
        prev2 = set(self.roundtrip(report2))
        week3 = f.select_new(cands(3), KNOWN_EMPTY, prev2)
        self.assertFalse(any(c["fresh"] for c in week3))

    def test_body_fits_github_limit(self):
        many = f.select_new(cands(5000, "A very long candidate dataset name that pads the report " * 2),
                            KNOWN_EMPTY, set())
        report = f.build_report(many, [], ["deadbeef"] * 10)
        self.assertLessEqual(f.u16len(report), 65536)
        hidden = f.SEEN_RE.search(report).group(1).split()
        self.assertTrue({f.khash(c["key"]) for c in many} <= set(hidden))


if __name__ == "__main__":
    unittest.main()
