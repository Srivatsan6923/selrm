"""Build rule_v1 (A-D4 core freeze, A-D5..D8 test and diagnostic sets, A-D9 folds).

  python scripts/build_rule_v1.py                  # data/rule_v1, fold 1, full sizes
  python scripts/build_rule_v1.py --freeze         # also mark the sets frozen in data/REGISTRY.json
  python scripts/build_rule_v1.py --fold 2         # data/rule_v1_fold2: test_L2, dev, train blocks/triplets
  python scripts/build_rule_v1.py --out /tmp/x --scale 0.01   # small build for tests

Sets (fold 1): test_L2 (held-out classes, test templates), missing (missing
twins of the first test_L2 groups + one ordinary case each), dev (training
rules, test templates), dev_missing (threshold set for MR at 5% FR), and
train_{natural,balanced,blocks,triplets} (training rules, train templates).
Every set gets records.jsonl + MANIFEST.json; triplet sets must pass shortcut
validation. Output is deterministic (seeded by group id); frozen registry
entries are never overwritten.
"""
import argparse
import datetime
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import folds as FD  # noqa: E402
from selrm.library import LIBRARY, LIBRARY_BY_ID  # noqa: E402
from selrm.rules_grammar import invented_rules  # noqa: E402

SIZES = {"test_L2": 2000, "missing": 1000, "dev": 300, "train": 60000, "ladder": 1000, "readapply": 1000}
HARD = {"long": 1, "superseded": 1, "delabelled": 1}
POOL = 40000                     # training group specs (natural needs about 18k groups)


def ladder_and_diagnostics(emit, rules, n, SET):
    """A-D5 ladder (L0, L1, L3-alt, L3-inv), A-D6 hard tiers, A-D8 reading/application."""
    for name, key, level, tiers, seed in (("test_L0", "train_rules", "L0", D.TIER_W, "test_L0"),
                                          ("test_L1", "l1_rules", "L1", D.TIER_W, "test_L1"),
                                          ("test_L3alt", "train_rules", "L3-alt", {"alt": 1}, "test_L3alt"),
                                          ("test_hard", "l2_rules", "L2", HARD, "test_hard")):
        st = Counter()
        specs = D.sample_specs(rules(key), n["ladder"], seed, tiers)
        emit(name, (r for g in D.groups(specs, "test", SET, level, st) for r in g),
             {"split": "test", "level": level, "templates": "test", "tiers": sorted(tiers), "stats": st},
             validate=True)
    st = Counter()
    inv = D.register(invented_rules())
    specs = D.sample_specs(inv, n["ladder"], "test_L3inv")
    emit("test_L3inv", (r for g in D.groups(specs, "test", SET, "L3-inv", st) for r in g),
         {"split": "test", "level": "L3-inv", "templates": "test", "rules": [r.rid for r in inv],
          "note": "grammar-sampled rules over invented conditions and orders (rules_grammar.INVENTED)",
          "stats": st}, validate=True)
    specs = D.sample_specs([r for r in rules("train_rules") if r.kind == "score" or r.logic == "any"],
                           3 * n["readapply"], "readapply")
    emit("readapply", D.readapply_set(specs, n["readapply"], SET, "L0"),
         {"split": "test", "level": "L0", "templates": "test",
          "note": "triplets (tid) + reading and application pairs (tid.base, tid.flip; case kinds "
                  "read/apply, claim_type conclusion); rules whose one-line cases decide the conclusion"},
         validate=True)


