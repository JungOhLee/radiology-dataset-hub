/* Radiology Dataset Hub — client logic (vanilla JS, no build step) */

const REGION_ORDER = [
  "Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis",
  "MSK", "Breast", "HeadNeck", "Dental", "WholeBody", "Multi", "Phantom",
];
const REGION_LABEL = {
  Neuro: "Neuro (Brain & Spine)",
  Chest: "Chest & Thorax",
  Cardiac: "Cardiac",
  Vascular: "Vascular",
  Abdomen: "Abdominal",
  Pelvis: "Pelvic & Prostate",
  MSK: "Musculoskeletal",
  Breast: "Breast",
  HeadNeck: "Head & Neck",
  Dental: "Dental & Maxillofacial",
  WholeBody: "Whole-Body",
  Multi: "Unspecified / various body parts",
  Phantom: "Phantoms (non-anatomical)",
  Repository: "Data Repositories & Portals",
};
const REGION_DESC = {
  Neuro: "MRI/CT/PET of brain, spine and head",
  Chest: "Chest X-ray and thoracic CT",
  Cardiac: "Cardiac MRI and coronary/cardiac CT",
  Vascular: "Angiography and vessel imaging",
  Abdomen: "Liver, kidney, pancreas, multi-organ",
  Pelvis: "Prostate and pelvic imaging",
  MSK: "Knee, bone, joints — MRI/X-ray",
  Breast: "Mammography, DBT and breast MRI",
  HeadNeck: "Oncology PET/CT and H&N imaging",
  Dental: "Panoramic X-ray and CBCT",
  WholeBody: "Whole-body PET/CT, MRI and total-body segmentation",
  Multi: "Body region not itemised by the source",
  Phantom: "Geometric / QA phantoms without anatomy",
  Repository: "Hubs hosting many collections",
};
const REGION_ICON = {
  Neuro: "🧠", Chest: "🫁", Cardiac: "🫀", Vascular: "🩸", Abdomen: "🫃",
  Pelvis: "⬇️", MSK: "🦴", Breast: "🎀", HeadNeck: "👤", Dental: "🦷",
  WholeBody: "🌐", Multi: "🧩", Phantom: "🧪", Repository: "🗄️",
};
const REGION_SHORT = {
  Neuro: "Neuro", Chest: "Chest", Cardiac: "Cardiac", Vascular: "Vascular",
  Abdomen: "Abdomen", Pelvis: "Pelvis", MSK: "MSK", Breast: "Breast",
  HeadNeck: "Head & Neck", Dental: "Dental", WholeBody: "Whole-body",
  Multi: "Various", Phantom: "Phantom", Repository: "Repositories",
};
const MODALITIES = ["CT", "MRI", "PET", "X-ray", "DXA"];

// "Image–text (multimodal)" is a characteristic, not a section: paired reports/captions/QA.
const VLM_TASKS = ["vqa", "captioning", "report-generation", "grounding",
  "phrase-grounding", "scene-graph-generation", "image-text-retrieval", "concept-detection"];
const isVLM = d => d.paired_text === true &&
  (d.tasks || []).some(t => VLM_TASKS.includes(String(t).toLowerCase()));

const hasTag = (d, t) => (d.tags || []).includes(t);

/* ---------- schema v2 (data/vocab.json) with v1 fallbacks ---------- */
const fmts = d => d.image_format || d.format || [];
const protoNote = d => d.protocol_note || d.multi_sequence_detail || "";
const protoShort = p => String(p).includes(":") ? String(p).split(":").slice(1).join(":") : String(p);
const relList = d => (d.details && d.details.related) || [];
const isDerived = d => d.type !== "annotation" && relList(d).some(r => r.relation === "derived-from");
const phantomOf = d => d.phantom || (d.details && d.details.phantom) || null;
const isPhantom = d => (d.subjects || []).includes("phantom") || hasTag(d, "phantom") || !!phantomOf(d);
const labelsOnly = d => d.type === "annotation" || d.images_included === false;
const GROUP_LABEL = {
  "neoplasm": "Tumour / cancer", "vascular": "Vascular", "trauma": "Trauma", "infection-inflammation": "Infection / inflammation",
  "degenerative": "Degenerative", "neurodegenerative": "Neurodegenerative", "cardiac": "Cardiac disease",
  "congenital": "Congenital", "metabolic-endocrine": "Metabolic / endocrine", "healthy-normal": "Healthy / normal",
  "unselected-mixed": "Unselected / mixed", "not-applicable": "n/a (phantom, synthetic)",
};
const POP_LABEL = { "adult": "Adult", "pediatric": "Pediatric", "fetal-neonatal": "Fetal / neonatal" };
let VOCAB = null;

const TOGGLES = [
  { key: "raw_image", label: "Raw (DICOM/NIfTI)", test: d => d.raw_image === true },
  { key: "paired_text", label: "Paired text / VLM", test: d => d.paired_text === true },
  { key: "segmentation", label: "Segmentation", test: d => d.segmentation === true },
  { key: "multi_sequence", label: "Multi-seq/phase", test: d => d.multi_sequence === true },
  { key: "multi_region", label: "Multi-region", test: d => (d.regions || []).length > 1 },
  { key: "cohort", label: "Population cohort", test: d => hasTag(d, "population-cohort") },
  { key: "body_comp", label: "Body composition", test: d => d.body_composition === true || hasTag(d, "body-composition") },
  { key: "clinical", label: "Linkable clinical data", test: d => !!d.clinical_variables || hasTag(d, "clinical-linkage") },
  { key: "longitudinal", label: "Longitudinal", test: d => d.longitudinal === true || hasTag(d, "longitudinal") },
  { key: "open", label: "Open access", test: d => d.access === "open" },
  { key: "phantom", label: "Phantom", test: isPhantom },
  { key: "derived", label: "Derived / aggregated", test: isDerived },
  { key: "labels_only", label: "Labels only", test: labelsOnly },
  { key: "verified", label: "Human-verified", test: d => d.review === "human-verified" },
];

