# 🩻 Radiology Dataset Hub

**Find the right open-source radiology dataset for your research — fast.**

A curated, filterable catalog of **open-source radiology imaging datasets** across **CT, MRI, PET and X-ray**.
Every entry is organized by body region and tagged with the metadata you actually use to pick a dataset:
native image format (DICOM/NIfTI vs. derived JPEG/PNG), **paired text/reports**, **multi-sequence / multi-phase**
images, **segmentation labels**, size, license and access route.

### 🔎 [**Browse the interactive catalog →**](https://jungohlee.github.io/radiology-dataset-hub/)

> Search and filter by modality, body region, "has segmentation", "has paired text", "multi-sequence",
> "raw DICOM/NIfTI only" and "open access only" — no scrolling through a giant markdown wall.

---

## Why another list?

Existing lists (which are great starting points) tend to be **flat markdown** with a name and a link, or
comprehensive tables with **no way to filter**. When you have a concrete need — *"a multi-sequence brain MRI
dataset with tumor segmentation and an open license"* — you still have to open 30 links to find out.

This hub is built around **dataset selection**:

- **Raw-image first.** Native DICOM/NIfTI/NRRD are flagged 🟢; derived PNG/JPEG are flagged 🟡 so you know what you're getting.
- **Selection metadata on every card** — paired text (image–text/multimodal), multi-sequence/phase, segmentation labels, license, access. Each dataset's **label schema, file layout and splits** are one click away in the detail view.
- **Organized by body region, and a dataset can belong to several** — multi-organ/whole-body sets appear under each region they cover (`regions` is an array, not a single category).
- **Multimodal is a characteristic, not a section** — image–text/VLM datasets carry the *paired text* attribute and live under their actual body region(s).
- **One machine-readable source** ([`data/datasets.json`](data/datasets.json)) generates both the website and the tables below — easy to query, easy to contribute to.
- **Kept current automatically** — a monthly tracker scans dataset-source APIs for new releases; see [SOURCES.md](SOURCES.md).

## How to use

- **Interactive site:** <https://jungohlee.github.io/radiology-dataset-hub/> — filter and search live.
- **Tables below:** browse by region right here on GitHub.
- **Programmatic:** fetch [`data/datasets.json`](data/datasets.json) directly.

---

<!-- AUTOGEN:START -->

**714 curated datasets** · 340 CT · 354 MRI · 81 PET · 159 X-ray · 563 native DICOM/NIfTI · 131 with reports/text · 377 with segmentation labels

Jump to: [Neuro (Brain & Spine)](#neuro-brain-spine) · [Chest & Thorax](#chest-thorax) · [Cardiac](#cardiac) · [Vascular](#vascular) · [Abdominal](#abdominal) · [Pelvic & Prostate](#pelvic-prostate) · [Musculoskeletal](#musculoskeletal) · [Breast](#breast) · [Head & Neck](#head-neck) · [Dental & Maxillofacial](#dental-maxillofacial) · [Whole-Body & PET](#whole-body-pet) · [Multiple / Various body parts](#multiple-various-body-parts) · [Data Repositories & Portals](#data-repositories-portals)

**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). Text = paired reports/captions/QA (i.e. image–text / multimodal) · Seg = segmentation masks · Multi = multi-sequence MRI or multi-phase CT. 🏷 = label/annotation set for another dataset's images. Access: OPEN = direct download · REGISTRATION = free account · DUA = data-use agreement · REQUEST = apply for access. **Datasets covering several body regions (128) appear under each region.**

