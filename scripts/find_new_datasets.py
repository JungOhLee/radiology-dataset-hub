#!/usr/bin/env python3
"""Track new open radiology datasets by querying source APIs and diffing against
the catalog. Best-effort: each source is queried independently and failures are
skipped so the report is always produced.

Sources: catalog publishers (Hugging Face orgs / GitHub owners that already publish
a dataset in the catalog — e.g. AbdomenAtlas, MrGiovanni), Hugging Face Datasets
(repo-id search + card-tag filters), GitHub repository search, TCIA collections,
Zenodo (newest + most-viewed back-catalog), Grand Challenge, Kaggle datasets
(unauthenticated), Kaggle competitions (needs KAGGLE_USERNAME/KAGGLE_KEY),
PhysioNet, OpenNeuro. Optional GITHUB_TOKEN / HF_TOKEN raise API rate limits.
Run in CI (network required). Prints a Markdown report of candidate datasets not
yet in data/datasets.json for human review; the GitHub Action opens/updates an issue.

Usage: python scripts/find_new_datasets.py [--limit N] [--prev PREV_REPORT.md]
  --prev: previous report (e.g. the current issue body); candidates never listed in
          an earlier report are flagged 🆕 so weekly reviews only need to scan new
          rows. The report carries its full seen-set in a hidden comment, so rows cut
          by the per-source display cap don't come back as 🆕 the following week.
"""
import base64
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"
HF_DATASET = "https://huggingface.co/datasets/"
GH_API = "https://api.github.com"

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

# What's left of a candidate name after removing a catalog name, when that residue
# marks a new version/extension rather than a mirror: Merlin -> Merlin+ / MerlinPlus,
# TotalSegmentator -> TotalSegmentator v3, BraTS -> BraTS 2026, X -> X-MRI.
DERIVATIVE = re.compile(r"plus|v?\d{1,2}|20\d\d|ext|extended|extension|xl|large|next|"
                        r"pro|ii|iii|iv|mri|ct|pet|cxr|3d|4d")

# GitHub hosts mostly code; a repo counts as a dataset release only if it says so
DATASETISH = re.compile(r"\b(datasets?|benchmark|annotations?|masks?|cohort|"
                        r"collection|corpus|atlas)\b", re.I)

# Publishers whose datasets are in the catalog under a non-HF/GitHub URL (Merlin is
# linked on stanfordaimi.azurewebsites.net), so catalog_publishers() can't see them.
EXTRA_HF_PUBLISHERS = ["stanfordmimi"]
EXTRA_GITHUB_PUBLISHERS = ["StanfordMIMI"]
PUBLISHER_LOOKBACK_DAYS = 365      # publisher watch: repos created in the last year
GITHUB_SEARCH_LOOKBACK_DAYS = 120  # GitHub search: repos created in the last ~4 months


def norm(s):
    # "+" is meaningful in dataset names (fastMRI+, Merlin+): spell it out so
    # "Merlin+" matches "MerlinPlus" instead of colliding with "Merlin"
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower().replace("+", "plus"))


def get_json(url, timeout=25, headers=None, data=None):
    h = {"User-Agent": "radiology-dataset-hub-tracker"}
    h.update(headers or {})
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, headers=h, data=body)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def hf_auth():
    tok = os.environ.get("HF_TOKEN")
    return {"Authorization": "Bearer " + tok} if tok else {}


def gh_auth():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        h["Authorization"] = "Bearer " + tok
    return h


def load_catalog():
    return json.loads(DATA.read_text())


def load_known(ds=None):
    ds = load_catalog() if ds is None else ds
    display = {}   # norm key -> catalog display name (to say what a derivative extends)
    for d in ds:
        for n in (d.get("full_name"), d["name"]):   # name wins on a clash
            if n:
                display[norm(n)] = d["name"]
    names = set(display)
    urls = {(d.get("url") or "").lower().rstrip("/") for d in ds}
    slugs = set()
    for u in urls:
        for part in re.split(r"[/:]", u):
            if len(part) > 4:
                slugs.add(norm(part))
    # canonical tokens used for substring matching to catch reuploads; min length 8 so
    # short generic names ("ATLAS", "BraTS") can't swallow unrelated new candidates
    short = {k for k in names if 8 <= len(k) <= 24}
    return names, slugs, short, display


