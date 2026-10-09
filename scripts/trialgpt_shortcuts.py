"""Shortcut validation of clin_v1/trialgpt_{dev,test} (FINAL_TASKS: every new set has one
before any model is scored): case-blind predictors and their macro-F1 / accuracy on the
non-N/A items, written into each MANIFEST.json under "shortcut_validation".
A claim-only scorer (u depends on the claim alone) gives the same prediction for every
item (Proposition 1 (i)), so it is one of the constant predictors. The type prior is the
most frequent category per criterion type in the development portion.
  python scripts/trialgpt_shortcuts.py"""
import collections, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm.metrics import prf

CATS = ("met", "not_met", "nei")


def items(split):
    recs = [json.loads(l) for l in open(f"{REPO}/data/clin_v1/trialgpt_{split}/records.jsonl", encoding="utf-8")]
    return [(r["family"], r["meta"]["category"]) for r in recs if r["claim_role"] == "s" and r["meta"]["category"] != "na"]


def main():
    dev = items("dev")
    prior = {t: collections.Counter(c for tt, c in dev if tt == t).most_common(1)[0][0] for t in ("inclusion", "exclusion")}
    for split in ("dev", "test"):
        xs = items(split)
        gold = [c for _, c in xs]
        preds = {f"always {c}": [c] * len(xs) for c in CATS}
        preds[f"type prior from dev {prior}"] = [prior[t] for t, _ in xs]
        res = {k: {m: v for m, v in prf(gold, p, CATS).items() if m in ("macroF1", "acc")} for k, p in preds.items()}
        path = f"{REPO}/data/clin_v1/trialgpt_{split}/MANIFEST.json"
        man = json.load(open(path, encoding="utf-8"))
        man["shortcut_validation"] = {"predictors": res, "n_items": len(xs),
                                      "note": "case-blind predictors on non-N/A items; a claim-only scorer equals a constant predictor"}
        json.dump(man, open(path, "w", encoding="utf-8", newline="\n"), indent=1)
        print(split, json.dumps(res))


if __name__ == "__main__":
    main()