const state = {
  q: "",
  modalities: new Set(),
  regions: new Set(),   // region keys, plus the literal "Repository"
  toggles: new Set(),
  protocols: new Set(),   // "MRI:FLAIR" … — chips appear once a modality is chosen
  groups: new Set(),      // condition groups
  population: new Set(),
  sort: "region",
};

let DATA = [];

const $ = sel => document.querySelector(sel);

async function boot() {
  try {
    const res = await fetch("data/datasets.json", { cache: "no-cache" });
    DATA = await res.json();
    try { VOCAB = await (await fetch("data/vocab.json", { cache: "no-cache" })).json(); } catch (e) { VOCAB = null; }
  } catch (e) {
    $("#results").innerHTML = `<div class="empty"><h2>Could not load data</h2>
      <p>Open this page via a local server or GitHub Pages (fetch is blocked on file://).</p></div>`;
    return;
  }
  DATA.sort((a, b) => (b.year || 0) - (a.year || 0));
  buildControls();
  updateHeaderStats();
  render();
  wireDetailModal();
}

function wireDetailModal() {
  const results = $("#results");
  results.addEventListener("click", e => {
    if (e.target.closest("a")) return;            // let source links work
    const card = e.target.closest(".card");
    if (card) openDetail(card.dataset.id);
  });
  results.addEventListener("keydown", e => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const card = e.target.closest(".card");
    if (card) { e.preventDefault(); openDetail(card.dataset.id); }
  });
  document.getElementById("modal-close").addEventListener("click", closeDetail);
  document.getElementById("detail-overlay").addEventListener("click", e => {
    if (e.target.id === "detail-overlay") closeDetail();
    const go = e.target.closest("[data-goto]");    // "Related datasets" links
    if (go) { e.preventDefault(); openDetail(go.dataset.goto); }
  });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && !document.getElementById("detail-overlay").hidden) closeDetail();
  });
}

function regionCount(r) {
  if (r === "Repository") return DATA.filter(d => d.type === "repository").length;
  return DATA.filter(d => d.type !== "repository" && (d.regions || []).includes(r)).length;
}

function buildControls() {
  // modality chips
  const modWrap = $("#modality-filters");
  MODALITIES.forEach(m => {
    const b = chip(m, () => toggleSet(state.modalities, m, b));
    modWrap.appendChild(b);
  });
  // body-region filter chips (multi-select banners) + Repositories
  const regionWrap = $("#region-filters");
  [...REGION_ORDER, "Repository"].forEach(r => {
    const n = regionCount(r);
    if (!n) return;
    const b = document.createElement("button");
    b.className = "chip region-chip"; b.setAttribute("aria-pressed", "false");
    b.dataset.region = r;
    b.innerHTML = `<span class="chip-ico">${REGION_ICON[r] || ""}</span> ${REGION_SHORT[r] || r} <span class="chip-n">${n}</span>`;
    b.addEventListener("click", () => toggleSet(state.regions, r, b));
    regionWrap.appendChild(b);
  });
  renderProtocolChips();
  // clinical context: condition groups + population (only values that occur)
  const cWrap = $("#context-filters");
  if (cWrap) {
    const addCtx = (set, key, label, field) => {
      const n = DATA.filter(d => (d[field] || []).includes(key)).length;
      if (!n) return;
      const b = chip(label, () => toggleSet(set, key, b));
      b.innerHTML = `${esc(label)} <span class="chip-n">${n}</span>`;
      cWrap.appendChild(b);
    };
    Object.keys(GROUP_LABEL).forEach(g => addCtx(state.groups, g, GROUP_LABEL[g], "condition_groups"));
    Object.keys(POP_LABEL).forEach(g => addCtx(state.population, g, POP_LABEL[g], "population"));
    if (!cWrap.querySelector(".chip")) cWrap.closest(".filters").hidden = true;
  }
  // characteristic toggle chips
  const tWrap = $("#toggle-filters");
  TOGGLES.forEach(t => {
    const b = chip(t.label, () => toggleSet(state.toggles, t.key, b));
    b.classList.add("toggle-chip");
    tWrap.appendChild(b);
  });
  // debounce rendering so the input stays responsive while typing over a large catalog
  let searchTimer = null;
  $("#search").addEventListener("input", e => {
    state.q = e.target.value.trim();
    clearTimeout(searchTimer);
    searchTimer = setTimeout(render, 130);
  });
  $("#sort-select").addEventListener("change", e => { state.sort = e.target.value; render(); });
  $("#reset").addEventListener("click", () => {
    state.q = ""; state.modalities.clear(); state.regions.clear(); state.toggles.clear();
    state.protocols.clear(); state.groups.clear(); state.population.clear();
    $("#search").value = "";
    document.querySelectorAll(".chip[aria-pressed='true']").forEach(c => c.setAttribute("aria-pressed", "false"));
    renderProtocolChips();
    render();
  });
}

// MRI sequences / CT phases / PET tracers of the chosen modalities (schema v2 `protocols`)
function renderProtocolChips() {
  const wrap = $("#protocol-filters");
  if (!wrap) return;
  const row = wrap.closest(".filters");
  for (const p of [...state.protocols]) if (!state.modalities.has(p.split(":")[0])) state.protocols.delete(p);
  wrap.innerHTML = "";
  const counts = {};
  DATA.forEach(d => (d.protocols || []).forEach(p => { counts[p] = (counts[p] || 0) + 1; }));
  const order = VOCAB ? Object.entries(VOCAB.protocols).flatMap(([m, ps]) => ps.map(x => `${m}:${x}`)) : Object.keys(counts).sort();
  const shown = order.filter(p => state.modalities.has(p.split(":")[0]) && counts[p]);
  shown.forEach(p => {
    const b = chip(protoShort(p), () => toggleSet(state.protocols, p, b));
    b.innerHTML = `${esc(state.modalities.size > 1 ? p.replace(":", " ") : protoShort(p))} <span class="chip-n">${counts[p]}</span>`;
    if (state.protocols.has(p)) b.setAttribute("aria-pressed", "true");
    wrap.appendChild(b);
  });
  if (row) row.hidden = !shown.length;
}

