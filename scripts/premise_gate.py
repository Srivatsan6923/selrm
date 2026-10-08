"""B-AE-premise-gate (Table 9 'premise gate', after evpv2026; CPU): the step check (released Med-PRM, scored by C as
C-AUD-medprm: u = log-odds of '+' for every claim record), attenuated toward a neutral score when the claim's premise
is not supported by a ledger extracted once per case. The ledger is the reader output of B-F-ledger2-triplets-s0;
its support for a claim is A's rule program applied to that ledger (B-AE-program-ledger: u = +10 when the program
finds the claim correct). Gated score: u = u_prm if supported, else alpha * u_prm; alpha is chosen on rule_v1/dev
(triplet accuracy, ties fail) from ALPHAS and then fixed for rule_v1/test_L2. Writes results_git/B-AE-premise-gate/.
  python scripts/premise_gate.py [--prm_ref origin/role-c]"""
import argparse, datetime, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from eval_local import summarize
from report_b import DATA, RG

ALPHAS = (0.0, 0.25, 0.5, 0.75, 1.0)          # 1.0 = the ungated step check
OUT = "B-AE-premise-gate"
KEEP = ("iid", "tid", "case_kind", "claim_type", "claim_role", "label", "rid", "nm_kind", "tier", "level", "family", "meta")


def load_scores(text):
    return {r["iid"]: r["u"] for r in map(json.loads, text.splitlines()) if r}


def gated(prm, prog, alpha):
    return {i: (u if prog.get(i, -1.0) > 0 else alpha * u) for i, u in prm.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prm_ref", default="origin/role-c")
    a = ap.parse_args()
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    git = lambda path: subprocess.run(["git", "-C", ROOT, "show", f"{a.prm_ref}:{path}"], capture_output=True, text=True,
                                      encoding="utf-8", check=True).stdout
    data = {}
    for s in ("rule_v1/dev", "rule_v1/test_L2"):
        name = s.replace("/", "~")
        prm = load_scores(git(f"results_git/C-AUD-medprm/scores_{name}.jsonl"))
        prog = load_scores(open(f"{RG}/B-AE-program-ledger/scores_{name}.jsonl", encoding="utf-8").read())
        recs =[r for r in ({k: x[k] for k in KEEP} for x in map(json.loads, open(f"{DATA}/{reg[s]['path']}", encoding="utf-8")))
                if r["iid"] in prm]
        data[s] = (recs, prm, prog)
    recs, prm, prog = data["rule_v1/dev"]
    dev_ta = {}
    for al in ALPHAS:
        u = gated(prm, prog, al)
        dev_ta[al] = (summarize(recs, [u[r["iid"]] for r in recs], OUT, "rule_v1/dev").get("all") or {}).get("TA")
    alpha = max(ALPHAS, key=lambda al: (dev_ta[al] if dev_ta[al] is not None else -1, -al))
    out = f"{RG}/{OUT}"
    os.makedirs(out, exist_ok=True)
    for s, (recs, prm, prog) in data.items():
        name = s.replace("/", "~")
        u = gated(prm, prog, alpha)
        with open(f"{out}/scores_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for r in recs:
                f.write(json.dumps({"iid": r["iid"], "u": u[r["iid"]]}) + "\n")
        summ = summarize(recs, [u[r["iid"]] for r in recs], OUT, s)
        summ["eval"] = {"mode": "premise_gate", "alpha": alpha, "alpha_dev_TA": {str(k): v for k, v in dev_ta.items()},
                        "supported_share": round(sum(prog.get(i, -1) > 0 for i in prm) / len(prm), 4),
                        "step_check": "C-AUD-medprm", "ledger_support": "B-AE-program-ledger"}
        json.dump(summ, open(f"{out}/summary_{name}.json", "w", encoding="utf-8", newline="\n"), indent=1)
    commit = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    prm_commit = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short=12", a.prm_ref], capture_output=True, text=True).stdout.strip()
    json.dump({"run_id": OUT, "kind": "eval (CPU)", "step_check": f"C-AUD-medprm at {a.prm_ref} {prm_commit}",
               "ledger_support": "B-AE-program-ledger (A's rule program on B-F-ledger2-triplets-s0's ledgers)",
               "alpha": alpha, "alphas": list(ALPHAS), "alpha_chosen_on": "rule_v1/dev", "git_commit": commit,
               "eval_sets": list(data)}, open(f"{out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{out}/DONE", "w", newline="\n").write(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")
    print(json.dumps({"alpha": alpha, "dev_TA": dev_ta}))


if __name__ == "__main__":
    main()
