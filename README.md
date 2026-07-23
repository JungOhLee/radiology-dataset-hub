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

**383 curated datasets** · 188 CT · 180 MRI · 43 PET · 90 X-ray · 319 native DICOM/NIfTI · 90 with reports/text · 240 with segmentation labels

Jump to: [Neuro (Brain & Spine)](#neuro-brain-spine) · [Chest & Thorax](#chest-thorax) · [Cardiac](#cardiac) · [Vascular](#vascular) · [Abdominal](#abdominal) · [Pelvic & Prostate](#pelvic-prostate) · [Musculoskeletal](#musculoskeletal) · [Breast](#breast) · [Head & Neck](#head-neck) · [Dental & Maxillofacial](#dental-maxillofacial) · [Whole-Body & PET](#whole-body-pet) · [Multiple / Various body parts](#multiple-various-body-parts) · [Data Repositories & Portals](#data-repositories-portals)

**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). Text = paired reports/captions/QA (i.e. image–text / multimodal) · Seg = segmentation masks · Multi = multi-sequence MRI or multi-phase CT. Access: OPEN = direct download · REGISTRATION = free account · DUA = data-use agreement · REQUEST = apply for access. **Datasets covering several body regions (56) appear under each region.**

### 🧠 Neuro (Brain & Spine)  <sub>(103)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CFB-GBM](https://www.cancerimagingarchive.net/collection/cfb-gbm/) | MRI, CT | 2026 | 🟢 NIfTI, TSV | ✅ | ✅ | ✅ | OPEN | 208.01 GB; 264 patients |
| [BRISC2025](https://www.kaggle.com/datasets/briscdataset/brisc2025) | MRI | 2025 | 🟡 JPG | — | ✅ | — | OPEN | 6,000 contrast-enhanced T1-weighted MRI images across axial, sagittal, and coronal planes |
| [Brain-Mets-Lung-MRI-Path-Segs](https://www.cancerimagingarchive.net/collection/brain-mets-lung-mri-path-segs/) | MRI | 2025 | 🟢 NIfTI, SVS, XLSX | ✅ | ✅ | ✅ | OPEN | 19.21 GB; 103 patients (111 imaging-pathology pairs) |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MR-RATE](https://huggingface.co/datasets/Forithmus/MR-RATE) | MRI | 2025 | 🟢 NIfTI, CSV | ✅ | ✅ | ✅ | REGISTRATION | 705,254 MRI volumes from 98,334 studies of 83,425 patients (~8-38 TB across repositories) |
| [MU-Glioma-Post](https://www.cancerimagingarchive.net/collection/mu-glioma-post/) | MRI | 2025 | 🟢 NIfTI, XLSX | ✅ | ✅ | ✅ | OPEN | 11 GB; 203 patients (596 timepoints) |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [OpenMind](https://huggingface.co/datasets/AnonRes/OpenMind) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | OPEN | ~114K MRI images (1.04 TB) curated from 800 OpenNeuro datasets across 30+ scanners |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RSNA 2025 Aneurysm Detection](https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection) | CT, MRI | 2025 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 4,000+ studies (CTA/MRA/MRI); ~200 with segmentation |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [Spine Generic (Multi-Subject)](https://github.com/spine-generic/data-multi-subject) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | ~260+ subjects, ~26 GB, 40+ sites |
| [TopBrain 2025](https://topbrain2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Batches 1-2 on Zenodo: 50 angiographic scans (25 paired CTA/MRA subjects), ~2.0 GB; 40 CTA / 42 MRA vessel labels (34 overlapping) |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [APIS](https://bivl2ab.uis.edu.co/challenges/apis) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 100 studies (60 train / 40 test) |
| [BONBID-HIE 2024](https://bonbid-hie2024.grand-challenge.org/) | MRI | 2024 | 🟢 MHA | — | ✅ | ✅ | OPEN | Labeled MGH cohort (~133 patients on base record) plus unlabeled BCH cohort; 44 test cases (Track 1 segmentation), 53 test cases (Track 2 outcome prediction), 4 validation cases per track |
| [BraTS 2024 Post-Treatment Glioma (BraTS-GLI)](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2200 multi-institutional post-treatment MRI cases |
| [BraTS-GoAT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | Pooled multi-tumor BraTS cohort (thousands of cases across glioma, meningioma, metastases, pediatric) |
| [BraTS-MEN-RT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 750 radiotherapy-planning brain MRIs (multi-institutional) with expert GTV annotations on the training/validation partitions |
| [COSTA](https://doi.org/10.5281/zenodo.11025761) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REQUEST | 423 TOF-MRA volumes across 8 centers (4 vendors, 1.5T/3.0T) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [ISLES 2024](https://isles-24.grand-challenge.org/) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~150 training cases |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MSLesSeg 2024](https://iplab.dmi.unict.it/mfs/ms-les-seg/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~90 patients, ~150 MRI timepoints (1-5 per patient) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [UCSF-ALPTDG](https://imagingdatasets.ucsf.edu/dataset/2) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 298 patients; 596 post-treatment MRI exams (two consecutive posttreatment timepoints per patient) |
| [BONBID-HIE](https://zenodo.org/records/8104103) | MRI | 2023 | 🟢 MHA | — | ✅ | ✅ | OPEN | 133 neonates |
| [BraTS-Africa](https://www.cancerimagingarchive.net/collection/BraTS-Africa/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 146 patients |
| [BraTS-MEN](https://www.synapse.org/Synapse:syn51514106) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 1,650 cases (1,000 public training) |
| [BraTS-Mets](https://www.synapse.org/Synapse:syn51156910/wiki/622553) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 328 cases (238 public training) |
| [BraTS-PEDs](https://www.synapse.org/Synapse:syn51156910/wiki/622461) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 228 patients (99 public training) |
| [Burdenko-GBM-Progression](https://www.cancerimagingarchive.net/collection/burdenko-gbm-progression/) | CT, MRI | 2023 | 🟢 DICOM | — | ✅ | ✅ | DUA | 180 patients; 645 studies; 4,956 series; 344,003 images; 131.23 GB |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [M4Raw](https://github.com/mylyu/M4Raw) | MRI | 2023 | 🟡 HDF5 | — | — | ✅ | OPEN | — |
| [Meningioma-SEG-CLASS](https://www.cancerimagingarchive.net/collection/meningioma-seg-class/) | MRI | 2023 | 🟢 DICOM, XLSX | — | ✅ | ✅ | DUA | 96 patients (180 studies, 674 series, 47,520 images, 9.39 GB) |
| [Pretreat-MetsToBrain-Masks](https://www.cancerimagingarchive.net/collection/pretreat-metstobrain-masks/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 200 subjects (1000 studies), 1.7 GB |
| [Queensland Twin Adolescent Brain (QTAB)](https://openneuro.org/datasets/ds004146) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | OPEN | 417 subjects (twin pairs), ~683 GB, 27718 files; two timepoints |
| [RHUH-GBM](https://www.cancerimagingarchive.net/collection/rhuh-gbm/) | MRI | 2023 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 40 patients; ~600 series, 37,425 DICOM images (15.96 GB) plus 2.9 GB NIfTI |
| [ReMIND](https://www.cancerimagingarchive.net/collection/remind/) | MRI | 2023 | 🟢 DICOM, NRRD | ✅ | ✅ | ✅ | OPEN | 114 subjects; 43.6 GB (preop MRI 4 sequences, 301 intraop MRI series, 320 intraop 3D US series) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SMILE-UHURA](https://osf.io/jg7cr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | ~14 annotated training subjects (7T ToF-MRA volumes) plus held-out test set |
| [SynthRAD2023](https://synthrad2023.grand-challenge.org/) | MRI, CT | 2023 | 🟢 MHA | — | — | — | OPEN | 540 paired MRI-CT and 540 CBCT-CT sets (>500 patients per task) from three centers |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [crossMoDA 2023](https://crossmoda-challenge.ml/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [ATLAS R2.0](https://atlas.grand-challenge.org/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 655 labeled T1w MRIs (+300 hidden test) |
| [Developing Human Connectome Project (dHCP)](http://www.developingconnectome.org/data-release/) | MRI | 2022 | 🟢 NIfTI, BIDS | — | ✅ | ✅ | DUA | ~783 neonates (886 datasets) and ~273 fetuses (4th release) |
| [INSTANCE 2022](https://instance.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 NCCT scans (100 train) |
| [ISLES 2022](https://zenodo.org/records/7153326) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 250 training cases |
| [LUMIERE](https://springernature.figshare.com/articles/dataset/The_LUMIERE_Dataset/16944846) | MRI | 2022 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 91 patients, 638 study dates, 2487 MRI images (~32.5 GB imaging ZIP) |
| [RSNA 2022 Cervical Spine Fracture](https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection) | CT | 2022 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~3,000 CT studies |
| [Shifts MS](https://zenodo.org/records/7051658) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [UCSF-PDGM](https://www.cancerimagingarchive.net/collection/ucsf-pdgm/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 495 patients |
| [UPenn-GBM](https://www.cancerimagingarchive.net/collection/upenn-gbm/) | MRI | 2022 | 🟢 NIfTI, DICOM | — | ✅ | ✅ | OPEN | 630 glioblastoma patients |
| [BraTS 2021](https://www.synapse.org/Synapse:syn25829067) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2,040 patients (1,251 public training) |
| [FeTA](https://www.synapse.org/Synapse:syn25649159) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | DUA | ~80 subjects (FeTA 2021) |
| [FeTS 2021/2022](https://fets-ai.github.io/Challenge/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [GLIS-RT](https://www.cancerimagingarchive.net/collection/glis-rt/) | CT, MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 230 patients (28.26 GB) |
| [MSSEG-2](https://portal.fli-iam.irisa.fr/msseg-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 patients, 2 time-points each |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [Vestibular-Schwannoma-SEG](https://www.cancerimagingarchive.net/collection/vestibular-schwannoma-seg/) | MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 28.21 GB |
| [ADAM](https://adam.isi.uu.nl/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 113 training TOF-MRA cases |
| [CADA](https://cada.grand-challenge.org/) | X-ray | 2020 | 🟢 NIfTI, STL | — | ✅ | — | REGISTRATION | 131 3DRA datasets (115 patients) |
| [CT-ICH (PhysioNet)](https://physionet.org/content/ct-ich/1.3.1/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | DUA | 82 non-contrast head CT scans (75 public in NIfTI); 36 with hemorrhage |
| [EPISURG](https://rdr.ucl.ac.uk/articles/dataset/EPISURG/9996158) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 430 postoperative T1w MRIs |
| [MOOD](https://www.synapse.org/mood) | MRI, CT | 2020 | 🟢 NIfTI | — | — | — | REGISTRATION | ~800 brain MRI + ~600 abdominal CT scans |
| [VerSe](https://github.com/anjany/verse) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 374 CT scans / ~4,500 vertebrae |
| [fastMRI Brain](https://fastmri.med.nyu.edu) | MRI | 2020 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | 6,970 brain MRI volumes |
| [ACRIN-FMISO-Brain](https://www.cancerimagingarchive.net/collection/acrin-fmiso-brain/) | PET, MRI, CT | 2019 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 96 GB |
| [OASIS-3](https://sites.wustl.edu/oasisbrains/) | MRI, PET | 2019 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 1378 participants |
| [RSNA 2019 ICH Detection](https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection) | CT | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 25,272 non-contrast head CT exams |
| [iSeg](https://iseg2019.web.unc.edu) | MRI | 2019 | 🟢 Analyze | — | ✅ | ✅ | DUA | iSeg-2019: 39 subjects (multi-site) |
| [ABCD Study](https://nda.nih.gov/abcd) | MRI | 2018 | 🟢 NIfTI, DICOM | — | — | ✅ | DUA | ~11,880 children |
| [Brain-Tumor-Progression](https://www.cancerimagingarchive.net/collection/brain-tumor-progression/) | MRI | 2018 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 3.16 GB |
| [CPTAC-GBM](https://www.cancerimagingarchive.net/collection/cptac-gbm/) | MRI, CT | 2018 | 🟢 DICOM | — | — | ✅ | REGISTRATION | 41.1 GB radiology (192.6 GB with histopathology) |
| [CQ500](http://headctstudy.qure.ai/dataset) | CT | 2018 | 🟢 DICOM | — | — | — | OPEN | 491 head CT scans |
| [Calgary-Campinas CC-359](https://www.ccdataset.com) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 359 T1w volumes (+ raw k-space subset) |
| [MRBrainS](https://mrbrains18.isi.uu.nl) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | MRBrainS18: 30 subjects (7 fully annotated) |
| [MRI of 3-12 year old children (Pixar)](https://openneuro.org/datasets/ds000228) | MRI | 2018 | 🟢 NIfTI | — | — | ✅ | OPEN | 155 subjects (122 children, 33 adults) |
| [Brain Tumor Dataset (figshare)](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427) | MRI | 2017 | 🟡 MAT | — | ✅ | — | OPEN | 3,064 T1-CE MRI slices from 233 patients |
| [CRL Fetal Brain Atlas](http://crl.med.harvard.edu/research/fetal_brain_atlas/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | — | OPEN | Atlas derived from MRI of 81 healthy fetuses (19-39 GA weeks); per-gestational-week template and label volumes (~weeks 21-38) |
| [HCP Young Adult](https://www.humanconnectome.org/study/hcp-young-adult) | MRI | 2017 | 🟢 NIfTI, CIFTI | — | ✅ | ✅ | REGISTRATION | 1206 subjects |
| [Healthy Brain Network (HBN)](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/) | MRI | 2017 | 🟢 NIfTI, BIDS | — | — | ✅ | DUA | 5,000+ target subjects; thousands of MRI datasets released (8,000+ total participants enrolled) |
| [LGG-1p19qDeletion](https://www.cancerimagingarchive.net/collection/lgg-1p19qdeletion/) | MRI | 2017 | 🟢 DICOM, NIfTI | ✅ | ✅ | ✅ | OPEN | 2.8 GB |
| [M-CRIB](https://github.com/DevelopmentalImagingMCRI/M-CRIB_atlas) | MRI | 2017 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 10 neonates (individual images plus group T1/T2 templates) |
| [WMH Segmentation Challenge](https://wmh.isi.uu.nl/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 60 training subjects |
| [IvyGAP](https://www.cancerimagingarchive.net/collection/ivygap/) | MRI | 2016 | 🟢 DICOM | ✅ | — | ✅ | OPEN | 139.98 GB |
| [Cam-CAN](https://www.cam-can.org/) | MRI | 2015 | 🟢 NIfTI | — | — | ✅ | DUA | ~700 subjects |
| [REMBRANDT](https://www.cancerimagingarchive.net/collection/rembrandt/) | MRI | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 10.59 GB |
| [TCGA-GBM](https://www.cancerimagingarchive.net/collection/tcga-gbm/) | MRI, CT, X-ray | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 73.51 GB |
| [TCGA-LGG](https://www.cancerimagingarchive.net/collection/tcga-lgg/) | MRI, CT | 2014 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 42.92 GB |
| [ABIDE](https://fcon_1000.projects.nitrc.org/indi/abide/) | MRI | 2012 | 🟢 NIfTI | — | — | ✅ | REGISTRATION | 1112 subjects (ABIDE I) |
| [Mindboggle-101](https://mindboggle.info/data.html) | MRI | 2012 | 🟢 NIfTI, VTK | — | ✅ | — | OPEN | 101 subjects |
| [Neonatal Brain Atlases (ALBERTs / Gousias)](https://brain-development.org/brain-atlases/neonatal-brain-atlases/) | MRI | 2012 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 20 neonates, 50 labeled regions each (with corresponding T1/T2 MRI scans) |
| [ADHD-200](https://fcon_1000.projects.nitrc.org/indi/adhd200/) | MRI | 2011 | 🟢 NIfTI | — | — | ✅ | OPEN | 973 subjects (8 sites) |
| [AIBL](https://aibl.org.au/) | MRI, PET | 2011 | 🟢 DICOM, NIfTI | — | — | ✅ | DUA | — |
| [PPMI](https://www.ppmi-info.org/) | MRI, PET | 2011 | 🟢 DICOM, NIfTI | — | — | ✅ | DUA | — |
| [OASIS-2](https://sites.wustl.edu/oasisbrains/) | MRI | 2010 | 🟢 Analyze, NIfTI | ✅ | — | — | DUA | 150 subjects, 373 imaging sessions |
| [OASIS-1](https://sites.wustl.edu/oasisbrains/) | MRI | 2007 | 🟢 NIfTI, Analyze | — | ✅ | — | DUA | 416 subjects |
| [ADNI](https://adni.loni.usc.edu/) | MRI, PET | 2004 | 🟢 DICOM, NIfTI | — | — | ✅ | REQUEST | 2000+ participants (ADNI 1/GO/2/3/4) |
| [IXI](https://brain-development.org/ixi-dataset/) | MRI | — | 🟢 NIfTI | — | — | ✅ | OPEN | ~600 healthy subjects |

### 🫁 Chest & Thorax  <sub>(94)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-GEC](https://www.cancerimagingarchive.net/collection/cmb-gec/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 36.37 GB total (22.13 GB radiology); ~12 open-access radiology subjects, 251 series, 38,709 images |
| [CMB-LCA](https://www.cancerimagingarchive.net/collection/cmb-lca/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 421.59 GB total (191.92 GB radiology); 209 subjects |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [TAIX-Ray](https://huggingface.co/datasets/TLAIM/TAIX-Ray) | X-ray | 2026 | 🟡 Parquet, PNG | — | — | — | OPEN | ~215,000 chest radiographs (138k train / 42.9k test / 34.9k validation) from ICU patients |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [HiPaS](https://zenodo.org/records/14879605) | CT | 2025 | 🟡 NPZ | — | ✅ | — | OPEN | ~250 chest CT scans (ct_scan.zip 24 GB) |
| [LUNA25](https://luna25.grand-challenge.org/) | CT | 2025 | 🟢 MHA | — | — | — | REGISTRATION | Over 4,000 annotated low-dose chest CT exams for development, 468 hidden test cases, 300 reader-study cases |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [ReXGradient-160K](https://huggingface.co/datasets/rajpurkarlab/ReXGradient-160K) | X-ray | 2025 | 🟡 PNG, CSV | ✅ | — | — | REGISTRATION | 273,004 images from 160,000 studies of 109,487 patients across 79 sites (3 U.S. health systems) |
| [ReXGroundingCT](https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 3,142 non-contrast chest CT scans; 8,028 text-to-segmentation pairs; 16,301 annotated entities |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [TrackRAD2025](https://trackrad2025.grand-challenge.org/) | MRI | 2025 | 🟢 MHA | — | ✅ | — | REGISTRATION | 585 patients (108 with manual tumor segmentations, 477 unlabeled) from 6 international MRI-linac centers |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 25,692 CT volumes (50,188 with reconstructions) from 21,304 patients; ~21.3 TB |
| [CheXpert Plus](https://huggingface.co/datasets/StanfordAIMI/CheXpert-Plus) | X-ray | 2024 | 🟢 DICOM, PNG | ✅ | — | — | DUA | 223,228 chest radiographs paired with 187,711 radiology reports from 64,725 patients |
| [DRR-RATE](https://huggingface.co/datasets/farrell236/DRR-RATE) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | OPEN | 50,188 digitally reconstructed radiographs (~8 GB) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [PadChest-GR](https://bimcv.cipf.es/bimcv-projects/padchest-gr/) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | DUA | 4,555 CXR studies (3,099 abnormal, 1,456 normal); 7,037 positive and 3,422 negative finding sentences; ~46 GB |
| [RadGenome-ChestCT](https://huggingface.co/datasets/RadGenome/RadGenome-ChestCT) | CT | 2024 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 25,692 CT volumes with 665K grounded report regions + 1.3M VQA |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [AIIB23](https://codalab.lisn.upsaclay.fr/competitions/13238) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | — |
| [AeroPath](https://github.com/raidionics/AeroPath) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 27 CT scans (~5 GB) |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [INSPECT](https://inspect.stanford.edu/) | CT | 2023 | 🟢 DICOM | ✅ | — | — | DUA | 23,248 CTPA studies / 19,402 patients with reports and EHR |
| [LNQ2023](https://lnq2023.grand-challenge.org/) | CT | 2023 | 🟢 DICOM, NRRD, NIfTI | — | ✅ | — | REGISTRATION | 513 subjects (~35 GB) on TCIA |
| [MAIDA](https://maida.stanford.edu/) | X-ray | 2023 | 🟢 DICOM, PNG | ✅ | — | — | REGISTRATION | multi-institution chest X-rays across 22+ hospitals in 12 countries |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/) | X-ray | 2023 | 🟡 JPG | ✅ | — | — | DUA | 700,703 QA pairs over 164,324 image pairs |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [ATM'22](https://atm22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 500 chest CT scans |
| [BRAX](https://physionet.org/content/brax/) | X-ray | 2022 | 🟢 DICOM, PNG | — | — | — | DUA | 40,967 images / 19,351 patients |
| [CheXlocalize](https://github.com/rajpurkarlab/cheXlocalize) | X-ray | 2022 | 🟡 JPG, JSON | — | ✅ | — | REGISTRATION | 234 validation images (200 patients) and 668 test images (500 patients) |
| [MELA](https://mela.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | — | — | REGISTRATION | 1,100 chest CT scans (770 train / 110 val / 220 test) |
| [MS-CXR](https://physionet.org/content/ms-cxr/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 1,162 image-sentence bounding-box pairs across 8 findings |
| [NODE21](https://node21.grand-challenge.org/) | X-ray, CT | 2022 | 🟢 MHA | — | — | — | OPEN | 4,882 frontal chest radiographs (1,134 with 1,476 nodule bounding boxes; 3,748 nodule-free) plus LUNA16-derived CT nodule patches |
| [REFLACX](https://physionet.org/content/reflacx-xray-localization/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 3,032 eye-tracking + report sessions for 2,616 chest X-rays |
| [VinDr-PCXR](https://physionet.org/content/vindr-pcxr/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 9,125 studies (children under 10) |
| [CANDID-PTX](https://figshare.com/articles/dataset/CANDID-PTX/14173982) | X-ray | 2021 | 🟢 DICOM | ✅ | ✅ | — | REQUEST | 19,237 adult chest X-rays |
| [COVID-CT-MD](https://github.com/ShahinSHH/COVID-CT-MD) | CT | 2021 | 🟢 DICOM | — | — | — | OPEN | 305 patients (169 COVID-19, 60 CAP, 76 normal); labeled subset of 54 COVID and 25 CAP cases with 4,957 infection-positive and 18,392 infection-negative slices |
| [COVID-CTset](https://github.com/mr7495/COVID-CTset) | CT | 2021 | 🟡 TIFF | — | — | — | OPEN | 63,849 images, 377 patients (95 COVID, 282 normal) |
| [Chest ImaGenome](https://physionet.org/content/chest-imagenome/) | X-ray | 2021 | 🟡 JPG | ✅ | — | — | DUA | 242,072 frontal CXRs with scene graphs |
| [ChestX-Det](https://github.com/Deepwise-AILab/ChestX-Det-Dataset) | X-ray | 2021 | 🟡 PNG, JSON | — | ✅ | — | OPEN | 3,578 chest X-ray images (from NIH ChestX-ray14) |
| [RibSeg](https://github.com/HINTLab/RibSeg) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 490 CT scans, 11,719 ribs (320 train / 50 dev / 120 test) |
| [SIIM-FISABIO-RSNA COVID-19](https://www.kaggle.com/c/siim-covid19-detection) | X-ray | 2021 | 🟢 DICOM, CSV | — | — | — | REGISTRATION | ~6,334 chest radiographs (training) |
| [STOIC2021](https://stoic2021.grand-challenge.org/) | CT | 2021 | 🟢 MHA | — | — | — | REGISTRATION | 2,000 public training CT scans (from a 10,735-patient cohort) |
| [VinDr-CXR](https://physionet.org/content/vindr-cxr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 18,000 images (15,000 train / 3,000 test) |
| [ACRIN-NSCLC-FDG-PET](https://www.cancerimagingarchive.net/collection/acrin-nsclc-fdg-pet/) | PET, CT | 2020 | 🟢 DICOM | ✅ | ✅ | — | OPEN | 145.5 GB |
| [BIMCV-COVID19](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/) | X-ray, CT | 2020 | 🟢 PNG, DICOM | ✅ | ✅ | — | REGISTRATION | 21,342 CR + 34,829 DX studies + 7,918 CT (positive partition) |
| [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) | X-ray | 2020 | 🟡 PNG | — | ✅ | — | REGISTRATION | 21,165 images (4 classes) |
| [COVID-19-CT-Seg](https://zenodo.org/records/3757476) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 20 labeled CT scans |
| [COVIDx CXR](https://github.com/lindawangg/COVID-Net) | X-ray | 2020 | 🟡 PNG | — | — | — | REGISTRATION | COVIDx CXR-3: ~29,986 images / 16,648 patients |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [Lung-PET-CT-Dx](https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/) | CT, PET | 2020 | 🟢 DICOM | — | — | ✅ | OPEN | 355 patients / 251,135 DICOM images |
| [MedSeg COVID-19 CT Segmentation](https://www.medseg.ai/covid-19) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 100 axial CT slices (~40 patients) plus 9 CT volumes (~829 slices) |
| [MosMedData](https://academictorrents.com/details/f2175c4676e041ea65568bb70c2bcd15c7325fd2) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,110 CT studies (~50 with masks) |
| [Object-CXR](https://github.com/hlk-1135/object-CXR) | X-ray | 2020 | 🟡 JPEG | — | — | — | OPEN | 10,000 frontal X-rays (5,000 with foreign objects) |
| [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) | X-ray | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 160,868 images / 67,625 patients |
| [RSNA-STR Pulmonary Embolism CT](https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection) | CT | 2020 | 🟢 DICOM | — | — | — | REGISTRATION | 7,279 CTPA studies (public training set) |
| [RibFrac](https://ribfrac.grand-challenge.org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 660 CT scans (~5,000 fractures); 420 train, 80 val, 160 test |
| [TBX11K](https://mmcheng.net/tb/) | X-ray | 2020 | 🟡 PNG, XML, JSON | — | — | — | OPEN | 11,200 chest X-ray images at 512x512 |
| [Anti-PD-1_Lung](https://www.cancerimagingarchive.net/collection/anti-pd-1_lung/) | PET, CT | 2019 | 🟢 DICOM | ✅ | ✅ | — | REGISTRATION | 61 GB |
| [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) | X-ray | 2019 | 🟡 JPEG | — | — | — | REGISTRATION | 224,316 radiographs / 65,240 patients |
| [LNDb](https://lndb.grand-challenge.org/) | CT | 2019 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | REGISTRATION | 294 CT scans |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/) | X-ray | 2019 | 🟢 DICOM | ✅ | — | — | DUA | 377,110 images / 227,835 studies / ~65,379 patients |
| [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/) | X-ray | 2019 | 🟡 JPEG | — | — | — | DUA | 377,110 JPG images / 227,827 studies |
| [SIIM-ACR Pneumothorax](https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation) | X-ray | 2019 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~12,047 train + ~3,205 test |
| [SegTHOR](https://competitions.codalab.org/competitions/21145) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 60 CT scans (40 train / 20 test) |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Four tasks; 50 training CT scans (+10 test) each for head-neck and chest cohorts |
| [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) | X-ray | 2018 | 🟡 JPEG | — | — | — | OPEN | 5,856 chest radiographs |
| [FUMPE](https://figshare.com/collections/FUMPE/4107803) | CT | 2018 | 🟢 DICOM, MAT | — | ✅ | — | OPEN | 35 CT pulmonary angiography scans (35 subjects) |
| [RSNA Pneumonia Detection](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) | X-ray | 2018 | 🟢 DICOM | — | — | — | REGISTRATION | ~26,684 training radiographs |
| [TB Portals](https://tbportals.niaid.nih.gov/) | X-ray, CT | 2018 | 🟢 DICOM | ✅ | — | — | DUA | 27,294 chest X-ray and CT imaging studies; 24,752 TB cases; 16 countries, 40 sites |
| [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 112,120 frontal images / 30,805 patients |
| [LUNA16](https://luna16.grand-challenge.org/) | CT | 2016 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | OPEN | 888 CT scans / 1,186 nodule annotations |
| [NSCLC-Radiogenomics](https://www.cancerimagingarchive.net/collection/nsclc-radiogenomics/) | CT, PET | 2015 | 🟢 DICOM, CSV | ✅ | ✅ | ✅ | OPEN | 211 patients (CT and PET/CT; RNA-seq for 130) |
| [SPIE-AAPM Lung CT Challenge (LUNGx)](https://www.cancerimagingarchive.net/collection/spie-aapm-lung-ct-challenge/) | CT | 2015 | 🟢 DICOM, XLSX | — | — | — | OPEN | 70 subjects, 22,489 images (~12 GB) |
| [Montgomery County CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | ✅ | — | OPEN | 138 frontal X-rays (80 normal, 58 TB) |
| [NSCLC-Radiomics](https://www.cancerimagingarchive.net/collection/nsclc-radiomics/) | CT | 2014 | 🟢 DICOM, CSV | ✅ | ✅ | — | OPEN | 422 patients (tumor segmentations for 318) |
| [Shenzhen Hospital CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | — | — | OPEN | 662 frontal X-rays (326 normal, 336 TB) |
| [NLST](https://www.cancerimagingarchive.net/collection/nlst/) | CT | 2013 | 🟢 DICOM | — | — | — | OPEN | 26,254 subjects / 73,116 CT studies |
| [Open-i / Indiana University CXR](https://openi.nlm.nih.gov/) | X-ray | 2013 | 🟢 DICOM, PNG | ✅ | — | — | OPEN | 7,470 images / 3,955 reports |
| [LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/) | CT | 2011 | 🟢 DICOM, XML | — | ✅ | — | OPEN | 1,018 CT scans / 1,010 patients |
| [EMPIRE10](https://empire10.grand-challenge.org/) | CT | 2010 | 🟢 MetaImage (.mhd/.raw) | — | — | — | REGISTRATION | 30 intra-subject chest CT scan pairs |
| [JSRT](http://db.jsrt.or.jp/eng.php) | X-ray | 2000 | 🟡 IMG | — | — | — | REGISTRATION | 247 posterior-anterior chest radiographs (154 with a lung nodule: 100 malignant, 54 benign; 93 without nodules); 2048x2048, 12-bit, 0.175 mm pixel spacing |

### 🫀 Cardiac  <sub>(30)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [MultiD4CAD](https://zenodo.org/records/15148653) | CT | 2025 | 🟢 DICOM | — | ✅ | — | DUA | 118 patients (40 non-CAD, 78 CAD); ~4.6 TB |
| [CADICA](https://data.mendeley.com/datasets/p9bpx9ctcv) | X-ray | 2024 | 🟡 PNG, XLSX, TXT, MAT | — | — | — | OPEN | 42 patients; invasive coronary angiography videos, frames extracted to 512x512 PNG (1-151 frames per video, ~10 fps) |
| [CMRxRecon2024](https://cmrxrecon.github.io/2024/) | MRI | 2024 | 🟢 MATLAB | — | — | ✅ | REGISTRATION | 330 healthy volunteers (200 training, 60 validation, 70 test) |
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
| [M&Ms-2](https://www.ub.edu/mnms-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 360 patients |
| [EMIDEC](http://emidec.com/) | MRI | 2020 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 150 cases (50 normal, 100 pathological) |
| [ImageCHD](https://github.com/XiaoweiXu/ImageCHD-A-3D-Computed-Tomography-Image-Dataset-for-Classification-of-Congenital-Heart-Disease) | CT | 2020 | 🟢 NRRD | — | ✅ | — | REGISTRATION | 110 3D CT images |
| [M&Ms](https://www.ub.edu/mnms/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 375 patients (multi-vendor) |
| [MyoPS 2020](https://zmiclab.github.io/zxh/0/myops20/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 45 patients (25 train + 20 test) |
| [OCMR](https://ocmr.info/) | MRI | 2020 | 🟢 ISMRMRD, HDF5 | — | — | — | OPEN | 165 fully sampled acquisitions (279 slices) and 212 prospectively undersampled acquisitions (842 slices) |
| [MS-CMRSeg 2019](https://zmiclab.github.io/zxh/0/mscmrseg19/) | MRI | 2019 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 45 cardiomyopathy patients (3 sequences each: LGE, T2, bSSFP) |
| [Atria Seg 2018](https://www.cardiacatlas.org/atriaseg2018-challenge/) | MRI | 2018 | 🟢 NRRD | — | ✅ | — | REGISTRATION | 154 3D LGE-MRI (100 train + 54 test) |
| [MSD Heart (Task02)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 30 cases (20 train + 10 test) |
| [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 150 patients (100 train + 50 test) |
| [MM-WHS](https://zmiclab.github.io/zxh/0/mmwhs/) | CT, MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 120 images (60 CT/CTA + 60 MRI) |
| [HVSMR 2016](http://segchd.csail.mit.edu/) | MRI | 2016 | 🟢 NRRD | — | ✅ | — | OPEN | 20 3D cardiovascular MR images (10 training + 10 test) |
| [Second Annual Data Science Bowl](https://www.kaggle.com/c/second-annual-data-science-bowl) | MRI | 2016 | 🟢 DICOM | — | — | — | REGISTRATION | ~1,140 patients (cine cardiac MRI studies) |
| [RVSC](https://rvsc.projets.litislab.fr/) | MRI | 2012 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 48 patients (16 train + 32 test) |
| [Sunnybrook Cardiac Data](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) | MRI | 2009 | 🟢 DICOM | — | ✅ | — | OPEN | 45 patients |

### 🩸 Vascular  <sub>(24)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [HiPaS](https://zenodo.org/records/14879605) | CT | 2025 | 🟡 NPZ | — | ✅ | — | OPEN | ~250 chest CT scans (ct_scan.zip 24 GB) |
| [TopBrain 2025](https://topbrain2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Batches 1-2 on Zenodo: 50 angiographic scans (25 paired CTA/MRA subjects), ~2.0 GB; 40 CTA / 42 MRA vessel labels (34 overlapping) |
| [AortaSeg24](https://aortaseg24.grand-challenge.org/) | CT | 2024 | 🟢 MHA, NIfTI | — | ✅ | — | REGISTRATION | 100 annotated CTA volumes |
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
| [Parse2022](https://parse2022.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 CTPA volumes (100 train, 30 validation, 70 test) |
| [COCA (Stanford)](https://aimi.stanford.edu/datasets/coca-coronary-calcium-chest-ct) | CT | 2021 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~1000 patients (789 gated + 214 non-gated) |
| [ASOCA](https://asoca.grand-challenge.org/) | CT | 2020 | 🟢 NRRD | — | ✅ | — | DUA | 60 cases (40 train + 20 test) |
| [FUMPE](https://figshare.com/collections/FUMPE/4107803) | CT | 2018 | 🟢 DICOM, MAT | — | ✅ | — | OPEN | 35 CT pulmonary angiography scans (35 subjects) |
| [HVSMR 2016](http://segchd.csail.mit.edu/) | MRI | 2016 | 🟢 NRRD | — | ✅ | — | OPEN | 20 3D cardiovascular MR images (10 training + 10 test) |
| [orCaScore](https://orcascore.grand-challenge.org/) | CT | 2014 | 🟢 MHD | — | ✅ | — | REGISTRATION | 72 patients (32 train + 40 test) |
| [VESSEL12](https://vessel12.grand-challenge.org/) | CT | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 20 chest CT scans |

### 🫃 Abdominal  <sub>(71)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-CRC](https://www.cancerimagingarchive.net/collection/cmb-crc/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 400.75 GB; 102 subjects (v11); 62 radiology patients with 269,002 images |
| [CMB-GEC](https://www.cancerimagingarchive.net/collection/cmb-gec/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 36.37 GB total (22.13 GB radiology); ~12 open-access radiology subjects, 251 series, 38,709 images |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [CMB-OV](https://www.cancerimagingarchive.net/collection/cmb-ov/) | CT, MRI | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 36.99 GB radiology (Version 4); 19 radiology subjects, 71 studies, 554 series, 68,415 images; 162 GB histopathology (48 subjects) |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [Gastric-X](https://huggingface.co/datasets/HaoChen2/Gastric-X) | CT | 2026 | 🟢 NIfTI, JSON, PNG | ✅ | ✅ | ✅ | REGISTRATION | 1,403 patients; 4,897 CT phases (~155 GB) |
| [AbdomenAtlas 3.0](https://github.com/MrGiovanni/RadGPT) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 9,262 CT volumes (3,220 with a contrast-enhanced phase) + reports |
| [CURVAS-PDAC](https://curvas-pdacvi.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | OPEN | Training set: 40 contrast-enhanced abdominal CT cases (of a 125-scan cohort; validation=5, test=85 withheld); ~5.5 GB; each case has 5 PDAC segmentations plus STAPLE consensus and vessel annotations |
| [CirrMRI600+](https://github.com/NUBagciLab/CirrMRI600Plus) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 600+ MRI volumes (T1W and T2W); ~15GB |
| [Cyst-X](https://osf.io/74vfs/) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 1,461 abdominal MRI scans from 764 patients across 7 centers |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PanTS](https://github.com/MrGiovanni/PanTS) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | — | OPEN | 36,390 3D CT volumes from 145 centers; ~300GB |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [TrackRAD2025](https://trackrad2025.grand-challenge.org/) | MRI | 2025 | 🟢 MHA | — | ✅ | — | REGISTRATION | 585 patients (108 with manual tumor segmentations, 477 unlabeled) from 6 international MRI-linac centers |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [AbdomenAtlas 1.0](https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas1.0Mini) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | DUA | 5,195 annotated CT volumes, 326 GB |
| [AbdomenAtlas 1.1](https://github.com/MrGiovanni/AbdomenAtlas) | CT | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 9,262 CT volumes; >251,000 masks |
| [CARE 2024 LiQA](http://www.zmic.org.cn/care_2024/track3/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 440 patients; training 250 (30 with liver segmentation masks + 220 unannotated, all 250 with fibrosis staging labels); test 160 (120 known vendors + 40 unseen vendor) |
| [CURVAS](https://curvas.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 90 CT scans (training set ~6.3 GB) |
| [FLARE 2024](https://www.codabench.org/competitions/2320/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Thousands of partially labeled and unlabeled abdominal CT scans (large semi-supervised set) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [Learn2Reg](https://learn2reg.grand-challenge.org/) | CT, MRI, PET | 2024 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | Multiple task datasets (e.g., OASIS 416 brain MR scans, extended NLST lung CT, ThoraxCBCT, Abdomen CT-CT 30/20, Abdomen MR-CT, Hippocampus MR 263/131, whole-body PSMA PET/CT ~597 scans) |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients (>6M images) |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [PANORAMA](https://panorama.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | ~2,238 CECT training scans (two centers) plus 194 MSD and 80 NIH external cases; ~197 GB |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [ATLAS](https://atlas-challenge.u-bourgogne.fr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 90 T1 contrast-enhanced MRI scans (60 train / 30 test) from 90 unresectable HCC patients |
| [Adrenal-ACC-Ki67-Seg](https://www.cancerimagingarchive.net/collection/adrenal-acc-ki67-seg/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 53 patients; 65 studies; 177 series; 18,255 images; ~9.9 GB |
| [Colorectal-Liver-Metastases](https://www.cancerimagingarchive.net/collection/colorectal-liver-metastases/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 197 patients |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [FLARE23](https://codalab.lisn.upsaclay.fr/competitions/12239) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 4000 train + 100 val + 400 test CT |
| [KiTS23](https://kits-challenge.org/kits23/) | CT | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 599 CT (489 train / 110 test) |
| [LLD-MMRI](https://github.com/LMMMEng/LLD-MMRI-Dataset) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | REQUEST | 498 patients, 8 sequences each |
| [RSNA 2023 Abdominal Trauma Detection](https://www.kaggle.com/competitions/rsna-2023-abdominal-trauma-detection) | CT | 2023 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~4,700 patients (multiple CT series each) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [FLARE22](https://flare22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 2300 CT (50 labeled + 2000 unlabeled train) |
| [KiPA22](https://kipa22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 130 CTA cases (100 available: 70 training + 30 open test) |
| [WORD](https://github.com/HiLab-git/WORD) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 150 CT (100 train / 20 val / 30 test) |
| [AbdomenCT-1K](https://github.com/JunMa11/AbdomenCT-1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 1112 CT from 12 centers |
| [CT Kidney Dataset: Normal-Cyst-Tumor-Stone](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone) | CT | 2021 | 🟡 JPG | — | — | — | REGISTRATION | 12,446 CT images (Normal 5,077; Cyst 3,709; Tumor 2,283; Stone 1,377) |
| [FLARE21](https://flare.grand-challenge.org/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 511 CT (361 train / 50 val / 100 test) |
| [HCC-TACE-Seg](https://www.cancerimagingarchive.net/collection/hcc-tace-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 105 patients; ~28.6 GB |
| [KiTS21](https://kits-challenge.org/kits21/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 train + 100 test CT |
| [Pancreatic-CT-CBCT-SEG](https://www.cancerimagingarchive.net/collection/pancreatic-ct-cbct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 40 patients (~14.3 GB, 370 series, 24,246 images) |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [MOOD](https://www.synapse.org/mood) | MRI, CT | 2020 | 🟢 NIfTI | — | — | — | REGISTRATION | ~800 brain MRI + ~600 abdominal CT scans |
| [TCGA-KIRC](https://www.cancerimagingarchive.net/collection/tcga-kirc/) | CT, MRI, X-ray | 2020 | 🟢 DICOM | ✅ | — | ✅ | OPEN | 91.56 GB |
| [CHAOS](https://chaos.grand-challenge.org/) | CT, MRI | 2019 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 40 CT + 120 MRI series (40 patients) |
| [KiTS19](https://kits19.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 CT (210 train / 90 test) |
| [MSD Colon (Task10)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 190 CT (126 train / 64 test) |
| [MSD Hepatic Vessel (Task08)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 443 CT (303 train / 140 test) |
| [MSD Liver (Task03)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 201 CT (131 train / 70 test) |
| [MSD Pancreas (Task07)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 420 CT (282 train / 139 test) |
| [MSD Spleen (Task09)](http://medicaldecathlon.com/) | CT | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 61 CT (41 train / 20 test) |
| [LiTS](https://competitions.codalab.org/competitions/17094) | CT | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 131 train + 70 test CT |
| [BTCV / Synapse Multi-organ](https://www.synapse.org/Synapse:syn3193805) | CT | 2015 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 30 train + 20 test contrast CT |
| [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 825 patients (prone + supine) |
| [Pancreas-CT (NIH)](https://www.cancerimagingarchive.net/collection/pancreas-ct/) | CT | 2015 | 🟢 DICOM, NIfTI | — | ✅ | — | OPEN | 82 contrast-enhanced abdominal CT |

### ⬇️ Pelvic & Prostate  <sub>(32)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-CRC](https://www.cancerimagingarchive.net/collection/cmb-crc/) | CT, MRI, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 400.75 GB; 102 subjects (v11); 62 radiology patients with 269,002 images |
| [CMB-OV](https://www.cancerimagingarchive.net/collection/cmb-ov/) | CT, MRI | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 36.99 GB radiology (Version 4); 19 radiology subjects, 71 studies, 554 series, 68,415 images; 162 GB histopathology (48 subjects) |
| [CMB-PCA](https://www.cancerimagingarchive.net/collection/cmb-pca/) | MRI, CT, PET, X-ray | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | ✅ | OPEN | 98.09 GB; 76 subjects (open radiology tier: 26 subjects, ~16.41 GB) |
| [COBRA2026](https://doi.org/10.5281/zenodo.21322350) | CT | 2026 | 🟢 MHA, XML, YAML, PNG | — | — | — | OPEN | 867 cases (692 train / 52 val / 123 test); ~950 GB total |
| [LUND-PROBE](https://datahub.aida.scilifelab.se/10.23698/aida/lund-probe) | MRI, CT | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 467 patients (432 primary + 35 extended deep-learning subset), 176.56 GB |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [Healthy-Total-Body-CTs](https://www.cancerimagingarchive.net/collection/healthy-total-body-cts/) | CT | 2024 | 🟢 DICOM, NIfTI, XLSX | — | ✅ | — | REQUEST | 30 healthy adult subjects; 59.03 GB; 111,778 images across 135 series |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients (>6M images) |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [fastMRI Prostate](https://fastmri.med.nyu.edu/) | MRI | 2024 | 🟡 HDF5 | — | — | ✅ | DUA | — |
| [DAP Atlas](https://github.com/alexanderjaus/AtlasDataset) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 533 whole-body CT scans (from AutoPET), 142 anatomical structures |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [SAROS](https://github.com/UMEssen/SAROS-dataset) | CT | 2023 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 882 subjects, 900 whole-body CT series, ~13,000 sparsely annotated axial slices |
| [SynthRAD2023](https://synthrad2023.grand-challenge.org/) | MRI, CT | 2023 | 🟢 MHA | — | — | — | OPEN | 540 paired MRI-CT and 540 CBCT-CT sets (>500 patients per task) from three centers |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [PI-CAI](https://pi-cai.grand-challenge.org/) | MRI | 2022 | 🟢 MHA, NIfTI | — | ✅ | ✅ | OPEN | 1500 bpMRI (1476 patients, public set) |
| [Prostate158](https://github.com/kbressem/prostate158) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 158 studies (139 train / 19 test) |
| [QUBIQ](https://qubiq.grand-challenge.org/) | MRI, CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | Multiple tasks across brain, kidney, prostate and pancreas (dozens of cases per task) |
| [CTPelvic1K](https://github.com/MIRACLE-Center/CTPelvic1K) | CT | 2020 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 1,184 CT volumes (~320K slices), ~17 GB |
| [Prostate-MRI-US-Biopsy](https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/) | MRI | 2020 | 🟢 DICOM, STL, XLSX | ✅ | ✅ | ✅ | OPEN | 1,151 subjects; 2,799 studies; ~80 GB |
| [Gold Atlas](https://zenodo.org/records/583096) | MRI, CT | 2018 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 19 patients, ~1.7 TB |
| [MSD Prostate (Task05)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 48 mpMRI (32 train / 16 test) |
| [ProstateX](https://www.cancerimagingarchive.net/collection/prostatex/) | MRI | 2017 | 🟢 DICOM | — | — | ✅ | OPEN | 346 patients (330 lesions train) |
| [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 825 patients (prone + supine) |
| [Prostate-3T](https://www.cancerimagingarchive.net/collection/prostate-3t/) | MRI | 2015 | 🟢 DICOM, MHA, NRRD | — | ✅ | — | OPEN | 59 subjects, 1161 images (~269 MB) |
| [PROMISE12](https://promise12.grand-challenge.org/) | MRI | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 50 train + 30 test T2W MRI |

### 🦴 Musculoskeletal  <sub>(38)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [Bone_metastases_pet_ct_for_BlueprINT](https://huggingface.co/datasets/FangDai/Bone_metastases_pet_ct_for_BlueprINT) | PET, CT | 2025 | 🟡 PNG | — | — | — | OPEN | 1,642 image samples |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [RAM-W600](https://huggingface.co/datasets/TokyoTechMagicYang/RAM-W600) | X-ray | 2025 | 🟡 BMP, NPY, JSON | — | ✅ | — | OPEN | 1,048 wrist conventional radiographs from 388 patients across 6 medical centers (618 with instance segmentation masks, 800 with SvdH bone erosion scores) |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [Spine Generic (Multi-Subject)](https://github.com/spine-generic/data-multi-subject) | MRI | 2025 | 🟢 NIfTI, BIDS | — | — | ✅ | OPEN | ~260+ subjects, ~26 GB, 40+ sites |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
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
| [CTSpine1K](https://github.com/MIRACLE-Center/CTSpine1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,005 CT volumes (>500,000 labeled slices, >11,000 vertebrae) |
| [RibSeg](https://github.com/HINTLab/RibSeg) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 490 CT scans, 11,719 ribs (320 train / 50 dev / 120 test) |
| [SKM-TEA](https://aimi.stanford.edu/datasets/skm-tea-knee-mri) | MRI | 2021 | 🟢 HDF5 (k-space), DICOM | — | ✅ | — | REGISTRATION | 155 qDESS knee scans (~1.6 TB) |
| [VinDr-SpineXR](https://physionet.org/content/vindr-spinexr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 10,466 spine X-ray images from 5,000 studies |
| [CTPelvic1K](https://github.com/MIRACLE-Center/CTPelvic1K) | CT | 2020 | 🟢 NIfTI, DICOM | — | ✅ | — | OPEN | 1,184 CT volumes (~320K slices), ~17 GB |
| [RibFrac](https://ribfrac.grand-challenge.org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 660 CT scans (~5,000 fractures); 420 train, 80 val, 160 test |
| [LERA](https://aimi.stanford.edu/datasets/lera-lower-extremity-radiographs) | X-ray | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 182 patients (foot, knee, ankle, hip) |
| [MRSpineSeg](https://github.com/pangshumao/SpineParseNet) | MRI | 2019 | 🟢 NIfTI | — | ✅ | — | REQUEST | 172 training + 20 (round-1) + 23 (round-2) sagittal T2-weighted lumbar MRI volumes (test labels withheld) |
| [MRNet](https://stanfordmlgroup.github.io/competitions/mrnet/) | MRI | 2018 | 🟢 NPY | — | — | ✅ | REGISTRATION | 1,370 knee MRI exams |
| [MURA](https://stanfordmlgroup.github.io/competitions/mura/) | X-ray | 2018 | 🟡 PNG | — | — | — | REGISTRATION | 40,561 images / 14,863 studies / 12,173 patients |
| [fastMRI knee](https://fastmri.med.nyu.edu/) | MRI | 2018 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | >1,500 fully-sampled knee k-space MRIs + 10,000 clinical DICOM knee MRIs (~1.35 TB) |
| [KneeMRI](http://www.riteh.uniri.hr/~istajduh/projects/kneeMRI/) | MRI | 2017 | 🟢 PCK | — | — | — | OPEN | 917 sagittal PD-weighted knee MRI volumes |
| [RSNA Bone Age](https://www.rsna.org/rsnai/ai-image-challenge/rsna-pediatric-bone-age-challenge-2017) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 14,236 pediatric hand radiographs |
| [Soft-tissue-Sarcoma](https://www.cancerimagingarchive.net/collection/soft-tissue-sarcoma/) | PET, CT, MRI | 2015 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 9.87 GB |
| [Digital Hand Atlas](https://ipilab.usc.edu/research/baaweb/) | X-ray | 2007 | 🟡 JPEG | — | — | — | OPEN | ~1,400 normal pediatric hand radiographs |
| [OAI](https://nda.nih.gov/oai/) | MRI, X-ray | — | 🟢 DICOM | — | — | ✅ | DUA | 4,796 participants, longitudinal bilateral knee MRI and X-ray |

### 🎀 Breast  <sub>(24)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [MAMA-MIA](https://www.ub.edu/mama-mia/) | MRI | 2025 | 🟢 NIfTI, DICOM | ✅ | ✅ | ✅ | DUA | 1,506 annotated training scans plus 574 external validation cases (multi-institutional) |
| [NL-Breast-Screening](https://www.frdr-dfdr.ca/repo/dataset/c702145e-2e53-4421-b578-8bb53bbd3952) | X-ray | 2025 | 🟢 DICOM | — | — | — | OPEN | 5,997 mammography exams (4 standard views each), biopsy-confirmed |
| [ODELIA Breast MRI 2025](https://huggingface.co/datasets/ODELIA-AI/ODELIA-Challenge-2025) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | DUA | 500 studies (~135GB) from six European centers, multiple vendors at 1.5T and 3T |
| [TN-Mammo](https://physionet.org/content/tn-mammo-breast-density/) | X-ray | 2025 | 🟡 JPEG | — | — | — | DUA | 676 exams (2,704 images, 4 views each) |
| [Advanced-MRI-Breast-Lesions](https://www.cancerimagingarchive.net/collection/advanced-mri-breast-lesions/) | MRI | 2024 | 🟢 DICOM, XLSX | ✅ | ✅ | ✅ | OPEN | 645.62 GB; 632 imaging sessions (1,259,688 images, 6,811 series) |
| [CMB-BRCA](https://www.cancerimagingarchive.net/collection/cmb-brca/) | CT, MRI, PET, X-ray | 2024 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 203.94 GB total (78.94 GB radiology, 125 GB pathology); 101 subjects |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [fastMRI Breast](https://fastmri.med.nyu.edu/) | MRI | 2024 | 🟡 HDF5 | — | — | — | DUA | 300 clinical exams |
| [BreastDM](https://github.com/smallboy-code/Breast-cancer-dataset) | MRI | 2023 | 🟡 PNG | — | ✅ | ✅ | OPEN | 232 cases (147 malignant, 85 benign) |
| [EMBED](https://registry.opendata.aws/emory-breast-imaging-dataset-embed/) | X-ray | 2023 | 🟢 DICOM | — | — | — | DUA | 3.4M images from ~110,000 patients; 60,000 annotated lesions |
| [RSNA Screening Mammography](https://www.kaggle.com/competitions/rsna-breast-cancer-detection) | X-ray | 2023 | 🟢 DICOM | — | — | — | REGISTRATION | ~54,700 images / ~20,000 patients |
| [ISPY2](https://www.cancerimagingarchive.net/collection/ispy2/) | MRI | 2022 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 719 patients |
| [VinDr-Mammo](https://physionet.org/content/vindr-mammo/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 5,000 exams / 20,000 images |
| [BCS-DBT](https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,060 patients / 22,032 scans (~1.63 TB) |
| [CMMD](https://www.cancerimagingarchive.net/collection/cmmd/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,202 images / 1,775 patients |
| [ACRIN-FLT-Breast](https://www.cancerimagingarchive.net/collection/acrin-flt-breast/) | PET, CT | 2020 | 🟢 DICOM | ✅ | — | — | OPEN | 74.24 GB |
| [Duke Breast Cancer MRI](https://www.cancerimagingarchive.net/collection/duke-breast-cancer-mri/) | MRI | 2018 | 🟢 DICOM | — | — | ✅ | OPEN | 922 patients / ~773,000 images |
| [CBIS-DDSM](https://www.cancerimagingarchive.net/collection/cbis-ddsm/) | X-ray | 2016 | 🟢 DICOM | — | ✅ | — | OPEN | 10,239 images / 1,566 subjects |
| [ISPY1 (ACRIN 6657)](https://www.cancerimagingarchive.net/collection/ispy1/) | MRI | 2016 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 222 patients |
| [INbreast](http://medicalresearch.inescporto.pt/breastresearch/index.php/Get_INbreast_Database) | X-ray | 2012 | 🟢 DICOM, XML | — | ✅ | — | REQUEST | 410 images / 115 cases |
| [Breast-Diagnosis](https://www.cancerimagingarchive.net/collection/breast-diagnosis/) | MRI, PET, CT, X-ray | 2011 | 🟢 DICOM | — | — | ✅ | OPEN | 88 subjects / ~105,050 images |
| [OPTIMAM (OMI-DB)](https://medphys.royalsurrey.nhs.uk/omidb/) | X-ray | 2008 | 🟢 DICOM | — | — | ✅ | REQUEST | ~750,000 cases (2D full-field digital mammography and 3D tomosynthesis) |
| [mini-MIAS](https://www.mammoimage.org/databases/) | X-ray | 1994 | 🟡 PGM | — | — | — | OPEN | 322 images (~2.3 GB original; ~100 MB distributed) |
| [3D-MammographyDataset](https://huggingface.co/datasets/iMerit/3D-MammographyDataset) | X-ray | — | 🟢 DICOM, JSON, XLSX | — | — | — | DUA | ~650 MB, fewer than 1,000 cases |

### 👤 Head & Neck  <sub>(28)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [HECKTOR 2025](https://hecktor25.grand-challenge.org/) | PET, CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 1200+ patients from 11+ centers (FDG-PET/CT); ~850 training from prior editions plus ~400 new test cases from two French cohorts |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [Panoramic_Radiographs_for_Dental_Condition](https://huggingface.co/datasets/ismaelportog/Panoramic_Radiographs_for_Dental_Condition) | X-ray | 2025 | 🟡 JPG, Parquet | — | — | — | OPEN | ~27,884 annotated rows / 1.42 GB (from ~1,808 source panoramic radiographs; 1,628 training + 180 external validation) |
| [SegRap2025](https://hilab-git.github.io/SegRap2025_Challenge) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 260 NPC patients with GTV annotations, 402 patients with LN CTV annotations, plus 500 unlabeled CT scans |
| [SynthRAD2025](https://synthrad2025.grand-challenge.org/) | CT, MRI | 2025 | 🟢 MHA | — | — | — | REGISTRATION | ~900 paired MR-CT cases (Task 1) and ~1500 paired CBCT-CT cases (Task 2) from 5 European university medical centers |
| [ToothFairy3](https://toothfairy3.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Publicly annotated CBCT scans with 77 anatomical classes (expanded from ToothFairy2's 42) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [HNTS-MRG 2024](https://hntsmrg24.grand-challenge.org/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | ~150 training patients (pre-RT and mid-RT), ~50 test patients |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [RADCURE](https://www.cancerimagingarchive.net/collection/radcure/) | CT | 2024 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 3,346 patients |
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
| [HN1](https://www.cancerimagingarchive.net/collection/head-neck-radiomics-hn1/) | CT | 2019 | 🟢 DICOM, RTSTRUCT, SEG | ✅ | ✅ | — | DUA | 137 patients |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | CT | 2019 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Four tasks; 50 training CT scans (+10 test) each for head-neck and chest cohorts |
| [Head-Neck-PET-CT](https://www.cancerimagingarchive.net/collection/head-neck-pet-ct/) | PET, CT | 2017 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 298 patients |
| [QIN-HeadNeck](https://www.cancerimagingarchive.net/collection/qin-headneck/) | PET, CT | 2015 | 🟢 DICOM, SEG, SR | ✅ | ✅ | — | REQUEST | 279 subjects |
| [TCGA-HNSC](https://www.cancerimagingarchive.net/collection/tcga-hnsc/) | CT, PET, MRI | 2014 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 227 patients (479 studies) |

### 🦷 Dental & Maxillofacial  <sub>(8)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [Panoramic_Radiographs_for_Dental_Condition](https://huggingface.co/datasets/ismaelportog/Panoramic_Radiographs_for_Dental_Condition) | X-ray | 2025 | 🟡 JPG, Parquet | — | — | — | OPEN | ~27,884 annotated rows / 1.42 GB (from ~1,808 source panoramic radiographs; 1,628 training + 180 external validation) |
| [ToothFairy3](https://toothfairy3.grand-challenge.org/) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Publicly annotated CBCT scans with 77 anatomical classes (expanded from ToothFairy2's 42) |
| [STS 2024](https://zenodo.org/records/17712688) | X-ray, CT | 2024 | 🟢 PNG, NIfTI | — | ✅ | — | OPEN | ~2,380 panoramic X-ray (OPG) images + ~330 CBCT scans; ~968 MB total on Zenodo |
| [ToothFairy2](https://toothfairy2.grand-challenge.org/) | CT | 2024 | 🟢 MHA | — | ✅ | — | REGISTRATION | 480 public training CBCT volumes |
| [DENTEX](https://dentex.grand-challenge.org/) | X-ray | 2023 | 🟡 PNG | — | — | — | OPEN | 1,005 fully-annotated panoramic X-rays (3,903 total) |
| [CTooth](https://github.com/liangjiubujiu/CTooth) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 22 annotated CBCT volumes (CTooth+ adds 146 unlabeled) |
| [Tufts Dental Database](https://tdd.ece.tufts.edu/) | X-ray | 2022 | 🟡 JPG, TIFF | ✅ | ✅ | — | REQUEST | 1,000 panoramic X-rays |

### 🌐 Whole-Body & PET  <sub>(25)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [ViMed-PET-CT](https://huggingface.co/datasets/thainamhoang/ViMed-PET-CT) | PET, CT | 2026 | 🟡 NPZ | ✅ | — | — | OPEN | 304 studies, ~205 GB |
| [Bone_metastases_pet_ct_for_BlueprINT](https://huggingface.co/datasets/FangDai/Bone_metastases_pet_ct_for_BlueprINT) | PET, CT | 2025 | 🟡 PNG | — | — | — | OPEN | 1,642 image samples |
| [CADS](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes; 167 anatomical structures; ~1.92 TB |
| [CADS-dataset](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes with segmentation masks (10K<n<100K files) |
| [Deep-PSMA](https://deep-psma.grand-challenge.org/) | PET, CT | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 100 training patients (~24.1 GB, NIfTI, on Zenodo); challenge also includes 10 preliminary validation and 40 test cases; single center (Peter MacCallum Cancer Centre) |
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
| [autoPET I](https://autopet.grand-challenge.org/) | PET, CT | 2022 | 🟢 DICOM, NIfTI | — | ✅ | — | DUA | 1,014 studies / 900 patients (FDG) |
| [Pediatric-CT-SEG](https://www.cancerimagingarchive.net/collection/pediatric-ct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | — | OPEN | 359 patients (ages 5 days to 16 years); 65.69 GB |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [Anti-PD-1_Melanoma](https://www.cancerimagingarchive.net/collection/anti-pd-1_melanoma/) | PET, CT, MRI | 2018 | 🟢 DICOM | ✅ | — | — | REQUEST | 98.41 GB |

### 🧩 Multiple / Various body parts  <sub>(29)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMB-MEL](https://www.cancerimagingarchive.net/collection/cmb-mel/) | CT, MRI, PET | 2026 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | ~46.79 GB open radiology (75,459 DICOM images, 32 subjects); additional 37.94 GB restricted; 155.5 GB histopathology |
| [FLARE26-MLLM-3D](https://huggingface.co/datasets/FLARE-MedFM/FLARE26-MLLM-3D) | CT | 2026 | 🟢 NIfTI, JSON | ✅ | ✅ | — | REGISTRATION | ~374 GB; thousands of 3D CT volumes with paired reports/QA |
| [ViMed-PET-CT](https://huggingface.co/datasets/thainamhoang/ViMed-PET-CT) | PET, CT | 2026 | 🟡 NPZ | ✅ | — | — | OPEN | 304 studies, ~205 GB |
| [CADS-dataset](https://huggingface.co/datasets/mrmrx/CADS-dataset) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 22,022 CT volumes with segmentation masks (10K<n<100K files) |
| [FLARE-Task4-CT-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-CT-FM) | CT | 2025 | 🟢 NIfTI | — | — | — | REGISTRATION | 10,000+ 3D CT volumes (807 GB) |
| [FLARE-Task4-MRI-FM](https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task4-MRI-FM) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 10,000+ unlabeled 3D MRI volumes for pretraining, plus smaller labeled downstream sets |
| [MedVision](https://huggingface.co/datasets/YongchengYAO/MedVision) | CT, MRI, PET, X-ray | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 29K 3D images / 11.2M 2D slices (~1TB complete) |
| [PancancerCTSeg](https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg) | CT | 2025 | 🟢 NIfTI | — | ✅ | — | REQUEST | ~1.24 TB; 17,000+ labeled CT scans plus unlabeled and validation subsets |
| [PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) | CT | 2025 | 🟢 NIfTI | — | — | — | OPEN | ~160,000 CT volumes; ~5.63TB |
| [RadImageNet-VQA](https://huggingface.co/datasets/raidium/RadImageNet-VQA) | CT, MRI | 2025 | 🟡 Parquet | ✅ | — | — | REGISTRATION | ~77 GB; 750K images with ~7.5M generated samples (750K captions + 6.75M QA pairs) |
| [GMAI-MMBench](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench) | CT, MRI, X-ray, PET | 2024 | 🟡 TSV | ✅ | — | — | REGISTRATION | ~26K cases (25,726 QA) from 284 datasets across 38 modalities |
| [IMed-361M](https://huggingface.co/datasets/General-Medical-AI/IMed-361M) | CT, MRI, X-ray, PET | 2024 | 🟢 NPZ, PNG, NIfTI | — | ✅ | — | REGISTRATION | 287 GB; ~6.4M image-mask pairs with 361 million masks |
| [M3D-Seg](https://huggingface.co/datasets/GoodBaiBai88/M3D-Seg) | CT | 2024 | 🟡 NPY, NPZ, JSON | ✅ | ✅ | — | OPEN | ~5,772 3D CT images with 149,196 3D mask annotations (~240 GB), aggregated from 25 datasets |
| [MedPix-2.0](https://huggingface.co/datasets/architojha/medpix-2.0-dataset) | CT, MRI, X-ray | 2024 | 🟡 Parquet | ✅ | — | — | OPEN | 2,050 image-text case items |
| [MedTrinity-25M](https://huggingface.co/datasets/UCSC-VLAA/MedTrinity-25M) | CT, MRI, X-ray | 2024 | 🟡 JPEG, PNG | ✅ | ✅ | — | REGISTRATION | ~25M images (18M accessible image-text pairs) across 10 modalities |
| [OmniMedVQA](https://huggingface.co/datasets/foreverbeliever/OmniMedVQA) | CT, MRI, X-ray | 2024 | 🟡 PNG, JSON | ✅ | — | — | OPEN | 118,010 images / 127,995 QA items from 73 source datasets |
| [ROCOv2](https://doi.org/10.5281/zenodo.10821435) | X-ray, CT, MRI, PET | 2024 | 🟡 JPG | ✅ | — | — | OPEN | 79,789 images with captions and UMLS concepts |
| [VoComni](https://huggingface.co/datasets/Luffy503/VoComni) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 20,000 CT volumes; ~1.7TB |
| [CMB-AML](https://www.cancerimagingarchive.net/collection/cmb-aml/) | CT, MRI, PET, X-ray | 2023 | 🟢 DICOM, SVS, JSON | ✅ | — | — | OPEN | 448.08 GB, 16 subjects |
| [PMC-OA](https://huggingface.co/datasets/axiong/pmc_oa) | X-ray, CT, MRI, PET | 2023 | 🟡 JPG | ✅ | — | — | OPEN | 1.6 million image-caption pairs |
| [PMC-VQA](https://huggingface.co/datasets/xmcmic/PMC-VQA) | CT, MRI, X-ray | 2023 | 🟡 JPEG, CSV | ✅ | — | — | OPEN | ~149K images, ~227K question-answer pairs (21.8 GB) |
| [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M) | CT, MRI, X-ray | 2023 | 🟡 PNG, JSON | — | ✅ | ✅ | OPEN | ~16M images / 20M masks (16M version publicly released), 353 GB |
| [ULS23](https://uls23.grand-challenge.org/) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | ~38,000 lesion VOIs across multi-part release; e.g. Part 1 = 1,618 lesions, 15.9 GB |
| [RadImageNet](https://www.radimagenet.com/) | CT, MRI | 2022 | 🟡 DICOM, PNG | — | — | — | REQUEST | ~1.35 million annotated images from 131,000+ patients (CT, MRI, ultrasound) |
| [SLAKE](https://www.med-vqa.com/slake/) | X-ray, CT, MRI | 2021 | 🟡 PNG | ✅ | ✅ | — | OPEN | 642 images with 14,028 QA pairs |
| [MedICaT](https://github.com/allenai/medicat) | X-ray, CT, MRI | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 217,060 figures from 131,410 papers |
| [DeepLesion](https://nihcc.app.box.com/v/DeepLesion) | CT | 2018 | 🟡 PNG | — | — | — | OPEN | 32,735 lesions on 32,120 CT slices from 4,427 patients (~225 GB) |
| [ROCO](https://github.com/razorx89/roco-dataset) | X-ray, CT, MRI, PET | 2018 | 🟡 JPG, PNG | ✅ | — | — | OPEN | ~81,000 radiology image-caption pairs |
| [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) | X-ray, CT, MRI | 2018 | 🟡 JPG | ✅ | — | — | OPEN | 315 images with 3,515 QA pairs |

### 🗄️ Data Repositories & Portals  <sub>(16)</sub>

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
| [UK Biobank Imaging](https://www.ukbiobank.ac.uk/) | Multiple | 2014 | 🟢 Various | — | — | ✅ | REQUEST | 100,000 participants; 1B+ images |
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
