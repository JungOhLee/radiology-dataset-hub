#!/usr/bin/env python3
"""Track new open radiology datasets by querying source APIs and diffing against
the catalog. Best-effort: each source is queried independently and failures are
skipped so the report is always produced.

Sources: Hugging Face Datasets, TCIA collections, Zenodo (newest + most-viewed
back-catalog), Grand Challenge, Kaggle datasets (unauthenticated), Kaggle
competitions (needs KAGGLE_USERNAME/KAGGLE_KEY), PhysioNet, OpenNeuro.
Run in CI (network required). Prints a Markdown report of candidate datasets not
yet in data/datasets.json for human review; the GitHub Action opens/updates an issue.

Usage: python scripts/find_new_datasets.py [--limit N] [--prev PREV_REPORT.md]
  --prev: previous report (e.g. the current issue body); candidates whose URL was
          not in it are flagged 🆕 so weekly reviews only need to scan new rows.
"""
import base64
import json
import os
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
    r"lesion|lung|cardiac|abdomen|abdominal|prostate|vertebra|spine|nodule|segmentation|"
    r"liver|hepatic|kidney|renal|pancrea|spleen|knee|shoulder|hip|bone|breast|"
    r"stroke|aneurysm|fracture|osteo|meniscus|glioma|carcinoma|metasta|"
    r"biobank|cohort|population imaging|body composition|\bdxa\b|dexa|"
    r"epidemiolog|phenotyp|opportunistic|sarcopenia|whole-?body)\b",
    re.I,
)

# OpenNeuro is dominated by task-fMRI cognitive studies; only surface records that
# look clinical/pathological (the radiology-relevant slice of BIDS neuroimaging).
CLINICAL = re.compile(
    r"\b(lesion|tumou?r|glioma|stroke|epilep|sclerosis|alzheim|parkinson|dementia|"
    r"clinical|patient|trauma|injur|carcinoma|cancer|hemorrhage|haemorrhage|"
    r"aneurysm|hydrocephalus|schizophren|psychosis|depressi|disorder)\b", re.I,
)

