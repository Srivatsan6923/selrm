"""One-off (3 Oct evening, NEXT_TASKS_B): new rows (case-visible judges, LOKO seeds 1-2 and the decision-bit reader,
rewritten notes) and the cuts (diversity curves, dose curve, seeds 1-2 of non-core cells, extra ablation seeds,
change loss). Runs already claimed or finished on the PVC are never cut."""
import csv, io, os, re, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
busy = set(subprocess.run(["kubectl", "-n", "ecepxie", "exec", "selrm-b-sync", "--", "sh", "-c",
                           "cd /pvc/selrm/results && for d in */; do ls $d | grep -qE '^(CLAIMED_|DONE|FAILED_|KILLED_)' "
                           "&& echo ${d%/}; done"], capture_output=True, text=True, check=True).stdout.split())
p = "docs/RUN_MATRIX_B.csv"
rows = list(csv.DictReader(open(p, encoding="utf-8")))
fields = list(rows[0].keys())
byid = {r["run_id"]: r for r in rows}
tmpl = byid["B-F-ledger2-triplets-s0"]
CORE = {(f, c) for f in ("verdict", "summary2", "ledger2") for c in ("blocks", "triplets")}
note = lambda r, t: r.__setitem__("notes", (r["notes"] + "; " if r["notes"] else "") + t)

new = []
def add(rid, paper, what, data, seed, notes):
    if rid not in byid:
        new.append({**tmpl, "run_id": rid, "paper_item": paper, "kind": "train+eval", "what": what, "data": data,
                    "seed": str(seed), "runtime": "GPU", "est_hours": "", "measured_hours": "", "priority": "P0",
                    "depends_on": "B-C0", "status": "queued", "notes": notes})

for corpus, seeds in (("triplets", (0, 1, 2)), ("blocks", (0,))):
    for sd in seeds:
        add(f"B-LC-ledger2-{corpus}-s{sd}", "Tab3,S3", "ledger pipeline whose judge also sees the case (rule, case, ledger, claim)",
            f"rule_v1/train_{corpus}", sd, "NEXT_TASKS_B 2; format ledger2_case; registered for C")
for corpus, seeds in (("blocks", (0,)), ("triplets", (1, 2))):
    for sd in seeds:
        add(f"B-SC-summary2-{corpus}-s{sd}", "Tab3,S3", "summary pipeline whose judge also sees the case (rule, case, prose, claim)",
            f"rule_v1/train_{corpus}", sd, "NEXT_TASKS_B 2; format summary2_case; registered for C")
for kind in ("subject", "time", "boundary"):
    for fmt in ("verdict", "summary2"):
        for sd in (1, 2):
            add(f"B-LOKO-{kind}-{fmt}-s{sd}", "Tab9,P0.5", f"{fmt} on triplets without {kind} near-misses (seed {sd})",
                f"rule_v1/train_triplets_no_{kind}", sd, "NEXT_TASKS_B 4; eval dev, test_L2, test_L0 (+ new sets)")
    add(f"B-LOKO-{kind}-bit_reader-s0", "Tab9,P0.5", f"decision-bit reader on triplets without {kind} near-misses",
        f"rule_v1/train_triplets_no_{kind}", 0, "NEXT_TASKS_B 4; format bit_reader")
for fmt in ("verdict", "summary2"):
    add(f"B-RW-{fmt}-triplets-s0", "Tab3,rewrite", f"{fmt} trained on triplets with 25% rewritten notes",
        "rule_v1x/train_triplets_rw (A)", 0, "NEXT_TASKS_B 5; queued once A freezes the corpus; seeds 1-2 for the better one")
rows += new

cut = []
for r in rows:
    rid, st = r["run_id"], r["status"]
    if st in ("done", "dropped", "deferred") or rid in busy:
        continue
    m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", rid)
    reason = None
    if rid.startswith("B-DIV-"):
        reason = "diversity curves"
    elif rid.startswith("B-DOSE-"):
        reason = "dose curve"
    elif m and (m[1], m[2]) not in CORE and m[3] != "0":
        reason = "seeds 1-2 of non-core cells"
    elif re.fullmatch(r"B-AB-.+-s[1-9]", rid) or rid == "B-AB-concl-only-s0" or "change" in rid.lower():
        reason = "extra ablation seeds / not in the list"
    elif re.fullmatch(r"B-(BB|TR|FOLD\d)-.+-s[1-9]", rid):
        reason = "one seed each for the remaining v10 rows"
    if reason:
        r["status"] = "dropped"
        note(r, f"cut by NEXT_TASKS_B (3 Oct): {reason}")
        cut.append(rid)
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader()
w.writerows(rows)
open(p, "w", encoding="utf-8", newline="").write(buf.getvalue())
print(len(new), "rows added;", len(cut), "cut:", ", ".join(cut[:8]), "...")
