#!/usr/bin/env python3
"""Track new open radiology datasets by querying source APIs and diffing against
the catalog. Best-effort: each source is queried independently and failures are
skipped so the report is always produced.

Sources: Hugging Face Datasets, TCIA collections, Zenodo, Grand Challenge.
Run in CI (network required). Prints a Markdown report of candidate datasets not
yet in data/datasets.json for human review; the GitHub Action opens/updates an issue.

Usage: python scripts/find_new_datasets.py [--limit N]
"""
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"

# radiology-relevance keywords (title/description must contain at least one)
RELEVANT = re.compile(
    r"\b(radiolog|\bct\b|computed tomog|\bmri\b|magnetic reson|\bpet\b|x-?ray|"
    r"radiograph|mammograph|tomosynthesis|dicom|nifti|chest|brain|tumor|tumour|"
    r"lesion|lung|cardiac|abdomen|prostate|vertebra|spine|nodule|segmentation)\b",
    re.I,
)
# exclude obvious non-radiology modalities
EXCLUDE = re.compile(
    r"\b(histopatholog|whole slide|dermoscop|fundus|retina|oct\b|endoscop|"
    r"ultrasound echocardio|ecg|eeg|audio|speech|genom|protein)\b", re.I,
)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def get_json(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "radiology-dataset-hub-tracker"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def load_known():
    ds = json.loads(DATA.read_text())
    names = {norm(d["name"]) for d in ds}
    names |= {norm(d.get("full_name")) for d in ds if d.get("full_name")}
    urls = {(d.get("url") or "").lower().rstrip("/") for d in ds}
    slugs = set()
    for u in urls:
        for part in re.split(r"[/:]", u):
            if len(part) > 4:
                slugs.add(norm(part))
    # short canonical tokens used for substring matching to catch reuploads
    short = {k for k in names if 5 <= len(k) <= 24}
    return names, slugs, short


def is_known(key, names, slugs, short):
    if not key or key in names or key in slugs:
        return True
    # reupload/mirror under a different account: canonical name embedded in the id
    for k in short:
        if k in key or (len(key) >= 6 and key in k):
            return True
    return False


def relevant(*texts):
    blob = " ".join(t for t in texts if t)
    return bool(RELEVANT.search(blob)) and not EXCLUDE.search(blob)


def huggingface(limit, min_downloads=50, min_likes=3):
    """Only surface established datasets (enough downloads/likes) to cut reupload noise."""
    out = []
    terms = ["radiology", "CT scan", "MRI", "chest x-ray", "medical imaging segmentation",
             "PET CT", "DICOM", "brain MRI", "mammography"]
    seen = set()
    for term in terms:
        url = ("https://huggingface.co/api/datasets?full=true&limit=%d&sort=downloads&direction=-1&search=%s"
               % (limit, urllib.parse.quote(term)))
        try:
            for d in get_json(url):
                did = d.get("id", "")
                if did in seen:
                    continue
                seen.add(did)
                dl, likes = d.get("downloads", 0) or 0, d.get("likes", 0) or 0
                if dl < min_downloads and likes < min_likes:
                    continue
                desc = (d.get("description") or "") + " " + " ".join(d.get("tags", []))
                if relevant(did, desc):
                    out.append({"name": did.split("/")[-1], "id": did,
                                "url": "https://huggingface.co/datasets/" + did,
                                "source": "HuggingFace", "pop": f"{dl}⬇ {likes}♥"})
        except Exception as e:
            print(f"  (HuggingFace '{term}' skipped: {e})", file=sys.stderr)
    return out


def tcia():
    try:
        url = "https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues"
        data = get_json(url)
        return [{"name": c.get("Collection"), "id": c.get("Collection"),
                 "url": "https://www.cancerimagingarchive.net/collections/", "source": "TCIA"}
                for c in data if c.get("Collection")]
    except Exception as e:
        print(f"  (TCIA skipped: {e})", file=sys.stderr)
        return []


def zenodo(limit):
    out = []
    try:
        url = ("https://zenodo.org/api/records?q=%s&size=%d&type=dataset&sort=newest"
               % (urllib.parse.quote("radiology CT MRI imaging dataset"), limit))
        data = get_json(url)
        for h in data.get("hits", {}).get("hits", []):
            md = h.get("metadata", {})
            title = md.get("title", "")
            if relevant(title, md.get("description", "")):
                out.append({"name": title[:80], "id": str(h.get("id")),
                            "url": h.get("links", {}).get("self_html") or h.get("doi_url", ""),
                            "source": "Zenodo"})
    except Exception as e:
        print(f"  (Zenodo skipped: {e})", file=sys.stderr)
    return out


def grand_challenge(limit):
    out = []
    try:
        url = "https://grand-challenge.org/api/v1/challenges/?limit=%d" % limit
        data = get_json(url)
        for c in data.get("results", []):
            title = c.get("title", "") or c.get("short_name", "")
            desc = c.get("description", "")
            if relevant(title, desc):
                out.append({"name": title, "id": c.get("slug", title),
                            "url": c.get("url", "https://grand-challenge.org/challenges/"),
                            "source": "GrandChallenge"})
    except Exception as e:
        print(f"  (GrandChallenge skipped: {e})", file=sys.stderr)
    return out


def main():
    limit = 100
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    known_names, known_slugs, known_short = load_known()

    candidates = []
    candidates += huggingface(limit)
    candidates += tcia()
    candidates += zenodo(limit)
    candidates += grand_challenge(limit)

    new, seen = [], set()
    for c in candidates:
        key = norm(c["name"])
        if not key or key in seen:
            continue
        if is_known(key, known_names, known_slugs, known_short):
            continue
        seen.add(key)
        new.append(c)

    by_src = {}
    for c in new:
        by_src.setdefault(c["source"], []).append(c)

    print(f"# Candidate radiology datasets not yet in the catalog ({len(new)})\n")
    print("_Auto-generated by `scripts/find_new_datasets.py`. Heuristic — review each before adding; "
          "some may be out of scope, duplicates under another name, or non-open._\n")
    for src in sorted(by_src):
        print(f"## {src} ({len(by_src[src])})\n")
        for c in sorted(by_src[src], key=lambda x: x["name"].lower()):
            pop = f" — `{c['pop']}`" if c.get("pop") else ""
            print(f"- [{c['name']}]({c['url']}){pop}")
        print()
    if not new:
        print("_No new candidates found this run._")


if __name__ == "__main__":
    main()