def diversity(emit, F, fold, scale, SET):
    """A-D10 diversity curves (Fig. 3 left): triplets corpora over x training rules,
    records proportional to x (60k at 256), grown three ways from the same 16 rules:
    rules of new classes, rules of the two starting classes, or only more groups for
    the 16 rules. Sizes a library cannot fill are skipped (logged in the manifest)."""
    rng = random.Random(f"div.{F['seed']}")
    train = set(fold["train_rules"])
    cls = {c: sorted(r for r in rids if r in train) for c, rids in F["classes"].items()}
    cls = {c: rng.sample(v, len(v)) for c, v in sorted(cls.items()) if v}
    a, b = sorted(cls, key=lambda c: (-len(cls[c]), c))[:2]           # the two largest classes
    start = cls[a][:8] + cls[b][:8]
    same = start + [r for r in cls[a][8:] + cls[b][8:]]
    others = [c for c in cls if c not in (a, b)]
    rest = [r for i in range(max(len(v) for v in cls.values()))       # round robin over new classes
            for c in others for r in cls[c][i:i + 1]]
    new = start + rest + cls[a][8:] + cls[b][8:]
    per_rule = 60000 / 256
    # standard sizes, plus the largest size each grown curve reaches (all three curves are
    # built there too, so every point compares matched data)
    sizes = sorted({x for x in (16, 32, 64, 128, 256) if x <= len(new)} | {min(len(same), 256), min(len(new), 256)})
    for x in sizes:
        n = max(14 * 4, int(per_rule * x * scale))
        for name, rids in (("new", new[:x]), ("same", same[:x]), ("patients", start)):
            if x == 16 and name != "new":
                continue                                            # the three curves share x = 16
            if len(rids) < (16 if name == "patients" else x):
                continue
            pool = D.sample_specs([LIBRARY_BY_ID[r] for r in rids], max(n, 14 * 20), f"div.{name}.{x}")
            emit(f"div_{'base' if x == 16 else name}_{x}", D.corpus("triplets", pool, n, SET),
                 {"split": "train", "level": "L0", "templates": "train", "corpus": "triplets",
                  "diversity": {"curve": name, "x": x, "rules": rids, "start_classes": [a, b]}})


def ablations(emit, pool, n, SET):
    """A-D12 corpora that cannot be derived from the four main corpora: triplets
    without presentation edits, triplets with conclusion claims only (same record
    count), and the blocks corpus plus its groups' near-miss and presentation cases
    as probes (meta.probe) for re-weighting. Decision-field, bit-only and
    no-resampling variants use meta.criterion_holds and the ledgers of each case."""
    for name, kind, kw in (("abl_nopres_triplets", "triplets_nopres", {}),
                           ("abl_conclusion_triplets", "triplets", {"claim_types": ("conclusion",)}),
                           ("abl_probe_blocks", "blocks", {"probes": True})):
        st = Counter()
        emit(name, D.corpus(kind, pool, n["train"], SET, st, **kw),
             {"split": "train", "level": "L0", "templates": "train", "corpus": kind, "ablation": name,
              "stats": st})


