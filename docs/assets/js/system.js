/* System page: role flow diagram, rule library tiles, dataset registry, module list. */

window.renderPage = function () {
  renderFlow();
  renderLibrary();
  renderRegistry("all");
  renderModules();
};

/* Four role nodes, animated dashed edges between them. */
function renderFlow() {
  const nodes = [
    { id: "A", x: 20, title: "A · Rules & data", sub: ["engine.py · 353 rules", "triplets, ladder, twins"] },
    { id: "B", x: 260, title: "B · Training", sub: ["Qwen3.5-9B LoRA", "5 formats × 4 corpora"] },
    { id: "C", x: 500, title: "C · Evaluation", sub: ["metrics, judges, PRMs", "audit + clinical sets"] },
    { id: "D", x: 740, title: "D · Downstream", sub: ["answer selection, GRPO", "tables → paper"] },
  ];
  const W = 960, H = 200, w = 200, h = 96, y = 52;
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  const add = (parent, tag, attrs, text) => {
    const n = document.createElementNS(ns, tag);
    for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
    if (text != null) n.textContent = text;
    parent.append(n);
    return n;
  };

  // Edges: A→B, B→C, C→D, plus A→C (test sets) and B→D (adapters) as arcs.
  const mid = (n) => n.x + w / 2;
  for (let i = 0; i < 3; i++) {
    add(svg, "path", { class: "edge", d: `M${nodes[i].x + w} ${y + h / 2} L${nodes[i + 1].x} ${y + h / 2}` });
  }
  add(svg, "path", { class: "edge", d: `M${mid(nodes[0])} ${y} C${mid(nodes[0])} 0, ${mid(nodes[2])} 0, ${mid(nodes[2])} ${y}` });
  add(svg, "path", { class: "edge", d: `M${mid(nodes[1])} ${y + h} C${mid(nodes[1])} ${H}, ${mid(nodes[3])} ${H}, ${mid(nodes[3])} ${y + h}` });
  add(svg, "text", { x: (mid(nodes[0]) + mid(nodes[2])) / 2, y: 22, "text-anchor": "middle", class: "sub", fill: "var(--muted)", "font-size": 11 }, "frozen test sets");
  add(svg, "text", { x: (mid(nodes[1]) + mid(nodes[3])) / 2, y: H - 10, "text-anchor": "middle", fill: "var(--muted)", "font-size": 11 }, "kept adapters");

  for (const n of nodes) {
    const g = add(svg, "g", { class: "node", style: "cursor:pointer" });
    add(g, "rect", { x: n.x, y, width: w, height: h, rx: 14 });
    add(g, "text", { x: n.x + 16, y: y + 30 }, n.title);
    n.sub.forEach((s, i) => add(g, "text", { x: n.x + 16, y: y + 54 + i * 18, class: "sub" }, s));
    g.addEventListener("click", () => (location.href = `runs.html#owner=${n.id}`));
  }
  $("#flow").append(svg);
}

function renderLibrary() {
  const lib = DATA.library || {};
  const src = lib.rules_by_source || {};
  const tiles = [
    { value: lib.rules_total || 0, label: "rules in total" },
    { value: (src.grammar_sampled || 0), label: "grammar-sampled" },
    { value: (lib.rules_by_kind || {}).score || 0, label: "scoring rules" },
    { value: lib.invented_rules_L3inv || 0, label: "invented (L3, test only)" },
  ];
  $("#library").append(...tiles.map((t) =>
    el("div", { class: "card stat reveal" },
      el("div", { class: "value", "data-count": t.value }, "0"),
      el("div", { class: "label" }, t.label))));
}

function renderRegistry(split) {
  const sets = DATA.registry;
  const filter = $("#split-filter");
  if (!filter.childElementCount) {
    const splits = ["all", ...new Set(sets.map((s) => s.split || "other"))];
    filter.append(...splits.map((sp) => el("button", {
      class: "chip" + (sp === split ? " on" : ""),
      onclick: (e) => {
        $$(".chip", filter).forEach((c) => c.classList.toggle("on", c === e.target));
        renderRegistry(sp);
      },
    }, sp === "all" ? `All ${sets.length}` : sp)));
  }
  const rows = sets.filter((s) => split === "all" || (s.split || "other") === split);
  const maxRec = Math.max(...rows.map((s) => s.records || 0), 1);
  const table = $("#registry");
  table.innerHTML = "";
  table.append(
    el("thead", {}, el("tr", {}, ["Set", "Split", "Level", "Tier", "Groups", "Records", ""].map((h) =>
      el("th", { class: ["Groups", "Records"].includes(h) ? "num" : null }, h)))),
    el("tbody", {}, rows.map((s) => el("tr", {},
      el("td", { class: "id" }, s.name),
      el("td", {}, el("span", { class: "pill plain" }, s.split || "–")),
      el("td", { class: "small" }, s.level || "–"),
      el("td", { class: "small" }, s.tier || "–"),
      el("td", { class: "num" }, (s.groups ?? "–").toLocaleString()),
      el("td", { class: "num" }, (s.records ?? "–").toLocaleString()),
      el("td", { style: { width: "18%" } },
        el("div", { class: "split-bar" }, el("span", { style: { width: (100 * (s.records || 0)) / maxRec + "%" } })),
        s.frozen ? el("span", { class: "muted small" }, "frozen") : el("span", { class: "s-dropped small" }, "not frozen"))))));
}

function renderModules() {
  const byFolder = {};
  for (const m of DATA.modules) (byFolder[m.folder] ||= []).push(m);
  const titles = { selrm: "Library · selrm/", scripts: "Entry points · scripts/" };
  $("#modules").append(...Object.entries(byFolder).map(([folder, mods]) =>
    el("div", { class: "card reveal" },
      el("h3", {}, titles[folder] || folder),
      el("ul", { class: "list" }, mods.map((m) => el("li", {},
        el("div", { class: "module" }, el("code", {}, m.path.split("/")[1]), el("span", { class: "muted small num" }, `${m.loc} lines`)),
        m.doc ? el("div", { class: "muted small" }, m.doc) : null))))));
}
