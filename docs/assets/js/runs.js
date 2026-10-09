/* Runs page: summary bar, per-paper-item progress, filterable + sortable run table. */

const filters = { owner: "all", state: "all", query: "", showSmoke: false };
let sortKey = "id";
let sortDir = 1;

const COLUMNS = [
  { key: "id", label: "Run" },
  { key: "owner", label: "Role" },
  { key: "state", label: "State" },
  { key: "item", label: "Paper item" },
  { key: "what", label: "What" },
  { key: "priority", label: "Prio" },
  { key: "gpu_hours", label: "GPU h", num: true },
  { key: "ta", label: "TA L2", num: true },
];

window.renderPage = function () {
  readHash();
  $("#summary").append(stateStack(DATA.runs));
  renderItems();
  renderToolbar();
  renderTable();
};

/* "#owner=B&state=done" pre-selects filters (used by links from the overview). */
function readHash() {
  const params = new URLSearchParams(location.hash.slice(1));
  if (params.get("owner")) filters.owner = params.get("owner");
  if (params.get("state")) filters.state = params.get("state");
}

function renderItems() {
  const groups = {};
  for (const r of DATA.runs.filter((r) => r.in_matrix)) (groups[r.item || "—"] ||= []).push(r);
  const rows = Object.entries(groups).sort((a, b) => b[1].length - a[1].length);
  $("#items").append(...rows.map(([item, runs]) => {
    const done = runs.filter((r) => r.state === "done").length;
    return el("div", { class: "item-bar" },
      el("span", { title: item }, item),
      stateStack(runs, { legend: false }),
      el("span", { class: "num muted" }, `${done}/${runs.length}`));
  }));
}

function renderToolbar() {
  const bar = $("#toolbar");
  const chipGroup = (label, key, options) =>
    el("div", { class: "group" }, el("span", {}, label),
      el("div", { class: "chips" }, options.map(([value, text]) =>
        el("button", {
          class: "chip" + (filters[key] === value ? " on" : ""),
          onclick: (e) => {
            filters[key] = value;
            $$(".chip", e.target.parentNode).forEach((c) => c.classList.toggle("on", c === e.target));
            renderTable();
          },
        }, text))));

  const presentStates = STATES.filter((s) => DATA.runs.some((r) => r.state === s.key));
  bar.append(
    chipGroup("Role", "owner", [["all", "All"], ...["A", "B", "C", "D"].map((o) => [o, o])]),
    chipGroup("State", "state", [["all", "All"], ...presentStates.map((s) => [s.key, s.label])]),
    el("label", { class: "small muted" },
      el("input", { type: "checkbox", onchange: (e) => { filters.showSmoke = e.target.checked; renderTable(); } }),
      " smoke & validation runs"),
    el("input", {
      class: "search", type: "search", placeholder: "Search id, data, notes…",
      oninput: (e) => { filters.query = e.target.value.toLowerCase(); renderTable(); },
    }));
}

function visibleRuns() {
  return DATA.runs
    .filter((r) => filters.owner === "all" || r.owner === filters.owner)
    .filter((r) => filters.state === "all" || r.state === filters.state)
    .filter((r) => filters.showSmoke || !r.smoke)
    .filter((r) => !filters.query ||
      [r.id, r.what, r.data, r.item, r.notes, r.kind].join(" ").toLowerCase().includes(filters.query))
    .map((r) => ({ ...r, ta: summaryOf(r, "rule_v1/test_L2")?.all?.TA }))
    .sort((a, b) => {
      const x = a[sortKey] ?? "", y = b[sortKey] ?? "";
      const nx = parseFloat(x), ny = parseFloat(y);
      if (!isNaN(nx) && !isNaN(ny)) return (nx - ny) * sortDir;
      return String(x).localeCompare(String(y), undefined, { numeric: true }) * sortDir;
    });
}

function renderTable() {
  const runs = visibleRuns();
  $("#count").textContent = `${runs.length} of ${DATA.runs.length} runs`;

  const table = $("#runs-table");
  table.innerHTML = "";
  table.append(el("thead", {}, el("tr", {}, COLUMNS.map((c) =>
    el("th", {
      class: c.num ? "num" : null,
      onclick: () => { sortDir = sortKey === c.key ? -sortDir : 1; sortKey = c.key; renderTable(); },
    }, c.label, sortKey === c.key ? (sortDir > 0 ? " ↑" : " ↓") : "")))));

  // Render in chunks so a long list stays responsive.
  const body = el("tbody");
  table.append(body);
  const row = (r) => el("tr", { class: "clickable", onclick: () => openRun(r) },
    el("td", { class: "id" }, r.id, r.smoke ? el("span", { class: "tag-smoke" }, "smoke") : null),
    el("td", {}, r.owner),
    el("td", {}, statePill(r.state)),
    el("td", { class: "small" }, r.item || "–"),
    el("td", { class: "what small" }, (r.what || "").slice(0, 110) + ((r.what || "").length > 110 ? "…" : "")),
    el("td", { class: "small" }, r.priority || "–"),
    el("td", { class: "num" }, r.gpu_hours != null ? fmt(+r.gpu_hours, 2) : "–"),
    el("td", { class: "num" }, fmt(r.ta)));
  let i = 0;
  const chunk = () => {
    body.append(...runs.slice(i, i + 80).map(row));
    i += 80;
    if (i < runs.length) requestAnimationFrame(chunk);
  };
  chunk();
}
