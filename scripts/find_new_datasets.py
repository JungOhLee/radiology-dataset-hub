#!/usr/bin/env python3
"""Track new open radiology datasets by querying source APIs and diffing against
the catalog. Best-effort: each source is queried independently and failures are
skipped so the report is always produced.

Sources: catalog publishers (Hugging Face orgs / GitHub owners that already publish
a dataset in the catalog — e.g. AbdomenAtlas, MrGiovanni), Hugging Face Datasets
(repo-id search + card-tag filters), GitHub repository search, TCIA (NBIA API +
the website's collection and analysis-result listings — collections distributed
outside NBIA, e.g. CDD-CESM via Aspera, and label-only analysis results), Zenodo
(newest + most-viewed back-catalog, 2 pages), Grand Challenge, Kaggle datasets
(unauthenticated), Kaggle competitions (needs KAGGLE_USERNAME/KAGGLE_KEY),
PhysioNet, OpenNeuro, AWS Open Data Registry (RSNA / Emory / UCSF releases),
figshare, Harvard Dataverse, VinDr, and dataset papers (Scientific Data, Data in
Brief via Crossref — catches datasets hosted anywhere, incl. hosts we don't poll).
Portals without an API (RSNA MIRA, Stanford AIMI, BIMCV, Science Data Bank, FRDR)
are listed as a monthly manual checklist. data/triage.json records review
decisions so rejected candidates stop reappearing and the backlog can drain; a
rotating backlog window resurfaces rows the per-source cap would hide forever.
Optional GITHUB_TOKEN / HF_TOKEN raise API rate limits.
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
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"
HF_DATASET = "https://huggingface.co/datasets/"
GH_API = "https://api.github.com"

# radiology-relevance keywords (title/description must contain at least one). The
# whole alternation sits between \b...\b, so stems need an explicit \w* ("radiolog\w*")
# and nouns an explicit plural, or "radiology", "mammography", "tumors" never match.
RELEVANT = re.compile(
    r"\b(radiolog\w*|ct|computed[\s-]tomog\w*|mri|magnetic[\s-]reson\w*|pet|x-?rays?|"
    r"radiograph\w*|mammogra\w*|tomosynthesis|dicom|nifti|medical[\s-]imag\w*|chest|brains?|"
    r"tumou?rs?|lesions?|lungs?|cardiac|abdomen|abdominal|prostate|vertebra\w*|spine|spinal|"
    r"nodules?|segmentation|liver|hepatic|kidneys?|renal|pancrea\w*|spleen|knees?|shoulders?|"
    r"hips?|bones?|breast|stroke|aneurysms?|fractures?|osteo\w*|meniscus|gliomas?|carcinomas?|"
    r"metasta\w*|biobank|cohorts?|population imaging|body composition|dxa|dexa|"
    r"epidemiolog\w*|phenotyp\w*|opportunistic|sarcopenia|whole-?body)\b",
    re.I,
)

# explicit in-scope imaging modality: overrides EXCLUDE ("CT of histologically confirmed
# nodules") and is required of publisher-watch rows, which have no medical pre-filter
MODALITY = re.compile(
    r"\b(radiolog\w*|ct|cta|cbct|computed[\s-]tomog\w*|mri|magnetic[\s-]reson\w*|pet[\s/-]?ct|"
    r"x-?rays?|radiograph\w*|mammogra\w*|tomosynthesis|dicom|nifti|dxa|dexa)\b", re.I)

# OpenNeuro is dominated by task-fMRI cognitive studies; only surface records that
# look clinical/pathological (the radiology-relevant slice of BIDS neuroimaging).
CLINICAL = re.compile(
    r"\b(lesion|tumou?r|glioma|stroke|epilep|sclerosis|alzheim|parkinson|dementia|"
    r"clinical|patient|trauma|injur|carcinoma|cancer|hemorrhage|haemorrhage|"
    r"aneurysm|hydrocephalus|schizophren|psychosis|depressi|disorder|"
    # image-quality / artefact / test-retest sets (MR-ART was missed without these)
    r"motion|artefacts?|artifacts?|quality control|image quality|test-retest|phantom)\b", re.I,
)

# Portals with no usable listing API: printed every report as a manual checklist so a
# whole host can't drop out of sight (REVEAL-CXR on RSNA MIRA, BrainMetShare on AIMI,
# PLC-CECT on Science Data Bank, NL-Breast-Screening on FRDR were all missed this way).
PORTALS = [
    ("RSNA MIRA (RSNA datasets & benchmarks)", "https://mira.rsna.org/"),
    ("Stanford AIMI dataset index", "https://aimidatasetindex.stanford.edu/"),
    ("BIMCV projects (PadChest family)", "https://bimcv.cipf.es/bimcv-projects/"),
    ("Science Data Bank (scidb.cn) — Chinese imaging datasets", "https://www.scidb.cn/en"),
    ("FRDR (Canada) — search 'mammography', 'CT', 'MRI'", "https://www.frdr-dfdr.ca/repo/"),
    ("NCI Imaging Data Commons collections", "https://portal.imaging.datacommons.cancer.gov/explore/"),
    ("Mendeley Data — search radiology terms", "https://data.mendeley.com/"),
]

TRIAGE = ROOT / "data" / "triage.json"
BACKLOG_ROTATION = 25   # backlog rows resurfaced per report, cycling through all of them

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
# exclude obvious non-radiology modalities (unless an in-scope MODALITY is also named)
EXCLUDE = re.compile(
    r"\b(histopatholog\w*|histolog\w*|whole[\s-]slide|dermoscop\w*|fundus|retina\w*|oct|"
    r"endoscop\w*|ultrasound echocardio\w*|ecg|eeg|audio|speech|genom\w*|proteins?)\b", re.I,
)

# What's left of a candidate name after removing a catalog name, when that residue
# marks a new version/extension rather than a mirror: Merlin -> Merlin+ / MerlinPlus,
# TotalSegmentator -> TotalSegmentator v3, BraTS -> BraTS 2026, X -> X-MRI.
DERIVATIVE = re.compile(r"plus|v?\d{1,2}|20\d\d|ext|extended|extension|xl|large|next|"
                        r"pro|ii|iii|iv|mri|ct|pet|cxr|3d|4d")

# Packaging suffixes of a reformatted copy of a dataset (AMOS22-Lite, PI-CAI-preprocessed,
# X-nifti-2d): a catalog name followed only by these is a mirror, not a new release.
MIRROR_SUFFIX = re.compile(r"(?:lite|mini|subset|samples?|demo|preprocessed|processed|prepared|"
                           r"nifti|nii|npz|png|jpe?g|2d|slices|resized|mirror|reupload|"
                           r"dataset|data|hf|parquet|clean(?:ed)?)+$")

# GitHub hosts mostly code; a repo counts as a dataset release only if it introduces
# one. DATA_USE marks mentions of data the repo merely uses ("trained on a large
# corpus of chest X-rays", "detection using MRI datasets", "custom dataset loader").
DATASETISH = re.compile(r"\b(datasets?|benchmarks?|annotations?|masks?|cohorts?|"
                        r"collections?|corpus|atlas)\b", re.I)
DATA_USE = re.compile(
    r"\b(?:using|uses|use|on|from|with|of|in|for|across|into|like|trained|train|built|"
    r"evaluat\w*|tested|validated|fine-?tuned|pre-?trained)\s+(?:[\w'/+.-]+\s+){0,5}?"
    r"(?:datasets?|benchmarks?|annotations?|masks?|cohorts?|collections?|corpus|atlas)\b"
    r"|\b(?:datasets?|data)[\s_-]*loaders?\b", re.I)
MEDICAL = re.compile(r"\b(medical|clinical|patients?|hospitals?|cancers?|tumou?rs?|diseases?)\b", re.I)

# Publishers the catalog URLs don't reveal: Merlin is linked on stanfordaimi.azurewebsites.net,
# and the JHU AbdomenAtlas group also hosts data under the HF user MrGiovanni
# (AbdomenAtlas2.0Mini) while its catalog URLs point at GitHub.
EXTRA_HF_PUBLISHERS = ["stanfordmimi", "MrGiovanni"]
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


_hf_token_ok = True


def hf_get(url):
    """GET a Hugging Face API URL with the optional HF_TOKEN. A stale or revoked token
    gets 401 even on public listings, so fall back to anonymous for the rest of the
    run rather than silently losing every Hugging Face source."""
    global _hf_token_ok
    tok = os.environ.get("HF_TOKEN") if _hf_token_ok else None
    if tok:
        try:
            return get_json(url, headers={"Authorization": "Bearer " + tok})
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise
            _hf_token_ok = False
            print("  (HF_TOKEN rejected with 401 - continuing anonymously; update or remove the secret)",
                  file=sys.stderr)
    return get_json(url)


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
    cover = {}     # norm key -> tokens of that entry's names/year/modalities
    for d in ds:
        text = " ".join([d.get("full_name") or "", d["name"], str(d.get("year") or "")]
                        + list(d.get("modality") or []))
        toks = set(re.findall(r"[a-z]+|\d+", text.lower().replace("+", " plus ")))
        # aliases: paper titles and other names the same dataset is announced under
        # ("Full Field Digital Mammography Dataset from a Population Screening Program"
        # = NL-Breast-Screening), so paper/portal rows for catalog datasets drop out
        for n in (*(d.get("aliases") or []), d.get("full_name"), d["name"]):   # name wins on a clash
            if n:
                display[norm(n)] = d["name"]
                cover[norm(n)] = cover.get(norm(n), set()) | toks
    names = set(display)
    # official alternative locations (AWS registry, Zenodo record, AIMI page, mirrors) count
    # too, or the same dataset resurfaces from every host it is published on
    urls = {(u or "").lower().rstrip("/") for d in ds
            for u in [d.get("url")] + [x.get("url") for x in d.get("links") or []]}
    slugs = set()
    for u in urls:
        for part in re.split(r"[/:]", u):
            if len(part) > 4:
                slugs.add(norm(part))
    # canonical tokens used for substring matching to catch reuploads; min length 8 so
    # short generic names ("ATLAS", "BraTS") can't swallow unrelated new candidates
    short = {k for k in names if 8 <= len(k) <= 24}
    return names, slugs, short, display, cover


def known_urls(ds=None):
    """Catalog URLs plus each entry's `links` (other official locations, mirrors),
    normalised: a candidate on one of these pages is a catalog dataset."""
    ds = load_catalog() if ds is None else ds
    return {(u or "").lower().rstrip("/") for d in ds
            for u in [d.get("url")] + [x.get("url") for x in d.get("links") or []] if u}


def covered(residue, toks):
    """True if the catalog entry already covers the edition/modality the residue names:
    VerSe "(2019 & 2020)" covers VerSe'20; LiTS (2017) covers LiTS17; AMOS [CT, MRI]
    covers AMOS-MRI."""
    alts = {residue}
    m = re.fullmatch(r"v?(\d+)", residue)
    if m:
        alts |= {m.group(1), "20" + m.group(1)}
    return bool(alts & toks)


def classify(key, names, slugs, short, cover=None):
    """("known", None): in the catalog, or a mirror/reupload of a catalog dataset.
    ("derivative", base): a catalog name + version/extension marker (DERIVATIVE) that
      the catalog entry doesn't already cover — likely a new release building on catalog
      dataset `base`, so it must surface.
    (None, None): unrelated to the catalog."""
    if not key or key in names or key in slugs:
        return "known", None
    if is_mirror(key, names, slugs):
        return "known", None
    # longest catalog name the candidate starts with: "totalsegmentatormriv2" extends
    # "TotalSegmentator MRI" (residue v2), not "TotalSegmentator" (residue mriv2). A
    # residue can't continue a number: "HVSMR 2024" is not "HVSMR-2.0" + "24". Also try
    # the name minus a packaging suffix, or "COVIDx CXR-4 Dataset" (residue 4dataset)
    # would fall through to the substring rule and be dropped as a mirror.
    m = MIRROR_SUFFIX.search(key)
    for core in dict.fromkeys([key, key[:m.start()] if m else key]):
        bases = [k for k in names if len(k) >= 4 and len(core) > len(k) and core.startswith(k)
                 and DERIVATIVE.fullmatch(core[len(k):])
                 and not (k[-1].isdigit() and core[len(k)].isdigit())]
        if bases:
            base = max(bases, key=len)
            if cover and covered(core[len(base):], cover.get(base, set())):
                return "known", None
            return "derivative", base
    # reupload/mirror under a different account: canonical name embedded in the id
    for k in short:
        if k in key or (len(key) >= 6 and key in k):
            return "known", None
    return None, None


def is_mirror(key, names, slugs):
    """Catalog name + packaging suffix: AMOS22-Lite, VerSe-Lite, AbdomenAtlas1.1Mini.
    A 2-digit year may be abbreviated: HNTSMRG24-Lite copies HNTS-MRG 2024."""
    m = MIRROR_SUFFIX.search(key)
    base = key[:m.start()] if m else ""
    if len(base) < 4:
        return False
    y = re.fullmatch(r"(.*\D)(\d\d)", base)
    return any(b in names or b in slugs for b in {base, y and y.group(1) + "20" + y.group(2)} if b)


def is_known(key, names, slugs, short):
    return classify(key, names, slugs, short)[0] is not None


def relevant(*texts):
    blob = " ".join(t for t in texts if t)
    if not RELEVANT.search(blob):
        return False
    return not EXCLUDE.search(blob) or bool(MODALITY.search(blob))


def claims_dataset(name, desc, topics=""):
    """A GitHub repo that introduces a dataset ("the first public CT dataset", repo
    named *-Dataset), not one that uses one. Every GitHub-search hit mentions
    "dataset" by construction, so a bare keyword check filters nothing."""
    words = re.sub(r"(?<=[a-z])(?=[A-Z])|[_.-]", " ", name)   # Dataset_GBC_CT -> Dataset GBC CT
    text = f"{words}. {desc}. {topics}"
    return len(DATASETISH.findall(text)) > len(DATA_USE.findall(text))


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


def huggingface(limit, min_downloads=50, min_likes=3, tag_min_downloads=200, tag_min_likes=5):
    """Only surface established datasets (enough downloads/likes) to cut reupload noise.
    `search` matches the repo id only (owner/name), so it finds ids like
    "x/brain-mri" but never research releases with non-generic names
    (AbdomenAtlas/MerlinPlus); card-tag filters catch those by what the card
    declares, newest-first as well as most-downloaded. Tags match far more repos than
    id terms (82 -> 371 rows in the first live run, mostly personal uploads), so tag
    hits need a higher floor; known publishers are covered without one by hf_publishers()."""
    out = []
    terms = ["radiology", "CT scan", "MRI", "chest x-ray", "medical imaging segmentation",
             "PET CT", "DICOM", "brain MRI", "mammography"]
    # no "pet" tag: it means pets, and RELEVANT's \bpet\b would let those through. A
    # "+" joins tags that must all be present (repeated `filter` params are ANDed).
    tags = ["radiology", "medical-imaging", "ct", "ct-scan", "computed-tomography", "mri",
            "x-ray", "chest-x-ray", "mammography", "medical+modality:3d"]
    queries = [("search", t, "downloads", min_downloads, min_likes) for t in terms]
    queries += [("filter", t, sort, tag_min_downloads, tag_min_likes)
                for t in tags for sort in ("downloads", "createdAt")]
    seen = set()   # lowest floor runs first, so a repo seen once never deserved a laxer one
    for param, value, sort, floor_dl, floor_likes in queries:
        qs = "&".join("%s=%s" % (param, urllib.parse.quote(v)) for v in value.split("+"))
        url = ("https://huggingface.co/api/datasets?full=true&limit=%d&sort=%s&direction=-1&%s"
               % (limit, sort, qs))
        try:
            for d in hf_get(url):
                did = d.get("id", "")
                if did in seen:
                    continue
                seen.add(did)
                dl, likes = d.get("downloads", 0) or 0, d.get("likes", 0) or 0
                if dl < floor_dl and likes < floor_likes:
                    continue
                desc = (d.get("description") or "") + " " + " ".join(d.get("tags", []))
                if relevant(did, desc):
                    out.append({"name": did.split("/")[-1], "id": did,
                                "url": HF_DATASET + did,
                                "source": "HuggingFace", "pop": f"{dl}⬇ {likes}♥"})
        except Exception as e:
            print(f"  (HuggingFace {param}='{value}'/{sort} skipped: {e})", file=sys.stderr)
    return out


def imaging(*texts):
    """Publisher-watch gate: orgs like OpenGVLab or microsoft publish plenty of
    non-radiology data, so an anatomy/task word ("segmentation", "hip") isn't enough."""
    blob = " ".join(t for t in texts if t)
    return relevant(blob) and bool(MODALITY.search(blob) or MEDICAL.search(blob))