def classify(key, names, slugs, short):
    """("known", None): in the catalog, or a mirror/reupload of a catalog dataset.
    ("derivative", base): a catalog name + version/extension marker (DERIVATIVE) —
      likely a new release building on catalog dataset `base`, so it must surface.
    (None, None): unrelated to the catalog."""
    if not key or key in names or key in slugs:
        return "known", None
    # longest catalog name the candidate starts with: "totalsegmentatormriv2" extends
    # "TotalSegmentator MRI" (residue v2), not "TotalSegmentator" (residue mriv2)
    bases = [k for k in names if len(k) >= 4 and key.startswith(k)
             and DERIVATIVE.fullmatch(key[len(k):])]
    if bases:
        return "derivative", max(bases, key=len)
    # reupload/mirror under a different account: canonical name embedded in the id
    for k in short:
        if k in key or (len(key) >= 6 and key in k):
            return "known", None
    return None, None


def is_known(key, names, slugs, short):
    return classify(key, names, slugs, short)[0] is not None


def relevant(*texts):
    blob = " ".join(t for t in texts if t)
    return bool(RELEVANT.search(blob)) and not EXCLUDE.search(blob)


def catalog_publishers(ds):
    """HF orgs and GitHub owners that already publish a dataset in the catalog. A
    group that released one catalog dataset tends to release follow-ups (AbdomenAtlas
    -> PanTS -> Merlin Plus), and those are the likeliest true positives."""
    hf, gh = {}, {}
    for d in ds:
        u = d.get("url") or ""
        m = re.match(r"https?://huggingface\.co/datasets/([\w.-]+)/", u)
        if m:
            hf.setdefault(m.group(1).lower(), m.group(1))
        m = re.match(r"https?://github\.com/([\w-]+)/", u)
        if m and m.group(1).lower() not in ("orgs", "topics", "features", "sponsors"):
            gh.setdefault(m.group(1).lower(), m.group(1))
    for a in EXTRA_HF_PUBLISHERS:
        hf.setdefault(a.lower(), a)
    for a in EXTRA_GITHUB_PUBLISHERS:
        gh.setdefault(a.lower(), a)
    return sorted(hf.values(), key=str.lower), sorted(gh.values(), key=str.lower)


def days_ago(n):
    return (datetime.date.today() - datetime.timedelta(days=n)).isoformat()


def huggingface(limit, min_downloads=50, min_likes=3):
    """Only surface established datasets (enough downloads/likes) to cut reupload noise.
    `search` matches the repo id only (owner/name), so it finds ids like
    "x/brain-mri" but never research releases with non-generic names
    (AbdomenAtlas/MerlinPlus); card-tag filters catch those by what the card
    declares, newest-first as well as most-downloaded."""
    out = []
    terms = ["radiology", "CT scan", "MRI", "chest x-ray", "medical imaging segmentation",
             "PET CT", "DICOM", "brain MRI", "mammography"]
    # no "pet" tag: it means pets, and RELEVANT's \bpet\b would let those through
    tags = ["radiology", "medical-imaging", "ct", "ct-scan", "computed-tomography", "mri",
            "x-ray", "chest-x-ray", "mammography"]
    queries = [("search", t, "downloads") for t in terms]
    queries += [("filter", t, sort) for t in tags for sort in ("downloads", "createdAt")]
    seen = set()
    for param, value, sort in queries:
        url = ("https://huggingface.co/api/datasets?full=true&limit=%d&sort=%s&direction=-1&%s=%s"
               % (limit, sort, param, urllib.parse.quote(value)))
        try:
            for d in get_json(url, headers=hf_auth()):
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
                                "url": HF_DATASET + did,
                                "source": "HuggingFace", "pop": f"{dl}⬇ {likes}♥"})
        except Exception as e:
            print(f"  (HuggingFace {param}='{value}'/{sort} skipped: {e})", file=sys.stderr)
    return out


def hf_publishers(authors, since):
    """Recent datasets from HF orgs that already publish catalog datasets. No
    download/like floor: a release is worth reviewing on day one, before it has any."""
    out = []
    for a in authors:
        url = ("https://huggingface.co/api/datasets?author=%s&full=true&limit=50&sort=createdAt&direction=-1"
               % urllib.parse.quote(a))
        try:
            data = get_json(url, headers=hf_auth())
        except Exception as e:
            print(f"  (HuggingFace publisher '{a}' skipped: {e})", file=sys.stderr)
            continue
        for d in data:
            created = (d.get("createdAt") or "")[:10]
            if created and created < since:
                continue
            did = d.get("id", "")
            desc = (d.get("description") or "") + " " + " ".join(d.get("tags", []))
            if relevant(did, desc):
                out.append({"name": did.split("/")[-1], "id": did, "url": HF_DATASET + did,
                            "source": "HuggingFace", "publisher": a,
                            "pop": " · ".join(x for x in (a, created) if x)})
    return out


