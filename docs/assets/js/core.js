/* ==========================================================================
   SelRM status site — shared helpers
   Every page loads data.js (window.SELRM) and then this file.
   ========================================================================== */

const DATA = window.SELRM || { runs: [], registry: [], tasks: [], roles: [], milestones: [] };

const PAGES = [
  { href: "index.html", label: "Overview" },
  { href: "runs.html", label: "Runs" },
  { href: "results.html", label: "Results" },
  { href: "system.html", label: "System" },
  { href: "team.html", label: "Team" },
];

/* Run states in display order, with their CSS colour variable. */
const STATES = [
  { key: "done", label: "Done", color: "var(--done)" },
  { key: "running", label: "Running", color: "var(--running)" },
  { key: "claimed", label: "Claimed", color: "var(--claimed)" },
  { key: "queued", label: "Queued", color: "var(--claimed)" },
  { key: "in progress", label: "In progress", color: "var(--claimed)" },
  { key: "todo", label: "To do", color: "var(--todo)" },
  { key: "untracked", label: "Extra", color: "var(--other)" },
  { key: "dropped", label: "Dropped", color: "var(--dropped)" },
];

const ROLE_NAMES = { A: "Data & rules", B: "Training", C: "Evaluation", D: "Downstream & lead" };

/* ---------- Tiny DOM helpers ---------- */

/** Create an element: el("div", {class: "card"}, child1, "text"). */
function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v == null || v === false) continue;
    if (k === "class") node.className = v;
    else if (k === "html") node.innerHTML = v;
    else if (k === "style" && typeof v === "object") Object.assign(node.style, v);
    else if (k.startsWith("on")) node.addEventListener(k.slice(2), v);
    else node.setAttribute(k, v);
  }
  for (const c of children.flat()) {
    if (c == null || c === false) continue;
    node.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return node;
}

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

/** CSS class for a state string ("in progress" -> "s-in-progress"). */
const stateClass = (s) => "s-" + String(s || "other").toLowerCase().replace(/\s+/g, "-");

function statePill(state) {
  const meta = STATES.find((s) => s.key === state);
  return el("span", { class: "pill " + stateClass(state) }, meta ? meta.label : state);
}

const fmt = (v, digits = 1) => (typeof v === "number" ? v.toFixed(digits) : "–");

function countBy(items, keyFn) {
  const out = {};
  for (const it of items) {
    const k = keyFn(it);
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

/* ---------- Data helpers ---------- */

/** Runs whose numbers may be charted: done, with summaries, not smoke/timing. */
function reportableRuns() {
  return DATA.runs.filter((r) => r.state === "done" && !r.smoke && Object.keys(r.summaries || {}).length);
}

/** Headline summary for a set, e.g. summaryOf(run, "rule_v1/test_L2"). */
const summaryOf = (run, set) => (run.summaries || {})[set];

/* ---------- Layout: nav + footer ---------- */

function renderChrome() {
  const here = location.pathname.split("/").pop() || "index.html";
  const nav = el("nav", { class: "nav" },
    el("div", { class: "wrap" },
      el("a", { class: "brand", href: "index.html" }, el("i", { class: "brand-dot" }), el("span", {}, "SelRM")),
      el("div", { class: "nav-links" },
        PAGES.map((p) => el("a", { href: p.href, class: p.href === here ? "active" : null }, p.label))),
      el("button", { class: "theme-btn", title: "Toggle theme", onclick: toggleTheme }, "◐")));
  document.body.prepend(nav);

  const gen = DATA.generated ? new Date(DATA.generated) : null;
  document.body.append(el("footer", {},
    el("div", { class: "wrap" },
      "Generated ", gen ? gen.toLocaleString() : "–", " from commit ",
      el("code", {}, DATA.commit || "–"), " · rebuild with ",
      el("code", {}, "python scripts/build_site.py"))));
}

/* ---------- Theme ---------- */

function applyStoredTheme() {
  try {
    const t = localStorage.getItem("selrm-theme");
    if (t) document.documentElement.dataset.theme = t;
  } catch (e) { /* storage blocked: follow the OS */ }
}

function toggleTheme() {
  const root = document.documentElement;
  const dark = root.dataset.theme
    ? root.dataset.theme === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches;
  root.dataset.theme = dark ? "light" : "dark";
  try { localStorage.setItem("selrm-theme", root.dataset.theme); } catch (e) { /* ignore */ }
}

/* ---------- Animations ---------- */

/** Fade elements with .reveal in as they scroll into view. */
function observeReveals(root = document) {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      e.target.classList.add("in");
      e.target.querySelectorAll("[data-count]").forEach(countUp);
      e.target.querySelectorAll("[data-width]").forEach((n) => (n.style.width = n.dataset.width));
      io.unobserve(e.target);
    }
  // threshold 0: tall elements (the run table) must reveal as soon as their top shows.
  }, { threshold: 0, rootMargin: "0px 0px -6% 0px" });
  $$(".reveal", root).forEach((n, i) => {
    n.style.transitionDelay = Math.min(i % 6, 5) * 60 + "ms";
    io.observe(n);
  });
}

