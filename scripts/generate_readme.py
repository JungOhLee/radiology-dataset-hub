#!/usr/bin/env python3
"""Generate README.md tables from data/datasets.json (single source of truth).

Usage: python scripts/generate_readme.py
Rewrites the section between the AUTO-GEN markers in README.md.
Datasets are grouped by body region; a multi-region dataset appears under each
of its regions. Repositories (type=repository) get their own section.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "datasets.json"
README = ROOT / "README.md"

START = "<!-- AUTOGEN:START -->"
END = "<!-- AUTOGEN:END -->"

REGION_ORDER = ["Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis",
                "MSK", "Breast", "HeadNeck", "Dental", "WholeBody", "Multi"]
REGION_LABEL = {
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
    "Multi": "🧩 Multiple / Various body parts",
}
REPO_LABEL = "🗄️ Data Repositories & Portals"


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


def anchor(label):
    s = label.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = s.strip().replace(" ", "-")
    return re.sub(r"-+", "-", s)


def build():
    datasets = json.loads(DATA.read_text())
    ds_only = [d for d in datasets if d.get("type") != "repository"]
    repos = [d for d in datasets if d.get("type") == "repository"]

    total = len(datasets)
    def n_mod(m): return sum(1 for d in datasets if m in (d.get("modality") or []))
    n_raw = sum(1 for d in datasets if d.get("raw_image"))
    n_text = sum(1 for d in datasets if d.get("paired_text"))
    n_seg = sum(1 for d in datasets if d.get("segmentation"))
    n_multi_region = sum(1 for d in ds_only if len(d.get("regions") or []) > 1)

    out = []
    out.append(f"**{total} curated datasets** · "
               f"{n_mod('CT')} CT · {n_mod('MRI')} MRI · {n_mod('PET')} PET · {n_mod('X-ray')} X-ray · "
               f"{n_raw} native DICOM/NIfTI · {n_text} with reports/text · {n_seg} with segmentation labels")
    out.append("")
    jumps = [f"[{REGION_LABEL[r].split(' ', 1)[-1]}](#{anchor(REGION_LABEL[r])})"
             for r in REGION_ORDER if any(r in (d.get('regions') or []) for d in ds_only)]
    jumps.append(f"[{REPO_LABEL.split(' ', 1)[-1]}](#{anchor(REPO_LABEL)})")
    out.append("Jump to: " + " · ".join(jumps))
    out.append("")
    out.append("**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). "
               "Text = paired reports/captions/QA (i.e. image–text / multimodal) · Seg = segmentation masks · "
               "Multi = multi-sequence MRI or multi-phase CT. "
               "Access: OPEN = direct download · REGISTRATION = free account · DUA = data-use agreement · "
               "REQUEST = apply for access. "
               f"**Datasets covering several body regions ({n_multi_region}) appear under each region.**")
    out.append("")

    for r in REGION_ORDER:
        items = [d for d in ds_only if r in (d.get("regions") or [])]
        if not items:
            continue
        items.sort(key=lambda d: (-(d.get("year") or 0), d.get("name", "")))
        out.append(f"### {REGION_LABEL[r]}  <sub>({len(items)})</sub>")
        out.append("")
        out.append(HEADER)
        for d in items:
            out.append(dataset_row(d))
        out.append("")

    # repositories
    if repos:
        repos.sort(key=lambda d: (-(d.get("year") or 0), d.get("name", "")))
        out.append(f"### {REPO_LABEL}  <sub>({len(repos)})</sub>")
        out.append("")
        out.append(HEADER)
        for d in repos:
            out.append(dataset_row(d))
        out.append("")

    return "\n".join(out)


def main():
    section = build()
    text = README.read_text() if README.exists() else ""
    block = f"{START}\n\n{section}\n{END}"
    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text = (text.rstrip() + "\n\n" + block + "\n") if text else block + "\n"
    README.write_text(text)
    print(f"README.md updated — {len(json.loads(DATA.read_text()))} datasets.")


if __name__ == "__main__":
    main()