def github_repo(r, source="GitHub", publisher=None):
    topics = " ".join(r.get("topics") or [])
    desc = r.get("description") or ""
    if r.get("fork") or r.get("archived"):
        return None
    if not (relevant(r.get("name", ""), desc, topics) and DATASETISH.search(f"{r.get('name', '')} {desc} {topics}")):
        return None
    created = (r.get("created_at") or "")[:10]
    stars = r.get("stargazers_count", 0) or 0
    c = {"name": r.get("name", ""), "id": r.get("full_name", ""), "url": r.get("html_url", ""),
         "source": source, "pop": " · ".join(x for x in (publisher, created, f"{stars}★") if x)}
    if publisher:
        c["publisher"] = publisher
    return c


def github_publishers(owners, since):
    """Recent dataset repos from GitHub owners that already publish catalog datasets
    (e.g. MrGiovanni: AbdomenAtlas, PanTS -> MerlinPlus). /users/{name}/repos serves
    both user and organization accounts."""
    out = []
    for o in owners:
        url = "%s/users/%s/repos?sort=created&direction=desc&per_page=30" % (GH_API, urllib.parse.quote(o))
        try:
            data = get_json(url, headers=gh_auth())
        except Exception as e:
            print(f"  (GitHub publisher '{o}' skipped: {e})", file=sys.stderr)
            continue
        for r in data:
            if (r.get("created_at") or "")[:10] < since:
                continue
            c = github_repo(r, publisher=o)
            if c:
                out.append(c)
    return out


def github_search(since):
    """New dataset repos anywhere on GitHub, top-starred first. Search allows 10
    requests/min unauthenticated (30 with GITHUB_TOKEN); this makes 7."""
    out, seen = [], set()
    terms = ["CT dataset", "MRI dataset", "X-ray dataset", "radiology dataset",
             "PET dataset", "mammography dataset", "medical imaging dataset"]
    for term in terms:
        q = f"{term} in:name,description created:>={since} fork:false"
        url = "%s/search/repositories?q=%s&sort=stars&order=desc&per_page=30" % (GH_API, urllib.parse.quote(q))
        try:
            data = get_json(url, headers=gh_auth())
        except Exception as e:
            print(f"  (GitHub search '{term}' skipped: {e})", file=sys.stderr)
            continue
        for r in data.get("items", []):
            if r.get("full_name") in seen:
                continue
            seen.add(r.get("full_name"))
            c = github_repo(r)
            if c:
                out.append(c)
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


SEEN_RE = re.compile(r"<!--\s*tracker-seen:([0-9a-f\s]*)-->")
BODY_LIMIT = 64000     # GitHub rejects issue bodies over 65,536 chars; keep headroom
MAX_ROWS = 50          # per section, shrunk automatically if the body would not fit


def khash(key):
    return hashlib.sha1(key.encode()).hexdigest()[:8]


def load_prev_seen(path):
    """Hashed keys of every candidate listed in earlier reports (the current issue
    body), newest first, so this run can flag first-time candidates with 🆕.
    Reports carry the full seen-set in a hidden `tracker-seen` comment: the visible
    rows are capped per source, so keying on them alone re-flagged every row that
    was cut last week (hundreds of false 🆕). Link TEXT (not URL: TCIA shares one
    landing URL) is still read so reports from before the comment keep working."""
    try:
        text = pathlib.Path(path).read_text(errors="replace")
    except OSError:
        return []
    out = []
    m = SEEN_RE.search(text)
    if m:
        out += m.group(1).split()
    # link text may contain \[ \] escapes (we emit them); norm() strips the backslashes
    out += [khash(norm(t)) for t in re.findall(r"\[((?:\\.|[^\]\\])+)\]\(https?://", text)]
    return list(dict.fromkeys(out))


def u16len(s):
    return len(s.encode("utf-16-le")) // 2   # GitHub counts UTF-16 code units


def row(c):
    pop = f" — `{c['pop']}`" if c.get("pop") else ""
    ext = f" · extends **{c['extends']}**" if c.get("extends") else ""
    mark = "🆕 " if c.get("fresh") else ""
    name = c["name"].replace("[", "\\[").replace("]", "\\]")
    return f"- {mark}[{name}]({c['url']}){pop}{ext}"


def section(lines, title, rows, max_rows, what, intro=None):
    lines.append(f"## {title} ({len(rows)})\n")
    if intro:
        lines.append(intro + "\n")
    # first-time candidates first, then alphabetical
    rows = sorted(rows, key=lambda x: (not x.get("fresh"), x["name"].lower()))
    lines += [row(c) for c in rows[:max_rows]]
    if len(rows) > max_rows:
        lines.append(f"- _…and {len(rows) - max_rows} more {what} not shown (🆕 items always shown first)._")
    lines.append("")


