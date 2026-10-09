/* Team page: role cards, task kanban, handoff feed, integrity checks, commits. */

/* Status board wording -> kanban column. */
const COLUMNS = [
  { title: "Not started", kinds: ["not started", "other"] },
  { title: "In progress", kinds: ["running", "partly", "queued", "open"] },
  { title: "Waiting / blocked", kinds: ["blocked", "waiting"] },
  { title: "Done", kinds: ["done", "dropped"] },
];

window.renderPage = function () {
  renderRoles();
  renderKanban();
  renderHandoffs();
  renderChecks();
  renderCommits();
};

function renderRoles() {
  $("#roles").append(...DATA.roles.map((r) => {
    const runs = DATA.runs.filter((x) => x.owner === r.id);
    const status = r.paused ? ["paused", "s-claimed"] : r.updated ? ["active", "s-done"] : ["no state yet", "s-todo"];
    const list = (title, items, cls) => items.length
      ? [el("h4", {}, title), el("ul", { class: cls }, items.slice(0, 4).map((t) => el("li", {}, t)))]
      : [];
    return el("div", { class: "card role-card reveal" },
      el("header", {},
        el("div", { class: "role-id" }, r.id),
        el("div", {}, el("h3", {}, r.name), el("div", { class: "muted small" }, r.updated || "–")),
        el("span", { class: "pill " + status[1], style: { marginLeft: "auto" } }, status[0])),
      stateStack(runs),
      list("Blockers", r.blockers, "s-dropped"),
      list("Asking for", r.requests),
      list("Next", r.next),
      r.decisions.length ? [el("h4", {}, `Latest decisions · ${r.n_decisions} logged`),
        el("ul", {}, r.decisions.slice(0, 2).map((d) => el("li", {}, d.text)))] : []);
  }));
}

function renderKanban() {
  $("#kanban").append(...COLUMNS.map((col) => {
    const tasks = DATA.tasks.filter((t) => col.kinds.includes(t.kind));
    return el("div", { class: "col" },
      el("h3", {}, col.title, el("span", { class: "muted" }, tasks.length)),
      tasks.map((t) => el("div", { class: "ticket", title: t.output ? "Output: " + t.output : "" },
        el("div", { class: "tid" }, `${t.id} · ${t.owner}`),
        el("div", {}, t.task.length > 90 ? t.task.slice(0, 90) + "…" : t.task),
        el("div", { class: "tstatus" }, t.status.length > 80 ? t.status.slice(0, 80) + "…" : t.status))));
  }));
}

function renderHandoffs() {
  $("#handoffs").append(...DATA.handoffs.map((h) => el("li", {},
    el("div", {}, el("div", { class: "arrow" }, `${h.from} → ${h.to}`), el("div", { class: "muted small" }, h.date)),
    el("div", { class: "small" }, h.what.length > 180 ? h.what.slice(0, 180) + "…" : h.what))));
}

function renderChecks() {
  $("#checks").append(...DATA.checks.map((c) => {
    const ok = /^pass/i.test(c.result);
    return el("li", {},
      el("div", {}, el("span", { class: "pill " + (ok ? "s-done" : "s-claimed") }, ok ? "pass" : "see note"), " ", c.check),
      el("div", { class: "muted small" }, c.result));
  }));
}

function renderCommits() {
  $("#commits").append(...(DATA.commits || []).map((c) => el("li", {},
    el("code", { class: "muted" }, c.hash), " ", c.msg,
    el("div", { class: "muted small" }, `${c.author} · ${c.date}`))));
}
