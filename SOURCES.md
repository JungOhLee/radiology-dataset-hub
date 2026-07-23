# Where the datasets come from — and how we track new ones

Keeping a radiology-dataset catalog current is the hard part. This repo uses **two
layers**: a broad one-time discovery sweep, and an ongoing automated tracker.

## Primary sources we monitor

| Source | What it holds | How we query it |
| --- | --- | --- |
| [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/) | DICOM cancer imaging collections (CT/MRI/PET) | NBIA REST API `getCollectionValues` |
| [Hugging Face Datasets](https://huggingface.co/datasets) | Foundation-model / report-paired / VLM sets (CT-RATE, MR-RATE, Merlin, RadGenome…) | `/api/datasets` search + downloads/likes filter |
| [Grand Challenge](https://grand-challenge.org/) | Segmentation/detection challenges with expert labels | `/api/v1/challenges/` |
| [Zenodo](https://zenodo.org/) | DOI-minted dataset releases (ROCOv2, TotalSegmentator…) | `/api/records?type=dataset` |
| [PhysioNet](https://physionet.org/) | Credentialed clinical imaging (MIMIC-CXR family) | manual / release feed |
| [OpenNeuro](https://openneuro.org/) | BIDS neuroimaging | manual |
| [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) | Cloud-hosted public collections | manual |
| Stanford AIMI, arXiv, Papers With Code | New dataset papers & institutional releases | manual / literature |

## Automated tracker

`scripts/find_new_datasets.py` queries the API-backed sources above, filters for
radiology relevance and (for Hugging Face) a minimum download/like count to skip
personal reuploads, then **diffs against `data/datasets.json`** — including
substring matching so mirrors of datasets we already list are suppressed.

The [`Track new datasets`](.github/workflows/track-datasets.yml) GitHub Action runs
it **monthly** (and on demand via *Run workflow*) and opens or updates a single
issue, **📡 New open radiology dataset candidates**, listing everything not yet in
the catalog for human review.

Run it locally:

```bash
python3 scripts/find_new_datasets.py --limit 100
```

The output is intentionally a *review queue*, not an auto-merge: candidates may be
out of scope, non-open, or duplicates under another name. Vet each, then add the
good ones to `data/datasets.json` (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## Bulk discovery (occasional)

For larger refreshes we run a multi-source discovery pass — parallel searches per
source and body region, each candidate adversarially verified against its official
page and deduped against the catalog, followed by a completeness-critic round.
This is how the catalog grew from 60 → 245 datasets. Re-run it when a whole area
needs refreshing rather than for incremental additions (that's the tracker's job).
