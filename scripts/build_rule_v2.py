"""Build, validate and register rule_v2: the stage-2 training library (STAGE2_TASKS_A, A5).

  python scripts/build_rule_v2.py --only dev               # one set (in memory unless --freeze)
  python scripts/build_rule_v2.py --freeze [--only ...]    # write records, manifests, registry
  python scripts/build_rule_v2.py --restore --only test_L2

rule_v1 is untouched. Two sources feed every set:
  v1 part   rule_v1's rule library and fold 1 (training rules; classes held out for L2), new cases from
            rule_v1's engine with new seeds: near-miss kinds numeric, boundary, subject, negation, time
  v2 part   rules of selrm/engine2.py with window and class conditions over the TRAINING classes of onto_v1:
            near-miss kinds window and class, and subject, negation, time on those conditions
Every record is in the stage-2 format (ledger entries with concept and the applies bit; struct; crit; cluster).
Sets: train_blocks, train_triplets (60,000 records each, same groups, differing in near-misses),
train_triplets_lo_window, train_triplets_lo_class, dev (300 groups, training rules, test templates),
test_L2 (2,000 groups, held-out classes of both parts, test templates).
"""
import argparse
import collections
import datetime
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import cls as C  # noqa: E402
from selrm import datasets as D  # noqa: E402
from selrm import engine as E1  # noqa: E402
from selrm import engine2 as E  # noqa: E402
from selrm import rules as R  # noqa: E402
from selrm import rules_grammar as RG  # noqa: E402
from selrm.library import LIBRARY_BY_ID  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

SET, SEED = "rule_v2", 20261009
N_TRAIN, N_DEV, N_TEST = 60000, 300, 2000
V2_BLOCKS = (1, 3, 5)                  # of every 7 blocks of 14 groups, these three come from the v2 part
V2_CLASSES = ("single|window", "single|class", "any|class+window", "any|class+class", "any|window+window",
              "all|class+window", "all|class+class", "all|window+window")
RULES_PER_CLASS = 30
WINDOWS = {"days": (7, 10, 14, 21, 28, 30, 45, 60, 90), "months": (1, 2, 3, 4, 6, 9, 12, 18, 24), "years": (1, 2, 3, 5, 10)}
NM_W = {"window": (("window", 0.7), ("negation", 0.15), ("subject", 0.15)),
        "class": (("class", 0.7), ("negation", 0.1), ("subject", 0.1), ("time", 0.1))}


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


# ---- v2 part: rules --------------------------------------------------------------------------------------
def v2_rules():
    """{signature class: [Rule2]} over the training classes of onto_v1, seeded."""
    rng = random.Random(f"{SEED}/rules")
    pool = [x for d in ("drug", "phenotype", "disease") for x in C.conditions("train", d)]
    out = {}
    for sig in V2_CLASSES:
        op, kinds = sig.split("|")
        rules, seen = [], set()
        while len(rules) < RULES_PER_CLASS:
            conds = []
            for i, k in enumerate(kinds.split("+")):
                if k == "window":
                    unit = rng.choice(sorted(WINDOWS))
                    conds.append(E.Cond(f"c{i + 1}", "window", rng.choice(sorted(E.EVENTS)), n=rng.choice(WINDOWS[unit]), unit=unit))
                else:
                    c = rng.choice(pool)[0]
                    conds.append(E.Cond(f"c{i + 1}", "class", c.key, domain=c.domain, name=c.name, members=c.members, near=c.near))
            key = tuple((c.kind, c.key, c.n, c.unit) for c in conds)
            if len({c.key for c in conds}) < len(conds) or key in seen:
                continue
            names = [n.lower() for c in conds if c.kind == "class" for _, ns in c.members for n in ns] + \
                    [n.lower() for c in conds if c.kind == "class" for _, n, _ in c.near] + \
                    [k for c in conds if c.kind == "window" for k in E.EVENTS[c.key][4]]
            sc = [s for s in RG.SCENARIOS if not any(n in " ".join(map(str, s[:4])).lower() for n in names if len(n) > 3)]
            intro, default, alt, setting, sex, ages = rng.choice(sc)
            seen.add(key)
            rules.append(E.Rule2(f"w{V2_CLASSES.index(sig)}{len(rules):02d}", "all" if op == "all" else "any", tuple(conds),
                                 intro, default, alt, setting, sex, ages, family=f"v2_{sig}"))
        out[sig] = rules
    return out


