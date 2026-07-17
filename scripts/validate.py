#!/usr/bin/env python3
"""Validate data/datasets.json against the catalog schema. Exits non-zero on error."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"

REQUIRED = ["id", "name", "category", "modality", "format", "raw_image",
            "access", "url", "description"]
CATEGORIES = {"Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis", "MSK",
              "Breast", "HeadNeck", "Dental", "WholeBody", "Multimodal", "Repository"}
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
                errors.append(f"[{tag}] missing required field: {f}")
        if d.get("id") in ids:
            errors.append(f"[{tag}] duplicate id")
        ids.add(d.get("id"))
        if d.get("category") not in CATEGORIES:
            errors.append(f"[{tag}] invalid category: {d.get('category')}")
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