def hf_publishers(authors, since):
    """Recent datasets from HF orgs that already publish catalog datasets. No
    download/like floor: a release is worth reviewing on day one, before it has any."""
    out = []
    for a in authors:
        url = ("https://huggingface.co/api/datasets?author=%s&full=true&limit=50&sort=createdAt&direction=-1"
               % urllib.parse.quote(a))
        try:
            data = hf_get(url)
        except Exception as e:
            print(f"  (HuggingFace publisher '{a}' skipped: {e})", file=sys.stderr)
            continue
        for d in data:
            created = (d.get("createdAt") or "")[:10]
            if created and created < since:
                continue
            did = d.get("id", "")
            # free-form card tags only: auto tags like task_categories:image-segmentation
            # would make any segmentation dataset look radiological
            tags = " ".join(t for t in d.get("tags") or [] if ":" not in t)
            if imaging(did, d.get("description") or "", tags):
                out.append({"name": did.split("/")[-1], "id": did, "url": HF_DATASET + did,
                            "source": "HuggingFace", "publisher": a,
                            "pop": " · ".join(x for x in (a, created) if x)})
    return out


def github_repo(r, source="GitHub", publisher=None):
    topics = " ".join(r.get("topics") or [])
    desc = r.get("description") or ""
    name = r.get("name", "")
    if r.get("fork") or r.get("archived"):
        return None
    # this catalog and awesome-lists mention every dataset but release none
    if (r.get("full_name", "").lower() == os.environ.get("GITHUB_REPOSITORY", "").lower()
            or re.search(r"awesome|curated list", f"{name} {desc}", re.I)):
        return None
    gate = imaging if publisher else relevant
    if not (gate(name, desc, topics) and claims_dataset(name, desc, topics)):
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
    # "PET CT", not "PET": a bare "PET dataset" search returns pet-animal datasets
    terms = ["CT dataset", "MRI dataset", "X-ray dataset", "radiology dataset",
             "PET CT dataset", "mammography dataset", "medical imaging dataset"]
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