def render(new, missing_watch, have_prev, max_rows):
    lines = [f"# Candidate radiology datasets not yet in the catalog ({len(new)})\n",
             "_Auto-generated by `scripts/find_new_datasets.py`. Heuristic — review each before adding; "
             "some may be out of scope, duplicates under another name, or non-open._\n",
             f"## ⚠️ Must-have resources still missing — curated watchlist ({len(missing_watch)})\n"]
    if missing_watch:
        lines.append("_High-value resources (esp. application-access population cohorts) that the dataset "
                     "APIs don't surface. These should almost certainly be added._\n")
        lines += [f"- [{nm}]({url})" for nm, url in missing_watch]
    else:
        lines.append("_All watchlist resources are in the catalog. ✅_")
    lines.append("")
    if have_prev:
        n_fresh = sum(1 for c in new if c.get("fresh"))
        lines.append(f"_{n_fresh} candidate(s) marked 🆕 were not in any previous report — review those first._\n")
    priority = [c for c in new if c.get("priority")]
    if priority:
        section(lines, "⭐ Priority — new from catalog publishers, or extending a catalog dataset",
                priority, max_rows, "priority candidates",
                intro="_Recent releases by Hugging Face orgs / GitHub owners that already publish a "
                      "catalog dataset, and names that extend one (X → X+ / X Plus / X v2). The likeliest "
                      "real additions — review these first._")
    by_src = {}
    for c in new:
        if not c.get("priority"):
            by_src.setdefault(c["source"], []).append(c)
    for src in sorted(by_src):
        section(lines, src, by_src[src], max_rows, f"from {src}")
    if not new:
        lines.append("_No new candidates found this run._")
    return "\n".join(lines) + "\n"


def build_report(new, missing_watch, prev_seen):
    """Render the report under GitHub's issue-body cap, then append the hidden
    seen-set: this run's candidates first (all of them, so none resurfaces as 🆕
    next week), then previously seen keys newest-first as room allows — keeping
    them means a source that fails one week doesn't turn its whole backlog 🆕."""
    cur = list(dict.fromkeys(khash(c["key"]) for c in new))
    cur_set = set(cur)
    carried = [h for h in prev_seen if h not in cur_set]
    for max_rows in (MAX_ROWS, 40, 30, 20, 10, 5):
        body = render(new, missing_watch, bool(prev_seen), max_rows)
        room = (BODY_LIMIT - u16len(body) - 40) // 9   # 8 hex chars + separator each
        if room >= len(cur):
            break
    seen = (cur + carried)[:max(room, len(cur))]
    return body + "\n<!-- tracker-seen: " + " ".join(seen) + " -->\n"


def select_new(candidates, known, prev_set):
    """Drop catalog datasets and their mirrors, dedupe by name (first row wins),
    and tag each survivor: extends (catalog name it builds on), priority, fresh."""
    names, slugs, short, display = known
    new, seen = [], set()
    for c in candidates:
        key = norm(c["name"])
        if not key or key in seen:
            continue
        status, base = classify(key, names, slugs, short)
        if status == "known":
            continue
        seen.add(key)
        c["key"] = key
        c["extends"] = display.get(base)
        c["priority"] = bool(c.get("publisher") or c["extends"])
        c["fresh"] = bool(prev_set) and khash(key) not in prev_set
        new.append(c)
    return new


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
    prev_seen = load_prev_seen(prev) if prev else []
    prev_set = set(prev_seen)   # empty on the very first run: then nothing is marked 🆕
    ds = load_catalog()
    known_names, known_slugs, known_short, display = load_known(ds)
    hf_pubs, gh_pubs = catalog_publishers(ds)

    # publisher watch first: on a duplicate name across sources the first row wins,
    # and publisher rows carry the context that puts them in the priority section
    candidates = []
    candidates += hf_publishers(hf_pubs, days_ago(PUBLISHER_LOOKBACK_DAYS))
    candidates += github_publishers(gh_pubs, days_ago(PUBLISHER_LOOKBACK_DAYS))
    candidates += huggingface(limit)
    candidates += github_search(days_ago(GITHUB_SEARCH_LOOKBACK_DAYS))
    candidates += tcia()
    candidates += zenodo(limit)
    candidates += grand_challenge(limit)
    candidates += kaggle_datasets(limit)
    candidates += kaggle_competitions()
    candidates += physionet()
    candidates += openneuro(limit)

    new = select_new(candidates, (known_names, known_slugs, known_short, display), prev_set)

    # curated watchlist: important resources (esp. population cohorts) that are missing
    missing_watch = [(nm, url) for nm, url in WATCHLIST
                     if not is_known(norm(nm.split("(")[0]), known_names, known_slugs, known_short)]

    print(build_report(new, missing_watch, prev_seen), end="")


if __name__ == "__main__":
    main()
