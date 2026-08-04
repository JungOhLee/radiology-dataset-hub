/* Radiology Dataset Hub — client logic (vanilla JS, no build step) */

const REGION_ORDER = [
  "Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis",
  "MSK", "Breast", "HeadNeck", "Dental", "WholeBody", "Multi",
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
  WholeBody: "Whole-Body & PET",
  Multi: "Multiple / Various body parts",
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
  WholeBody: "Whole-body PET/CT and total-body segmentation",
  Multi: "Datasets spanning many body regions",
  Repository: "Hubs hosting many collections",
};
const REGION_ICON = {
  Neuro: "🧠", Chest: "🫁", Cardiac: "🫀", Vascular: "🩸", Abdomen: "🫃",
  Pelvis: "⬇️", MSK: "🦴", Breast: "🎀", HeadNeck: "👤", Dental: "🦷",
  WholeBody: "🌐", Multi: "🧩", Repository: "🗄️",
};
const REGION_SHORT = {
  Neuro: "Neuro", Chest: "Chest", Cardiac: "Cardiac", Vascular: "Vascular",
  Abdomen: "Abdomen", Pelvis: "Pelvis", MSK: "MSK", Breast: "Breast",
  HeadNeck: "Head & Neck", Dental: "Dental", WholeBody: "Whole-body/PET",
  Multi: "Multi-region", Repository: "Repositories",
};
const MODALITIES = ["CT", "MRI", "PET", "X-ray", "DXA"];

// "Image–text (multimodal)" is a characteristic, not a section: paired reports/captions/QA.
const VLM_TASKS = ["vqa", "captioning", "report-generation", "grounding",
  "phrase-grounding", "scene-graph-generation", "image-text-retrieval", "concept-detection"];
const isVLM = d => d.paired_text === true &&
  (d.tasks || []).some(t => VLM_TASKS.includes(String(t).toLowerCase()));

const hasTag = (d, t) => (d.tags || []).includes(t);
const TOGGLES = [
  { key: "raw_image", label: "Raw (DICOM/NIfTI)", test: d => d.raw_image === true },
  { key: "paired_text", label: "Paired text / VLM", test: d => d.paired_text === true },
  { key: "segmentation", label: "Segmentation", test: d => d.segmentation === true },
  { key: "multi_sequence", label: "Multi-seq/phase", test: d => d.multi_sequence === true },
  { key: "multi_region", label: "Multi-region", test: d => (d.regions || []).length > 1 },
  { key: "cohort", label: "Population cohort", test: d => hasTag(d, "population-cohort") },
  { key: "body_comp", label: "Body composition", test: d => d.body_composition === true },
  { key: "clinical", label: "Linkable clinical data", test: d => !!d.clinical_variables || hasTag(d, "clinical-linkage") },
  { key: "longitudinal", label: "Longitudinal", test: d => d.longitudinal === true },
  { key: "open", label: "Open access", test: d => d.access === "open" },
];

const state = {
  q: "",
  modalities: new Set(),
  regions: new Set(),   // region keys, plus the literal "Repository"
  toggles: new Set(),
  sort: "region",
};

let DATA = [];

const $ = sel => document.querySelector(sel);

async function boot() {
  try {
    const res = await fetch("data/datasets.json", { cache: "no-cache" });
    DATA = await res.json();
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
    $("#search").value = "";
    document.querySelectorAll(".chip[aria-pressed='true']").forEach(c => c.setAttribute("aria-pressed", "false"));
    render();
  });
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

/* Tiered, field-boosted ranking. Returns null when there is no query (browse mode),
   else { t1, t2 }: t1 = title/name/id matches (shown first), t2 = extended matches
   in description/labels/metadata (shown below a divider). Punctuation/space-insensitive
   so "picai" -> PI-CAI and "MR RATE" -> MR-RATE. */
function searchRank(list, q) {
  q = (q || "").trim();
  if (!q) return null;
  const sqQuery = squash(q);
  if (!sqQuery) return null;
  // word-boundary tokens: a token matches a word that starts with it (prefix), so
  // "rate" won't match inside "accurate" and "mr" still matches "MRI".
  const tokens = q.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean);
  const allTok = wblob => tokens.length > 0 && tokens.every(t => wblob.includes(" " + t));
  const t1 = [], t2 = [];
  for (const d of list) {
    const x = searchIndex(d);
    let score = 0, tier = 0;
    if (x.sqName === sqQuery) { score = 100; tier = 1; }
    else if (x.sqName.startsWith(sqQuery)) { score = 90; tier = 1; }
    else if (x.sqName.includes(sqQuery)) { score = 80; tier = 1; }
    else if (x.sqTitle.includes(sqQuery)) { score = 70; tier = 1; }
    else if (allTok(x.wtitle)) { score = 60; tier = 1; }
    else if (x.sq.includes(sqQuery)) { score = 40; tier = 2; }
    else if (allTok(x.wraw)) { score = 20; tier = 2; }
    else continue;
    (tier === 1 ? t1 : t2).push({ d, score });
  }
  const by = (a, b) => b.score - a.score || (b.d.year || 0) - (a.d.year || 0) || a.d.name.localeCompare(b.d.name);
  t1.sort(by); t2.sort(by);
  return { t1: t1.map(o => o.d), t2: t2.map(o => o.d) };
}

