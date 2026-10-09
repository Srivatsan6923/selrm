/* Results page: test_L2 bars with CIs, factorial heatmap, ladder and near-miss heatmaps.
   Every number comes from a run's summary in data.js; empty cells say "not run". */

const L2 = "rule_v1/test_L2";
const FORMATS = ["verdict", "rationale", "summary2", "value2", "ledger2"];
const CORPORA = ["blocks", "triplets", "natural", "balanced"];
const LADDER = [
  ["test_L0", "L0 seen"], ["test_L1", "L1 new rules"], ["test_L2", "L2 new classes"],
  ["test_L3inv", "L3 invented"], ["test_L3alt", "L3 alt"], ["test_hard", "Hard"],
];
let metric = "TA";

window.renderPage = function () {
  renderMetricSwitch();
  renderL2Chart();
  renderFactorial();
  renderLadder();
  renderKinds();
};

/* Short display name: "B-F-verdict-blocks-s0" -> "verdict · blocks · s0". */
function shortName(id) {
  return id.replace(/^B-F-/, "").replace(/^B-BB-/, "4B · ").replace(/^A-D14-/, "shortcut · ").replace(/-/g, " · ");
}

function renderMetricSwitch() {
  const seg = $("#metric-seg");
  for (const m of ["TA", "Rev", "Hold"]) {
    seg.append(el("button", {
      class: m === metric ? "on" : null,
      onclick: (e) => {
        metric = m;
        $$("button", seg).forEach((b) => b.classList.toggle("on", b === e.target));
        renderL2Chart(true);
      },
    }, m));
  }
}

/* Horizontal bars, one metric, CI whiskers where the summary has them. */
function renderL2Chart(animateNow = false) {
  const root = $("#l2-chart");
  root.innerHTML = "";
  const runs = reportableRuns()
    .filter((r) => summaryOf(r, L2)?.all)
    .map((r) => ({ run: r, s: summaryOf(r, L2) }))
    .sort((a, b) => (b.s.all[metric] ?? 0) - (a.s.all[metric] ?? 0));
  if (!runs.length) return root.append(el("p", { class: "muted" }, "not run"));

  const W = 900, labelW = 230, rowH = 30, top = 24, plotW = W - labelW - 50;
  const H = top + runs.length * rowH + 10;
  const x = (v) => labelW + (plotW * v) / 100;
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  const add = (tag, attrs, text) => {
    const n = document.createElementNS(ns, tag);
    for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
    if (text != null) n.textContent = text;
    svg.append(n);
    return n;
  };

  // Recessive grid at 0/25/50/75/100.
  for (const t of [0, 25, 50, 75, 100]) {
    add("line", { x1: x(t), x2: x(t), y1: top - 6, y2: H - 6, class: "grid-line" });
    add("text", { x: x(t), y: top - 10, "text-anchor": "middle" }, t);
  }

  runs.forEach(({ run, s }, i) => {
    const y = top + i * rowH;
    const v = s.all[metric] ?? 0;
    const isShortcut = run.id.startsWith("A-D14");
    add("text", { x: labelW - 12, y: y + 18, "text-anchor": "end" }, shortName(run.id));
    const bar = add("rect", {
      x: labelW, y: y + 8, width: Math.max(2, x(v) - labelW), height: 14, rx: 4, class: "bar",
      fill: isShortcut ? "var(--todo)" : "var(--accent)",
    });
    const ci = s.ci && s.ci[metric];
    if (ci) {
      add("line", { x1: x(ci[0]), x2: x(ci[1]), y1: y + 15, y2: y + 15, stroke: "var(--text)", "stroke-width": 1.5 });
      for (const c of ci) add("line", { x1: x(c), x2: x(c), y1: y + 10, y2: y + 20, stroke: "var(--text)", "stroke-width": 1.5 });
    }
    add("text", { x: x(v) + (ci ? Math.max(0, x(ci[1]) - x(v)) : 0) + 8, y: y + 19 }, fmt(v));

    // Hit target is the whole row, bigger than the mark.
    const hit = add("rect", { x: 0, y, width: W, height: rowH, fill: "transparent", style: "cursor:pointer" });
    const tip = `${run.id} · ${metric} ${fmt(v)}${ci ? ` [${fmt(ci[0])}, ${fmt(ci[1])}]` : ""} · Rev ${fmt(s.all.Rev)} · Hold ${fmt(s.all.Hold)} · n ${s.all.n}`;
    hit.addEventListener("mousemove", (e) => tooltip.show(tip, e));
    hit.addEventListener("mouseleave", tooltip.hide);
    hit.addEventListener("click", () => openRun(run));
    bar.style.transitionDelay = i * 40 + "ms";
  });

  root.append(svg, el("div", { class: "legend" },
    el("span", {}, el("i", { style: { background: "var(--accent)" } }), "trained reward model"),
    el("span", {}, el("i", { style: { background: "var(--todo)" } }), "shortcut / reference scorer (A-D14)"),
    el("span", {}, "— 95% CI, bootstrap over rules")));
  if (animateNow) requestAnimationFrame(() => root.classList.add("in"));
}