def get_text(url, timeout=30, headers=None):
    h = {"User-Agent": "Mozilla/5.0 (radiology-dataset-hub-tracker)"}
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


TCIA_SITE = "https://www.cancerimagingarchive.net"


def tcia():
    """NBIA lists only collections whose DICOM is served by NBIA. The website's
    browse pages also list collections distributed another way (CDD-CESM: JPEG via
    Aspera) and label-only analysis results (e.g. tumour annotations on a TCGA
    collection), so both are read; each row links to its own collection page."""
    out, seen = [], set()
    try:
        data = get_json("https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues")
        for c in data:
            nm = c.get("Collection")
            if nm and norm(nm) not in seen:
                seen.add(norm(nm))
                slug = re.sub(r"[^a-z0-9]+", "-", nm.lower()).strip("-")
                out.append({"name": nm, "id": nm, "url": f"{TCIA_SITE}/collection/{slug}/", "source": "TCIA"})
    except Exception as e:
        print(f"  (TCIA NBIA skipped: {e})", file=sys.stderr)
    for page, kind in (("browse-collections", "collection"), ("browse-analysis-results", "analysis-result")):
        try:
            html = get_text(f"{TCIA_SITE}/{page}/")
            for slug in dict.fromkeys(re.findall(rf"cancerimagingarchive\.net/{kind}/([a-z0-9-]+)/", html)):
                nm = slug.upper() if kind == "collection" else slug.replace("-", " ")
                if norm(nm) in seen:
                    continue
                seen.add(norm(nm))
                out.append({"name": nm, "id": slug, "url": f"{TCIA_SITE}/{kind}/{slug}/",
                            "source": "TCIA" if kind == "collection" else "TCIA analysis results",
                            "pop": "" if kind == "collection" else "labels only"})
        except Exception as e:
            print(f"  (TCIA {page} skipped: {e})", file=sys.stderr)
    return out


