#!/usr/bin/env python3
"""Deterministic parts of the schema v1 -> v2 migration (CONTRIBUTING.md 'Schema v2').

  --seed       before the LLM enrichment pass: add what rules can fill (image_format /
               label_format from `format`, protocol_note from `multi_sequence_detail`,
               license_id / commercial_use from `license`, normalised host, review status).
               v1 fields stay, so an entry the enrichment pass fails on is still a valid v1 entry.
  --finalize   after it, on v2 entries (those with `subjects`): drop the v1 fields
               (format, multi_sequence_detail, other_labels -> details.label_schema,
               details.phantom -> phantom), map tasks/tags onto the controlled lists,
               recompute the derived booleans and order the keys.

Usage: python3 scripts/migrate_v2.py --seed [--curated-ids-from MAIN_datasets.json] | --finalize
"""
import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import catalog_schema as cs  # noqa: E402

DATA = cs.ROOT / "data" / "datasets.json"
ORDER = ["id", "name", "full_name", "type", "review", "verified_date", "enriched", "subjects", "regions",
         "anatomy", "organs", "modality", "other_modalities", "protocols", "protocol_note", "field_strength",
         "multi_sequence", "year", "image_format", "label_format", "preprocessing", "images_included",
         "raw_image", "size", "n_subjects", "n_studies", "n_images", "label_types", "segmentation",
         "segmentation_detail", "paired_text", "paired_text_detail", "conditions", "condition_groups",
         "population", "setting", "tasks", "tags", "longitudinal", "body_composition", "clinical_variables",
         "license", "license_id", "commercial_use", "access", "host", "url", "description", "phantom",
         "details", "aliases", "links"]


def dedup(xs):
    out = []
    for x in xs:
        if x not in out:
            out.append(x)
    return out


def seed(e, curated_ids=None):
    """Rule-based v2 fields added next to the v1 ones (idempotent; skips v2 entries)."""
    if cs.is_v2(e) or e.get("type") == "repository":
        return e
    img, lab = [], []
    for f in e.get("format") or []:
        i, l = cs.map_format(f)
        if i:
            img.append(i)
        if l:
            lab.append(l)
    if img and not e.get("image_format"):
        e["image_format"] = dedup(img)
    if lab and not e.get("label_format"):
        e["label_format"] = dedup(lab)
    if e.get("multi_sequence_detail") and not e.get("protocol_note"):
        e["protocol_note"] = e["multi_sequence_detail"]
    lid, com = cs.map_license(e.get("license"))
    e.setdefault("license_id", lid)
    e.setdefault("commercial_use", com)
    if e.get("host"):
        e["host"] = cs.map_host(e["host"])
    if "review" not in e:
        e["review"] = "curated" if curated_ids is None or e["id"] in curated_ids else "llm-proposed"
    return e


def finalize(e):
    """v2 entries only: drop v1 fields, normalise lists, derive booleans, order keys."""
    if not cs.is_v2(e):
        return e
    e.pop("format", None)
    e.pop("multi_sequence_detail", None)
    other = e.pop("other_labels", None) or []
    d = e.get("details")
    if other:
        d = e.setdefault("details", {})
        have = {str(x).lower() for x in d.get("label_schema") or []}
        extra = [x for x in other if str(x).lower() not in have and not any(str(x).lower() in h for h in have)]
        if extra:
            d["label_schema"] = (d.get("label_schema") or []) + extra
    if d and "phantom" in d:
        ph = d.pop("phantom")
        if "phantom" not in e and isinstance(ph, dict) and ph.get("type") in cs.V["phantom_type"]:
            e["phantom"] = ph
    if d is not None and not d:
        e.pop("details")
    e["tasks"] = dedup(t for t in (cs.map_task(x) for x in e.get("tasks") or []) if t)
    e["tags"] = dedup(t for t in (cs.map_tag(x) for x in e.get("tags") or []) if t)
    e["conditions"] = dedup(str(c).strip().lower() for c in e.get("conditions") or [] if str(c).strip())
    for k in cs.COUNTS:
        if not (isinstance(e.get(k), int) and e[k] > 0):
            e.pop(k, None)
    for k in ("tags", "aliases", "links", "label_format", "other_modalities", "field_strength"):
        if k in e and not e[k]:
            e.pop(k)
    if e.get("host"):
        e["host"] = cs.map_host(e["host"])
    if len(e.get("regions") or []) > 1 and "Multi" in e["regions"]:   # Multi only when nothing is itemised
        e["regions"] = [r for r in e["regions"] if r != "Multi"]
    cs.derive(e)
    ordered = {k: e[k] for k in ORDER if k in e}
    ordered.update({k: v for k, v in e.items() if k not in ordered})
    return ordered


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--seed", action="store_true")
    g.add_argument("--finalize", action="store_true")
    ap.add_argument("--curated-ids-from", metavar="DATASETS_JSON",
                    help="entries whose id is in this file are 'curated', others 'llm-proposed'")
    a = ap.parse_args()
    cat = json.loads(DATA.read_text())
    if a.seed:
        cur = None
        if a.curated_ids_from:
            cur = {e["id"] for e in json.loads(pathlib.Path(a.curated_ids_from).read_text())}
        cat = [seed(e, cur) for e in cat]
    else:
        cat = [finalize(e) for e in cat]
    DATA.write_text(json.dumps(cat, indent=2) + "\n")
    n2 = sum(1 for e in cat if cs.is_v2(e))
    print(f"{'seeded' if a.seed else 'finalized'} {len(cat)} entries ({n2} v2)")


if __name__ == "__main__":
    main()
