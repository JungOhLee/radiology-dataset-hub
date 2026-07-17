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
- **Selection metadata on every card** — paired text, multi-sequence/phase, segmentation labels, license, access.
- **Organized by subspecialty / body region**, cross-cut by modality, so the list never feels overwhelming.
- **One machine-readable source** ([`data/datasets.json`](data/datasets.json)) generates both the website and the tables below — easy to query, easy to contribute to.

## How to use

- **Interactive site:** <https://jungohlee.github.io/radiology-dataset-hub/> — filter and search live.
- **Tables below:** browse by region right here on GitHub.
- **Programmatic:** fetch [`data/datasets.json`](data/datasets.json) directly.

---

<!-- AUTOGEN:START -->

**169 curated datasets** · 69 CT · 65 MRI · 17 PET · 45 X-ray · 143 native DICOM/NIfTI · 36 with reports/text · 105 with segmentation labels

Jump to: [Neuro (Brain & Spine)](#neuro-brain-spine) · [Chest & Thorax](#chest-thorax) · [Cardiac](#cardiac) · [Vascular](#vascular) · [Abdominal](#abdominal) · [Pelvic & Prostate](#pelvic-prostate) · [Musculoskeletal](#musculoskeletal) · [Breast](#breast) · [Head & Neck](#head-neck) · [Dental & Maxillofacial](#dental-maxillofacial) · [Whole-Body & PET](#whole-body-pet) · [Multimodal / Image–Text](#multimodal-imagetext) · [Data Repositories & Portals](#data-repositories-portals)

**Legend** — Format: 🟢 native raw (DICOM/NIfTI/NRRD) · 🟡 derived (PNG/JPEG). Text = paired reports/captions · Seg = segmentation masks · Multi = multi-sequence MRI or multi-phase CT. Access: OPEN = direct download · REGISTRATION = free account · DUA = data-use agreement · REQUEST = apply for access.

### 🧠 Neuro (Brain & Spine)  <sub>(32)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [RSNA 2025 Aneurysm Detection](https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection) | CT, MRI | 2025 | 🟢 DICOM | — | ✅ | ✅ | REGISTRATION | 4,000+ studies (CTA/MRA/MRI); ~200 with segmentation |
| [BraTS-Africa](https://www.cancerimagingarchive.net/collection/BraTS-Africa/) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 146 patients |
| [BraTS-MEN](https://www.synapse.org/Synapse:syn51514106) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 1,650 cases (1,000 public training) |
| [BraTS-Mets](https://www.synapse.org/Synapse:syn51156910/wiki/622553) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 328 cases (238 public training) |
| [BraTS-PEDs](https://www.synapse.org/Synapse:syn51156910/wiki/622461) | MRI | 2023 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 228 patients (99 public training) |
| [ATLAS R2.0](https://atlas.grand-challenge.org/) | MRI | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 655 labeled T1w MRIs (+300 hidden test) |
| [INSTANCE 2022](https://instance.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | DUA | 200 NCCT scans (100 train) |
| [ISLES 2022](https://zenodo.org/records/7153326) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 250 training cases |
| [RSNA 2022 Cervical Spine Fracture](https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection) | CT | 2022 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~3,000 CT studies |
| [Shifts MS](https://zenodo.org/records/7051658) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | — |
| [UPenn-GBM](https://www.cancerimagingarchive.net/collection/upenn-gbm/) | MRI | 2022 | 🟢 NIfTI, DICOM | — | ✅ | ✅ | OPEN | 630 glioblastoma patients |
| [BraTS 2021](https://www.synapse.org/Synapse:syn25829067) | MRI | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | ~2,040 patients (1,251 public training) |
| [FeTA](https://www.synapse.org/Synapse:syn25649159) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | DUA | ~80 subjects (FeTA 2021) |
| [MSSEG-2](https://portal.fli-iam.irisa.fr/msseg-2/) | MRI | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 100 patients, 2 time-points each |
| [ADAM](https://adam.isi.uu.nl/) | MRI | 2020 | 🟢 NIfTI | — | ✅ | ✅ | REGISTRATION | 113 training TOF-MRA cases |
| [CADA](https://cada.grand-challenge.org/) | X-ray | 2020 | 🟢 NIfTI, STL | — | ✅ | — | REGISTRATION | 131 3DRA datasets (115 patients) |
| [EPISURG](https://rdr.ucl.ac.uk/articles/dataset/EPISURG/9996158) | MRI | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 430 postoperative T1w MRIs |
| [VerSe](https://github.com/anjany/verse) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 374 CT scans / ~4,500 vertebrae |
| [fastMRI Brain](https://fastmri.med.nyu.edu) | MRI | 2020 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | 6,970 brain MRI volumes |
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

### 🫁 Chest & Thorax  <sub>(29)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [BRAX](https://physionet.org/content/brax/) | X-ray | 2022 | 🟢 DICOM, PNG | — | — | — | DUA | 40,967 images / 19,351 patients |
| [VinDr-PCXR](https://physionet.org/content/vindr-pcxr/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 9,125 studies (children under 10) |
| [CANDID-PTX](https://figshare.com/articles/dataset/CANDID-PTX/14173982) | X-ray | 2021 | 🟢 DICOM | ✅ | ✅ | — | REQUEST | 19,237 adult chest X-rays |
| [VinDr-CXR](https://physionet.org/content/vindr-cxr/) | X-ray | 2021 | 🟢 DICOM | — | — | — | DUA | 18,000 images (15,000 train / 3,000 test) |
| [BIMCV-COVID19](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/) | X-ray, CT | 2020 | 🟢 PNG, DICOM | ✅ | ✅ | — | REGISTRATION | 21,342 CR + 34,829 DX studies + 7,918 CT (positive partition) |
| [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) | X-ray | 2020 | 🟡 PNG | — | ✅ | — | REGISTRATION | 21,165 images (4 classes) |
| [COVID-19-CT-Seg](https://zenodo.org/records/3757476) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 20 labeled CT scans |
| [COVIDx CXR](https://github.com/lindawangg/COVID-Net) | X-ray | 2020 | 🟡 PNG | — | — | — | REGISTRATION | COVIDx CXR-3: ~29,986 images / 16,648 patients |
| [Lung-PET-CT-Dx](https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/) | CT, PET | 2020 | 🟢 DICOM | — | — | ✅ | OPEN | 355 patients / 251,135 DICOM images |
| [MosMedData](https://academictorrents.com/details/f2175c4676e041ea65568bb70c2bcd15c7325fd2) | CT | 2020 | 🟢 NIfTI | — | ✅ | — | OPEN | 1,110 CT studies (~50 with masks) |
| [Object-CXR](https://github.com/hlk-1135/object-CXR) | X-ray | 2020 | 🟡 JPEG | — | — | — | OPEN | 10,000 frontal X-rays (5,000 with foreign objects) |
| [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) | X-ray | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 160,868 images / 67,625 patients |
| [RSNA-STR Pulmonary Embolism CT](https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection) | CT | 2020 | 🟢 DICOM | — | — | — | REGISTRATION | 7,279 CTPA studies (public training set) |
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

### 🫀 Cardiac  <sub>(12)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [CMRxRecon](https://cmrxrecon.github.io/) | MRI | 2023 | 🟢 MATLAB (.mat k-space) | — | ✅ | ✅ | REGISTRATION | 300 subjects |
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

### 🩸 Vascular  <sub>(5)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [ImageCAS](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation-based-on-CT) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REQUEST | 1000 patients |
| [AVT](https://figshare.com/articles/dataset/Aortic_Vessel_Tree_AVT_CTA_Datasets_and_Segmentations/14806362) | CT | 2022 | 🟢 NRRD | — | ✅ | — | OPEN | 56 aortas (3 collections) |
| [COCA (Stanford)](https://aimi.stanford.edu/datasets/coca-coronary-calcium-chest-ct) | CT | 2021 | 🟢 DICOM | — | ✅ | — | REGISTRATION | ~1000 patients (789 gated + 214 non-gated) |
| [ASOCA](https://asoca.grand-challenge.org/) | CT | 2020 | 🟢 NRRD | — | ✅ | — | DUA | 60 cases (40 train + 20 test) |
| [orCaScore](https://orcascore.grand-challenge.org/) | CT | 2014 | 🟢 MHD | — | ✅ | — | REGISTRATION | 72 patients (32 train + 40 test) |

### 🫃 Abdominal  <sub>(23)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [AMOS-MM](https://era-ai-biomed.github.io/amos/dataset.html) | CT | 2024 | 🟢 NIfTI | ✅ | — | — | REGISTRATION | 2088 CT with reports (1288 train / 400 val) |
| [FLARE23](https://codalab.lisn.upsaclay.fr/competitions/12239) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 4000 train + 100 val + 400 test CT |
| [KiTS23](https://kits-challenge.org/kits23/) | CT | 2023 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 599 CT (489 train / 110 test) |
| [LLD-MMRI](https://github.com/LMMMEng/LLD-MMRI-Dataset) | MRI | 2023 | 🟢 NIfTI | — | — | ✅ | REQUEST | 498 patients, 8 sequences each |
| [TotalSegmentator](https://zenodo.org/records/10047292) | CT | 2023 | 🟢 NIfTI | — | ✅ | — | OPEN | 1228 CT (v2) |
| [AMOS22](https://amos22.grand-challenge.org/) | CT, MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 500 CT + 100 MRI scans |
| [FLARE22](https://flare22.grand-challenge.org/) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 2300 CT (50 labeled + 2000 unlabeled train) |
| [WORD](https://github.com/HiLab-git/WORD) | CT | 2022 | 🟢 NIfTI | — | ✅ | — | REQUEST | 150 CT (100 train / 20 val / 30 test) |
| [AbdomenCT-1K](https://github.com/JunMa11/AbdomenCT-1K) | CT | 2021 | 🟢 NIfTI | — | ✅ | ✅ | REQUEST | 1112 CT from 12 centers |
| [FLARE21](https://flare.grand-challenge.org/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | REGISTRATION | 511 CT (361 train / 50 val / 100 test) |
| [KiTS21](https://kits-challenge.org/kits21/) | CT | 2021 | 🟢 NIfTI | — | ✅ | — | OPEN | 300 train + 100 test CT |
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

### ⬇️ Pelvic & Prostate  <sub>(5)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [PI-CAI](https://pi-cai.grand-challenge.org/) | MRI | 2022 | 🟢 MHA, NIfTI | — | ✅ | ✅ | OPEN | 1500 bpMRI (1476 patients, public set) |
| [Prostate158](https://github.com/kbressem/prostate158) | MRI | 2022 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 158 studies (139 train / 19 test) |
| [MSD Prostate (Task05)](http://medicaldecathlon.com/) | MRI | 2018 | 🟢 NIfTI | — | ✅ | ✅ | OPEN | 48 mpMRI (32 train / 16 test) |
| [ProstateX](https://www.cancerimagingarchive.net/collection/prostatex/) | MRI | 2017 | 🟢 DICOM | — | — | ✅ | OPEN | 346 patients (330 lesions train) |
| [PROMISE12](https://promise12.grand-challenge.org/) | MRI | 2012 | 🟢 MHD | — | ✅ | — | REGISTRATION | 50 train + 30 test T2W MRI |

### 🦴 Musculoskeletal  <sub>(9)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [SKM-TEA](https://aimi.stanford.edu/datasets/skm-tea-knee-mri) | MRI | 2021 | 🟢 HDF5 (k-space), DICOM | — | ✅ | — | REGISTRATION | 155 qDESS knee scans (~1.6 TB) |
| [LERA](https://aimi.stanford.edu/datasets/lera-lower-extremity-radiographs) | X-ray | 2019 | 🟢 DICOM | — | — | — | REGISTRATION | 182 patients (foot, knee, ankle, hip) |
| [MRNet](https://stanfordmlgroup.github.io/competitions/mrnet/) | MRI | 2018 | 🟢 NPY | — | — | ✅ | REGISTRATION | 1,370 knee MRI exams |
| [MURA](https://stanfordmlgroup.github.io/competitions/mura/) | X-ray | 2018 | 🟡 PNG | — | — | — | REGISTRATION | 40,561 images / 14,863 studies / 12,173 patients |
| [fastMRI knee](https://fastmri.med.nyu.edu/) | MRI | 2018 | 🟢 HDF5 (k-space), DICOM | — | — | ✅ | DUA | >1,500 fully-sampled knee k-space MRIs + 10,000 clinical DICOM knee MRIs (~1.35 TB) |
| [KneeMRI](http://www.riteh.uniri.hr/~istajduh/projects/kneeMRI/) | MRI | 2017 | 🟢 PCK | — | — | — | OPEN | 917 sagittal PD-weighted knee MRI volumes |
| [RSNA Bone Age](https://www.rsna.org/rsnai/ai-image-challenge/rsna-pediatric-bone-age-challenge-2017) | X-ray | 2017 | 🟡 PNG | — | — | — | OPEN | 14,236 pediatric hand radiographs |
| [Digital Hand Atlas](https://ipilab.usc.edu/research/baaweb/) | X-ray | 2007 | 🟡 JPEG | — | — | — | OPEN | ~1,400 normal pediatric hand radiographs |
| [OAI](https://nda.nih.gov/oai/) | MRI, X-ray | — | 🟢 DICOM | — | — | ✅ | DUA | 4,796 participants, longitudinal bilateral knee MRI and X-ray |

### 🎀 Breast  <sub>(12)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [BreastDM](https://github.com/smallboy-code/Breast-cancer-dataset) | MRI | 2023 | 🟡 PNG | — | ✅ | ✅ | OPEN | 232 cases (147 malignant, 85 benign) |
| [EMBED](https://registry.opendata.aws/emory-breast-imaging-dataset-embed/) | X-ray | 2023 | 🟢 DICOM | — | — | — | DUA | 3.4M images from ~110,000 patients; 60,000 annotated lesions |
| [RSNA Screening Mammography](https://www.kaggle.com/competitions/rsna-breast-cancer-detection) | X-ray | 2023 | 🟢 DICOM | — | — | — | REGISTRATION | ~54,700 images / ~20,000 patients |
| [ISPY2](https://www.cancerimagingarchive.net/collection/ispy2/) | MRI | 2022 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 719 patients |
| [VinDr-Mammo](https://physionet.org/content/vindr-mammo/) | X-ray | 2022 | 🟢 DICOM | — | — | — | DUA | 5,000 exams / 20,000 images |
| [BCS-DBT](https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,060 patients / 22,032 scans (~1.63 TB) |
| [CMMD](https://www.cancerimagingarchive.net/collection/cmmd/) | X-ray | 2021 | 🟢 DICOM | — | — | — | OPEN | 5,202 images / 1,775 patients |
| [Duke Breast Cancer MRI](https://www.cancerimagingarchive.net/collection/duke-breast-cancer-mri/) | MRI | 2018 | 🟢 DICOM | — | — | ✅ | OPEN | 922 patients / ~773,000 images |
| [CBIS-DDSM](https://www.cancerimagingarchive.net/collection/cbis-ddsm/) | X-ray | 2016 | 🟢 DICOM | — | ✅ | — | OPEN | 10,239 images / 1,566 subjects |
| [ISPY1 (ACRIN 6657)](https://www.cancerimagingarchive.net/collection/ispy1/) | MRI | 2016 | 🟢 DICOM | — | ✅ | ✅ | OPEN | 222 patients |
| [INbreast](http://medicalresearch.inescporto.pt/breastresearch/index.php/Get_INbreast_Database) | X-ray | 2012 | 🟢 DICOM, XML | — | ✅ | — | REQUEST | 410 images / 115 cases |
| [Breast-Diagnosis](https://www.cancerimagingarchive.net/collection/breast-diagnosis/) | MRI, PET, CT, X-ray | 2011 | 🟢 DICOM | — | — | ✅ | OPEN | 88 subjects / ~105,050 images |

### 👤 Head & Neck  <sub>(7)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [RADCURE](https://www.cancerimagingarchive.net/collection/radcure/) | CT | 2024 | 🟢 DICOM, RTSTRUCT | ✅ | ✅ | — | REQUEST | 3,346 patients |
| [HECKTOR](https://hecktor.grand-challenge.org/) | PET, CT | 2022 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | ~882 cases (2022 edition) |
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

### 🌐 Whole-Body & PET  <sub>(4)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [PSMA-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/psma-pet-ct-lesions/) | PET, CT | 2024 | 🟢 DICOM | — | ✅ | — | REGISTRATION | 597 studies / 378 patients |
| [autoPET III](https://autopet-iii.grand-challenge.org/) | PET, CT | 2024 | 🟢 DICOM, NIfTI | — | ✅ | ✅ | DUA | 1,611 studies (1,014 FDG + 597 PSMA) |
| [FDG-PET-CT-Lesions](https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/) | PET, CT | 2022 | 🟢 DICOM | — | ✅ | — | DUA | 1,014 studies / 900 patients |
| [autoPET I](https://autopet.grand-challenge.org/) | PET, CT | 2022 | 🟢 DICOM, NIfTI | — | ✅ | — | DUA | 1,014 studies / 900 patients (FDG) |

### 📝 Multimodal / Image–Text  <sub>(13)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [ROCOv2](https://doi.org/10.5281/zenodo.10821435) | X-ray, CT, MRI, PET | 2024 | 🟡 JPG | ✅ | — | — | OPEN | 79,789 images with captions and UMLS concepts |
| [RadGenome-ChestCT](https://huggingface.co/datasets/RadGenome/RadGenome-ChestCT) | CT | 2024 | 🟢 NIfTI | ✅ | ✅ | — | REGISTRATION | 25,692 CT volumes with 665K grounded report regions + 1.3M VQA |
| [INSPECT](https://inspect.stanford.edu/) | CT | 2023 | 🟢 DICOM | ✅ | — | — | DUA | 23,248 CTPA studies / 19,402 patients with reports and EHR |
| [MAIDA](https://maida.stanford.edu/) | X-ray | 2023 | 🟢 DICOM, PNG | ✅ | — | — | REGISTRATION | multi-institution chest X-rays across 22+ hospitals in 12 countries |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/) | X-ray | 2023 | 🟡 JPG | ✅ | — | — | DUA | 700,703 QA pairs over 164,324 image pairs |
| [PMC-OA](https://huggingface.co/datasets/axiong/pmc_oa) | X-ray, CT, MRI, PET | 2023 | 🟡 JPG | ✅ | — | — | OPEN | 1.6 million image-caption pairs |
| [MS-CXR](https://physionet.org/content/ms-cxr/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 1,162 image-sentence bounding-box pairs across 8 findings |
| [REFLACX](https://physionet.org/content/reflacx-xray-localization/) | X-ray | 2022 | 🟡 JPG | ✅ | — | — | DUA | 3,032 eye-tracking + report sessions for 2,616 chest X-rays |
| [Chest ImaGenome](https://physionet.org/content/chest-imagenome/) | X-ray | 2021 | 🟡 JPG | ✅ | — | — | DUA | 242,072 frontal CXRs with scene graphs |
| [SLAKE](https://www.med-vqa.com/slake/) | X-ray, CT, MRI | 2021 | 🟡 PNG | ✅ | ✅ | — | OPEN | 642 images with 14,028 QA pairs |
| [MedICaT](https://github.com/allenai/medicat) | X-ray, CT, MRI | 2020 | 🟡 PNG | ✅ | — | — | REQUEST | 217,060 figures from 131,410 papers |
| [ROCO](https://github.com/razorx89/roco-dataset) | X-ray, CT, MRI, PET | 2018 | 🟡 JPG, PNG | ✅ | — | — | OPEN | ~81,000 radiology image-caption pairs |
| [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) | X-ray, CT, MRI | 2018 | 🟡 JPG | ✅ | — | — | OPEN | 315 images with 3,515 QA pairs |

### 🗄️ Data Repositories & Portals  <sub>(14)</sub>

| Dataset | Modality | Year | Format | Text | Seg | Multi | Access | Size |
| --- | --- | --- | --- | :-: | :-: | :-: | --- | --- |
| [Stanford AIMI](https://aimi.stanford.edu/shared-datasets) | Multiple | 2021 | 🟢 Various | ✅ | ✅ | — | REGISTRATION | 30+ curated medical imaging datasets |
| [IDC](https://portal.imaging.datacommons.cancer.gov/) | Multiple | 2020 | 🟢 Various | — | ✅ | — | OPEN | 85+ TB across many collections |
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