AWS_REGISTRY_TREE = "https://api.github.com/repos/awslabs/open-data-registry/git/trees/main?recursive=1"
AWS_REGISTRY_RAW = "https://raw.githubusercontent.com/awslabs/open-data-registry/main/"
AWS_FILE_HINT = re.compile(r"rsna|emory|embed|ucsf|radiolog|imaging|mri|\bct\b|-ct-|ct-|chest|xray|x-ray|"
                           r"mammo|breast|brain|lung|tcia|idc|nih|cancer|tumor|medical|clinical|"
                           r"spine|knee|cardiac|liver|kidney|prostate|aneurysm|hemorrhage|trauma", re.I)


def aws_open_data():
    """AWS Open Data Registry: RSNA challenge datasets, EMBED, UCSF-RMaC live here and
    nowhere else we poll. One tree call lists ~1,500 YAML files; only names that hint at
    medical imaging are fetched (raw.githubusercontent, no API quota)."""
    out = []
    try:
        tree = get_json(AWS_REGISTRY_TREE, headers=gh_auth())
        paths = [t["path"] for t in tree.get("tree", [])
                 if t["path"].startswith("datasets/") and t["path"].endswith(".yaml")]
    except Exception as e:
        print(f"  (AWS Open Data skipped: {e})", file=sys.stderr)
        return out
    for p in paths:
        slug = p[len("datasets/"):-len(".yaml")]
        if not AWS_FILE_HINT.search(slug.replace("-", " ")) and not AWS_FILE_HINT.search(slug):
            continue
        try:
            y = get_text(AWS_REGISTRY_RAW + p)
        except Exception:
            continue
        m = re.search(r"^Name:\s*\"?(.+?)\"?\s*$", y, re.M)
        name = m.group(1) if m else slug
        tags = " ".join(re.findall(r"^\s*-\s*([\w .-]+)\s*$", y.split("License:")[0], re.M))
        desc = (re.search(r"^Description:\s*\|?\s*\n?(.{0,600})", y, re.M | re.S) or [None, ""])[1]
        if re.search(r"medic|imaging|radiolog|health|cancer|x-ray|mri", tags, re.I) and relevant(name, desc, tags):
            out.append({"name": name[:80], "id": slug,
                        "url": f"https://registry.opendata.aws/{slug}/", "source": "AWS Open Data"})
    return out


