"""Shortcut validation (project spec, "Shortcut validation"; the Oct 2 checkpoint).

Generates triplets for every valid (rule, criterion, near-miss kind, tier) cell
in both template splits, or reads a JSONL set; re-checks every invariant;
scores the shortcut scorers on every claim type; and requires
  always-default       TA = 0 and Hold = 100
  concept-named        TA = 0 on finding triplets, with Rev = 100 and Hold = 0
                       there (the keyword invariant seen through Proposition 1)
  oracle (program)     TA = 100 on every claim type
  naive-number-parser  fails the superseded tier (TA = 0 there)
TA uses the conclusion claim. Exit status 0 iff all hold.

  python scripts/validate_shortcuts.py [--per-cell 10] [--seed 0] [--set FILE]
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from selrm import engine, metrics, shortcuts  # noqa: E402

COLS = ("rev", "hold", "ta", "pres_hold", "ties", "base_acc")


def generate(per_cell, seed, stats):
    return [engine.make_triplet(rid, cid, nm, tier, split, seed * 100_000 + i, stats)
            for split in ("train", "test") for rid, cid, nm, tier in engine.cells()
            for i in range(per_cell)]


def _ci(s):
    return f"{s[0]:5.1f} [{s[1]:5.1f},{s[2]:5.1f}]"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Shortcut validation (Oct 2 checkpoint).")
    ap.add_argument("--set", type=Path, help="JSONL triplet file (default: generate)")
    ap.add_argument("--per-cell", type=int, default=10, help="triplets per cell and split")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--boot", type=int, default=1000, help="bootstrap resamples over rules")
    a = ap.parse_args(argv)

    if a.set:
        ts = [json.loads(s) for s in a.set.read_text(encoding="utf-8").splitlines() if s.strip()]
        print(f"read {len(ts)} triplets from {a.set}")
    else:
        stats = Counter()
        ts = generate(a.per_cell, a.seed, stats)
        reasons = ", ".join(f"{k[7:]} {v}" for k, v in sorted(stats.items()) if k.startswith("reject "))
        print(f"generated {len(ts)} triplets ({len(engine.cells())} cells x 2 splits x {a.per_cell}); "
              f"rejected {stats['rejected']} of {stats['proposed']} proposals "
              f"({100 * stats['rejected'] / stats['proposed']:.1f}%){': ' + reasons if reasons else ''}")
    bad = [(t["tid"], e) for t in ts for e in engine.check(t)]
    print(f"invariant violations: {len(bad)}")
    for tid, e in bad[:20]:
        print(f"  {tid}: {e}")

    rows = {name: [metrics.row(t, shortcuts.score(t, f, claim), claim)
                   for t in ts for claim in t["claims"]] for name, f in shortcuts.SCORERS.items()}
    concl = {name: [r for r in rs if r["claim"] == "conclusion"] for name, rs in rows.items()}
    print(f"\nconclusion claim\n{'scorer':20} {'subset':8} {'n':>5}  "
          + "  ".join(f"{c:>19}" for c in COLS))
    summ = {}
    for name, rs in concl.items():
        summ[name] = {"all": metrics.summarize(rs, a.boot),
                      **metrics.breakdown(rs, "kind", boot=a.boot),
                      **{("heldout" if k else "seen"): v
                         for k, v in metrics.breakdown(rs, "heldout", boot=a.boot).items()}}
        for subset, s in summ[name].items():
            print(f"{name:20} {subset:8} {s['n']:5}  " + "  ".join(f"{_ci(s[c]):>19}" for c in COLS))
    for key, src in (("claim", rows), ("nm_kind", concl), ("tier", concl)):
        print(f"\nHold / TA by {key}" + (" (all claim types)" if key == "claim" else ""))
        for name, rs in src.items():
            parts = metrics.breakdown(rs, key, boot=1)
            print(f"  {name:20} " + " | ".join(f"{g} {s['hold'][0]:.0f}/{s['ta'][0]:.0f}"
                                               for g, s in parts.items()))

    s = {name: parts["all"] for name, parts in summ.items()}
    fnd = summ["concept_named"].get("finding", {"n": 0})
    orc = metrics.breakdown(rows["oracle"], "claim", boot=1)
    sup = metrics.breakdown(concl["naive_number_parser"], "tier", boot=1).get("superseded", {"n": 0})
    checks = [
        ("no invariant violations", not bad),
        ("always-default TA = 0", s["always_default"]["ta"][0] == 0),
        ("always-default Hold = 100", s["always_default"]["hold"][0] == 100),
        ("concept-named TA = 0 on finding triplets", fnd["n"] > 0 and fnd["ta"][0] == 0),
        ("concept-named Rev = 100 on finding triplets", fnd["n"] > 0 and fnd["rev"][0] == 100),
        ("concept-named Hold = 0 on finding triplets", fnd["n"] > 0 and fnd["hold"][0] == 0),
        ("oracle TA = 100 on every claim type", all(v["ta"][0] == 100 for v in orc.values())),
        ("naive-number-parser TA = 0 on the superseded tier", sup["n"] > 0 and sup["ta"][0] == 0),
    ]
    print("\nshortcut validation")
    for what, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {what}")
    passed = all(ok for _, ok in checks)
    print("CHECKPOINT PASSED" if passed else "CHECKPOINT FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
