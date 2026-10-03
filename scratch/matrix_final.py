"""One-off (3 Oct, FINAL_TASKS_B): run-matrix changes for the final role-B plan."""
import csv, io, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = "docs/RUN_MATRIX_B.csv"
rows = list(csv.DictReader(open(p, encoding="utf-8")))
fields = list(rows[0].keys())
byid = {r["run_id"]: r for r in rows}
tmpl = byid["B-F-ledger2-triplets-s0"]
note = lambda r, t: r.__setitem__("notes", (r["notes"] + "; " if r["notes"] else "") + t)
changed = []

# LOKO: {verdict, summary2, ledger2} x {subject, time, boundary} on A's train_triplets_no_<kind>
for r in rows:
    if r["run_id"].startswith("B-LOKO-") and "-negation-" in r["run_id"]:
        r["status"] = "dropped"
        note(r, "replaced 3 Oct by the boundary kind (FINAL_TASKS_B P0.5)")
        changed.append(r["run_id"])
new = []
for kind in ("subject", "time", "boundary"):
    for fmt in ("verdict", "summary2", "ledger2"):
        rid = f"B-LOKO-{kind}-{fmt}-s0"
        if rid in byid:
            r = byid[rid]
            r.update({"data": f"rule_v1/train_triplets_no_{kind} (A, FINAL_TASKS_A P0.4)", "priority": "P0", "status": "todo",
                      "depends_on": "A (train_triplets_no_*)",
                      "notes": "eval dev, test_L2, test_L0; scored on the held-out kind; Table 9 '- other-person / past / "
                               "threshold near-misses' rows (ledger2)"})
        else:
            new.append({**tmpl, "run_id": rid, "paper_item": "Tab9, P0.5", "kind": "train+eval",
                        "what": f"{fmt} on triplets without {kind} near-misses; TA on the held-out kind vs B-F-{fmt}-triplets-s0",
                        "data": f"rule_v1/train_triplets_no_{kind} (A, FINAL_TASKS_A P0.4)", "seed": "0", "est_hours": "",
                        "measured_hours": "", "priority": "P0", "depends_on": "A (train_triplets_no_*)", "status": "todo",
                        "notes": "eval dev, test_L2, test_L0; scored on the held-out kind"})
for rid, what, data, pr, dep, kind_, nt in (
        ("B-SC-summary2-triplets-s0", "summary pipeline whose judge also sees the case (rule, case, prose, claim)",
         "rule_v1/triplets", "P0", "B-C0", "train+eval", "format summary2_case (B-defined judge prompt); Tab3 + Tab9 row"),
        ("B-AB-conddrv-s0", "condition derived by the reader (reader gets rule and claim, finds the condition)",
         "rule_v1/triplets (variant)", "P1", "B-C0", "train+eval", "needs a new reader format (to do)"),
        ("B-AE-program-ledger", "rule program applied to the predicted ledger of B-F-ledger2-triplets-s0",
         "rule_v1 test", "P0", "B-F-ledger2-triplets-s0", "eval", "CPU: A's rule program on parsed reader ledgers; "
         "Tab9 'program on predicted ledger'")):
    if rid not in byid:
        new.append({**tmpl, "run_id": rid, "paper_item": "Tab3,Tab9" if rid.startswith("B-SC") else "Tab9,Sec7.4",
                    "kind": kind_, "what": what, "data": data, "seed": "0" if rid.endswith("s0") else "-",
                    "runtime": "CPU" if rid == "B-AE-program-ledger" else "GPU", "est_hours": "", "measured_hours": "",
                    "priority": pr, "depends_on": dep, "status": "todo", "notes": nt})
rows += new
changed += [r["run_id"] for r in new]
# core cells now include summary2 x {blocks, triplets}: seeds 3-4 back in (P1)
for c in ("blocks", "triplets"):
    for sd in ("3", "4"):
        r = byid.get(f"B-F-summary2-{c}-s{sd}")
        if r and r["status"] == "dropped":
            r["status"] = "todo"
            note(r, "restored 3 Oct: summary2 x blocks/triplets is a core cell in FINAL_TASKS_B (seeds 3-4, P1)")
            changed.append(r["run_id"])
# one second backbone (FINAL_TASKS_B P1): granite-4.1-8b on the four verdict/ledger cells; Qwen3.5-4B deferred
for r in rows:
    if r["run_id"].startswith("B-BB-qwen3.5-4b") and r["status"] not in ("done",):
        r["status"] = "deferred"
        note(r, "deferred 3 Oct: FINAL_TASKS_B asks for one second backbone; granite-4.1-8b (non-Qwen) chosen")
        changed.append(r["run_id"])
# runs FINAL_TASKS_B does not list: seeds 1-2 of non-core cells, the dose curve -> after everything
core = {(f, c) for f in ("verdict", "summary2", "ledger2") for c in ("blocks", "triplets")}
for r in rows:
    parts = r["run_id"].split("-")
    if r["run_id"].startswith("B-F-") and r["seed"] in ("1", "2") and (parts[2], parts[3]) not in core \
            and r["status"] in ("queued", "todo"):
        r["status"] = "todo"
        note(r, "not in FINAL_TASKS_B (non-core cells are seed 0 only): after everything")
        changed.append(r["run_id"])
    if r["run_id"].startswith("B-DOSE-") and r["status"] in ("queued", "todo"):
        r["status"] = "todo"
        note(r, "not in FINAL_TASKS_B / v13: after everything")
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader()
w.writerows(rows)
open(p, "w", encoding="utf-8", newline="").write(buf.getvalue())
print(len(rows), "rows;", len(changed), "changed or added:", ", ".join(changed[:12]), "...")
