"""Why reader ledgers fail the frozen check (INTERFACES 3), per reader unit, from a run's stored outputs. No GPU.
  python scripts/malformed_reasons.py RUN_DIR SET [--bcode scratch/bcode]
Classes, first failing entry decides: entry not five lines (a value written over several lines); last entry cut
(fewer than five lines at the end: generation cap); field names or order; found not verbatim in the case; other.
Writes RUN_DIR/malformed_reasons_<set>.json."""
import argparse, collections, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("run_dir"); ap.add_argument("set"); ap.add_argument("--bcode", default=f"{REPO}/scratch/bcode")
a = ap.parse_args()
sys.path.insert(0, a.bcode)
from selrm.formats import well_formed

name = a.set.replace("/", "~")
recs = {r["iid"]: r for r in map(json.loads, open(f"{REPO}/data/{a.set}/records.jsonl", encoding="utf-8"))}
seen, why = set(), collections.Counter()
for row in map(json.loads, open(f"{a.run_dir}/scores_{name}.jsonl", encoding="utf-8")):
    rec = recs[row["iid"]]
    unit = (rec["tid"], rec["case_kind"])
    if unit in seen:
        continue
    seen.add(unit)
    t = row.get("reader_output", "")
    if well_formed(t, rec["case_text"], "ledger2"):
        why["well formed"] += 1
        continue
    entries, bad = t.strip().split("\n\n"), "other"
    for k, e in enumerate(entries):
        lines = e.split("\n")
        if len(lines) != 5:
            bad = "last entry cut" if k == len(entries) - 1 and len(lines) < 5 else "entry not five lines"
            break
        if [l.partition(": ")[0] for l in lines] != ["need", "found", "subject", "status", "time"]:
            bad = "field names or order"
            break
        f = lines[1].partition(": ")[2]
        if f != "not mentioned" and f not in rec["case_text"]:
            bad = "found not verbatim"
            break
    why[bad] += 1
n = sum(why.values())
out = {"run": os.path.basename(os.path.normpath(a.run_dir)), "set": a.set, "units": n, "counts": dict(why),
       "shares": {k: 100.0 * v / n for k, v in why.items()}}
json.dump(out, open(f"{a.run_dir}/malformed_reasons_{name}.json", "w", encoding="utf-8", newline="\n"), indent=1)
print(json.dumps(out))
