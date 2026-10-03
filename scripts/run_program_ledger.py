"""B-AE-program-ledger: rule program on the predicted ledgers of an adapter's evaluation (CPU; Table 9).
Writes results_git/<out>/{scores_<set>.jsonl, summary_<set>.json, meta.json, DONE} from the source run's reader
outputs, using role A's frozen rule program (scripts/program_ledger.py in a separate process).
  python scripts/run_program_ledger.py [--src B-F-ledger2-triplets-s0] [--out B-AE-program-ledger]"""
import argparse, datetime, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from report_b import DATA, RG, records
from selrm.metrics import bootstrap_ci, decisions, summarise

A_CODE = os.environ.get("SELRM_A_CODE", f"{ROOT}/scratch/role_a_frozen")   # role A's freeze e40789bd5d7a (same code)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="B-F-ledger2-triplets-s0")
    ap.add_argument("--out", default="B-AE-program-ledger")
    ap.add_argument("--sets", default="rule_v1/dev,rule_v1/test_L2,rule_v1/dev_missing,rule_v1/missing")
    a = ap.parse_args()
    out = f"{RG}/{a.out}"
    os.makedirs(out, exist_ok=True)
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    stats_all = {}
    for s in a.sets.split(","):
        name = s.replace("/", "~")
        src = f"{RG}/{a.src}/scores_{name}.jsonl"
        if not os.path.exists(src):
            continue
        stats_path = f"{out}/stats_{name}.json"
        subprocess.run([sys.executable, f"{ROOT}/scripts/program_ledger.py", f"{DATA}/{reg[s]['path']}", src,
                        f"{out}/scores_{name}.jsonl", stats_path], env={**os.environ, "PYTHONPATH": A_CODE}, check=True)
        stats_all[s] = json.load(open(stats_path))
        os.remove(stats_path)
        R = records(s)
        S = {r["iid"]: r["u"] for r in map(json.loads, open(f"{out}/scores_{name}.jsonl", encoding="utf-8"))}
        R = [r for r in R if r["iid"] in S]
        T = decisions(R, [S[r["iid"]] for r in R])
        summ = {"run_id": a.out, "set": s, "claim_type": "conclusion", **summarise(T)}
        if summ.get("all"):
            summ["CI95"] = {m: list(bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
        summ["eval"] = {"mode": "program_on_predicted_ledger", "source_run": a.src, **stats_all[s]}
        json.dump(summ, open(f"{out}/summary_{name}.json", "w", newline="\n"), indent=1)
    commit = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    tot = {k: sum(v.get(k, 0) for v in stats_all.values()) for k in ("matched", "unmatched", "no_answer", "malformed", "records")}
    json.dump({"run_id": a.out, "kind": "eval (CPU)", "source_run": a.src, "program": "role A rule_v1 freeze e40789bd5d7a",
               "eval_sets": list(stats_all), "git_commit": commit, **tot, "per_set": stats_all},
              open(f"{out}/meta.json", "w", newline="\n"), indent=1)
    open(f"{out}/DONE", "w", newline="\n").write(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")
    print(json.dumps(tot))


if __name__ == "__main__":
    main()