/** Animate a number from 0 to data-count. */
function countUp(node) {
  const target = parseFloat(node.dataset.count);
  const digits = parseInt(node.dataset.digits || "0", 10);
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
    node.textContent = target.toLocaleString(undefined, { minimumFractionDigits: digits, maximumFractionDigits: digits });
    return;
  }
  const start = performance.now();
  const dur = 1100;
  const step = (now) => {
    const t = Math.min(1, (now - start) / dur);
    const eased = 1 - Math.pow(1 - t, 3);
    node.textContent = (target * eased).toLocaleString(undefined, {
      minimumFractionDigits: digits, maximumFractionDigits: digits });
    if (t < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

/** Fade out before following an internal link. */
function smoothLinks() {
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a");
    if (!a || a.target || e.metaKey || e.ctrlKey) return;
    const href = a.getAttribute("href") || "";
    if (!href.endsWith(".html")) return;
    e.preventDefault();
    document.body.classList.add("leaving");
    setTimeout(() => (location.href = href), 160);
  });
}

/* ---------- Shared widgets ---------- */

/** Stacked bar of run states + legend. */
function stateStack(runs, { legend = true } = {}) {
  const counts = countBy(runs, (r) => r.state);
  const total = runs.length || 1;
  const bar = el("div", { class: "stack" },
    STATES.filter((s) => counts[s.key]).map((s) =>
      el("span", { style: { background: s.color }, "data-width": (100 * counts[s.key]) / total + "%",
        title: `${s.label}: ${counts[s.key]}` })));
  if (!legend) return bar;
  const leg = el("div", { class: "legend" },
    STATES.filter((s) => counts[s.key]).map((s) =>
      el("span", {}, el("i", { style: { background: s.color } }), `${s.label} ${counts[s.key]}`)));
  return el("div", {}, bar, leg);
}

/** One shared tooltip for charts. */
const tooltip = (() => {
  let node;
  return {
    show(text, e) {
      if (!node) document.body.append((node = el("div", { class: "tooltip" })));
      node.textContent = text;
      node.style.opacity = 1;
      node.style.left = Math.min(e.clientX + 14, innerWidth - 290) + "px";
      node.style.top = e.clientY + 14 + "px";
    },
    hide() { if (node) node.style.opacity = 0; },
  };
})();

/** Colour for a 0–100 score: light surface at 0 to the accent at 100. */
function heatColor(v) {
  if (typeof v !== "number") return "var(--surface-2)";
  return `color-mix(in srgb, var(--accent) ${Math.round(v)}%, var(--surface-2))`;
}

/* ---------- Boot ---------- */

applyStoredTheme();
document.addEventListener("DOMContentLoaded", () => {
  renderChrome();
  smoothLinks();
  if (typeof window.renderPage === "function") window.renderPage();
  observeReveals();
});
