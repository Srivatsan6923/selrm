"""Build, validate and register kb_v1 (criterion from the DDXPlus lists; STAGE2_TASKS_A, A2.3-5).

  python scripts/build_kb_v1.py             # support check, triplets, validation (prints; writes the support file)
  python scripts/build_kb_v1.py --freeze    # write records, manifest, registry
  python scripts/build_kb_v1.py --restore   # rewrite the frozen records if the rebuild matches

Label pairs: the 134 (gold, trap) diagnosis pairs of MedEinst's test split (data/kb_v1/medeinst_pairs.json,
written by --pairs from role C's frozen clin_v1/medeinst_test records).
"""
import argparse
import collections
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import kb_criterion as K  # noqa: E402
from selrm import kb_triplets as T  # noqa: E402
from selrm import schema  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

SEED = 20261008
PER_PAIR = 20
POOL = 300                   # patients tried per pair, in the seeded order, to find PER_PAIR that qualify
OUT = ROOT / "data" / T.SET
PAIRS = OUT / "medeinst_pairs.json"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_pairs(src):
    c = collections.Counter()
    for ln in open(src, encoding="utf-8"):
        r = json.loads(ln)
        if r["claim_role"] == "s" and r["case_kind"] == "base":
            c[(r["meta"]["y_gt"], r["meta"]["y_bias"])] += 1
    OUT.mkdir(parents=True, exist_ok=True)
    PAIRS.write_text(json.dumps({"source": "clin_v1/medeinst_test (zhui711/MedEinst, test split)",
                                 "pairs": [[a, b, n] for (a, b), n in sorted(c.items())]}, indent=1), encoding="utf-8")
    print(len(c), "pairs")


def support(pairs):
    """Support check on the validation patients."""
    cond = K.kb()[0]
    by_a = collections.defaultdict(list)
    for a, b, _ in pairs:
        by_a[a].append(b)
    n = outside = 0
    dec = {(a, b): collections.Counter() for a, b, _ in pairs}
    for p in T.patients("validate"):
        codes = T.present(T.answers(p["evidences"]))
        listed = set(cond[p["pathology"]]["symptoms"]) | set(cond[p["pathology"]]["antecedents"])
        n += 1
        outside += bool(codes - listed)
        for b in by_a.get(p["pathology"], ()):
            d = T.decide(codes, p["pathology"], b)
            dec[(p["pathology"], b)]["own" if d == p["pathology"] else "other" if d == b else "undecided"] += 1
    rows = [{"gold": a, "trap": b, "medeinst_pairs": k, "patients": sum(dec[(a, b)].values()),
             **{x: dec[(a, b)][x] for x in ("own", "other", "undecided")},
             "share_decided_for_gold": round(dec[(a, b)]["own"] / max(1, sum(dec[(a, b)].values())), 4)} for a, b, k in pairs]
    tot = sum(r["patients"] for r in rows)
    return {"validation_patients": n, "share_with_a_finding_outside_the_pathology_list": round(outside / n, 4),
            "pairs": len(rows), "patient_pair_judgments": tot,
            "share_decided_for_gold": round(sum(r["own"] for r in rows) / tot, 4),
            "share_decided_for_trap": round(sum(r["other"] for r in rows) / tot, 4),
            "share_undecided": round(sum(r["undecided"] for r in rows) / tot, 4),
            "pairs_with_no_exclusive_finding_for_gold": sum(not K.lists(a, b)[0] for a, b, _ in pairs),
            "pairs_with_no_exclusive_finding_for_trap": sum(not K.lists(a, b)[1] for a, b, _ in pairs),
            "by_pair": rows}


def build(split_file, split, pairs):
    """Up to PER_PAIR qualifying patients per label pair, the first in a seeded order of the patients."""
    by_a = collections.defaultdict(list)
    for a, b, _ in pairs:
        by_a[a].append(b)
    cand = collections.defaultdict(list)
    for p in T.patients(split_file):                     # keep only the POOL first patients of the seeded order
        for b in by_a.get(p["pathology"], ()):
            c = cand[(p["pathology"], b)]
            c.append((T._h(SEED, split, p["pathology"], b, p["pid"]), p))
            if len(c) > 2 * POOL:
                c.sort(key=lambda x: x[0])
                del c[POOL:]
    recs, per_pair = [], {}
    for a, b, _ in pairs:
        ps = [p for _, p in sorted(cand[(a, b)], key=lambda x: x[0])[:POOL]]
        n = 0
        for p in ps:
            r = T.records(p, a, b, split, SEED)
            if r:
                recs += r
                n += 1
                if n == PER_PAIR:
                    break
        per_pair[f"{a} -> {b}"] = n
    return recs, per_pair


def scorers():
    def named(r):                                        # a trap-only question occurs in the case
        ev = K.kb()[1]
        return any(ev[c]["question_en"] in r["case_text"] for c in r["struct"]["only_b"])

    def procedure(r):                                    # the executor reads the case text
        codes = T.read_case(r["case_text"])
        d = T.decide(codes, r["meta"]["pathology"], r["meta"]["other"])
        return float(d == (r["meta"]["pathology"] if r["claim_role"] == "s" else r["meta"]["other"]))
    return {"always_gold": lambda r: float(r["claim_role"] == "s"),
            "concept_named": lambda r: float((r["claim_role"] == "s_prime") == named(r)),
            "claim_only": lambda r: float(len(r["claim_text"]) % 7) / 7,     # any function of the claim alone
            "procedure_on_text": procedure}