# Curated "must-have" resources across categories — especially application-access
# population cohorts that the dataset-repository APIs above do NOT surface. The
# tracker flags any of these that are missing from the catalog so a whole class of
# datasets (e.g. large imaging cohorts with clinical linkage) can't be silently missed.
WATCHLIST = [
    ("NAKO German National Cohort", "https://nako.de/"),
    ("SHIP (Study of Health in Pomerania)", "https://www.fvcm.med.uni-greifswald.de/"),
    ("Rhineland Study", "https://www.rheinland-studie.de/"),
    ("Rotterdam Study", "https://www.ergo-onderzoek.nl/"),
    ("Generation R", "https://generationr.nl/"),
    ("Lifelines", "https://www.lifelines.nl/"),
    ("Maastricht Study", "https://www.demaastrichtstudie.nl/"),
    ("ALSPAC", "http://www.bristol.ac.uk/alspac/"),
    ("HUNT Study", "https://www.ntnu.edu/hunt"),
    ("Tromso Study", "https://uit.no/research/tromsostudy"),
    ("Hamburg City Health Study", "https://www.uke.de/hchs"),
    ("MESA (Multi-Ethnic Study of Atherosclerosis)", "https://www.mesa-nhlbi.org/"),
    ("CARDIA", "https://www.cardia.dopm.uab.edu/"),
    ("Framingham Heart Study", "https://www.framinghamheartstudy.org/"),
    ("Jackson Heart Study", "https://www.jacksonheartstudy.org/"),
    ("ARIC", "https://sites.cscc.unc.edu/aric/"),
    ("COPDGene", "http://www.copdgene.org/"),
    ("SPIROMICS", "https://www.spiromics.org/"),
    ("NHANES (whole-body DXA)", "https://www.cdc.gov/nchs/nhanes/"),
    ("BioBank Japan", "https://biobankjp.org/"),
    ("China Kadoorie Biobank", "https://www.ckbiobank.org/"),
    ("KoGES (Korean Genome Epidemiology Study)", "https://www.nih.go.kr/"),
    ("Taiwan Biobank", "https://www.twbiobank.org.tw/"),
    ("AGES-Reykjavik", "https://hjarta.is/en/"),
    ("Qatar Biobank", "https://www.qatarbiobank.org.qa/"),
    ("All of Us Research Program", "https://allofus.nih.gov/"),
    ("NHLBI BioLINCC", "https://biolincc.nhlbi.nih.gov/"),
    ("dbGaP", "https://www.ncbi.nlm.nih.gov/gap/"),
]
# exclude obvious non-radiology modalities
EXCLUDE = re.compile(
    r"\b(histopatholog|whole slide|dermoscop|fundus|retina|oct\b|endoscop|"
    r"ultrasound echocardio|ecg|eeg|audio|speech|genom|protein)\b", re.I,
)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def get_json(url, timeout=25, headers=None, data=None):
    h = {"User-Agent": "radiology-dataset-hub-tracker"}
    h.update(headers or {})
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, headers=h, data=body)
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
    # canonical tokens used for substring matching to catch reuploads; min length 8 so
    # short generic names ("ATLAS", "BraTS") can't swallow unrelated new candidates
    short = {k for k in names if 8 <= len(k) <= 24}
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
    """Per search term, two passes: newest uploads (weekly diff) + most-viewed
    (back-catalog — a popular dataset published years ago, e.g. Duke Liver, never
    shows up under sort=newest, so without this pass it can be missed forever).
    Narrow modality/organ terms matter: broad queries bury mid-popularity records
    below the 25-per-page unauthenticated cap."""
    out, seen = [], set()
    size = min(limit, 25)   # unauthenticated Zenodo caps page size at 25 (400 above that)
    terms = ["radiology dataset", "medical imaging dataset", "CT dataset", "MRI dataset",
             "x-ray dataset", "PET dataset", "brain MRI", "liver MRI", "cardiac MRI",
             "chest x-ray", "abdominal CT", "mammography"]
    for term in terms:
        for sort in ("newest", "mostviewed"):
            try:
                url = ("https://zenodo.org/api/records?q=%s&size=%d&type=dataset&sort=%s"
                       % (urllib.parse.quote(term), size, sort))
                data = get_json(url)
                for h in data.get("hits", {}).get("hits", []):
                    if h.get("id") in seen:
                        continue
                    seen.add(h.get("id"))
                    md = h.get("metadata", {})
                    title = md.get("title", "")
                    if relevant(title, md.get("description", "")):
                        views = int((h.get("stats") or {}).get("views") or 0)
                        out.append({"name": title[:80], "id": str(h.get("id")),
                                    "url": h.get("links", {}).get("self_html") or h.get("doi_url", ""),
                                    "source": "Zenodo", "pop": f"{views}👁" if views else ""})
            except Exception as e:
                print(f"  (Zenodo '{term}'/{sort} skipped: {e})", file=sys.stderr)
    return out


