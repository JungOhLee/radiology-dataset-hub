#!/usr/bin/env python3
"""Validate data/datasets.json against the catalog schema. Exits non-zero on error.

v1 entries (no `subjects`) get the original checks; v2 entries (scripts/catalog_schema.py,
data/vocab.json) also get controlled vocabularies, derived-field consistency and provenance
rules. --require-v2 makes every non-repository entry v2.
"""
import copy
import datetime
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import catalog_schema as cs  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"

REQUIRED = ["id", "name", "type", "regions", "modality", "format", "raw_image",
            "access", "url", "description"]
REGIONS = set(cs.V["regions"])
TYPES = {"dataset", "repository", "annotation"}   # annotation = label set on another dataset's images
ACCESS_TP = {"permitted", "no-restriction-found", "prohibited", "unclear"}
LABEL_SOURCE = {"nlp-report", "radiologist-single", "radiologist-multi", "radiologist-consensus",
                "pathology", "follow-up", "clinical-record", "dataset-definition", "model-generated", "crowd"}
LABEL_UNIT = {"patient", "study", "series", "image", "breast", "lesion", "voxel", "sentence"}
DICOM_HEADERS = {"intact", "partially-anonymized", "stripped (converted to NIfTI/PNG/JPEG)", "n/a"}
PHANTOM_TYPES = set(cs.V["phantom_type"])
RELATIONS = {"derived-from", "subset-of", "superset-of", "overlaps", "extends", "label-addon-for",
             "mirror-of", "same-images-as"}
ACCESS = {"open", "registration", "dua", "request"}
BOOL_FIELDS = ["raw_image", "paired_text", "multi_sequence", "segmentation",
               "body_composition", "longitudinal"]  # last two optional (cohorts)


def check_details(tag, d):
    """Optional structured label/provenance keys inside `details` (see CONTRIBUTING.md)."""
    errs, dt = [], d.get("details")
    if dt is None:
        if d.get("type") == "annotation":
            errs.append(f"[{tag}] annotation entries need details.related (label-addon-for <base>)")
        return errs
    if not isinstance(dt, dict):
        return [f"[{tag}] details must be an object"]
    for key, allowed in (("label_source", LABEL_SOURCE), ("label_unit", LABEL_UNIT)):
        v = dt.get(key)
        if v is not None:
            if not isinstance(v, list):
                errs.append(f"[{tag}] details.{key} must be a list")
            else:
                errs += [f"[{tag}] details.{key}: unknown value {x!r}" for x in v if x not in allowed]
    if dt.get("third_party_processing") not in (None, *ACCESS_TP):
        errs.append(f"[{tag}] details.third_party_processing must be one of {sorted(ACCESS_TP)}")
    if dt.get("dicom_headers") not in (None, *DICOM_HEADERS):
        errs.append(f"[{tag}] details.dicom_headers must be one of {sorted(DICOM_HEADERS)}")
    for key in ("related", "label_variants"):
        v = dt.get(key)
        if v is not None and not (isinstance(v, list) and all(isinstance(x, dict) for x in v)):
            errs.append(f"[{tag}] details.{key} must be a list of objects")
    for x in dt.get("label_variants") or []:
        if x.get("url") and not str(x["url"]).startswith(("http://", "https://")):
            errs.append(f"[{tag}] details.label_variants url must be http(s): {x['url']}")
    ph = dt.get("phantom")
    if ph is not None:
        if not isinstance(ph, dict) or ph.get("type") not in PHANTOM_TYPES:
            errs.append(f"[{tag}] details.phantom must be an object with type in {sorted(PHANTOM_TYPES)}")
        elif any(not isinstance(ph.get(k, ""), str) for k in ("body_part", "model", "purpose")):
            errs.append(f"[{tag}] details.phantom body_part/model/purpose must be strings")
    for r in dt.get("related") or []:
        if r.get("relation") not in RELATIONS:
            errs.append(f"[{tag}] details.related: unknown relation {r.get('relation')!r}")
    if d.get("type") == "annotation" and not any(
            r.get("relation") == "label-addon-for" for r in dt.get("related") or []):
        errs.append(f"[{tag}] annotation entries need details.related with relation label-addon-for")
    return errs