def v2_held_out():
    """Two of the six two-condition signature classes, seeded, are held out for test_L2."""
    two = [s for s in V2_CLASSES if "+" in s]
    return sorted(random.Random(f"{SEED}/l2").sample(two, 2))


def v2_specs(rules, n, seed, drop=(), only=None, target=None):
    """n specs (rule, cid, near-miss kind, tier) with window and class targets in equal shares."""
    rng = random.Random(f"{SEED}/specs/{seed}")
    targets = {"window": [(r, c) for r in rules for c in r.conds if c.kind == "window"],
               "class": [(r, c) for r in rules for c in r.conds if c.kind == "class"]}
    out = []
    for i in range(n):
        kind = target or ("window", "class")[i % 2]
        r, c = rng.choice(targets[kind])
        kinds = [(k, w) for k, w in NM_W[kind] if k not in drop and (only is None or k in only)]
        nm = rng.choices([k for k, _ in kinds], [w for _, w in kinds])[0]
        out.append((r, c.cid, nm, rng.choice(("easy", "easy", "long"))))
    rng.shuffle(out)
    return out


def v2_groups(specs, split, level, tpl_split, stats, start=0):
    for i, (r, cid, nm, tier) in enumerate(specs):
        yield E.make_group(r, cid, nm, tier, split, start + i, SET, level, tpl_split=tpl_split, stats=stats)


# ---- v1 part: records of rule_v1's engine in the stage-2 format ------------------------------------------
def to_stage2(rec):
    rule = D.RULES_BY_ID[rec["rid"]]
    c = rule.crit(rec["cid"])
    thr = (rec["meta"].get("overrides") or {}).get(c.cid, c.threshold)
    ms = [R.Mention(**m) for m in rec["state"] if m["concept"] == c.concept]
    entries = []
    for i, e in enumerate(rec["ledger"]):
        m = ms[i] if e["found"] != "not mentioned" and i < len(ms) else None
        ok = bool(m and c.applies(m) and m.status == "present" and (c.kind == "finding" or R.OPS[c.op](m.value, thr)))
        entries.append({**{k: e[k] for k in E.LEDGER2_KEYS[:5]}, "concept": "", "applies": "yes" if ok else "no"})
    out = dict(rec, ledger=entries, cluster=rec["rid"],
               crit={"source": "stated", "provenance": "generated rule (selrm.engine, rule_v1 library)", "text_sha": sha(rec["rule_text"])},
               struct={"kind": c.kind, "concept": c.concept, "op": c.op, "threshold": thr,
                       "subject": "patient or first-degree relative" if c.counts_family else "patient",
                       "time": "ever" if c.counts_past else "current"})
    E.validate2(out)
    return out


def v1_groups(specs, split, level, tpl_split, stats, missing):
    for g in D.groups(specs, split, SET, level, stats, tpl_split, missing):
        yield [to_stage2(r) for r in g]


# ---- sets -------------------------------------------------------------------------------------------------
def corpus(kind, v1_specs, v2_spec_list, n_records, stats):
    """Blocks of 14 groups with the case pattern of selrm.datasets.CORPORA[kind]; blocks 1, 3 and 5 of every 7
    come from the v2 part. The same specs give train_blocks and train_triplets the same groups."""
    size, pattern = D.CORPORA[kind]
    g1 = v1_groups(v1_specs, "train", "L0", None, stats["v1"], True)
    g2 = v2_groups(v2_spec_list, "train", "L0", None, stats["v2"])
    n = b = 0
    while True:
        gen = g2 if b % 7 in V2_BLOCKS else g1
        for want in pattern(random.Random(f"{kind}.{b}")):
            for r in next(gen):
                if r["case_kind"] in want:
                    yield r
                    n += 1
        b += 1
        if n >= n_records:
            return


def no_missing(groups):
    for g in groups:
        yield [r for r in g if r["case_kind"] != "missing"]


def scorers():
    def named(r):
        if r["rid"] in D.RULES_BY_ID:
            kws = D.RULES_BY_ID[r["rid"]].crit(r["cid"]).keywords
            return any(k in r["case_text"].lower() for k in kws)
        return r["ledger"][0]["found"] != "not mentioned"
    return {"always_default": lambda r: float(r["claim_role"] == "s"),
            "concept_named": lambda r: float((r["claim_role"] == "s_prime") == named(r)),
            "program": lambda r: float(r["label"])}


