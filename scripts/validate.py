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
TYPES = {"dataset", "repository"}
ACCESS = {"open", "registration", "dua", "request"}
BOOL_FIELDS = ["raw_image", "paired_text", "multi_sequence", "segmentation"]


def main():
    datasets = json.loads(DATA.read_text())
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
        url = d.get("url", "")
        if url and not str(url).startswith("http"):
            errors.append(f"[{tag}] url should start with http: {url}")

    if errors:
        print(f"✗ {len(errors)} validation error(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"✓ {len(datasets)} datasets valid.")


if __name__ == "__main__":
    main()