def kaggle_datasets(limit, min_downloads=100):
    """Unauthenticated (verified): /api/v1/datasets/list. 20 items/page, so honor
    `limit` by paging (capped at 3 pages/query). Download threshold cuts the heavy
    personal-reupload noise on Kaggle."""
    out, seen = [], set()
    terms = ["radiology", "CT scan", "MRI", "chest x-ray", "mammography", "medical imaging"]
    pages = max(1, min(3, (limit + 19) // 20))
    for term in terms:
        for sort in ("votes", "updated"):
            for page in range(1, pages + 1):
                try:
                    url = ("https://www.kaggle.com/api/v1/datasets/list?search=%s&sortBy=%s&page=%d"
                           % (urllib.parse.quote(term), sort, page))
                    batch = get_json(url)
                except Exception as e:
                    print(f"  (Kaggle datasets '{term}'/{sort} p{page} skipped: {e})", file=sys.stderr)
                    break
                if not batch:
                    break
                for d in batch:
                    ref = d.get("ref", "")
                    if not ref or ref in seen:
                        continue
                    seen.add(ref)
                    dl = d.get("downloadCount", 0) or 0
                    if dl < min_downloads:
                        continue
                    if relevant(d.get("title", ""), d.get("subtitle", ""), ref):
                        out.append({"name": d.get("title") or ref, "id": ref,
                                    "url": d.get("url") or "https://www.kaggle.com/datasets/" + ref,
                                    "source": "Kaggle datasets", "pop": f"{dl}⬇"})
    return out


def kaggle_competitions():
    """Kaggle's competitions API rejects unauthenticated calls; needs the API token
    (repo secrets KAGGLE_USERNAME / KAGGLE_KEY -> HTTP Basic). Skips silently when
    unset so local runs still work."""
    user, key = os.environ.get("KAGGLE_USERNAME"), os.environ.get("KAGGLE_KEY")
    if not (user and key):
        print("  (Kaggle competitions skipped: KAGGLE_USERNAME/KAGGLE_KEY not set)", file=sys.stderr)
        return []
    auth = {"Authorization": "Basic " + base64.b64encode(f"{user}:{key}".encode()).decode()}
    out, seen = [], set()
    for term in ["radiology", "MRI", "CT", "x-ray", "medical imaging"]:
        try:
            url = "https://www.kaggle.com/api/v1/competitions/list?search=" + urllib.parse.quote(term)
            for c in get_json(url, headers=auth):
                ref = c.get("ref") or c.get("url") or ""
                if not ref or ref in seen:
                    continue
                seen.add(ref)
                if relevant(c.get("title", ""), c.get("description", ""), ref):
                    out.append({"name": c.get("title") or ref, "id": ref,
                                "url": c.get("url") or "https://www.kaggle.com/competitions/" + str(ref).split("/")[-1],
                                "source": "Kaggle competitions",
                                "pop": (c.get("deadline") or "")[:10]})
        except Exception as e:
            print(f"  (Kaggle competitions '{term}' skipped: {e})", file=sys.stderr)
    return out


def physionet():
    """Unauthenticated (verified): one call returns the full published-project
    catalog (~700 records); filter to imaging-relevant databases client-side."""
    out = []
    try:
        data = get_json("https://physionet.org/api/v1/project/published/")
        for p in data:
            if p.get("resource_type") not in ("Database", "Challenge"):
                continue
            title = p.get("title", "")
            if relevant(title, p.get("short_description", ""), p.get("abstract", "")):
                slug, ver = p.get("slug", ""), p.get("version", "")
                out.append({"name": title[:80], "id": slug,
                            "url": p.get("source_url") or f"https://physionet.org/content/{slug}/{ver}/",
                            "source": "PhysioNet", "pop": p.get("publish_date", "")})
    except Exception as e:
        print(f"  (PhysioNet skipped: {e})", file=sys.stderr)
    return out


def openneuro(limit):
    """Unauthenticated GraphQL (verified). Only clinical/pathology records — the
    bulk of OpenNeuro is task-fMRI cognitive studies out of catalog scope."""
    out = []
    query = ("query { datasets(first: %d, orderBy: {publishDate: descending}, "
             "filterBy: {public: true}) { edges { node { id publishDate "
             "latestSnapshot { description { Name } summary { modalities } } } } } }" % min(limit, 100))
    try:
        data = get_json("https://openneuro.org/crn/graphql", data={"query": query})
        for e in (data.get("data", {}).get("datasets", {}) or {}).get("edges", []):
            node = (e or {}).get("node") or {}
            snap = node.get("latestSnapshot") or {}
            name = ((snap.get("description") or {}).get("Name") or "").strip()
            if name and CLINICAL.search(name):
                out.append({"name": name[:80], "id": node.get("id", ""),
                            "url": "https://openneuro.org/datasets/" + node.get("id", ""),
                            "source": "OpenNeuro", "pop": (node.get("publishDate") or "")[:10]})
    except Exception as e:
        print(f"  (OpenNeuro skipped: {e})", file=sys.stderr)
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


def load_prev_names(path):
    """Candidate names already listed in the previous report (the current issue
    body), so this run can flag first-time candidates with 🆕. Keyed on the link
    TEXT, not the URL: some sources (TCIA) share one landing URL across candidates."""
    try:
        text = pathlib.Path(path).read_text(errors="replace")
    except OSError:
        return set()
    # link text may contain \[ \] escapes (we emit them); norm() strips the backslashes
    return {norm(t) for t in re.findall(r"\[((?:\\.|[^\]\\])+)\]\(https?://", text)}


def arg_value(flag):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
        print(f"  ({flag} ignored: missing value)", file=sys.stderr)
    return None


def main():
    limit = int(arg_value("--limit") or 100)
    prev = arg_value("--prev")
    prev_names = load_prev_names(prev) if prev else set()
    known_names, known_slugs, known_short = load_known()

    candidates = []
    candidates += huggingface(limit)
    candidates += tcia()
    candidates += zenodo(limit)
    candidates += grand_challenge(limit)
    candidates += kaggle_datasets(limit)
    candidates += kaggle_competitions()
    candidates += physionet()
    candidates += openneuro(limit)

    new, seen = [], set()
    for c in candidates:
        key = norm(c["name"])
        if not key or key in seen:
            continue
        if is_known(key, known_names, known_slugs, known_short):
            continue
        seen.add(key)
        c["fresh"] = bool(prev_names) and key not in prev_names
        new.append(c)

    by_src = {}
    for c in new:
        by_src.setdefault(c["source"], []).append(c)

    # curated watchlist: important resources (esp. population cohorts) that are missing
    missing_watch = [(nm, url) for nm, url in WATCHLIST
                     if not is_known(norm(nm.split("(")[0]), known_names, known_slugs, known_short)]

    print(f"# Candidate radiology datasets not yet in the catalog ({len(new)})\n")
    print("_Auto-generated by `scripts/find_new_datasets.py`. Heuristic — review each before adding; "
          "some may be out of scope, duplicates under another name, or non-open._\n")

    print(f"## ⚠️ Must-have resources still missing — curated watchlist ({len(missing_watch)})\n")
    if missing_watch:
        print("_High-value resources (esp. application-access population cohorts) that the dataset "
              "APIs don't surface. These should almost certainly be added._\n")
        for nm, url in missing_watch:
            print(f"- [{nm}]({url})")
    else:
        print("_All watchlist resources are in the catalog. ✅_")
    print()
    n_fresh = sum(1 for c in new if c.get("fresh"))
    if prev_names:
        print(f"_{n_fresh} candidate(s) marked 🆕 were not in the previous report — review those first._\n")
    MAX_ROWS = 50   # per source; keeps the report under GitHub's 65,536-char issue-body cap
    for src in sorted(by_src):
        print(f"## {src} ({len(by_src[src])})\n")
        # first-time candidates first, then alphabetical
        rows = sorted(by_src[src], key=lambda x: (not x.get("fresh"), x["name"].lower()))
        for c in rows[:MAX_ROWS]:
            pop = f" — `{c['pop']}`" if c.get("pop") else ""
            mark = "🆕 " if c.get("fresh") else ""
            name = c["name"].replace("[", "\\[").replace("]", "\\]")
            print(f"- {mark}[{name}]({c['url']}){pop}")
        if len(rows) > MAX_ROWS:
            print(f"- _…and {len(rows) - MAX_ROWS} more from {src} not shown (🆕 items always shown first)._")
        print()
    if not new:
        print("_No new candidates found this run._")


if __name__ == "__main__":
    main()
