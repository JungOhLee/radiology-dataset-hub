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

The catalog exists so that someone who needs images for a given modality, MRI sequence / CT
phase or clinical situation can see which datasets exist and roughly what is inside them before
downloading anything. Record modality, sequences/phases, anatomy, size, labels and splits as
precisely as the official source allows.

- **Human imaging only.** Animal, preclinical and veterinary datasets (mouse, rat, canine,
  patient-derived xenograft models, …) are out of scope.
- **Phantoms count.** Physical and digital phantoms are useful for QA, harmonisation, dose and
  reconstruction work. Describe them in `details.phantom` (type, body part, phantom model,
  purpose), put the body part in `anatomy` and tag them `phantom`.
- **Derived and aggregated sets count** when they are radiology: preprocessed or resized
  versions, relabels, benchmark mixes, VQA / caption collections built from other datasets.
  List every source dataset in `details.related` (relation `derived-from`, catalog `id` when it
  exists, and a `note` on what was done — e.g. "2D slices resized to 28×28 PNG", "questions
  generated from MIMIC-CXR reports"), and tag them `derived` (plus `vqa` for question-answer sets).
- **Label/annotation sets count too.** Expert relabels, adjudicated reference standards and
  analysis results for a public image dataset (Google's adjudicated labels for NIH ChestX-ray14,
  CXR-LT on MIMIC-CXR, TCIA analysis results) are often what decides whether a dataset is usable
  for evaluation. Add them as `"type": "annotation"` entries that point at the base dataset
  (`details.related`, relation `label-addon-for`), or — for a small add-on — as
  `details.label_variants` on the base entry.
- **Must contain image data** (or, for `annotation` entries, label an image dataset in the catalog).
  Prefer native raw formats (DICOM, NIfTI, NRRD, MHA). Derived
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
| `type` | enum | `dataset`, `repository` (hubs like TCIA/PhysioNet), or `annotation` (labels for another dataset's images) |
| `aliases` | string[] | optional — other names the dataset is announced under (paper title, challenge name), so trackers recognise it |
| `links` | object[] | optional — `{label, url}` for other official locations (AWS registry, Zenodo record, AIMI page) and clearly-labelled unofficial mirrors |
| `regions` | string[] | **one or more** body regions — a dataset spanning several lists them all: `Neuro`, `Chest`, `Cardiac`, `Vascular`, `Abdomen`, `Pelvis`, `MSK`, `Breast`, `HeadNeck`, `Dental`, `WholeBody`, `Multi` (various). Empty only for repositories. |
| `anatomy` | string | organ/region, e.g. `"liver"` |
| `modality` | string[] | any of `CT`, `MRI`, `PET`, `X-ray`, `DXA` (mammography/DBT → `X-ray`, CBCT → `CT`) |
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
| `tags` | string[] | optional characteristics — e.g. `population-cohort`, `body-composition`, `longitudinal`, `clinical-linkage`, `genetics`, `opportunistic`, `mortality-outcome` |
| `clinical_variables` | string \| null | for cohorts: the linkable clinical/phenotype/outcome data (labs, disease outcomes, genetics, mortality) |
| `body_composition` | bool | VAT/ASAT/muscle/organ-fat/DXA phenotypes available or derivable |
| `longitudinal` | bool | repeated imaging timepoints |
| `access` | enum | `open`, `registration`, `dua`, `request` |
| `host` | string | e.g. `TCIA`, `PhysioNet`, `Grand Challenge`, `Synapse`, `OpenNeuro`, `Zenodo`, `Kaggle` |
| `url` | string | official homepage |
| `description` | string | one factual sentence |
| `details` | object | optional — data & label structure shown in the site's detail view (below) |

### `details` — what the labels are and how far to trust them

When you need a dataset later ("adjudicated chest X-ray labels", "biopsy-proven mammography with
real screening prevalence", "multiphase CT with intact DICOM headers", "may I send these images to
an external LLM API?"), these fields answer it. All optional; use `null` rather than guessing.

| Key | Type | Notes |
| --- | --- | --- |
| `label_schema` | string[] | each label/column and what it means |
| `file_structure` | string | folders, file formats, label files |
| `splits` | string | official splits |
| `label_source` | string[] | `nlp-report`, `radiologist-single`, `radiologist-multi`, `radiologist-consensus`, `pathology`, `follow-up`, `clinical-record`, `dataset-definition` (implied by protocol/design), `model-generated`, `crowd` |
| `label_readers` | string | e.g. "3 radiologists, disagreements adjudicated" |
| `label_unit` | string[] | `patient`, `study`, `series`, `image`, `breast`, `lesion`, `voxel`, `sentence` |
| `reference_standard` | string | what "positive" means and how it was confirmed, incl. prevalence if enriched |
| `label_variants` | object[] | `{name, url, note}` — other label sets on the same images |
| `phantom` | object | phantoms only: `{type, body_part, model, purpose}` — type = `physical`, `digital` or `hybrid`; e.g. `{"type": "physical", "body_part": "chest", "model": "Kyoto Kagaku Lungman N1 with synthetic nodules", "purpose": "CT radiomics repeatability across dose and kernel"}` |
| `related` | object[] | `{id, name, relation, note?}` (`note`: for `derived-from`, what was done to the source); relation = `derived-from`, `subset-of`, `superset-of`, `overlaps`, `extends`, `label-addon-for`, `mirror-of`, `same-images-as` — flag overlaps before using two datasets as independent test sets |
| `version`, `release_date` | string | current version and public release date (matters for pre-training contamination) |
| `dicom_headers` | enum | `intact`, `partially-anonymized`, `stripped (converted to NIfTI/PNG/JPEG)`, `n/a` |
| `third_party_processing` | enum | `permitted`, `prohibited`, `unclear` — whether the licence/DUA allows sending images to external online services (e.g. commercial LLM APIs); quote the clause in `third_party_note`. Not legal advice — re-read the licence before use. |
| `extra` | string | anything else (known label issues, caveats) |

## Accuracy

Metadata should reflect the **official source**, not third-party mirrors. When unsure about a field,
use `null` rather than guessing. Corrections are very welcome — open an issue with a source link.

## Finding new datasets

We monitor dataset sources automatically — see [SOURCES.md](SOURCES.md). Run
`python3 scripts/find_new_datasets.py` to list open radiology datasets not yet in the catalog,
or check the weekly **📡 New open radiology dataset candidates** issue. Once a month a workflow
triages a batch of candidates with Claude and opens a draft PR with the proposed entries — review
those against the official source like any other contribution.
