# Where the datasets come from — and how we track new ones

Keeping a radiology-dataset catalog current is the hard part. This repo uses **two
layers**: a broad one-time discovery sweep, and an ongoing automated tracker.

## Primary sources we monitor

| Source | What it holds | How we query it |
| --- | --- | --- |
| [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/) | DICOM cancer imaging collections (CT/MRI/PET) | NBIA REST API `getCollectionValues` |
| **Catalog publishers** | Follow-up releases from groups already in the catalog (AbdomenAtlas → PanTS → Merlin Plus) | Every Hugging Face org and GitHub owner in a catalog `url` (plus a few extras: `stanfordmimi`, and `BodyMaps` / HF `MrGiovanni` for the AbdomenAtlas group): `/api/datasets?author=…&sort=createdAt` and `/users/…/repos?sort=created`, last 365 days, **no popularity floor** but must name an imaging modality or medical term — reported in the ⭐ Priority section |
| [Hugging Face Datasets](https://huggingface.co/datasets) | Foundation-model / report-paired / VLM sets (CT-RATE, MR-RATE, Merlin, RadGenome…) | `/api/datasets` `search` (matches the **repo id only**) **and** card-tag `filter` (`radiology`, `ct`, `mri`, `medical-imaging`…, by downloads and newest) + downloads/likes filter |
| [GitHub](https://github.com/search?type=repositories) | Dataset releases announced as a repo (README + download link to HF/Zenodo) | `/search/repositories` for "CT/MRI/X-ray/PET/mammography/radiology/medical imaging dataset" created in the last 120 days, top-starred; must *introduce* a dataset rather than use one ("the first public CT dataset" vs "trained on …") (uses the workflow's `GITHUB_TOKEN`) |
| [Grand Challenge](https://grand-challenge.org/) | Segmentation/detection challenges with expert labels | `/api/v1/challenges/` |
| [Zenodo](https://zenodo.org/) | DOI-minted dataset releases (ROCOv2, TotalSegmentator, Duke Liver…) | `/api/records?type=dataset`, per modality/organ term, `sort=newest` **and** `sort=mostviewed` (back-catalog; unauthenticated page cap is 25) |
| [Kaggle datasets](https://www.kaggle.com/datasets) | Community uploads & competition mirrors | `/api/v1/datasets/list` (unauthenticated) + download-count filter |
| [Kaggle competitions](https://www.kaggle.com/competitions) | RSNA/SPR/UW-Madison etc. medical-imaging challenges | `/api/v1/competitions/list` — needs `KAGGLE_USERNAME`/`KAGGLE_KEY` repo secrets (kaggle.com → Settings → API); skipped gracefully if unset |
| [PhysioNet](https://physionet.org/) | Credentialed clinical imaging (MIMIC-CXR family) | `/api/v1/project/published/` (full catalog JSON, filtered client-side) |
| [OpenNeuro](https://openneuro.org/) | BIDS neuroimaging | GraphQL `/crn/graphql`, newest public datasets, clinical/pathology keyword filter |
| [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) | Cloud-hosted public collections | manual |
| Stanford AIMI, arXiv, Papers With Code | New dataset papers & institutional releases | manual / literature |

## Population / epidemiological imaging cohorts

A whole class of datasets is **not** surfaced by the dataset-repository APIs above:
large population cohorts whose value is *linkable clinical variables* (labs, disease
outcomes, genetics, mortality) and *body-composition phenotypes* (VAT/ASAT, muscle,
DXA), accessed by application. These live in national-biobank portals and registries,
not on Hugging Face or Grand Challenge:

- Registries: [NHLBI BioLINCC](https://biolincc.nhlbi.nih.gov/), [dbGaP](https://www.ncbi.nlm.nih.gov/gap/), [Maelstrom Research catalogue](https://www.maelstrom-research.org/), the [EU cohort directory](https://www.eucanconnect.eu/).
- National cohorts: UK Biobank, NAKO, SHIP, Rhineland, Rotterdam, Lifelines, Maastricht,
  MESA, CARDIA, Framingham, COPDGene, SPIROMICS, NHANES, BioBank Japan, China Kadoorie,
  KoGES, AGES-Reykjavik, and more.

Because no API covers these, the tracker keeps a **curated watchlist** (`WATCHLIST` in
`find_new_datasets.py`) of must-have resources and reports any that are missing from the
catalog at the top of every run — so this category can't be silently dropped. These
datasets use extra schema fields: `tags` (e.g. `population-cohort`, `body-composition`,
`longitudinal`, `clinical-linkage`), `clinical_variables`, `body_composition`,
`longitudinal`, and the `DXA` modality.

## Automated tracker

`scripts/find_new_datasets.py` queries the API-backed sources above, filters for
radiology relevance and (for Hugging Face search/tags) a minimum download/like count
to skip personal reuploads, then **diffs against `data/datasets.json`** — including
substring matching so mirrors of datasets we already list are suppressed. A name
that is a catalog name plus a version/extension marker (`X+`, `X Plus`, `X v2`,
`X 2026`, `X-MRI`) is *not* treated as a mirror: unless the catalog entry already
covers that edition/modality (VerSe "(2019 & 2020)" covers VerSe'20), it is flagged
"extends **X**" and listed in the ⭐ Priority section with the catalog-publisher releases. It also
checks the curated watchlist of population cohorts described above.

**Why the publisher watch exists — the Merlin Plus miss (Sep 2026).** Merlin Plus
(`AbdomenAtlas/MerlinPlus`, tumor/organ masks for the Merlin CTs) was never
reported: Hugging Face `search` only matches repo ids, and `MerlinPlus` contains none
of the generic terms (`MRI`, `radiology`, …); no source covered GitHub; and even a
"Merlin+" title would have been normalized to "Merlin" and dropped as already
catalogued. Research groups rarely put modality words in release names, but they
do publish under the same org/owner — AbdomenAtlas and MrGiovanni were already in
the catalog — so watching catalog publishers catches this whole class.

The [`Track new datasets`](.github/workflows/track-datasets.yml) GitHub Action runs
it **weekly (Mondays 06:00 UTC)** (and on demand via *Run workflow*) and opens or
updates a single issue, **📡 New open radiology dataset candidates**, listing
everything not yet in the catalog for human review. Candidates not yet shown in an
earlier report are flagged **🆕** and sorted first, so the weekly review only needs
to scan the new rows. The issue body carries the cumulative seen-set in a hidden
`<!-- tracker-seen: … -->` comment; rows cut by the per-source display cap are *not*
recorded as seen, so a 🆕 backlog drains over the following weeks instead of being lost.
To enable the Kaggle *competitions* source, add `KAGGLE_USERNAME` / `KAGGLE_KEY`
repository secrets; an optional `HF_TOKEN` secret raises the Hugging Face rate limit
(all other sources are credential-free). *Run workflow* with **dry run** checked
prints the report to the job log instead of updating the issue.

Run it locally:

```bash
python3 scripts/find_new_datasets.py --limit 100          # full report
python3 scripts/find_new_datasets.py --prev prev.md       # flag 🆕 vs a previous report
python3 -m unittest discover -s scripts -p 'test_*.py'    # offline tests (no network)
```

The weekly loop end to end: **tracker issue → vet candidates (official page, scope,
duplicates) → add entries to `data/datasets.json` with label-structure details →
`python3 scripts/validate.py` → commit**. Asking Claude Code to "process this week's
tracker issue" covers the vet-research-add-validate steps in one pass.

The output is intentionally a *review queue*, not an auto-merge: candidates may be
out of scope, non-open, or duplicates under another name. Vet each, then add the
good ones to `data/datasets.json` (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## Bulk discovery (occasional)

For larger refreshes we run a multi-source discovery pass — parallel searches per
source and body region, each candidate adversarially verified against its official
page and deduped against the catalog, followed by a completeness-critic round.
This is how the catalog grew from 60 → 245 datasets. Re-run it when a whole area
needs refreshing rather than for incremental additions (that's the tracker's job).
