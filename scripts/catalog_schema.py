"""Catalog schema v2 — shared by validate.py, migrate_v2.py, triage_candidates.py,
enrich_entries.py (and mirrored by assets/app.js).

v2 adds searchable, controlled fields (data/vocab.json) for what people look for —
protocols (MRI sequence / CT phase / PET tracer), clinical situation, organs, subjects,
label types, image format and preprocessing, numeric counts, licence class, review status —
and turns a few v1 booleans into values derived from them (see derive()). An entry is v2
when it has `subjects`.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = json.loads((ROOT / "data" / "vocab.json").read_text())

PROTOCOLS = [f"{m}:{p}" for m, ps in V["protocols"].items() for p in ps]
NATIVE_FORMATS = {"DICOM", "NIfTI", "NRRD", "MHA", "Analyze", "raw-data"}
TEXT_LABELS = {"report", "caption", "qa-pairs"}
DEPRECATED = ("format", "multi_sequence_detail", "other_labels")   # removed by migrate_v2 --finalize
DERIVED = ("raw_image", "segmentation", "paired_text", "longitudinal", "body_composition")
ENUM_LISTS = {   # v2 list fields and their vocabularies
    "subjects": V["subjects"], "other_modalities": V["other_modalities"], "protocols": PROTOCOLS,
    "field_strength": V["field_strength"], "condition_groups": V["condition_groups"],
    "population": V["population"], "setting": V["setting"], "organs": V["organs"],
    "label_types": V["label_types"], "image_format": V["image_format"],
    "preprocessing": V["preprocessing"], "tasks": V["tasks"], "tags": V["tags"],
}
COUNTS = ("n_subjects", "n_studies", "n_images")


def is_v2(e):
    return "subjects" in e


# ---------------------------------------------------------------- deterministic maps

def map_task(t):
    """Free-text task -> canonical task, or None (topic-like values belong in conditions)."""
    s = str(t or "").strip().lower()
    if s in V["tasks"]:
        return s
    rules = [("hosting", None), ("segment", "segmentation"), ("visual question", "vqa"), ("vqa", "vqa"),
             ("report", "report-generation"), ("caption", "captioning"), ("retriev", "retrieval"),
             ("grounding", "grounding"), ("registration", "registration"), ("reconstruct", "reconstruction"),
             ("accelerated", "reconstruction"), ("denois", "denoising"), ("pretrain", "pretraining"),
             ("pre-train", "pretraining"), ("self-supervised", "pretraining"), ("foundation", "pretraining"),
             ("image-text learning", "pretraining"), ("synthesis", "synthesis"), ("translation", "synthesis"),
             ("generation", "synthesis"), ("surviv", "outcome-prediction"), ("prognos", "outcome-prediction"),
             ("outcome", "outcome-prediction"), ("risk", "outcome-prediction"), ("response", "outcome-prediction"),
             ("progression", "outcome-prediction"), ("detect", "detection"), ("locali", "detection"),
             ("classif", "classification"), ("grading", "classification"), ("diagnos", "classification"),
             ("regression", "quantification"), ("quantif", "quantification"), ("scoring", "quantification"),
             ("measurement", "quantification"), ("body composition", "quantification"),
             ("estimation", "quantification")]
    for key, val in rules:
        if key in s:
            return val
    return None


_TAG_MAP = {"multi-site": "multi-center", "multi-scanner": "multi-vendor", "repeatability": "test-retest",
            "radiomics-reproducibility": "radiomics", "radiomics-robustness": "radiomics",
            "neoadjuvant-chemotherapy": "treatment-response", "organs-at-risk": "radiotherapy",
            "mllm-evaluation": "model-evaluation", "vlm-evaluation": "model-evaluation",
            "hallucination": "model-evaluation", "explainability": "model-evaluation",
            "bilingual": "multilingual", "dose-levels": "image-quality", "quantitative": "quantitative-imaging"}


def map_tag(t):
    s = str(t or "").strip().lower()
    if s in V["tags"]:
        return s
    return _TAG_MAP.get(s)


def map_format(f):
    """v1 `format` value -> (image_format or None, label_format or None)."""
    raw = str(f or "").strip()
    s = raw.lower()
    if not s or s in ("derived", "various", "images") or s.startswith("2d image") or s.startswith("derived "):
        return None, None
    if s.startswith("dicom") or s in ("seg", "sr", "rtstruct"):
        if any(k in s for k in ("seg", "rtstruct", "sr")) and "ct-pd" not in s:
            return None, raw
        return ("raw-data" if "ct-pd" in s else "DICOM"), None
    if "k-space" in s or "ismrmrd" in s or s.startswith("mrd") or "list-mode" in s or s in ("raw", "rctd", "vol") \
            or s.startswith("rctd") or s.startswith("vol "):
        return "raw-data", None
    pairs = [("nifti", "NIfTI"), ("bids", "NIfTI"), ("nrrd", "NRRD"), ("mha", "MHA"), ("mhd", "MHA"),
             ("metaimage", "MHA"), ("analyze", "Analyze"), ("png", "PNG"), ("jpeg", "JPEG"), ("jpg", "JPEG"),
             ("tif", "TIFF"), ("npz", "NumPy"), ("npy", "NumPy"), ("numpy", "NumPy"), ("pytorch", "NumPy"),
             ("hdf5", "HDF5"), ("h5", "HDF5"), ("lmdb", "HDF5"), ("matlab", "MAT")]
    for key, val in pairs:
        if key in s:
            return val, None
    if s in ("mat", "img"):
        return ("MAT" if s == "mat" else "Analyze"), None
    if s in ("bmp", "pgm"):
        return "other", None
    return None, raw   # CSV, JSON, XLSX, STL, … — label / metadata files


def map_license(text):
    """v1 licence text -> (license_id, commercial_use)."""
    s = str(text or "").strip().lower()
    if not s or s == "none":
        return "unknown", "unclear"
    if "controlled" in s:
        return "NIH-controlled", "unclear"
    if "physionet" in s and "credential" in s:
        return "PhysioNet-credentialed", "unclear"
    if "physionet" in s and "restricted" in s:
        return "PhysioNet-restricted", "unclear"
    if "cc0" in s or "public domain" in s:
        return "CC0", "allowed"
    if re.search(r"cc[\s-]*by", s):
        nc, nd, sa = (bool(re.search(rf"\b{k}\b", s)) for k in ("nc", "nd", "sa"))
        lid = "CC-BY" + ("-NC" if nc else "") + ("-SA" if sa else "") + ("-ND" if nd and not sa else "")
        lid = {"CC-BY-ND": "CC-BY-ND"}.get(lid, lid)
        return lid, "prohibited" if nc else "allowed"
    if "odc" in s or "open data commons" in s or "odbl" in s:
        return "ODC", "allowed"
    if re.search(r"\b(mit|apache|gpl|bsd)\b", s):
        return "software-license", "allowed"
    noncom = bool(re.search(r"non-?commercial|research (use )?only|research use agreement", s))
    if noncom or re.search(r"agreement|dua|terms|research use|policy", s):
        return "custom-DUA", "prohibited" if noncom else "unclear"
    return "other", "unclear"


_HOSTS = {"the cancer imaging archive (tcia)": "TCIA", "figshare": "figshare", "hugging face": "Hugging Face",
          "synapse (sage bionetworks)": "Synapse", "kaggle (rsna)": "Kaggle",
          "bimcv (bimcv.cipf.es)": "BIMCV"}


def map_host(h):
    s = str(h or "").strip()
    low = s.lower()
    if low in _HOSTS:
        return _HOSTS[low]
    if low.startswith("hugging face ("):
        return "Hugging Face"
    return s


def derive(e):
    """v1 booleans as values derived from v2 fields (kept so cards, filters and the README
    keep working; never edit them by hand on a v2 entry)."""
    fmt, pre, lab, tags = (set(e.get(k) or []) for k in ("image_format", "preprocessing", "label_types", "tags"))
    e["raw_image"] = bool(fmt & NATIVE_FORMATS) and (not pre or "native" in pre)
    e["segmentation"] = "mask" in lab
    e["paired_text"] = bool(lab & TEXT_LABELS)
    for key, tag in (("longitudinal", "longitudinal"), ("body_composition", "body-composition")):
        if tag in tags:
            e[key] = True
        else:
            e.pop(key, None)
    return e


# ---------------------------------------------------------------- JSON-schema fragments (LLM outputs)

def _enum(values):
    return {"type": "string", "enum": list(values)}


def _arr(items):
    return {"type": "array", "items": items}


def _obj(props):
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def phantom_schema():
    return _obj({"type": _enum(V["phantom_type"] + ["not-a-phantom"]), "anthropomorphic": {"type": "boolean"},
                 "body_part": _enum(V["organs"] + [""]), "model": {"type": "string"},
                 "purpose": {"type": "string"}})


def llm_v2_properties():
    """The v2 fields an LLM fills (unknown = "" / 0 / [])."""
    s, i = {"type": "string"}, {"type": "integer"}
    return {
        "subjects": _arr(_enum(V["subjects"] + ["animal"])),
        "other_modalities": _arr(_enum(V["other_modalities"])),
        "protocols": _arr(_enum(PROTOCOLS)),
        "protocol_note": s,
        "field_strength": _arr(_enum(V["field_strength"])),
        "conditions": _arr(s),
        "condition_groups": _arr(_enum(V["condition_groups"])),
        "population": _arr(_enum(V["population"])),
        "setting": _arr(_enum(V["setting"])),
        "organs": _arr(_enum(V["organs"])),
        "label_types": _arr(_enum(V["label_types"])),
        "image_format": _arr(_enum(V["image_format"])),
        "label_format": _arr(s),
        "preprocessing": _arr(_enum(V["preprocessing"])),
        "images_included": {"type": "boolean"},
        "n_subjects": i, "n_studies": i, "n_images": i,
        "tasks": _arr(_enum(V["tasks"])),
        "tags": _arr(_enum(V["tags"])),
        "license_id": _enum(V["license_id"]),
        "commercial_use": _enum(V["commercial_use"]),
        "phantom": phantom_schema(),
    }


GUIDE = """\
Schema v2 fields (controlled values only — use the listed enums):
- subjects: whose images — human, phantom, synthetic (simulated / generated), ex-vivo (cadaver, \
specimens); "animal" for any non-human subject (mouse, rat, rabbit, pig, canine, xenograft).
- protocols: every acquisition the data contains, prefixed by modality — MRI sequences \
(MRI:T1w, MRI:T1w-CE, MRI:FLAIR, MRI:DWI …), CT phases/techniques (CT:non-contrast, \
CT:portal-venous, CT:CTA, CT:low-dose …; use CT:contrast-unspecified rather than inferring a \
phase from the disease), PET tracers, X-ray types. protocol_note: the source's own wording \
(field strength, vendors, b-values …). field_strength for MRI when stated.
- conditions: lowercase common names of the diseases/findings the data is about ("glioma", \
"ischemic stroke", "lung nodule", "pneumothorax"); [] for healthy or unselected data. \
condition_groups: the broad groups (healthy-normal for healthy-volunteer sets, \
unselected-mixed for consecutive/unselected clinical data, not-applicable for phantoms). \
population: adult / pediatric / fetal-neonatal as stated. setting: clinical context.
- organs: the organs/body parts imaged (none-geometric for non-anatomical phantoms; \
whole-body / multi-organ when broad).
- label_types: what the labels are (mask, bounding-box, landmark, image-level-class, report, \
caption, qa-pairs, outcome, molecular, pathology-result, measurement; none if unlabelled).
- image_format: formats of the IMAGES as distributed ("none" when only labels are shipped); \
label_format: label/metadata file formats (CSV, JSON, DICOM-SEG …). preprocessing: native when \
images are as acquired, else what was done. images_included: false when the download has \
only labels and images must be fetched from the source dataset.
- n_subjects / n_studies / n_images: counts of the public data as stated (0 = not stated).
- tasks: intended ML tasks (controlled list). tags: only from the controlled list.
- license_id / commercial_use: licence class and whether commercial use is allowed.
- phantom: for phantoms — type, anthropomorphic (true for human-shaped phantoms), body part, \
model/product, purpose; otherwise type "not-a-phantom".
"""
