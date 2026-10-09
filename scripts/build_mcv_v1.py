"""Build, validate and register mcv_v1 (MedCalc-V; STAGE2_TASKS_A, A1).

  python scripts/build_mcv_v1.py                    # build in memory, print counts and validation
  python scripts/build_mcv_v1.py --filter dev       # run the fidelity filter (API, cached) on the dev edits
  python scripts/build_mcv_v1.py --filter test      # ... on the test edits (after the prompts are fixed)
  python scripts/build_mcv_v1.py --freeze           # write records, manifest, registry (needs both filters)
  python scripts/build_mcv_v1.py --restore          # rewrite the frozen records if the rebuild matches

Portions: criteria_test, natural_band_test, edits_test, ruleside_test (test notes); dev (20% of the training
notes, all item types); adapt_blocks and adapt_triplets (the other training notes, scores not held out).
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
from selrm import mcv  # noqa: E402
from selrm import schema  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402
from selrm.mcv import edits as E  # noqa: E402
from selrm.mcv import fidelity as F  # noqa: E402
from selrm.mcv import items as I  # noqa: E402

SET = "mcv_v1"
SEED = 20261008
HELD_OUT = 6                 # scores held out of both adaptation corpora
ADAPT_RECORDS = 12000
MIN_NOTE = 400               # training notes shorter than this are fragments and are left out
OUT = ROOT / "data" / SET
FID = OUT / "FIDELITY.jsonl"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_training(train, test):
    """(dev rows, adaptation rows, drop counts): deduplicated against test by note id and text hash."""
    ids, texts = {r["Note ID"] for r in test}, {sha(r["Patient Note"]) for r in test}
    drops = collections.Counter()
    dev, adapt = [], []
    for r in train:
        if r["Note ID"] in ids:
            drops["note id occurs in test"] += 1
        elif sha(r["Patient Note"]) in texts:
            drops["note text occurs in test"] += 1
        elif len(r["Patient Note"]) < MIN_NOTE:
            drops[f"note shorter than {MIN_NOTE} characters"] += 1
        elif int(sha(f"{SEED}/{r['Note ID']}"), 16) % 5 == 0:
            dev.append(r)
        else:
            adapt.append(r)
    return dev, adapt, dict(drops)


def held_out(specs):
    cids = sorted(specs)
    random.Random(SEED).shuffle(cids)
    return sorted(cids[:HELD_OUT])


def portion(rows, specs, defs, ranges, units, lexicon, split):
    c = I.criteria(rows, specs, defs, split)
    v, vs = I.value_edits(rows, specs, defs, ranges, units, split)
    s, ss = E.sentence_edits(rows, specs, defs, lexicon, split)
    r, rs = E.ruleside(rows, specs, defs, ranges, split)
    return {"criteria": c, "natural_band": I.natural_band(c, rows, specs), "edits": v + s, "ruleside": r,
            "skips": {"value": vs, "sentence": ss, "ruleside": rs}}


def groups(recs):
    g = collections.OrderedDict()
    for r in recs:
        g.setdefault(r["tid"], []).append(r)
    return g


def adaptation(edit_recs):
    """(blocks, triplets): the same groups and flip cases; the triplets corpus has a near-miss in place of
    the base case in every second group. At most one sentence group per note and item."""
    g = groups(edit_recs)
    one = {}
    for tid, recs in g.items():
        m = recs[0]["meta"]
        key = (m["row"], recs[0]["cid"], recs[0]["edit_type"], m.get("input"))
        if key not in one or sha(f"{SEED}/{tid}") < sha(f"{SEED}/{one[key]}"):
            one[key] = tid
    tids = sorted(one.values())
    random.Random(SEED).shuffle(tids)
    tids = tids[:ADAPT_RECORDS // 4]
    blocks, triplets = [], []
    for n, tid in enumerate(tids):
        by = {k: [r for r in g[tid] if r["case_kind"] == k] for k in ("base", "flip", "near")}
        blocks += by["base"] + by["flip"]
        triplets += (by["near"] if n % 2 else by["base"]) + by["flip"]
    for name, recs in (("adapt_blocks", blocks), ("adapt_triplets", triplets)):
        for r in recs:
            r["split"] = "train"
    return blocks, triplets


# ---- validation -------------------------------------------------------------------------------------------
def scorers(train_criteria, lexicon):
    """Shortcut scorers: u(claim), higher = claim judged correct."""
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.linear_model import LogisticRegression
    vec = CountVectorizer(ngram_range=(1, 2), min_df=2)
    X = vec.fit_transform([r["claim_text"] for r in train_criteria])
    lr = LogisticRegression(max_iter=2000, C=1.0).fit(X, [r["label"] for r in train_criteria])

    def claim_only(recs):
        return [float(x) for x in lr.predict_proba(vec.transform([r["claim_text"] for r in recs]))[:, 1]]

    def named(r):
        if r["struct"]["kind"] != "finding":
            return True                                  # a numeric input is named in every case
        entry = lexicon.get(r["meta"]["calculator_id"], {}).get(r["condition"])
        return bool(entry) and not E.silent(r["case_text"], entry)

    def concept_named(recs):                             # prefers the claim with points iff the concept is named
        return [float((r["meta"]["claimed_points"] != 0) == named(r)) for r in recs]

    def attribute_blind(recs):                           # reads values, ignores subject, status and time
        return [float(r["label"]) if r.get("edit_type") == "value" or r["struct"]["kind"] != "finding"
                else float((r["meta"]["claimed_points"] != 0) == named(r)) for r in recs]

    def ignores_rule_change(recs):                       # answers every rule-side item as under the original text
        orig = {(r["meta"]["xr"]["item"], r["claim_role"]): r["label"] for r in recs
                if "xr" in r["meta"] and r["meta"]["xr"]["variant"] == "orig"}
        return [float(orig[(r["meta"]["xr"]["item"], r["claim_role"])]) if "xr" in r["meta"] else float(r["label"])
                for r in recs]

    return {"always_default": lambda recs: [float(r["claim_role"] == "s") for r in recs],
            "always_no_points": lambda recs: [float(r["meta"]["claimed_points"] == 0) for r in recs],
            "ignores_rule_change": ignores_rule_change, "claim_only": claim_only, "concept_named": concept_named, "attribute_blind": attribute_blind,
            "rule_code": lambda recs: [float(r["label"]) for r in recs]}


def balanced_accuracy(recs, u):
    """Mean of the accuracy on items that score points and on items that score none (ties are wrong)."""
    d = {}
    for r, x in zip(recs, u):
        d.setdefault(r["tid"], {})[r["claim_role"]] = (x, r)
    acc = {True: [], False: []}
    for v in d.values():
        acc[v["s"][1]["meta"]["points"] != 0].append(v["s"][0] > v["s_prime"][0])
    return round(50 * (sum(acc[True]) / len(acc[True]) + sum(acc[False]) / len(acc[False])), 2)


def crossed(recs, u):
    right = collections.defaultdict(list)
    d = {}
    for r, x in zip(recs, u):
        d.setdefault(r["tid"], {})[r["claim_role"]] = (x, r)
    for v in d.values():
        r = v["s"][1]
        diff = v["s"][0] - v["s_prime"][0]
        right[r["meta"]["xr"]["item"]].append(diff > 0 if r["label"] == 1 else diff < 0)
    return round(100 * sum(all(v) for v in right.values()) / len(right), 2) if right else None


def validate(P, fns):
    out = {}
    for name, fn in fns.items():
        row = {"criteria_test_balanced_accuracy": balanced_accuracy(P["criteria"], fn(P["criteria"]))}
        if P["edits"]:
            S = summarise(decisions(P["edits"], fn(P["edits"]), claim_type="criterion"), by=())["all"]
            row.update({f"edits_test_{k}": round(S[k], 2) for k in ("TA", "Rev", "Hold")})
            for et in ("value", "sentence"):
                sub = [r for r in P["edits"] if r["edit_type"] == et]
                if sub:
                    row[f"edits_test_TA_{et}"] = round(summarise(decisions(sub, fn(sub), claim_type="criterion"), by=())["all"]["TA"], 2)
        row["ruleside_test_XA"] = crossed(P["ruleside"], fn(P["ruleside"]))
        out[name] = row
    return out


def counts(recs):
    s = [r for r in recs if r["claim_role"] == "s" and r["case_kind"] in ("base", "contested")]
    c = lambda key: dict(sorted(collections.Counter(str(key(r)) for r in s).items()))  # noqa: E731
    return {"records": len(recs), "groups": len({r["tid"] for r in recs}), "notes": len({r["cluster"] for r in recs}),
            "by_score": c(lambda r: r["rid"]), "by_note_type": c(lambda r: r["note_type"]),
            "by_stratum": c(lambda r: r["stratum"]), "by_edit_type": c(lambda r: r.get("edit_type", "none")),
            "by_nm_kind": c(lambda r: r["nm_kind"]), "items_with_points": sum(r["meta"]["points"] != 0 for r in s),
            "by_item": c(lambda r: r["rid"] + "/" + r["cid"])}


def apply_filter(edit_recs, verdicts):
    keep = [r for r in edit_recs if verdicts[r["tid"]]["keep"]]
    n = len({r["tid"] for r in edit_recs})
    return keep, {"triplets": n, "kept": len({r["tid"] for r in keep}),
                  "retention": round(len({r["tid"] for r in keep}) / n, 4) if n else None}


def lines(recs):
    return "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in recs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--filter", choices=("dev", "test"))
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()

    test, train = mcv.rows("test"), mcv.rows("train")
    specs = mcv.load_scores()
    accepted = {cid: s for cid, s in specs.items()
                if all(s.total(r["ent"]) == r["answer"] for r in test + train if r["cid"] == cid)}
    test = [r for r in test if r["cid"] in accepted]
    train = [r for r in train if r["cid"] in accepted]
    defs = I.definitions(test + train)
    lexicon = E.load_lexicon()
    dev_rows, adapt_rows, drops = split_training(train, test)
    held = held_out(accepted)
    ranges = I.plausible(train)
    units = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in train:
        for k in r["ent"]:
            units[r["cid"]][k].add(I._unit(r["ent"], k))

    T = portion(test, accepted, defs, ranges, units, lexicon, "test")
    D = portion(dev_rows, accepted, defs, ranges, units, lexicon, "dev")
    A = portion([r for r in adapt_rows if r["cid"] not in held], accepted, defs, ranges, units, lexicon, "train")
    for name, P in (("test", T), ("dev", D), ("adapt", A)):
        print(name, {k: len({r["tid"] for r in v}) for k, v in P.items() if k != "skips"}, P["skips"])

    verdicts = {}
    if FID.exists():
        for ln in open(FID, encoding="utf-8"):
            v = json.loads(ln)
            verdicts[v["tid"]] = v
    if a.filter:
        P = D if a.filter == "dev" else T
        new = F.run(P["edits"], lexicon)
        verdicts.update({tid: {"tid": tid, **v} for tid, v in new.items()})
        OUT.mkdir(parents=True, exist_ok=True)
        with open(FID, "w", encoding="utf-8", newline="\n") as f:
            for tid in sorted(verdicts):
                f.write(json.dumps(verdicts[tid], sort_keys=True, ensure_ascii=False) + "\n")
        kept = sum(v["keep"] for v in new.values())
        print(f"fidelity {a.filter}: kept {kept} of {len(new)} triplets")
        by = collections.Counter((v["reads"][0]["kind"], v["keep"]) for v in new.values())
        print(dict(by))
        return

    fid = {}
    for name, P in (("test", T), ("dev", D)):
        missing = {r["tid"] for r in P["edits"]} - set(verdicts)
        if missing:
            print(f"{name}: {len(missing)} edit triplets have no fidelity verdict yet; this portion is not final")
            fid[name] = None
        else:
            P["rejects"] = [r for r in P["edits"] if not verdicts[r["tid"]]["keep"]]
            P["edits"], fid[name] = apply_filter(P["edits"], verdicts)
    blocks, triplets = adaptation(A["edits"])
    portions = {"criteria_test": T["criteria"], "natural_band_test": T["natural_band"], "edits_test": T["edits"],
                "ruleside_test": T["ruleside"], "dev": D["criteria"] + D["edits"] + D["ruleside"],
                "adapt_blocks": blocks, "adapt_triplets": triplets}
    for recs in portions.values():
        for r in recs:
            schema.validate(r)
    val = validate(T, scorers(A["criteria"] + D["criteria"], lexicon))
    for k, v in val.items():
        print(f"{k:18s} {v}")
    info = {p: counts(recs) for p, recs in portions.items()}
    for p, c in info.items():
        print(p, {k: c[k] for k in ("records", "groups", "notes", "by_note_type", "by_edit_type")})
    ok = (val["rule_code"]["criteria_test_balanced_accuracy"] == 100 and val["rule_code"].get("edits_test_TA", 100) == 100
          and val["rule_code"]["ruleside_test_XA"] in (100, None) and val["always_default"].get("edits_test_TA", 0) == 0
          and val["always_no_points"]["criteria_test_balanced_accuracy"] == 50
          and val["ignores_rule_change"]["ruleside_test_XA"] in (0, None)
          and all(val[k].get("edits_test_TA_sentence", 0) == 0 for k in ("claim_only", "concept_named", "attribute_blind")))
    print("VALIDATION:", "PASS" if ok else "FAIL")
    if not (a.freeze or a.restore):
        return
    if not ok or fid["test"] is None or fid["dev"] is None:
        sys.exit("not frozen: validation failed or the fidelity filter has not run on both portions")

    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    texts = {p: lines(recs) for p, recs in portions.items()}
    if a.restore:
        for p, t in texts.items():
            e = registry[f"{SET}/{p}"]
            if sha(t) != e["sha256"]:
                sys.exit(f"{p}: rebuild does not match the frozen sha256")
            (ROOT / "data" / e["path"]).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / "data" / e["path"]).write_text(t, encoding="utf-8", newline="\n")
        print("restored")
        return
    if any(registry.get(f"{SET}/{p}", {}).get("frozen") for p in portions):
        sys.exit("refusing to rebuild: mcv_v1 is frozen (use --restore)")
    plan = (ROOT / "docs" / "ANALYSIS_PLAN_STAGE2.md")
    if not plan.exists():
        sys.exit("not frozen: docs/ANALYSIS_PLAN_STAGE2.md is not in this checkout (it must be on main first)")
    today = datetime.date.today().isoformat()
    manifest = {
        "set": SET, "created": today, "seed": SEED, "purpose": "MedCalc-V: criterion claims and edits on clinical notes with the score definition shipped in the instance (stage 2, comparisons 7-9)",
        "source": mcv.PIN, "analysis_plan_sha256": hashlib.sha256(plan.read_bytes()).hexdigest(),
        "scores_accepted": sorted(accepted), "scores_held_out_of_adaptation": held,
        "training_note_drops": drops, "dev_notes": len({r["Note ID"] for r in dev_rows}),
        "band": {"absolute": I.BAND_ABS, "relative": I.BAND_REL}, "templates": E.TEMPLATES, "relatives": E.RELATIVES,
        "plausible_ranges": "lowest and highest value released per score, input and unit in the training rows",
        "skips": {"test": T["skips"], "dev": D["skips"], "adapt": A["skips"]},
        "fidelity": {"extractors": list(F._api().EXTRACTORS), "params": F.PARAMS, "test": fid["test"], "dev": fid["dev"],
                     "verdicts": "data/mcv_v1/FIDELITY.jsonl", "adaptation": "not filtered (silver)"},
        "shortcut_validation": val, "portions": {},
        "note": "Labels are the rule code's points on the released (or edited) entity dictionary, relative to the score text shown. Edited notes are not real patients.",
    }
    for p, t in texts.items():
        d = OUT / p
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(t, encoding="utf-8", newline="\n")
        manifest["portions"][p] = {**info[p], "sha256": sha(t)}
        split = "test" if p.endswith("_test") else ("dev" if p == "dev" else "train")
        registry[f"{SET}/{p}"] = {"path": f"{SET}/{p}/records.jsonl", "split": split, "level": "external", "tier": "external",
                                 "n_groups": info[p]["groups"], "n_records": info[p]["records"], "sha256": sha(t),
                                 "manifest": f"{SET}/MANIFEST.json", "created": today, "frozen": True}
    rej = T.get("rejects", []) + D.get("rejects", [])
    (OUT / "REJECTED_EDITS.jsonl").write_text(lines(rej), encoding="utf-8", newline="\n")
    manifest["rejected_edits"] = {"file": "data/mcv_v1/REJECTED_EDITS.jsonl", "triplets": len({r["tid"] for r in rej})}
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print("frozen and registered:", ", ".join(portions))


if __name__ == "__main__":
    main()