def experiments(emit, rules, pool, n, SET):
    """Two later experiments. Leave one near-miss kind out: the triplets corpus over
    groups of the other near-miss kinds only (subject, negation, time or boundary held out).
    Near-miss dose: the blocks corpus with 5, 12 or 25% of base cases replaced by
    near-misses of all kinds (0% = train_blocks, 50% = train_triplets, same pool)."""
    for held in ("subject", "negation", "time", "boundary"):
        st = Counter()
        lo_pool = D.sample_specs(rules("train_rules"), len(pool), f"train.lo_{held}",
                                 kinds=[k for k in D.KINDS if k != held])
        emit(f"train_triplets_lo_{held}", D.corpus("triplets", lo_pool, n["train"], SET, st),
             {"split": "train", "level": "L0", "templates": "train", "corpus": "triplets",
              "experiment": {"leave_out_near_miss_kind": held}, "stats": st})
    for pct in (5, 12, 25):
        st = Counter()
        emit(f"train_dose_{pct:02d}", D.corpus(f"dose_{pct:02d}", pool, n["train"], SET, st),
             {"split": "train", "level": "L0", "templates": "train", "corpus": f"dose_{pct:02d}",
              "experiment": {"base_cases_replaced_by_near_misses": pct / 100}, "stats": st})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data")
    ap.add_argument("--fold", type=int, default=1)
    ap.add_argument("--scale", type=float, default=1.0)
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--only", default="", help="comma-separated set names: build only these (new sets "
                    "of a frozen version; the frozen fold assignment is read, never rewritten)")
    a = ap.parse_args()
    n = {k: max(14, int(v * a.scale)) for k, v in SIZES.items()}
    root = Path(a.out)
    SET = "rule_v1" if a.fold == 1 else f"rule_v1_fold{a.fold}"
    out = root / SET
    reg_path = root / "REGISTRY.json"
    registry = json.loads(reg_path.read_text()) if reg_path.exists() else {}
    only = set(filter(None, a.only.split(",")))
    frozen = [k for k, v in registry.items() if k.startswith(SET + "/") and v.get("frozen")
              and (not only or k.split("/", 1)[1] in only)]
    if frozen:
        sys.exit(f"refusing to rebuild: frozen sets {frozen}")

    frozen_folds = root / "rule_v1" / "FOLDS.json"
    if (a.fold != 1 or only) and frozen_folds.exists():   # folds 2-3 and added sets use the frozen folds
        F = json.loads(frozen_folds.read_text())
    else:
        F = json.loads(json.dumps(FD.make_folds(LIBRARY)))
    out.mkdir(parents=True, exist_ok=True)
    if not (only and (out / "FOLDS.json").exists()):
        (out / "FOLDS.json").write_text(json.dumps(F, indent=1), encoding="utf-8")
    fold = F["folds"][str(a.fold)]

    def rules(key):
        return [LIBRARY_BY_ID[x] for x in fold[key]]

    created = datetime.date.today().isoformat()
    base = {"set": SET, "fold": a.fold, "fold_seed": F["seed"], "created": created,
            "generator": "scripts/build_rule_v1.py", "frozen": a.freeze}
    mans = {}

    def emit(name, recs, info, validate=False):
        if only and name not in only:          # records are generated lazily: skipped sets cost nothing
            return
        stats = info.pop("stats", None)
        m = D.write(out, name, recs, dict(base, **info), validate)
        if stats is not None:
            m["rejects"] = {"proposed": stats["proposed"], "rejected": stats["rejected"],
                            "by_reason": {k: v for k, v in sorted(stats.items()) if k.startswith("reject ")}}
            (out / name / "MANIFEST.json").write_text(json.dumps(m, indent=1, sort_keys=True), encoding="utf-8")
        mans[name] = m
        print(f"{name}: {m['n_groups']} groups, {m['n_records']} records, "
              f"shortcuts {m['shortcut_validation']['result']}")

    # held-out classes: triplets, and missing twins of the first groups
    st = Counter()
    test_specs = D.sample_specs(rules("l2_rules"), n["test_L2"], "test_L2")
    emit("test_L2", (r for g in D.groups(test_specs, "test", SET, "L2", st) for r in g),
         {"split": "test", "level": "L2", "rules": fold["l2_rules"], "classes": fold["l2_classes"],
          "templates": "test", "stats": st}, validate=True)
    core = a.fold != 1          # folds 2-3: test_L2, dev and the blocks/triplets corpora only
    if not core:
        emit("missing", D.missing_set(D.groups(test_specs[:n["missing"]], "test", SET, "L2", missing=True)),
             {"split": "test", "level": "L2", "templates": "test",
              "note": "missing twins of the first test_L2 groups (same tids) + one base or flip case each"})

    # development: training rules, test templates
    st = Counter()
    dev_specs = D.sample_specs(rules("train_rules"), n["dev"], "dev")
    emit("dev", (r for g in D.groups(dev_specs, "dev", SET, "L0", st, "test") for r in g),
         {"split": "dev", "level": "L0", "templates": "test", "stats": st}, validate=True)
    if not core:
        emit("dev_missing", D.missing_set(D.groups(dev_specs, "dev", SET, "L0", tpl_split="test",
                                                   missing=True)),
             {"split": "dev", "level": "L0", "templates": "test",
              "note": "threshold set for MR at 5% false rejection; missing twins of the dev groups"})
        ladder_and_diagnostics(emit, rules, n, SET)
        diversity(emit, F, fold, a.scale, SET)

    # training corpora: one group pool, training rules, train templates
    pool = D.sample_specs(rules("train_rules"), max(int(POOL * a.scale), 14 * 200), "train")
    for kind in (("blocks", "triplets") if core else D.CORPORA):
        st = Counter()
        emit(f"train_{kind}", D.corpus(kind, pool, n["train"], SET, st),
             {"split": "train", "level": "L0", "templates": "train", "corpus": kind, "stats": st})
    if not core:
        ablations(emit, pool, n, SET)
        experiments(emit, rules, pool, n, SET)
    missing_names = only - set(mans)
    if missing_names:
        sys.exit(f"unknown set names in --only: {sorted(missing_names)}")

    for name, m in mans.items():
        registry[f"{SET}/{name}"] = {
            "path": f"{SET}/{name}/records.jsonl", "split": m["split"], "level": m["level"],
            "tier": "mixed", "n_groups": m["n_groups"], "n_records": m["n_records"],
            "manifest": f"{SET}/{name}/MANIFEST.json", "frozen": a.freeze, "created": created,
            "sha256": m["sha256"]}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    bad = [k for k, m in mans.items() if m["shortcut_validation"]["result"] == "FAIL"]
    if bad:
        sys.exit(f"shortcut validation FAILED: {bad}")


if __name__ == "__main__":
    main()