### 🧠 Neuro (Brain & Spine)  <sub>(205)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [BEAMSTER](https://doi.org/10.6084/m9.figshare.29365844) | MRI | 2026 | 🟢 NIfTI, CSV, XLSX | — | ✅ | — | OPEN | 140 patients / 140 contrast-enhanced T1 MRI volumes; 260 annotated metastases |
| [Brain MRI Clinical Protocol Motion Dataset](https://doi.org/10.1038/s41597-026-07144-z) | MRI | 2026 | 🟢 NIfTI, ISMRMRD | — | — | ✅ | OPEN | 22 healthy adults; 6 sequences (T1 MPR n=22, T2 FLAIR n=10, T1 STIR n=22, T2 TSE n=22, T2* GRE n=19, DWI n=10), each still/nodding (plus shaking for T1 MPR) with and without prospective motion correction |
| [BrainTRACE](https://huggingface.co/datasets/lanqz7766/BrainTRACE) 🏷 | MRI | 2026 | 🟡 Parquet | ✅ | — | — | OPEN | 6,923 source rows / 7,273 scored VQA instances; source cohort of 1,778 patients and 7,299 MR-RATE studies |
| [CFB-GBM](https://www.cancerimagingarchive.net/collection/cfb-gbm/) | MRI, CT | 2026 | 🟢 NIfTI, TSV | ✅ | ✅ | ✅ | OPEN | 208.01 GB; 264 patients |
| [Clinical Brain MRI Motion Artifact Paired Dataset](https://figshare.com/articles/dataset/A_clinical_brain_MRI_dataset_of_naturally_occurring_motion_artifacts_with_paired_artifact-free_images/30978316) | MRI | 2026 | 🟡 — | — | — | ✅ | OPEN | 5,143 paired 2D slices from 731 patients and 147 paired 3D volumes from 146 patients; ~16 GB |
| [FOMO260K](https://doi.org/10.57967/hf/8670) | MRI | 2026 | 🟢 NIfTI | — | — | ✅ | OPEN | 260,927 MRI scans / 77,589 sessions / 55,378 subjects from 910 public sources |
| [Multi-b-value Test-Retest dMRI (OpenNeuro ds008695)](https://openneuro.org/datasets/ds008695) | MRI | 2026 | 🟢 NIfTI | — | — | ✅ | OPEN | 11 healthy volunteers x 4 sessions; raw data 8.3 GB, preprocessed 39.5 GB |
| [PROTEAS Brain Metastases](https://zenodo.org/records/23171182) | MRI, CT | 2026 | 🟡 — | — | ✅ | — | OPEN | 185 imaging studies (MRI and CT) / 40 patients; 65 segmented brain metastases |
| [Pedi-Cranial-CT-Healthy](https://www.cancerimagingarchive.net/collection/pedi-cranial-ct-healthy/) | CT | 2026 | 🟢 MHA | — | — | — | OPEN | 100 non-contrast cranial CT volumes / 100 healthy subjects (aged 1 month to 10 years); 3.2 GB |
| [Pediatric Brain MRI Motion Correction (Rigshospitalet)](https://doi.org/10.70883/vmif5895) | MRI | 2026 | 🟢 NIfTI, BIDS | — | — | ✅ | DUA | 47 children aged 4-11 years, one session each (variable number of structural sequences per child) |
| [Penn Epilepsy 3T-7T MRI + iEEG](https://doi.org/10.26275/aosz-hj9u) | MRI, CT | 2026 | 🟢 NIfTI, BIDS | — | ✅ | ✅ | OPEN | 30 drug-resistant focal epilepsy patients with paired 3T and 7T MRI; iEEG epochs and post-implant CT for 15 of them |
| [UCSD-BMETS-Longitudinal](https://www.cancerimagingarchive.net/collection/ucsd-bmets-longitudinal/) | MRI | 2026 | 🟢 NIfTI, TSV | — | ✅ | ✅ | OPEN | 300 patients / 1,065 MRI timepoints (TCIA table: 1,066 studies, 11,405 series); 163 GB |
| [UCSD-VS-Longitudinal](https://www.cancerimagingarchive.net/collection/ucsd-vs-longitudinal/) | MRI | 2026 | 🟢 NIfTI, TSV | — | ✅ | ✅ | OPEN | 570 MRI timepoints / 191 patients; 4,391 series; ~40 GB |
| [UTSW-Glioma](https://www.cancerimagingarchive.net/collection/utsw-glioma/) | MRI | 2026 | 🟢 NIfTI, TSV | — | ✅ | ✅ | OPEN | 625 patients / 6,349 series; 22.9 GB |
| [Aging Mouse Brain rdMRI 9.4T](https://doi.org/10.6084/m9.figshare.28433102) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | 30 male C57BL/6 mice (5 age groups x 6: 2, 6, 12, 18, 24 months) |
| [BCBM-RadioGenomics](https://www.cancerimagingarchive.net/collection/bcbm-radiogenomics/) | MRI | 2025 | 🟢 NIfTI, XLSX | — | ✅ | — | OPEN | 268 T1 post-contrast MRI studies / 165 patients (3,089 series); 10.72 GB |
| [BRISC2025](https://www.kaggle.com/datasets/briscdataset/brisc2025) | MRI | 2025 | 🟡 JPG | — | ✅ | — | OPEN | 6,000 contrast-enhanced T1-weighted MRI images across axial, sagittal, and coronal planes |
| [BraTS-Lighthouse 2025](https://www.synapse.org/Synapse:syn64153130) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 11 tasks. New 2025 data: BraTS-METS 2025 with 1,296 training / 179 validation / 305 test pre- and post-treatment metastasis cases, and a 150-case Lighthouse test set (75 metastases, 25 gliomas, 25 meningiomas, 25 meningioma-RT). Most other segmentation tasks reuse earlier BraTS training/validation data. |
| [Brain-Mets-Lung-MRI-Path-Segs](https://www.cancerimagingarchive.net/collection/brain-mets-lung-mri-path-segs/) | MRI | 2025 | 🟢 NIfTI, SVS, XLSX | ✅ | ✅ | ✅ | OPEN | 19.21 GB; 103 patients (111 imaging-pathology pairs) |
| [Circadian Rhythmicity MID fMRI (ds005479)](https://openneuro.org/datasets/ds005479) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | 37 participants (healthy men aged 20-30); one T1w, one task-fMRI run (397 volumes) and AP/PA fieldmaps each |
| [Ex-vivo Brain 7T Multimodal MRI](https://doi.org/10.1038/s41597-025-04932-x) | MRI | 2025 | 🟢 — | — | ✅ | ✅ | OPEN | 6 ex-vivo right-hemisphere specimens (Chinese adult donors) plus population-average templates |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [Germinoma MRI/CT Dataset](https://doi.org/10.1038/s41597-025-04596-7) | MRI, CT | 2025 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | ✅ | OPEN | 65 patients; 63 CT and 50 MRI studies |
| [Low-Field Infant Brain MRI (0.35 T)](https://doi.org/10.57760/sciencedb.10690) | MRI | 2025 | 🟢 NIfTI | — | ✅ | — | DUA | 100 infants (54 female, 46 male), one axial T2w scan each (14-16 slices) |
| [MR-RATE](https://huggingface.co/datasets/Forithmus/MR-RATE) | MRI | 2025 | 🟢 NIfTI, CSV | ✅ | ✅ | ✅ | REGISTRATION | 705,254 MRI volumes from 98,334 studies of 83,425 patients (~8-38 TB across repositories) |
| [MU-Glioma-Post](https://www.cancerimagingarchive.net/collection/mu-glioma-post/) | MRI | 2025 | 🟢 NIfTI, XLSX | ✅ | ✅ | ✅ | OPEN | 11 GB; 203 patients (596 timepoints) |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [Nigerian Brain MRI](https://doi.org/10.25663/brainlife.pub.61) | MRI | 2025 | 🟢 NIfTI, BIDS | — | ✅ | ✅ | DUA | 88 participants (31 dementia, 22 Parkinson's disease, 35 controls); 761 anatomical sequences; >15 GB including derivatives |
| [OpenMind](https://huggingface.co/datasets/AnonRes/OpenMind) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | OPEN | ~114K MRI images (1.04 TB) curated from 800 OpenNeuro datasets across 30+ scanners |
| [Paired 3T-7T MRI Hippocampal Subfields](https://doi.org/10.1038/s41597-025-04586-9) | MRI | 2025 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | OPEN | 20 healthy volunteers, each with paired 3T and 7T scans |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RSNA 2025 Aneurysm Detection](https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection) | CT, MRI | 2025 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 4,000+ studies (CTA/MRA/MRI); ~200 with segmentation |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [Spine Generic (Multi-Subject)](https://github.com/spine-generic/data-multi-subject) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | ~260+ subjects, ~26 GB, 40+ sites |
| [TopBrain 2025](https://topbrain2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Batches 1-2 on Zenodo: 50 angiographic scans (25 paired CTA/MRA subjects), ~2.0 GB; 40 CTA / 42 MRA vessel labels (34 overlapping) |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [Trigeminal Neuralgia Pre/Post-Surgical MRI](https://doi.org/10.1038/s41597-025-06311-y) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | 160 participants (112 trigeminal neuralgia patients, 48 healthy controls); 6-month post-treatment follow-up MRI for 58 patients |
| [UCSD-PTGBM](https://www.cancerimagingarchive.net/collection/ucsd-ptgbm/) | MRI | 2025 | 🟢 NIfTI, XLSX | — | ✅ | ✅ | OPEN | 243 timepoints / 178 patients; 44.98 GB |
| [Vestibular-Schwannoma-MC-RC2](https://www.cancerimagingarchive.net/collection/vestibular-schwannoma-mc-rc2/) | MRI | 2025 | 🟢 NIfTI, XLSX, TSV | — | ✅ | ✅ | OPEN | 190 patients, 621 time points; 543 T1CE, 481 T1 and 133 T2 scans (1,157 scans); ~6 GB |
| [Yale-Brain-Mets-Longitudinal](https://www.cancerimagingarchive.net/collection/yale-brain-mets-longitudinal/) | MRI | 2025 | 🟢 NIfTI, XLSX | — | — | ✅ | OPEN | 11,892 MRI studies / 33,811 series / 1,430 patients; ~43 GB |
| [APIS](https://bivl2ab.uis.edu.co/challenges/apis) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 100 studies (60 train / 40 test) |
| [ARC](https://openneuro.org/datasets/ds004884) | MRI | 2024 | 🟢 NIfTI, BIDS | — | ✅ | ✅ | OPEN | 230 chronic stroke patients / 902 sessions; 228 expert lesion masks |
| [BAMF AIMI Annotations](https://zenodo.org/records/13244892) 🏷 | CT, MRI, PET | 2024 | 🟡 DICOM-SEG, CSV | — | ✅ | — | OPEN | 11 task archives (~650 MB total) of AI segmentations for IDC collections; ~10% of predictions reviewed/corrected |
| [BONBID-HIE 2024](https://bonbid-hie2024.grand-challenge.org/) | MRI | 2024 | 🟢 MHA | — | ✅ | ✅ | OPEN | Labeled MGH cohort (~133 patients on base record) plus unlabeled BCH cohort; 44 test cases (Track 1 segmentation), 53 test cases (Track 2 outcome prediction), 4 validation cases per track |
| [BraTS 2024 Post-Treatment Glioma (BraTS-GLI)](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2200 multi-institutional post-treatment MRI cases |
| [BraTS-GoAT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | Pooled multi-tumor BraTS cohort (thousands of cases across glioma, meningioma, metastases, pediatric) |
| [BraTS-MEN-RT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 750 radiotherapy-planning brain MRIs (multi-institutional) with expert GTV annotations on the training/validation partitions |
| [Brain-Structure (Radiata)](https://huggingface.co/datasets/radiata-ai/brain-structure) | MRI | 2024 | 🟢 NIfTI | — | — | — | OPEN | 3794 T1w MRI scans / 2607 individuals |
| [COSTA](https://doi.org/10.5281/zenodo.11025761) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REQUEST | 423 TOF-MRA volumes across 8 centers (4 vendors, 1.5T/3.0T) |
| [CPAISD](https://zenodo.org/records/10892316) | CT | 2024 | 🟢 DICOM, NPZ | — | ✅ | — | OPEN | 112 non-contrast cranial CT studies; 10,165 slices; 5.2 GB |
| [DFCI-BCH-BWH-PEDs-HGG](https://www.cancerimagingarchive.net/collection/dfci-bch-bwh-peds-hgg/) | MRI | 2024 | 🟢 NIfTI, XLSX | — | — | ✅ | OPEN | 61 subjects / 245 series; 2.16 GB |
| [EPVS 2024](https://www.synapse.org/Synapse:syn54100278/wiki/626542) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 200 brain MRI scans: 100 training (with masks), 50 validation, 50 test, from 4 cohorts (Edinburgh, NUS-SG70, NUS-MACC, Shanghai TCM); training set ~3.3 GB (400 NIfTI files) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [ISLES 2024](https://isles-24.grand-challenge.org/) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~150 training cases |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MSLesSeg 2024](https://iplab.dmi.unict.it/mfs/ms-les-seg/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~90 patients, ~150 MRI timepoints (1-5 per patient) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [SPR Head CT Age Prediction](https://www.kaggle.com/competitions/spr-head-ct-age-prediction-challenge) | CT | 2024 | 🟢 DICOM | — | — | — | REGISTRATION | 2,525 head CT studies (2,377 train + 148 test) |
| [UCSF-ALPTDG](https://imagingdatasets.ucsf.edu/dataset/2) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 298 patients; 596 post-treatment MRI exams (two consecutive posttreatment timepoints per patient) |
| [BONBID-HIE](https://zenodo.org/records/8104103) | MRI | 2023 | 🟢 MHA | — | ✅ | ✅ | OPEN | 133 neonates |
| [BraTS-Africa](https://www.cancerimagingarchive.net/collection/BraTS-Africa/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 146 patients |
| [BraTS-MEN](https://www.synapse.org/Synapse:syn51514106) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 1,650 cases (1,000 public training) |
| [BraTS-Mets](https://www.synapse.org/Synapse:syn51156910/wiki/622553) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 328 cases (238 public training) |
| [BraTS-PEDs](https://www.synapse.org/Synapse:syn51156910/wiki/622461) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 228 patients (99 public training) |
| [Brain-TR-GammaKnife](https://www.cancerimagingarchive.net/collection/brain-tr-gammaknife/) | MRI | 2023 | 🟢 DICOM, NRRD | — | ✅ | — | DUA | 47 patients, 76 studies, 228 series, 16,792 images (DICOM, 9.59 GB); 244 annotated lesions |
| [Burdenko-GBM-Progression](https://www.cancerimagingarchive.net/collection/burdenko-gbm-progression/) | CT, MRI | 2023 | 🟢 DICOM | — | ✅ | ✅ | DUA | 180 patients; 645 studies; 4,956 series; 344,003 images; 131.23 GB |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [Infant Brain MRI Myelin Maturation](https://zenodo.org/records/8055666) | MRI | 2023 | 🟡 — | — | — | ✅ | OPEN | 833 brain MRI cases (T1w and T2w); 11.3 GB zip |
| [M4Raw](https://github.com/mylyu/M4Raw) | MRI | 2023 | 🟡 HDF5 | — | — | ✅ | OPEN | — |
| [Meningioma-SEG-CLASS](https://www.cancerimagingarchive.net/collection/meningioma-seg-class/) | MRI | 2023 | 🟢 DICOM, XLSX | — | ✅ | ✅ | DUA | 96 patients (180 studies, 674 series, 47,520 images, 9.39 GB) |
| [Pretreat-MetsToBrain-Masks](https://www.cancerimagingarchive.net/collection/pretreat-metstobrain-masks/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 200 subjects (1000 studies), 1.7 GB |
| [Queensland Twin Adolescent Brain (QTAB)](https://openneuro.org/datasets/ds004146) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | OPEN | 417 subjects (twin pairs), ~683 GB, 27718 files; two timepoints |
| [RHUH-GBM](https://www.cancerimagingarchive.net/collection/rhuh-gbm/) | MRI | 2023 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 40 patients; ~600 series, 37,425 DICOM images (15.96 GB) plus 2.9 GB NIfTI |
| [ReMIND](https://www.cancerimagingarchive.net/collection/remind/) | MRI | 2023 | 🟢 DICOM, NRRD | ✅ | ✅ | ✅ | OPEN | 114 subjects; 43.6 GB (preop MRI 4 sequences, 301 intraop MRI series, 320 intraop 3D US series) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SMILE-UHURA](https://osf.io/jg7cr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | ~14 annotated training subjects (7T ToF-MRA volumes) plus held-out test set |
| [Seg-CQ500](https://zenodo.org/records/8063221) 🏷 | CT | 2023 | 🟡 — | — | ✅ | — | OPEN | 3D ICH masks for 51 CQ500 head CT scans (Seg-CQ500.zip, 2.3 GB) |
| [SynthRAD2023](https://synthrad2023.grand-challenge.org/) | MRI, CT | 2023 | 🟢 MHA | — | — | — | OPEN | 540 paired MRI-CT and 540 CBCT-CT sets (>500 patients per task) from three centers |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [Vestibular-Schwannoma-MC-RC](https://www.cancerimagingarchive.net/collection/vestibular-schwannoma-mc-rc/) | MRI | 2023 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | OPEN | 160 patients, 427 timepoints, 487 3D MRI images (30,102 DICOM images); 14.25 GB |
| [crossMoDA 2023](https://crossmoda-challenge.ml/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [ATLAS R2.0](https://atlas.grand-challenge.org/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 655 labeled T1w MRIs (+300 hidden test) |
| [BigBrain-MR](https://zenodo.org/records/7432527) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Single whole-brain digital phantom at 100, 400 and 800 µm isotropic resolution (~30 NIfTI files, ~29 GB) |
| [Developing Human Connectome Project (dHCP)](http://www.developingconnectome.org/data-release/) | MRI | 2022 | 🟢 NIfTI, BIDS | — | ✅ | ✅ | DUA | ~783 neonates (886 datasets) and ~273 fetuses (4th release) |
| [GammaKnife-Hippocampal](https://www.cancerimagingarchive.net/collection/gammaknife-hippocampal/) | CT, MRI | 2022 | 🟢 DICOM | — | ✅ | ✅ | REQUEST | 390 patients; 1,509 studies; 8,307 series; 565,921 images; 312.06 GB |
| [INSTANCE 2022](https://instance.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 NCCT scans (100 train) |
| [ISLES 2022](https://zenodo.org/records/7153326) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 250 training cases |
| [LUMIERE](https://springernature.figshare.com/articles/dataset/The_LUMIERE_Dataset/16944846) | MRI | 2022 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 91 patients, 638 study dates, 2487 MRI images (~32.5 GB imaging ZIP) |
| [MR-ART](https://openneuro.org/datasets/ds004173) | MRI | 2022 | 🟢 NIfTI | — | — | — | OPEN | 148 healthy adults, up to 3 T1-weighted scans each (8 participants miss one motion scan) |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [RSNA 2022 Cervical Spine Fracture](https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection) | CT | 2022 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~3,000 CT studies |
| [Shifts MS](https://zenodo.org/records/7051658) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [UCSF-PDGM](https://www.cancerimagingarchive.net/collection/ucsf-pdgm/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 495 patients |
| [UPenn-GBM](https://www.cancerimagingarchive.net/collection/upenn-gbm/) | MRI | 2022 | 🟢 NIfTI, DICOM | — | ✅ | ✅ | OPEN | 630 glioblastoma patients |
| [fastMRI+](https://github.com/microsoft/fastmri-plus) | MRI | 2022 | 🟡 CSV (annotations only) | — | — | — | OPEN | 24,380 annotations, no images: knee 16,154 bounding boxes + 13 study-level labels (22 classes, all 1,172 knee volumes) and brain 7,570 bounding boxes + 643 study-level labels (30 classes, 1,001 of 5,847 brain studies) |
| [BraTS 2021](https://www.synapse.org/Synapse:syn25829067) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2,040 patients (1,251 public training) |
| [BrainPTM 2021](https://brainptm-2021.grand-challenge.org/) | MRI | 2021 | 🟢 — | — | ✅ | ✅ | DUA | 75 cases (60 training with annotations, 15 test without) |
| [FeTA](https://www.synapse.org/Synapse:syn25649159) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | DUA | ~80 subjects (FeTA 2021) |
| [FeTS 2021/2022](https://fets-ai.github.io/Challenge/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [GLIS-RT](https://www.cancerimagingarchive.net/collection/glis-rt/) | CT, MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 230 patients (28.26 GB) |
| [MSSEG-2](https://portal.fli-iam.irisa.fr/msseg-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 patients, 2 time-points each |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [UniToBrain](https://zenodo.org/records/5109415) | CT | 2021 | 🟢 DICOM | — | — | — | OPEN | Zenodo: 115 subjects (100 train / 15 test), 50.8 GB; full 258-subject collection on IEEE DataPort (80.04 GB) |
| [Vestibular-Schwannoma-SEG](https://www.cancerimagingarchive.net/collection/vestibular-schwannoma-seg/) | MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 28.21 GB |
| [ADAM](https://adam.isi.uu.nl/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 113 training TOF-MRA cases |
| [BHX](https://physionet.org/content/bhx-brain-bounding-box/1.1/) 🏷 | CT | 2020 | 🟡 CSV | — | — | — | OPEN | 6,283 manual boxes on 3,558 thick-slice images; 39,668 boxes on 23,409 images after extrapolation (clean set: 27,203 boxes on 15,979 images); from the 491-scan CQ500 dataset |
| [CADA](https://cada.grand-challenge.org/) | X-ray | 2020 | 🟢 NIfTI, STL | — | ✅ | — | REGISTRATION | 131 3DRA datasets (115 patients) |
| [CT-ICH (PhysioNet)](https://physionet.org/content/ct-ich/1.3.1/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | DUA | 82 non-contrast head CT scans (75 public in NIfTI); 36 with hemorrhage |
| [EPISURG](https://rdr.ucl.ac.uk/articles/dataset/EPISURG/9996158) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 430 postoperative T1w MRIs |
| [GBM-DSC-MRI-DRO](https://www.cancerimagingarchive.net/collection/gbm-dsc-mri-dro/) | MRI | 2020 | 🟢 DICOM | — | ✅ | — | OPEN | 3 subjects (computational phantoms), 31 studies, 364 series, 47,164 images; 4.46 GB |
| [Hamburg City Health Study](https://hchs.hamburg/) | MRI | 2020 | 🟢 DICOM | — | — | ✅ | REQUEST | ~45,000-participant target (>17,000 enrolled) |
| [Hypothalamic Region MRI Atlas (MDA 990 HCP)](https://zenodo.org/records/3942115) | MRI | 2020 | 🟢 NIfTI, CSV | — | ✅ | ✅ | OPEN | Population-average T1w and T2w MDA templates at 0.25 and 0.5 mm isotropic resolution, built from 990 HCP1200 subjects; 25 labelled structures |
| [ICDC-Glioma](https://www.cancerimagingarchive.net/collection/icdc-glioma/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | MR: 57 canine subjects, 58 studies, 650 series, 17,797 images (5.1 GB); plus H&E whole-slide images for 78 subjects (172 GB) |
| [LDCT-and-Projection-data](https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/) | CT | 2020 | 🟢 DICOM, DICOM-CT-PD | — | — | — | OPEN | 299 patient exams + 1 phantom: chest 99 (256.81 GB), liver/abdomen 100 (604.12 GB), head 99 (462.77 GB, restricted) |
| [MOOD](https://www.synapse.org/mood) | MRI, CT | 2020 | 🟢 NIfTI | — | — | — | REGISTRATION | ~800 brain MRI + ~600 abdominal CT scans |
| [VerSe](https://github.com/anjany/verse) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 374 CT scans / ~4,500 vertebrae |
| [fastMRI Brain](https://fastmri.med.nyu.edu) | MRI | 2020 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | 6,970 brain MRI volumes |
| [ACRIN-DSC-MR-Brain](https://www.cancerimagingarchive.net/collection/acrin-dsc-mr-brain/) | MRI, CT | 2019 | 🟢 DICOM | — | — | ✅ | REQUEST | 123 subjects / 566 studies / 7,629 series / 717,070 images (86.89 GB) |
| [ACRIN-FMISO-Brain](https://www.cancerimagingarchive.net/collection/acrin-fmiso-brain/) | PET, MRI, CT | 2019 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 96 GB |
| [Crowds-Cure-2018](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2018/) 🏷 | CT | 2019 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | 4,756 bi-directional lesion measurements on CT scans of 324 patients from 13 TCIA collections; label files 5.76 MB |
| [EDEN2020 Healthy Brain MRI](https://zenodo.org/records/3994749) | MRI | 2019 | 🟢 NIfTI | — | — | ✅ | OPEN | 15 healthy adult subjects (~6.6 GB, one zip per subject) |
| [OASIS-3](https://sites.wustl.edu/oasisbrains/) | MRI, PET | 2019 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 1378 participants |
| [RSNA 2019 ICH Detection](https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection) | CT | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 25,272 non-contrast head CT exams |
| [iSeg](https://iseg2019.web.unc.edu) | MRI | 2019 | 🟢 Analyze | — | ✅ | ✅ | DUA | iSeg-2019: 39 subjects (multi-site) |
| [ABCD Study](https://nda.nih.gov/abcd) | MRI | 2018 | 🟢 NIfTI, DICOM | — | — | ✅ | DUA | ~11,880 children |
| [BigBrain FDG PET Brain Phantom](https://zenodo.org/records/8045458) | PET, MRI, CT | 2018 | 🟢 NIfTI, RAW, MAT | — | ✅ | — | OPEN | 1 digital phantom (uptake, attenuation map, CT, MRI and tissue-class volumes); ~3.1 GB across 7 files |
| [Brain-Tumor-Progression](https://www.cancerimagingarchive.net/collection/brain-tumor-progression/) | MRI | 2018 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 3.16 GB |
| [CPTAC-GBM](https://www.cancerimagingarchive.net/collection/cptac-gbm/) | MRI, CT | 2018 | 🟢 DICOM | — | — | ✅ | REGISTRATION | 41.1 GB radiology (192.6 GB with histopathology) |
| [CQ500](http://headctstudy.qure.ai/dataset) | CT | 2018 | 🟢 DICOM | — | — | — | OPEN | 491 head CT scans |
| [Calgary-Campinas CC-359](https://www.ccdataset.com) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 359 T1w volumes (+ raw k-space subset) |
| [Generation R](https://generationr.nl/researchers/) | MRI, DXA | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~several thousand children with repeated brain MRI and DXA (birth cohort of ~9,700 mothers/children) |
| [HCP Lifespan (HCP-Aging & HCP-Development)](https://www.humanconnectome.org/study/hcp-lifespan-aging) | MRI | 2018 | 🟢 NIfTI, derived | — | ✅ | ✅ | REGISTRATION | ~1,500 aging adults (ages 36-100+) plus ~1,300-1,400 youth (ages 5-21) |
| [MRBrainS](https://mrbrains18.isi.uu.nl) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | MRBrainS18: 30 subjects (7 fully annotated) |
| [MRI of 3-12 year old children (Pixar)](https://openneuro.org/datasets/ds000228) | MRI | 2018 | 🟢 NIfTI | — | — | ✅ | OPEN | 155 subjects (122 children, 33 adults) |
| [NiftyPET Amyloid PET mMR Scan](https://zenodo.org/records/3877529) | PET, MRI | 2018 | 🟢 PET list-mode (raw) | — | ✅ | — | OPEN | 1 scan: 60-min dynamic list-mode florbetapir PET with normalisation files, UTE mu-map, T1w MRI, parcellation and pseudo-CT; 9.3 GB zip |
| [TractSeg HCP105 Reference Tracts](https://zenodo.org/records/1477956) 🏷 | MRI | 2018 | 🟡 TRK | — | ✅ | — | OPEN | 72 white matter tracts x 105 HCP subjects; 41.0 GB zip |
| [BraTS-TCGA-GBM](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-gbm/) 🏷 | MRI | 2017 | 🟢 NIfTI, CSV | — | ✅ | ✅ | OPEN | 102 subjects available (processed NIfTI with segmentations, 767 MB); 33-subject BraTS test set no longer available; derived from 135 TCGA-GBM subjects |
| [BraTS-TCGA-LGG](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-lgg/) 🏷 | MRI | 2017 | 🟢 NIfTI, CSV | — | ✅ | ✅ | OPEN | 108 subjects labelled; 65-subject training set currently downloadable (536 MB); 43-subject test set no longer available |
| [Brain Tumor Dataset (figshare)](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427) | MRI | 2017 | 🟡 MAT | — | ✅ | — | OPEN | 3,064 T1-CE MRI slices from 233 patients |
| [CRL Fetal Brain Atlas](http://crl.med.harvard.edu/research/fetal_brain_atlas/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | — | OPEN | Atlas derived from MRI of 81 healthy fetuses (19-39 GA weeks); per-gestational-week template and label volumes (~weeks 21-38) |
| [HCP Young Adult](https://www.humanconnectome.org/study/hcp-young-adult) | MRI | 2017 | 🟢 NIfTI, CIFTI | — | ✅ | ✅ | REGISTRATION | 1206 subjects |
| [Healthy Brain Network (HBN)](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/) | MRI | 2017 | 🟢 NIfTI, BIDS | — | — | ✅ | DUA | 5,000+ target subjects; thousands of MRI datasets released (8,000+ total participants enrolled) |
| [LGG-1p19qDeletion](https://www.cancerimagingarchive.net/collection/lgg-1p19qdeletion/) | MRI | 2017 | 🟢 DICOM, NIfTI | ✅ | ✅ | ✅ | OPEN | 2.8 GB |
| [M-CRIB](https://github.com/DevelopmentalImagingMCRI/M-CRIB_atlas) | MRI | 2017 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 10 neonates (individual images plus group T1/T2 templates) |
| [Mouse-Astrocytoma](https://www.cancerimagingarchive.net/collection/mouse-astrocytoma/) | MRI | 2017 | 🟢 DICOM | — | — | ✅ | OPEN | 48 mice; 48 studies, 286 series, 37,110 DICOM images (2.2 GB) |
| [WMH Segmentation Challenge](https://wmh.isi.uu.nl/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 60 training subjects |
| [IvyGAP](https://www.cancerimagingarchive.net/collection/ivygap/) | MRI | 2016 | 🟢 DICOM | ✅ | — | ✅ | OPEN | 139.98 GB |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Rhineland Study](https://www.rheinland-studie.de/en/) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | REQUEST | ~20,000-participant target (>10,000 enrolled) |
| [Tromsø Study](https://uit.no/research/tromsostudy) | DXA, MRI | 2016 | 🟢 derived, DICOM | — | — | ✅ | REQUEST | Tens of thousands of participants across seven survey waves (DXA and brain MRI collected in sub-samples) |
| [ALSPAC](http://www.bristol.ac.uk/alspac/researchers/access/) | DXA, MRI | 2015 | 🟢 derived, DICOM, NIfTI | — | — | ✅ | REQUEST | ~14,000 index children (thousands with repeated DXA; ~900 with brain MRI at 18-24y) |
| [Cam-CAN](https://www.cam-can.org/) | MRI | 2015 | 🟢 NIfTI | — | — | ✅ | DUA | ~700 subjects |
| [Heinz Nixdorf Recall / 1000BRAINS](https://imibe.uk-essen.de/recall/) | CT, MRI | 2015 | 🟢 DICOM | — | — | ✅ | REQUEST | ~4,800 base cohort (Recall); ~1,300 in 1000BRAINS MRI sub-study |
| [ISLES 2015-2018](https://zenodo.org/records/17736412) | MRI, CT | 2015 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | ~8.4 GB zipped across the Zenodo versions; ISLES 2015 SISS 28 train / 36 test and SPES 30 train / 20 test; ISLES 2016 30 train (Zenodo folders; paper reports 35) / 19 test; ISLES 2017 43 train / 32 test; ISLES 2018 94 train / 62 test CT perfusion slabs (63 / 40 patients) |
| [Insight 46 (MRC NSHD 1946 birth cohort)](https://www.nshd.mrc.ac.uk/data/) | MRI, PET, DXA | 2015 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~500 imaged participants (Insight 46); ~5,300 in the NSHD birth cohort |
| [LIFE-Adult](https://www.uniklinikum-leipzig.de/einrichtungen/life) | MRI | 2015 | 🟢 DICOM | — | — | ✅ | REQUEST | ~2,600 participants with 3T brain MRI (of ~10,000-participant cohort) |
| [Normal Male Head MRI (Lionheart)](https://zenodo.org/records/16956) | MRI | 2015 | 🟢 DICOM | — | — | ✅ | OPEN | 1 subject (normal male, aged 52); DICOM.zip 4.6 MB |
| [QIN-BRAIN-DSC-MRI](https://www.cancerimagingarchive.net/collection/qin-brain-dsc-mri/) | MRI | 2015 | 🟢 DICOM | — | ✅ | ✅ | DUA | 49 subjects / 52 studies / 349 series / 116,778 images; 30.76 GB |
| [QIN-GBM-Treatment-Response](https://www.cancerimagingarchive.net/collection/qin-gbm-treatment-response/) | MRI | 2015 | 🟢 DICOM | — | — | ✅ | DUA | 54 patients / 106 studies / 1,942 series / 589,314 images; 33.51 GB |
| [REMBRANDT](https://www.cancerimagingarchive.net/collection/rembrandt/) | MRI | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 10.59 GB |
| [TCGA-GBM](https://www.cancerimagingarchive.net/collection/tcga-gbm/) | MRI, CT, X-ray | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 73.51 GB |
| [TCGA-LGG](https://www.cancerimagingarchive.net/collection/tcga-lgg/) | MRI, CT | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 42.92 GB |
| [The Maastricht Study](https://www.demaastrichtstudie.nl/research/data-guidelines) | MRI | 2014 | 🟢 DICOM | — | — | ✅ | REQUEST | ~10,000 participants (deep-phenotyping cohort target) |
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | MRI, DXA | 2014 | 🟢 DICOM, NIfTI, derived phenotypes (TSV) | — | — | ✅ | REQUEST | ~100,000 participants imaged; abdominal MRI-derived phenotypes for 40,000+ |
| [Whitehall II Imaging Sub-study](https://www.dementiasplatform.uk/) | MRI | 2014 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~800 participants (brain MRI sub-study of the Whitehall II cohort) |
| [Tohoku Medical Megabank (TMM)](https://www.megabank.tohoku.ac.jp/english/) | MRI | 2013 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | DUA | ~150,000 total cohort participants (CommCohort ~80,000; BirThree ~70,000); brain-MRI sub-study on a subset |
| [ABIDE](https://fcon_1000.projects.nitrc.org/indi/abide/) | MRI | 2012 | 🟢 NIfTI | — | — | ✅ | REGISTRATION | 1112 subjects (ABIDE I) |
| [Mindboggle-101](https://mindboggle.info/data.html) | MRI | 2012 | 🟢 NIfTI, VTK | — | ✅ | — | OPEN | 101 subjects |
| [Neonatal Brain Atlases (ALBERTs / Gousias)](https://brain-development.org/brain-atlases/neonatal-brain-atlases/) | MRI | 2012 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 20 neonates, 50 labeled regions each (with corresponding T1/T2 MRI scans) |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [ADHD-200](https://fcon_1000.projects.nitrc.org/indi/adhd200/) | MRI | 2011 | 🟢 NIfTI | — | — | ✅ | OPEN | 973 subjects (8 sites) |
| [AGES-Reykjavik](https://hjarta.is/en/research/ages/) | MRI, CT | 2011 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~5,764 participants (baseline); brain MRI in most, thigh/abdomen QCT in sub-samples |
| [AIBL](https://aibl.org.au/) | MRI, PET | 2011 | 🟢 DICOM, NIfTI | — | — | ✅ | DUA | — |
| [PPMI](https://www.ppmi-info.org/) | MRI, PET | 2011 | 🟢 DICOM, NIfTI | — | — | ✅ | DUA | — |
| [RIDER-NEURO-MRI](https://www.cancerimagingarchive.net/collection/rider-neuro-mri/) | MRI | 2011 | 🟢 DICOM | — | — | ✅ | DUA | 19 patients / 108 studies / 368 series / 70,220 images (7.79 GB) |
| [IMAGEN](https://imagen-project.org/the-imagen-dataset/) | MRI | 2010 | 🟢 NIfTI, DICOM | — | ✅ | ✅ | DUA | ~2,000 adolescents recruited at age 14 across 8 sites in 4 European countries |
| [OASIS-2](https://sites.wustl.edu/oasisbrains/) | MRI | 2010 | 🟢 Analyze, NIfTI | ✅ | — | — | DUA | 150 subjects, 373 imaging sessions |
| [GUSTO](https://www.gusto.sg/) | MRI, DXA, CT | 2009 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~1,200 mother-offspring pairs |
| [DIAN (Dominantly Inherited Alzheimer Network)](https://dian.wustl.edu/) | MRI, PET | 2008 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~500+ participants from autosomal-dominant Alzheimer's disease families |
| [HCHS/SOL](https://sites9.cscc.unc.edu/hchs/) | MRI | 2008 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | 16,415 participants |
| [NEO Study](https://www.lumc.nl/en/afdelingen/Clinical-Epidemiology/obesity--related-diseases/) | MRI | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | 6,671 participants |
| [Lothian Birth Cohorts (1936/1921)](https://lothian-birth-cohorts.ed.ac.uk/data-access-collaboration) | MRI | 2007 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | LBC1936 ~1,091 (born 1936); LBC1921 ~550 (born 1921), with brain MRI from age ~73/78 |
| [OASIS-1](https://sites.wustl.edu/oasisbrains/) | MRI | 2007 | 🟢 NIfTI, Analyze | — | ✅ | — | DUA | 416 subjects |
| [Rotterdam Study](https://www.ergo-onderzoek.nl) | MRI, DXA | 2005 | 🟢 DICOM, derived | — | ✅ | ✅ | REQUEST | ~20,000 participants aged 40+ enrolled overall; ~5,000+ with repeated brain MRI |
| [ADNI](https://adni.loni.usc.edu/) | MRI, PET | 2004 | 🟢 DICOM, NIfTI | — | — | ✅ | REQUEST | 2000+ participants (ADNI 1/GO/2/3/4) |
| [CoLaus \| PsyCoLaus](https://www.colaus-psycolaus.ch/professionals/) | MRI, DXA | 2003 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~6,700 baseline participants; imaging sub-studies (BrainLaus, OsteoLaus) on subsets |
| [Three-City Study (3C)](http://three-city-study.com/) | MRI | 2003 | 🟢 DICOM, derived | — | ✅ | ✅ | REQUEST | ~9,294 participants (~3,442 with baseline brain MRI in the 3C-Dijon substudy) |
| [CARDIA](https://biolincc.nhlbi.nih.gov/studies/cardia/) | CT, MRI, DXA | 2000 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 5,115 participants enrolled (1985-86); imaging performed in subsets or the full cohort across follow-up exams |
| [HUNT Study](https://www.ntnu.edu/hunt/data) | DXA, MRI | 1995 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~250,000 participants across HUNT1-4 since 1984 |
| [BLSA](https://www.blsa.nih.gov/how-apply) | MRI, PET, DXA | 1994 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,000+ active participants with serial imaging (study cohort >3,200 enrolled since 1958) |
| [ROSMAP](https://www.radc.rush.edu/) | MRI | 1994 | 🟢 NIfTI, DICOM, derived | — | — | ✅ | DUA | ~3,600+ enrolled participants; ex vivo MRI on a subset of donated brains |
| [ARIC](https://sites.cscc.unc.edu/aric/) | MRI, PET | 1993 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 15,792 participants enrolled (1987-89); brain MRI in subsets (~1,900 at visit 3 and ~1,900 in ARIC-NCS) and amyloid PET in a smaller subset (ARIC-PET) |
| [CHS](https://chs-nhlbi.org/) | MRI | 1991 | 🟡 derived | ✅ | — | ✅ | DUA | 5,888 older-adult participants enrolled (1989-90, 1992-93); cranial MRI in ~3,600 (1991-94) with a repeat scan in ~2,900 (1997-99) |
| [Raine Study](https://rainestudy.org.au/) | MRI, DXA | 1989 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | DUA | ~2,900 Gen2 offspring (born 1989-1991) plus Gen1 parents and Gen3 grandchildren |
| [Dunedin Study](https://dunedinstudy.otago.ac.nz/) | MRI | 1972 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 1,037 birth cohort (born 1972-73); ~875 completed brain MRI at age 45 |
| [BrainMetShare](https://aimi.stanford.edu/datasets/brainmetshare) | MRI | — | 🟡 2D image slices (file type not stated) | — | ✅ | ✅ | REGISTRATION | 156 patients (105 labeled training / 51 unlabeled test); 1,517 annotated metastases in the 105 training scans |
| [IXI](https://brain-development.org/ixi-dataset/) | MRI | — | 🟢 NIfTI | — | — | ✅ | OPEN | ~600 healthy subjects |
| [Infant 3T/7T Precision Imaging](https://registry.opendata.aws/infant-3t-7t-precision-mri/) | MRI | — | 🟢 BIDS | — | — | — | OPEN | 6 highly sampled infant participants |
| [LAION-fMRI](https://registry.opendata.aws/laion-fmri/) | MRI | — | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | 5 participants; 165 sessions (165 hours) of 7T fMRI; >25,000 unique natural images viewed |
| [NYUMets Brain](https://registry.opendata.aws/nyumets-brain/) | MRI | — | 🟢 NIfTI, CSV | — | ✅ | — | REQUEST | 8,000+ brain MRIs / 2,000+ patients |
| [UCSF-BMSR](https://imagingdatasets.ucsf.edu/dataset/1) | MRI | — | 🟢 NIfTI | — | ✅ | ✅ | DUA | 560 brain MRIs / 412 patients; 5136 annotated brain metastases |
| [UCSF-PCNSL](https://registry.opendata.aws/ucsf-pcnsl/) | MRI | — | 🟢 BIDS | ✅ | ✅ | ✅ | REQUEST | 150 patients |

### 🫁 Chest & Thorax  <sub>(186)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [BDCXR-3257](https://figshare.com/articles/dataset/_b_BDCXR-3257_b_A_Comprehensive_Chest_Radiography_Dataset_with_Multi-Etiological_Pneumonia_Labels_from_a_Clinical_Setting/32086362) | X-ray | 2026 | 🟡 JPEG | — | — | — | OPEN | 3,257 chest X-ray images (880.2 MB zip) |
| [BSTT_CT](https://zenodo.org/records/18862454) | CT | 2026 | 🟢 MHD/RAW, NRRD, CSV, NumPy | — | ✅ | — | OPEN | 61 CT series / 59 patients; 779 annotated nodules; ~6.9 GB |
| [CBCT-IQ](https://zenodo.org/records/20124496) | CT | 2026 | 🟢 NIfTI, CSV | — | — | — | OPEN | 36 reconstructed CBCT volumes, 1,764 selected image slices from 2 anthropomorphic phantoms (~790 MB) |
| [CMB-GEC](https://www.cancerimagingarchive.net/collection/cmb-gec/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 36.37 GB total (22.13 GB radiology); ~12 open-access radiology subjects, 251 series, 38,709 images |
| [CMB-LCA](https://www.cancerimagingarchive.net/collection/cmb-lca/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 421.59 GB total (191.92 GB radiology); 209 subjects |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [CONFLUX Chest-CT](https://huggingface.co/datasets/gevaertlab/conflux-chest-ct) | CT | 2026 | 🟢 NIfTI, CSV | — | — | — | REGISTRATION | 200,000 synthetic 3D chest CT volumes (216x176x200, 1.5 mm isotropic); 1.84 TB |
| [CT-PEGCT-Diag](https://doi.org/10.57760/sciencedb.37604) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 642 non-enhanced CT scans / 642 pediatric patients |
| [CT-RATE-Refined](https://huggingface.co/datasets/YYama0/CT-RATE-Refined) 🏷 | CT | 2026 | 🟡 CSV | — | — | — | OPEN | Labels for all CT-RATE train/validation volumes (24,446 unique reports after deduplication); 100-report development reference set; 250-report confirmatory radiologist reference set |
| [CT-SpatialVQA](https://huggingface.co/datasets/Mashrafi2827/CT-SpatialVQA) 🏷 | CT | 2026 | 🟡 JSON | ✅ | — | — | OPEN | 9,077 QA pairs on 1,601 CT volumes (CT-RATE validation split) |
| [CT2XR Projections](https://huggingface.co/datasets/qureaiorg/ct2xr-projections) | X-ray | 2026 | 🟡 PNG, Parquet | — | — | — | OPEN | 22,124 synthetic PA radiographs (each with 4 aligned 512x512 images) from 22,124 CT-RATE volumes / 14,538 patients; ~7.9 GB |
| [CancerVerse](https://huggingface.co/datasets/BodyMaps/CancerVerse) | CT | 2026 | 🟢 NIfTI, CSV | ✅ | — | ✅ | REGISTRATION | 24,168 CT volumes from 13,863 patients (staged release; stage 1: 22,865 volumes with reports) |
| [CheXmask-U](https://physionet.org/content/chexmask-u/1.0.0/) 🏷 | X-ray | 2026 | 🟡 CSV | — | ✅ | — | OPEN | Annotations for 657,566 chest X-rays (112,120 ChestX-ray8; 187,825 CheXpert; 243,334 MIMIC-CXR-JPG; 96,287 PadChest; 18,000 VinDr-CXR); 39.9 GB uncompressed |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [Lunguage](https://physionet.org/content/lunguage/1.0.0/) 🏷 | X-ray | 2026 | 🟡 — | ✅ | — | — | DUA | 1,473 chest X-ray reports from 230 patients (MIMIC-CXR official test split); sequential subset of 80 reports from 10 patients |
| [REVEAL-CXR](https://mira.rsna.org/dataset/10) | X-ray | 2026 | 🟢 DICOM | — | — | — | REGISTRATION | 200 chest radiograph studies (100 released + 100 holdout retained by RSNA); 12 labels |
| [TAIX-Ray](https://huggingface.co/datasets/TLAIM/TAIX-Ray) | X-ray | 2026 | 🟡 Parquet, PNG | — | — | — | OPEN | ~215,000 chest radiographs (138k train / 42.9k test / 34.9k validation) from ICU patients |
| [TAM-ARa Phantom CT/CBCT](https://zenodo.org/records/18927128) | CT | 2026 | 🟢 DICOM | — | — | — | OPEN | 3 acquisitions (CT supine, CBCT supine, CBCT upright); ~65 MB |
| [BPD-Neo](https://zenodo.org/records/15768091) | MRI | 2025 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | OPEN | 40 neonates (18 M / 22 F); BPD-Neo-data.zip 224.4 MB |
| [CIED-CXR](https://physionet.org/content/cardiac-implantable-device-cxr/1.0.0/) | X-ray | 2025 | 🟡 PNG | — | ✅ | — | DUA | 13,393 images: 2,321 chest radiographs + 11,072 smartphone photos of them / 896 patients |
| [CT-RATE Generated Scans](https://huggingface.co/datasets/dmolino/CT-RATE_Generated_Scans) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | 1,000 synthetic 3D chest CT volumes |
| [CT-RATE-Thinking](https://huggingface.co/datasets/AlpachinoNLP/CT-RATE-Thinking) 🏷 | CT | 2025 | 🟡 JSONL | ✅ | — | — | OPEN | English VQA: 634,652 train + 31,353 val; Chinese VQA: 626,437 train + 31,353 val; report-level thinking: 39,778 train + 2,169 val records per language |
| [CT-ScanGaze](https://huggingface.co/datasets/phamtrongthang/CT-ScanGaze) | CT | 2025 | 🟢 NIfTI | ✅ | — | — | OPEN | 1045 CT volumes |
| [CT4Harmonization-Multicentric](https://www.cancerimagingarchive.net/collection/ct4harmonization-multicentric/) | CT | 2025 | 🟢 DICOM | — | ✅ | — | OPEN | 1 physical phantom; 1,378 CT series from 649 scans on 13 scanners (8 institutions); TCIA lists 1,378 studies, 2,756 series, 467,224 images; 252.38 GB |
| [CXR-Align](https://physionet.org/content/cxr-align/1.0.0/) 🏷 | X-ray | 2025 | 🟡 JSON | ✅ | — | — | DUA | — |
| [CXReasonBench / CheXStruct](https://physionet.org/content/chexstruct-cxreasonbench/) 🏷 | X-ray | 2025 | 🟡 CSV, JSON | ✅ | — | — | DUA | CheXStruct: 51,095-184,169 MIMIC-CXR-JPG cases per task (12 tasks, after QC); CXReasonBench: 1,200 cases (100 per task), 18,988 QA pairs |
| [Dynamic Thorax Phantom 4DCT/CBCT](https://zenodo.org/records/17256015) | CT | 2025 | 🟢 DICOM | — | — | — | OPEN | DICOM.zip 731.2 MB, processed.zip 821.5 MB, breathing_curves.zip 4.7 MB (number of scans not stated) |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [HiPaS](https://zenodo.org/records/14879605) | CT | 2025 | 🟡 NPZ | — | ✅ | — | OPEN | ~250 chest CT scans (ct_scan.zip 24 GB) |
| [LATTE-CXR](https://physionet.org/content/latte-cxr/1.0.0/) 🏷 | X-ray | 2025 | 🟡 CSV | ✅ | — | — | DUA | 3,926 bounding box–statement pairs from 1,668 readings; 13,751 eye-tracking bounding box–sentence pairs from 2,742 readings (REFLACX phases 2 and 3) |
| [LUNA25](https://luna25.grand-challenge.org/) | CT | 2025 | 🟢 MHA | — | — | — | REGISTRATION | Over 4,000 annotated low-dose chest CT exams for development, 468 hidden test cases, 300 reader-study cases |
| [MIMIC-Ext-CXR-QBA](https://physionet.org/content/mimic-ext-cxr-qba/) 🏷 | X-ray | 2025 | 🟡 — | ✅ | — | — | DUA | 42,172,827 QA pairs (31,230,906 selected for pre-training, 7,532,281 of these for fine-tuning) plus per-study scene graphs, built from 227,827 reports / 377,110 CXRs of MIMIC-CXR |
| [MedVH](https://physionet.org/content/medvh/1.0.0/) | X-ray, CT, MRI | 2025 | 🟡 JPEG, JSON | ✅ | — | — | DUA | 5 MC-VQA hallucination tasks (500 questions each for Wrongful Image, None Of The Above, False Confidence Justification, Abnormality Detection and Clinically Incorrect Question) plus 200 MIMIC-CXR report-generation samples, with matching baseline test sets |
| [Medical-CXR-VQA](https://physionet.org/content/medical-cxr-vqa-dataset/1.0.0/) 🏷 | X-ray | 2025 | 🟡 CSV, JSON | ✅ | — | — | DUA | 780,014 question-answer pairs from 215,547 MIMIC-CXR studies (AP/PA views only) |
| [NTM/TB Mycobacterial CT](https://doi.org/10.34740/kaggle/ds/6248246) | CT | 2025 | 🟢 DICOM, NIfTI, CSV | — | ✅ | — | OPEN | 1,301 patients (430 NTM, 871 TB) chest CT; lesion annotations for 240 patients |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [RadVLM Instruction Dataset](https://physionet.org/content/radvlm-instruction-dataset/1.0.0/) 🏷 | X-ray | 2025 | 🟡 JSON | ✅ | — | — | DUA | 719,675 image–instruction instances (PhysioNet release; full RadVLM set 1,115,021 incl. CheXpert/PadChest-derived data not released) |
| [ReXGradient-160K](https://huggingface.co/datasets/rajpurkarlab/ReXGradient-160K) | X-ray | 2025 | 🟡 PNG, CSV | ✅ | — | — | REGISTRATION | 273,004 images from 160,000 studies of 109,487 patients across 79 sites (3 U.S. health systems) |
| [ReXGroundingCT](https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 3,142 non-contrast chest CT scans; 8,028 text-to-segmentation pairs; 16,301 annotated entities |
| [Symile-MIMIC](https://physionet.org/content/symile-mimic/1.0.0/) | X-ray | 2025 | 🟡 CSV, NPY | — | — | — | DUA | 11,622 admissions / 9,573 patients (one CXR, one ECG and up to 50 blood labs per admission) |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [TrackRAD2025](https://trackrad2025.grand-challenge.org/) | MRI | 2025 | 🟢 MHA | — | ✅ | — | REGISTRATION | 585 patients (108 with manual tumor segmentations, 477 unlabeled) from 6 international MRI-linac centers |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [Aortic Dissection (Graz)](https://doi.org/10.6084/m9.figshare.22269091) | CT | 2024 | 🟢 NRRD, STL | — | ✅ | — | OPEN | 40 CTA volumes / 40 patients |
| [BAMF AIMI Annotations](https://zenodo.org/records/13244892) 🏷 | CT, MRI, PET | 2024 | 🟡 DICOM-SEG, CSV | — | ✅ | — | OPEN | 11 task archives (~650 MB total) of AI segmentations for IDC collections; ~10% of predictions reviewed/corrected |
| [CDSL](https://physionet.org/content/covid-data-shared-learning/1.0.0/) | X-ray, CT | 2024 | 🟡 JPG, CSV | — | — | — | REQUEST | 1,444,764 JPG images (4,608 X-rays; 1,440,156 CT images) from 1,859 patients; structured EHR for 4,479 hospitalized patients |
| [CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 25,692 CT volumes (50,188 with reconstructions) from 21,304 patients; ~21.3 TB |
| [CheXchoNet](https://physionet.org/content/chexchonet/1.0.0/) | X-ray | 2024 | 🟡 JPEG, CSV | — | — | — | DUA | 71,589 PA chest X-rays / 24,689 patients |
| [CheXpert Plus](https://huggingface.co/datasets/StanfordAIMI/CheXpert-Plus) | X-ray | 2024 | 🟢 DICOM, PNG | ✅ | — | — | DUA | 223,228 chest radiographs paired with 187,711 radiology reports from 64,725 patients |
| [DLCSD24](https://zenodo.org/records/13799069) | CT | 2024 | 🟡 — | — | — | — | REQUEST | 1,613 CT volumes with 2,487 annotated nodules (selected from 2,061 patients) |
| [DRR-RATE](https://huggingface.co/datasets/farrell236/DRR-RATE) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | OPEN | 50,188 digitally reconstructed radiographs (~8 GB) |
| [EHRXQA](https://physionet.org/content/ehrxqa/1.0.0/) 🏷 | X-ray | 2024 | 🟡 — | ✅ | — | — | DUA | 46,152 QA samples from 417 templates (16,366 image-related, 16,529 table-related, 13,257 image+table); silver database 800 patients, gold database 400 patients |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MedMNIST+](https://zenodo.org/records/10519652) | X-ray, CT | 2024 | 🟡 NPZ | — | — | — | OPEN | ~708K 2D images and ~10K 3D images across 18 datasets (12 2D, 6 3D); sizes 28/64/128/224 px (2D) and 28/64 voxels (3D) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [PadChest-GR](https://bimcv.cipf.es/bimcv-projects/padchest-gr/) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | DUA | 4,555 CXR studies (3,099 abnormal, 1,456 normal); 7,037 positive and 3,422 negative finding sentences; ~46 GB |
| [RaDialog Instruct Dataset](https://physionet.org/content/radialog-instruct-dataset/) 🏷 | X-ray | 2024 | 🟡 JSON | ✅ | — | — | DUA | — |
| [RadGenome-ChestCT](https://huggingface.co/datasets/RadGenome/RadGenome-ChestCT) | CT | 2024 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 25,692 CT volumes with 665K grounded report regions + 1.3M VQA |
| [VAREPOP-APOLLO](https://www.cancerimagingarchive.net/collection/varepop-apollo/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM | — | — | — | OPEN | 41 subjects, 279 studies, 1,549 series, 235,421 images (129.1 GB), version 3 |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [AIIB23](https://codalab.lisn.upsaclay.fr/competitions/13238) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | — |
| [AeroPath](https://github.com/raidionics/AeroPath) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 27 CT scans (~5 GB) |
| [CXLSeg](https://physionet.org/content/chest-x-ray-segmentation/1.0.0/) | X-ray | 2023 | 🟡 JPEG, CSV | ✅ | ✅ | — | DUA | 243,324 frontal chest X-ray images (segmented image + lung mask, 224x224 JPEG) |
| [CXR-LT](https://physionet.org/content/cxr-lt-iccv-workshop-cvamd/) 🏷 | X-ray | 2023 | 🟡 CSV | — | — | — | DUA | Labels for 377,110 MIMIC-CXR-JPG images: 26 findings (2023) / 45 findings (2024); 406-report manually annotated gold-standard subset |
| [CheXmask](https://physionet.org/content/chexmask-cxr-segmentation-data/) 🏷 | X-ray | 2023 | 🟡 CSV | — | ✅ | — | OPEN | 676,803 anatomical segmentation masks (v0.1) across 6 chest X-ray datasets; 37.7 GB uncompressed (v0.1) |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [INSPECT](https://inspect.stanford.edu/) | CT | 2023 | 🟢 DICOM | ✅ | — | — | DUA | 23,248 CTPA studies / 19,402 patients with reports and EHR |
| [LNQ2023](https://lnq2023.grand-challenge.org/) | CT | 2023 | 🟢 DICOM, NRRD, NIfTI | — | ✅ | — | REGISTRATION | 513 subjects (~35 GB) on TCIA |
| [MAIDA](https://maida.stanford.edu/) | X-ray | 2023 | 🟢 DICOM, PNG | ✅ | — | — | REGISTRATION | multi-institution chest X-rays across 22+ hospitals in 12 countries |
| [MIMIC-Eye](https://physionet.org/content/mimic-eye-multimodal-datasets/1.0.0/) | X-ray | 2023 | 🟡 — | ✅ | — | — | DUA | 3,689 chest X-ray images / 3,192 patients / 1,644 ED stays |
| [MS-CXR-T](https://physionet.org/content/ms-cxr-t/1.0.0/) 🏷 | X-ray | 2023 | 🟡 CSV | ✅ | — | — | DUA | 1,326 frontal chest X-ray image pairs (800 subjects) with progression labels; 361 sentence pairs |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/) | X-ray | 2023 | 🟡 JPG | ✅ | — | — | DUA | 700,703 QA pairs over 164,324 image pairs |
| [RIDER Pilot](https://www.cancerimagingarchive.net/collection/rider-pilot/) | CT, X-ray | 2023 | 🟢 DICOM | — | — | — | OPEN | 8 subjects / 54 studies / 194 series / 20,531 images (11.22 GB) |
| [ReFiSco](https://physionet.org/content/refisco/1.0/) 🏷 | X-ray | 2023 | 🟡 CSV | ✅ | — | — | DUA | 60 MIMIC-CXR studies (single frontal view); 3 report sources; annotations by 4 radiologists |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SPR X-Ray Age Prediction](https://www.kaggle.com/competitions/spr-x-ray-age) | X-ray | 2023 | 🟡 PNG | — | — | — | REGISTRATION | 11,747 chest radiographs (~10.7K train / ~1.1K test) |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [ATM'22](https://atm22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 500 chest CT scans |
| [BRAX](https://physionet.org/content/brax/) | X-ray | 2022 | 🟢 DICOM, PNG | — | — | — | DUA | 40,967 images / 19,351 patients |
| [CT-vs-PET-Ventilation-Imaging](https://www.cancerimagingarchive.net/collection/ct-vs-pet-ventilation-imaging/) | CT, PET | 2022 | 🟢 DICOM, XLSX | — | — | ✅ | OPEN | 20 patients / 22 studies / 119 series / 29,491 images (14.93 GB) |
| [CheXlocalize](https://github.com/rajpurkarlab/cheXlocalize) | X-ray | 2022 | 🟡 JPG, JSON | — | ✅ | — | REGISTRATION | 234 validation images (200 patients) and 668 test images (500 patients) |
| [MELA](https://mela.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | — | — | REGISTRATION | 1,100 chest CT scans (770 train / 110 val / 220 test) |
| [MS-CXR](https://physionet.org/content/ms-cxr/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 1,162 image-sentence bounding-box pairs across 8 findings |
| [NODE21](https://node21.grand-challenge.org/) | X-ray, CT | 2022 | 🟢 MHA | — | — | — | OPEN | 4,882 frontal chest radiographs (1,134 with 1,476 nodule bounding boxes; 3,748 nodule-free) plus LUNA16-derived CT nodule patches |
| [REFLACX](https://physionet.org/content/reflacx-xray-localization/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 3,032 eye-tracking + report sessions for 2,616 chest X-rays |
| [VinDr-PCXR](https://physionet.org/content/vindr-pcxr/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 9,125 studies (children under 10) |
| [AHEP0731](https://www.cancerimagingarchive.net/collection/ahep0731/) | CT, MRI, PET, X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 190 subjects / 855 studies / 5,704 series / 417,972 images (220.94 GB; includes ultrasound) |
| [CANDID-PTX](https://figshare.com/articles/dataset/CANDID-PTX/14173982) | X-ray | 2021 | 🟢 DICOM | ✅ | ✅ | — | REQUEST | 19,237 adult chest X-rays |
| [COVID-19-NY-SBU](https://www.cancerimagingarchive.net/collection/covid-19-ny-sbu/) | X-ray, CT, MRI, PET | 2021 | 🟢 DICOM, CSV | — | — | — | OPEN | 1,384 patients / 7,361 studies / 17,950 series / 562,376 images; 511.48 GB |
| [COVID-CT-MD](https://github.com/ShahinSHH/COVID-CT-MD) | CT | 2021 | 🟢 DICOM | — | — | — | OPEN | 305 patients (169 COVID-19, 60 CAP, 76 normal); labeled subset of 54 COVID and 25 CAP cases with 4,957 infection-positive and 18,392 infection-negative slices |
| [COVID-CTset](https://github.com/mr7495/COVID-CTset) | CT | 2021 | 🟡 TIFF | — | — | — | OPEN | 63,849 images, 377 patients (95 COVID, 282 normal) |
| [Chest ImaGenome](https://physionet.org/content/chest-imagenome/) | X-ray | 2021 | 🟡 JPG | ✅ | — | — | DUA | 242,072 frontal CXRs with scene graphs |
| [ChestX-Det](https://github.com/Deepwise-AILab/ChestX-Det-Dataset) | X-ray | 2021 | 🟡 PNG, JSON | — | ✅ | — | OPEN | 3,578 chest X-ray images (from NIH ChestX-ray14) |
| [MIDRC-RICORD-1B](https://www.cancerimagingarchive.net/collection/midrc-ricord-1b/) | CT | 2021 | 🟢 DICOM, XLSX | — | — | — | OPEN | 120 thoracic CT studies / 117 patients (120 series, 21,220 images); 8.67 GB |
| [MIDRC-RICORD-1C](https://www.cancerimagingarchive.net/collection/midrc-ricord-1c/) | X-ray | 2021 | 🟢 DICOM, JSON | — | — | — | OPEN | 998 chest X-ray studies / 361 patients (1,241 series, 1,257 images); 12.27 GB |
| [RadGraph](https://physionet.org/content/radgraph/1.0.0/) 🏷 | X-ray | 2021 | 🟡 JSON | ✅ | — | — | DUA | 600 radiologist-annotated reports (500 MIMIC-CXR train/dev + 100 test: 50 MIMIC-CXR, 50 CheXpert); model-generated graphs for 220,763 MIMIC-CXR and 500 CheXpert reports |
| [RibSeg](https://github.com/HINTLab/RibSeg) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 490 CT scans, 11,719 ribs (320 train / 50 dev / 120 test) |
| [SIIM-FISABIO-RSNA COVID-19](https://www.kaggle.com/c/siim-covid19-detection) | X-ray | 2021 | 🟢 DICOM, CSV | — | — | — | REGISTRATION | ~6,334 chest radiographs (training) |
| [STOIC2021](https://stoic2021.grand-challenge.org/) | CT | 2021 | 🟢 MHA | — | — | — | REGISTRATION | 2,000 public training CT scans (from a 10,735-patient cohort) |
| [VinDr-CXR](https://physionet.org/content/vindr-cxr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 18,000 images (15,000 train / 3,000 test) |
| [psCBCT AAPM Thoracic](https://zenodo.org/records/5035494) | CT | 2021 | 🟡 — | — | ✅ | — | OPEN | Train archive 16.1 GB + test archive 4.3 GB; each planning CT/OAR case augmented into 23 paired CT/psCBCT/OAR sets |
| [4D CBCT Phantom Data Set](https://zenodo.org/records/10303690) | CT | 2020 | 🟡 — | — | — | — | OPEN | 6 time-resolved (4D) CBCT scans; 4d_cbct_boosting.zip (5.9 GB) |
| [ACRIN-NSCLC-FDG-PET](https://www.cancerimagingarchive.net/collection/acrin-nsclc-fdg-pet/) | PET, CT | 2020 | 🟢 DICOM | ✅ | ✅ | — | OPEN | 145.5 GB |
| [BIMCV-COVID19](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/) | X-ray, CT | 2020 | 🟢 PNG, DICOM | ✅ | ✅ | — | REGISTRATION | 21,342 CR + 34,829 DX studies + 7,918 CT (positive partition) |
| [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) | X-ray | 2020 | 🟡 PNG | — | ✅ | — | REGISTRATION | 21,165 images (4 classes) |
| [COVID-19-AR](https://www.cancerimagingarchive.net/collection/covid-19-ar/) | CT, X-ray | 2020 | 🟢 DICOM, XLSX | ✅ | — | — | OPEN | 105 patients, 256 studies, 461 series, 31,935 images (19.93 GB) |
| [COVID-19-CT-Seg](https://zenodo.org/records/3757476) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 20 labeled CT scans |
| [COVIDx CXR](https://github.com/lindawangg/COVID-Net) | X-ray | 2020 | 🟡 PNG | — | — | — | REGISTRATION | COVIDx CXR-3: ~29,986 images / 16,648 patients |
| [CT-IMAGES-IN-COVID-19](https://www.cancerimagingarchive.net/collection/ct-images-in-covid-19/) | CT | 2020 | 🟢 NIfTI | — | — | — | OPEN | 661 subjects; 14.71 GB (first dataset: 632 patients / 650 CTs; second dataset: 121 serial CTs from 29 patients) |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [CXR-Phone](https://physionet.org/content/cxr-phone/1.0.0/) | X-ray | 2020 | 🟡 JPEG, CSV | — | — | — | DUA | 6,453 smartphone photographs of frontal CXRs in 4 subsets (Photo-MMC 1,759; Photo-CXP 1,337; Photo-MED 1,337; Photo-DEV 2,020) |
| [EGD-CXR](https://physionet.org/content/egd-cxr/1.0.0/) 🏷 | X-ray | 2020 | 🟡 CSV, JSON, WAV, MP3, PNG | ✅ | ✅ | — | DUA | 1,083 MIMIC-CXR images / 1,038 subjects (images obtained separately from MIMIC-CXR) |
| [LDCT-and-Projection-data](https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/) | CT | 2020 | 🟢 DICOM, DICOM-CT-PD | — | — | — | OPEN | 299 patient exams + 1 phantom: chest 99 (256.81 GB), liver/abdomen 100 (604.12 GB), head 99 (462.77 GB, restricted) |
| [Lung-PET-CT-Dx](https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/) | CT, PET | 2020 | 🟢 DICOM | — | — | ✅ | OPEN | 355 patients / 251,135 DICOM images |
| [MedSeg COVID-19 CT Segmentation](https://www.medseg.ai/covid-19) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 100 axial CT slices (~40 patients) plus 9 CT volumes (~829 slices) |
| [MosMedData](https://academictorrents.com/details/f2175c4676e041ea65568bb70c2bcd15c7325fd2) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,110 CT studies (~50 with masks) |
| [Object-CXR](https://github.com/hlk-1135/object-CXR) | X-ray | 2020 | 🟡 JPEG | — | — | — | OPEN | 10,000 frontal X-rays (5,000 with foreign objects) |
| [PDMR-292921-168-R](https://www.cancerimagingarchive.net/collection/pdmr-292921-168-r/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 19 subjects (mice), 86 studies, 154 series, 2,546 images; 1.56 GB |
| [PDMR-425362-245-T](https://www.cancerimagingarchive.net/collection/pdmr-425362-245-t/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 20 mice / 115 studies / 210 series / 3,509 images (2.35 GB) |
| [PDMR-997537-175-T](https://www.cancerimagingarchive.net/collection/pdmr-997537-175-t/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 24 mice / 76 studies / 128 series / 1,966 images; 1.18 GB |
| [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) | X-ray | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 160,868 images / 67,625 patients |
| [RAD-ChestCT](https://zenodo.org/records/6406114) | CT | 2020 | 🟡 NPZ | ✅ | — | — | REQUEST | 3,630 chest CT volumes released on Zenodo (initial ~10% release of 35,747 scans from 19,661 adult patients) |
| [RSNA-STR Pulmonary Embolism CT](https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection) | CT | 2020 | 🟢 DICOM | — | — | — | REGISTRATION | 7,279 CTPA studies (public training set) |
| [RibFrac](https://ribfrac.grand-challenge.org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 660 CT scans (~5,000 fractures); 420 train, 80 val, 160 test |
| [TBX11K](https://mmcheng.net/tb/) | X-ray | 2020 | 🟡 PNG, XML, JSON | — | — | — | OPEN | 11,200 chest X-ray images at 512x512 |
| [Anti-PD-1_Lung](https://www.cancerimagingarchive.net/collection/anti-pd-1_lung/) | PET, CT | 2019 | 🟢 DICOM | ✅ | ✅ | — | REGISTRATION | 61 GB |
| [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) | X-ray | 2019 | 🟡 JPEG | — | — | — | REGISTRATION | 224,316 radiographs / 65,240 patients |
| [Crowds-Cure-2018](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2018/) 🏷 | CT | 2019 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | 4,756 bi-directional lesion measurements on CT scans of 324 patients from 13 TCIA collections; label files 5.76 MB |
| [LNDb](https://lndb.grand-challenge.org/) | CT | 2019 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | REGISTRATION | 294 CT scans |
| [LoDoPaB-CT](https://zenodo.org/records/3384092) | CT | 2019 | 🟡 HDF5 | — | — | — | OPEN | 42,895 slice pairs (train 35,820 / validation 3,522 / test 3,553) from 752 patients; ~51 GB |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/) | X-ray | 2019 | 🟢 DICOM | ✅ | — | — | DUA | 377,110 images / 227,835 studies / ~65,379 patients |
| [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/) | X-ray | 2019 | 🟡 JPEG | — | — | — | DUA | 377,110 JPG images / 227,827 studies |
| [NIH CXR14 Google Expert Labels](https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest) 🏷 | X-ray | 2019 | 🟡 CSV | — | — | — | REGISTRATION | Four findings: 4,374 images (2,412 validation + 1,962 test); all findings: 810 PA test images x 5 readers |
| [SIIM-ACR Pneumothorax](https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation) | X-ray | 2019 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~12,047 train + ~3,205 test |
| [SegTHOR](https://competitions.codalab.org/competitions/21145) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 60 CT scans (40 train / 20 test) |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Four tasks; 50 training CT scans (+10 test) each for head-neck and chest cohorts |
| [CPTAC-LSCC](https://www.cancerimagingarchive.net/collection/cptac-lscc/) | CT, PET | 2018 | 🟢 DICOM | — | — | — | OPEN | Radiology: 36 subjects, 43 studies, 233 series, ~51,000 images (30.06 GB) CT/PT, plus 1 restricted head CT subject; pathology: 1,081 whole-slide images from 212 subjects (414 GB) |
| [CPTAC-LUAD](https://www.cancerimagingarchive.net/collection/cptac-luad/) | CT, PET, MRI | 2018 | 🟢 DICOM, SVS | — | — | — | OPEN | Radiology: 38 subjects / 75 studies / 448 series / 72,555 images (45.32 GB); pathology: 1,137 whole-slide images from 243 subjects (431.5 GB) |
| [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) | X-ray | 2018 | 🟡 JPEG | — | — | — | OPEN | 5,856 chest radiographs |
| [Crowds-Cure-2017](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2017/) 🏷 | CT | 2018 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | Annotations for 352 subjects (source CT: 352 studies, 443 series, 49,211 images, 25.99 GB); annotation files 4.64 MB |
| [FUMPE](https://figshare.com/collections/FUMPE/4107803) | CT | 2018 | 🟢 DICOM, MAT | — | ✅ | — | OPEN | 35 CT pulmonary angiography scans (35 subjects) |
| [Generation R](https://generationr.nl/researchers/) | MRI, DXA | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~several thousand children with repeated brain MRI and DXA (birth cohort of ~9,700 mothers/children) |
| [Lung-Fused-CT-Pathology](https://www.cancerimagingarchive.net/collection/lung-fused-ct-pathology/) | CT | 2018 | 🟢 DICOM, MHA, TIFF, XLSX | — | ✅ | — | OPEN | 6 patients; CT/SEG: 36 studies, 52 series, 11,210 images (5.91 GB); plus 25 annotated whole-slide histology images (21.3 GB); 27.21 GB total |
| [RSNA Pneumonia Detection](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) | X-ray | 2018 | 🟢 DICOM | — | — | — | REGISTRATION | ~26,684 training radiographs |
| [SCAPIS](https://www.scapis.org/data-access/) | CT | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~30,000 participants |
| [TB Portals](https://tbportals.niaid.nih.gov/) | X-ray, CT | 2018 | 🟢 DICOM | ✅ | — | — | DUA | 27,294 chest X-ray and CT imaging studies; 24,752 TB cases; 16 countries, 40 sites |
| [CC-Radiomics-Phantom](https://www.cancerimagingarchive.net/collection/cc-radiomics-phantom/) | CT | 2017 | 🟢 DICOM, DICOM RTSTRUCT | — | ✅ | — | OPEN | 17 CT scans (17 subjects/studies, 51 series, 2,672 images); 1.43 GB |
| [Lifelines (ImaLife)](https://www.lifelines-biobank.com/) | CT | 2017 | 🟢 DICOM | — | — | — | DUA | ~167,000 total cohort; 12,055 low-dose chest CT (ImaLife) |
| [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 112,120 frontal images / 30,805 patients |
| [4D-Lung](https://www.cancerimagingarchive.net/collection/4d-lung/) | CT | 2016 | 🟢 DICOM, RTSTRUCT | — | ✅ | — | OPEN | 20 patients / 589 studies / 6,690 series / 347,330 images (183.04 GB): 82 4D fan-beam CT and 507 4D cone-beam CT images |
| [LUNA16](https://luna16.grand-challenge.org/) | CT | 2016 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | OPEN | 888 CT scans / 1,186 nodule annotations |
| [CT Lymph Nodes](https://www.cancerimagingarchive.net/collection/ct-lymph-nodes/) | CT | 2015 | 🟢 DICOM, DICOM-SEG, NIfTI, TXT, MPS | — | ✅ | — | OPEN | 176 CT scans / 176 patients (90 mediastinal, 86 abdominal); 352 series, 110,179 images; 58.42 GB |
| [NRG-1308](https://www.cancerimagingarchive.net/collection/nrg-1308/) | CT | 2015 | 🟢 DICOM | — | ✅ | — | REQUEST | 12 subjects / 12 studies / 85 series / 1,983 images; 1.68 GB |
| [NSCLC-Radiogenomics](https://www.cancerimagingarchive.net/collection/nsclc-radiogenomics/) | CT, PET | 2015 | 🟢 DICOM, CSV | ✅ | ✅ | ✅ | OPEN | 211 patients (CT and PET/CT; RNA-seq for 130) |
| [Phantom FDA](https://www.cancerimagingarchive.net/collection/phantom-fda/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 7 phantom subjects, 76 studies, 4,433 series, 1,468,751 images (782.22 GB) |
| [QIN LUNG CT](https://www.cancerimagingarchive.net/collection/qin-lung-ct/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 47 subjects / 47 studies / 47 series / 3,954 images; 2.09 GB |
| [SPIE-AAPM Lung CT Challenge (LUNGx)](https://www.cancerimagingarchive.net/collection/spie-aapm-lung-ct-challenge/) | CT | 2015 | 🟢 DICOM, XLSX | — | — | — | OPEN | 70 subjects, 22,489 images (~12 GB) |
| [TCGA-LUSC](https://www.cancerimagingarchive.net/collection/tcga-lusc/) | CT, PET | 2015 | 🟢 DICOM | — | — | — | OPEN | 37 subjects / 74 studies / 279 series / 36,518 images (15.02 GB) |
| [Lung Phantom](https://www.cancerimagingarchive.net/collection/lung-phantom/) | CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 1 phantom, 1 CT series, 237 images (127.5 MB) |
| [LungCT-Diagnosis](https://www.cancerimagingarchive.net/collection/lungct-diagnosis/) | CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 61 patients / 61 CT series / 4,682 images (2.47 GB) |
| [Montgomery County CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | ✅ | — | OPEN | 138 frontal X-rays (80 normal, 58 TB) |
| [NSCLC-Radiomics](https://www.cancerimagingarchive.net/collection/nsclc-radiomics/) | CT | 2014 | 🟢 DICOM, CSV | ✅ | ✅ | — | OPEN | 422 patients (tumor segmentations for 318) |
| [QIN-SARCOMA](https://www.cancerimagingarchive.net/collection/qin-sarcoma/) | MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 15 subjects / 38 studies / 2,168 series / 46,614 images; 10.29 GB |
| [Shenzhen Hospital CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | — | — | OPEN | 662 frontal X-rays (326 normal, 336 TB) |
| [TCGA-ESCA](https://www.cancerimagingarchive.net/collection/tcga-esca/) | CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 16 patients / 17 studies / 126 series / 20,593 CT images (10.94 GB) |
| [TCGA-LUAD](https://www.cancerimagingarchive.net/collection/tcga-luad/) | CT, PET | 2014 | 🟢 DICOM | — | — | — | OPEN | 69 subjects, 152 studies, 624 series, 48,931 images (19.62 GB) |
| [TCGA-SARC](https://www.cancerimagingarchive.net/collection/tcga-sarc/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 5 subjects / 6 studies / 33 series / 5,653 images; 2.8 GB |
| [NLST](https://www.cancerimagingarchive.net/collection/nlst/) | CT | 2013 | 🟢 DICOM | — | — | — | OPEN | 26,254 subjects / 73,116 CT studies |
| [Open-i / Indiana University CXR](https://openi.nlm.nih.gov/) | X-ray | 2013 | 🟢 DICOM, PNG | ✅ | — | — | OPEN | 7,470 images / 3,955 reports |
| [RIDER Lung CT](https://www.cancerimagingarchive.net/collection/rider-lung-ct/) | CT | 2012 | 🟢 DICOM | — | ✅ | — | OPEN | 32 patients / 100 studies / 936 series / 81,548 images (43.01 GB, v3) |
| [LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/) | CT | 2011 | 🟢 DICOM, XML | — | ✅ | — | OPEN | 1,018 CT scans / 1,010 patients |
| [RIDER Lung PET-CT](https://www.cancerimagingarchive.net/collection/rider-lung-pet-ct/) | PET, CT | 2011 | 🟢 DICOM | — | — | — | OPEN | 243 subjects / 274 studies / 1,328 series / 266,280 images; 83.27 GB |
| [EMPIRE10](https://empire10.grand-challenge.org/) | CT | 2010 | 🟢 MetaImage (.mhd/.raw) | — | — | — | REGISTRATION | 30 intra-subject chest CT scan pairs |
| [SPIROMICS](https://www.spiromics.org/spiromics/) | CT | 2010 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 2,982 participants |
| [COPDGene](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000179) | CT | 2007 | 🟢 DICOM, derived | — | — | ✅ | DUA | 10,719 participants (over 40,000 inspiratory/expiratory chest CT scans through Phase 3) |
| [Framingham Heart Study MDCT](https://www.framinghamheartstudy.org/fhs-for-researchers/data-available-overview/) | CT | 2002 | 🟢 DICOM, derived | — | ✅ | — | REQUEST | ~3,500 participants in the MDCT substudy (of >15,000 total FHS cohort) |
| [JSRT](http://db.jsrt.or.jp/eng.php) | X-ray | 2000 | 🟡 IMG | — | — | — | REGISTRATION | 247 posterior-anterior chest radiographs (154 with a lung nodule: 100 malignant, 54 benign; 93 without nodules); 2048x2048, 12-bit, 0.175 mm pixel spacing |
| [MESA](https://biolincc.nhlbi.nih.gov/studies/mesa/) | MRI, CT | 2000 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 6,814 participants |

### 🫀 Cardiac  <sub>(52)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CIED-CXR](https://physionet.org/content/cardiac-implantable-device-cxr/1.0.0/) | X-ray | 2025 | 🟡 PNG | — | ✅ | — | DUA | 13,393 images: 2,321 chest radiographs + 11,072 smartphone photos of them / 896 patients |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [MultiD4CAD](https://zenodo.org/records/15148653) | CT | 2025 | 🟢 DICOM | — | ✅ | — | DUA | 118 patients (40 non-CAD, 78 CAD); ~4.6 TB |
| [CADICA](https://data.mendeley.com/datasets/p9bpx9ctcv) | X-ray | 2024 | 🟡 PNG, XLSX, TXT, MAT | — | — | — | OPEN | 42 patients; invasive coronary angiography videos, frames extracted to 512x512 PNG (1-151 frames per video, ~10 fps) |
| [CMRxRecon2024](https://cmrxrecon.github.io/2024/) | MRI | 2024 | 🟢 MATLAB | — | — | ✅ | REGISTRATION | 330 healthy volunteers (200 training, 60 validation, 70 test) |
| [CheXchoNet](https://physionet.org/content/chexchonet/1.0.0/) | X-ray | 2024 | 🟡 JPEG, CSV | — | — | — | DUA | 71,589 PA chest X-rays / 24,689 patients |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [HVSMR-2.0](https://figshare.com/articles/dataset/HVSMR-2_0_A_3D_cardiovascular_MR_dataset_for_whole-heart_segmentation_in_congenital_heart_disease/25226360) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 60 cardiovascular MR scans |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MBAS 2024](https://zenodo.org/records/19120533) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 100 annotated 3D LGE-MRI scans (70 training + 30 testing) released on Zenodo (~1.5 GB); part of a 200-scan multi-centre challenge cohort |
| [ARCADE](https://arcade.grand-challenge.org/) | X-ray | 2023 | 🟡 PNG, COCO-JSON | — | ✅ | — | OPEN | 1,500 training + 1,500 validation images (segmentation & stenosis tasks) plus 300 test images per task |
| [CMRxRecon](https://cmrxrecon.github.io/) | MRI | 2023 | 🟢 MATLAB (.mat k-space) | — | ✅ | ✅ | REGISTRATION | 300 subjects |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [CMRxMotion](https://www.synapse.org/Synapse:syn28503327) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | ~40 healthy volunteers imaged under 4 respiratory-motion levels |
| [LAScarQS 2022](https://zmiclab.github.io/projects/lascarqs22/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 194 LGE-MRI |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [M&Ms-2](https://www.ub.edu/mnms-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 360 patients |
| [EMIDEC](http://emidec.com/) | MRI | 2020 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 150 cases (50 normal, 100 pathological) |
| [Hamburg City Health Study](https://hchs.hamburg/) | MRI | 2020 | 🟢 DICOM | — | — | ✅ | REQUEST | ~45,000-participant target (>17,000 enrolled) |
| [ImageCHD](https://github.com/XiaoweiXu/ImageCHD-A-3D-Computed-Tomography-Image-Dataset-for-Classification-of-Congenital-Heart-Disease) | CT | 2020 | 🟢 NRRD | — | ✅ | — | REGISTRATION | 110 3D CT images |
| [M&Ms](https://www.ub.edu/mnms/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 375 patients (multi-vendor) |
| [MyoPS 2020](https://zmiclab.github.io/zxh/0/myops20/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 45 patients (25 train + 20 test) |
| [OCMR](https://ocmr.info/) | MRI | 2020 | 🟢 ISMRMRD, HDF5 | — | — | — | OPEN | 165 fully sampled acquisitions (279 slices) and 212 prospectively undersampled acquisitions (842 slices) |
| [MS-CMRSeg 2019](https://zmiclab.github.io/zxh/0/mscmrseg19/) | MRI | 2019 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 45 cardiomyopathy patients (3 sequences each: LGE, T2, bSSFP) |
| [Atria Seg 2018](https://www.cardiacatlas.org/atriaseg2018-challenge/) | MRI | 2018 | 🟢 NRRD | — | ✅ | — | REGISTRATION | 154 3D LGE-MRI (100 train + 54 test) |
| [Generation R](https://generationr.nl/researchers/) | MRI, DXA | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~several thousand children with repeated brain MRI and DXA (birth cohort of ~9,700 mothers/children) |
| [MSD Heart (Task02)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 30 cases (20 train + 10 test) |
| [SCAPIS](https://www.scapis.org/data-access/) | CT | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~30,000 participants |
| [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 150 patients (100 train + 50 test) |
| [Lifelines (ImaLife)](https://www.lifelines-biobank.com/) | CT | 2017 | 🟢 DICOM | — | — | — | DUA | ~167,000 total cohort; 12,055 low-dose chest CT (ImaLife) |
| [MM-WHS](https://zmiclab.github.io/zxh/0/mmwhs/) | CT, MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 120 images (60 CT/CTA + 60 MRI) |
| [HVSMR 2016](http://segchd.csail.mit.edu/) | MRI | 2016 | 🟢 NRRD | — | ✅ | — | OPEN | 20 3D cardiovascular MR images (10 training + 10 test) |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Second Annual Data Science Bowl](https://www.kaggle.com/c/second-annual-data-science-bowl) | MRI | 2016 | 🟢 DICOM | — | — | — | REGISTRATION | ~1,140 patients (cine cardiac MRI studies) |
| [Heinz Nixdorf Recall / 1000BRAINS](https://imibe.uk-essen.de/recall/) | CT, MRI | 2015 | 🟢 DICOM | — | — | ✅ | REQUEST | ~4,800 base cohort (Recall); ~1,300 in 1000BRAINS MRI sub-study |
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | MRI, DXA | 2014 | 🟢 DICOM, NIfTI, derived phenotypes (TSV) | — | — | ✅ | REQUEST | ~100,000 participants imaged; abdominal MRI-derived phenotypes for 40,000+ |
| [CONSTANCES](https://www.constances.fr/espace-scientifique/) | MRI | 2012 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~220,000 participants |
| [RVSC](https://rvsc.projets.litislab.fr/) | MRI | 2012 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 48 patients (16 train + 32 test) |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [AGES-Reykjavik](https://hjarta.is/en/research/ages/) | MRI, CT | 2011 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~5,764 participants (baseline); brain MRI in most, thigh/abdomen QCT in sub-samples |
| [MASALA](https://www.masalastudy.org/for-researchers) | CT | 2010 | 🟢 DICOM, derived | — | ✅ | — | DUA | ~1,164 participants at baseline (expanded in later exams) |
| [Sunnybrook Cardiac Data](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) | MRI | 2009 | 🟢 DICOM | — | ✅ | — | OPEN | 45 patients |
| [ELSA-Brasil](https://estudoelsa.fiocruz.br/) | CT, MRI | 2008 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 15,105 participants |
| [HCHS/SOL](https://sites9.cscc.unc.edu/hchs/) | MRI | 2008 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | 16,415 participants |
| [NEO Study](https://www.lumc.nl/en/afdelingen/Clinical-Epidemiology/obesity--related-diseases/) | MRI | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | 6,671 participants |
| [Jackson Heart Study (JHS)](https://biolincc.nhlbi.nih.gov/studies/jhs/) | MRI, CT | 2004 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | 5,306 participants |
| [Framingham Heart Study MDCT](https://www.framinghamheartstudy.org/fhs-for-researchers/data-available-overview/) | CT | 2002 | 🟢 DICOM, derived | — | ✅ | — | REQUEST | ~3,500 participants in the MDCT substudy (of >15,000 total FHS cohort) |
| [CARDIA](https://biolincc.nhlbi.nih.gov/studies/cardia/) | CT, MRI, DXA | 2000 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 5,115 participants enrolled (1985-86); imaging performed in subsets or the full cohort across follow-up exams |
| [MESA](https://biolincc.nhlbi.nih.gov/studies/mesa/) | MRI, CT | 2000 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 6,814 participants |
| [Coronary Angiography SYNTAX](https://huggingface.co/datasets/MesserMMP/coronary-angiography-syntax) | X-ray | — | 🟢 DICOM, JSON, PDF | ✅ | — | — | OPEN | ~985 GB total; main-cohort DICOM studies plus two holdouts: Philips 97 studies (880 projections) and Siemens 20 studies (187 projections) |

### 🩸 Vascular  <sub>(41)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [HiPaS](https://zenodo.org/records/14879605) | CT | 2025 | 🟡 NPZ | — | ✅ | — | OPEN | ~250 chest CT scans (ct_scan.zip 24 GB) |
| [TopBrain 2025](https://topbrain2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Batches 1-2 on Zenodo: 50 angiographic scans (25 paired CTA/MRA subjects), ~2.0 GB; 40 CTA / 42 MRA vessel labels (34 overlapping) |
| [AortaSeg24](https://aortaseg24.grand-challenge.org/) | CT | 2024 | 🟢 MHA, NIfTI | — | ✅ | — | REGISTRATION | 100 annotated CTA volumes |
| [Aortic Dissection (Graz)](https://doi.org/10.6084/m9.figshare.22269091) | CT | 2024 | 🟢 NRRD, STL | — | ✅ | — | OPEN | 40 CTA volumes / 40 patients |
| [CADICA](https://data.mendeley.com/datasets/p9bpx9ctcv) | X-ray | 2024 | 🟡 PNG, XLSX, TXT, MAT | — | — | — | OPEN | 42 patients; invasive coronary angiography videos, frames extracted to 512x512 PNG (1-151 frames per video, ~10 fps) |
| [COSTA](https://doi.org/10.5281/zenodo.11025761) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REQUEST | 423 TOF-MRA volumes across 8 centers (4 vendors, 1.5T/3.0T) |
| [HVSMR-2.0](https://figshare.com/articles/dataset/HVSMR-2_0_A_3D_cardiovascular_MR_dataset_for_whole-heart_segmentation_in_congenital_heart_disease/25226360) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 60 cardiovascular MR scans |
| [TopCoW 2024](https://topcow24.grand-challenge.org/) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 125 training patients (250 paired CTA+MRA images), plus 10 validation and 70 test pairs |
| [ARCADE](https://arcade.grand-challenge.org/) | X-ray | 2023 | 🟡 PNG, COCO-JSON | — | ✅ | — | OPEN | 1,500 training + 1,500 validation images (segmentation & stenosis tasks) plus 300 test images per task |
| [CAS2023](https://codalab.lisn.upsaclay.fr/competitions/9804) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 TOF-MRA training cases |
| [CMB-AML](https://www.cancerimagingarchive.net/collection/cmb-aml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 448.08 GB, 16 subjects |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [ImageCAS](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REQUEST | 1000 patients |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SMILE-UHURA](https://osf.io/jg7cr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | ~14 annotated training subjects (7T ToF-MRA volumes) plus held-out test set |
| [AVT](https://figshare.com/articles/dataset/Aortic_Vessel_Tree_AVT_CTA_Datasets_and_Segmentations/14806362) | CT | 2022 | 🟢 NRRD | — | ✅ | — | OPEN | 56 aortas (3 collections) |
| [KiPA22](https://kipa22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 130 CTA cases (100 available: 70 training + 30 open test) |
| [Lausanne TOF-MRA Aneurysm Cohort](https://openneuro.org/datasets/ds003949) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 284 subjects (157 aneurysm patients, 127 healthy controls) |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [Parse2022](https://parse2022.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 CTPA volumes (100 train, 30 validation, 70 test) |
| [COCA (Stanford)](https://aimi.stanford.edu/datasets/coca-coronary-calcium-chest-ct) | CT | 2021 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~1000 patients (789 gated + 214 non-gated) |
| [ASOCA](https://asoca.grand-challenge.org/) | CT | 2020 | 🟢 NRRD | — | ✅ | — | DUA | 60 cases (40 train + 20 test) |
| [Hamburg City Health Study](https://hchs.hamburg/) | MRI | 2020 | 🟢 DICOM | — | — | ✅ | REQUEST | ~45,000-participant target (>17,000 enrolled) |
| [FUMPE](https://figshare.com/collections/FUMPE/4107803) | CT | 2018 | 🟢 DICOM, MAT | — | ✅ | — | OPEN | 35 CT pulmonary angiography scans (35 subjects) |
| [SCAPIS](https://www.scapis.org/data-access/) | CT | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~30,000 participants |
| [HVSMR 2016](http://segchd.csail.mit.edu/) | MRI | 2016 | 🟢 NRRD | — | ✅ | — | OPEN | 20 3D cardiovascular MR images (10 training + 10 test) |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Heinz Nixdorf Recall / 1000BRAINS](https://imibe.uk-essen.de/recall/) | CT, MRI | 2015 | 🟢 DICOM | — | — | ✅ | REQUEST | ~4,800 base cohort (Recall); ~1,300 in 1000BRAINS MRI sub-study |
| [LIFE-Adult](https://www.uniklinikum-leipzig.de/einrichtungen/life) | MRI | 2015 | 🟢 DICOM | — | — | ✅ | REQUEST | ~2,600 participants with 3T brain MRI (of ~10,000-participant cohort) |
| [orCaScore](https://orcascore.grand-challenge.org/) | CT | 2014 | 🟢 MHD | — | ✅ | — | REGISTRATION | 72 patients (32 train + 40 test) |
| [Qatar Biobank](https://www.qphi.org.qa/research/how-to-apply) | DXA, Ultrasound | 2012 | 🟡 derived | — | — | — | REQUEST | ~60,000 participants target (DXA and carotid ultrasound on examination subsets) |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [VESSEL12](https://vessel12.grand-challenge.org/) | CT | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 20 chest CT scans |
| [AGES-Reykjavik](https://hjarta.is/en/research/ages/) | MRI, CT | 2011 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~5,764 participants (baseline); brain MRI in most, thigh/abdomen QCT in sub-samples |
| [MASALA](https://www.masalastudy.org/for-researchers) | CT | 2010 | 🟢 DICOM, derived | — | ✅ | — | DUA | ~1,164 participants at baseline (expanded in later exams) |
| [ELSA-Brasil](https://estudoelsa.fiocruz.br/) | CT, MRI | 2008 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 15,105 participants |
| [NEO Study](https://www.lumc.nl/en/afdelingen/Clinical-Epidemiology/obesity--related-diseases/) | MRI | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | 6,671 participants |
| [Jackson Heart Study (JHS)](https://biolincc.nhlbi.nih.gov/studies/jhs/) | MRI, CT | 2004 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | 5,306 participants |
| [MESA](https://biolincc.nhlbi.nih.gov/studies/mesa/) | MRI, CT | 2000 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 6,814 participants |
| [ARIC](https://sites.cscc.unc.edu/aric/) | MRI, PET | 1993 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 15,792 participants enrolled (1987-89); brain MRI in subsets (~1,900 at visit 3 and ~1,900 in ARIC-NCS) and amyloid PET in a smaller subset (ARIC-PET) |
| [Coronary Angiography SYNTAX](https://huggingface.co/datasets/MesserMMP/coronary-angiography-syntax) | X-ray | — | 🟢 DICOM, JSON, PDF | ✅ | — | — | OPEN | ~985 GB total; main-cohort DICOM studies plus two holdouts: Philips 97 studies (880 projections) and Siemens 20 studies (187 projections) |

### 🫃 Abdominal  <sub>(144)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-CRC](https://www.cancerimagingarchive.net/collection/cmb-crc/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 400.75 GB; 102 subjects (v11); 62 radiology patients with 269,002 images |
| [CMB-GEC](https://www.cancerimagingarchive.net/collection/cmb-gec/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 36.37 GB total (22.13 GB radiology); ~12 open-access radiology subjects, 251 series, 38,709 images |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [CMB-OV](https://www.cancerimagingarchive.net/collection/cmb-ov/) | CT, MRI | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 36.99 GB radiology (Version 4); 19 radiology subjects, 71 studies, 554 series, 68,415 images; 162 GB histopathology (48 subjects) |
| [CPTAC-STAD](https://www.cancerimagingarchive.net/collection/cptac-stad/) | CT | 2026 | 🟢 DICOM | — | — | — | OPEN | Radiology: 20 subjects, 22 studies, 99 series, 38,660 DICOM images (CT, US; ~21 GB); whole collection 168 subjects incl. 703 whole-slide images (~1.1 TB) |
| [CT-PEGCT-Diag](https://doi.org/10.57760/sciencedb.37604) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 642 non-enhanced CT scans / 642 pediatric patients |
| [CancerVerse](https://huggingface.co/datasets/BodyMaps/CancerVerse) | CT | 2026 | 🟢 NIfTI, CSV | ✅ | — | ✅ | REGISTRATION | 24,168 CT volumes from 13,863 patients (staged release; stage 1: 22,865 volumes with reports) |
| [DeepTumorVQA v2](https://huggingface.co/datasets/tumor-vqa/DeepTumorVQA_2.0) | CT | 2026 | 🟢 NIfTI, PNG, MP4, JSON, CSV | ✅ | — | — | OPEN | 438K QA pairs: 10,000-question benchmark on 991 CT volumes (NIfTI, ~70 GB) plus 428,050 training QA on 8,334 CTs (CTs linked upstream); 20K+20K agent trajectories |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [Gastric-X](https://huggingface.co/datasets/HaoChen2/Gastric-X) | CT | 2026 | 🟢 NIfTI, JSON, PNG | ✅ | ✅ | ✅ | REGISTRATION | 1,403 patients; 4,897 CT phases (~155 GB) |
| [KUB-StoneX](https://figshare.com/articles/dataset/_b_KUB-StoneX_b_Annotated_Kidney-Ureter-Bladder_X-ray_Dataset_with_Expert_Stone_Segmentations_and_Radiomic_Features/32049369) | X-ray | 2026 | 🟡 — | — | ✅ | — | OPEN | 2,570 AP KUB radiographs / 1,703 patients; 19.3 GB zip |
| [Merlin Plus](https://github.com/MrGiovanni/MerlinPlus) | CT | 2026 | 🟡 NIfTI, CSV | ✅ | ✅ | — | OPEN | 1,193 radiologist-created tumor masks (9 organs) + 44-class AI organ masks for the 25,494 Merlin CT scans (18,317 patients); 3,830 patients with 2+ scans; no images included |
| [SwissPancreas](https://huggingface.co/datasets/AbdomenAtlas/SwissPancreas) | CT | 2026 | 🟡 — | ✅ | — | — | OPEN | 684 CT-report pairs (445 with pancreatic tumors) |
| [TAM-ARa Phantom CT/CBCT](https://zenodo.org/records/18927128) | CT | 2026 | 🟢 DICOM | — | — | — | OPEN | 3 acquisitions (CT supine, CBCT supine, CBCT upright); ~65 MB |
| [AbdomenAtlas 2.0](https://github.com/BodyMaps/AbdomenAtlas2.0) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | OPEN | 10,135 CT scans from 89 hospitals; 15,130 tumor masks; 5,893 control scans (~400 GB) |
| [AbdomenAtlas 3.0](https://github.com/MrGiovanni/RadGPT) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 9,262 CT volumes (3,220 with a contrast-enhanced phase) + reports |
| [CT-ScanGaze](https://huggingface.co/datasets/phamtrongthang/CT-ScanGaze) | CT | 2025 | 🟢 NIfTI | ✅ | — | — | OPEN | 1045 CT volumes |
| [CT4Harmonization-Multicentric](https://www.cancerimagingarchive.net/collection/ct4harmonization-multicentric/) | CT | 2025 | 🟢 DICOM | — | ✅ | — | OPEN | 1 physical phantom; 1,378 CT series from 649 scans on 13 scanners (8 institutions); TCIA lists 1,378 studies, 2,756 series, 467,224 images; 252.38 GB |
| [CURVAS-PDAC](https://curvas-pdacvi.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | OPEN | Training set: 40 contrast-enhanced abdominal CT cases (of a 125-scan cohort; validation=5, test=85 withheld); ~5.5 GB; each case has 5 PDAC segmentations plus STAPLE consensus and vessel annotations |
| [CirrMRI600+](https://github.com/NUBagciLab/CirrMRI600Plus) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 600+ MRI volumes (T1W and T2W); ~15GB |
| [Cyst-X](https://osf.io/74vfs/) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 1,461 abdominal MRI scans from 764 patients across 7 centers |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MCT-LTDiag](https://doi.org/10.7910/DVN/S3RW15) | CT | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 517 patients / 2,068 CT series (4 phases per patient) |
| [MRISegmentator-Abdomen](https://github.com/rsummers11/MRISegmenter) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 195 patients, 780 T1-weighted series (69,248 slices); 4.8 GB zip |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2025 | 🟢 NIfTI, XLSX, CSV | ✅ | ✅ | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients |
| [PANTHER](https://zenodo.org/records/15192302) | MRI | 2025 | 🟡 — | — | ✅ | ✅ | REQUEST | 509 MR scans (Task 1: 459 diagnostic scans from Radboudumc, 92 annotated; Task 2: 50 MR-Linac scans from Odense University Hospital) |
| [PHLF Gd-EOB-DTPA MRI](https://zenodo.org/records/18622298) | MRI | 2025 | 🟢 NIfTI, XLSX | — | ✅ | — | OPEN | 220 patients from 3 centers; 14,895 images; 22,342 annotations; PHLF.zip 1.3 GB |
| [PanTS](https://github.com/MrGiovanni/PanTS) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | — | OPEN | 36,390 3D CT volumes from 145 centers; ~300GB |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [TrackRAD2025](https://trackrad2025.grand-challenge.org/) | MRI | 2025 | 🟢 MHA | — | ✅ | — | REGISTRATION | 585 patients (108 with manual tumor segmentations, 477 unlabeled) from 6 international MRI-linac centers |
| [UCSF-RMaC](https://registry.opendata.aws/ucsf-rmac/) | CT | 2025 | 🟢 HDF5 | — | ✅ | ✅ | OPEN | 831 multiphase CT exams (one HDF5 file per patient ID), acquired 2002-2018 |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [AbdomenAtlas 1.0](https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas1.0Mini) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | DUA | 5,195 annotated CT volumes, 326 GB |
| [AbdomenAtlas 1.1](https://github.com/MrGiovanni/AbdomenAtlas) | CT | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 9,262 CT volumes; >251,000 masks |
| [Aortic Dissection (Graz)](https://doi.org/10.6084/m9.figshare.22269091) | CT | 2024 | 🟢 NRRD, STL | — | ✅ | — | OPEN | 40 CTA volumes / 40 patients |
| [BAMF AIMI Annotations](https://zenodo.org/records/13244892) 🏷 | CT, MRI, PET | 2024 | 🟡 DICOM-SEG, CSV | — | ✅ | — | OPEN | 11 task archives (~650 MB total) of AI segmentations for IDC collections; ~10% of predictions reviewed/corrected |
| [CARE 2024 LiQA](http://www.zmic.org.cn/care_2024/track3/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 440 patients; training 250 (30 with liver segmentation masks + 220 unannotated, all 250 with fibrosis staging labels); test 160 (120 known vendors + 40 unseen vendor) |
| [CURVAS](https://curvas.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 90 CT scans (training set ~6.3 GB) |
| [FLARE 2024](https://www.codabench.org/competitions/2320/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Thousands of partially labeled and unlabeled abdominal CT scans (large semi-supervised set) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MRE-IBD](https://zenodo.org/records/13839321) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 114 patients, one coronal HASTE volume each (25-31 slices); 441.5 MB |
| [MedMNIST+](https://zenodo.org/records/10519652) | X-ray, CT | 2024 | 🟡 NPZ | — | — | — | OPEN | ~708K 2D images and ~10K 3D images across 18 datasets (12 2D, 6 3D); sizes 28/64/128/224 px (2D) and 28/64 voxels (3D) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [PANORAMA](https://panorama.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | ~2,238 CECT training scans (two centers) plus 194 MSD and 80 NIH external cases; ~197 GB |
| [PLC-CECT](https://doi.org/10.57760/sciencedb.12207) | CT | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 361 subjects (278 primary liver cancer: 94 HCC, 99 ICC, 85 cHCC-CCA; 83 non-liver-cancer controls); 1,444 3D CECT volumes; ~42 GB |
| [PanSegData](https://osf.io/kysnj/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 767 MRI (385 T1W + 382 T2W; 499 participants, 5 centers) |
| [VAREPOP-APOLLO](https://www.cancerimagingarchive.net/collection/varepop-apollo/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM | — | — | — | OPEN | 41 subjects, 279 studies, 1,549 series, 235,421 images (129.1 GB), version 3 |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [WAW-TACE](https://zenodo.org/records/12741586) | CT | 2024 | 🟢 NIfTI, NRRD, XLSX, CSV | — | ✅ | ✅ | OPEN | 233 patients, 854 CT volumes, 377 tumor masks (48.2 GB) |
| [ATLAS](https://atlas-challenge.u-bourgogne.fr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 90 T1 contrast-enhanced MRI scans (60 train / 30 test) from 90 unresectable HCC patients |
| [Adrenal-ACC-Ki67-Seg](https://www.cancerimagingarchive.net/collection/adrenal-acc-ki67-seg/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 53 patients; 65 studies; 177 series; 18,255 images; ~9.9 GB |
| [CT-Phantom4Radiomics](https://www.cancerimagingarchive.net/collection/ct-phantom4radiomics/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 1 physical phantom; 238 CT series with 8 parameter variations (476 series incl. SEG, 78,452 images); 42.49 GB |
| [Colorectal-Liver-Metastases](https://www.cancerimagingarchive.net/collection/colorectal-liver-metastases/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 197 patients |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [Duke Liver Dataset](https://zenodo.org/records/7774566) | MRI | 2023 | 🟢 DICOM, CSV | — | ✅ | ✅ | REQUEST | 2,146 MRI series (113,280 images) from 105 patients; liver masks for 310 series / 95 patients |
| [Duke Spleen Data Set](https://zenodo.org/records/7636640) | CT, MRI | 2023 | 🟢 DICOM | — | ✅ | ✅ | REQUEST | 109 CT/MRI series (6,322 images) from 69 patients: 29 axial post-contrast CT, 40 coronal SSFSE MRI, 40 axial T1w opposed-phase MRI |
| [FLARE23](https://codalab.lisn.upsaclay.fr/competitions/12239) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 4000 train + 100 val + 400 test CT |
| [KiTS23](https://kits-challenge.org/kits23/) | CT | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 599 CT (489 train / 110 test) |
| [LLD-MMRI](https://github.com/LMMMEng/LLD-MMRI-Dataset) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | REQUEST | 498 patients, 8 sequences each |
| [LiverHccSeg](https://zenodo.org/records/8179129) | MRI | 2023 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | ✅ | OPEN | 17 patients with liver masks / 14 with tumor masks (one multiphasic MRI study each); 2.6 GB |
| [RSNA 2023 Abdominal Trauma Detection](https://www.kaggle.com/competitions/rsna-2023-abdominal-trauma-detection) | CT | 2023 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~4,700 patients (multiple CT series each) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [CTpred-Sunitinib-panNET](https://www.cancerimagingarchive.net/collection/ctpred-sunitinib-pannet/) | CT | 2022 | 🟢 DICOM, XLSX | — | — | — | OPEN | 38 patients / 76 studies / 76 series / 22,474 CT images (11.85 GB); 171 lesions |
| [FLARE22](https://flare22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 2300 CT (50 labeled + 2000 unlabeled train) |
| [KiPA22](https://kipa22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 130 CTA cases (100 available: 70 training + 30 open test) |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [StageII-Colorectal-CT](https://www.cancerimagingarchive.net/collection/stageii-colorectal-ct/) | CT | 2022 | 🟢 DICOM | — | — | — | OPEN | 230 patients / 230 studies / 230 series / 13,850 images; 7.31 GB |
| [UW-Madison GI Tract](https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation) | MRI | 2022 | 🟡 PNG, CSV | — | ✅ | — | REGISTRATION | 85 cases / 38,496 slices (competition train); full release 107 patients / 467 scans / 67,248 slices |
| [VinDr-Multiphase](https://vindr.ai/datasets/abdomen-phases) | CT | 2022 | 🟢 DICOM | — | — | ✅ | DUA | 265 studies (265 patients) / 1,188 CT scans, 2015-2020 |
| [WORD](https://github.com/HiLab-git/WORD) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 150 CT (100 train / 20 val / 30 test) |
| [AHEP0731](https://www.cancerimagingarchive.net/collection/ahep0731/) | CT, MRI, PET, X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 190 subjects / 855 studies / 5,704 series / 417,972 images (220.94 GB; includes ultrasound) |
| [AbdomenCT-1K](https://github.com/JunMa11/AbdomenCT-1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 1112 CT from 12 centers |
| [CT Kidney Dataset: Normal-Cyst-Tumor-Stone](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone) | CT | 2021 | 🟡 JPG | — | — | — | REGISTRATION | 12,446 CT images (Normal 5,077; Cyst 3,709; Tumor 2,283; Stone 1,377) |
| [FLARE21](https://flare.grand-challenge.org/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 511 CT (361 train / 50 val / 100 test) |
| [HCC-TACE-Seg](https://www.cancerimagingarchive.net/collection/hcc-tace-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 105 patients; ~28.6 GB |
| [KiTS21](https://kits-challenge.org/kits21/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 train + 100 test CT |
| [Pancreatic-CT-CBCT-SEG](https://www.cancerimagingarchive.net/collection/pancreatic-ct-cbct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 40 patients (~14.3 GB, 370 series, 24,246 images) |
| [QIBA-CT-Liver-Phantom](https://www.cancerimagingarchive.net/collection/qiba-ct-liver-phantom/) | CT | 2021 | 🟢 DICOM | — | — | — | OPEN | 3 phantom datasets; 5 studies, 684 series, 102,022 images; 53.85 GB |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [T2-weighted Kidney MRI Segmentation](https://zenodo.org/records/5153568) | MRI | 2021 | 🟡 — | — | ✅ | — | OPEN | 100 T2-weighted abdominal MRI scans (50 healthy controls, 50 CKD patients; 10 subjects scanned 5 times in one session); ~153 MB |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [LDCT-and-Projection-data](https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/) | CT | 2020 | 🟢 DICOM, DICOM-CT-PD | — | — | — | OPEN | 299 patient exams + 1 phantom: chest 99 (256.81 GB), liver/abdomen 100 (604.12 GB), head 99 (462.77 GB, restricted) |
| [MOOD](https://www.synapse.org/mood) | MRI, CT | 2020 | 🟢 NIfTI | — | — | — | REGISTRATION | ~800 brain MRI + ~600 abdominal CT scans |
| [PDMR-292921-168-R](https://www.cancerimagingarchive.net/collection/pdmr-292921-168-r/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 19 subjects (mice), 86 studies, 154 series, 2,546 images; 1.56 GB |
| [PDMR-425362-245-T](https://www.cancerimagingarchive.net/collection/pdmr-425362-245-t/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 20 mice / 115 studies / 210 series / 3,509 images (2.35 GB) |
| [PDMR-833975-119-R](https://www.cancerimagingarchive.net/collection/pdmr-833975-119-r/) | MRI | 2020 | 🟢 DICOM | — | — | — | OPEN | 20 mice (subjects), 100 studies, 180 series, 2,980 images; 1.82 GB |
| [TCGA-KIRC](https://www.cancerimagingarchive.net/collection/tcga-kirc/) | CT, MRI, X-ray | 2020 | 🟢 DICOM | ✅ | — | ✅ | OPEN | 91.56 GB |
| [C4KC-KiTS](https://www.cancerimagingarchive.net/collection/c4kc-kits/) | CT | 2019 | 🟢 DICOM | — | ✅ | — | OPEN | 210 subjects / 210 studies / 621 series / 71,423 images (40.72 GB) |
| [CHAOS](https://chaos.grand-challenge.org/) | CT, MRI | 2019 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 40 CT + 120 MRI series (40 patients) |
| [Crowds-Cure-2018](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2018/) 🏷 | CT | 2019 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | 4,756 bi-directional lesion measurements on CT scans of 324 patients from 13 TCIA collections; label files 5.76 MB |
| [KiTS19](https://kits19.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 CT (210 train / 90 test) |
| [CPTAC-CCRCC](https://www.cancerimagingarchive.net/collection/cptac-ccrcc/) | CT, MRI | 2018 | 🟢 DICOM | — | — | ✅ | OPEN | Radiology: 65 subjects / 85 studies / 727 series / 99,098 images (56.58 GB), plus rare-kidney-tumor radiology 6 subjects / 139 series (6.64 GB); 262 subjects in total including pathology-only (v14) |
| [CPTAC-PDA](https://www.cancerimagingarchive.net/collection/cptac-pda/) | CT, MRI, PET | 2018 | 🟢 DICOM | — | — | ✅ | OPEN | Radiology: 110 subjects / 134 studies / 1,133 series / 132,852 images (67.24 GB); pathology 168 subjects (88 GB); 168 subjects in total (v15) |
| [Crowds-Cure-2017](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2017/) 🏷 | CT | 2018 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | Annotations for 352 subjects (source CT: 352 studies, 443 series, 49,211 images, 25.99 GB); annotation files 4.64 MB |
| [DenseVNet Multi-organ Abdominal CT Labels](https://zenodo.org/records/1169361) 🏷 | CT | 2018 | 🟡 NIfTI | — | ✅ | — | OPEN | Segmentations for 90 abdominal CT cases (43 TCIA Pancreas-CT + 47 BTCV) |
| [MSD Colon (Task10)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 190 CT (126 train / 64 test) |
| [MSD Hepatic Vessel (Task08)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 443 CT (303 train / 140 test) |
| [MSD Liver (Task03)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 201 CT (131 train / 70 test) |
| [MSD Pancreas (Task07)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 420 CT (282 train / 139 test) |
| [MSD Spleen (Task09)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 61 CT (41 train / 20 test) |
| [SCAPIS](https://www.scapis.org/data-access/) | CT | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~30,000 participants |
| [LiTS](https://competitions.codalab.org/competitions/17094) | CT | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 131 train + 70 test CT |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Rhineland Study](https://www.rheinland-studie.de/en/) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | REQUEST | ~20,000-participant target (>10,000 enrolled) |
| [TCGA-LIHC](https://www.cancerimagingarchive.net/collection/tcga-lihc/) | CT, MRI, PET | 2016 | 🟢 DICOM | ✅ | — | ✅ | OPEN | 56.38 GB (97 subjects / 237 studies / 1,688 series / 125,397 images) |
| [BTCV / Synapse Multi-organ](https://www.synapse.org/Synapse:syn3193805) | CT | 2015 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 30 train + 20 test contrast CT |
| [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 825 patients (prone + supine) |
| [CT Lymph Nodes](https://www.cancerimagingarchive.net/collection/ct-lymph-nodes/) | CT | 2015 | 🟢 DICOM, DICOM-SEG, NIfTI, TXT, MPS | — | ✅ | — | OPEN | 176 CT scans / 176 patients (90 mediastinal, 86 abdominal); 352 series, 110,179 images; 58.42 GB |
| [Mouse-Mammary](https://www.cancerimagingarchive.net/collection/mouse-mammary/) | MRI | 2015 | 🟢 DICOM | — | — | — | OPEN | 32 mice / 149 studies / 205 series / 23,487 images; 8.58 GB |
| [Pancreas-CT (NIH)](https://www.cancerimagingarchive.net/collection/pancreas-ct/) | CT | 2015 | 🟢 DICOM, NIfTI | — | ✅ | — | OPEN | 82 contrast-enhanced abdominal CT |
| [TCGA-COAD](https://www.cancerimagingarchive.net/collection/tcga-coad/) | CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 25 subjects / 32 studies / 93 series / 8,387 images (CT, OT); 4.5 GB |
| [TCGA-KICH](https://www.cancerimagingarchive.net/collection/tcga-kich/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 15 subjects / 15 studies / 109 series / 9,221 images; 4.56 GB |
| [TCGA-KIRP](https://www.cancerimagingarchive.net/collection/tcga-kirp/) | CT, MRI, PET | 2014 | 🟢 DICOM | — | — | — | OPEN | 33 subjects / 47 studies / 376 series / 26,667 images (10.27 GB) |
| [TCGA-SARC](https://www.cancerimagingarchive.net/collection/tcga-sarc/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 5 subjects / 6 studies / 33 series / 5,653 images; 2.8 GB |
| [TCGA-STAD](https://www.cancerimagingarchive.net/collection/tcga-stad/) | CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 46 subjects / 46 studies / 308 series / 43,908 images (23.32 GB) |
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | MRI, DXA | 2014 | 🟢 DICOM, NIfTI, derived phenotypes (TSV) | — | — | ✅ | REQUEST | ~100,000 participants imaged; abdominal MRI-derived phenotypes for 40,000+ |
| [CONSTANCES](https://www.constances.fr/espace-scientifique/) | MRI | 2012 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~220,000 participants |
| [Qatar Biobank](https://www.qphi.org.qa/research/how-to-apply) | DXA, Ultrasound | 2012 | 🟡 derived | — | — | — | REQUEST | ~60,000 participants target (DXA and carotid ultrasound on examination subsets) |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [AGES-Reykjavik](https://hjarta.is/en/research/ages/) | MRI, CT | 2011 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~5,764 participants (baseline); brain MRI in most, thigh/abdomen QCT in sub-samples |
| [MASALA](https://www.masalastudy.org/for-researchers) | CT | 2010 | 🟢 DICOM, derived | — | ✅ | — | DUA | ~1,164 participants at baseline (expanded in later exams) |
| [GUSTO](https://www.gusto.sg/) | MRI, DXA, CT | 2009 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~1,200 mother-offspring pairs |
| [NEO Study](https://www.lumc.nl/en/afdelingen/Clinical-Epidemiology/obesity--related-diseases/) | MRI | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | 6,671 participants |
| [Jackson Heart Study (JHS)](https://biolincc.nhlbi.nih.gov/studies/jhs/) | MRI, CT | 2004 | 🟢 DICOM, derived | — | ✅ | ✅ | DUA | 5,306 participants |
| [Framingham Heart Study MDCT](https://www.framinghamheartstudy.org/fhs-for-researchers/data-available-overview/) | CT | 2002 | 🟢 DICOM, derived | — | ✅ | — | REQUEST | ~3,500 participants in the MDCT substudy (of >15,000 total FHS cohort) |
| [CARDIA](https://biolincc.nhlbi.nih.gov/studies/cardia/) | CT, MRI, DXA | 2000 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 5,115 participants enrolled (1985-86); imaging performed in subsets or the full cohort across follow-up exams |
| [MESA](https://biolincc.nhlbi.nih.gov/studies/mesa/) | MRI, CT | 2000 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | 6,814 participants |
| [MrOS](https://mrosonline.ucsf.edu/) | CT, DXA, X-ray | 2000 | 🟢 DICOM, derived | — | ✅ | — | DUA | 5,994 men (aged 65+) |
| [NHANES DXA](https://wwwn.cdc.gov/nchs/nhanes/dxa/dxa.aspx) | DXA | 1999 | 🟡 derived | ✅ | — | — | OPEN | ~30,000+ participants with whole-body DXA (1999-2006 cycles); additional femur/spine bone-density and visceral-fat DXA in later cycles |
| [Health ABC](https://agingresearchbiobank.nia.nih.gov/studies/healthabc/) | CT, DXA | 1997 | 🟢 DICOM, derived | — | ✅ | — | DUA | 3,075 older adults (aged 70-79 at baseline) |
| [Fenland Study](https://studies.epi.ims.cam.ac.uk/fenland/data-sharing) | DXA | — | 🟡 derived | — | — | — | REQUEST | ~12,435 participants |

### ⬇️ Pelvic & Prostate  <sub>(68)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CBCT-IQ](https://zenodo.org/records/20124496) | CT | 2026 | 🟢 NIfTI, CSV | — | — | — | OPEN | 36 reconstructed CBCT volumes, 1,764 selected image slices from 2 anthropomorphic phantoms (~790 MB) |
| [CMB-CRC](https://www.cancerimagingarchive.net/collection/cmb-crc/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 400.75 GB; 102 subjects (v11); 62 radiology patients with 269,002 images |
| [CMB-OV](https://www.cancerimagingarchive.net/collection/cmb-ov/) | CT, MRI | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 36.99 GB radiology (Version 4); 19 radiology subjects, 71 studies, 554 series, 68,415 images; 162 GB histopathology (48 subjects) |
| [CMB-PCA](https://www.cancerimagingarchive.net/collection/cmb-pca/) | MRI, CT, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 98.09 GB; 76 subjects (open radiology tier: 26 subjects, ~16.41 GB) |
| [COBRA2026](https://doi.org/10.5281/zenodo.21322350) | CT | 2026 | 🟢 MHA, XML, YAML, PNG | — | — | — | OPEN | 867 cases (692 train / 52 val / 123 test); ~950 GB total |
| [CT-PEGCT-Diag](https://doi.org/10.57760/sciencedb.37604) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 642 non-enhanced CT scans / 642 pediatric patients |
| [CTSpinoPelvic1K](https://huggingface.co/datasets/OpenSpineConsortium/CTSpinoPelvic1K) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 802 CT/label pairs (abdominopelvic CT colonography volumes); ~195 GB |
| [CancerVerse](https://huggingface.co/datasets/BodyMaps/CancerVerse) | CT | 2026 | 🟢 NIfTI, CSV | ✅ | — | ✅ | REGISTRATION | 24,168 CT volumes from 13,863 patients (staged release; stage 1: 22,865 volumes with reports) |
| [KUB-StoneX](https://figshare.com/articles/dataset/_b_KUB-StoneX_b_Annotated_Kidney-Ureter-Bladder_X-ray_Dataset_with_Expert_Stone_Segmentations_and_Radiomic_Features/32049369) | X-ray | 2026 | 🟡 — | — | ✅ | — | OPEN | 2,570 AP KUB radiographs / 1,703 patients; 19.3 GB zip |
| [Merlin Plus](https://github.com/MrGiovanni/MerlinPlus) | CT | 2026 | 🟡 NIfTI, CSV | ✅ | ✅ | — | OPEN | 1,193 radiologist-created tumor masks (9 organs) + 44-class AI organ masks for the 25,494 Merlin CT scans (18,317 patients); 3,830 patients with 2+ scans; no images included |
| [VSD Lower Extremities Seg](https://huggingface.co/datasets/BoneHub/vsd-lower-extremities-seg) | CT | 2026 | 🟢 NIfTI, STL, JSON | — | ✅ | — | OPEN | 30 lower-body CT scans (14 female / 16 male, aged 19-95) with 63-label bone maps and per-bone STL meshes; ~8.7 GB |
| [AbdomenAtlas 2.0](https://github.com/BodyMaps/AbdomenAtlas2.0) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | OPEN | 10,135 CT scans from 89 hospitals; 15,130 tumor masks; 5,893 control scans (~400 GB) |
| [Endometriosis Pelvic MRI](https://doi.org/10.1038/s41597-025-05623-3) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 132 subjects: Dataset 1 with 51 subjects (multicenter, 15 sites) and Dataset 2 with 81 subjects (single site) |
| [LUND-PROBE](https://datahub.aida.scilifelab.se/10.23698/aida/lund-probe) | MRI, CT | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 467 patients (432 primary + 35 extended deep-learning subset), 176.56 GB |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2025 | 🟢 NIfTI, XLSX, CSV | ✅ | ✅ | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [UT-EndoMRI](https://zenodo.org/records/15750762) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 133 patients (51 in dataset 1 + 82 in dataset 2); ~7.4 GB |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [BAMF AIMI Annotations](https://zenodo.org/records/13244892) 🏷 | CT, MRI, PET | 2024 | 🟡 DICOM-SEG, CSV | — | ✅ | — | OPEN | 11 task archives (~650 MB total) of AI segmentations for IDC collections; ~10% of predictions reviewed/corrected |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [VAREPOP-APOLLO](https://www.cancerimagingarchive.net/collection/varepop-apollo/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM | — | — | — | OPEN | 41 subjects, 279 studies, 1,549 series, 235,421 images (129.1 GB), version 3 |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [fastMRI Prostate](https://fastmri.med.nyu.edu/) | MRI | 2024 | 🟡 HDF5 | — | — | ✅ | DUA | — |
| [CC-Tumor-Heterogeneity](https://www.cancerimagingarchive.net/collection/cc-tumor-heterogeneity/) | MRI, PET, CT | 2023 | 🟢 DICOM, XLSX | — | ✅ | ✅ | OPEN | 23 patients / 171 studies / 821 series / 131,556 images (28.39 GB) |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [ExACT](https://www.cancerimagingarchive.net/collection/exact/) | MRI | 2023 | 🟢 DICOM, XLSX, PDF | — | — | ✅ | DUA | 30 subjects / 30 studies / 179 series / 6,400 images; 1.64 GB |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SynthRAD2023](https://synthrad2023.grand-challenge.org/) | MRI, CT | 2023 | 🟢 MHA | — | — | — | OPEN | 540 paired MRI-CT and 540 CBCT-CT sets (>500 patients per task) from three centers |
| [μ-RegPro](https://zenodo.org/records/8004388) | MRI | 2023 | 🟡 — | — | — | — | OPEN | More than a hundred paired prostate MR and TRUS images (train.zip 104.4 MB, val.zip 12.1 MB) |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [Cross-institution Male Pelvic Structures](https://zenodo.org/records/7013610) | MRI | 2022 | 🟡 — | — | ✅ | — | OPEN | 589 T2-weighted MR images / 589 patients; 7 institution subsets; data.zip 3.1 GB |
| [PI-CAI](https://pi-cai.grand-challenge.org/) | MRI | 2022 | 🟢 MHA, NIfTI | — | ✅ | ✅ | OPEN | 1500 bpMRI (1476 patients, public set) |
| [Prostate158](https://github.com/kbressem/prostate158) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 158 studies (139 train / 19 test) |
| [StageII-Colorectal-CT](https://www.cancerimagingarchive.net/collection/stageii-colorectal-ct/) | CT | 2022 | 🟢 DICOM | — | — | — | OPEN | 230 patients / 230 studies / 230 series / 13,850 images; 7.31 GB |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [CTPelvic1K](https://github.com/MIRACLE-Center/CTPelvic1K) | CT | 2020 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 1,184 CT volumes (~320K slices), ~17 GB |
| [Prostate-MRI-US-Biopsy](https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/) | MRI | 2020 | 🟢 DICOM, STL, XLSX | ✅ | ✅ | ✅ | OPEN | 1,151 subjects; 2,799 studies; ~80 GB |
| [CPTAC-UCEC](https://www.cancerimagingarchive.net/collection/cptac-ucec/) | CT, MRI, PET | 2019 | 🟢 DICOM, SVS | — | — | — | OPEN | Radiology: 90 subjects, 146 studies, 1,959 series, 187,026 images (80.24 GB); pathology: 250 subjects, 887 whole-slide images (154 GB) |
| [Crowds-Cure-2018](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2018/) 🏷 | CT | 2019 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | 4,756 bi-directional lesion measurements on CT scans of 324 patients from 13 TCIA collections; label files 5.76 MB |
| [Pelvic-Reference-Data](https://www.cancerimagingarchive.net/collection/pelvic-reference-data/) | CT | 2019 | 🟢 DICOM, XLSX | — | — | — | OPEN | 58 subjects / 116 studies / 116 series / 13,644 images (7.19 GB): one CT and one cone-beam CT per case |
| [Crowds-Cure-2017](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2017/) 🏷 | CT | 2018 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | Annotations for 352 subjects (source CT: 352 studies, 443 series, 49,211 images, 25.99 GB); annotation files 4.64 MB |
| [Gold Atlas](https://zenodo.org/records/583096) | MRI, CT | 2018 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 19 patients, ~1.7 TB |
| [MSD Prostate (Task05)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 48 mpMRI (32 train / 16 test) |
| [QIN-PROSTATE-Repeatability](https://www.cancerimagingarchive.net/collection/qin-prostate-repeatability/) | MRI | 2018 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 15 subjects / 30 studies / 330 series / 38,500 images; 14.86 GB |
| [ProstateX](https://www.cancerimagingarchive.net/collection/prostatex/) | MRI | 2017 | 🟢 DICOM | — | — | ✅ | OPEN | 346 patients (330 lesions train) |
| [Prostate Fused-MRI-Pathology](https://www.cancerimagingarchive.net/collection/prostate-fused-mri-pathology/) | MRI | 2016 | 🟢 DICOM, TIFF, XML, MHA, MATLAB, XLSX | — | ✅ | ✅ | OPEN | 28 subjects / 28 MR studies / 324 series / 32,508 DICOM images (4.74 GB); plus 76.8 GB pseudo-whole-mount histopathology |
| [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 825 patients (prone + supine) |
| [PROSTATE-DIAGNOSIS](https://www.cancerimagingarchive.net/collection/prostate-diagnosis/) | MRI | 2015 | 🟢 DICOM, NRRD, MHA, XLS | ✅ | ✅ | ✅ | OPEN | 87 subjects / 87 studies / 348 series / 30,903 images (5.67 GB); collection header lists 92 subjects |
| [Prostate-3T](https://www.cancerimagingarchive.net/collection/prostate-3t/) | MRI | 2015 | 🟢 DICOM, MHA, NRRD | — | ✅ | — | OPEN | 59 subjects, 1161 images (~269 MB) |
| [SPL Prostate MRI-US Registration](https://zenodo.org/records/16396) | MRI | 2015 | 🟢 NRRD, FCSV | — | ✅ | — | OPEN | 3 patients: 3 prostate MRI volumes + 3 resampled TRUS volumes (~35 MB) |
| [TCGA-PRAD](https://www.cancerimagingarchive.net/collection/tcga-prad/) | MRI, CT, PET | 2015 | 🟢 DICOM | — | — | — | OPEN | 14 subjects / 20 studies / 207 series / 16,790 images (3.74 GB) |
| [TCGA-UCEC](https://www.cancerimagingarchive.net/collection/tcga-ucec/) | CT, PET, MRI, X-ray | 2015 | 🟢 DICOM | — | — | — | OPEN | 65 subjects / 226 studies / 912 series / 77,214 images (37.85 GB) |
| [TCGA-BLCA](https://www.cancerimagingarchive.net/collection/tcga-blca/) | CT, MRI, PET, X-ray | 2014 | 🟢 DICOM | — | — | — | OPEN | 120 subjects / 192 studies / 1,051 series / 111,781 images (58.03 GB) |
| [TCGA-CESC](https://www.cancerimagingarchive.net/collection/tcga-cesc/) | MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 54 subjects / 57 studies / 488 series / 19,135 MR images (9.5 GB) |
| [TCGA-OV](https://www.cancerimagingarchive.net/collection/tcga-ov/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 143 subjects / 322 studies / 844 series / 53,662 images (28.3 GB) |
| [TCGA-READ](https://www.cancerimagingarchive.net/collection/tcga-read/) | MRI, CT | 2014 | 🟢 DICOM | — | — | — | OPEN | 3 subjects / 4 studies / 34 series / 1,796 images (423.48 MB) |
| [TCGA-SARC](https://www.cancerimagingarchive.net/collection/tcga-sarc/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 5 subjects / 6 studies / 33 series / 5,653 images; 2.8 GB |
| [NaF PROSTATE](https://www.cancerimagingarchive.net/collection/naf-prostate/) | PET, CT | 2013 | 🟢 DICOM | — | — | — | OPEN | 9 subjects / 44 studies / 214 series / 64,535 images (13.25 GB) |
| [PROMISE12](https://promise12.grand-challenge.org/) | MRI | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 50 train + 30 test T2W MRI |
| [MrOS](https://mrosonline.ucsf.edu/) | CT, DXA, X-ray | 2000 | 🟢 DICOM, derived | — | ✅ | — | DUA | 5,994 men (aged 65+) |
| [SOF](https://sofonline.ucsf.edu/) | DXA, CT, X-ray | 1986 | 🟢 DICOM, derived | — | — | — | DUA | 9,704 older women (plus ~662 Black women in a later supplement) |
| [UCSF-ProstateMR](https://registry.opendata.aws/ucsf-prostatemr/) | MRI | — | 🟡 — | — | ✅ | — | REQUEST | 973 prostate MRI exams |

### 🦴 Musculoskeletal  <sub>(72)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CTSpinoPelvic1K](https://huggingface.co/datasets/OpenSpineConsortium/CTSpinoPelvic1K) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 802 CT/label pairs (abdominopelvic CT colonography volumes); ~195 GB |
| [Dynamic Volumetric MRI Validation (Thigh)](https://doi.org/10.5281/zenodo.21194933) | MRI | 2026 | 🟢 MRD (ISMRMRD HDF5), NIfTI | — | ✅ | ✅ | OPEN | 9 healthy volunteers; per subject 1 validation scan (9 pressure levels), 1 hybrid scan and 4 dynamic k-space scans, plus anatomical and Dixon images; ~27 GB |
| [OrthoFrac-XR](https://figshare.com/articles/dataset/_b_OrthoFrac-XR_b_A_Clinically_Validated_Multimodal_High-Resolution_X-ray_Imaging_Dataset_for_Bone_Fracture_Detection_and_Localization/32021085) | X-ray | 2026 | 🟡 — | ✅ | — | — | OPEN | 1,493 orthopedic radiographs / ~1,300 patients (497.1 MB zip) |
| [RAM-H1200](https://huggingface.co/datasets/TokyoTechMagicYang/RAM-H1200-v1) | X-ray | 2026 | 🟡 BMP, COCO JSON | — | ✅ | — | REGISTRATION | Full-hand radiographs (left/right) with joint-level ROI crops; 2.75 GB (exact image count not stated on the card) |
| [RSNA 2026 Knee Abnormality Detection](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection) | MRI | 2026 | 🟢 DICOM, CSV | ✅ | — | ✅ | REGISTRATION | >5,000 knee MRI exams (train: 4,407 studies / 24,371 series / 819,078 DICOM files) |
| [VSD Lower Extremities Seg](https://huggingface.co/datasets/BoneHub/vsd-lower-extremities-seg) | CT | 2026 | 🟢 NIfTI, STL, JSON | — | ✅ | — | OPEN | 30 lower-body CT scans (14 female / 16 male, aged 19-95) with 63-label bone maps and per-bone STL meshes; ~8.7 GB |
| [Visible Human 3D Bone Models](https://huggingface.co/datasets/BoneHub/visible-human-3d-models) | CT | 2026 | 🟢 NIfTI, NRRD, STL, IGES, STEP | — | ✅ | — | OPEN | 2 whole-body CT volumes (Visible Human Male and Female); 142 (male) and 143 (female) individually labeled bones |
| [BTXRD](https://doi.org/10.6084/m9.figshare.27865398) | X-ray | 2025 | 🟡 JPEG, JSON, CSV | — | ✅ | — | OPEN | 3,746 radiographs (1,879 normal, 1,525 benign tumor, 342 malignant tumor); ~801 MB |
| [Bone_metastases_pet_ct_for_BlueprINT](https://huggingface.co/datasets/FangDai/Bone_metastases_pet_ct_for_BlueprINT) | PET, CT | 2025 | 🟡 PNG | — | — | — | OPEN | 1,642 image samples |
| [KMAR-50K](https://data.mendeley.com/datasets/xw7mrg7ntg) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | OPEN | 1,190 patients; 1,444 paired MRI sequences (motion-artifact vs rescanned ground truth); 62,506 slices |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [RAM-W600](https://huggingface.co/datasets/TokyoTechMagicYang/RAM-W600) | X-ray | 2025 | 🟡 BMP, NPY, JSON | — | ✅ | — | OPEN | 1,048 wrist conventional radiographs from 388 patients across 6 medical centers (618 with instance segmentation masks, 800 with SvdH bone erosion scores) |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [Spine Generic (Multi-Subject)](https://github.com/spine-generic/data-multi-subject) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | ~260+ subjects, ~26 GB, 40+ sites |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [CBCT Knee Phantom (Planmeca Viso G7)](https://zenodo.org/records/12722386) | CT | 2024 | 🟡 MAT | — | — | — | OPEN | 1 phantom scan, 500 flat-field-corrected projections (single 513.3 MB .mat file) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [PENGWIN](https://pengwin.grand-challenge.org/) | CT, X-ray | 2024 | 🟢 MHA, TIFF | — | ✅ | — | REGISTRATION | 150 patient CT scans plus synthetically generated 2D X-ray images |
| [RSNA 2024 Lumbar Spine Degenerative Classification](https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification) | MRI | 2024 | 🟢 DICOM | — | — | ✅ | REGISTRATION | ~1975 lumbar spine MRI studies |
| [SPIDER](https://zenodo.org/records/10159290) | MRI | 2024 | 🟢 MHA | — | ✅ | ✅ | OPEN | 218 studies, 447 sagittal T1/T2 MRI series (~3.8 GB) |
| [Spine-Mets-CT-SEG](https://www.cancerimagingarchive.net/collection/spine-mets-ct-seg/) | CT | 2024 | 🟢 DICOM, NIfTI | ✅ | ✅ | — | OPEN | 20.36 GB; 55 patients; 35,582 images across 110 series |
| [CMB-MML](https://www.cancerimagingarchive.net/collection/cmb-mml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 177 subjects; ~50,000 radiology images + 1,071 pathology slides; 6.05 TB |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [FracAtlas](https://figshare.com/articles/dataset/The_dataset_of_fractured_bone_x-ray_images/22363012) | X-ray | 2023 | 🟡 JPG, COCO JSON, YOLO, Pascal VOC, VGG | — | ✅ | — | OPEN | ~4,073 X-ray images (717 fractured); ~338 MB |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [GRAZPEDWRI-DX](https://figshare.com/articles/dataset/GRAZPEDWRI-DX/14825193) | X-ray | 2022 | 🟡 PNG, CSV | — | — | — | OPEN | 20,327 radiographs from 6,091 pediatric patients (~16.3 GB) |
| [K2S](https://k2s.grand-challenge.org/) | MRI | 2022 | 🟡 HDF5 | — | ✅ | — | REGISTRATION | — |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [fastMRI+](https://github.com/microsoft/fastmri-plus) | MRI | 2022 | 🟡 CSV (annotations only) | — | — | — | OPEN | 24,380 annotations, no images: knee 16,154 bounding boxes + 13 study-level labels (22 classes, all 1,172 knee volumes) and brain 7,570 bounding boxes + 643 study-level labels (30 classes, 1,001 of 5,847 brain studies) |
| [CTSpine1K](https://github.com/MIRACLE-Center/CTSpine1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,005 CT volumes (>500,000 labeled slices, >11,000 vertebrae) |
| [RibSeg](https://github.com/HINTLab/RibSeg) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 490 CT scans, 11,719 ribs (320 train / 50 dev / 120 test) |
| [SKM-TEA](https://aimi.stanford.edu/datasets/skm-tea-knee-mri) | MRI | 2021 | 🟢 HDF5 (k-space), DICOM | — | ✅ | — | REGISTRATION | 155 qDESS knee scans (~1.6 TB) |
| [VinDr-SpineXR](https://physionet.org/content/vindr-spinexr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 10,466 spine X-ray images from 5,000 studies |
| [CTPelvic1K](https://github.com/MIRACLE-Center/CTPelvic1K) | CT | 2020 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 1,184 CT volumes (~320K slices), ~17 GB |
| [RibFrac](https://ribfrac.grand-challenge.org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 660 CT scans (~5,000 fractures); 420 train, 80 val, 160 test |
| [LERA](https://aimi.stanford.edu/datasets/lera-lower-extremity-radiographs) | X-ray | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 182 patients (foot, knee, ankle, hip) |
| [MRSpineSeg](https://github.com/pangshumao/SpineParseNet) | MRI | 2019 | 🟢 NIfTI | — | ✅ | — | REQUEST | 172 training + 20 (round-1) + 23 (round-2) sagittal T2-weighted lumbar MRI volumes (test labels withheld) |
| [OAI-ZIB](https://doi.org/10.12752/4.ATEZ.1.0) | MRI | 2019 | 🟡 ITK MetaImage (MHD/RAW), NIfTI (OAIZIB-CM mirror) | — | ✅ | — | OPEN | 507 manual segmentation masks (384x384x160 voxels) + 116 bone-only masks; ~90 MB zip (matching OAI MRIs obtained separately) |
| [Generation R](https://generationr.nl/researchers/) | MRI, DXA | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~several thousand children with repeated brain MRI and DXA (birth cohort of ~9,700 mothers/children) |
| [MRNet](https://stanfordmlgroup.github.io/competitions/mrnet/) | MRI | 2018 | 🟢 NPY | — | — | ✅ | REGISTRATION | 1,370 knee MRI exams |
| [MURA](https://stanfordmlgroup.github.io/competitions/mura/) | X-ray | 2018 | 🟡 PNG | — | — | — | REGISTRATION | 40,561 images / 14,863 studies / 12,173 patients |
| [fastMRI knee](https://fastmri.med.nyu.edu/) | MRI | 2018 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | >1,500 fully-sampled knee k-space MRIs + 10,000 clinical DICOM knee MRIs (~1.35 TB) |
| [KneeMRI](http://www.riteh.uniri.hr/~istajduh/projects/kneeMRI/) | MRI | 2017 | 🟢 PCK | — | — | — | OPEN | 917 sagittal PD-weighted knee MRI volumes |
| [Lifelines (ImaLife)](https://www.lifelines-biobank.com/) | CT | 2017 | 🟢 DICOM | — | — | — | DUA | ~167,000 total cohort; 12,055 low-dose chest CT (ImaLife) |
| [RSNA Bone Age](https://www.rsna.org/rsnai/ai-image-challenge/rsna-pediatric-bone-age-challenge-2017) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 14,236 pediatric hand radiographs |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Tromsø Study](https://uit.no/research/tromsostudy) | DXA, MRI | 2016 | 🟢 derived, DICOM | — | — | ✅ | REQUEST | Tens of thousands of participants across seven survey waves (DXA and brain MRI collected in sub-samples) |
| [ALSPAC](http://www.bristol.ac.uk/alspac/researchers/access/) | DXA, MRI | 2015 | 🟢 derived, DICOM, NIfTI | — | — | ✅ | REQUEST | ~14,000 index children (thousands with repeated DXA; ~900 with brain MRI at 18-24y) |
| [Insight 46 (MRC NSHD 1946 birth cohort)](https://www.nshd.mrc.ac.uk/data/) | MRI, PET, DXA | 2015 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~500 imaged participants (Insight 46); ~5,300 in the NSHD birth cohort |
| [Lower Spine T2 MRI VB Segmentation](https://zenodo.org/records/22304) | MRI | 2015 | 🟢 NIfTI | — | ✅ | — | OPEN | 23 patients (23 T2-weighted MR volumes + binary masks) |
| [Soft-tissue-Sarcoma](https://www.cancerimagingarchive.net/collection/soft-tissue-sarcoma/) | PET, CT, MRI | 2015 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 9.87 GB |
| [QIN-SARCOMA](https://www.cancerimagingarchive.net/collection/qin-sarcoma/) | MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 15 subjects / 38 studies / 2,168 series / 46,614 images; 10.29 GB |
| [TCGA-SARC](https://www.cancerimagingarchive.net/collection/tcga-sarc/) | CT, MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 5 subjects / 6 studies / 33 series / 5,653 images; 2.8 GB |
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | MRI, DXA | 2014 | 🟢 DICOM, NIfTI, derived phenotypes (TSV) | — | — | ✅ | REQUEST | ~100,000 participants imaged; abdominal MRI-derived phenotypes for 40,000+ |
| [AGES-Reykjavik](https://hjarta.is/en/research/ages/) | MRI, CT | 2011 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~5,764 participants (baseline); brain MRI in most, thigh/abdomen QCT in sub-samples |
| [GUSTO](https://www.gusto.sg/) | MRI, DXA, CT | 2009 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~1,200 mother-offspring pairs |
| [Digital Hand Atlas](https://ipilab.usc.edu/research/baaweb/) | X-ray | 2007 | 🟡 JPEG | — | — | — | OPEN | ~1,400 normal pediatric hand radiographs |
| [Rotterdam Study](https://www.ergo-onderzoek.nl) | MRI, DXA | 2005 | 🟢 DICOM, derived | — | ✅ | ✅ | REQUEST | ~20,000 participants aged 40+ enrolled overall; ~5,000+ with repeated brain MRI |
| [CoLaus \| PsyCoLaus](https://www.colaus-psycolaus.ch/professionals/) | MRI, DXA | 2003 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~6,700 baseline participants; imaging sub-studies (BrainLaus, OsteoLaus) on subsets |
| [MOST](https://agingresearchbiobank.nia.nih.gov/studies/most/) | X-ray, MRI | 2003 | 🟢 DICOM | — | — | ✅ | DUA | 4,551 participants (3,026 original cohort enrolled 2003 + 1,525 new-cohort participants 2016-18); longitudinal knee radiographs, full-limb radiographs and 1.0T knee MRI through the 168-month visit |
| [MrOS](https://mrosonline.ucsf.edu/) | CT, DXA, X-ray | 2000 | 🟢 DICOM, derived | — | ✅ | — | DUA | 5,994 men (aged 65+) |
| [NHANES DXA](https://wwwn.cdc.gov/nchs/nhanes/dxa/dxa.aspx) | DXA | 1999 | 🟡 derived | ✅ | — | — | OPEN | ~30,000+ participants with whole-body DXA (1999-2006 cycles); additional femur/spine bone-density and visceral-fat DXA in later cycles |
| [Health ABC](https://agingresearchbiobank.nia.nih.gov/studies/healthabc/) | CT, DXA | 1997 | 🟢 DICOM, derived | — | ✅ | — | DUA | 3,075 older adults (aged 70-79 at baseline) |
| [HUNT Study](https://www.ntnu.edu/hunt/data) | DXA, MRI | 1995 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~250,000 participants across HUNT1-4 since 1984 |
| [BLSA](https://www.blsa.nih.gov/how-apply) | MRI, PET, DXA | 1994 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,000+ active participants with serial imaging (study cohort >3,200 enrolled since 1958) |
| [SOF](https://sofonline.ucsf.edu/) | DXA, CT, X-ray | 1986 | 🟢 DICOM, derived | — | — | — | DUA | 9,704 older women (plus ~662 Black women in a later supplement) |
| [OAI](https://nda.nih.gov/oai/) | MRI, X-ray | — | 🟢 DICOM | — | — | ✅ | DUA | 4,796 participants, longitudinal bilateral knee MRI and X-ray |

### 🎀 Breast  <sub>(47)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [BreastMammo / DenseMammo](https://osf.io/n4yr2/) | X-ray | 2026 | 🟢 DICOM, PNG | — | — | — | OPEN | BreastMammo: DICOM zip 171.2 MB + 16-bit PNG zip 234.1 MB; DenseMammo: size not stated; image and patient counts not stated |
| [Compressed bCT Breast Phantoms](https://zenodo.org/records/18617629) | CT | 2026 | 🟢 NRRD | — | ✅ | — | OPEN | 821 digital breast phantoms (CC-compressed and uncompressed versions); ~3.1 GB |
| [MAMA-MIAAI](https://physionet.org/content/mama-miaai-herewegoagain/1.0.0/) | MRI | 2026 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 1,506 cases (7,868 bias-field-corrected DCE-MRI images); 1,506 automated + 94 manual whole-breast masks |
| [Breast Micro-Calcifications Sequential Mammograms](https://zenodo.org/records/14859694) | X-ray | 2025 | 🟢 DICOM, JPEG | — | ✅ | — | OPEN | 100 pairs of temporally sequential mammograms (prior and recent, CC and MLO views); ~2.8 GB |
| [BreastDCEDL](https://doi.org/10.5281/zenodo.15627232) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 2,070 patients (Duke 916, I-SPY1 172, I-SPY2 982); Zenodo latest version ~26.9 GB (tumor-centred MinCrop for all cohorts + full I-SPY1); full I-SPY2 54 GB on TCIA |
| [MAMA-MIA](https://www.ub.edu/mama-mia/) | MRI | 2025 | 🟢 NIfTI, DICOM | ✅ | ✅ | ✅ | DUA | 1,506 annotated training scans plus 574 external validation cases (multi-institutional) |
| [Mammo-MX](https://zenodo.org/records/17740027) | X-ray | 2025 | 🟢 DICOM, CSV | — | — | — | OPEN | 13,659 mammograms / 3,368 patients; ~77 GB |
| [NL-Breast-Screening](https://www.frdr-dfdr.ca/repo/dataset/2af839d4-d54f-48d7-9a1a-a00e57fe72ea) | X-ray | 2025 | 🟢 DICOM | — | — | — | OPEN | 5,997 four-view exams / 26,988 images / 5,935 patients; 90.8 GB download (3 .7z archives + metadata CSV) |
| [ODELIA Breast MRI 2025](https://huggingface.co/datasets/ODELIA-AI/ODELIA-Challenge-2025) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | DUA | 500 studies (~135GB) from six European centers, multiple vendors at 1.5T and 3T |
| [TN-Mammo](https://physionet.org/content/tn-mammo-breast-density/) | X-ray | 2025 | 🟡 JPEG | — | — | — | DUA | 676 exams (2,704 images, 4 views each) |
| [Advanced-MRI-Breast-Lesions](https://www.cancerimagingarchive.net/collection/advanced-mri-breast-lesions/) | MRI | 2024 | 🟢 DICOM, XLSX | ✅ | ✅ | ✅ | OPEN | 645.62 GB; 632 imaging sessions (1,259,688 images, 6,811 series) |
| [BAMF AIMI Annotations](https://zenodo.org/records/13244892) 🏷 | CT, MRI, PET | 2024 | 🟡 DICOM-SEG, CSV | — | ✅ | — | OPEN | 11 task archives (~650 MB total) of AI segmentations for IDC collections; ~10% of predictions reviewed/corrected |
| [Breast Masses Sequential Mammograms](https://zenodo.org/records/11446259) | X-ray | 2024 | 🟡 — | — | ✅ | — | OPEN | 100 pairs of mammograms (prior and recent rounds, two views per patient); ~3.0 GB |
| [CMB-BRCA](https://www.cancerimagingarchive.net/collection/cmb-brca/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 203.94 GB total (78.94 GB radiology, 125 GB pathology); 101 subjects |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [fastMRI Breast](https://fastmri.med.nyu.edu/) | MRI | 2024 | 🟡 HDF5 | — | — | — | DUA | 300 clinical exams |
| [BreastDM](https://github.com/smallboy-code/Breast-cancer-dataset) | MRI | 2023 | 🟡 PNG | — | ✅ | ✅ | OPEN | 232 cases (147 malignant, 85 benign) |
| [DMID](https://figshare.com/articles/dataset/_b_Digital_mammography_Dataset_for_Breast_Cancer_Diagnosis_Research_DMID_b_DMID_rar/24522883) | X-ray | 2023 | 🟢 DICOM, TIFF | ✅ | ✅ | — | OPEN | 510 mammograms (DICOM + TIFF); ~11.7 GB |
| [EA1141](https://www.cancerimagingarchive.net/collection/ea1141/) | MRI, X-ray, CT | 2023 | 🟢 DICOM | — | — | — | OPEN | 500 subjects / 1,976 studies / 14,343 series / 855,640 images; 2.82 TB |
| [EMBED](https://registry.opendata.aws/emory-breast-imaging-dataset-embed/) | X-ray | 2023 | 🟢 DICOM | — | — | — | DUA | 3.4M images from ~110,000 patients; 60,000 annotated lesions |
| [RSNA Screening Mammography](https://mira.rsna.org/dataset/3) | X-ray | 2023 | 🟢 DICOM | — | — | — | REGISTRATION | Just under 20,000 screening exams from 2 sites (Kaggle training split: 54,706 images / 11,913 patients) |
| [VICTRE Simulated Tomosynthesis Projections](https://zenodo.org/records/8108701) | X-ray | 2023 | 🟡 — | — | — | — | OPEN | 2 sets of 259 raw DBT projections, each from a different phantom (~5.5 GB zipped) |
| [ISPY2](https://www.cancerimagingarchive.net/collection/ispy2/) | MRI | 2022 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 719 patients |
| [VinDr-Mammo](https://physionet.org/content/vindr-mammo/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 5,000 exams / 20,000 images |
| [ACRIN-6698](https://www.cancerimagingarchive.net/collection/acrin-6698/) | MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 385 subjects / 1,123 studies / 18,747 series / 2,911,334 images (~842 GB download) |
| [ACRIN-Contralateral-Breast-MR](https://www.cancerimagingarchive.net/collection/acrin-contralateral-breast-mr/) | MRI, X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 984 patients / 1,103 studies / 10,184 series / 626,782 images (199.59 GB) |
| [BCS-DBT](https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,060 patients / 22,032 scans (~1.63 TB) |
| [CDD-CESM](https://www.cancerimagingarchive.net/collection/cdd-cesm/) | X-ray | 2021 | 🟡 JPEG | ✅ | ✅ | — | OPEN | 2,006 images (1,003 low-energy + 1,003 subtracted CESM) / 326 patients; ~1.5 GB |
| [CMMD](https://www.cancerimagingarchive.net/collection/cmmd/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,202 images / 1,775 patients |
| [CSAW-M](https://figshare.scilifelab.se/articles/dataset/CSAW-M_An_Ordinal_Classification_Dataset_for_Benchmarking_Mammographic_Masking_of_Cancer/14687271) | X-ray | 2021 | 🟡 — | — | — | — | REQUEST | Mammograms from over 10,000 individuals |
| [ACRIN-FLT-Breast](https://www.cancerimagingarchive.net/collection/acrin-flt-breast/) | PET, CT | 2020 | 🟢 DICOM | ✅ | — | — | OPEN | 74.24 GB |
| [CSAW-S](https://zenodo.org/records/4030660) | X-ray | 2020 | 🟡 — | — | ✅ | — | REQUEST | Mammography screenings from 172 patients |
| [VICTRE](https://www.cancerimagingarchive.net/collection/victre/) | X-ray | 2019 | 🟢 DICOM | — | — | — | OPEN | 2,994 computational phantom subjects; 8,749 studies/series; 217,913 images; 1.03 TB |
| [Duke Breast Cancer MRI](https://www.cancerimagingarchive.net/collection/duke-breast-cancer-mri/) | MRI | 2018 | 🟢 DICOM | — | — | ✅ | OPEN | 922 patients / ~773,000 images |
| [Breast-MRI-NACT-Pilot](https://www.cancerimagingarchive.net/collection/breast-mri-nact-pilot/) | MRI | 2016 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 64 patients / 189 studies / 2,224 series / 98,936 images (19.51 GB) |
| [CBIS-DDSM](https://www.cancerimagingarchive.net/collection/cbis-ddsm/) | X-ray | 2016 | 🟢 DICOM | — | ✅ | — | OPEN | 10,239 images / 1,566 subjects |
| [ISPY1 (ACRIN 6657)](https://www.cancerimagingarchive.net/collection/ispy1/) | MRI | 2016 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 222 patients |
| [Mouse-Mammary](https://www.cancerimagingarchive.net/collection/mouse-mammary/) | MRI | 2015 | 🟢 DICOM | — | — | — | OPEN | 32 mice / 149 studies / 205 series / 23,487 images; 8.58 GB |
| [QIN-SARCOMA](https://www.cancerimagingarchive.net/collection/qin-sarcoma/) | MRI | 2014 | 🟢 DICOM | — | — | — | OPEN | 15 subjects / 38 studies / 2,168 series / 46,614 images; 10.29 GB |
| [TCGA-BRCA](https://www.cancerimagingarchive.net/collection/tcga-brca/) | MRI, X-ray | 2014 | 🟢 DICOM | — | — | — | OPEN | 139 subjects / 164 studies / 1,877 series / 230,167 images; 88.13 GB |
| [INbreast](http://medicalresearch.inescporto.pt/breastresearch/index.php/Get_INbreast_Database) | X-ray | 2012 | 🟢 DICOM, XML | — | ✅ | — | REQUEST | 410 images / 115 cases |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [Breast-Diagnosis](https://www.cancerimagingarchive.net/collection/breast-diagnosis/) | MRI, PET, CT, X-ray | 2011 | 🟢 DICOM | — | — | ✅ | OPEN | 88 subjects / ~105,050 images |
| [RIDER Breast MRI](https://www.cancerimagingarchive.net/collection/rider-breast-mri/) | MRI | 2011 | 🟢 DICOM | — | — | — | OPEN | 5 patients / 10 studies / 40 series / 2,400 images; 401.61 MB |
| [OPTIMAM (OMI-DB)](https://medphys.royalsurrey.nhs.uk/omidb/) | X-ray | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | ~750,000 cases (2D full-field digital mammography and 3D tomosynthesis) |
| [mini-MIAS](https://www.mammoimage.org/databases/) | X-ray | 1994 | 🟡 PGM | — | — | — | OPEN | 322 images (~2.3 GB original; ~100 MB distributed) |
| [3D-MammographyDataset](https://huggingface.co/datasets/iMerit/3D-MammographyDataset) | X-ray | — | 🟢 DICOM, JSON, XLSX | — | — | — | DUA | ~650 MB, fewer than 1,000 cases |

### 👤 Head & Neck  <sub>(48)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [CT-PEGCT-Diag](https://doi.org/10.57760/sciencedb.37604) | CT | 2026 | 🟢 NIfTI | — | ✅ | — | OPEN | 642 non-enhanced CT scans / 642 pediatric patients |
| [UCSD-VS-Longitudinal](https://www.cancerimagingarchive.net/collection/ucsd-vs-longitudinal/) | MRI | 2026 | 🟢 NIfTI, TSV | — | ✅ | ✅ | OPEN | 570 MRI timepoints / 191 patients; 4,391 series; ~40 GB |
| [CBCT projection images of phantoms](https://zenodo.org/records/17879108) | CT | 2025 | 🟡 — | — | — | — | OPEN | 4 CBCT projection acquisitions (Skull.zip 1.6 GB, bone_inset_phantom_polychrome.zip 31.1 MB, MultiMaterialDisk.zip 2.0 GB, SegmentedHead.zip 1.7 GB) |
| [HECKTOR 2025](https://hecktor25.grand-challenge.org/) | PET, CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 1200+ patients from 11+ centers (FDG-PET/CT); ~850 training from prior editions plus ~400 new test cases from two French cohorts |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [Panoramic_Radiographs_for_Dental_Condition](https://huggingface.co/datasets/ismaelportog/Panoramic_Radiographs_for_Dental_Condition) | X-ray | 2025 | 🟡 JPG, Parquet | — | — | — | OPEN | ~27,884 annotated rows / 1.42 GB (from ~1,808 source panoramic radiographs; 1,628 training + 180 external validation) |
| [SegRap2025](https://hilab-git.github.io/SegRap2025_Challenge) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 260 NPC patients with GTV annotations, 402 patients with LN CTV annotations, plus 500 unlabeled CT scans |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [Tongue Musculature MRI](https://osf.io/wt9fc/) | MRI | 2025 | 🟢 — | — | ✅ | — | OPEN | 47 healthy participants (BeLong 4 T2w, EATT4MND 19 T2w, BMC 24 T1w) |
| [ToothFairy3](https://toothfairy3.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Publicly annotated CBCT scans with 77 anatomical classes (expanded from ToothFairy2's 42) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [HNC-IMRT-70-33](https://www.cancerimagingarchive.net/collection/hnc-imrt-70-33/) | CT | 2024 | 🟢 DICOM, CSV | — | ✅ | — | REQUEST | 211 patients / 211 studies / 844 series / 38,032 images; 23.27 GB |
| [HNTS-MRG 2024](https://hntsmrg24.grand-challenge.org/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | ~150 training patients (pre-RT and mid-RT), ~50 test patients |
| [Head Neck CBCT CT](https://zenodo.org/records/13231287) | CT | 2024 | 🟡 — | — | ✅ | — | OPEN | Paired planning CT and first-treatment-day CBCT scans; one 387.2 MB RAR archive (patient count not stated) |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [NPC MRI Multi-modality Segmentation](https://zenodo.org/records/13131827) | MRI | 2024 | 🟡 — | ✅ | ✅ | ✅ | OPEN | 277 patients; ~5.3 GB (primary_data.zip 4.6 GB, images.zip 718 MB) |
| [NasalSeg](https://zenodo.org/records/13893419) | CT | 2024 | 🟢 — | — | ✅ | — | OPEN | 130 CT scans; NasalSeg.zip 213.6 MB |
| [RADCURE](https://www.cancerimagingarchive.net/collection/radcure/) | CT | 2024 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 3,346 patients |
| [RPA-Head-and-Neck-Lymph-Nodes](https://www.cancerimagingarchive.net/collection/rpa-head-and-neck-lymph-nodes/) | CT | 2024 | 🟢 DICOM, RTSTRUCT | — | ✅ | — | DUA | 46 subjects, 46 studies, 92 series, 8,788 images (4.79 GB) |
| [VAREPOP-APOLLO](https://www.cancerimagingarchive.net/collection/varepop-apollo/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM | — | — | — | OPEN | 41 subjects, 279 studies, 1,549 series, 235,421 images (129.1 GB), version 3 |
| [ACRIN 6685-Tumor-Annotations](https://www.cancerimagingarchive.net/analysis-result/acrin-6685-tumor-annotations/) 🏷 | CT, PET, MRI | 2023 | 🟡 DICOM RTSTRUCT, CSV | — | ✅ | — | OPEN | 258 subjects / 481 studies / 2,085 RTSTRUCT series (37.59 MB); annotates 250 subjects with segmentations plus 16 with negative assessments |
| [CMB-MML](https://www.cancerimagingarchive.net/collection/cmb-mml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 177 subjects; ~50,000 radiology images + 1,071 pathology slides; 6.05 TB |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [HaN-Seg](https://han-seg2023.grand-challenge.org/) | CT, MRI | 2023 | 🟢 NRRD | — | ✅ | — | OPEN | 42 patients (paired CT and T1-weighted MR), 4.9 GB |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SegRap2023](https://segrap2023.grand-challenge.org/) | CT | 2023 | 🟢 NIfTI, MHA | — | ✅ | ✅ | DUA | 400 CT scans (200 patients, paired contrast-enhanced + non-contrast); 120 train, 20 validation, 60 test |
| [HECKTOR](https://hecktor.grand-challenge.org/) | PET, CT | 2022 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | ~882 cases (2022 edition) |
| [ACRIN-HNSCC-FDG-PET-CT](https://www.cancerimagingarchive.net/collection/acrin-hnscc-fdg-pet-ct/) | PET, CT, MRI | 2021 | 🟢 DICOM | ✅ | ✅ | — | DUA | 147.77 GB |
| [Vestibular-Schwannoma-SEG](https://www.cancerimagingarchive.net/collection/vestibular-schwannoma-seg/) | MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 28.21 GB |
| [HNSCC](https://www.cancerimagingarchive.net/collection/hnscc/) | CT, PET, MRI | 2020 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 627 patients |
| [AAPM-RT-MAC](https://www.cancerimagingarchive.net/collection/aapm-rt-mac/) | MRI | 2019 | 🟢 DICOM, DICOM RTSTRUCT | — | ✅ | — | DUA | 55 patients / 55 studies / 110 series / 6,655 images (3.52 GB) |
| [Crowds-Cure-2018](https://www.cancerimagingarchive.net/analysis-result/crowds-cure-2018/) 🏷 | CT | 2019 | 🟡 CSV, DICOM-SR | — | — | — | OPEN | 4,756 bi-directional lesion measurements on CT scans of 324 patients from 13 TCIA collections; label files 5.76 MB |
| [HN1](https://www.cancerimagingarchive.net/collection/head-neck-radiomics-hn1/) | CT | 2019 | 🟢 DICOM, RTSTRUCT, SEG | ✅ | ✅ | — | DUA | 137 patients |
| [OpenEar](https://zenodo.org/records/1473724) | CT | 2019 | 🟡 — | — | ✅ | — | OPEN | 8 human temporal bone datasets (ALPHA–THETA), ~55 GB total |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Four tasks; 50 training CT scans (+10 test) each for head-neck and chest cohorts |
| [CPTAC-HNSCC](https://www.cancerimagingarchive.net/collection/cptac-hnscc/) | CT, MRI, PET | 2018 | 🟢 DICOM | — | — | — | DUA | Radiology (v19): 156 subjects, 466 studies, 3,127 series, 460,097 images (246.08 GB); collection total 207 subjects incl. 390 pathology slides (97 GB) |
| [HNSCC-3DCT-RT](https://www.cancerimagingarchive.net/collection/hnscc-3dct-rt/) | CT | 2018 | 🟢 DICOM, XLS | — | ✅ | — | REQUEST | 31 patients / 93 studies / 371 series / 18,905 images (14.35 GB) |
| [MRI-DIR](https://www.cancerimagingarchive.net/collection/mri-dir/) | MRI, CT | 2018 | 🟢 DICOM, MATLAB | — | ✅ | ✅ | OPEN | 9 subjects, 25 studies, 61 series, 3,596 images (1.44 GB DICOM) + 64 deformation vector field files (1.7 GB); 3.14 GB total |
| [Head-Neck-PET-CT](https://www.cancerimagingarchive.net/collection/head-neck-pet-ct/) | PET, CT | 2017 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 298 patients |
| [Normal Male Head MRI (Lionheart)](https://zenodo.org/records/16956) | MRI | 2015 | 🟢 DICOM | — | — | ✅ | OPEN | 1 subject (normal male, aged 52); DICOM.zip 4.6 MB |
| [QIN-HeadNeck](https://www.cancerimagingarchive.net/collection/qin-headneck/) | PET, CT | 2015 | 🟢 DICOM, SEG, SR | ✅ | ✅ | — | REQUEST | 279 subjects |
| [TCGA-HNSC](https://www.cancerimagingarchive.net/collection/tcga-hnsc/) | CT, PET, MRI | 2014 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 227 patients (479 studies) |
| [TCGA-THCA](https://www.cancerimagingarchive.net/collection/tcga-thca/) | CT, PET | 2014 | 🟢 DICOM | — | — | — | OPEN | 6 subjects / 7 studies / 28 series / 2,780 images (1.15 GB) |
| [Head-Neck Cetuximab](https://www.cancerimagingarchive.net/collection/head-neck-cetuximab/) | PET, CT | 2013 | 🟢 DICOM | — | ✅ | — | REQUEST | 111 subjects / 368 studies / 1,682 series / 202,574 images (52.36 GB) |

### 🦷 Dental & Maxillofacial  <sub>(16)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [DOLCHID](https://springernature.figshare.com/articles/dataset/Dental_Odontogenic_Lesion_CBCT_and_Histopathology_Integrated_Dataset_for_Benchmarking_Deep_Learning_Algorithms/30156622) | CT | 2026 | 🟡 — | — | ✅ | — | OPEN | 262 patients (262 pre-operative CBCT scans + 262 paired H&E histopathology slides); DOLCHID.zip 39.7 GB |
| [DentIRO](https://figshare.com/articles/dataset/_b_DentIRO_b_A_High-Quality_Multi-Class_Single-Tooth_Intraoral_Radiograph_Dataset_for_Automated_Dental_Diagnosis/32086377) | X-ray | 2026 | 🟡 PNG | — | — | — | OPEN | 5,300 single-tooth intraoral radiographs / 3,243 patients; ~672 MB |
| [Dental CBCT Missing Teeth](https://doi.org/10.57760/sciencedb.26465) | CT | 2026 | 🟢 DICOM, JSON | — | — | — | OPEN | 158 full-arch CBCT volumes / 158 patients (59,978 slices); 501 missing-tooth sites, 114 sites in 85 volumes annotated (4,994 slices) |
| [InReDD-PAN924-Ext-BoneLoss-769](https://physionet.org/content/inredd-pan924-ext-boneloss-769/1.0.0/) | X-ray | 2026 | 🟡 JPEG, COCO JSON | — | ✅ | — | DUA | 769 panoramic radiographs; 21,047 polygon annotations |
| [AU-OPG](https://huggingface.co/datasets/YSFF/AU-OPG) | X-ray | 2025 | 🟡 JPEG, CSV | — | — | — | OPEN | 901 panoramic radiographs; 7,006 tooth-level annotations |
| [FDTooth](https://physionet.org/content/fdtooth/1.0.0/) | CT | 2025 | 🟢 DICOM, JPEG, CSV, JSON | — | — | — | DUA | 241 patients: 241 CBCT scans (DICOM) + 241 intraoral photographs (JPEG); 12 anterior teeth labelled per patient |
| [InReDD-Dataset-PAN924](https://physionet.org/content/inredd-dataset-pan924/1.0.0/) | X-ray | 2025 | 🟡 JPEG, JSON (COCO) | — | ✅ | — | REQUEST | 924 panoramic radiographs; 20,957 box annotations (924 mouth, 20,033 teeth); 4,621 tooth segmentation masks on 200 images |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [Panoramic_Radiographs_for_Dental_Condition](https://huggingface.co/datasets/ismaelportog/Panoramic_Radiographs_for_Dental_Condition) | X-ray | 2025 | 🟡 JPG, Parquet | — | — | — | OPEN | ~27,884 annotated rows / 1.42 GB (from ~1,808 source panoramic radiographs; 1,628 training + 180 external validation) |
| [ToothFairy3](https://toothfairy3.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Publicly annotated CBCT scans with 77 anatomical classes (expanded from ToothFairy2's 42) |
| [STS 2024](https://zenodo.org/records/17712688) | X-ray, CT | 2024 | 🟢 PNG, NIfTI | — | ✅ | — | OPEN | ~2,380 panoramic X-ray (OPG) images + ~330 CBCT scans; ~968 MB total on Zenodo |
| [ToothFairy2](https://toothfairy2.grand-challenge.org/) | CT | 2024 | 🟢 MHA | — | ✅ | — | REGISTRATION | 480 public training CBCT volumes |
| [DENTEX](https://dentex.grand-challenge.org/) | X-ray | 2023 | 🟡 PNG | — | — | — | OPEN | 1,005 fully-annotated panoramic X-rays (3,903 total) |
| [Multimodal Dental Dataset (PhysioNet)](https://physionet.org/content/multimodal-dental-dataset/) | CT, X-ray | 2023 | 🟢 DICOM, TIFF | — | — | — | DUA | 389 patients: 574 CBCT scans (DICOM), 13 panoramic radiographs (DICOM), 333 folders of 29,199 CBCT-derived simulated periapical radiographs (TIFF) from 240 patients (v1.0.0) |
| [CTooth](https://github.com/liangjiubujiu/CTooth) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 22 annotated CBCT volumes (CTooth+ adds 146 unlabeled) |
| [Tufts Dental Database](https://tdd.ece.tufts.edu/) | X-ray | 2022 | 🟡 JPG, TIFF | ✅ | ✅ | — | REQUEST | 1,000 panoramic X-rays |

### 🌐 Whole-Body & PET  <sub>(49)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [ViMed-PET-CT](https://huggingface.co/datasets/thainamhoang/ViMed-PET-CT) | PET, CT | 2026 | 🟡 NPZ | ✅ | — | — | OPEN | 304 studies, ~205 GB |
| [Visible Human 3D Bone Models](https://huggingface.co/datasets/BoneHub/visible-human-3d-models) | CT | 2026 | 🟢 NIfTI, NRRD, STL, IGES, STEP | — | ✅ | — | OPEN | 2 whole-body CT volumes (Visible Human Male and Female); 142 (male) and 143 (female) individually labeled bones |
| [Bone_metastases_pet_ct_for_BlueprINT](https://huggingface.co/datasets/FangDai/Bone_metastases_pet_ct_for_BlueprINT) | PET, CT | 2025 | 🟡 PNG | — | — | — | OPEN | 1,642 image samples |
| [CADS](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes; 167 anatomical structures; ~1.92 TB |
| [CADS-dataset](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes with segmentation masks (10K<n<100K files) |
| [Deep-PSMA](https://deep-psma.grand-challenge.org/) | PET, CT | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 100 training patients (~24.1 GB, NIfTI, on Zenodo); challenge also includes 10 preliminary validation and 40 test cases; single center (Peter MacCallum Cancer Centre) |
| [ENHANCE.PET 1.6k](https://registry.opendata.aws/enhance-pet-1-6k/) | PET, CT | 2025 | 🟢 NIfTI, XLSX | — | ✅ | — | OPEN | 1,597 whole-/total-body FDG-PET/CT studies; ~250 GB |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [autoPET IV](https://autopet-iv.grand-challenge.org/) | PET, CT | 2025 | 🟢 NIfTI | — | ✅ | — | OPEN | Longitudinal-CT: 300 melanoma patients x 2 timepoints, 57.2 GB; plus multi-tracer whole-body PET/CT cohort from prior autoPET editions |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [PSMA-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/psma-pet-ct-lesions/) | PET, CT | 2024 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 597 studies / 378 patients |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [autoPET III](https://autopet-iii.grand-challenge.org/) | PET, CT | 2024 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 1,611 studies (1,014 FDG + 597 PSMA) |
| [CMB-AML](https://www.cancerimagingarchive.net/collection/cmb-aml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 448.08 GB, 16 subjects |
| [CMB-MML](https://www.cancerimagingarchive.net/collection/cmb-mml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 177 subjects; ~50,000 radiology images + 1,071 pathology slides; 6.05 TB |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [FDG-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/) | PET, CT | 2022 | 🟢 DICOM | — | ✅ | — | DUA | 1,014 studies / 900 patients |
| [NAKO](https://transfer.nako.de/transfer/) | MRI | 2022 | 🟢 DICOM | — | — | ✅ | REQUEST | ~30,000 imaging participants (of 205,000 total cohort) |
| [autoPET I](https://autopet.grand-challenge.org/) | PET, CT | 2022 | 🟢 DICOM, NIfTI | — | ✅ | — | DUA | 1,014 studies / 900 patients (FDG) |
| [Pediatric-CT-SEG](https://www.cancerimagingarchive.net/collection/pediatric-ct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | — | OPEN | 359 patients (ages 5 days to 16 years); 65.69 GB |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [Anti-PD-1_Melanoma](https://www.cancerimagingarchive.net/collection/anti-pd-1_melanoma/) | PET, CT, MRI | 2018 | 🟢 DICOM | ✅ | — | — | REQUEST | 98.41 GB |
| [Generation R](https://generationr.nl/researchers/) | MRI, DXA | 2018 | 🟢 DICOM, derived | — | — | ✅ | REQUEST | ~several thousand children with repeated brain MRI and DXA (birth cohort of ~9,700 mothers/children) |
| [KORA-MRI](https://www.helmholtz-munich.de/en/epi/cohort/kora) | MRI | 2016 | 🟢 DICOM | — | — | ✅ | DUA | ~400 participants (whole-body MRI sub-study of KORA-FF4) |
| [Tromsø Study](https://uit.no/research/tromsostudy) | DXA, MRI | 2016 | 🟢 derived, DICOM | — | — | ✅ | REQUEST | Tens of thousands of participants across seven survey waves (DXA and brain MRI collected in sub-samples) |
| [ALSPAC](http://www.bristol.ac.uk/alspac/researchers/access/) | DXA, MRI | 2015 | 🟢 derived, DICOM, NIfTI | — | — | ✅ | REQUEST | ~14,000 index children (thousands with repeated DXA; ~900 with brain MRI at 18-24y) |
| [Insight 46 (MRC NSHD 1946 birth cohort)](https://www.nshd.mrc.ac.uk/data/) | MRI, PET, DXA | 2015 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~500 imaged participants (Insight 46); ~5,300 in the NSHD birth cohort |
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | MRI, DXA | 2014 | 🟢 DICOM, NIfTI, derived phenotypes (TSV) | — | — | ✅ | REQUEST | ~100,000 participants imaged; abdominal MRI-derived phenotypes for 40,000+ |
| [Qatar Biobank](https://www.qphi.org.qa/research/how-to-apply) | DXA, Ultrasound | 2012 | 🟡 derived | — | — | — | REQUEST | ~60,000 participants target (DXA and carotid ultrasound on examination subsets) |
| [SHIP](https://www.fvcm.med.uni-greifswald.de/) | MRI | 2012 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,300 whole-body MRI participants (SHIP-2 and SHIP-TREND); ~15,000 total cohort participants |
| [GUSTO](https://www.gusto.sg/) | MRI, DXA, CT | 2009 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~1,200 mother-offspring pairs |
| [RabbitCT](https://zenodo.org/records/21267885) | CT | 2009 | 🟡 RCTD (custom projection format), VOL (float32 volume) | — | — | — | OPEN | 1 C-arm cone-beam CT scan: 496 projections with calibrated 3x4 projection matrices (512³ and 1024³ targets) plus a 256³ reference reconstruction; ~7 GB |
| [Rotterdam Study](https://www.ergo-onderzoek.nl) | MRI, DXA | 2005 | 🟢 DICOM, derived | — | ✅ | ✅ | REQUEST | ~20,000 participants aged 40+ enrolled overall; ~5,000+ with repeated brain MRI |
| [CoLaus \| PsyCoLaus](https://www.colaus-psycolaus.ch/professionals/) | MRI, DXA | 2003 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | REQUEST | ~6,700 baseline participants; imaging sub-studies (BrainLaus, OsteoLaus) on subsets |
| [CARDIA](https://biolincc.nhlbi.nih.gov/studies/cardia/) | CT, MRI, DXA | 2000 | 🟢 DICOM, derived | ✅ | ✅ | ✅ | DUA | 5,115 participants enrolled (1985-86); imaging performed in subsets or the full cohort across follow-up exams |
| [MrOS](https://mrosonline.ucsf.edu/) | CT, DXA, X-ray | 2000 | 🟢 DICOM, derived | — | ✅ | — | DUA | 5,994 men (aged 65+) |
| [NHANES DXA](https://wwwn.cdc.gov/nchs/nhanes/dxa/dxa.aspx) | DXA | 1999 | 🟡 derived | ✅ | — | — | OPEN | ~30,000+ participants with whole-body DXA (1999-2006 cycles); additional femur/spine bone-density and visceral-fat DXA in later cycles |
| [Health ABC](https://agingresearchbiobank.nia.nih.gov/studies/healthabc/) | CT, DXA | 1997 | 🟢 DICOM, derived | — | ✅ | — | DUA | 3,075 older adults (aged 70-79 at baseline) |
| [BLSA](https://www.blsa.nih.gov/how-apply) | MRI, PET, DXA | 1994 | 🟢 DICOM | — | — | ✅ | REQUEST | ~3,000+ active participants with serial imaging (study cohort >3,200 enrolled since 1958) |
| [NLM Visible Human Project](https://zenodo.org/records/16114440) | CT, MRI | 1994 | 🟢 DICOM | — | — | — | OPEN | 2 cadavers (1 male, 1 female); cryosection, CT and MRI images |
| [Raine Study](https://rainestudy.org.au/) | MRI, DXA | 1989 | 🟢 DICOM, NIfTI, derived | — | — | ✅ | DUA | ~2,900 Gen2 offspring (born 1989-1991) plus Gen1 parents and Gen3 grandchildren |
| [SOF](https://sofonline.ucsf.edu/) | DXA, CT, X-ray | 1986 | 🟢 DICOM, derived | — | — | — | DUA | 9,704 older women (plus ~662 Black women in a later supplement) |
| [Fenland Study](https://studies.epi.ims.cam.ac.uk/fenland/data-sharing) | DXA | — | 🟡 derived | — | — | — | REQUEST | ~12,435 participants |

### 🧩 Multiple / Various body parts  <sub>(49)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [EAY131](https://www.cancerimagingarchive.net/collection/eay131/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM | — | — | — | OPEN | 2,813 subjects / 3,124 studies / 14,494 series / 1,435,665 images; 796.15 GB |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [RadRepro CBCT](https://zenodo.org/records/18401318) | CT | 2026 | 🟡 — | — | ✅ | — | OPEN | 120 CBCT image volumes of a Catphan phantom (CBCT_Data.zip, 2.3 GB) |
| [ViMed-PET-CT](https://huggingface.co/datasets/thainamhoang/ViMed-PET-CT) | PET, CT | 2026 | 🟡 NPZ | ✅ | — | — | OPEN | 304 studies, ~205 GB |
| [CADS-dataset](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes with segmentation masks (10K<n<100K files) |
| [CVPR-BiomedSegFM](https://huggingface.co/datasets/junma/CVPR-BiomedSegFM) | CT, MRI, PET | 2025 | 🟡 NPZ | ✅ | ✅ | — | OPEN | 340 GB total (preprocessed npz); 3D_train_npz_all plus a 10% (16 GB) coreset subset, validation set |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [GMAI-VL-5.5M](https://huggingface.co/datasets/General-Medical-AI/GMAI-VL-5.5M) | CT, MRI, X-ray | 2025 | 🟡 JSONL | ✅ | — | — | OPEN | ~5.5M QA pairs: 1.7M captions, 0.9M instruction QA and 1.3M perception labels (multimodal), plus 1.7M text-only QA; only part of the multimodal pairs ship with redistributable images |
| [MIDI-B](https://www.cancerimagingarchive.net/collection/midi-b-test-midi-b-validation/) | CT, MRI, PET, X-ray | 2025 | 🟢 DICOM | — | — | — | OPEN | 538 subjects, 71.07 GB; synthetic validation 216 subjects / 280 series / 23,921 images; synthetic test 322 subjects / 428 series / 29,660 images; plus TCIA-curated versions of both |
| [MedVH](https://physionet.org/content/medvh/1.0.0/) | X-ray, CT, MRI | 2025 | 🟡 JPEG, JSON | ✅ | — | — | DUA | 5 MC-VQA hallucination tasks (500 questions each for Wrongful Image, None Of The Above, False Confidence Justification, Abnormality Detection and Clinically Incorrect Question) plus 200 MIMIC-CXR report-generation samples, with matching baseline test sets |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PCCT/DECT Phantom Dose Levels](https://zenodo.org/records/17119205) | CT | 2025 | 🟢 DICOM | — | — | ✅ | OPEN | PCCT: 270 series / 42,029 DICOM images (~29.7 GB unzipped); DECT: 267 series / 24,243 DICOM images (~13.0 GB unzipped); ~19.8 GB zipped |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [M3D-Seg](https://huggingface.co/datasets/GoodBaiBai88/M3D-Seg) | CT | 2024 | 🟡 NPY, NPZ, JSON | ✅ | ✅ | — | OPEN | ~5,772 3D CT images with 149,196 3D mask annotations (~240 GB), aggregated from 25 datasets |
| [MedMNIST+](https://zenodo.org/records/10519652) | X-ray, CT | 2024 | 🟡 NPZ | — | — | — | OPEN | ~708K 2D images and ~10K 3D images across 18 datasets (12 2D, 6 3D); sizes 28/64/128/224 px (2D) and 28/64 voxels (3D) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [MedTrinity-25M](https://huggingface.co/datasets/UCSC-VLAA/MedTrinity-25M) | CT, MRI, X-ray | 2024 | 🟡 JPEG, PNG | ✅ | ✅ | — | REGISTRATION | ~25M images (18M accessible image-text pairs) across 10 modalities |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [ROCOv2](https://doi.org/10.5281/zenodo.10821435) | X-ray, CT, MRI, PET | 2024 | 🟡 JPG | ✅ | — | — | OPEN | 79,789 images with captions and UMLS concepts |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [CMB-AML](https://www.cancerimagingarchive.net/collection/cmb-aml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 448.08 GB, 16 subjects |
| [PDMR-Texture-Analysis](https://www.cancerimagingarchive.net/collection/pdmr-texture-analysis/) | MRI | 2023 | 🟢 DICOM | — | — | — | OPEN | 175 mice, 18 PDX models; 689 studies, 1,203 series, 19,343 images (11.78 GB) |
| [PMC-OA](https://huggingface.co/datasets/axiong/pmc_oa) | X-ray, CT, MRI, PET | 2023 | 🟡 JPG | ✅ | — | — | OPEN | 1.6 million image-caption pairs |
| [PMC-VQA](https://huggingface.co/datasets/xmcmic/PMC-VQA) | CT, MRI, X-ray | 2023 | 🟡 JPEG, CSV | ✅ | — | — | OPEN | ~149K images, ~227K question-answer pairs (21.8 GB) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [ULS23](https://uls23.grand-challenge.org/) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | ~38,000 lesion VOIs across multi-part release; e.g. Part 1 = 1,618 lesions, 15.9 GB |
| [RadImageNet](https://www.radimagenet.com/) | CT, MRI | 2022 | 🟡 DICOM, PNG | — | — | — | REQUEST | ~1.35 million annotated images from 131,000+ patients (CT, MRI, ultrasound) |
| [COVID-19-NY-SBU](https://www.cancerimagingarchive.net/collection/covid-19-ny-sbu/) | X-ray, CT, MRI, PET | 2021 | 🟢 DICOM, CSV | — | — | — | OPEN | 1,384 patients / 7,361 studies / 17,950 series / 562,376 images; 511.48 GB |
| [Pseudo-PHI-DICOM-Data](https://www.cancerimagingarchive.net/collection/pseudo-phi-dicom-data/) | CT, MRI, PET, X-ray | 2021 | 🟢 DICOM, CSV | — | — | — | OPEN | 21 patients, 22 studies, 26 series, 1,693 images in each of two versions (evaluation and de-identified); 1.24 GB |
| [SLAKE](https://www.med-vqa.com/slake/) | X-ray, CT, MRI | 2021 | 🟡 PNG | ✅ | ✅ | — | OPEN | 642 images with 14,028 QA pairs |
| [VinDr-BodyPartXR](https://vindr.ai/datasets/bodypartxr) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 16,093 X-ray images |
| [MedICaT](https://github.com/allenai/medicat) | X-ray, CT, MRI | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 217,060 figures from 131,410 papers |
| [CC-Radiomics-Phantom-2](https://www.cancerimagingarchive.net/collection/cc-radiomics-phantom-2/) | CT | 2019 | 🟢 DICOM | — | — | — | OPEN | 251 CT scans (251 series, 57,839 images); 30.48 GB |
| [CC-Radiomics-Phantom-3](https://www.cancerimagingarchive.net/collection/cc-radiomics-phantom-3/) | CT | 2019 | 🟢 DICOM, XLSX | — | ✅ | — | OPEN | 95 subjects (phantom scan sets), 113 studies, 550 series, 25,612 images; 13.44 GB |
| [CPTAC-AML](https://www.cancerimagingarchive.net/collection/cptac-aml/) | CT | 2019 | 🟢 DICOM, SVS, CSV | — | — | — | OPEN | Radiology (CT, US): 5 subjects, 9 studies, 47 series, 4,108 DICOM images (2.51 GB); pathology: 273 whole-slide images from 180 subjects (1.02 TB) |
| [CPTAC-SAR](https://www.cancerimagingarchive.net/collection/cptac-sar/) | CT, MRI, PET | 2019 | 🟢 DICOM | — | — | — | OPEN | Radiology: 24 subjects, 33 studies, 265 series, 29,595 images (15.2 GB); plus 300 whole-slide pathology images from 88 subjects (72 GB) |
| [CPTAC-CM](https://www.cancerimagingarchive.net/collection/cptac-cm/) | CT, MRI, PET | 2018 | 🟢 DICOM | — | — | — | OPEN | Radiology: 18 subjects, 24 studies, 264 series, 52,368 images (25.82 GB); plus 777 whole-slide pathology images from 182 subjects (335.5 GB) |
| [DeepLesion](https://nihcc.app.box.com/v/DeepLesion) | CT | 2018 | 🟡 PNG | — | — | — | OPEN | 32,735 lesions on 32,120 CT slices from 4,427 patients (~225 GB) |
| [ROCO](https://github.com/razorx89/roco-dataset) | X-ray, CT, MRI, PET | 2018 | 🟡 JPG, PNG | ✅ | — | — | OPEN | ~81,000 radiology image-caption pairs |
| [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) | X-ray, CT, MRI | 2018 | 🟡 JPG | ✅ | — | — | OPEN | 315 images with 3,515 QA pairs |
| [QIN PET Phantom](https://www.cancerimagingarchive.net/collection/qin-pet-phantom/) | PET | 2014 | 🟢 DICOM | — | — | — | OPEN | 2 phantom subjects (2 sites), 4 studies, 44 series, 2,816 images; 246.31 MB |
| [RIDER PHANTOM MRI](https://www.cancerimagingarchive.net/collection/rider-phantom-mri/) | MRI | 2011 | 🟢 DICOM, PDF | — | — | — | OPEN | 10 subjects (phantom), 13 studies, 45 series, 7,061 images; 3.6 GB |
| [RIDER PHANTOM PET-CT](https://www.cancerimagingarchive.net/collection/rider-phantom-pet-ct/) | PET, CT | 2011 | 🟢 DICOM, DOC | — | — | — | OPEN | 20 phantom scans / 20 studies / 60 series / 2,231 images (~724 MB) |

### 🗄️ Data Repositories & Portals  <sub>(15)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [Stanford AIMI](https://aimi.stanford.edu/shared-datasets) | Multiple | 2021 | 🟢 Various | ✅ | ✅ | — | REGISTRATION | 30+ curated medical imaging datasets |
| [BIMCV](https://bimcv.cipf.es/bimcv-projects/) | X-ray, CT | 2020 | 🟢 DICOM, PNG, NIfTI | ✅ | — | — | REGISTRATION | PadChest ~160,000 CXR images from ~67,000 patients; BIMCV-COVID19+ tens of thousands of CXR/CT studies |
| [IDC](https://portal.imaging.datacommons.cancer.gov/) | Multiple | 2020 | 🟢 Various | — | ✅ | — | OPEN | 85+ TB across many collections |
| [MIDRC](https://www.midrc.org/) | X-ray, CT, MRI | 2020 | 🟢 DICOM | — | — | — | DUA | hundreds of thousands of imaging studies across tens of thousands of patients |
| [AWS Open Data](https://registry.opendata.aws/) | Multiple | 2018 | 🟢 Various | — | — | — | OPEN | hundreds of datasets (incl. medical imaging) |
| [Medical Segmentation Decathlon](http://medicaldecathlon.com/) | CT, MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 10 tasks / ~2,600 3D volumes |
| [OpenNeuro](https://openneuro.org/) | Multiple | 2017 | 🟢 Various | — | — | ✅ | OPEN | 1,000+ datasets |
| [Hugging Face](https://huggingface.co/datasets) | Multiple | 2016 | 🟢 Various | ✅ | — | — | OPEN | thousands of medical/imaging datasets |
| [Zenodo](https://zenodo.org/) | Multiple | 2013 | 🟢 Various | — | — | — | OPEN | millions of records (general-purpose) |
| [Grand Challenge](https://grand-challenge.org/) | Multiple | 2011 | 🟢 Various | — | ✅ | — | REGISTRATION | 390+ public and private challenges |
| [Synapse](https://www.synapse.org/) | Multiple | 2011 | 🟢 Various | — | — | — | REGISTRATION | thousands of projects and datasets |
| [Kaggle Datasets](https://www.kaggle.com/datasets) | Multiple | 2010 | 🟢 Various | — | — | — | REGISTRATION | hundreds of thousands of public datasets |
| [TCIA](https://www.cancerimagingarchive.net/) | Multiple | 2010 | 🟢 Various | — | — | — | OPEN | 200+ collections |
| [Radiopaedia](https://radiopaedia.org/) | Multiple | 2005 | 🟡 Various | ✅ | — | ✅ | OPEN | 50,000+ cases, 900,000+ images |
| [PhysioNet](https://physionet.org/) | Multiple | 1999 | 🟢 Various | ✅ | — | — | REGISTRATION | 200+ databases |

<!-- AUTOGEN:END -->

---

## Contributing

Found a dataset we're missing, or a field that's wrong? See [CONTRIBUTING.md](CONTRIBUTING.md).
Edit [`data/datasets.json`](data/datasets.json), run `python3 scripts/validate.py` and
`python3 scripts/generate_readme.py`, and open a PR.

## Related projects

- [sfikas/medical-imaging-datasets](https://github.com/sfikas/medical-imaging-datasets) — broad medical imaging list
- [uni-medical/Project-Imaging-X](https://github.com/uni-medical/Project-Imaging-X) — 1000+ dataset survey
- [linhandev/dataset](https://github.com/linhandev/dataset) — large medical imaging index
- [open-dicom/awesome-dicom](https://github.com/open-dicom/awesome-dicom) — DICOM tooling

## Disclaimer

This catalog links to third-party datasets and summarizes their metadata for convenience.
**Always review each dataset's own license and data-use agreement before downloading or using it.**
Metadata is provided as-is and may contain errors — please [report corrections](../../issues).

Catalog content is licensed [CC BY 4.0](LICENSE). Individual datasets retain their own licenses.
