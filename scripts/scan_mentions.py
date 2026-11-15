#!/usr/bin/env python3
"""List datasets that your own notes mention but the catalog doesn't have.

Research projects discuss and download datasets (study plans, data protocols,
download guides) long before anyone adds them to data/datasets.json; this closes
that gap. It reads Markdown/text notes under the given folders, pulls out links to
dataset hosts (TCIA, PhysioNet, Zenodo, figshare, Hugging Face datasets, Grand
Challenge, Kaggle, OpenNeuro, AWS Open Data, Stanford AIMI, VinDr, FRDR, BIMCV,
RSNA MIRA, Science Data Bank, Dataverse, Dryad, Synapse) and reports the ones whose
identifier appears nowhere in the catalog. Only link targets and file paths are
printed, never note contents. Runs locally (the CI tracker can't see your notes).

Usage: python3 scripts/scan_mentions.py DIR [DIR ...] [--min-files N]
Folders named phi, Vault, data, outputs, logs, node_modules and dot-folders are skipped.
"""
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"
SKIP_DIRS = {"phi", "vault", "data", "outputs", "logs", "node_modules", "__pycache__", "zz_archive"}
EXTS = {".md", ".txt", ".markdown"}

# (host label, regex with one group = the identifier that should appear in the catalog)
PATTERNS = [
    ("TCIA", r"cancerimagingarchive\.net/(?:collection|analysis-result)/([a-z0-9-]+)"),
    ("PhysioNet", r"physionet\.org/(?:content|files)/([a-z0-9-]+)"),
    ("Zenodo", r"zenodo\.org/(?:records?|doi/10\.5281/zenodo\.)/?(\d{5,})"),
    ("figshare", r"figshare\.com/(?:articles/(?:dataset/)?[^/\s)]+/|collections/[^/\s)]+/)(\d{6,})"),
    ("Hugging Face", r"huggingface\.co/datasets/([\w.-]+/[\w.-]+)"),
    ("Grand Challenge", r"https?://([a-z0-9-]+)\.grand-challenge\.org"),
    ("Kaggle", r"kaggle\.com/(?:c|competitions|datasets/[\w-]+)/([\w-]+)"),
    ("OpenNeuro", r"(?:openneuro\.org/datasets/|OpenNeuroDatasets/)(ds\d{6})"),
    ("AWS Open Data", r"registry\.opendata\.aws/([a-z0-9-]+)"),
    ("Stanford AIMI", r"aimi\.stanford\.edu/datasets/([\w-]+)"),
    ("VinDr", r"vindr\.ai/datasets/([a-z0-9-]+)"),
    ("FRDR", r"doi\.org/(10\.20383/[\d.]+)"),
    ("BIMCV", r"bimcv\.cipf\.es/bimcv-projects/([a-z0-9-]+)"),
    ("RSNA MIRA", r"mira\.rsna\.org/dataset/(\d+)"),
    ("Science Data Bank", r"scidb\.cn/(?:en/)?detail\?dataSetId=([\w-]+)"),
    ("Dataverse", r"dataverse\.[\w.]+/dataset\.xhtml\?persistentId=(doi:[\w./-]+)"),
    ("Dryad", r"datadryad\.org/(?:stash/)?dataset/(doi:[\w./-]+)"),
    ("Synapse", r"synapse\.org/#?!?Synapse:(syn\d+)"),
]
PATTERNS = [(h, re.compile(p, re.I)) for h, p in PATTERNS]
# hub/portal landing pages are not datasets
GENERIC = {"collections", "datasets", "shared-datasets", "bimcv-projects", "padchest", "browse-collections"}


def walk(root):
    for p in pathlib.Path(root).expanduser().rglob("*"):
        if any(part.lower() in SKIP_DIRS or part.startswith(".") for part in p.relative_to(root).parts[:-1]):
            continue
        if p.is_file() and p.suffix.lower() in EXTS:
            yield p


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    min_files = 1
    if "--min-files" in sys.argv:
        min_files = int(sys.argv[sys.argv.index("--min-files") + 1])
    if not args:
        sys.exit(__doc__)
    hay = DATA.read_text().lower()
    triage = ROOT / "data" / "triage.json"   # reviewed and rejected/deferred links stay quiet
    if triage.exists():
        hay += triage.read_text().lower()
    hits = defaultdict(lambda: {"host": "", "url": "", "files": set()})
    for root in args:
        root = pathlib.Path(root).expanduser()
        for f in walk(root):
            try:
                text = f.read_text(errors="ignore")
            except OSError:
                continue
            for host, rx in PATTERNS:
                for m in rx.finditer(text):
                    ident = m.group(1).rstrip(".,;:)").lower()
                    if ident in GENERIC:
                        continue
                    h = hits[(host, ident)]
                    h["host"], h["url"] = host, h["url"] or m.group(0)
                    h["files"].add(str(f.relative_to(root.parent)))
    missing = [(k, v) for k, v in hits.items()
               if k[1] not in hay and k[1].split("/")[-1] not in hay and len(v["files"]) >= min_files]
    missing.sort(key=lambda kv: (-len(kv[1]["files"]), kv[0]))
    print(f"# Dataset links in notes that are not in the catalog ({len(missing)} of {len(hits)} linked)\n")
    print("| Host | Identifier | Link | Mentioned in |\n| --- | --- | --- | --- |")
    for (host, ident), v in missing:
        files = sorted(v["files"])
        shown = ", ".join(files[:3]) + (f" (+{len(files) - 3})" if len(files) > 3 else "")
        url = v["url"] if v["url"].startswith("http") else "https://" + v["url"]
        print(f"| {host} | `{ident}` | {url} | {shown} |")
    print("\n_Vet each (some links are tools, papers or mirrors), then add it to data/datasets.json "
          "or record a decision in data/triage.json._")


if __name__ == "__main__":
    main()
