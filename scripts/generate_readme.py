#!/usr/bin/env python3
"""Generate README.md tables from data/datasets.json (single source of truth).

Usage: python scripts/generate_readme.py
The script rewrites the section between the AUTO-GEN markers in README.md.
"""
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"
README = ROOT / "README.md"

START = "<!-- AUTOGEN:START -->"
END = "<!-- AUTOGEN:END -->"

CATEGORY_ORDER = [
    "Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis",
    "MSK", "Breast", "HeadNeck", "Dental", "WholeBody", "Multimodal", "Repository",
]
CATEGORY_LABEL = {
    "Neuro": "🧠 Neuro (Brain & Spine)",
    "Chest": "🫁 Chest & Thorax",
    "Cardiac": "🫀 Cardiac",
    "Vascular": "🩸 Vascular",
    "Abdomen": "🫃 Abdominal",
    "Pelvis": "⬇️ Pelvic & Prostate",
    "MSK": "🦴 Musculoskeletal",
    "Breast": "🎀 Breast",
    "HeadNeck": "👤 Head & Neck",
    "Dental": "🦷 Dental & Maxillofacial",
    "WholeBody": "🌐 Whole-Body & PET",
    "Multimodal": "📝 Multimodal / Image–Text",
    "Repository": "🗄️ Data Repositories & Portals",
}


def yn(v):
    return "✅" if v else "—"


def cell(v):
    if v is None or v == "":
        return "—"
    return str(v).replace("|", "\\|").replace("\n", " ")


def dataset_row(d):
    name = cell(d.get("name"))
    url = d.get("url")
    name_md = f"[{name}]({url})" if url else name
    mods = ", ".join(d.get("modality") or []) or "—"
    fmt = ", ".join(d.get("format") or []) or "—"
    raw = "🟢" if d.get("raw_image") else "🟡"
    text = yn(d.get("paired_text"))
    seg = yn(d.get("segmentation"))
    seq = yn(d.get("multi_sequence"))
    access = cell(d.get("access")).upper() if d.get("access") else "—"
    size = cell(d.get("size"))
    return (
        f"| {name_md} | {mods} | {d.get('year') or '—'} | {raw} {fmt} | "
        f"{text} | {seg} | {seq} | {access} | {size} |"
    )


HEADER = (
    "| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |\n"
    "| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |"
)


def build():
    datasets = json.loads(DATA.read_text())
    by_cat = {}
    for d in datasets:
        by_cat.setdefault(d.get("category", "Other"), []).append(d)

    total = len(datasets)
    n_ct = sum(1 for d in datasets if "CT" in (d.get("modality") or []))
    n_mri = sum(1 for d in datasets if "MRI" in (d.get("modality") or []))
    n_pet = sum(1 for d in datasets if "PET" in (d.get("modality") or []))
    n_xr = sum(1 for d in datasets if "X-ray" in (d.get("modality") or []))
    n_raw = sum(1 for d in datasets if d.get("raw_image"))
    n_text = sum(1 for d in datasets if d.get("paired_text"))
    n_seg = sum(1 for d in datasets if d.get("segmentation"))

    out = []
    out.append(f"**{total} curated datasets** · "
               f"{n_ct} CT · {n_mri} MRI · {n_pet} PET · {n_xr} X-ray · "
               f"{n_raw} native DICOM/NIfTI · {n_text} with reports/text · {n_seg} with segmentation labels")
    out.append("")
    out.append("Jump to: " + " · ".join(
        f"[{CATEGORY_LABEL.get(c, c).split(' ', 1)[-1]}](#{anchor(c)})"
        for c in CATEGORY_ORDER if c in by_cat))
    out.append("")
    out.append("**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). "
               "Text = paired reports/captions · Seg = segmentation masks · "
               "Multi = multi-sequence MRI or multi-phase CT. "
               "Access: OPEN = direct download · REGISTRATION = free account · "
               "DUA = data-use agreement · REQUEST = apply for access.")
    out.append("")

    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        items = sorted(by_cat[cat], key=lambda d: (-(d.get("year") or 0), d.get("name", "")))
        out.append(f"### {CATEGORY_LABEL.get(cat, cat)}  <sub>({len(items)})</sub>")
        out.append("")
        out.append(HEADER)
        for d in items:
            out.append(dataset_row(d))
        out.append("")

    return "\n".join(out)


def anchor(cat):
    label = CATEGORY_LABEL.get(cat, cat)
    # GitHub slugify: lowercase, strip emoji/punct, spaces->dash
    import re
    s = label.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = s.strip().replace(" ", "-")
    s = re.sub(r"-+", "-", s)
    return s


def main():
    section = build()
    text = README.read_text() if README.exists() else ""
    block = f"{START}\n\n{section}\n{END}"
    if START in text and END in text:
        pre = text.split(START)[0]
        post = text.split(END)[1]
        text = pre + block + post
    else:
        text = (text.rstrip() + "\n\n" + block + "\n") if text else block + "\n"
    README.write_text(text)
    print(f"README.md updated with {section.count('|') and 'tables'} — "
          f"{len(json.loads(DATA.read_text()))} datasets.")


if __name__ == "__main__":
    main()