DATE_RX = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
REQUIRED_V2 = ["id", "name", "type", "regions", "modality", "image_format", "access", "url", "description"]


def _date_ok(v):
    if not DATE_RX.match(str(v)):
        return False
    return str(v)[:10] <= datetime.date.today().isoformat()


def check_v2(tag, d, all_ids):
    """Schema v2 rules (CONTRIBUTING.md 'Schema v2')."""
    errs = []
    repo = d.get("type") == "repository"
    for key, allowed in cs.ENUM_LISTS.items():
        v = d.get(key)
        if v is None:
            continue
        if not isinstance(v, list):
            errs.append(f"[{tag}] {key} must be a list")
            continue
        errs += [f"[{tag}] {key}: unknown value {x!r}" for x in v if x not in allowed]
    for key in ("subjects", "label_types", "image_format", "condition_groups") + (() if repo else ("organs",)):
        if not d.get(key):
            errs.append(f"[{tag}] v2 entry needs a non-empty {key}")
    if "animal" in (d.get("subjects") or []):
        errs.append(f"[{tag}] animal subjects are out of scope (human imaging only)")
    errs += [f"[{tag}] modality: unknown value {m!r}" for m in d.get("modality") or [] if m not in cs.V["modality"]]
    mods = set(d.get("modality") or [])
    errs += [f"[{tag}] protocol {p!r} names a modality the entry does not list"
             for p in d.get("protocols") or [] if p.split(":", 1)[0] not in mods]
    for key, allowed in (("review", cs.V["review"]), ("license_id", cs.V["license_id"]),
                         ("commercial_use", cs.V["commercial_use"])):
        if d.get(key) not in allowed:
            errs.append(f"[{tag}] {key} must be one of {allowed}")
    if not all(isinstance(c, str) and c == c.lower() and c.strip() for c in d.get("conditions") or []):
        errs.append(f"[{tag}] conditions must be lowercase strings")
    if not isinstance(d.get("label_format", []), list):
        errs.append(f"[{tag}] label_format must be a list")
    for k in cs.COUNTS:
        v = d.get(k)
        if v is not None and not (isinstance(v, int) and not isinstance(v, bool) and v > 0):
            errs.append(f"[{tag}] {k} must be a positive integer or null")
    if "images_included" in d and not isinstance(d["images_included"], bool):
        errs.append(f"[{tag}] images_included must be a boolean")
    ph = d.get("phantom")
    if ph is not None:
        if not isinstance(ph, dict) or ph.get("type") not in PHANTOM_TYPES:
            errs.append(f"[{tag}] phantom.type must be one of {sorted(PHANTOM_TYPES)}")
        else:
            if ph.get("body_part", "") not in cs.V["organs"] + [""]:
                errs.append(f"[{tag}] phantom.body_part must be an organs value")
            if "anthropomorphic" in ph and not isinstance(ph["anthropomorphic"], bool):
                errs.append(f"[{tag}] phantom.anthropomorphic must be a boolean")
        if "phantom" not in (d.get("subjects") or []):
            errs.append(f"[{tag}] an entry with phantom details needs 'phantom' in subjects")
    for k in cs.DEPRECATED:
        if k in d:
            errs.append(f"[{tag}] {k} is a v1 field — run scripts/migrate_v2.py --finalize")
    if "phantom" in (d.get("details") or {}):
        errs.append(f"[{tag}] details.phantom moved to the top-level phantom")
    want = cs.derive(copy.deepcopy(d))
    for k in cs.DERIVED:
        if want.get(k) != d.get(k):
            errs.append(f"[{tag}] {k} is derived ({want.get(k)!r}) — run scripts/migrate_v2.py --finalize")
    for r in (d.get("details") or {}).get("related") or []:
        if r.get("relation") == "derived-from" and not r.get("note"):
            errs.append(f"[{tag}] details.related derived-from {r.get('name') or r.get('id')!r} needs a note")
        if r.get("id") and r["id"] not in all_ids:
            errs.append(f"[{tag}] details.related id {r['id']!r} is not in the catalog")
        bad = [x for x in r.get("process") or [] if x not in cs.V["related_process"]]
        if bad:
            errs.append(f"[{tag}] details.related process: unknown {bad}")
    rd = (d.get("details") or {}).get("release_date")
    if rd and not _date_ok(rd):
        errs.append(f"[{tag}] details.release_date must be YYYY[-MM[-DD]] and not in the future: {rd!r}")
    if d.get("review") == "human-verified" and not _date_ok(d.get("verified_date", "")):
        errs.append(f"[{tag}] human-verified entries need verified_date (YYYY-MM-DD)")
    return errs


