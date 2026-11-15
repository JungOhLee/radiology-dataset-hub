#!/usr/bin/env python3
"""Validate data/datasets.json against the catalog schema. Exits non-zero on error."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"

REQUIRED = ["id", "name", "type", "regions", "modality", "format", "raw_image",
            "access", "url", "description"]
REGIONS = {"Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis", "MSK",
           "Breast", "HeadNeck", "Dental", "WholeBody", "Multi"}
TYPES = {"dataset", "repository", "annotation"}   # annotation = label set on another dataset's images
ACCESS_TP = {"permitted", "prohibited", "unclear"}
LABEL_SOURCE = {"nlp-report", "radiologist-single", "radiologist-multi", "radiologist-consensus",
                "pathology", "follow-up", "clinical-record", "dataset-definition", "model-generated", "crowd"}
LABEL_UNIT = {"patient", "study", "series", "image", "breast", "lesion", "voxel", "sentence"}
DICOM_HEADERS = {"intact", "partially-anonymized", "stripped (converted to NIfTI/PNG/JPEG)", "n/a"}
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
    for r in dt.get("related") or []:
        if r.get("relation") not in RELATIONS:
            errs.append(f"[{tag}] details.related: unknown relation {r.get('relation')!r}")
    if d.get("type") == "annotation" and not any(
            r.get("relation") == "label-addon-for" for r in dt.get("related") or []):
        errs.append(f"[{tag}] annotation entries need details.related with relation label-addon-for")
    return errs


def validate(datasets):
    """All schema errors for a list of catalog entries (empty list = valid)."""
    errors = []
    ids = set()
    for i, d in enumerate(datasets):
        tag = d.get("id") or d.get("name") or f"#{i}"
        for f in REQUIRED:
            if f not in d or d[f] in (None, ""):
                # regions may legitimately be [] for repositories
                if f == "regions" and d.get("type") == "repository" and d.get("regions") == []:
                    continue
                errors.append(f"[{tag}] missing required field: {f}")
        if d.get("id") in ids:
            errors.append(f"[{tag}] duplicate id")
        ids.add(d.get("id"))
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
        if not isinstance(d.get("modality"), list) or not d.get("modality"):
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
    return errors


def main():
    datasets = json.loads(DATA.read_text())
    errors = validate(datasets)
    if errors:
        print(f"✗ {len(errors)} validation error(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"✓ {len(datasets)} datasets valid.")


if __name__ == "__main__":
    main()