function chip(label, onClick) {
  const b = document.createElement("button");
  b.className = "chip"; b.textContent = label; b.setAttribute("aria-pressed", "false");
  b.addEventListener("click", () => { onClick(); });
  return b;
}
function toggleSet(set, key, el) {
  if (set.has(key)) { set.delete(key); el.setAttribute("aria-pressed", "false"); }
  else { set.add(key); el.setAttribute("aria-pressed", "true"); }
  if (set === state.modalities) renderProtocolChips();
  render();
}

function matchesRegion(d) {
  if (!state.regions.size) return true;
  if (d.type === "repository") return state.regions.has("Repository");
  return (d.regions || []).some(r => state.regions.has(r));
}

// facet filters only (modality / region / characteristic toggles); text is applied separately
function facetMatches(d) {
  if (state.modalities.size && !(d.modality || []).some(m => state.modalities.has(m))) return false;
  if (!matchesRegion(d)) return false;
  if (state.protocols.size && !(d.protocols || []).some(p => state.protocols.has(p))) return false;
  if (state.groups.size && !(d.condition_groups || []).some(g => state.groups.has(g))) return false;
  if (state.population.size && !(d.population || []).some(g => state.population.has(g))) return false;
  for (const key of state.toggles) {
    const t = TOGGLES.find(x => x.key === key);
    if (t && !t.test(d)) return false;
  }
  return true;
}

/* ---------- flexible search ----------
   Punctuation/space-insensitive so "picai" matches "PI-CAI" and "MR RATE" matches
   "MR-RATE". Two passes: a precise whole-query match first, then a broad token
   match (any order, any field) only when the precise pass finds nothing. */
function squash(s) {
  return String(s == null ? "" : s).toLowerCase().replace(/[^a-z0-9]+/g, "");
}

/* ---------- facet vocabulary ----------
   Maps query n-grams (squashed) to structured facets — modality, body region, or an
   anatomy term — so "abdominal ct" surfaces every Abdomen-region CT dataset in its own
   tier right after title matches instead of buried among description matches.
   Facet kinds: {mod} matches d.modality; {region} matches d.regions;
   {anat, terms} word-matches anatomy/title/segmentation fields. A facet may combine
   kinds (mammography = X-ray + Breast); a dataset must satisfy EVERY facet parsed. */
