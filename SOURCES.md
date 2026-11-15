# Where the datasets come from — and how we track new ones

Keeping a radiology-dataset catalog current is the hard part. This repo uses **two
layers**: a broad one-time discovery sweep, and an ongoing automated tracker.

## Primary sources we monitor

| Source | What it holds | How we query it |
| --- | --- | --- |
| [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/) | DICOM cancer imaging collections (CT/MRI/PET), plus collections distributed outside NBIA (e.g. CDD-CESM, JPEG via Aspera) and label-only *analysis results* | NBIA REST API `getCollectionValues` **and** the site's `browse-collections` / `browse-analysis-results` listings |
| **Catalog publishers** | Follow-up releases from groups already in the catalog (AbdomenAtlas → PanTS → Merlin Plus) | Every Hugging Face org and GitHub owner in a catalog `url` (plus a few extras the URLs don't reveal: `stanfordmimi`, HF `MrGiovanni`): `/api/datasets?author=…&sort=createdAt` and `/users/…/repos?sort=created`, last 365 days, **no popularity floor** but must name an imaging modality or medical term — reported in the ⭐ Priority section |
| [Hugging Face Datasets](https://huggingface.co/datasets) | Foundation-model / report-paired / VLM sets (CT-RATE, MR-RATE, Merlin, RadGenome…) | `/api/datasets` `search` (matches the **repo id only**) **and** card-tag `filter` (`radiology`, `ct`, `mri`, `medical-imaging`…, by downloads and newest) + downloads/likes filter |
| [GitHub](https://github.com/search?type=repositories) | Dataset releases announced as a repo (README + download link to HF/Zenodo) | `/search/repositories` for "CT/MRI/X-ray/PET/mammography/radiology/medical imaging dataset" created in the last 120 days, top-starred; must *introduce* a dataset rather than use one ("the first public CT dataset" vs "trained on …") (uses the workflow's `GITHUB_TOKEN`) |
| [Grand Challenge](https://grand-challenge.org/) | Segmentation/detection challenges with expert labels | `/api/v1/challenges/` |
| [Zenodo](https://zenodo.org/) | DOI-minted dataset releases (ROCOv2, TotalSegmentator, Duke Liver…) | `/api/records?type=dataset`, per modality/organ term, `sort=newest` **and** `sort=mostviewed` (back-catalog; unauthenticated page cap is 25) |
| [Kaggle datasets](https://www.kaggle.com/datasets) | Community uploads & competition mirrors | `/api/v1/datasets/list` (unauthenticated) + download-count filter |
| [Kaggle competitions](https://www.kaggle.com/competitions) | RSNA/SPR/UW-Madison etc. medical-imaging challenges | `/api/v1/competitions/list` — needs `KAGGLE_USERNAME`/`KAGGLE_KEY` repo secrets (kaggle.com → Settings → API); skipped gracefully if unset |
| [PhysioNet](https://physionet.org/) | Credentialed clinical imaging (MIMIC-CXR family) | `/api/v1/project/published/` (full catalog JSON, filtered client-side) |
| [OpenNeuro](https://openneuro.org/) | BIDS neuroimaging | GraphQL `/crn/graphql`, newest public datasets, clinical/pathology keyword filter |
| [AWS Open Data Registry](https://registry.opendata.aws/) | RSNA challenge datasets, EMBED, UCSF releases (RMaC, BMSR, PCNSL, prostate) | registry YAML on GitHub (one tree call, medical-looking files fetched raw) |
| [figshare](https://figshare.com/) | Journal-linked datasets (DMID, CSAW-M, FUMPE, AVT) | `/v2/articles/search`, `item_type=3`, title must name a dataset and a modality |
| [Harvard Dataverse](https://dataverse.harvard.edu/) | Institutional deposits | `/api/search?type=dataset` |
| [VinDr](https://vindr.ai/datasets) | Vingroup releases, some request-only (VinDr-Multiphase) | dataset page listing |
| Dataset papers — *Scientific Data*, *Data in Brief* | The announcement of datasets hosted anywhere (CDD-CESM, NL-Breast-Screening, PLC-CECT, BreastDCEDL) | Crossref `journals/{ISSN}/works`, last two years, by relevance |
| [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) | Cloud-hosted public collections | manual (portal checklist) |
| Portals with no listing API — [RSNA MIRA](https://mira.rsna.org/), [Stanford AIMI index](https://aimidatasetindex.stanford.edu/), [BIMCV](https://bimcv.cipf.es/bimcv-projects/), [Science Data Bank](https://www.scidb.cn/en), [FRDR](https://www.frdr-dfdr.ca/repo/), [Mendeley Data](https://data.mendeley.com/) | Society benchmarks (REVEAL-CXR), AIMI releases (BrainMetShare), Chinese and Canadian repositories | printed in every report as a monthly manual checklist |
| Your own project notes | Datasets a research project discusses or downloads | `scripts/scan_mentions.py <folders>` (local) |

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

## Review loop — so candidates don't pile up unseen

- **Triage file.** `data/triage.json` records every decision on a candidate that is *not* added:
  `rejected` (out of scope, not data, broken link), `deferred` (with `until`), or `added`
  (it is a catalog entry under another name). The tracker drops those rows, so the queue
  shrinks instead of growing. Synonyms of catalog entries go into the entry's `aliases`
  (names, paper titles) and `links` (other official locations) instead.
- **Backlog rotation.** Each source section shows at most 50 rows. Rows past that cap used to
  be invisible forever once they lost 🆕; the report now shows a different window of 25 of
  them every week (🗂 Backlog rotation) until they are added or triaged.
- **Monthly auto-triage.** On the 5th, `.github/workflows/triage-candidates.yml` re-runs the
  scan and `scripts/triage_candidates.py` works through up to 40 candidates (priority rows
  first): it fetches each candidate's official metadata itself (Zenodo / Hugging Face /
  GitHub / figshare APIs, else the page text) and asks Claude (`claude-opus-5-5`, no tools —
  page text can't make it run anything) for a JSON decision: `add` with a full entry,
  `duplicate`, `reject` or `defer`. The script validates every proposed entry, records the
  other decisions in `data/triage.json` (field `by` marks automatic ones) and the workflow
  opens a **draft PR** for a person to review and merge. Auth is Workload Identity
  Federation (no stored API key); a per-run budget cap and the workspace spend limit bound
  the cost. Run it by hand (Actions → Monthly dataset triage → Run workflow) with a larger
  `max_candidates` to drain a backlog.
- **Portal checklist.** Hosts without an API are listed in every report; check them monthly.
- **Your notes.** Research projects find datasets before the tracker does. Run
  `python3 scripts/scan_mentions.py <notes folders>` — it lists dataset links in your Markdown
  notes whose identifier appears nowhere in the catalog (or triage file).

## Gap audit (2026-11) — why datasets were missed

Two research projects (an LLM/decision-model calibration study on CXR + mammography, and a
CT/MRI series-identity program) had used or discussed ~25 datasets that were not in the
catalog. Causes, and the fix for each:

| Cause | Examples | Fix |
| --- | --- | --- |
| Host not polled | DMID (figshare), UCSF-RMaC (AWS), REVEAL-CXR (RSNA MIRA), BrainMetShare (AIMI), VinDr-Multiphase (VinDr portal), PLC-CECT (Science Data Bank) | figshare, Dataverse, AWS registry, VinDr sources; paper-first Crossref layer; portal checklist |
| TCIA collections outside NBIA / analysis results | CDD-CESM (Aspera, JPEG), LiverHccSeg | read the TCIA site listings as well as NBIA |
| Label-only sets out of scope | Google expert labels for NIH ChestX-ray14, CXR-LT | new `annotation` type and `label_variants` |
| Surfaced but never reviewed (cap of 50 rows/source; seen ≠ reviewed) | CPTAC-CCRCC, CPTAC-PDA, 4D-Lung, LDCT-and-Projection, Pelvic-Reference-Data | backlog rotation + `data/triage.json` |
| Search too shallow / filters too narrow | WAW-TACE, UniToBrain (Zenodo page cap, generic terms); MR-ART (OpenNeuro newest-100, "clinical" keyword filter) | phase/protocol Zenodo terms + 2nd page; OpenNeuro paging + artefact/QC keywords |
| Same dataset under another URL looked new | RSNA AWS releases, Zenodo records of challenge data | `links` on the catalog entry |

## Bulk discovery (occasional)

For larger refreshes we run a multi-source discovery pass — parallel searches per
source and body region, each candidate adversarially verified against its official
page and deduped against the catalog, followed by a completeness-critic round.
This is how the catalog grew from 60 → 245 datasets. Re-run it when a whole area
needs refreshing rather than for incremental additions (that's the tracker's job).
