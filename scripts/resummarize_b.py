"""Recompute summary_<set>.json of finished B runs from their scores files with the current eval_local.summarize and
selrm/metrics.py (crossed accuracy on xr_v1 and pair reversal on clinical pair sets for summaries written by older
runner code; CIs with the reproducible bootstrap). Each summary keeps its "eval" block. Eval-mode variant files
(set~mode) and CPU runs' summaries are left alone. Records come from the local data copy (report_b.DATA); one set
is in memory at a time, without case texts, ledgers and prose.
  python scripts/resummarize_b.py RUN_ID [RUN_ID ...]   |   python scripts/resummarize_b.py --all"""
import collections, glob, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from eval_local import summarize
from report_b import DATA, RG

KEEP = ("iid", "tid", "case_kind", "claim_type", "claim_role", "label", "rid", "nm_kind", "tier", "level", "family",
        "meta")


def main():
    runs = (sorted(os.path.basename(d) for d in glob.glob(f"{RG}/B-*") if os.path.exists(f"{d}/DONE"))
            if sys.argv[1:] == ["--all"] else sys.argv[1:])
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    todo, skipped = collections.defaultdict(list), set()
    for rid in runs:
        for sp in sorted(glob.glob(f"{RG}/{rid}/summary_*.json")):
            name = os.path.basename(sp)[len("summary_"):-len(".json")]
            sc = f"{RG}/{rid}/scores_{name}.jsonl"
            if name.count("~") != 1 or not os.path.exists(sc):
                continue
            set_name = name.replace("~", "/")
            if set_name not in reg:          # no local copy of this set (e.g. other folds): left as the runner wrote it
                skipped.add(set_name)
                continue
            todo[set_name].append((rid, sp, sc))
    n = 0
    for set_name, items in sorted(todo.items()):
        R_all = [{k: r[k] for k in KEEP}     # streamed: the full records hold case texts, ledgers and prose
                 for r in map(json.loads, open(f"{DATA}/{reg[set_name]['path']}", encoding="utf-8"))]
        for rid, sp, sc in items:
            old = json.load(open(sp, encoding="utf-8"))
            u = {r["iid"]: r["u"] for r in map(json.loads, open(sc, encoding="utf-8"))}
            R = [r for r in R_all if r["iid"] in u]
            new = summarize(R, [u[r["iid"]] for r in R], rid, set_name) | ({"eval": old["eval"]} if "eval" in old else {})
            json.dump(new, open(sp, "w", encoding="utf-8", newline="\n"), indent=1)
            n += 1
        del R_all
    print(n, "summaries recomputed" + (f"; no local copy, left as written: {sorted(skipped)}" if skipped else ""))


if __name__ == "__main__":
    main()