const FACET_VOCAB = (() => {
  const V = Object.create(null);   // null prototype: a token like "constructor" must not resolve
  const add = (facet, ...keys) => keys.forEach(k => { V[k] = facet; });
  // modalities
  add({ mod: "CT" }, "ct", "computedtomography", "computedtomographyscan");
  add({ mod: "MRI" }, "mri", "mr", "magneticresonance", "magneticresonanceimaging");
  add({ mod: "X-ray" }, "xray", "xrays", "radiograph", "radiographs", "radiography", "cxr");
  add({ mod: "PET" }, "pet");
  add({ mod: "DXA" }, "dxa", "dexa");
  add({ mod: "Ultrasound" }, "ultrasound", "ultrasonography", "sonography");
  // modality techniques: require the technique word itself in the record (term), not just
  // the modality — otherwise "cta"/"fmri" would flood the tier with every CT/MRI dataset
  const tech = (mod, ...keys) => keys.forEach(k => add({ mod, term: k }, k));
  tech("CT", "cect", "hrct");
  tech("MRI", "dmri");
  // schema v2 protocols: match d.protocols; entries without protocols fall back to the word
  const proto = (p, ...keys) => keys.forEach(k => add({ proto: p, term: k }, squash(k)));
  proto("MRI:FLAIR", "flair"); proto("MRI:T1w-CE", "t1ce", "t1c", "t1gd", "contrast enhanced t1", "postcontrast t1");
  proto("MRI:T1w", "t1w", "t1 weighted"); proto("MRI:T2w", "t2w", "t2 weighted"); proto("MRI:PD", "proton density");
  proto("MRI:DWI", "dwi", "diffusion weighted", "diffusion"); proto("MRI:DTI", "dti", "tractography");
  proto("MRI:SWI", "swi"); proto("MRI:DCE", "dce"); proto("MRI:perfusion", "dsc", "asl", "mr perfusion");
  proto("MRI:MRA", "mra"); proto("MRI:cine", "cine"); proto("MRI:LGE", "lge", "late gadolinium");
  proto("MRI:fMRI", "fmri", "functional mri", "bold"); proto("MRI:MRS", "spectroscopy");
  proto("MRI:kspace-raw", "kspace", "k space");
  proto("CT:non-contrast", "ncct", "non contrast", "noncontrast", "unenhanced");
  proto("CT:arterial", "arterial phase"); proto("CT:portal-venous", "portal venous", "venous phase");
  proto("CT:delayed", "delayed phase"); proto("CT:CTA", "cta", "ct angiography"); proto("CT:CTPA", "ctpa");
  proto("CT:perfusion", "ct perfusion", "ctp"); proto("CT:low-dose", "ldct", "low dose");
  proto("CT:CBCT", "cbct", "cone beam"); proto("CT:spectral", "dect", "dual energy", "spectral ct");
  proto("CT:photon-counting", "pcct", "photon counting"); proto("CT:4D", "4dct", "4d ct");
  proto("PET:FDG", "fdg"); proto("PET:PSMA", "psma"); proto("PET:amyloid", "amyloid"); proto("PET:tau", "tau pet");
  proto("X-ray:DBT", "dbt", "tomosynthesis"); proto("X-ray:fluoroscopy-DSA", "dsa", "fluoroscopy");
  proto("X-ray:panoramic", "panoramic", "opg");
  // body regions
  add({ region: "Neuro" }, "brain", "neuro", "neuroimaging", "cerebral", "intracranial", "head");
  add({ region: "Chest" }, "chest", "thorax", "thoracic", "lung", "lungs", "pulmonary");
  add({ region: "Cardiac" }, "cardiac", "heart", "cardiovascular", "coronary");
  add({ region: "Vascular" }, "vascular", "vessel", "vessels", "angiography", "angiogram", "aorta", "aortic");
  add({ region: "Abdomen" }, "abdomen", "abdominal");
  add({ region: "Pelvis" }, "pelvis", "pelvic");
  add({ region: "MSK" }, "msk", "musculoskeletal", "orthopedic", "orthopaedic", "bone", "bones", "joint", "joints");
  add({ region: "Breast" }, "breast");
  add({ region: "HeadNeck" }, "headneck", "headandneck");
  add({ region: "Dental" }, "dental", "tooth", "teeth", "maxillofacial");
  add({ region: "WholeBody" }, "wholebody", "totalbody");
  // modality + region combos
  add({ mod: "X-ray", region: "Breast" }, "mammography", "mammogram", "mammograms", "mammo");
  // anatomy terms — matched against the dataset's anatomy/title/segmentation fields as
  // whole words; a trailing "*" marks a deliberate prefix stem (pancrea* → pancreatic).
  // Whole-word is the default so "hip" can't match hippocampus or HiPaS. Lookup keys
  // are the de-starred terms plus any extra typed forms.
  const anat = (label, terms, ...keys) => add({ anat: label, terms }, ...terms.map(t => t.replace("*", "")), ...keys);
  anat("liver", ["liver", "livers", "hepatic"]);
  anat("kidney", ["kidney", "kidneys", "renal"]);
  anat("pancreas", ["pancrea*"], "pancreas", "pancreatic");
  anat("spleen", ["spleen", "splenic"]);
  anat("colon", ["colon", "colorectal"]);
  anat("prostate", ["prostate"]);
  anat("knee", ["knee", "knees"]);
  anat("shoulder", ["shoulder", "shoulders"]);
  anat("hip", ["hip", "hips"]);
  anat("hand", ["hand", "hands"]);
  anat("wrist", ["wrist", "wrists"]);
  anat("spine", ["spine", "spinal", "vertebra*", "lumbar", "cervical"], "vertebrae");
  anat("skull", ["skull", "cranial"]);
  anat("thyroid", ["thyroid"]);
  anat("bladder", ["bladder"]);
  anat("uterus", ["uterus", "uterine", "cervix"]);
  anat("ovary", ["ovar*"], "ovary", "ovarian", "ovaries");
  anat("rectum", ["rectum", "rectal"]);
  anat("stomach", ["stomach", "gastric"]);
  anat("esophagus", ["esophag*", "oesophag*"], "esophagus", "esophageal", "oesophagus", "oesophageal");
  anat("airway", ["airway", "airways"]);
  anat("nodule", ["nodule", "nodules"]);
  return V;
})();

/* Greedy n-gram scan (longest first) splitting query tokens into structured facets
   and leftover free-text tokens: ["abdominal","ct"] -> 2 facets; ["duke","liver"]
   -> facet liver + free "duke". */
function parseFacets(tokens) {
  const facets = [], free = [];
  for (let i = 0; i < tokens.length; ) {
    let hit = null, len = 1;
    for (const n of [3, 2, 1]) {
      if (i + n > tokens.length) continue;
      const f = FACET_VOCAB[tokens.slice(i, i + n).join("")];
      if (f) { hit = f; len = n; break; }
    }
    if (hit) facets.push(hit); else free.push(tokens[i]);
    i += len;
  }
  return { facets, free };
}

function facetMatch(d, x, f) {
  if (f.proto) {
    if ((d.protocols || []).length) { if (!d.protocols.includes(f.proto)) return false; }
    else if (!x.sq.includes(squash(f.term))) return false;
  }
  if (f.mod && !(d.modality || []).includes(f.mod)) return false;
  if (f.region && !(d.regions || []).includes(f.region)) return false;
  if (f.term && !x.wraw.includes(" " + f.term)) return false;
  // "*" = prefix stem; otherwise whole word (wanat is padded with spaces at both ends)
  if (f.anat && !(d.organs || []).some(o => o.includes(f.anat)) && !f.terms.some(t => t.endsWith("*")
      ? x.wanat.includes(" " + t.slice(0, -1))
      : x.wanat.includes(" " + t + " "))) return false;
  return true;
}

function facetTierLabel(facets, n) {
  const chips = facets.map(f => {
    let h = "";
    if (f.mod) h += `<span class="mod">${esc(f.mod)}</span>`;
    if (f.proto) h += `<span class="rtag">${esc(f.proto.replace(":", " "))}</span>`;
    else if (f.term) h += `<span class="rtag">${esc(f.term)}</span>`;
    if (f.region) h += `<span class="rtag">${REGION_ICON[f.region] || ""} ${esc(REGION_SHORT[f.region] || f.region)}</span>`;
    if (f.anat) h += `<span class="rtag">${esc(f.anat)}</span>`;
    return h;
  }).join("");
  const hasMod = facets.some(f => f.mod || f.proto), hasBody = facets.some(f => f.region || f.anat);
  const by = hasMod && hasBody ? "modality & body part" : hasMod ? "modality" : "body part";
  return `${chips}<span>matched by ${by} (${n})</span>`;
}

