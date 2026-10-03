"""Reference row 'Extraction + hand-written program' (Table 4 references; C-REF-extract-program): the untrained
backbone's prompted ledger (format-normalised readout, the ledger its judge read) is the extracted state, and role A's
frozen rule program labels each claim from it. Uses role B's scripts/program_ledger.py unchanged (B d3c801a, copied to
scratch/bpl/) with role A's rule_v1 freeze e40789b (scratch/afreeze) in a separate process; u = +10 if the program
finds the claim correct, else -10; a malformed ledger or no program answer rejects both claims. No GPU.
  python scripts/ref_extract_program.py [--src C-TF-promptledger-lenient] [--out C-REF-extract-program]
Validation: --src B-F-ledger2-triplets-s0 --field reader_output (B's own ledgers) reproduces B-AE-program-ledger."""
import argparse, datetime, json, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

RES = f"{REPO}/results_git"
SETS = ("rule_v1/dev_missing", "rule_v1/missing", "rule_v1/test_L2", "rule_v1/test_L3alt")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="C-TF-promptledger-lenient")
    ap.add_argument("--src-dir", default=RES)
    ap.add_argument("--out", default="C-REF-extract-program")
    ap.add_argument("--field", default="ledger_lenient", help="score field holding the extracted ledger")
    ap.add_argument("--sets", default=",".join(SETS))
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    a = ap.parse_args()
    out = f"{RES}/{a.out}"
    os.makedirs(out, exist_ok=True)
    reg = json.load(open(f"{a.data}/REGISTRY.json", encoding="utf-8"))
    stats = {}
    for s in a.sets.split(","):
        name = s.replace("/", "~")
        src = f"{a.src_dir}/{a.src}/scores_{name}.jsonl"
        if not os.path.exists(src):
            print("no scores:", src)
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8", newline="\n") as tmp:
            for line in open(src, encoding="utf-8"):
                r = json.loads(line)
                tmp.write(json.dumps({"iid": r["iid"], "reader_output": r.get(a.field) or ""}) + "\n")
        st = f"{out}/stats_{name}.json"
        subprocess.run([sys.executable, f"{REPO}/scratch/bpl/program_ledger.py", f"{a.data}/{reg[s]['path']}", tmp.name,
                        f"{out}/scores_{name}.jsonl", st], env={**os.environ, "PYTHONPATH": f"{REPO}/scratch/afreeze"},
                       check=True)
        os.remove(tmp.name)
        stats[s] = json.load(open(st, encoding="utf-8"))
        os.remove(st)
        u = {r["iid"]: r["u"] for r in map(json.loads, open(f"{out}/scores_{name}.jsonl", encoding="utf-8"))}
        recs = [r for r in map(json.loads, open(f"{a.data}/{reg[s]['path']}", encoding="utf-8")) if r["iid"] in u]
        T = M.decisions(recs, [u[r["iid"]] for r in recs])
        summ = {"run_id": a.out, "set": s, "claim_type": "conclusion", **M.summarise(T)}
        if summ.get("all"):
            summ["CI95"] = {m: list(M.bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
        summ["eval"] = {"mode": "program_on_extracted_ledger", "source_run": a.src, "field": a.field, **stats[s]}
        json.dump(summ, open(f"{out}/summary_{name}.json", "w", encoding="utf-8", newline="\n"), indent=1)
        print(s, summ.get("all"), stats[s])
    if "rule_v1/dev_missing" in stats and "rule_v1/missing" in stats:
        u = lambda n: {r["iid"]: r["u"] for r in map(json.loads, open(f"{out}/scores_{n}.jsonl", encoding="utf-8"))}
        load = lambda s, sc: [r for r in map(json.loads, open(f"{a.data}/{reg[s]['path']}", encoding="utf-8")) if r["iid"] in sc]
        ud, um = u("rule_v1~dev_missing"), u("rule_v1~missing")
        dm, mi = load("rule_v1/dev_missing", ud), load("rule_v1/missing", um)
        mr = M.missing_rejection(mi, [um[r["iid"]] for r in mi], M.mr_threshold(dm, [ud[r["iid"]] for r in dm]))
        p = f"{out}/summary_rule_v1~missing.json"
        json.dump(json.load(open(p, encoding="utf-8")) | mr, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    json.dump({"run_id": a.out, "kind": "eval (CPU)", "source_run": a.src, "field": a.field,
               "program": "role A rule_v1 freeze e40789b; role B scripts/program_ledger.py d3c801a",
               "git_commit": commit, "per_set": stats}, open(f"{out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{out}/DONE", "w", newline="\n").write(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")


if __name__ == "__main__":
    main()