def validate(recs):
    out = {}
    for name, fn in scorers().items():
        S = summarise(decisions(recs, [fn(r) for r in recs]), by=("nm_kind",))
        out[name] = {k: {m: round(v[m], 2) for m in ("TA", "Rev", "Hold", "n")} for k, v in sorted(S.items())}
    ok = (out["procedure_on_text"]["all"]["TA"] == 100
          and all(out[k]["all"]["TA"] == 0 for k in ("always_gold", "concept_named", "claim_only")))
    return out, ok


def counts(recs, per_pair):
    base = [r for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s"]
    return {"records": len(recs), "groups": len(base), "patients": len({r["cluster"] for r in recs}),
            "pairs_with_triplets": sum(n > 0 for n in per_pair.values()), "pairs": len(per_pair),
            "by_nm_kind": dict(collections.Counter(r["nm_kind"] for r in base)),
            "flip_scope": dict(collections.Counter("+".join(r["meta"]["flip_scope"]) for r in base)),
            "patients_per_pair": per_pair}


def lines(recs):
    return "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in recs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", help="path of clin_v1/medeinst_test/records.jsonl: write the pair list and stop")
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    if a.pairs:
        return write_pairs(a.pairs)
    pairs = json.loads(PAIRS.read_text(encoding="utf-8"))["pairs"]
    portions, info, val, ok = {}, {}, {}, True
    for name, split_file, split in (("triplets_dev", "validate", "dev"), ("triplets_test", "test", "test")):
        recs, per_pair = build(split_file, split, pairs)
        for r in recs:
            schema.validate(r)
        portions[name], info[name] = recs, counts(recs, per_pair)
        val[name], good = validate(recs)
        ok = ok and good
        print(name, {k: v for k, v in info[name].items() if k != "patients_per_pair"})
        for k, v in val[name].items():
            print(f"  {k:18s} {v}")
    print("VALIDATION:", "PASS" if ok else "FAIL")
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    texts = {p: lines(r) for p, r in portions.items()}
    if a.restore:
        for p, t in texts.items():
            e = registry[f"{T.SET}/{p}"]
            if sha(t) != e["sha256"]:
                sys.exit(f"{p}: rebuild does not match the frozen sha256")
            (ROOT / "data" / e["path"]).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / "data" / e["path"]).write_text(t, encoding="utf-8", newline="\n")
        return print("restored")
    sup = support(pairs)
    print({k: v for k, v in sup.items() if k != "by_pair"})
    (OUT / "SUPPORT.json").write_text(json.dumps(sup, indent=1), encoding="utf-8")
    if not a.freeze:
        return
    if not ok:
        sys.exit("not frozen: validation failed")
    if any(registry.get(f"{T.SET}/{p}", {}).get("frozen") for p in portions):
        sys.exit("refusing to rebuild: kb_v1 is frozen (use --restore)")
    plan = ROOT / "docs" / "ANALYSIS_PLAN_STAGE2.md"
    if not plan.exists():
        sys.exit("not frozen: docs/ANALYSIS_PLAN_STAGE2.md is not in this checkout")
    today = datetime.date.today().isoformat()
    files = {}
    for f in sorted(K.EXT.glob("release_*")):
        files[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
    manifest = {"set": T.SET, "created": today, "seed": SEED, "source": K.PIN, "files_sha256": files,
                "analysis_plan_sha256": hashlib.sha256(plan.read_bytes()).hexdigest(),
                "purpose": "Knowledge-base triplets: DDXPlus patients edited by script, criterion rendered from the DDXPlus lists (stage 2, secondary analysis 8); the renderer serves comparison (11)",
                "procedure": K.PROCEDURE, "patients_per_pair": PER_PAIR, "label_pairs": str(PAIRS.relative_to(ROOT)),
                "support_check": {k: v for k, v in sup.items() if k != "by_pair"}, "support_file": "data/kb_v1/SUPPORT.json",
                "shortcut_validation": val, "portions": {},
                "note": "Labels are relative to the lists and their procedure, not to clinical truth. Flip cases are not real patients: findings listed for the gold diagnosis only are removed and findings listed for the other only are added. Lines about a relative use the prefix 'About the patient's <relative>: '."}
    for p, t in texts.items():
        (OUT / p).mkdir(parents=True, exist_ok=True)
        (OUT / p / "records.jsonl").write_text(t, encoding="utf-8", newline="\n")
        manifest["portions"][p] = {**info[p], "sha256": sha(t)}
        registry[f"{T.SET}/{p}"] = {"path": f"{T.SET}/{p}/records.jsonl", "split": "dev" if p.endswith("dev") else "test",
                                   "level": "external", "tier": "external", "n_groups": info[p]["groups"],
                                   "n_records": info[p]["records"], "sha256": sha(t), "manifest": f"{T.SET}/MANIFEST.json",
                                   "created": today, "frozen": True}
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print("frozen and registered:", ", ".join(portions))


if __name__ == "__main__":
    main()
