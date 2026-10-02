"""Build an evaluation set (project spec, "Sets").

  python scripts/make_set.py --set test   # 2,000 triplets -> data/test.jsonl
  python scripts/make_set.py --set dev    #   300 triplets -> data/dev.jsonl

test: test-split templates, cues and names; 60% easy / 40% hard, the hard part
split evenly over the hard tiers a family group has cells for (long,
superseded, delabelled, alt); 25% of triplets from the held-out structural
families. dev: train-split phrases and seen families only, so no choice made
on dev sees held-out phrasing or structure. Within each (family group, tier)
stratum, near-miss kinds and then rules are drawn round-robin, and cells
uniformly within a rule. Each set has its own seed; a triplet whose
base/flip/near texts repeat is redrawn.
"""
import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from selrm import engine  # noqa: E402
from selrm.rules import HELDOUT_FAMILIES, RULES_BY_ID  # noqa: E402

SETS = {"test": dict(n=2000, seed=1, split="test", heldout=0.25),
        "dev": dict(n=300, seed=2, split="train", heldout=0.0)}
HARD = 0.4


def plan(n, heldout, rng):
    """Cells for n triplets, stratified by family group and tier."""
    out = []
    n_held = round(n * heldout)
    for held, m in ((True, n_held), (False, n - n_held)):
        cs = [c for c in engine.cells() if (RULES_BY_ID[c[0]].family in HELDOUT_FAMILIES) == held]
        if not m:
            continue
        hard = sorted({c[3] for c in cs} - {"easy"})
        n_hard = round(m * HARD)
        quota = {"easy": m - n_hard,
                 **{t: n_hard // len(hard) + (i < n_hard % len(hard)) for i, t in enumerate(hard)}}
        for tier, q in quota.items():
            by_kind = {}
            for c in cs:
                if c[3] == tier:
                    by_kind.setdefault(c[2], {}).setdefault(c[0], []).append(c)
            kinds = sorted(by_kind)
            rng.shuffle(kinds)
            rules = {k: rng.sample(sorted(v), len(v)) for k, v in by_kind.items()}
            for i in range(q):     # round-robin over near-miss kinds, then rules
                k = kinds[i % len(kinds)]
                rid = rules[k][(i // len(kinds)) % len(rules[k])]
                out.append(rng.choice(by_kind[k][rid]))
    rng.shuffle(out)
    return out


def build(name, n=None):
    cfg = SETS[name]
    rng = random.Random(f"set:{name}:{cfg['seed']}")
    seen, ts, stats = set(), [], Counter()
    for i, cell in enumerate(plan(n or cfg["n"], cfg["heldout"], rng)):
        for retry in range(20):
            t = engine.make_triplet(*cell, cfg["split"], f"{name}{cfg['seed']}-{i}-{retry}", stats)
            key = tuple(t["cases"][k]["text"] for k in ("base", "flip", "near"))
            if key not in seen:
                break
        else:
            raise RuntimeError(f"{cell}: 20 duplicate draws")
        seen.add(key)
        ts.append(t)
    return ts, stats


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the test or dev set.")
    ap.add_argument("--set", choices=sorted(SETS), required=True)
    ap.add_argument("--n", type=int, help="override the set size")
    ap.add_argument("--out", type=Path, help="default data/<set>.jsonl")
    a = ap.parse_args(argv)
    ts, stats = build(a.set, a.n)
    out = a.out or Path(__file__).resolve().parents[1] / "data" / f"{a.set}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(t) + "\n" for t in ts), encoding="utf-8")
    held = Counter(RULES_BY_ID[t["rule"]].family in HELDOUT_FAMILIES for t in ts)
    print(f"wrote {len(ts)} triplets to {out}; rejected {stats['rejected']} of "
          f"{stats['proposed']} proposals")
    print(f"  held-out families {held[True]}, seen {held[False]}; rules {len({t['rule'] for t in ts})}")
    for key in ("tier", "nm_kind", "split"):
        print(f"  {key}: {dict(sorted(Counter(t[key] for t in ts).items()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