def figshare():
    """figshare (DMID, FUMPE, AVT and many journal-linked datasets live here). Public
    search API; item_type 3 = dataset. Figure/table records with HTML-caption titles
    are dropped."""
    out, seen = [], set()
    terms = ["mammography dataset", "CT dataset", "MRI dataset", "chest x-ray dataset",
             "radiology dataset", "medical imaging dataset", "PET dataset", "segmentation CT MRI"]
    for term in terms:
        try:
            data = get_json("https://api.figshare.com/v2/articles/search",
                            data={"search_for": term, "item_type": 3, "page_size": 100})
        except Exception as e:
            print(f"  (figshare '{term}' skipped: {e})", file=sys.stderr)
            continue
        for a in data or []:
            # titles may carry HTML (DMID's is wrapped in <b>); captions of figure/table
            # records don't name a dataset and fail PAPER_TITLE
            title = re.sub(r"<[^>]+>", "", a.get("title") or "").strip()
            if not title or a.get("id") in seen:
                continue
            seen.add(a.get("id"))
            if relevant(title) and MODALITY.search(title) and PAPER_TITLE.search(title):
                out.append({"name": title[:80], "id": str(a.get("id")),
                            "url": a.get("url_public_html") or f"https://figshare.com/articles/{a.get('id')}",
                            "source": "figshare", "pop": (a.get("published_date") or "")[:10]})
    return out


