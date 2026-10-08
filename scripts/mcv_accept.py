"""Acceptance test of the MedCalc-V score specifications (STAGE2_TASKS_A, A1.2).

A score is accepted iff the sum of its item points over the released entity dictionary equals
`Ground Truth Answer` on every rule-based test and training row. No row-level special cases.

  python scripts/mcv_accept.py                 # table for every specified score
  python scripts/mcv_accept.py --cid 45 -v     # one score, mismatching rows with their explanation
  python scripts/mcv_accept.py --write         # results/A-MCV-ACCEPT/summary.json
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import mcv  # noqa: E402


def check(score, rows):
    bad = []
    for r in rows:
        try:
            got = score.total(r["ent"])
        except Exception as e:                      # an unhandled unit or type is a mismatch, not a crash
            got = f"{type(e).__name__}: {e}"
        if got != r["answer"]:
            bad.append((r, got))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cid", type=int)
    ap.add_argument("-v", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    data = {s: mcv.rows(s) for s in ("test", "train")}
    specs = mcv.load_scores()
    cids = sorted({r["cid"] for r in data["test"]})
    out = {"run_id": "A-MCV-ACCEPT", "pin": mcv.PIN, "scores": {}}
    for cid in cids:
        if a.cid and cid != a.cid:
            continue
        name = next(r["Calculator Name"] for r in data["test"] if r["cid"] == cid)
        row = {"name": name, "specified": cid in specs}
        for split in ("test", "train"):
            rs = [r for r in data[split] if r["cid"] == cid]
            row[f"{split}_rows"] = len(rs)
            row[f"{split}_human"] = sum(r["Note Type"] == "Extracted" for r in rs)
            if cid in specs:
                bad = check(specs[cid], rs)
                row[f"{split}_mismatch"] = len(bad)
                row[f"{split}_mismatch_rows"] = [r["Row Number"] for r, _ in bad]
                if a.v:
                    for r, got in bad[:8]:
                        print(f"--- {split} row {r['Row Number']} note {r['Note ID']}: got {got}, answer {r['answer']}")
                        print(json.dumps(specs[cid].item_points(r["ent"]) if not isinstance(got, str) else got))
                        print(r["ent"])
                        print(r["Ground Truth Explanation"].encode("ascii", "replace").decode())
        row["accepted"] = bool(row["specified"] and not row["test_mismatch"] and not row["train_mismatch"])
        out["scores"][str(cid)] = row
        print(f"{cid:3d} {name[:48]:48s} items {len(specs[cid].items) if cid in specs else '-':>3} "
              f"test {row.get('test_mismatch', '-')}/{row['test_rows']} train {row.get('train_mismatch', '-')}/{row['train_rows']}"
              f"  {'ACCEPTED' if row['accepted'] else ('mismatch' if row['specified'] else 'no spec')}")
    acc = [r for r in out["scores"].values() if r["accepted"]]
    out["n_scores"], out["n_accepted"] = len(out["scores"]), len(acc)
    out["test_rows_covered"] = sum(r["test_rows"] for r in acc)
    out["test_human_covered"] = sum(r["test_human"] for r in acc)
    out["train_rows_covered"] = sum(r["train_rows"] for r in acc)
    print(f"accepted {out['n_accepted']} of {out['n_scores']}; test rows {out['test_rows_covered']} "
          f"(human-written {out['test_human_covered']}); training rows {out['train_rows_covered']}")
    if a.write:
        d = ROOT / "results" / "A-MCV-ACCEPT"
        d.mkdir(parents=True, exist_ok=True)
        (d / "summary.json").write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
        (d / "DONE").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
