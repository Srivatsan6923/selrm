/* Overview page: headline numbers, triplet explainer, progress, timeline. */

window.renderPage = function () {
  renderCountdown();
  renderStats();
  renderTriplet();
  renderProgress();
  renderTimeline();
};

function renderCountdown() {
  const deadline = DATA.milestones.find((m) => m.title === "ARR deadline");
  if (!deadline) return;
  const days = Math.ceil((new Date(deadline.at) - Date.now()) / 864e5);
  $("#countdown").append(
    el("span", { class: "pill plain" }, el("i", { class: "live-dot" }), days > 0 ? `${days} days to deadline` : "Deadline passed"),
    el("span", { class: "pill plain" }, "Backbone ", el("code", {}, "Qwen3.5-9B")),
    el("span", { class: "pill plain" }, "4 roles · 4 GPUs"));
}

function renderStats() {
  const runs = DATA.runs;
  const done = runs.filter((r) => r.state === "done").length;
  const gpuHours = runs.reduce((s, r) => s + (parseFloat(r.gpu_hours) || 0), 0);
  const frozen = DATA.registry.filter((s) => s.frozen).length;
  const stats = [
    { value: DATA.library.rules_total || 0, label: "executable rules" },
    { value: frozen, label: "frozen datasets" },
    { value: done, label: `runs done of ${runs.length}` },
    { value: gpuHours, label: "GPU-hours logged", digits: 1 },
  ];
  $("#stats").append(...stats.map((s) =>
    el("div", { class: "card stat reveal" },
      el("div", { class: "value", "data-count": s.value, "data-digits": s.digits || 0 }, "0"),
      el("div", { class: "label" }, s.label))));
}

/* Three cases cycle; the score needle shows which claim the reward should prefer. */
function renderTriplet() {
  const cases = [
    { tag: "Base", text: "No allergy recorded.", want: "+", note: "prefer s" },
    { tag: "Flip", text: "Patient has a penicillin allergy.", want: "−", note: "reverse → prefer s′" },
    { tag: "Near-miss", text: "Patient's mother has a penicillin allergy.", want: "+", note: "hold → prefer s" },
  ];
  const root = $("#triplet");
  root.append(
    el("div", { class: "rule-line" },
      el("span", { class: "pill plain" }, "Rule"),
      " Penicillin allergy in the patient → avoid amoxicillin."),
    el("div", { class: "claims" },
      el("span", {}, el("b", {}, "s"), " Prescribe amoxicillin."),
      el("span", {}, el("b", {}, "s′"), " Prescribe azithromycin.")),
    el("div", { class: "cases" }, cases.map((c, i) =>
      el("div", { class: "case", "data-i": i },
        el("div", { class: "case-tag" }, c.tag),
        el("div", { class: "case-text" }, c.text),
        el("div", { class: "needle" }, el("span", { class: "needle-dot" + (c.want === "+" ? " pos" : " neg") })),
        el("div", { class: "case-note" }, el("b", {}, c.want === "+" ? "d > 0" : "d < 0"), " ", c.note)))),
    el("p", { class: "muted small center" },
      "Solved only if all three are right. Labels come from executing the rule — never from an LLM."));

  // Highlight one case at a time, looping.
  let i = 0;
  const step = () => {
    $$(".case", root).forEach((n, j) => n.classList.toggle("active", j === i));
    i = (i + 1) % cases.length;
  };
  step();
  setInterval(step, 2200);
}

function renderProgress() {
  const root = $("#progress");
  root.append(el("div", { class: "progress-all" }, stateStack(DATA.runs)));
  root.append(el("div", { class: "owner-rows" }, "ABCD".split("").map((o) => {
    const mine = DATA.runs.filter((r) => r.owner === o);
    const done = mine.filter((r) => r.state === "done").length;
    return el("a", { class: "owner-row", href: `runs.html#owner=${o}` },
      el("div", {}, el("b", {}, o), " ", el("span", { class: "muted" }, ROLE_NAMES[o])),
      stateStack(mine, { legend: false }),
      el("div", { class: "num small muted" }, `${done}/${mine.length}`));
  })));
}

function renderTimeline() {
  const ms = DATA.milestones.map((m) => ({ ...m, t: new Date(m.at).getTime() }));
  const t0 = ms[0].t, t1 = ms[ms.length - 1].t;
  const pos = (t) => Math.max(0, Math.min(100, (100 * (t - t0)) / (t1 - t0)));
  const now = Date.now();
  $("#today").textContent = "Today: " + new Date().toDateString();

  const line = el("div", { class: "tl" },
    el("div", { class: "tl-track" }, el("div", { class: "tl-fill", "data-width": pos(now) + "%" })),
    el("div", { class: "tl-now", style: { left: pos(now) + "%" } }, "now"),
    ms.map((m, i) => el("div", {
      class: "tl-point" + (m.t < now ? " past" : "") + (i % 2 ? " below" : ""),
      style: { left: pos(m.t) + "%" },
    },
      el("i", {}),
      el("div", { class: "tl-label" },
        el("b", {}, m.title),
        el("span", {}, new Date(m.at).toLocaleDateString(undefined, { weekday: "short", day: "numeric", month: "short", timeZone: "UTC" }))))));
  // Narrow screens get a vertical list instead (CSS picks one).
  const list = el("ol", { class: "tl-list" }, ms.map((m) =>
    el("li", { class: m.t < now ? "past" : "" },
      el("b", {}, m.title), " ",
      el("span", { class: "muted small" }, new Date(m.at).toLocaleDateString(undefined, { day: "numeric", month: "short", timeZone: "UTC" }), " · ", m.note))));
  $("#timeline").append(line, list);
}
