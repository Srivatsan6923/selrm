"""C-DG-shift (App. F diagnosis figure): shift classes and kappa per signal, each computed from its source run's
per-example scores by scripts/diagnostics.py shift (rule_v1/missing; tau from the run's rule_v1/test_L2), written as
slices signal=<name> of results_git/C-DG-shift/summary_rule_v1~test_L0.json (the set make_tables reads); a later
call adds or replaces signals. Shares are percentages of the opposed cases. No GPU.
  python scripts/dg_shift.py NAME=RUN_DIR [NAME=RUN_DIR ...]"""
import datetime, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from diagnostics import shift

OUT = f"{REPO}/results_git/C-DG-shift"
DATA = os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1")


def main():
    os.makedirs(OUT, exist_ok=True)
    p = f"{OUT}/summary_rule_v1~test_L0.json"
    summ = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {
        "run_id": "C-DG-shift", "set": "rule_v1/test_L0", "analysed_set": "rule_v1/missing",
        "definition": "scripts/diagnostics.py shift (v13 App. F, Eq. 1-2)"}
    for arg in sys.argv[1:]:
        name, run = arg.split("=", 1)
        res = shift(run, DATA)
        if res is None:
            print(f"{name}: no missing / test_L2 scores in {run}")
            continue
        sh = res["shares_of_opposed"] or {}
        summ[f"signal={name}"] = {"crossed": sh.get("crossed"), "short": sh.get("short"), "unmoved": sh.get("unmoved"),
                                  "wrong": sh.get("wrong_direction"), "kappa": res["kappa"], "tau": res["tau"],
                                  "counts": res["counts"], "n_opposed": res["n_opposed"],
                                  "source_run": os.path.basename(os.path.normpath(run))}
        print(name, json.dumps(summ[f"signal={name}"]))
    json.dump(summ, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{OUT}/DONE", "w", newline="\n").write(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")


if __name__ == "__main__":
    main()
