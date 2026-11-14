"use strict";

const $ = (id) => document.getElementById(id);
const NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
const noteName = (n) => `${NOTES[n % 12]}${Math.floor(n / 12) - 2}`;
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const state = {
  samples: [], groups: null, selected: 0, rack: null, pad: null, shortlist: null,
  base: 36, mode: null, lastHit: 0, launchpad: null,
};

async function api(method, url, body) {
  const response = await fetch(url, {
    method, headers: body ? { "Content-Type": "application/json" } : {},
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw Object.assign(new Error(data.detail || response.statusText), { status: response.status });
  return data;
}
const get = (url) => api("GET", url);
const fail = (error) => alert(error.message);

// ---------------------------------------------------------------- audio

const player = new Audio();
function play(sampleId) {
  player.pause();
  player.src = `/api/samples/${sampleId}/audio`;
  player.currentTime = 0;
  player.play().catch(fail);
}

// ---------------------------------------------------------------- status

async function refreshStatus() {
  try {
    const s = await get("/api/status");
    const c = s.counts;
    $("status").textContent = `${c.samples} samples · ${c.analyzed} analyzed · ${c.excluded} excluded · ` +
      (s.library.scanning ? "scanning… " : "") + (s.library.analyzing ? "analyzing… " : "") + (s.library.message || "");
  } catch (e) { $("status").textContent = "server unreachable"; }
}

async function loadFilters() {
  const [folders, racks] = await Promise.all([get("/api/folders"), get("/api/source-racks")]);
  const folder = $("folder").value;
  $("folder").innerHTML = '<option value="">All folders</option>' +
    folders.map((f) => `<option value="${esc(f.folder)}">${esc(f.folder.split("/").slice(-2).join("/"))} (${f.n})</option>`).join("");
  $("folder").value = folder;
  const rackOptions = racks.map((r) => `<option value="${r.id}">${esc(r.name)} (${r.pads} pads${r.origin === "builder" ? ", builder" : ""})</option>`).join("");
  const rf = $("rackfilter").value;
  $("rackfilter").innerHTML = '<option value="">Any rack</option>' + rackOptions;
  $("rackfilter").value = rf;
  $("sourcerack").innerHTML = '<option value="">Duplicate an existing rack…</option>' + rackOptions;
}

// ---------------------------------------------------------------- sample browser

let searchTimer = null;
function scheduleSearch() { clearTimeout(searchTimer); searchTimer = setTimeout(search, 200); }

async function search() {
  const params = new URLSearchParams({
    q: $("q").value, folder: $("folder").value, rack: $("rackfilter").value, excluded: $("excluded").value,
    sort: $("sort").value, group: $("group").value, limit: 1000,
  });
  try {
    const data = await get(`/api/samples?${params}`);
    state.samples = data.samples;
    state.groups = data.groups || null;
    state.selected = Math.min(state.selected, Math.max(0, data.samples.length - 1));
    $("count").textContent = `${data.total} match${data.total === 1 ? "" : "es"}` + (data.total > data.samples.length ? ` (showing ${data.samples.length})` : "");
    renderSamples();
  } catch (e) { fail(e); }
}

function fmt(sample) {
  const d = sample.duration == null ? "–" : sample.duration < 1 ? `${Math.round(sample.duration * 1000)} ms` : `${sample.duration.toFixed(1)} s`;
  const p = sample.pitch_midi == null || sample.pitch_confidence < 0.6 ? "–" : noteName(Math.round(sample.pitch_midi));
  const level = sample.lufs ?? sample.rms_db;
  const l = level == null ? "–" : `${level.toFixed(0)} ${sample.lufs != null ? "LU" : "dB"}`;
  const b = sample.centroid_hz == null ? "–" : sample.centroid_hz >= 1000 ? `${(sample.centroid_hz / 1000).toFixed(1)} kHz` : `${Math.round(sample.centroid_hz)} Hz`;
  return { d, p, l, b };
}

function rowHtml(sample, index) {
  const f = fmt(sample);
  const err = sample.analysis_error ? ` title="${esc(sample.analysis_error)}"` : "";
  return `<div class="row${index === state.selected ? " selected" : ""}${sample.excluded ? " excluded" : ""}" data-i="${index}"${err}>
    <button class="play" data-act="play">▶</button>
    <div><span class="name">${esc(sample.name)}</span><span class="folder">${esc(sample.folder)}</span></div>
    <span class="num" title="duration">${f.d}</span><span class="num" title="pitch">${f.p}</span>
    <span class="num" title="loudness">${f.l}</span><span class="num" title="brightness (spectral centroid)">${f.b}</span>
    <span class="actions">
      <button data-act="exclude" title="X">${sample.excluded ? "Include" : "Exclude"}</button>
      <button data-act="assign" title="A: assign to the selected pad">→ pad</button>
      <button data-act="shortlist" title="S: add to the open shortlist">+ list</button>
    </span></div>`;
}

function renderSamples() {
  const box = $("samples");
  if (state.groups) {
    const index = new Map(state.samples.map((s, i) => [s.id, i]));
    box.innerHTML = state.groups.map((g) => `<div class="grouphead">${esc(g.label)} (${g.ids.length})</div>` +
      g.ids.map((id) => rowHtml(state.samples[index.get(id)], index.get(id))).join("")).join("");
  } else {
    box.innerHTML = state.samples.map(rowHtml).join("");
  }
}

function selectRow(index, scroll = true) {
  if (!state.samples.length) return;
  state.selected = Math.max(0, Math.min(state.samples.length - 1, index));
  document.querySelectorAll("#samples .row.selected").forEach((r) => r.classList.remove("selected"));
  const row = document.querySelector(`#samples .row[data-i="${state.selected}"]`);
  if (row) { row.classList.add("selected"); if (scroll) row.scrollIntoView({ block: "nearest" }); }
}

async function sampleAction(action, sample) {
  if (action === "play") return play(sample.id);
  if (action === "exclude") {
    await api("POST", `/api/samples/${sample.id}/exclude`, { excluded: !sample.excluded });
    sample.excluded = !sample.excluded;
    if ($("excluded").value === "hide" && sample.excluded || $("excluded").value === "only" && !sample.excluded) {
      state.samples.splice(state.samples.indexOf(sample), 1);
      if (state.groups) state.groups.forEach((g) => { g.ids = g.ids.filter((id) => id !== sample.id); });
    }
    renderSamples(); selectRow(state.selected);
    return;
  }
  if (action === "assign") {
    if (!state.rack || state.pad == null) return alert("Select a rack and a pad first.");
    state.rack = await api("PUT", `/api/racks/${state.rack.id}/pads/${state.pad}`, { sample_id: sample.id, keep: false });
    return renderRack();
  }
  if (action === "shortlist") {
    if (!state.shortlist) return alert("Open a pad's shortlist first (select a pad, then create or open a shortlist).");
    await api("POST", `/api/shortlists/${state.shortlist}/items`, { sample_id: sample.id });
    state.rack = await get(`/api/racks/${state.rack.id}`);
    return renderRack();
  }
}

$("samples").addEventListener("click", (event) => {
  const row = event.target.closest(".row");
  if (!row) return;
  const index = Number(row.dataset.i);
  selectRow(index, false);
  const action = event.target.dataset.act;
  if (action) sampleAction(action, state.samples[index]).catch(fail);
});
$("samples").addEventListener("dblclick", (event) => {
  const row = event.target.closest(".row");
  if (row) play(state.samples[Number(row.dataset.i)].id);
});

// Keyboard shortcuts act on the browser list unless the focus is in a text field.
document.addEventListener("keydown", (event) => {
  if (event.target.matches("input, select, textarea") || event.metaKey || event.ctrlKey) return;
  if (state.mode === "pairwise" && ["1", "2", "ArrowLeft", "ArrowRight"].includes(event.key)) return comparisonKey(event);
  const sample = state.samples[state.selected];
  const keys = {
    ArrowDown: () => { selectRow(state.selected + 1); if (sample) play(state.samples[state.selected].id); },
    ArrowUp: () => { selectRow(state.selected - 1); if (sample) play(state.samples[state.selected].id); },
    " ": () => sample && play(sample.id),
    x: () => sample && sampleAction("exclude", sample),
    a: () => sample && sampleAction("assign", sample),
    s: () => sample && sampleAction("shortlist", sample),
  };
  const handler = keys[event.key];
  if (handler) { event.preventDefault(); Promise.resolve(handler()).catch(fail); }
});

["q"].forEach((id) => $(id).addEventListener("input", scheduleSearch));
["folder", "rackfilter", "excluded", "sort", "group"].forEach((id) => $(id).addEventListener("change", search));
$("rescan").addEventListener("click", async () => {
  $("status").textContent = "scanning…";
  await api("POST", "/api/scan").catch(fail);
  await Promise.all([loadFilters(), search(), refreshStatus()]);
});

// ---------------------------------------------------------------- racks

async function loadRacks(selectId) {
  const racks = await get("/api/racks");
  $("rackselect").innerHTML = '<option value="">Choose a rack…</option>' +
    racks.map((r) => `<option value="${r.id}">${esc(r.name)} (${r.pad_count} pads)</option>`).join("");
  if (selectId) { $("rackselect").value = selectId; await openRack(selectId); }
}

async function openRack(id) {
  state.pad = null; state.shortlist = null; state.mode = null;
  $("compare").innerHTML = ""; $("report").innerHTML = "";
  if (!id) { state.rack = null; return renderRack(); }
  state.rack = await get(`/api/racks/${id}`);
  $("filename").value = state.rack.name;
  const notes = state.rack.pads.map((p) => p.note);
  if (notes.length) state.base = Math.max(0, Math.min(64, Math.floor(Math.min(...notes) / 4) * 4));
  if (state.launchpad?.connected) await api("POST", "/api/launchpad/rack", { rack_id: state.rack.id });
  renderRack();
}

function padState(note) {
  const pad = state.rack?.pads.find((p) => p.note === note);
  if (pad && pad.sample_id != null) return { pad, cls: pad.sample_missing ? "missing" : pad.keep ? "kept" : "assigned" };
  if (state.rack?.shortlists.some((s) => s.note === note)) return { pad, cls: "shortlist" };
  return { pad, cls: "" };
}

function renderRack() {
  const rack = state.rack;
  $("rackinfo").textContent = rack
    ? `${rack.pads.length} pads · ${rack.base_path ? "duplicate of " + rack.base_path.split("/").pop() : "new rack from the default template"}` +
      (rack.last_export ? ` · last exported to ${rack.last_export}` : "")
    : "Create a rack or duplicate one to start assigning pads.";
  $("bank").textContent = `${noteName(state.base)}–${noteName(state.base + 63)}`;
  const cells = [];
  for (let row = 7; row >= 0; row--) {
    for (let column = 0; column < 8; column++) {
      if (column === 4) cells.push('<div class="gap"></div>');
      const note = state.base + (column < 4 ? 0 : 32) + row * 4 + (column % 4);
      const { pad, cls } = padState(note);
      const label = pad ? (pad.name || pad.sample_name || pad.base_label || "") : (rack?.shortlists.find((s) => s.note === note)?.name || "");
      cells.push(`<div class="cell ${cls}${state.pad === note ? " selected" : ""}" data-note="${note}">
        <span class="n">${noteName(note)} · ${note}</span><span class="l">${esc(label)}</span></div>`);
    }
  }
  $("grid").innerHTML = rack ? cells.join("") : "";
  renderPad();
}

$("grid").addEventListener("click", (event) => {
  const cell = event.target.closest(".cell");
  if (!cell) return;
  const note = Number(cell.dataset.note);
  state.pad = note;
  const lists = state.rack.shortlists.filter((s) => s.note === note);
  state.shortlist = lists.length ? lists[0].id : null;
  state.mode = null; $("compare").innerHTML = "";
  const { pad } = padState(note);
  if (pad?.sample_id != null && !pad.sample_missing) play(pad.sample_id);
  renderRack();
});

function renderPad() {
  const box = $("pad");
  if (!state.rack || state.pad == null) { box.innerHTML = ""; return; }
  const note = state.pad;
  const { pad } = padState(note);
  const lists = state.rack.shortlists.filter((s) => s.note === note);
  const sample = pad && pad.sample_id != null
    ? `<button class="play" data-play="${pad.sample_id}">▶</button> ${esc(pad.sample_name)}${pad.keep ? " <em>(kept from source)</em>" : ""}${pad.sample_missing ? ' <span class="bad">missing</span>' : ""}`
    : "<em>no sample</em>";
  const source = pad?.source_note != null ? `starts from source pad ${noteName(pad.source_note)}: ${esc(pad.base_label)}` : "new pad (default Simpler)";
  box.innerHTML = `<div class="box"><h3>Pad ${noteName(note)} (${note})</h3>
    <div class="line">Sample: ${sample}</div>
    ${pad ? `<div class="line">${source}</div>
      <div class="line"><label>Name <input id="padname" value="${esc(pad.name)}" placeholder="${esc(pad.sample_name || "")}"></label>
        <button id="padrename">Rename</button>
        <label>Move to <input id="padmove" type="number" min="0" max="127" value="${note}" style="width:5em"></label><button id="padmovebtn">Move</button>
        ${pad.source_note != null && !pad.keep ? '<button id="padrevert">Revert to source sample</button>' : ""}
        <button id="padclear">Remove pad</button></div>` : ""}
    <h3>Shortlists</h3>
    ${lists.map((l) => `<div class="box" data-list="${l.id}">
      <div class="line"><strong>${esc(l.name)}</strong> (${l.items.length})
        <button data-listact="open">${state.shortlist === l.id ? "open ✓" : "Open"}</button>
        <button data-listact="pairwise">Compare in pairs</button><button data-listact="bracket">Bracket</button>
        <button data-listact="rename">Rename</button><button data-listact="delete">Delete</button></div>
      ${l.items.map((i) => `<div class="cand"><button class="play" data-play="${i.sample_id}">▶</button>
        <span class="name">${esc(i.name)}</span>
        <button data-candact="assign" data-sample="${i.sample_id}">Assign</button>
        <button data-candact="remove" data-sample="${i.sample_id}">✕</button></div>`).join("")}
    </div>`).join("")}
    <div class="line"><input id="newlist" placeholder="Shortlist name, e.g. Kick"><button id="newlistbtn">Add shortlist</button></div>
  </div>`;
  const on = (id, fn) => $(id) && $(id).addEventListener("click", () => fn().catch(fail));
  const rackUrl = `/api/racks/${state.rack.id}`;
  on("padrename", async () => { state.rack = await api("PUT", `${rackUrl}/pads/${note}`, { sample_id: pad.sample_id, keep: !!pad.keep, name: $("padname").value }); renderRack(); });
  on("padmovebtn", async () => { const target = Number($("padmove").value); state.rack = await api("POST", `${rackUrl}/pads/${note}/move`, { target }); state.pad = target; renderRack(); });
  on("padrevert", async () => { state.rack = await api("POST", `${rackUrl}/pads/${note}/revert`); renderRack(); });
  on("padclear", async () => { if (confirm("Remove this pad from the rack?")) { state.rack = await api("DELETE", `${rackUrl}/pads/${note}`); renderRack(); } });
  on("newlistbtn", async () => {
    const name = $("newlist").value.trim() || `${noteName(note)} candidates`;
    const list = await api("POST", `${rackUrl}/pads/${note}/shortlists`, { name });
    state.shortlist = list.id; state.rack = await get(rackUrl); renderRack();
  });
}

$("pad").addEventListener("click", (event) => {
  const t = event.target;
  if (t.dataset.play) return play(Number(t.dataset.play));
  const listBox = t.closest("[data-list]");
  if (!listBox) return;
  const listId = Number(listBox.dataset.list);
  const rackUrl = `/api/racks/${state.rack.id}`;
  const run = async () => {
    if (t.dataset.listact === "open") { state.shortlist = listId; return renderPad(); }
    if (t.dataset.listact === "pairwise") { state.shortlist = listId; return openPairwise(); }
    if (t.dataset.listact === "bracket") { state.shortlist = listId; return openBracket(); }
    if (t.dataset.listact === "rename") {
      const name = prompt("Shortlist name"); if (!name) return;
      await api("PATCH", `/api/shortlists/${listId}`, { name });
    }
    if (t.dataset.listact === "delete") {
      if (!confirm("Delete this shortlist and its comparisons?")) return;
      await api("DELETE", `/api/shortlists/${listId}`);
      if (state.shortlist === listId) state.shortlist = null;
    }
    if (t.dataset.candact === "assign") await api("PUT", `${rackUrl}/pads/${state.pad}`, { sample_id: Number(t.dataset.sample), keep: false });
    if (t.dataset.candact === "remove") await api("DELETE", `/api/shortlists/${listId}/items/${t.dataset.sample}`);
    state.rack = await get(rackUrl); renderRack();
  };
  run().catch(fail);
});

// ---------------------------------------------------------------- comparison

const nameOf = (id) => {
  for (const list of state.rack.shortlists) for (const item of list.items) if (item.sample_id === id) return item.name;
  return `#${id}`;
};

async function focus(sampleId) {
  play(sampleId);
  if (state.launchpad?.connected) await api("POST", "/api/launchpad/focus", { note: state.pad, sample_id: sampleId });
}

async function openPairwise() {
  state.mode = "pairwise";
  const data = await get(`/api/shortlists/${state.shortlist}/pairwise`);
  state.pair = data.pair;
  const rows = data.ranking.map((r, i) => `<tr><td>${i + 1}</td><td>${esc(nameOf(r.sample_id))}</td><td>${r.wins}–${r.losses}</td><td>${r.score}</td>
    <td><button data-assign="${r.sample_id}">Assign</button></td></tr>`).join("");
  const versus = data.pair
    ? `<div class="versus">${data.pair.map((id, i) => `<div class="side"><div>${i ? "B" : "A"}: ${esc(nameOf(id))}</div>
        <div class="line" style="justify-content:center"><button data-focus="${id}">▶ ${i ? "2" : "1"}</button>
        <button class="primary" data-win="${id}" data-lose="${data.pair[1 - i]}">Prefer ${i ? "B (→)" : "A (←)"}</button></div></div>`).join("")}</div>`
    : "<p>Add at least two candidates to compare.</p>";
  $("compare").innerHTML = `<div class="box"><h3>Pairwise · ${data.votes} votes</h3>
    <p class="hint">1/2 play A/B · ←/→ prefer A/B. With the Launchpad connected, the pad plays the candidate you last played.</p>
    ${versus}<div class="line"><button id="undo">Undo last vote</button><button id="closecmp">Close</button></div>
    <table><tr><th>#</th><th>Sample</th><th>W–L</th><th>Score</th><th></th></tr>${rows}</table></div>`;
  $("compare").scrollIntoView({ block: "nearest" });
  $("undo").onclick = () => api("DELETE", `/api/shortlists/${state.shortlist}/votes/last`).then(openPairwise).catch(fail);
  $("closecmp").onclick = closeCompare;
}

async function vote(winner, loser) {
  await api("POST", `/api/shortlists/${state.shortlist}/votes`, { winner, loser });
  await openPairwise();
}

function comparisonKey(event) {
  if (!state.pair) return;
  event.preventDefault();
  const [a, b] = state.pair;
  const actions = { 1: () => focus(a), 2: () => focus(b), ArrowLeft: () => vote(a, b), ArrowRight: () => vote(b, a) };
  actions[event.key]().catch(fail);
}

async function openBracket() {
  state.mode = "bracket";
  let data = await get(`/api/shortlists/${state.shortlist}/bracket`);
  if (!data.bracket) data = await api("POST", `/api/shortlists/${state.shortlist}/bracket`);
  renderBracket(data);
}

function renderBracket(data) {
  const rounds = data.bracket.rounds.map((round, r) => `<div class="round"><strong>${r === data.bracket.rounds.length - 1 ? "Final" : `Round ${r + 1}`}</strong>
    ${round.map((m) => `<div class="m">${[m.a, m.b].map((id) => id == null ? "<em>bye</em>" : `<div class="${m.winner === id ? "w" : ""}">${esc(nameOf(id))}</div>`).join("")}</div>`).join("")}</div>`).join("");
  const current = data.current
    ? `<div class="versus">${[data.current.a, data.current.b].map((id) => `<div class="side"><div>${esc(nameOf(id))}</div>
        <div class="line" style="justify-content:center"><button data-focus="${id}">▶</button><button class="primary" data-pick="${id}">Advance</button></div></div>`).join("")}</div>`
    : `<p>Champion: <strong>${esc(nameOf(data.champion))}</strong> <button data-assign="${data.champion}">Assign to pad</button></p>`;
  $("compare").innerHTML = `<div class="box"><h3>Bracket (seeded by the pairwise ranking)</h3>${current}
    <div class="rounds">${rounds}</div><div class="line"><button id="restart">New bracket</button><button id="closecmp">Close</button></div></div>`;
  $("compare").scrollIntoView({ block: "nearest" });
  $("restart").onclick = () => api("POST", `/api/shortlists/${state.shortlist}/bracket`).then(renderBracket).catch(fail);
  $("closecmp").onclick = closeCompare;
}

function closeCompare() {
  state.mode = null; state.pair = null; $("compare").innerHTML = "";
  if (state.launchpad?.connected) api("POST", "/api/launchpad/focus", { note: state.pad, sample_id: null }).catch(fail);
}

$("compare").addEventListener("click", (event) => {
  const t = event.target;
  const run = async () => {
    if (t.dataset.focus) return focus(Number(t.dataset.focus));
    if (t.dataset.win) return vote(Number(t.dataset.win), Number(t.dataset.lose));
    if (t.dataset.pick) return renderBracket(await api("POST", `/api/shortlists/${state.shortlist}/bracket/pick`, { winner: Number(t.dataset.pick) }));
    if (t.dataset.assign) {
      state.rack = await api("PUT", `/api/racks/${state.rack.id}/pads/${state.pad}`, { sample_id: Number(t.dataset.assign), keep: false });
      renderRack();
    }
  };
  run().catch(fail);
});

// ---------------------------------------------------------------- rack actions

$("rackselect").addEventListener("change", () => openRack($("rackselect").value).catch(fail));
$("newrack").addEventListener("click", async () => {
  const name = prompt("Name for the new rack"); if (!name) return;
  const rack = await api("POST", "/api/racks", { name }).catch(fail);
  if (rack) await loadRacks(rack.id);
});
$("duplicate").addEventListener("click", async () => {
  const source = $("sourcerack").value;
  if (!source) return alert("Choose a rack to duplicate.");
  const label = $("sourcerack").selectedOptions[0].textContent.replace(/ \(.*$/, "");
  const name = prompt("Name for the copy", `${label} copy`); if (!name) return;
  const rack = await api("POST", "/api/racks", { name, source }).catch(fail);
  if (rack) await loadRacks(rack.id);
});
$("renamerack").addEventListener("click", async () => {
  if (!state.rack) return;
  const name = prompt("Rack name", state.rack.name); if (!name) return;
  await api("PATCH", `/api/racks/${state.rack.id}`, { name }).catch(fail);
  await loadRacks(state.rack.id);
});
$("deleterack").addEventListener("click", async () => {
  if (!state.rack || !confirm(`Delete "${state.rack.name}" from the builder? Exported .adg files stay where they are.`)) return;
  await api("DELETE", `/api/racks/${state.rack.id}`).catch(fail);
  await loadRacks(); await openRack("");
});
$("bankup").addEventListener("click", () => { state.base = Math.min(64, state.base + 16); renderRack(); });
$("bankdown").addEventListener("click", () => { state.base = Math.max(0, state.base - 16); renderRack(); });

$("export").addEventListener("click", async () => {
  if (!state.rack) return;
  const filename = $("filename").value.trim() || state.rack.name;
  let result;
  try {
    result = await api("POST", `/api/racks/${state.rack.id}/export`, { filename, overwrite: false });
  } catch (e) {
    if (!/already exists|source rack/.test(e.message)) return fail(e);
    if (!confirm(`${e.message}\n\nReplace it? The current file is copied to the builder's backups first.`)) return;
    result = await api("POST", `/api/racks/${state.rack.id}/export`, { filename, overwrite: true }).catch(fail);
    if (!result) return;
  }
  const r = result.report;
  $("report").innerHTML = `<div class="box"><h3 class="${r.ok ? "ok" : "bad"}">${r.ok ? "Exported and verified" : "Exported with problems"}</h3>
    <div>${esc(result.path)}</div>${result.backup ? `<div>Previous file backed up to ${esc(result.backup)}</div>` : ""}
    <div>${r.preserved_pads} kept · ${r.replaced_pads} replaced · ${r.added_pads} added · ${r.removed_pads} removed · rack settings ${r.device_settings_preserved ? "preserved" : "changed"}</div>
    ${r.problems.length ? `<ul class="bad">${r.problems.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>` : ""}</div>`;
  state.rack = await get(`/api/racks/${state.rack.id}`);
  renderRack(); loadFilters();
});

// ---------------------------------------------------------------- Launchpad

async function refreshLaunchpad() {
  try { state.launchpad = await get("/api/launchpad"); } catch (e) { return; }
  const lp = state.launchpad;
  const box = $("launchpad");
  box.innerHTML = `<div class="box"><h3>Launchpad Pro MK3</h3>
    ${!lp.available ? `<p>Unavailable: ${esc(lp.reason)}</p>` : `
    <div class="line">${lp.connected ? '<span class="ok">connected</span> in Programmer Mode' : lp.ports.length ? `found ${esc(lp.ports[0])}` : "no Launchpad port found"}
      ${lp.connected ? '<button id="lpoff">Disconnect</button>' : lp.ports.length ? '<button id="lpon">Connect</button>' : ""}</div>
    <p class="hint">Connecting switches the Launchpad to Programmer Mode and plays the open rack through this computer's audio output; Live may also receive the pad notes. The arrows shift the grid by 16 notes (now ${noteName(lp.base_note)}). Disconnecting restores the previous layout.</p>
    ${lp.error ? `<p class="bad">${esc(lp.error)}</p>` : ""}`}</div>`;
  if ($("lpon")) $("lpon").onclick = async () => {
    await api("POST", "/api/launchpad/connect").catch(fail);
    if (state.rack) await api("POST", "/api/launchpad/rack", { rack_id: state.rack.id }).catch(fail);
    refreshLaunchpad();
  };
  if ($("lpoff")) $("lpoff").onclick = () => api("POST", "/api/launchpad/disconnect").then(refreshLaunchpad).catch(fail);
  const hit = lp.events.at(-1);
  if (hit && hit.time > state.lastHit) {
    state.lastHit = hit.time;
    const cell = document.querySelector(`.cell[data-note="${hit.note}"]`);
    if (cell) { cell.classList.add("hit"); setTimeout(() => cell.classList.remove("hit"), 250); }
  }
}

// ---------------------------------------------------------------- start

(async () => {
  await Promise.all([refreshStatus(), loadFilters().catch(fail), loadRacks().catch(fail), refreshLaunchpad()]);
  await search();
  renderRack();
  setInterval(refreshStatus, 3000);
  setInterval(() => (state.launchpad?.connected ? refreshLaunchpad() : null), 400);
  setInterval(() => (!state.launchpad?.connected ? refreshLaunchpad() : null), 5000);
  // The first scan runs in the background; refresh the lists once it has had a moment.
  setTimeout(() => { loadFilters().catch(() => {}); search(); }, 2500);
})();
