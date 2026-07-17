/* Radiology Dataset Hub — client logic (vanilla JS, no build step) */

const CATEGORY_ORDER = [
  "Neuro", "Chest", "Cardiac", "Vascular", "Abdomen", "Pelvis",
  "MSK", "Breast", "HeadNeck", "Dental", "WholeBody", "Multimodal", "Repository",
];
const CATEGORY_LABEL = {
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
  Multimodal: "Multimodal / Image–Text",
  Repository: "Data Repositories & Portals",
};
const CATEGORY_DESC = {
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
  WholeBody: "Whole-body PET/CT lesion imaging",
  Multimodal: "Paired reports, captions and VQA",
  Repository: "Hubs hosting many collections",
};
const CATEGORY_ICON = {
  Neuro: "🧠", Chest: "🫁", Cardiac: "🫀", Vascular: "🩸", Abdomen: "🩻",
  Pelvis: "⬇️", MSK: "🦴", Breast: "🎀", HeadNeck: "👤", Dental: "🦷",
  WholeBody: "🌐", Multimodal: "📝", Repository: "🗄️",
};
const CATEGORY_SHORT = {
  Neuro: "Neuro", Chest: "Chest", Cardiac: "Cardiac", Vascular: "Vascular",
  Abdomen: "Abdomen", Pelvis: "Pelvis", MSK: "MSK", Breast: "Breast",
  HeadNeck: "Head & Neck", Dental: "Dental", WholeBody: "Whole-body/PET",
  Multimodal: "Multimodal", Repository: "Repositories",
};
const MODALITIES = ["CT", "MRI", "PET", "X-ray"];

const TOGGLES = [
  { key: "raw_image", label: "Raw (DICOM/NIfTI)", test: d => d.raw_image === true },
  { key: "paired_text", label: "Paired text", test: d => d.paired_text === true },
  { key: "segmentation", label: "Segmentation", test: d => d.segmentation === true },
  { key: "multi_sequence", label: "Multi-seq/phase", test: d => d.multi_sequence === true },
  { key: "open", label: "Open access", test: d => d.access === "open" },
];