const SEARCH_CAP = 150;   // max cards rendered while searching (keeps typing smooth)

function renderSearchHTML(t1, t2) {
  let html = "";
  if (t1.length) html += `<div class="grid">${t1.map(card).join("")}</div>`;
  const room = Math.max(t1.length ? 0 : 30, SEARCH_CAP - t1.length);
  const shownT2 = t2.slice(0, room);
  if (shownT2.length) {
    const label = t1.length
      ? `More results — matched in description, labels or metadata (${t2.length})`
      : `No title matches — showing matches in description, labels or metadata (${t2.length})`;
    html += `<div class="tier-divider"><span>${label}</span></div>`;
    html += `<div class="grid">${shownT2.map(card).join("")}</div>`;
  }
  const hidden = t2.length - shownT2.length;
  if (hidden > 0) html += `<div class="tier-more">+${hidden} more extended matches — refine your search to see them.</div>`;
  return html;
}

function searchIndex(d) {
  if (d._sidx) return d._sidx;
  const parts = [
    d.id, d.name, d.full_name, d.description, d.anatomy,
    (d.modality || []).join(" "),
    (d.regions || []).map(r => REGION_LABEL[r] || r).join(" "), (d.regions || []).join(" "),
    (d.tags || []).join(" "), (d.tasks || []).join(" "), (d.other_labels || []).join(" "),
    d.host, (d.format || []).join(" "), d.license, d.size, d.year,
    d.clinical_variables, d.segmentation_detail, d.multi_sequence_detail, d.paired_text_detail,
    d.details ? (d.details.label_schema || []).join(" ") : "",
  ];
  const raw = parts.filter(Boolean).join(" ").toLowerCase();
  const wordify = s => " " + String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim() + " ";
  d._sidx = {
    sq: raw.replace(/[^a-z0-9]+/g, ""),                          // punctuation-free blob
    sqName: squash(d.name),
    sqTitle: squash([d.id, d.name, d.full_name].filter(Boolean).join(" ")),
    wraw: wordify(raw),                                          // word-boundary blob (for prefix tokens)
    wtitle: wordify([d.id, d.name, d.full_name].filter(Boolean).join(" ")),
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
    const total = ranked.t1.length + ranked.t2.length;
    $("#count").innerHTML = `<b>${total}</b> of ${DATA.length} · <span class="count-sub">by relevance</span>`;
    results.innerHTML = total ? renderSearchHTML(ranked.t1, ranked.t2) : EMPTY_HTML;
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
  if (d.multi_sequence) badges.push(`<span class="badge seq" title="${esc(d.multi_sequence_detail || "Multi-sequence / multi-phase")}">≋ Multi-seq</span>`);
  if (hasTag(d, "population-cohort")) badges.push(`<span class="badge cohort" title="Population / epidemiological cohort${d.clinical_variables ? " — " + esc(d.clinical_variables) : ""}">◉ Cohort</span>`);
  if (d.body_composition) badges.push(`<span class="badge bodycomp" title="Body-composition phenotypes available (VAT/ASAT/muscle/DXA)">⚖ Body comp</span>`);
  const fmt = (d.format || []).slice(0, 3).map(f => `<span class="badge fmt">${esc(f)}</span>`).join("");

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
    ? `<a href="${esc(d.url)}" target="_blank" rel="noopener">${esc(d.name)}</a>`
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
  if (d.url) links.push(`<a href="${esc(d.url)}" target="_blank" rel="noopener">Official source ↗</a>`);
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
    if (dt.extra) parts += `<p class="note">${esc(dt.extra)}</p>`;
    structure = `<section class="detail-structure">${parts}</section>`;
  } else {
    structure = `<section class="detail-structure detail-structure-empty">
      <h4>Data & label structure</h4>
      <p>A detailed label schema hasn't been catalogued for this ${d.type === "repository" ? "repository" : "dataset"} yet.
      The fields above summarize what's inside; see the
      <a href="${esc(d.url || "#")}" target="_blank" rel="noopener">official source</a>
      for the exact folder layout and label definitions.
      <a href="https://github.com/JungOhLee/radiology-dataset-hub/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Contribute it →</a></p>
    </section>`;
  }

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
        ${row("Format", d.format)}
        ${boolRow("Raw image (DICOM/NIfTI)", d.raw_image)}
        ${row("Size", d.size)}
        ${boolRow("Paired text / image–text", d.paired_text, d.paired_text_detail)}
        ${boolRow("Multi-sequence / phase", d.multi_sequence, d.multi_sequence_detail)}
        ${boolRow("Segmentation labels", d.segmentation, d.segmentation_detail)}
        ${d.clinical_variables ? row("Linkable clinical data", d.clinical_variables) : ""}
        ${d.body_composition ? boolRow("Body composition", d.body_composition) : ""}
        ${d.longitudinal ? boolRow("Longitudinal (repeat imaging)", d.longitudinal) : ""}
        ${row("Other labels", d.other_labels)}
        ${(d.tags && d.tags.length) ? row("Tags", d.tags) : ""}
        ${row("Tasks", d.tasks)}
        ${row("Access", accessMap[d.access] || d.access)}
        ${row("License", d.license)}
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
