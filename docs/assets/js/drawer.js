/* Side drawer with the full record of one run. Used by the Runs and Results pages. */

function openRun(run) {
  const drawer = $("#drawer");
  const bg = $("#drawer-bg");
  drawer.innerHTML = "";

  const facts = [
    ["Owner", `${run.owner} · ${ROLE_NAMES[run.owner] || ""}`],
    ["Paper item", run.item],
    ["Kind", run.kind],
    ["Data", run.data],
    ["Seed", run.seed !== "" ? run.seed : null],
    ["Priority", run.priority],
    ["Depends on", run.depends && run.depends !== "-" ? run.depends : null],
    ["Runtime", run.runtime],
    ["Estimate", run.est_hours ? run.est_hours + " h" : null],
    ["Model", run.model],
    ["Format", run.format],
    ["Corpus", run.corpus],
    ["GPU", run.gpu],
    ["GPU-hours", run.gpu_hours != null ? fmt(+run.gpu_hours, 2) : null],
    ["Wall time", run.wall_seconds ? fmt(run.wall_seconds / 3600, 2) + " h" : null],
    ["Claimed", run.claims.map((c) => `${c.role}${c.note ? ": " + c.note : ""}`).join("; ") || null],
    ["Location", run.dirs.join(", ") || null],
    ["Notes", run.notes],
  ].filter(([, v]) => v != null && v !== "");

  drawer.append(
    el("button", { class: "theme-btn close", onclick: closeRun, title: "Close" }, "✕"),
    el("div", { class: "eyebrow" }, "Run"),
    el("h2", { class: "mono" }, run.id),
    el("div", { style: { margin: "10px 0" } }, statePill(run.state),
      run.smoke ? el("span", { class: "tag-smoke" }, "smoke / validation") : null,
      run.provisional ? el("span", { class: "tag-smoke" }, "provisional") : null),
    run.what ? el("p", { class: "muted" }, run.what) : null,
    el("dl", { class: "kv" }, facts.map(([k, v]) => [el("dt", {}, k), el("dd", {}, String(v))])));

  // Per-set metrics (TA with Rev / Hold underneath).
  const sets = Object.entries(run.summaries || {}).filter(([, s]) => s.all);
  if (sets.length) {
    drawer.append(el("h3", { style: { margin: "22px 0 8px" } }, "Triplet accuracy by set"));
    for (const [name, s] of sets) {
      drawer.append(el("div", { class: "metric-row", title: `Rev ${fmt(s.all.Rev)} · Hold ${fmt(s.all.Hold)} · n ${s.all.n}` },
        el("span", { class: "mono small" }, name.split("/").pop()),
        el("div", { class: "track" }, el("div", { class: "fill", "data-width": (s.all.TA || 0) + "%" })),
        el("span", { class: "num" }, fmt(s.all.TA))));
    }
    const l2 = summaryOf(run, "rule_v1/test_L2");
    if (l2 && l2.kinds) {
      drawer.append(el("h3", { style: { margin: "22px 0 8px" } }, "test_L2 by near-miss kind"));
      for (const [k, v] of Object.entries(l2.kinds)) {
        drawer.append(el("div", { class: "metric-row" }, el("span", { class: "small" }, k),
          el("div", { class: "track" }, el("div", { class: "fill", "data-width": (v || 0) + "%" })),
          el("span", { class: "num" }, fmt(v))));
      }
    }
    drawer.append(el("p", { class: "muted small" }, "Seed-level numbers read from summary_*.json. Not paper tables."));
  }

  bg.classList.add("open");
  drawer.classList.add("open");
  requestAnimationFrame(() => $$("[data-width]", drawer).forEach((n) => (n.style.width = n.dataset.width)));
}

function closeRun() {
  $("#drawer").classList.remove("open");
  $("#drawer-bg").classList.remove("open");
}

document.addEventListener("keydown", (e) => e.key === "Escape" && closeRun());
document.addEventListener("click", (e) => e.target.id === "drawer-bg" && closeRun());