def validate(datasets, require_v2=False):
    """All schema errors for a list of catalog entries (empty list = valid)."""
    errors = []
    ids = set()
    all_ids = {d.get("id") for d in datasets}
    for i, d in enumerate(datasets):
        tag = d.get("id") or d.get("name") or f"#{i}"
        if d.get("id") in ids:
            errors.append(f"[{tag}] duplicate id")
        ids.add(d.get("id"))
        errors += entry_errors(d, all_ids, require_v2, tag)
    return errors


def entry_errors(d, all_ids, require_v2=False, tag=None):
    """Schema errors for one entry; all_ids = every catalog id (for related-id checks)."""
    errors = []
    tag = tag or d.get("id") or d.get("name")
    if True:
        v2 = cs.is_v2(d)
        if require_v2 and not v2 and d.get("type") != "repository":
            errors.append(f"[{tag}] not migrated to schema v2 (no subjects)")
        for f in (REQUIRED_V2 if v2 else REQUIRED):
            if f not in d or d[f] in (None, ""):
                # regions may legitimately be [] for repositories
                if f == "regions" and d.get("type") == "repository" and d.get("regions") == []:
                    continue
                errors.append(f"[{tag}] missing required field: {f}")
        if d.get("type") not in TYPES:
            errors.append(f"[{tag}] invalid type: {d.get('type')}")
        regs = d.get("regions")
        if not isinstance(regs, list):
            errors.append(f"[{tag}] regions must be a list")
        else:
            if d.get("type") == "dataset" and not regs:
                errors.append(f"[{tag}] dataset needs at least one region")
            for r in regs:
                if r not in REGIONS:
                    errors.append(f"[{tag}] invalid region: {r}")
        if str(d.get("access", "")).lower() not in ACCESS:
            errors.append(f"[{tag}] invalid access: {d.get('access')}")
        if not isinstance(d.get("modality"), list) or (not d.get("modality") and d.get("type") != "repository"):
            errors.append(f"[{tag}] modality must be a non-empty list")
        for b in BOOL_FIELDS:
            if b in d and not isinstance(d[b], bool):
                errors.append(f"[{tag}] {b} must be a boolean")
        if "tags" in d and not isinstance(d["tags"], list):
            errors.append(f"[{tag}] tags must be a list")
        url = d.get("url", "")
        if url and not str(url).startswith(("http://", "https://")):
            errors.append(f"[{tag}] url should start with http: {url}")
        if "aliases" in d and not (isinstance(d["aliases"], list) and all(isinstance(a, str) for a in d["aliases"])):
            errors.append(f"[{tag}] aliases must be a list of strings")
        if "links" in d and not (isinstance(d["links"], list) and all(
                isinstance(x, dict) and str(x.get("url", "")).startswith(("http://", "https://")) for x in d["links"])):
            errors.append(f"[{tag}] links must be a list of {{label, url}} objects with http urls")
        errors += check_details(tag, d)
        if v2:
            errors += check_v2(tag, d, all_ids)
    return errors


def main():
    datasets = json.loads(DATA.read_text())
    errors = validate(datasets, require_v2="--require-v2" in sys.argv)
    if errors:
        print(f"✗ {len(errors)} validation error(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"✓ {len(datasets)} datasets valid.")


if __name__ == "__main__":
    main()