const state = {
  q: "",
  modalities: new Set(),
  categories: new Set(),
  toggles: new Set(),
  sort: "category",
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

function buildControls() {
  // modality chips
  const modWrap = $("#modality-filters");
  MODALITIES.forEach(m => {
    const b = chip(m, () => toggleSet(state.modalities, m, b));
    modWrap.appendChild(b);
  });
  // body-region filter chips (multi-select banners)
  const regionWrap = $("#region-filters");
  CATEGORY_ORDER.forEach(c => {
    const n = DATA.filter(d => d.category === c).length;
    if (!n) return;
    const b = document.createElement("button");
    b.className = "chip region-chip"; b.setAttribute("aria-pressed", "false");
    b.dataset.cat = c;
    b.innerHTML = `<span class="chip-ico">${CATEGORY_ICON[c] || ""}</span> ${CATEGORY_SHORT[c] || c} <span class="chip-n">${n}</span>`;
    b.addEventListener("click", () => toggleSet(state.categories, c, b));
    regionWrap.appendChild(b);
  });
  // toggle chips
  const tWrap = $("#toggle-filters");
  TOGGLES.forEach(t => {
    const b = chip(t.label, () => toggleSet(state.toggles, t.key, b));
    b.classList.add("toggle-chip");
    tWrap.appendChild(b);
  });
  // search
  $("#search").addEventListener("input", e => { state.q = e.target.value.toLowerCase().trim(); render(); });
  // sort
  $("#sort-select").addEventListener("change", e => { state.sort = e.target.value; render(); });
  // reset
  $("#reset").addEventListener("click", () => {
    state.q = ""; state.modalities.clear(); state.categories.clear(); state.toggles.clear();
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

function matches(d) {
  if (state.modalities.size && !(d.modality || []).some(m => state.modalities.has(m))) return false;
  if (state.categories.size && !state.categories.has(d.category)) return false;
  for (const key of state.toggles) {
    const t = TOGGLES.find(x => x.key === key);
    if (t && !t.test(d)) return false;
  }
  if (state.q) {
    const hay = [d.name, d.full_name, d.description, d.anatomy, (d.modality || []).join(" "),
      (d.tasks || []).join(" "), d.host, (d.format || []).join(" "), d.segmentation_detail,
      d.multi_sequence_detail, d.paired_text_detail].filter(Boolean).join(" ").toLowerCase();
    if (!hay.includes(state.q)) return false;
  }
  return true;
}

function render() {
  const list = DATA.filter(matches);
  $("#count").innerHTML = `<b>${list.length}</b> of ${DATA.length} datasets`;
  const results = $("#results");

  if (!list.length) {
    results.innerHTML = `<div class="empty"><h2>No datasets match</h2>
      <p>Try removing a filter or broadening your search.</p></div>`;
    return;
  }

  if (state.sort === "year" || state.sort === "name") {
    const sorted = [...list].sort((a, b) =>
      state.sort === "year" ? (b.year || 0) - (a.year || 0) : a.name.localeCompare(b.name));
    results.innerHTML = `<div class="grid">${sorted.map(card).join("")}</div>`;
    return;
  }

  // grouped by category
  let html = "";
  for (const cat of CATEGORY_ORDER) {
    const items = list.filter(d => d.category === cat);
    if (!items.length) continue;
    items.sort((a, b) => (b.year || 0) - (a.year || 0));
    html += `<section class="cat-section" id="cat-${cat}">
      <div class="cat-head">
        <span class="cat-ico">${CATEGORY_ICON[cat] || ""}</span>
        <h2>${CATEGORY_LABEL[cat] || cat}</h2>
        <span class="cat-count">${items.length}</span>
        <span class="cat-desc">${CATEGORY_DESC[cat] || ""}</span>
      </div>
      <div class="grid">${items.map(card).join("")}</div>
    </section>`;
  }
  results.innerHTML = html;
}

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"]/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function card(d) {
  const mods = (d.modality || []).map(m => `<span class="mod">${esc(m)}</span>`).join("");
  const badges = [];
  if (d.raw_image) badges.push(`<span class="badge raw" title="Native DICOM/NIfTI raw images">◆ Raw</span>`);
  if (d.paired_text) badges.push(`<span class="badge text" title="${esc(d.paired_text_detail || "Paired text")}">◨ Text</span>`);
  if (d.segmentation) badges.push(`<span class="badge seg" title="${esc(d.segmentation_detail || "Segmentation masks")}">▧ Seg</span>`);
  if (d.multi_sequence) badges.push(`<span class="badge seq" title="${esc(d.multi_sequence_detail || "Multi-sequence / multi-phase")}">≋ Multi</span>`);
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
      <p>A detailed label schema hasn't been catalogued for this dataset yet. The fields above summarize
      what's inside; see the <a href="${esc(d.url || "#")}" target="_blank" rel="noopener">official source</a>
      for the exact folder layout and label definitions.
      <a href="https://github.com/JungOhLee/radiology-dataset-hub/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Contribute it →</a></p>
    </section>`;
  }

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
        ${row("Body region", CATEGORY_LABEL[d.category] || d.category)}
        ${row("Anatomy", d.anatomy)}
        ${row("Modality", d.modality)}
        ${row("Year", d.year)}
        ${row("Format", d.format)}
        ${boolRow("Raw image (DICOM/NIfTI)", d.raw_image)}
        ${row("Size", d.size)}
        ${boolRow("Paired text", d.paired_text, d.paired_text_detail)}
        ${boolRow("Multi-sequence / phase", d.multi_sequence, d.multi_sequence_detail)}
        ${boolRow("Segmentation labels", d.segmentation, d.segmentation_detail)}
        ${row("Other labels", d.other_labels)}
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
