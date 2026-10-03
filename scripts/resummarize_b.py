"""Recompute summary_<set>.json of finished B runs from their scores files with the current eval_local.summarize and
selrm/metrics.py (crossed accuracy on xr_v1 and pair reversal on clinical pair sets for summaries written by older
runner code; CIs with the reproducible bootstrap). Each summary keeps its "eval" block. Eval-mode variant files
(set~mode) and CPU runs' summaries are left alone. Records come from the local data copy (report_b.DATA).
  python scripts/resummarize_b.py RUN_ID [RUN_ID ...]   |   python scripts/resummarize_b.py --all"""
import glob, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from eval_local import summarize
from report_b import RG, records


def main():
    runs = (sorted(os.path.basename(d) for d in glob.glob(f"{RG}/B-*") if os.path.exists(f"{d}/DONE"))
            if sys.argv[1:] == ["--all"] else sys.argv[1:])
    n = 0
    for rid in runs:
        for sp in sorted(glob.glob(f"{RG}/{rid}/summary_*.json")):
            name = os.path.basename(sp)[len("summary_"):-len(".json")]
            old = json.load(open(sp, encoding="utf-8"))
            sc = f"{RG}/{rid}/scores_{name}.jsonl"
            if name.count("~") != 1 or not os.path.exists(sc) or old.get("eval", {}).get("mode") == "program_on_predicted_ledger":
                continue
            u = {r["iid"]: r["u"] for r in map(json.loads, open(sc, encoding="utf-8"))}
            set_name = name.replace("~", "/")
            R = [r for r in records(set_name) if r["iid"] in u]
            new = summarize(R, [u[r["iid"]] for r in R], rid, set_name) | ({"eval": old["eval"]} if "eval" in old else {})
            json.dump(new, open(sp, "w", encoding="utf-8", newline="\n"), indent=1)
            n += 1
    print(n, "summaries recomputed")


if __name__ == "__main__":
    main()