def validate(recs):
    out = {}
    for name, fn in scorers().items():
        S = summarise(decisions(recs, [fn(r) for r in recs]), by=("nm_kind",))
        out[name] = {k: {m: round(v[m], 2) for m in ("TA", "Rev", "Hold", "n")} for k, v in sorted(S.items())}
    ok = (out["program"]["all"]["TA"] == 100 and out["always_default"]["all"]["TA"] == 0
          and all(v["TA"] == 0 for k, v in out["concept_named"].items()
                  if k.split("=")[-1] in ("subject", "negation", "time", "window", "class")))
    return out, ok


def target_claim_check(recs, rules2):
    """Re-executes every label from the state: violations (must be 0)."""
    bad = 0
    for r in recs:
        if r["case_kind"] == "missing":
            bad += r["label"] != 0
            continue
        if r["rid"] in rules2:
            rule = rules2[r["rid"]]
            import datetime as dt
            ref = dt.date.fromisoformat(r["ref_date"])
            y = rule.label(r["state"], ref) if r["claim_type"] == "conclusion" else int(rule.crit(r["cid"]).evaluate(r["state"], ref))
        else:
            rule = D.RULES_BY_ID[r["rid"]]
            ms, ov = tuple(R.Mention(**m) for m in r["state"]), r["meta"].get("overrides") or {}
            y = rule.label(ms, r["cid"], ov) if r["claim_type"] == "conclusion" else int(rule.crit(r["cid"]).evaluate(ms, ov.get(r["cid"])))
        bad += r["label"] != int((r["claim_role"] == "s_prime") == (y == 1))
    return bad