/* Tiered, field-boosted ranking. Returns null when there is no query (browse mode),
   else { t1, tf, t2, facets }: t1 = title/name/id matches (shown first), tf = facet
   matches — datasets whose modality / body region / anatomy satisfy every structured
   facet parsed from the query (e.g. "abdominal ct" -> Abdomen + CT), shown right after
   title matches — and t2 = extended matches in description/labels/metadata.
   Punctuation/space-insensitive so "picai" -> PI-CAI and "MR RATE" -> MR-RATE. */
function searchRank(list, q) {
  q = (q || "").trim();
  if (!q) return null;
  const sqQuery = squash(q);
  if (!sqQuery) return null;
  // word-boundary tokens: a token matches a word that starts with it (prefix), so
  // "rate" won't match inside "accurate" and "mr" still matches "MRI".
  const tokens = q.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean);
  const allTok = wblob => tokens.length > 0 && tokens.every(t => wblob.includes(" " + t));
  const { facets, free } = parseFacets(tokens);
  // leftover non-facet tokens ("duke" in "duke liver mri") must still match somewhere
  const freeTok = wblob => free.every(t => wblob.includes(" " + t));
  const t1 = [], tf = [], t2 = [];
  for (const d of list) {
    const x = searchIndex(d);
    let score = 0, tier = 0;
    if (x.sqName === sqQuery) { score = 100; tier = 1; }
    else if (x.sqName.startsWith(sqQuery)) { score = 90; tier = 1; }
    else if (x.sqName.includes(sqQuery)) { score = 80; tier = 1; }
    else if (x.sqTitle.includes(sqQuery)) { score = 70; tier = 1; }
    else if (allTok(x.wtitle)) { score = 60; tier = 1; }
    else if (facets.length && d.type !== "repository" &&
             facets.every(f => facetMatch(d, x, f)) && freeTok(x.wraw)) { score = 50; tier = 15; }
    else if (x.sq.includes(sqQuery)) { score = 40; tier = 2; }
    else if (allTok(x.wraw)) { score = 20; tier = 2; }
    else continue;
    (tier === 1 ? t1 : tier === 15 ? tf : t2).push({ d, score });
  }
  const by = (a, b) => b.score - a.score || (b.d.year || 0) - (a.d.year || 0) || a.d.name.localeCompare(b.d.name);
  t1.sort(by); tf.sort(by); t2.sort(by);
  return { t1: t1.map(o => o.d), tf: tf.map(o => o.d), t2: t2.map(o => o.d), facets };
}

const SEARCH_CAP = 150;   // max cards rendered while searching (keeps typing smooth)

function renderSearchHTML(r) {
  const { t1, tf, t2, facets } = r;
  let html = "";
  if (t1.length) html += `<div class="grid">${t1.map(card).join("")}</div>`;
  // facet tier: modality / body-part matches, right after title matches
  const roomF = Math.max(t1.length ? 0 : 30, SEARCH_CAP - t1.length);
  const shownTf = tf.slice(0, roomF);
  if (shownTf.length) {
    html += `<div class="tier-divider tier-facet">${facetTierLabel(facets, tf.length)}</div>`;
    html += `<div class="grid">${shownTf.map(card).join("")}</div>`;
  }
  const shownSoFar = t1.length + shownTf.length;
  const roomT2 = Math.max(shownSoFar ? 0 : 30, SEARCH_CAP - shownSoFar);
  const shownT2 = t2.slice(0, roomT2);
  if (shownT2.length) {
    const label = shownSoFar
      ? `More results — matched in description, labels or metadata (${t2.length})`
      : `No title matches — showing matches in description, labels or metadata (${t2.length})`;
    html += `<div class="tier-divider"><span>${label}</span></div>`;
    html += `<div class="grid">${shownT2.map(card).join("")}</div>`;
  }
  const hidden = (tf.length - shownTf.length) + (t2.length - shownT2.length);
  if (hidden > 0) html += `<div class="tier-more">+${hidden} more matches — refine your search to see them.</div>`;
  return html;
}

function searchIndex(d) {
  if (d._sidx) return d._sidx;
  const parts = [
    d.id, d.name, d.full_name, d.description, d.anatomy,
    (d.modality || []).join(" "),
    (d.regions || []).map(r => REGION_LABEL[r] || r).join(" "), (d.regions || []).join(" "),
    (d.tags || []).join(" "), (d.tasks || []).join(" "), (d.other_labels || []).join(" "),
    d.host, fmts(d).join(" "), d.license, d.license_id, d.size, d.year,
    d.clinical_variables, d.segmentation_detail, protoNote(d), d.paired_text_detail,
    (d.subjects || []).join(" "), (d.organs || []).join(" "), (d.other_modalities || []).join(" "),
    (d.protocols || []).map(p => p + " " + protoShort(p)).join(" "), (d.field_strength || []).join(" "),
    (d.conditions || []).join(" "), (d.condition_groups || []).join(" "), (d.population || []).join(" "),
    (d.setting || []).join(" "), (d.label_types || []).join(" "), (d.label_format || []).join(" "),
    (d.preprocessing || []).join(" "),
    phantomOf(d) ? ["phantom", phantomOf(d).type, phantomOf(d).body_part, phantomOf(d).model, phantomOf(d).purpose].join(" ") : "",
    d.details ? (d.details.label_schema || []).join(" ") : "",
    d.details ? [(d.details.label_source || []).join(" "), (d.details.label_unit || []).join(" "),
                 d.details.reference_standard, d.details.label_readers,
                 (d.details.label_variants || []).map(v => v.name).join(" "),
                 (d.details.related || []).map(r => [r.name || r.id, r.note, (r.process || []).join(" ")].join(" ")).join(" ")].join(" ") : "",
    (d.aliases || []).join(" "), d.type === "annotation" ? "annotation label set relabel expert labels" : "",
  ];
  const raw = parts.filter(Boolean).join(" ").toLowerCase();
  const wordify = s => " " + String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim() + " ";
  d._sidx = {
    sq: raw.replace(/[^a-z0-9]+/g, ""),                          // punctuation-free blob
    sqName: squash(d.name),
    sqTitle: squash([d.id, d.name, d.full_name].filter(Boolean).join(" ")),
    wraw: wordify(raw),                                          // word-boundary blob (for prefix tokens)
    wtitle: wordify([d.id, d.name, d.full_name].filter(Boolean).join(" ")),
    // anatomy scope for facet matching: where an anatomy term like "liver" must appear
    wanat: wordify([d.anatomy, d.name, d.full_name, d.segmentation_detail, (d.organs || []).join(" ")].filter(Boolean).join(" ")),
  };
  return d._sidx;
}