def dataverse():
    """Harvard Dataverse public search (e.g. DeepSight mammography sets)."""
    out, seen = [], set()
    for term in ["mammography", "computed tomography", "MRI imaging dataset", "chest radiograph", "DICOM"]:
        try:
            data = get_json("https://dataverse.harvard.edu/api/search?type=dataset&per_page=50&q="
                            + urllib.parse.quote(term))
        except Exception as e:
            print(f"  (Dataverse '{term}' skipped: {e})", file=sys.stderr)
            continue
        for it in (data.get("data") or {}).get("items", []):
            name, gid = it.get("name") or "", it.get("global_id") or ""
            if gid in seen:
                continue
            seen.add(gid)
            if relevant(name, it.get("description", "")) and MODALITY.search(name) and PAPER_TITLE.search(name):
                out.append({"name": name[:80], "id": gid, "url": it.get("url") or "",
                            "source": "Harvard Dataverse", "pop": (it.get("published_at") or "")[:10]})
    return out


def vindr():
    """VinDr (Vingroup) releases on its own portal, some only by request
    (VinDr-Multiphase); PhysioNet carries only part of them."""
    try:
        html = get_text("https://vindr.ai/datasets")
    except Exception as e:
        print(f"  (VinDr skipped: {e})", file=sys.stderr)
        return []
    return [{"name": "VinDr " + s.replace("-", " "), "id": s, "url": f"https://vindr.ai/datasets/{s}",
             "source": "VinDr"} for s in dict.fromkeys(re.findall(r'href="(?:https://vindr\.ai/)?/?datasets/([a-z0-9-]+)"', html))]


# Dataset-descriptor journals. A paper is often the only announcement of a dataset
# hosted somewhere we don't poll (CDD-CESM, NL-Breast-Screening, PLC-CECT, DMID).
PAPER_JOURNALS = [("2052-4463", "Scientific Data"), ("2352-3409", "Data in Brief")]
PAPER_TERMS = ["mammography dataset", "CT dataset", "MRI dataset", "chest radiograph dataset",
               "computed tomography dataset", "medical imaging dataset", "PET dataset",
               "contrast-enhanced dataset", "segmentation dataset CT"]
PAPER_TITLE = re.compile(r"\b(dataset|database|data set|benchmark|cohort|collection|repository)\b", re.I)


def dataset_papers(recent_days=730):
    """Crossref: dataset descriptors of the last two years per term, by relevance. Titles must name a
    dataset and an in-scope modality; the DOI page is the link to vet."""
    out, seen = [], set()
    since = days_ago(recent_days)
    for issn, journal in PAPER_JOURNALS:
        for term in PAPER_TERMS:
            # relevance order inside the date window (sort=created returned the newest
            # papers of any field, so nearly nothing survived the modality filter)
            url = (f"https://api.crossref.org/journals/{issn}/works?rows=40"
                   f"&filter=from-created-date:{since}&select=title,DOI,created"
                   f"&query.bibliographic={urllib.parse.quote(term)}")
            try:
                items = get_json(url, timeout=40).get("message", {}).get("items", [])
            except Exception as e:
                print(f"  (Crossref {journal} '{term}' skipped: {e})", file=sys.stderr)
                continue
            for it in items:
                title = re.sub(r"<[^>]+>", "", (it.get("title") or [""])[0]).strip()
                doi = it.get("DOI", "")
                if not title or doi in seen:
                    continue
                seen.add(doi)
                if PAPER_TITLE.search(title) and MODALITY.search(title) and relevant(title):
                    created = ((it.get("created") or {}).get("date-time") or "")[:10]
                    out.append({"name": title[:100], "id": doi, "url": "https://doi.org/" + doi,
                                "source": f"Papers — {journal}", "pop": created})
    return out