/* Generic heatmap: rows × cols, value getter, cell text in text tokens. */
function heatmap(rows, cols, get, { rowLabel = (r) => r, colLabel = (c) => c, onClick } = {}) {
  const grid = el("div", { class: "heat", style: { gridTemplateColumns: `minmax(110px, auto) repeat(${cols.length}, minmax(56px, 1fr))` } });
  grid.append(el("div"), ...cols.map((c) => el("div", { class: "head" }, colLabel(c))));
  for (const r of rows) {
    grid.append(el("div", { class: "head row-head" }, rowLabel(r)));
    for (const c of cols) {
      const cell = get(r, c);
      const v = cell?.value;
      grid.append(el("div", {
        class: "cell",
        style: {
          background: heatColor(v),
          color: typeof v === "number" && v > 55 ? "var(--heat-ink)" : "var(--text)",
          fontWeight: typeof v === "number" ? 600 : 400,
          cursor: cell?.run ? "pointer" : "default",
        },
        onmousemove: (e) => tooltip.show(cell?.tip || "not run", e),
        onmouseleave: tooltip.hide,
        onclick: () => cell?.run && onClick && onClick(cell.run),
      }, typeof v === "number" ? fmt(v) : el("span", { class: "muted small" }, "not run")));
    }
  }
  return el("div", { style: { overflowX: "auto" } }, grid);
}

function renderFactorial() {
  const cells = {};
  for (const r of reportableRuns()) {
    const m = r.id.match(/^B-F-(\w+)-(\w+)-s(\d+)$/);
    const ta = summaryOf(r, L2)?.all?.TA;
    if (!m || typeof ta !== "number") continue;
    (cells[m[1] + "|" + m[2]] ||= []).push({ ta, seed: m[3], run: r });
  }
  const totalPlanned = DATA.runs.filter((r) => /^B-F-/.test(r.id) && r.state !== "dropped").length;
  $("#factorial").append(
    heatmap(FORMATS, CORPORA, (f, c) => {
      const list = cells[f + "|" + c];
      if (!list) return null;
      const mean = list.reduce((s, x) => s + x.ta, 0) / list.length;
      return { value: mean, run: list[0].run,
        tip: `${f} × ${c}: ${list.map((x) => `s${x.seed} ${fmt(x.ta)}`).join(", ")}` };
    }, { onClick: openRun }),
    el("p", { class: "muted small" },
      `${Object.values(cells).flat().length} finished factorial runs of ${totalPlanned} planned. Click a cell for its run.`));
}

function renderLadder() {
  const runs = reportableRuns().filter((r) => summaryOf(r, "rule_v1/test_L0"));
  if (!runs.length) return $("#ladder").append(el("p", { class: "muted" }, "not run"));
  $("#ladder").append(heatmap(runs, LADDER, (r, [set]) => {
    const s = summaryOf(r, "rule_v1/" + set)?.all;
    return s ? { value: s.TA, run: r, tip: `${r.id} · ${set}: TA ${fmt(s.TA)} · Rev ${fmt(s.Rev)} · Hold ${fmt(s.Hold)}` } : null;
  }, { rowLabel: (r) => shortName(r.id), colLabel: ([, label]) => label, onClick: openRun }));
}

function renderKinds() {
  const runs = reportableRuns().filter((r) => summaryOf(r, L2)?.kinds);
  if (!runs.length) return $("#kinds").append(el("p", { class: "muted" }, "not run"));
  const kinds = [...new Set(runs.flatMap((r) => Object.keys(summaryOf(r, L2).kinds)))].sort();
  $("#kinds").append(heatmap(runs, kinds, (r, k) => {
    const v = summaryOf(r, L2).kinds[k];
    return typeof v === "number" ? { value: v, run: r, tip: `${r.id} · ${k}: TA ${fmt(v)}` } : null;
  }, { rowLabel: (r) => shortName(r.id), onClick: openRun }));
}
