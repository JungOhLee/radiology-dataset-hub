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

**245 curated datasets** · 109 CT · 105 MRI · 24 PET · 58 X-ray · 205 native DICOM/NIfTI · 58 with reports/text · 158 with segmentation labels

Jump to: [Neuro (Brain & Spine)](#neuro-brain-spine) · [Chest & Thorax](#chest-thorax) · [Cardiac](#cardiac) · [Vascular](#vascular) · [Abdominal](#abdominal) · [Pelvic & Prostate](#pelvic-prostate) · [Musculoskeletal](#musculoskeletal) · [Breast](#breast) · [Head & Neck](#head-neck) · [Dental & Maxillofacial](#dental-maxillofacial) · [Whole-Body & PET](#whole-body-pet) · [Multiple / Various body parts](#multiple-various-body-parts) · [Data Repositories & Portals](#data-repositories-portals)

**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). Text = paired reports/captions/QA (i.e. image–text / multimodal) · Seg = segmentation masks · Multi = multi-sequence MRI or multi-phase CT. Access: OPEN = direct download · REGISTRATION = free account · DUA = data-use agreement · REQUEST = apply for access. **Datasets covering several body regions (7) appear under each region.**

### 🧠 Neuro (Brain & Spine)  <sub>(51)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [MR-RATE](https://huggingface.co/datasets/Forithmus/MR-RATE) | MRI | 2025 | 🟢 NIfTI, CSV | ✅ | ✅ | ✅ | REGISTRATION | 705,254 MRI volumes from 98,334 studies of 83,425 patients (~8-38 TB across repositories) |
| [OpenMind](https://huggingface.co/datasets/AnonRes/OpenMind) | MRI | 2025 | 🟢 NIfTI | — | — | ✅ | OPEN | ~114K MRI images (1.04 TB) curated from 800 OpenNeuro datasets across 30+ scanners |
| [RSNA 2025 Aneurysm Detection](https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection) | CT, MRI | 2025 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 4,000+ studies (CTA/MRA/MRI); ~200 with segmentation |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [BraTS 2024 Post-Treatment Glioma (BraTS-GLI)](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2200 multi-institutional post-treatment MRI cases |
| [BraTS-GoAT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | Pooled multi-tumor BraTS cohort (thousands of cases across glioma, meningioma, metastases, pediatric) |
| [BraTS-MEN-RT 2024](https://www.synapse.org/Synapse:syn53708249) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 750 radiotherapy-planning brain MRIs (multi-institutional) with expert GTV annotations on the training/validation partitions |
| [ISLES 2024](https://isles-24.grand-challenge.org/) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~150 training cases |
| [MSLesSeg 2024](https://iplab.dmi.unict.it/mfs/ms-les-seg/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~90 patients, ~150 MRI timepoints (1-5 per patient) |
| [UCSF-ALPTDG](https://imagingdatasets.ucsf.edu/dataset/2) | MRI | 2024 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 298 patients; 596 post-treatment MRI exams (two consecutive posttreatment timepoints per patient) |
| [BraTS-Africa](https://www.cancerimagingarchive.net/collection/BraTS-Africa/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 146 patients |
| [BraTS-MEN](https://www.synapse.org/Synapse:syn51514106) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 1,650 cases (1,000 public training) |
| [BraTS-Mets](https://www.synapse.org/Synapse:syn51156910/wiki/622553) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 328 cases (238 public training) |
| [BraTS-PEDs](https://www.synapse.org/Synapse:syn51156910/wiki/622461) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 228 patients (99 public training) |
| [Burdenko-GBM-Progression](https://www.cancerimagingarchive.net/collection/burdenko-gbm-progression/) | CT, MRI | 2023 | 🟢 DICOM | — | ✅ | ✅ | DUA | 180 patients; 645 studies; 4,956 series; 344,003 images; 131.23 GB |
| [M4Raw](https://github.com/mylyu/M4Raw) | MRI | 2023 | 🟡 HDF5 | — | — | ✅ | OPEN | — |
| [Meningioma-SEG-CLASS](https://www.cancerimagingarchive.net/collection/meningioma-seg-class/) | MRI | 2023 | 🟢 DICOM, XLSX | — | ✅ | ✅ | DUA | 96 patients (180 studies, 674 series, 47,520 images, 9.39 GB) |
| [RHUH-GBM](https://www.cancerimagingarchive.net/collection/rhuh-gbm/) | MRI | 2023 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 40 patients; ~600 series, 37,425 DICOM images (15.96 GB) plus 2.9 GB NIfTI |
| [ReMIND](https://www.cancerimagingarchive.net/collection/remind/) | MRI | 2023 | 🟢 DICOM, NRRD | ✅ | ✅ | ✅ | OPEN | 114 subjects; 43.6 GB (preop MRI 4 sequences, 301 intraop MRI series, 320 intraop 3D US series) |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [ATLAS R2.0](https://atlas.grand-challenge.org/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 655 labeled T1w MRIs (+300 hidden test) |
| [INSTANCE 2022](https://instance.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 NCCT scans (100 train) |
| [ISLES 2022](https://zenodo.org/records/7153326) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 250 training cases |
| [LUMIERE](https://springernature.figshare.com/articles/dataset/The_LUMIERE_Dataset/16944846) | MRI | 2022 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 91 patients, 638 study dates, 2487 MRI images (~32.5 GB imaging ZIP) |
| [RSNA 2022 Cervical Spine Fracture](https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection) | CT | 2022 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~3,000 CT studies |
| [Shifts MS](https://zenodo.org/records/7051658) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [UCSF-PDGM](https://www.cancerimagingarchive.net/collection/ucsf-pdgm/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 495 patients |
| [UPenn-GBM](https://www.cancerimagingarchive.net/collection/upenn-gbm/) | MRI | 2022 | 🟢 NIfTI, DICOM | — | ✅ | ✅ | OPEN | 630 glioblastoma patients |
| [BraTS 2021](https://www.synapse.org/Synapse:syn25829067) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2,040 patients (1,251 public training) |
| [FeTA](https://www.synapse.org/Synapse:syn25649159) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | DUA | ~80 subjects (FeTA 2021) |
| [GLIS-RT](https://www.cancerimagingarchive.net/collection/glis-rt/) | CT, MRI | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 230 patients (28.26 GB) |
| [MSSEG-2](https://portal.fli-iam.irisa.fr/msseg-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 patients, 2 time-points each |
| [ADAM](https://adam.isi.uu.nl/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 113 training TOF-MRA cases |
| [CADA](https://cada.grand-challenge.org/) | X-ray | 2020 | 🟢 NIfTI, STL | — | ✅ | — | REGISTRATION | 131 3DRA datasets (115 patients) |
| [EPISURG](https://rdr.ucl.ac.uk/articles/dataset/EPISURG/9996158) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 430 postoperative T1w MRIs |
| [VerSe](https://github.com/anjany/verse) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 374 CT scans / ~4,500 vertebrae |
| [fastMRI Brain](https://fastmri.med.nyu.edu) | MRI | 2020 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | 6,970 brain MRI volumes |
| [ACRIN-FMISO-Brain](https://www.cancerimagingarchive.net/collection/acrin-fmiso-brain/) | PET, MRI, CT | 2019 | 🟢 DICOM | ✅ | ✅ | ✅ | OPEN | 96 GB |
| [OASIS-3](https://sites.wustl.edu/oasisbrains/) | MRI, PET | 2019 | 🟢 NIfTI | — | ✅ | ✅ | DUA | 1378 participants |
| [RSNA 2019 ICH Detection](https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection) | CT | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 25,272 non-contrast head CT exams |
| [iSeg](https://iseg2019.web.unc.edu) | MRI | 2019 | 🟢 Analyze | — | ✅ | ✅ | DUA | iSeg-2019: 39 subjects (multi-site) |
| [CQ500](http://headctstudy.qure.ai/dataset) | CT | 2018 | 🟢 DICOM | — | — | — | OPEN | 491 head CT scans |
| [Calgary-Campinas CC-359](https://www.ccdataset.com) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 359 T1w volumes (+ raw k-space subset) |
| [MRBrainS](https://mrbrains18.isi.uu.nl) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | MRBrainS18: 30 subjects (7 fully annotated) |
| [HCP Young Adult](https://www.humanconnectome.org/study/hcp-young-adult) | MRI | 2017 | 🟢 NIfTI, CIFTI | — | ✅ | ✅ | REGISTRATION | 1206 subjects |
| [WMH Segmentation Challenge](https://wmh.isi.uu.nl/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 60 training subjects |
| [ABIDE](https://fcon_1000.projects.nitrc.org/indi/abide/) | MRI | 2012 | 🟢 NIfTI | — | — | ✅ | REGISTRATION | 1112 subjects (ABIDE I) |
| [Mindboggle-101](https://mindboggle.info/data.html) | MRI | 2012 | 🟢 NIfTI, VTK | — | ✅ | — | OPEN | 101 subjects |
| [OASIS-1](https://sites.wustl.edu/oasisbrains/) | MRI | 2007 | 🟢 NIfTI, Analyze | — | ✅ | — | DUA | 416 subjects |
| [ADNI](https://adni.loni.usc.edu/) | MRI, PET | 2004 | 🟢 DICOM, NIfTI | — | — | ✅ | REQUEST | 2000+ participants (ADNI 1/GO/2/3/4) |
| [IXI](https://brain-development.org/ixi-dataset/) | MRI | — | 🟢 NIfTI | — | — | ✅ | OPEN | ~600 healthy subjects |

### 🫁 Chest & Thorax  <sub>(54)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [LUNA25](https://luna25.grand-challenge.org/) | CT | 2025 | 🟢 MHA | — | — | — | REGISTRATION | Over 4,000 annotated low-dose chest CT exams for development, 468 hidden test cases, 300 reader-study cases |
| [ReXGradient-160K](https://huggingface.co/datasets/rajpurkarlab/ReXGradient-160K) | X-ray | 2025 | 🟡 PNG, CSV | ✅ | — | — | REGISTRATION | 273,004 images from 160,000 studies of 109,487 patients across 79 sites (3 U.S. health systems) |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 25,692 CT volumes (50,188 with reconstructions) from 21,304 patients; ~21.3 TB |
| [CheXpert Plus](https://huggingface.co/datasets/StanfordAIMI/CheXpert-Plus) | X-ray | 2024 | 🟢 DICOM, PNG | ✅ | — | — | DUA | 223,228 chest radiographs paired with 187,711 radiology reports from 64,725 patients |
| [DRR-RATE](https://huggingface.co/datasets/farrell236/DRR-RATE) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | OPEN | 50,188 digitally reconstructed radiographs (~8 GB) |
| [PadChest-GR](https://bimcv.cipf.es/bimcv-projects/padchest-gr/) | X-ray | 2024 | 🟡 PNG | ✅ | — | — | DUA | 4,555 CXR studies (3,099 abnormal, 1,456 normal); 7,037 positive and 3,422 negative finding sentences; ~46 GB |
| [RadGenome-ChestCT](https://huggingface.co/datasets/RadGenome/RadGenome-ChestCT) | CT | 2024 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 25,692 CT volumes with 665K grounded report regions + 1.3M VQA |
| [INSPECT](https://inspect.stanford.edu/) | CT | 2023 | 🟢 DICOM | ✅ | — | — | DUA | 23,248 CTPA studies / 19,402 patients with reports and EHR |
| [LNQ2023](https://lnq2023.grand-challenge.org/) | CT | 2023 | 🟢 DICOM, NRRD, NIfTI | — | ✅ | — | REGISTRATION | 513 subjects (~35 GB) on TCIA |
| [MAIDA](https://maida.stanford.edu/) | X-ray | 2023 | 🟢 DICOM, PNG | ✅ | — | — | REGISTRATION | multi-institution chest X-rays across 22+ hospitals in 12 countries |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/) | X-ray | 2023 | 🟡 JPG | ✅ | — | — | DUA | 700,703 QA pairs over 164,324 image pairs |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [BRAX](https://physionet.org/content/brax/) | X-ray | 2022 | 🟢 DICOM, PNG | — | — | — | DUA | 40,967 images / 19,351 patients |
| [MS-CXR](https://physionet.org/content/ms-cxr/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 1,162 image-sentence bounding-box pairs across 8 findings |
| [NODE21](https://node21.grand-challenge.org/) | X-ray, CT | 2022 | 🟢 MHA | — | — | — | OPEN | 4,882 frontal chest radiographs (1,134 with 1,476 nodule bounding boxes; 3,748 nodule-free) plus LUNA16-derived CT nodule patches |
| [REFLACX](https://physionet.org/content/reflacx-xray-localization/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 3,032 eye-tracking + report sessions for 2,616 chest X-rays |
| [VinDr-PCXR](https://physionet.org/content/vindr-pcxr/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 9,125 studies (children under 10) |
| [CANDID-PTX](https://figshare.com/articles/dataset/CANDID-PTX/14173982) | X-ray | 2021 | 🟢 DICOM | ✅ | ✅ | — | REQUEST | 19,237 adult chest X-rays |
| [Chest ImaGenome](https://physionet.org/content/chest-imagenome/) | X-ray | 2021 | 🟡 JPG | ✅ | — | — | DUA | 242,072 frontal CXRs with scene graphs |
| [ChestX-Det](https://github.com/Deepwise-AILab/ChestX-Det-Dataset) | X-ray | 2021 | 🟡 PNG, JSON | — | ✅ | — | OPEN | 3,578 chest X-ray images (from NIH ChestX-ray14) |
| [SIIM-FISABIO-RSNA COVID-19](https://www.kaggle.com/c/siim-covid19-detection) | X-ray | 2021 | 🟢 DICOM, CSV | — | — | — | REGISTRATION | ~6,334 chest radiographs (training) |
| [VinDr-CXR](https://physionet.org/content/vindr-cxr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 18,000 images (15,000 train / 3,000 test) |
| [ACRIN-NSCLC-FDG-PET](https://www.cancerimagingarchive.net/collection/acrin-nsclc-fdg-pet/) | PET, CT | 2020 | 🟢 DICOM | ✅ | ✅ | — | OPEN | 145.5 GB |
| [BIMCV-COVID19](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/) | X-ray, CT | 2020 | 🟢 PNG, DICOM | ✅ | ✅ | — | REGISTRATION | 21,342 CR + 34,829 DX studies + 7,918 CT (positive partition) |
| [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) | X-ray | 2020 | 🟡 PNG | — | ✅ | — | REGISTRATION | 21,165 images (4 classes) |
| [COVID-19-CT-Seg](https://zenodo.org/records/3757476) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 20 labeled CT scans |
| [COVIDx CXR](https://github.com/lindawangg/COVID-Net) | X-ray | 2020 | 🟡 PNG | — | — | — | REGISTRATION | COVIDx CXR-3: ~29,986 images / 16,648 patients |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [Lung-PET-CT-Dx](https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/) | CT, PET | 2020 | 🟢 DICOM | — | — | ✅ | OPEN | 355 patients / 251,135 DICOM images |
| [MosMedData](https://academictorrents.com/details/f2175c4676e041ea65568bb70c2bcd15c7325fd2) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,110 CT studies (~50 with masks) |
| [Object-CXR](https://github.com/hlk-1135/object-CXR) | X-ray | 2020 | 🟡 JPEG | — | — | — | OPEN | 10,000 frontal X-rays (5,000 with foreign objects) |
| [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) | X-ray | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 160,868 images / 67,625 patients |
| [RSNA-STR Pulmonary Embolism CT](https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection) | CT | 2020 | 🟢 DICOM | — | — | — | REGISTRATION | 7,279 CTPA studies (public training set) |
| [TBX11K](https://mmcheng.net/tb/) | X-ray | 2020 | 🟡 PNG, XML, JSON | — | — | — | OPEN | 11,200 chest X-ray images at 512x512 |
| [Anti-PD-1_Lung](https://www.cancerimagingarchive.net/collection/anti-pd-1_lung/) | PET, CT | 2019 | 🟢 DICOM | ✅ | ✅ | — | REGISTRATION | 61 GB |
| [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) | X-ray | 2019 | 🟡 JPEG | — | — | — | REGISTRATION | 224,316 radiographs / 65,240 patients |
| [LNDb](https://lndb.grand-challenge.org/) | CT | 2019 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | REGISTRATION | 294 CT scans |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/) | X-ray | 2019 | 🟢 DICOM | ✅ | — | — | DUA | 377,110 images / 227,835 studies / ~65,379 patients |
| [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/) | X-ray | 2019 | 🟡 JPEG | — | — | — | DUA | 377,110 JPG images / 227,827 studies |
| [SIIM-ACR Pneumothorax](https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation) | X-ray | 2019 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~12,047 train + ~3,205 test |
| [RSNA Pneumonia Detection](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) | X-ray | 2018 | 🟢 DICOM | — | — | — | REGISTRATION | ~26,684 training radiographs |
| [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 112,120 frontal images / 30,805 patients |
| [LUNA16](https://luna16.grand-challenge.org/) | CT | 2016 | 🟢 MetaImage (.mhd/.raw) | — | ✅ | — | OPEN | 888 CT scans / 1,186 nodule annotations |
| [NSCLC-Radiogenomics](https://www.cancerimagingarchive.net/collection/nsclc-radiogenomics/) | CT, PET | 2015 | 🟢 DICOM, CSV | ✅ | ✅ | ✅ | OPEN | 211 patients (CT and PET/CT; RNA-seq for 130) |
| [Montgomery County CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | ✅ | — | OPEN | 138 frontal X-rays (80 normal, 58 TB) |
| [NSCLC-Radiomics](https://www.cancerimagingarchive.net/collection/nsclc-radiomics/) | CT | 2014 | 🟢 DICOM, CSV | ✅ | ✅ | — | OPEN | 422 patients (tumor segmentations for 318) |
| [Shenzhen Hospital CXR Set](https://openi.nlm.nih.gov/) | X-ray | 2014 | 🟡 PNG | ✅ | — | — | OPEN | 662 frontal X-rays (326 normal, 336 TB) |
| [NLST](https://www.cancerimagingarchive.net/collection/nlst/) | CT | 2013 | 🟢 DICOM | — | — | — | OPEN | 26,254 subjects / 73,116 CT studies |
| [Open-i / Indiana University CXR](https://openi.nlm.nih.gov/) | X-ray | 2013 | 🟢 DICOM, PNG | ✅ | — | — | OPEN | 7,470 images / 3,955 reports |
| [LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/) | CT | 2011 | 🟢 DICOM, XML | — | ✅ | — | OPEN | 1,018 CT scans / 1,010 patients |
| [EMPIRE10](https://empire10.grand-challenge.org/) | CT | 2010 | 🟢 MetaImage (.mhd/.raw) | — | — | — | REGISTRATION | 30 intra-subject chest CT scan pairs |
| [JSRT](http://db.jsrt.or.jp/eng.php) | X-ray | 2000 | 🟡 IMG | — | — | — | REGISTRATION | 247 posterior-anterior chest radiographs (154 with a lung nodule: 100 malignant, 54 benign; 93 without nodules); 2048x2048, 12-bit, 0.175 mm pixel spacing |

### 🫀 Cardiac  <sub>(14)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMRxRecon2024](https://cmrxrecon.github.io/2024/) | MRI | 2024 | 🟢 MATLAB | — | — | ✅ | REGISTRATION | 330 healthy volunteers (200 training, 60 validation, 70 test) |
| [CMRxRecon](https://cmrxrecon.github.io/) | MRI | 2023 | 🟢 MATLAB (.mat k-space) | — | ✅ | ✅ | REGISTRATION | 300 subjects |
| [CMRxMotion](https://www.synapse.org/Synapse:syn28503327) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | ~40 healthy volunteers imaged under 4 respiratory-motion levels |
| [LAScarQS 2022](https://zmiclab.github.io/projects/lascarqs22/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 194 LGE-MRI |
| [M&Ms-2](https://www.ub.edu/mnms-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 360 patients |
| [EMIDEC](http://emidec.com/) | MRI | 2020 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 150 cases (50 normal, 100 pathological) |
| [M&Ms](https://www.ub.edu/mnms/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 375 patients (multi-vendor) |
| [MyoPS 2020](https://zmiclab.github.io/zxh/0/myops20/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 45 patients (25 train + 20 test) |
| [Atria Seg 2018](https://www.cardiacatlas.org/atriaseg2018-challenge/) | MRI | 2018 | 🟢 NRRD | — | ✅ | — | REGISTRATION | 154 3D LGE-MRI (100 train + 54 test) |
| [MSD Heart (Task02)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | — | OPEN | 30 cases (20 train + 10 test) |
| [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/) | MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 150 patients (100 train + 50 test) |
| [MM-WHS](https://zmiclab.github.io/zxh/0/mmwhs/) | CT, MRI | 2017 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 120 images (60 CT/CTA + 60 MRI) |
| [RVSC](https://rvsc.projets.litislab.fr/) | MRI | 2012 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 48 patients (16 train + 32 test) |
| [Sunnybrook Cardiac Data](https://www.cardiacatlas.org/sunnybrook-cardiac-data/) | MRI | 2009 | 🟢 DICOM | — | ✅ | — | OPEN | 45 patients |

### 🩸 Vascular  <sub>(11)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [AortaSeg24](https://aortaseg24.grand-challenge.org/) | CT | 2024 | 🟢 MHA, NIfTI | — | ✅ | — | REGISTRATION | 100 annotated CTA volumes |
| [TopCoW 2024](https://topcow24.grand-challenge.org/) | CT, MRI | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 125 training patients (250 paired CTA+MRA images), plus 10 validation and 70 test pairs |
| [CAS2023](https://codalab.lisn.upsaclay.fr/competitions/9804) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 TOF-MRA training cases |
| [ImageCAS](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REQUEST | 1000 patients |
| [AVT](https://figshare.com/articles/dataset/Aortic_Vessel_Tree_AVT_CTA_Datasets_and_Segmentations/14806362) | CT | 2022 | 🟢 NRRD | — | ✅ | — | OPEN | 56 aortas (3 collections) |
| [Lausanne TOF-MRA Aneurysm Cohort](https://openneuro.org/datasets/ds003949) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 284 subjects (157 aneurysm patients, 127 healthy controls) |
| [Parse2022](https://parse2022.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 CTPA volumes (100 train, 30 validation, 70 test) |
| [COCA (Stanford)](https://aimi.stanford.edu/datasets/coca-coronary-calcium-chest-ct) | CT | 2021 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~1000 patients (789 gated + 214 non-gated) |
| [ASOCA](https://asoca.grand-challenge.org/) | CT | 2020 | 🟢 NRRD | — | ✅ | — | DUA | 60 cases (40 train + 20 test) |
| [orCaScore](https://orcascore.grand-challenge.org/) | CT | 2014 | 🟢 MHD | — | ✅ | — | REGISTRATION | 72 patients (32 train + 40 test) |
| [VESSEL12](https://vessel12.grand-challenge.org/) | CT | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 20 chest CT scans |

### 🫃 Abdominal  <sub>(36)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [AbdomenAtlas 3.0](https://github.com/MrGiovanni/RadGPT) | CT | 2025 | 🟢 NIfTI | ✅ | ✅ | ✅ | OPEN | 9,262 CT volumes (3,220 with a contrast-enhanced phase) + reports |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [AbdomenAtlas 1.0](https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas1.0Mini) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | DUA | 5,195 annotated CT volumes, 326 GB |
| [AbdomenAtlas 1.1](https://github.com/MrGiovanni/AbdomenAtlas) | CT | 2024 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 9,262 CT volumes; >251,000 masks |
| [CURVAS](https://curvas.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | 90 CT scans (training set ~6.3 GB) |
| [FLARE 2024](https://www.codabench.org/competitions/2320/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | Thousands of partially labeled and unlabeled abdominal CT scans (large semi-supervised set) |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients (>6M images) |
| [PANORAMA](https://panorama.grand-challenge.org/) | CT | 2024 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | ~2,238 CECT training scans (two centers) plus 194 MSD and 80 NIH external cases; ~197 GB |
| [ATLAS](https://atlas-challenge.u-bourgogne.fr/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 90 T1 contrast-enhanced MRI scans (60 train / 30 test) from 90 unresectable HCC patients |
| [Adrenal-ACC-Ki67-Seg](https://www.cancerimagingarchive.net/collection/adrenal-acc-ki67-seg/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 53 patients; 65 studies; 177 series; 18,255 images; ~9.9 GB |
| [Colorectal-Liver-Metastases](https://www.cancerimagingarchive.net/collection/colorectal-liver-metastases/) | CT | 2023 | 🟢 DICOM | — | ✅ | — | OPEN | 197 patients |
| [FLARE23](https://codalab.lisn.upsaclay.fr/competitions/12239) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 4000 train + 100 val + 400 test CT |
| [KiTS23](https://kits-challenge.org/kits23/) | CT | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 599 CT (489 train / 110 test) |
| [LLD-MMRI](https://github.com/LMMMEng/LLD-MMRI-Dataset) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | REQUEST | 498 patients, 8 sequences each |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [FLARE22](https://flare22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 2300 CT (50 labeled + 2000 unlabeled train) |
| [WORD](https://github.com/HiLab-git/WORD) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 150 CT (100 train / 20 val / 30 test) |
| [AbdomenCT-1K](https://github.com/JunMa11/AbdomenCT-1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 1112 CT from 12 centers |
| [FLARE21](https://flare.grand-challenge.org/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 511 CT (361 train / 50 val / 100 test) |
| [HCC-TACE-Seg](https://www.cancerimagingarchive.net/collection/hcc-tace-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 105 patients; ~28.6 GB |
| [KiTS21](https://kits-challenge.org/kits21/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 train + 100 test CT |
| [Pancreatic-CT-CBCT-SEG](https://www.cancerimagingarchive.net/collection/pancreatic-ct-cbct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 40 patients (~14.3 GB, 370 series, 24,246 images) |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
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

### ⬇️ Pelvic & Prostate  <sub>(12)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [Merlin](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | DUA | 25,494 abdominal/pelvic CT scans from 18,317 patients (>6M images) |
| [fastMRI Prostate](https://fastmri.med.nyu.edu/) | MRI | 2024 | 🟡 HDF5 | — | — | ✅ | DUA | — |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [PI-CAI](https://pi-cai.grand-challenge.org/) | MRI | 2022 | 🟢 MHA, NIfTI | — | ✅ | ✅ | OPEN | 1500 bpMRI (1476 patients, public set) |
| [Prostate158](https://github.com/kbressem/prostate158) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 158 studies (139 train / 19 test) |
| [Prostate-MRI-US-Biopsy](https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/) | MRI | 2020 | 🟢 DICOM, STL, XLSX | ✅ | ✅ | ✅ | OPEN | 1,151 subjects; 2,799 studies; ~80 GB |
| [Gold Atlas](https://zenodo.org/records/583096) | MRI, CT | 2018 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 19 patients, ~1.7 TB |
| [MSD Prostate (Task05)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 48 mpMRI (32 train / 16 test) |
| [ProstateX](https://www.cancerimagingarchive.net/collection/prostatex/) | MRI | 2017 | 🟢 DICOM | — | — | ✅ | OPEN | 346 patients (330 lesions train) |
| [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/) | CT | 2015 | 🟢 DICOM | — | — | — | OPEN | 825 patients (prone + supine) |
| [PROMISE12](https://promise12.grand-challenge.org/) | MRI | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 50 train + 30 test T2W MRI |

### 🦴 Musculoskeletal  <sub>(17)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [PENGWIN](https://pengwin.grand-challenge.org/) | CT, X-ray | 2024 | 🟢 MHA, TIFF | — | ✅ | — | REGISTRATION | 150 patient CT scans plus synthetically generated 2D X-ray images |
| [RSNA 2024 Lumbar Spine Degenerative Classification](https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification) | MRI | 2024 | 🟢 DICOM | — | — | ✅ | REGISTRATION | ~1975 lumbar spine MRI studies |
| [SPIDER](https://zenodo.org/records/10159290) | MRI | 2024 | 🟢 MHA | — | ✅ | ✅ | OPEN | 218 studies, 447 sagittal T1/T2 MRI series (~3.8 GB) |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [K2S](https://k2s.grand-challenge.org/) | MRI | 2022 | 🟡 HDF5 | — | ✅ | — | REGISTRATION | — |
| [SKM-TEA](https://aimi.stanford.edu/datasets/skm-tea-knee-mri) | MRI | 2021 | 🟢 HDF5 (k-space), DICOM | — | ✅ | — | REGISTRATION | 155 qDESS knee scans (~1.6 TB) |
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

### 🎀 Breast  <sub>(15)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [MAMA-MIA](https://www.ub.edu/mama-mia/) | MRI | 2025 | 🟢 NIfTI, DICOM | ✅ | ✅ | ✅ | DUA | 1,506 annotated training scans plus 574 external validation cases (multi-institutional) |
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

### 👤 Head & Neck  <sub>(10)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [HNTS-MRG 2024](https://hntsmrg24.grand-challenge.org/) | MRI | 2024 | 🟢 NIfTI | — | ✅ | — | OPEN | ~150 training patients (pre-RT and mid-RT), ~50 test patients |
| [RADCURE](https://www.cancerimagingarchive.net/collection/radcure/) | CT | 2024 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 3,346 patients |
| [SegRap2023](https://segrap2023.grand-challenge.org/) | CT | 2023 | 🟢 NIfTI, MHA | — | ✅ | ✅ | DUA | 400 CT scans (200 patients, paired contrast-enhanced + non-contrast); 120 train, 20 validation, 60 test |
| [HECKTOR](https://hecktor.grand-challenge.org/) | PET, CT | 2022 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | ~882 cases (2022 edition) |
| [ACRIN-HNSCC-FDG-PET-CT](https://www.cancerimagingarchive.net/collection/acrin-hnscc-fdg-pet-ct/) | PET, CT, MRI | 2021 | 🟢 DICOM | ✅ | ✅ | — | DUA | 147.77 GB |
| [HNSCC](https://www.cancerimagingarchive.net/collection/hnscc/) | CT, PET, MRI | 2020 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 627 patients |
| [HN1](https://www.cancerimagingarchive.net/collection/head-neck-radiomics-hn1/) | CT | 2019 | 🟢 DICOM, RTSTRUCT, SEG | ✅ | ✅ | — | DUA | 137 patients |
| [Head-Neck-PET-CT](https://www.cancerimagingarchive.net/collection/head-neck-pet-ct/) | PET, CT | 2017 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 298 patients |
| [QIN-HeadNeck](https://www.cancerimagingarchive.net/collection/qin-headneck/) | PET, CT | 2015 | 🟢 DICOM, SEG, SR | ✅ | ✅ | — | REQUEST | 279 subjects |
| [TCGA-HNSC](https://www.cancerimagingarchive.net/collection/tcga-hnsc/) | CT, PET, MRI | 2014 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 227 patients (479 studies) |

### 🦷 Dental & Maxillofacial  <sub>(4)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [ToothFairy2](https://toothfairy2.grand-challenge.org/) | CT | 2024 | 🟢 MHA | — | ✅ | — | REGISTRATION | 480 public training CBCT volumes |
| [DENTEX](https://dentex.grand-challenge.org/) | X-ray | 2023 | 🟡 PNG | — | — | — | OPEN | 1,005 fully-annotated panoramic X-rays (3,903 total) |
| [CTooth](https://github.com/liangjiubujiu/CTooth) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 22 annotated CBCT volumes (CTooth+ adds 146 unlabeled) |
| [Tufts Dental Database](https://tdd.ece.tufts.edu/) | X-ray | 2022 | 🟡 JPG, TIFF | ✅ | ✅ | — | REQUEST | 1,000 panoramic X-rays |

### 🌐 Whole-Body & PET  <sub>(9)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [TotalSegmentator-MRI](https://zenodo.org/records/14710732) | MRI | 2025 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 616 MRI images (~5.1 GB compressed archive) |
| [PSMA-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/psma-pet-ct-lesions/) | PET, CT | 2024 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 597 studies / 378 patients |
| [autoPET III](https://autopet-iii.grand-challenge.org/) | PET, CT | 2024 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 1,611 studies (1,014 FDG + 597 PSMA) |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [FDG-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/) | PET, CT | 2022 | 🟢 DICOM | — | ✅ | — | DUA | 1,014 studies / 900 patients |
| [autoPET I](https://autopet.grand-challenge.org/) | PET, CT | 2022 | 🟢 DICOM, NIfTI | — | ✅ | — | DUA | 1,014 studies / 900 patients (FDG) |
| [Pediatric-CT-SEG](https://www.cancerimagingarchive.net/collection/pediatric-ct-seg/) | CT | 2021 | 🟢 DICOM | — | ✅ | — | OPEN | 359 patients (ages 5 days to 16 years); 65.69 GB |
| [CT-ORG](https://www.cancerimagingarchive.net/collection/ct-org/) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 140 CT (119 train / 21 test) |
| [Anti-PD-1_Melanoma](https://www.cancerimagingarchive.net/collection/anti-pd-1_melanoma/) | PET, CT, MRI | 2018 | 🟢 DICOM | ✅ | — | — | REQUEST | 98.41 GB |

### 🧩 Multiple / Various body parts  <sub>(11)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [M3D-Seg](https://huggingface.co/datasets/GoodBaiBai88/M3D-Seg) | CT | 2024 | 🟡 NPY, NPZ, JSON | ✅ | ✅ | — | OPEN | ~5,772 3D CT images with 149,196 3D mask annotations (~240 GB), aggregated from 25 datasets |
| [MedTrinity-25M](https://huggingface.co/datasets/UCSC-VLAA/MedTrinity-25M) | CT, MRI, X-ray | 2024 | 🟡 JPEG, PNG | ✅ | ✅ | — | REGISTRATION | ~25M images (18M accessible image-text pairs) across 10 modalities |
| [ROCOv2](https://doi.org/10.5281/zenodo.10821435) | X-ray, CT, MRI, PET | 2024 | 🟡 JPG | ✅ | — | — | OPEN | 79,789 images with captions and UMLS concepts |
| [PMC-OA](https://huggingface.co/datasets/axiong/pmc_oa) | X-ray, CT, MRI, PET | 2023 | 🟡 JPG | ✅ | — | — | OPEN | 1.6 million image-caption pairs |
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