def zenodo(limit):
    """Per search term, two passes: newest uploads (weekly diff) + most-viewed
    (back-catalog — a popular dataset published years ago, e.g. Duke Liver, never
    shows up under sort=newest, so without this pass it can be missed forever).
    Narrow modality/organ terms matter: broad queries bury mid-popularity records
    below the 25-per-page unauthenticated cap."""
    out, seen = [], set()
    size = min(limit, 25)   # unauthenticated Zenodo caps page size at 25 (400 above that)
    # phase/protocol terms added after WAW-TACE (multiphase liver CT) and UniToBrain
    # (CT perfusion) were missed by the generic ones
    terms = ["radiology dataset", "medical imaging dataset", "CT dataset", "MRI dataset",
             "x-ray dataset", "PET dataset", "brain MRI", "liver MRI", "cardiac MRI",
             "chest x-ray", "abdominal CT", "mammography", "multiphase CT", "contrast-enhanced CT",
             "CT perfusion", "MR enterography", "breast MRI", "tomosynthesis", "CBCT"]
    for term in terms:
        for sort, page in (("newest", 1), ("mostviewed", 1), ("mostviewed", 2)):
            try:
                url = ("https://zenodo.org/api/records?q=%s&size=%d&type=dataset&sort=%s&page=%d"
                       % (urllib.parse.quote(term), size, sort, page))
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
    out, after = [], None
    # newest-first, several pages: one page only reached back a few weeks, so a 2022
    # release like MR-ART (ds004173) could never appear
    for _ in range(5):
        cursor = f', after: "{after}"' if after else ""
        query = ("query { datasets(first: %d%s, orderBy: {publishDate: descending}, "
                 "filterBy: {public: true}) { pageInfo { hasNextPage endCursor } edges { node { id publishDate "
                 "latestSnapshot { description { Name } summary { modalities } } } } } }"
                 % (min(limit, 100), cursor))
        try:
            data = (get_json("https://openneuro.org/crn/graphql", data={"query": query}).get("data", {})
                    .get("datasets", {})) or {}
        except Exception as e:
            print(f"  (OpenNeuro skipped: {e})", file=sys.stderr)
            break
        for e in data.get("edges", []):
            node = (e or {}).get("node") or {}
            snap = node.get("latestSnapshot") or {}
            name = ((snap.get("description") or {}).get("Name") or "").strip()
            if name and CLINICAL.search(name):
                out.append({"name": name[:80], "id": node.get("id", ""),
                            "url": "https://openneuro.org/datasets/" + node.get("id", ""),
                            "source": "OpenNeuro", "pop": (node.get("publishDate") or "")[:10]})
        info = data.get("pageInfo") or {}
        if not info.get("hasNextPage"):
            break
        after = info.get("endCursor")
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
MAX_ROWS = 50          # per source section, shrunk automatically if the body would not fit
PRIORITY_MAX_ROWS = 100   # ⭐ Priority is never shrunk to make room


def khash(key):
    return hashlib.sha1(key.encode()).hexdigest()[:8]


def load_prev_seen(path):
    """Hashed keys of every candidate shown in earlier reports (the current issue
    body), newest first, so this run can flag the rest with 🆕. Reports carry the
    cumulative seen-set in a hidden `tracker-seen` comment: visible rows alone forget
    everything shown in older reports, so rows rotated back in as 🆕 week after week
    (hundreds of false 🆕). Link TEXT (not URL: TCIA shares one landing URL) is still
    read so reports from before the comment keep working."""
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


def section(lines, title, rows, max_rows, what, shown, intro=None):
    lines.append(f"## {title} ({len(rows)})\n")
    if intro:
        lines.append(intro + "\n")
    # first-time candidates first, then alphabetical
    rows = sorted(rows, key=lambda x: (not x.get("fresh"), x["name"].lower()))
    visible = rows[:max_rows]
    lines += [row(c) for c in visible]
    shown.update(c["key"] for c in visible)
    if len(rows) > max_rows:
        lines.append(f"- _…and {len(rows) - max_rows} more {what} not shown (🆕 items always shown first)._")
    lines.append("")