const EMPTY_HTML = `<div class="empty"><h2>No datasets match</h2>
  <p>Try removing a filter or broadening your search.</p></div>`;

function render() {
  const base = DATA.filter(facetMatches);
  const results = $("#results");
  const ranked = searchRank(base, state.q);

  // ----- search mode: ranked flat list, title matches first -----
  if (ranked) {
    const total = ranked.t1.length + ranked.tf.length + ranked.t2.length;
    $("#count").innerHTML = `<b>${total}</b> of ${DATA.length} · <span class="count-sub">by relevance</span>`;
    results.innerHTML = total ? renderSearchHTML(ranked) : EMPTY_HTML;
    return;
  }

  // ----- browse mode: no query -----
  $("#count").innerHTML = `<b>${base.length}</b> of ${DATA.length} datasets`;
  if (!base.length) { results.innerHTML = EMPTY_HTML; return; }

  if (state.sort === "year" || state.sort === "name") {
    const sorted = [...base].sort((a, b) =>
      state.sort === "year" ? (b.year || 0) - (a.year || 0) : a.name.localeCompare(b.name));
    results.innerHTML = `<div class="grid">${sorted.map(card).join("")}</div>`;
    return;
  }

  // grouped by region; a multi-region dataset appears under each of its regions
  let html = "";
  for (const r of REGION_ORDER) {
    const items = base.filter(d => d.type !== "repository" && (d.regions || []).includes(r));
    if (!items.length) continue;
    items.sort((a, b) => (b.year || 0) - (a.year || 0));
    html += section(r, items);
  }
  const repos = base.filter(d => d.type === "repository");
  if (repos.length) {
    repos.sort((a, b) => (b.year || 0) - (a.year || 0));
    html += section("Repository", repos);
  }
  results.innerHTML = html;
}

function section(r, items) {
  return `<section class="cat-section" id="cat-${r}">
    <div class="cat-head">
      <span class="cat-ico">${REGION_ICON[r] || ""}</span>
      <h2>${REGION_LABEL[r] || r}</h2>
      <span class="cat-count">${items.length}</span>
      <span class="cat-desc">${REGION_DESC[r] || ""}</span>
    </div>
    <div class="grid">${items.map(card).join("")}</div>
  </section>`;
}

// only http(s) links are rendered as hrefs — a javascript:/data: URL in the catalog
// must never become clickable (defense in depth; validate.py also rejects them)
function safeUrl(u) {
  return /^https?:\/\//i.test(String(u || "")) ? String(u) : "";
}

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"]/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function regionTags(d) {
  if (d.type === "repository") {
    return `<span class="rtag">${REGION_ICON.Repository} Repository</span>`;
  }
  const rs = d.regions || [];
  const multi = rs.length > 1 ? ` <span class="rtag rtag-multi" title="Covers multiple body regions">multi-region</span>` : "";
  return rs.map(r => `<span class="rtag">${REGION_ICON[r] || ""} ${esc(REGION_SHORT[r] || r)}</span>`).join("") + multi;
}

function card(d) {
  const mods = (d.modality || []).map(m => `<span class="mod">${esc(m)}</span>`).join("");
  const badges = [];
  if (d.raw_image) badges.push(`<span class="badge raw" title="Native DICOM/NIfTI raw images">◆ Raw</span>`);
  if (d.paired_text) badges.push(`<span class="badge text" title="${esc(d.paired_text_detail || "Paired reports/captions/QA — image–text / multimodal")}">◨ ${isVLM(d) ? "Image–text" : "Text"}</span>`);
  if (d.segmentation) badges.push(`<span class="badge seg" title="${esc(d.segmentation_detail || "Segmentation masks")}">▧ Seg</span>`);
  if ((d.protocols || []).length) {
    const ps = d.protocols.slice(0, 4).map(protoShort);
    badges.push(`<span class="badge seq" title="${esc(protoNote(d) || d.protocols.join(", "))}">≋ ${esc(ps.join(" · "))}${d.protocols.length > 4 ? " …" : ""}</span>`);
  } else if (d.multi_sequence) badges.push(`<span class="badge seq" title="${esc(protoNote(d) || "Multi-sequence / multi-phase")}">≋ Multi-seq</span>`);
  if (isPhantom(d)) badges.push(`<span class="badge phantom" title="${esc(phantomOf(d) ? [phantomOf(d).type, phantomOf(d).body_part, phantomOf(d).model].filter(Boolean).join(" · ") : "Phantom")}">🧪 Phantom</span>`);
  if (isDerived(d)) badges.push(`<span class="badge derived" title="Built from: ${esc(relList(d).filter(r => r.relation === "derived-from").map(r => r.name || r.id).join(", "))}">⤳ Derived</span>`);
  if (d.review === "llm-proposed") badges.push(`<span class="badge unreviewed" title="Machine-proposed entry — not yet reviewed by a person">◌ Unreviewed</span>`);
  if (hasTag(d, "population-cohort")) badges.push(`<span class="badge cohort" title="Population / epidemiological cohort${d.clinical_variables ? " — " + esc(d.clinical_variables) : ""}">◉ Cohort</span>`);
  if (d.body_composition) badges.push(`<span class="badge bodycomp" title="Body-composition phenotypes available (VAT/ASAT/muscle/DXA)">⚖ Body comp</span>`);
  if (d.type === "annotation") badges.push(`<span class="badge seq" title="Label/annotation set for another dataset's images — images come from the base dataset">🏷 Label set</span>`);
  const fmt = fmts(d).slice(0, 3).map(f => `<span class="badge fmt">${esc(f)}</span>`).join("");

  const access = (d.access || "").toLowerCase();
  const accessCls = access === "open" ? "access-open"
    : access === "registration" ? "access-registration"
    : access === "dua" ? "access-dua" : "access-request";
  const accessLbl = access === "dua" ? "DUA" : (access ? access[0].toUpperCase() + access.slice(1) : "—");

  const meta = [];
  if (d.size) meta.push(`<span class="m"><b>Size</b> ${esc(d.size)}</span>`);
  if (d.host) meta.push(`<span class="m"><b>Host</b> ${esc(d.host)}</span>`);
  if (d.license) meta.push(`<span class="m"><b>License</b> ${esc(d.license)}</span>`);

  const title = d.url
    ? (safeUrl(d.url) ? `<a href="${esc(safeUrl(d.url))}" target="_blank" rel="noopener">${esc(d.name)}</a>` : esc(d.name))
    : esc(d.name);
  const hasDetails = !!d.details;

  return `<article class="card" data-id="${esc(d.id)}" tabindex="0" role="button" aria-label="View details for ${esc(d.name)}">
    <div class="card-top">
      <h3>${title}</h3>
      <span class="yr">${d.year || ""}</span>
    </div>
    ${d.full_name && d.full_name !== d.name ? `<div class="anatomy">${esc(d.full_name)}</div>` : ""}
    <div class="modality-row">${mods}${d.anatomy ? `<span class="anatomy">· ${esc(d.anatomy)}</span>` : ""}</div>
    <div class="rtags">${regionTags(d)}</div>
    <p class="desc">${esc(d.description || "")}</p>
    <div class="badges">${badges.join("")}${fmt}</div>
    <div class="meta-line">
      <span class="access-pill ${accessCls}">${accessLbl}</span>
      ${meta.join("")}
    </div>
    <div class="card-foot"><span class="detail-cue">${hasDetails ? "◳ View data & label structure" : "View details"} ›</span></div>
  </article>`;
}

