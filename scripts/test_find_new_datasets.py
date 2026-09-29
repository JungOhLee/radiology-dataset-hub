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
        self.names, self.slugs, self.short, self.display = f.load_known(BEFORE)

    def test_plus_is_spelled_out(self):
        self.assertEqual(f.norm("Merlin+"), f.norm("MerlinPlus"))
        self.assertEqual(f.norm("Merlin Plus"), "merlinplus")
        self.assertNotEqual(f.norm("Merlin+"), f.norm("Merlin"))

    def test_merlin_plus_is_a_derivative_of_merlin(self):
        for name in ("Merlin+", "MerlinPlus", "Merlin Plus", "Merlin-Plus"):
            status, base = f.classify(f.norm(name), self.names, self.slugs, self.short)
            self.assertEqual(status, "derivative", name)
            self.assertEqual(self.display[base], "Merlin")

    def test_merlin_itself_is_known(self):
        self.assertEqual(f.classify("merlin", self.names, self.slugs, self.short)[0], "known")

    def test_extension_of_long_name_not_swallowed_as_mirror(self):
        # before: any superstring of an 8+ char catalog name was suppressed as a reupload
        status, base = f.classify(f.norm("TotalSegmentator v3"), self.names, self.slugs, self.short)
        self.assertEqual(status, "derivative")

    def test_longest_base_wins(self):
        names = {"totalsegmentator", "totalsegmentatormri"}
        status, base = f.classify("totalsegmentatormriv2", names, set(), {"totalsegmentator"})
        self.assertEqual((status, base), ("derivative", "totalsegmentatormri"))

    def test_mirrors_still_suppressed(self):
        names = {"totalsegmentator"}
        self.assertEqual(f.classify("totalsegmentatordatasetmirror", names, set(), names)[0], "known")

    def test_unrelated_is_new(self):
        self.assertEqual(f.classify("somebrandnewctcohort", self.names, self.slugs, self.short), (None, None))


class Publishers(unittest.TestCase):
    def test_catalog_publishers_include_merlin_plus_publishers(self):
        hf, gh = f.catalog_publishers(BEFORE)
        self.assertIn("AbdomenAtlas", hf)     # AbdomenAtlas 1.0 is on HF under this org
        self.assertIn("MrGiovanni", gh)       # AbdomenAtlas 1.1 / 3.0, PanTS on GitHub
        self.assertIn("stanfordmimi", hf)     # Merlin's own publisher (extra)
        self.assertNotIn("datasets", [a.lower() for a in hf])


class EndToEnd(unittest.TestCase):
    def test_merlin_plus_surfaces_once_in_priority(self):
        report = run_main(BEFORE)
        pri = priority_section(report)
        self.assertIn(f"[MerlinPlus](https://huggingface.co/datasets/{MERLIN_PLUS_HF})", pri)
        self.assertIn("extends **Merlin**", pri)
        self.assertEqual(report.count("[MerlinPlus]("), 1)   # HF + GitHub deduped
        self.assertNotIn("OldCTRelease", report)
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

    def test_fresh_on_second_run_only_for_new(self):
        first = run_main(BEFORE, prev_text="")
        self.assertNotIn("- 🆕", first)                    # no previous report -> nothing flagged
        again = run_main(BEFORE, prev_text=first)
        self.assertNotIn("- 🆕", again)                    # nothing new since
        self.assertIn("_0 candidate(s) marked 🆕", again)


def cands(n, prefix="Candidate"):
    return [{"name": f"{prefix} {i:05d} CT", "url": f"https://example.org/{prefix}/{i}", "source": "Zenodo"}
            for i in range(n)]


KNOWN_EMPTY = (set(), set(), set(), {})


class SeenState(unittest.TestCase):
    def roundtrip(self, report):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as t:
            t.write(report)
        try:
            return f.load_prev_seen(t.name)
        finally:
            os.unlink(t.name)

    def test_rows_cut_by_display_cap_are_not_refreshed(self):
        week1 = f.select_new(cands(200), KNOWN_EMPTY, set())
        report1 = f.build_report(week1, [], [])
        self.assertIn("…and 150 more", report1)            # only 50 rows visible
        prev = self.roundtrip(report1)
        week2 = f.select_new(cands(200) + cands(1, "Brand new"), KNOWN_EMPTY, set(prev))
        fresh = [c["name"] for c in week2 if c["fresh"]]
        self.assertEqual(fresh, ["Brand new 00000 CT"])      # was: 151 (every cut row re-flagged)

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
