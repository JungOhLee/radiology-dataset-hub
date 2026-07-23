# Contributing a dataset

Thanks for helping researchers find open radiology data! This catalog is driven by a **single
source of truth**: [`data/datasets.json`](data/datasets.json). Both the website and the README
tables are generated from it.

## How to add or edit a dataset

1. Edit `data/datasets.json` — add one object to the array (or fix an existing one).
2. Run the checks locally:
   ```bash
   python3 scripts/validate.py          # schema check
   python3 scripts/generate_readme.py   # regenerate README tables
   ```
3. Open a pull request. CI validates the JSON automatically.

## Inclusion criteria

- **Must contain image data.** Prefer native raw formats (DICOM, NIfTI, NRRD, MHA). Derived
  formats (PNG/JPEG) are accepted but flagged `"raw_image": false`.
- **Must be open** for research use: direct download, free registration, a data-use agreement,
  or an application process. No fully closed/commercial-only data.
- Modalities in scope: **CT, MRI, PET, X-ray** (including mammography, DBT, CBCT). Ultrasound and
  pathology are out of scope for now.

## Schema

Each entry is a JSON object with these fields:

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | unique kebab-case id |
| `name` | string | short display name |
| `full_name` | string \| null | expanded name |
| `type` | enum | `dataset` or `repository` (hubs like TCIA/PhysioNet) |
| `regions` | string[] | **one or more** body regions — a dataset spanning several lists them all: `Neuro`, `Chest`, `Cardiac`, `Vascular`, `Abdomen`, `Pelvis`, `MSK`, `Breast`, `HeadNeck`, `Dental`, `WholeBody`, `Multi` (various). Empty only for repositories. |
| `anatomy` | string | organ/region, e.g. `"liver"` |
| `modality` | string[] | any of `CT`, `MRI`, `PET`, `X-ray` (note others in `description`) |
| `year` | int \| null | release year |
| `format` | string[] | e.g. `["DICOM"]`, `["NIfTI"]`, `["PNG"]` |
| `raw_image` | bool | `true` if primarily DICOM/NIfTI/NRRD/MHA |
| `size` | string \| null | e.g. `"1000 CT volumes / 800 patients"` |
| `paired_text` | bool | has reports/captions/clinical text |
| `paired_text_detail` | string \| null | what kind of text |
| `multi_sequence` | bool | multi-sequence MRI or multi-phase CT |
| `multi_sequence_detail` | string \| null | e.g. `"T1, T2, FLAIR"` |
| `segmentation` | bool | has segmentation masks |
| `segmentation_detail` | string \| null | what is segmented |
| `other_labels` | string[] | e.g. `["classification","detection"]` |
| `tasks` | string[] | `segmentation`, `classification`, `detection`, `reconstruction`, `registration`, `report-generation`, `vqa` |
| `license` | string \| null | e.g. `"CC BY-NC 4.0"` |
| `access` | enum | `open`, `registration`, `dua`, `request` |
| `host` | string | e.g. `TCIA`, `PhysioNet`, `Grand Challenge`, `Synapse`, `OpenNeuro`, `Zenodo`, `Kaggle` |
| `url` | string | official homepage |
| `description` | string | one factual sentence |

## Accuracy

Metadata should reflect the **official source**, not third-party mirrors. When unsure about a field,
use `null` rather than guessing. Corrections are very welcome — open an issue with a source link.

## Finding new datasets

We monitor dataset sources automatically — see [SOURCES.md](SOURCES.md). Run
`python3 scripts/find_new_datasets.py` to list open radiology datasets not yet in the catalog,
or check the monthly **📡 New open radiology dataset candidates** issue.