def describe(recs):
    groups = {}
    for r in recs:
        groups.setdefault(r["tid"], r)
    c = lambda f: dict(sorted(collections.Counter(str(f(r)) for r in groups.values()).items()))  # noqa: E731
    cases = collections.Counter(r["case_kind"] for r in recs if r["claim_role"] == "s" and r["claim_type"] == "conclusion")
    tot = sum(cases.values())
    return {"records": len(recs), "groups": len(groups), "rules": len({r["rid"] for r in recs}),
            "labels": dict(collections.Counter(str(r["label"]) for r in recs)), "by_nm_kind": c(lambda r: r["nm_kind"]),
            "by_family": c(lambda r: r["family"]), "by_tier": c(lambda r: r["tier"]),
            "by_part": c(lambda r: "v2" if r["rid"].startswith("w") else "v1"),
            "cases_by_kind": dict(cases), "case_share": {k: round(v / tot, 4) for k, v in cases.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--scale", type=float, default=1.0)
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    only = set(filter(None, a.only.split(",")))
    folds = json.loads((ROOT / "data/rule_v1/FOLDS.json").read_text(encoding="utf-8"))["folds"]["1"]
    train_rules = [LIBRARY_BY_ID[r] for r in folds["train_rules"]]
    l2_rules = [LIBRARY_BY_ID[r] for r in folds["l2_rules"]]
    by_sig = v2_rules()
    held = v2_held_out()
    v2_train = [r for s, rs in by_sig.items() if s not in held for r in rs]
    v2_test = [r for s in held for r in by_sig[s]]
    rules2 = {r.rid: r for rs in by_sig.values() for r in rs}
    n_train = int(N_TRAIN * a.scale)
    pool1 = D.sample_specs(train_rules, int(3600 * a.scale) + 28, f"{SEED}.train")
    pools2 = {"": v2_specs(v2_train, int(2800 * a.scale) + 42, "train"),
              "lo_window": v2_specs(v2_train, int(2800 * a.scale) + 42, "train", drop=("window",)),
              "lo_class": v2_specs(v2_train, int(2800 * a.scale) + 42, "train", drop=("class",))}
    n_test, n_dev = int(N_TEST * a.scale), int(N_DEV * a.scale)

    def test_l2(stats):
        yield from no_missing(v1_groups(D.sample_specs(l2_rules, int(0.6 * n_test), f"{SEED}.test_L2"), "test", "L2", None, stats["v1"], False))
        q = int(0.4 * n_test)
        k = int(q * 0.36)                                   # window and class near-misses: 36% of the v2 part each
        specs = (v2_specs(v2_test, k, "test.window", only=("window",), target="window")
                 + v2_specs(v2_test, k, "test.class", only=("class",), target="class")
                 + v2_specs(v2_test, q - 2 * k, "test.other", drop=("window", "class")))
        yield from no_missing(v2_groups(specs, "test", "L2", None, stats["v2"]))

    def dev(stats):
        yield from no_missing(v1_groups(D.sample_specs(train_rules, int(0.7 * n_dev), f"{SEED}.dev"), "dev", "L0", "test", stats["v1"], False))
        yield from no_missing(v2_groups(v2_specs(v2_train, n_dev - int(0.7 * n_dev), "dev"), "dev", "L0", "test", stats["v2"]))

    def flat(gen):
        return (r for g in gen for r in g)
    sets = {
        "dev": lambda st: flat(dev(st)),
        "test_L2": lambda st: flat(test_l2(st)),
        "train_blocks": lambda st: corpus("blocks", pool1, pools2[""], n_train, st),
        "train_triplets": lambda st: corpus("triplets", pool1, pools2[""], n_train, st),
        "train_triplets_lo_window": lambda st: corpus("triplets", pool1, pools2["lo_window"], n_train, st),
        "train_triplets_lo_class": lambda st: corpus("triplets", pool1, pools2["lo_class"], n_train, st),
    }
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    today = datetime.date.today().isoformat()
    for name, make in sets.items():
        if only and name not in only:
            continue
        key = f"{SET}/{name}"
        if registry.get(key, {}).get("frozen") and not a.restore:
            print(f"{key}: frozen, skipped")
            continue
        st = {"v1": collections.Counter(), "v2": collections.Counter()}
        recs = list(make(st))
        info = describe(recs)
        info["target_claim_violations"] = target_claim_check(recs, rules2)
        info["rejects"] = {p: {"proposed": c["proposed"], "rejected": c["rejected"]} for p, c in st.items()}
        if name in ("dev", "test_L2"):
            info["shortcut_validation"], ok = validate(recs)
        else:
            ok = True
        ok = ok and info["target_claim_violations"] == 0
        print(name, {k: info[k] for k in ("records", "groups", "rules", "by_nm_kind", "by_part", "case_share", "target_claim_violations", "rejects")},
              "PASS" if ok else "FAIL", flush=True)
        text = "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in recs)
        if a.restore:
            if sha(text) != registry[key]["sha256"]:
                sys.exit(f"{key}: rebuild does not match the frozen sha256")
            (ROOT / "data" / registry[key]["path"]).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / "data" / registry[key]["path"]).write_text(text, encoding="utf-8", newline="\n")
            continue
        if not a.freeze or a.scale != 1.0:
            continue
        if not ok:
            sys.exit(f"{key}: not frozen, checks failed")
        d = ROOT / "data" / SET / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
        split = "train" if name.startswith("train") else "dev" if name == "dev" else "test"
        man = {"set": SET, "name": name, "created": today, "seed": SEED, "split": split, "sha256": sha(text), **info,
               "templates": "train" if split == "train" else "test",
               "v1_part": "rule_v1 library, fold 1 (data/rule_v1/FOLDS.json): training rules for train and dev, L2 rules for test_L2; cases from selrm.engine with new seeds",
               "v2_part": {"engine": "selrm/engine2.py", "signature_classes": list(V2_CLASSES), "held_out_for_test_L2": held,
                           "rules_per_class": RULES_PER_CLASS, "classes": "training classes of onto_v1", "windows": WINDOWS,
                           "onto_v1_classes_sha256": json.loads((ROOT / "data/onto_v1/MANIFEST.json").read_text(encoding="utf-8"))["classes_sha256"]},
               "format": "stage 2: ledger entries (need, found, subject, status, time, concept, applies); struct; crit; cluster = rule id; ref_date on v2 records",
               "analysis_plan_sha256": hashlib.sha256((ROOT / "docs/ANALYSIS_PLAN_STAGE2.md").read_bytes()).hexdigest()}
        (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
        registry[key] = {"path": f"{SET}/{name}/records.jsonl", "split": split, "level": "L2" if name == "test_L2" else "L0", "tier": "mixed",
                         "n_groups": info["groups"], "n_records": info["records"], "sha256": sha(text),
                         "manifest": f"{SET}/{name}/MANIFEST.json", "created": today, "frozen": True}
        reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
        print("frozen:", key, flush=True)


if __name__ == "__main__":
    main()
