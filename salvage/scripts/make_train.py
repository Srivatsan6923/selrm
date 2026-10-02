"""Training corpora for E4 (project spec, "Training data (E4)").

  python scripts/make_train.py [--n 60000] [--seed 3] [--out data/train]

Writes balanced, flips, triplets, no_pres and conclusion_only, n examples each
with 50/50 labels, from seen rule families, train-split templates, cues and
names, and tiers easy and long (superseded, delabelled and alt stay test-only
shifts). An example is one case with one claim pair: claim type, the two
claims, the executed label, the case text and the program's ledger
(engine.prose() renders the prose variant). All corpora are cut from one pool
of triplets with shared random draws, so they differ in one ingredient:
  balanced         flip cases of one half of the pool, base or presentation
                   cases of the other half; no pairs
  flips            (base, flip) pairs; presentation edits = 15% of label-0 cases
  triplets         flips with half of the label-0 cases replaced by near-misses
                   (kinds equally often); presentation edits = 15% of label-0
  no_pres          triplets without presentation edits
  conclusion_only  triplets with the conclusion claim only (G7)
The two cases of a pair are adjacent, in random order, and share a pair id and
claim (for the change loss). Also writes manifest.json with the composition.
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

KINDS = ("numeric", "subject", "negation", "time")
CORPORA = ("balanced", "flips", "triplets", "no_pres", "conclusion_only")
PRES = 0.15         # share of label-0 cases that are presentation edits
LONG = 0.2          # share of long-tier triplets in the pool


def pool(n, seed, part, stats):
    """n train triplets, near-miss kinds cycled so each is equally frequent."""
    rng = random.Random(f"pool:{seed}:{part}")
    cs = [c for c in engine.cells()
          if RULES_BY_ID[c[0]].family not in HELDOUT_FAMILIES and c[3] in ("easy", "long")]
    rules = {k: sorted({c[0] for c in cs if c[2] == k}) for k in KINDS}
    out = []
    for i in range(n):
        kind = KINDS[i % len(KINDS)]
        rid = rng.choice(rules[kind])
        tier = "long" if rng.random() < LONG else "easy"
        cell = rng.choice([c for c in cs if c[0] == rid and c[2] == kind and c[3] == tier])
        out.append(engine.make_triplet(*cell, "train", f"train{seed}{part}-{i}", stats))
    return out


def example(corpus, t, role, claim, eid, pair=None):
    case = t["cases"][role]
    return {"eid": eid, "pair": pair, "corpus": corpus, "tid": t["tid"], "rule": t["rule"],
            "family": t["family"], "criterion": t["criterion"], "nm_kind": t["nm_kind"],
            "tier": t["tier"], "case": role, "claim": claim, "claims": t["claims"][claim],
            "label": case["labels"][claim], "rule_text": t["rule_text"], "text": case["text"],
            "ledger": case["ledger"]}


def build(n, seed):
    stats = Counter()
    half = n // 2
    a, b = pool(half, seed, "a", stats), pool(half, seed, "b", stats)
    rng = random.Random(f"draws:{seed}")
    u_claim_a = [rng.random() for _ in range(half)]
    u_claim_b = [rng.random() for _ in range(half)]
    u_pres = [rng.random() for _ in range(half)]
    u_swap = [rng.random() for _ in range(half)]
    near = set(rng.sample(range(half), half // 2))
    order = list(range(half))
    rng.shuffle(order)

    def claim(t, u):
        kinds = list(t["claims"])
        return kinds[int(u * len(kinds))]

    out = {c: [] for c in CORPORA}
    for i in order:
        t = a[i]
        label0 = {"flips": "pres" if u_pres[i] < PRES else "base",
                  "triplets": "near" if i in near else ("pres" if u_pres[i] < 2 * PRES else "base"),
                  "no_pres": "near" if i in near else "base"}
        label0["conclusion_only"] = label0["triplets"]
        for corpus, role in label0.items():
            c = "conclusion" if corpus == "conclusion_only" else claim(t, u_claim_a[i])
            pair = f"{corpus}:{i}"
            two = [example(corpus, t, r, c, f"{pair}:{r}", pair) for r in (role, "flip")]
            out[corpus] += two[::-1] if u_swap[i] < 0.5 else two
    for i in order:   # balanced: no pairs; label-1 from a, label-0 from b
        out["balanced"].append(example("balanced", a[i], "flip", claim(a[i], u_claim_a[i]),
                                       f"balanced:a{i}:flip"))
        role = "pres" if u_pres[i] < PRES else "base"
        out["balanced"].append(example("balanced", b[i], role, claim(b[i], u_claim_b[i]),
                                       f"balanced:b{i}:{role}"))
    rng.shuffle(out["balanced"])
    return out, stats


def manifest(corpora, stats):
    m = {"proposals": stats["proposed"], "rejected": stats["rejected"]}
    for name, exs in corpora.items():
        label0 = [e for e in exs if e["label"] == 0]
        m[name] = {"n": len(exs), "pairs": len({e["pair"] for e in exs if e["pair"]}),
                   "labels": dict(Counter(e["label"] for e in exs)),
                   "cases": dict(Counter(e["case"] for e in exs)),
                   "pres_share_of_label0": round(sum(e["case"] == "pres" for e in label0)
                                                 / max(1, len(label0)), 4),
                   "claims": dict(Counter(e["claim"] for e in exs)),
                   "near_kinds": dict(Counter(e["nm_kind"] for e in exs if e["case"] == "near")),
                   "tiers": dict(Counter(e["tier"] for e in exs)),
                   "rules": len({e["rule"] for e in exs})}
    return m


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the E4 training corpora.")
    ap.add_argument("--n", type=int, default=60000, help="examples per corpus")
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "data" / "train")
    a = ap.parse_args(argv)
    corpora, stats = build(a.n, a.seed)
    a.out.mkdir(parents=True, exist_ok=True)
    for name, exs in corpora.items():
        (a.out / f"{name}.jsonl").write_text("".join(json.dumps(e) + "\n" for e in exs),
                                             encoding="utf-8")
    m = manifest(corpora, stats)
    (a.out / "manifest.json").write_text(json.dumps(m, indent=1), encoding="utf-8")
    print(json.dumps(m, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