/* ---------- Detail modal ---------- */
function row(label, value) {
  if (value == null || value === "" || (Array.isArray(value) && !value.length)) return "";
  const v = Array.isArray(value) ? value.map(esc).join(", ") : esc(value);
  return `<tr><th>${esc(label)}</th><td>${v}</td></tr>`;
}
function boolRow(label, val, detail) {
  const yes = val === true;
  const mark = yes ? `<span class="yn yes">Yes</span>` : `<span class="yn no">No</span>`;
  const dtl = yes && detail ? ` — ${esc(detail)}` : "";
  return `<tr><th>${esc(label)}</th><td>${mark}${dtl}</td></tr>`;
}

function openDetail(id) {
  const d = DATA.find(x => x.id === id);
  if (!d) return;
  const accessMap = {
    open: "Open — direct download",
    registration: "Registration — free account required",
    dua: "DUA — data-use agreement required",
    request: "Request — application/approval required",
  };
  const links = [];
  if (safeUrl(d.url)) links.push(`<a href="${esc(safeUrl(d.url))}" target="_blank" rel="noopener">Official source ↗</a>`);
  for (const l of d.links || []) if (safeUrl(l.url)) links.push(`<a href="${esc(safeUrl(l.url))}" target="_blank" rel="noopener">${esc(l.label || "Also at")} ↗</a>`);
  links.push(`<a href="data/datasets.json" target="_blank" rel="noopener">JSON entry</a>`);

  let structure = "";
  if (d.details) {
    const dt = d.details;
    let parts = "";
    if (dt.label_schema && dt.label_schema.length) {
      parts += `<h4>Labels & annotation schema</h4><ul class="schema">${dt.label_schema.map(s => `<li>${esc(s)}</li>`).join("")}</ul>`;
    }
    if (dt.file_structure) parts += `<h4>File & data structure</h4><p class="mono">${esc(dt.file_structure)}</p>`;
    if (dt.splits) parts += `<h4>Splits</h4><p>${esc(dt.splits)}</p>`;
    // label provenance — what a label means and how trustworthy it is (CONTRIBUTING.md)
    const prov = [
      row("Label source", dt.label_source), row("Readers", dt.label_readers),
      row("Label unit", dt.label_unit), row("Reference standard", dt.reference_standard),
      row("Version", [dt.version, dt.release_date].filter(Boolean).join(" · ")),
      row("DICOM headers", dt.dicom_headers),
      row("Sending images to external services", dt.third_party_processing
        ? dt.third_party_processing + (dt.third_party_note ? " — " + dt.third_party_note : "") : ""),
    ].join("");
    if (prov) parts += `<h4>Label provenance & use</h4><table class="detail-table">${prov}</table>`;

    const rel = (dt.related || []).map(r => {
      const tgt = r.id && DATA.find(x => x.id === r.id);
      const nm = esc(r.name || (tgt && tgt.name) || r.id);
      const how = [(r.process || []).join(", "), r.note].filter(Boolean).join(" — ");
      return `<li>${esc(r.relation)}: ${tgt ? `<a href="#" data-goto="${esc(r.id)}">${nm}</a>` : nm}${how ? " — " + esc(how) : ""}</li>`;
    });
    const vars = (dt.label_variants || []).map(v =>
      `<li>${safeUrl(v.url) ? `<a href="${esc(safeUrl(v.url))}" target="_blank" rel="noopener">${esc(v.name)}</a>` : esc(v.name)}${v.note ? " — " + esc(v.note) : ""}</li>`);
    if (rel.length) parts += `<h4>Related datasets</h4><ul class="schema">${rel.join("")}</ul>`;
    if (vars.length) parts += `<h4>Other label sets for these images</h4><ul class="schema">${vars.join("")}</ul>`;
    if (dt.extra) parts += `<p class="note">${esc(dt.extra)}</p>`;
    structure = `<section class="detail-structure">${parts}</section>`;
  } else {
    structure = `<section class="detail-structure detail-structure-empty">
      <h4>Data & label structure</h4>
      <p>A detailed label schema hasn't been catalogued for this ${d.type === "repository" ? "repository" : "dataset"} yet.
      The fields above summarize what's inside; see the
      <a href="${esc(safeUrl(d.url) || "#")}" target="_blank" rel="noopener">official source</a>
      for the exact folder layout and label definitions.
      <a href="https://github.com/JungOhLee/radiology-dataset-hub/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Contribute it →</a></p>
    </section>`;
  }

  const ph = phantomOf(d);
  if (ph) structure = `<section class="detail-structure"><h4>Phantom</h4><table class="detail-table">${[
    row("Type", ph.type), row("Anthropomorphic", ph.anthropomorphic === true ? "yes" : ph.anthropomorphic === false ? "no" : ""),
    row("Body part", ph.body_part), row("Model", ph.model), row("Purpose", ph.purpose),
  ].join("")}</table></section>` + structure;

  const regionsTxt = d.type === "repository" ? "Data repository / portal"
    : (d.regions || []).map(r => REGION_LABEL[r] || r).join(", ");
  const modsBig = (d.modality || []).map(m => `<span class="mod">${esc(m)}</span>`).join("");
  document.getElementById("modal-body").innerHTML = `
    <div class="modal-head">
      <div class="modality-row">${modsBig}</div>
      <h2 id="modal-title">${esc(d.name)}</h2>
      ${d.full_name && d.full_name !== d.name ? `<p class="modal-sub">${esc(d.full_name)}</p>` : ""}
      <p class="modal-desc">${esc(d.description || "")}</p>
      <div class="modal-links">${links.join("")}</div>
    </div>
    <div class="detail-cols">
      <table class="detail-table">
        ${row("Body region(s)", regionsTxt)}
        ${row("Anatomy", d.anatomy)}
        ${row("Modality", d.modality)}
        ${row("Year", d.year)}
        ${row("Subjects", d.subjects)}
        ${row("Organs", d.organs)}
        ${row("Format", fmts(d))}
        ${row("Label / metadata files", d.label_format)}
        ${row("Preprocessing", d.preprocessing)}
        ${d.images_included === false ? row("Images included", "No — labels only; images come from the source dataset") : ""}
        ${boolRow("Raw image (DICOM/NIfTI)", d.raw_image)}
        ${row("Size", d.size)}
        ${row("Counts", [d.n_subjects && d.n_subjects.toLocaleString() + " subjects", d.n_studies && d.n_studies.toLocaleString() + " studies",
                         d.n_images && d.n_images.toLocaleString() + " images"].filter(Boolean).join(" · "))}
        ${boolRow("Paired text / image–text", d.paired_text, d.paired_text_detail)}
        ${boolRow("Multi-sequence / phase", d.multi_sequence, protoNote(d))}
        ${row("Protocols", (d.protocols || []).map(p => p.replace(":", " ")))}
        ${row("Field strength", d.field_strength)}
        ${row("Other modalities in the download", d.other_modalities)}
        ${row("Conditions", d.conditions)}
        ${row("Condition groups", (d.condition_groups || []).map(g => GROUP_LABEL[g] || g))}
        ${row("Population", (d.population || []).map(g => POP_LABEL[g] || g))}
        ${row("Clinical setting", d.setting)}
        ${row("Label types", d.label_types)}
        ${boolRow("Segmentation labels", d.segmentation, d.segmentation_detail)}
        ${d.clinical_variables ? row("Linkable clinical data", d.clinical_variables) : ""}
        ${d.body_composition ? boolRow("Body composition", d.body_composition) : ""}
        ${d.longitudinal ? boolRow("Longitudinal (repeat imaging)", d.longitudinal) : ""}
        ${row("Other labels", d.other_labels)}
        ${(d.tags && d.tags.length) ? row("Tags", d.tags) : ""}
        ${row("Tasks", d.tasks)}
        ${row("Access", accessMap[d.access] || d.access)}
        ${row("License", [d.license, d.license_id && `(${d.license_id}${d.commercial_use ? " · commercial use: " + d.commercial_use : ""})`].filter(Boolean).join(" "))}
        ${row("Review", d.review ? d.review + (d.verified_date ? " · " + d.verified_date : "") + (d.enriched ? " · enriched " + d.enriched : "") : "")}
        ${row("Host", d.host)}
      </table>
      ${structure}
    </div>`;
  const overlay = document.getElementById("detail-overlay");
  overlay.hidden = false;
  document.body.style.overflow = "hidden";
  document.getElementById("modal-close").focus();
}

function closeDetail() {
  document.getElementById("detail-overlay").hidden = true;
  document.body.style.overflow = "";
}

function updateHeaderStats() {
  const total = DATA.length;
  const byMod = m => DATA.filter(d => (d.modality || []).includes(m)).length;
  const raw = DATA.filter(d => d.raw_image).length;
  const text = DATA.filter(d => d.paired_text).length;
  const seg = DATA.filter(d => d.segmentation).length;
  $("#stats").innerHTML = `
    <span><b>${total}</b> datasets</span>
    <span><b>${byMod("CT")}</b> CT</span>
    <span><b>${byMod("MRI")}</b> MRI</span>
    <span><b>${byMod("PET")}</b> PET</span>
    <span><b>${byMod("X-ray")}</b> X-ray</span>
    <span><b>${raw}</b> raw DICOM/NIfTI</span>
    <span><b>${text}</b> with reports/text</span>
    <span><b>${seg}</b> with segmentation</span>`;
}

boot();