def render(new, missing_watch, have_prev, max_rows):
    """Report body, plus the keys of the candidate rows it actually displays."""
    shown = set()
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
    lines.append(f"## 🧭 Portals without an API — check by hand once a month ({len(PORTALS)})\n")
    lines.append("_No listing API to poll, so new releases here only surface through papers or by "
                 "looking. Record what you checked in data/triage.json._\n")
    # autolinks, not [text](url): load_prev_seen() reads every [text](http…) as a seen candidate
    lines += [f"- {nm}: <{url}>" for nm, url in PORTALS]
    lines.append("")
    if have_prev:
        n_fresh = sum(1 for c in new if c.get("fresh"))
        lines.append(f"_{n_fresh} candidate(s) marked 🆕 have not been shown in a previous report — "
                     "review those first._\n")
    priority = [c for c in new if c.get("priority")]
    if priority:
        section(lines, "⭐ Priority — new from catalog publishers, or extending a catalog dataset",
                priority, PRIORITY_MAX_ROWS, "priority candidates", shown,
                intro="_Recent releases by Hugging Face orgs / GitHub owners that already publish a "
                      "catalog dataset, and names that extend one (X → X+ / X Plus / X v2). The likeliest "
                      "real additions — review these first._")
    by_src = {}
    for c in new:
        if not c.get("priority"):
            by_src.setdefault(c["source"], []).append(c)
    # Rows past a source's display cap never come back on their own once they lose 🆕
    # (a cut 🆕 row stays 🆕 and sorts first next week, so those drain by themselves),
    # so an unreviewed backlog (CPTAC-CCRCC, 4D-Lung, CXR-LT sat there for months) is
    # invisible. Show a window of them each report, cycling by ISO week until triaged.
    hidden = []
    for src in by_src:
        rows = sorted(by_src[src], key=lambda x: (not x.get("fresh"), x["name"].lower()))
        hidden += [c for c in rows[max_rows:] if not c.get("fresh")]
    if hidden:
        hidden.sort(key=lambda c: khash(c["key"]))
        n = len(hidden)
        start = (datetime.date.today().isocalendar()[1] * BACKLOG_ROTATION) % n
        window = [hidden[(start + i) % n] for i in range(min(BACKLOG_ROTATION, n))]
        section(lines, f"🗂 Backlog rotation — {len(window)} of {n} rows hidden by the per-source cap",
                window, BACKLOG_ROTATION, "backlog rows", shown,
                intro="_Different rows each week. Add them to the catalog, or record a decision in "
                      "data/triage.json (rejected / deferred) so they leave the queue._")
    for src in sorted(by_src):
        section(lines, src, by_src[src], max_rows, f"from {src}", shown)
    if not new:
        lines.append("_No new candidates found this run._")
    return "\n".join(lines) + "\n", shown


def build_report(new, missing_watch, prev_seen):
    """Render the report under GitHub's issue-body cap, then append the hidden
    seen-set. Only rows a reviewer has actually seen are recorded (shown now, or
    already seen before): a 🆕 row cut by the display cap stays 🆕 and sorts first
    next week, so a backlog drains instead of being silently marked seen. Previously
    seen keys follow newest-first as room allows — keeping them means a source that
    fails one week doesn't turn its whole backlog 🆕."""
    for max_rows in (MAX_ROWS, 40, 30, 20, 10, 5):
        body, shown = render(new, missing_watch, bool(prev_seen), max_rows)
        cur = list(dict.fromkeys(khash(c["key"]) for c in new
                                 if c["key"] in shown or not c.get("fresh")))
        room = (BODY_LIMIT - u16len(body) - 40) // 9   # 8 hex chars + separator each
        if room >= len(cur):
            break
    cur_set = set(cur)
    carried = [h for h in prev_seen if h not in cur_set]
    seen = (cur + carried)[:max(room, len(cur))]
    return body + "\n<!-- tracker-seen: " + " ".join(seen) + " -->\n"


def load_triage(path=TRIAGE):
    """Review decisions: {"decisions": [{"name" | "url", "decision": added|rejected|deferred,
    "reason", "date", "until"?}]}. added/rejected leave the queue for good (added = the
    candidate is a catalog entry under another name); deferred returns after `until`."""
    try:
        doc = json.loads(pathlib.Path(path).read_text())
    except (OSError, ValueError):
        return set()
    today = datetime.date.today().isoformat()
    drop = set()
    for d in doc.get("decisions", []):
        if d.get("decision") == "deferred" and (d.get("until") or "9999") <= today:
            continue
        for k in (d.get("name"), d.get("url")):
            if k:
                drop.add(norm(k) if k == d.get("name") else k.lower().rstrip("/"))
    return drop


def select_new(candidates, known, prev_set, triaged=frozenset(), urls=frozenset()):
    """Drop catalog datasets, their mirrors and triaged rows, dedupe by name (first row
    wins), and tag each survivor: extends (catalog name it builds on), priority, fresh."""
    names, slugs, short, display, cover = known
    new, seen = [], set()
    for c in candidates:
        key = norm(c["name"])
        if not key or key in seen:
            continue
        url = (c.get("url") or "").lower().rstrip("/")
        if key in triaged or url in triaged or url in urls:   # same page as a catalog entry or its links
            continue
        status, base = classify(key, names, slugs, short, cover)
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
    known = load_known(ds)
    known_names, known_slugs, known_short = known[:3]
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
    candidates += aws_open_data()
    candidates += figshare()
    candidates += dataverse()
    candidates += vindr()
    candidates += dataset_papers()

    new = select_new(candidates, known, prev_set, load_triage(), known_urls(ds))

    # curated watchlist: important resources (esp. population cohorts) that are missing
    missing_watch = [(nm, url) for nm, url in WATCHLIST
                     if not is_known(norm(nm.split("(")[0]), known_names, known_slugs, known_short)]

    print(build_report(new, missing_watch, prev_seen), end="")


if __name__ == "__main__":
    main()
