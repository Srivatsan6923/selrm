"""One-off (2 Oct evening): regenerate B's queue files under the revised plan. Runs already claimed, running,
done or failed on the PVC keep the spec they were queued with (the plan: claimed runs keep their scope)."""
import json, os, subprocess, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "scripts")
import make_queue_b as Q

REG, V = "scratch/registry_rule_v1.json", "rule_v1"
out = subprocess.run(["kubectl", "-n", "ecepxie", "exec", "selrm-b-sync", "--", "sh", "-c",
                      "cd /pvc/selrm/results && for d in */; do ls $d | grep -qE '^(CLAIMED_|DONE|FAILED_|KILLED_)' "
                      "&& echo ${d%/}; done"], capture_output=True, text=True, check=True).stdout.split()
busy = set(out)
print(len(busy), "busy run dirs on the PVC")
adapters = subprocess.run(["kubectl", "-n", "ecepxie", "exec", "selrm-b-sync", "--", "sh", "-c", "ls /pvc/selrm/adapters"],
                          capture_output=True, text=True, check=True).stdout.split()
print(len(adapters), "adapters on the PVC")
VALIDATED = [0, 1, 2, 3, 4]      # B3.2: criterion on the seed mean, every seed tested (DECISIONS_B 10 Oct)
L3INV = ["B-TR-fover-s0", "B-F-ledger2-natural-s0", "B-F-ledger2-balanced-s0", "B-TR-clinonly-s0", "B-TR-tripclin-s0"]
FILES = {  # queue file -> generator (FINAL_TASKS_B, 3 Oct)
    "b_f_s0.json": lambda: Q.factorial({0}, REG, V),
    "b_f_key_s12.json": lambda: Q.factorial({1, 2}, REG, V, key_only=True),
    "b_f_s12.json": lambda: [r for r in Q.factorial({1, 2}, REG, V) if (r["format"], r["corpus"].split("_")[-1])
                             not in Q.CORE_CELLS],
    "b_f_s34.json": lambda: Q.factorial({3, 4}, REG, V, key_only=True),
    "b_tr_s0.json": lambda: [r for r in Q.transfer({0}, REG, V) if r["format"] != "genprm"],
    "v2/b_genprm_s0.json": lambda: [r for r in Q.transfer({0}, REG, V) if r["format"] == "genprm"],
    "b_tr_s1p.json": lambda: [r for r in Q.transfer({1, 2, 3, 4}, REG, V) if r["format"] != "genprm"],
    "v2/b_genprm_s12.json": lambda: [r for r in Q.transfer({1, 2, 3, 4}, REG, V) if r["format"] == "genprm"],
    "b_x_s0.json": lambda: [r for r in Q.extras({0}, REG, V) if r.get("min_gen", 0) < 2],
    "v2/b_x2_s0.json": lambda: [r for r in Q.extras({0}, REG, V) if r.get("min_gen", 0) >= 2],
    "b_x_s12.json": lambda: Q.extras({1, 2}, REG, V),
    "v2/b_bb_s0.json": lambda: Q.backbones({0}, REG, V),
    "v2/b_bb_s12.json": lambda: Q.backbones({1, 2}, REG, V),
    "v2/b_probe_rw_s0.json": lambda: Q.probe_rw(V),
    "b_new_s0.json": lambda: Q.newexp({0}, REG, V),
    "b_cv.json": lambda: Q.case_visible(REG, V),           # NEXT_TASKS_B 2 (the B-SC s0 run of b_sc_s0.json is done)
    "b_new_s12.json": lambda: Q.newexp({1, 2}, REG, V),    # NEXT_TASKS_B 4: LOKO seeds 1-2
    "b_rw.json": lambda: Q.rewritten(REG, V),              # NEXT_TASKS_B 5, once A freezes train_triplets_rw
    "b_aux.json": lambda: Q.aux(REG),                       # NEXT_TASKS_B 3 (docs/AUX_PROTOCOL.md S1)
    "v2/b_ns.json": lambda: Q.ns_eval(REG, adapters),      # P0.6: kept adapters on A's new sets
    "v2/b_v2.json": lambda: Q.stage2(REG),                 # stage 2 B2
    "v2/b_s2g.json": lambda: Q.composite(adapters),          # stage 2 B3: development sets (validation)
    "v2/b_s2g_test.json": lambda: Q.composite(adapters, tests=True, seeds=VALIDATED),   # only seeds that passed assemble_rmg.py --validate
    "v2/b_mix.json": lambda: Q.adaptation(REG),            # stage 2 B4, once mcv_v1 is in the PVC registry
    "v2/b_l3inv.json": lambda: Q.ns_eval(REG, [a for a in L3INV if a in adapters],      # stage 2 B0: red cells of Table 20
                                         fams={"L3inv": ["rule_v1/test_L3inv"]}),
}
for name, gen in FILES.items():
    path = f"configs/queues/{name}"
    old = {r["run_id"]: r for r in json.load(open(path))["runs"]} if os.path.exists(path) else {}
    runs, kept = [], []
    for r in Q.gate_new_fields(Q.with_new_sets(gen(), REG)):
        if r["run_id"] in busy and r["run_id"] in old:
            runs.append(old[r["run_id"]]); kept.append(r["run_id"])
        else:
            runs.append(r)
    gone = sorted(set(old) - {r["run_id"] for r in runs} - busy)
    json.dump({"runs": runs}, open(path, "w", newline="\n"), indent=1)
    print(f"{name}: {len(runs)} runs ({len(kept)} busy kept as queued){'; not regenerated: ' + str(gone) if gone else ''}")
