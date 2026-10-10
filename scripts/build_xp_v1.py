"""Build, validate and register xp_v1: program-preserving paraphrases of the rule text for 300 groups of
rule_v1/test_L2 (STAGE2_TASKS_A, A3; analysis plan, secondary 6).

  python scripts/build_xp_v1.py [--freeze | --restore]

Only the rule text changes; cases, claims, labels, tids and iids are those of rule_v1/test_L2, so a system's
verdicts on the two sets pair by iid. Groups are drawn from the grammar-sampled rules with two or more
conditions (their clause structure is known from the generator). Three transformations, all applied:
  reorder   the conditions in another order (commutative under any, all, at-least-two and score rules)
  move      the exception clause moved in front of the default ("prescribe A if ...; otherwise prescribe D")
  synonyms  words of the frame exchanged (list SYNONYMS; none is a rule_v1 cue phrase)
Check: the rule program rebuilt with the reordered conditions gives the same output as the original program
on every state of the group, and that output is the record's label.
"""
import argparse
import datetime
import hashlib
import json
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import phrases as P  # noqa: E402
from selrm import rules as R  # noqa: E402
from selrm import rules_grammar as RG  # noqa: E402
from selrm import schema  # noqa: E402

SET, SEED, N = "xp_v1", 20261008, 300
PARENT = "rule_v1/test_L2"
SYNONYMS = (("prescribe", "give"), ("at least two of the following apply", "two or more of the following hold"),
            ("the score is", "the total is"), ("Score", "Count"))


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def structures():
    """{rid: (family, intro, default, alternative, [(criterion, phrase)], cutoff, kwargs)} of the sampled
    rules, captured by re-running the generator; every captured rule must equal the library's rule."""
    seen, orig = {}, RG.G

    def spy(rid, family, title, intro, default, alternative, conds, setting, cutoff=None, **kw):
        seen[rid] = (family, title, intro, default, alternative, list(conds), setting, cutoff, kw)
        return orig(rid, family, title, intro, default, alternative, conds, setting, cutoff=cutoff, **kw)
    RG.G = spy
    try:
        again = {r.rid: r for r in RG.sample_rules()}
    finally:
        RG.G = orig
    lib = {r.rid: r for r in RG.SAMPLED}
    out = {}
    for rid, s in seen.items():
        if rid in lib and again[rid].text == lib[rid].text:      # generator rejects some candidates after G()
            out[rid] = s
    return out, lib


def order(rid, k):
    """A seeded order of the k conditions that is not the original one."""
    idx = list(range(k))
    rng = random.Random(f"{SEED}/{rid}")
    while idx == list(range(k)):
        rng.shuffle(idx)
    return idx


def paraphrase(rid, s):
    """(transformed rule object, text template with {thr_*} slots)."""
    family, title, intro, default, alt, conds, setting, cutoff, kw = s
    conds = [conds[i] for i in order(rid, len(conds))]
    rule = R.G(rid, family, title, intro, default, alt, conds, setting, cutoff=cutoff, **kw)   # reordered program
    ph = [p for _, p in conds]
    if family == "any_of":
        text = f"{intro}, prescribe {alt} if {' or '.join(ph)}; otherwise prescribe {default}."
    elif family == "all_of":
        text = f"{intro}, prescribe {alt} if {' and '.join(ph)}; otherwise prescribe {default}."
    elif family == "two_of_three":
        text = (f"{intro}, prescribe {alt} if at least two of the following apply, and otherwise prescribe {default}: "
                f"{'; '.join(ph)}.")
    else:
        items = "; ".join(f"{c.points} point{'s' if c.points > 1 else ''} {'if' if p.startswith('the ') else 'for'} {p}"
                          for c, p in conds)
        text = f"{intro}: Score {items}. Prescribe {alt} if the score is {cutoff} or more; otherwise prescribe {default}."
    for a, b in SYNONYMS:
        text = text.replace(a, b).replace(a.capitalize(), b.capitalize())
    rule.text = text
    return rule


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    parent = ROOT / "data" / registry[PARENT]["path"]
    raw = parent.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == registry[PARENT]["sha256"], "parent records differ from the frozen sha256"
    recs = [json.loads(x) for x in raw.decode("utf-8").splitlines()]
    struct, lib = structures()
    groups = {}
    for r in recs:
        groups.setdefault(r["tid"], []).append(r)
    eligible = sorted(t for t, g in groups.items() if g[0]["rid"] in struct)
    by_family = {}
    for t in eligible:
        by_family.setdefault(groups[t][0]["family"], []).append(t)
    pick = []
    for fam in sorted(by_family):                                # equal shares per family, seeded
        ts = sorted(by_family[fam], key=lambda t: sha(f"{SEED}/{t}"))
        pick += ts[:N // len(by_family)]
    pick = sorted(pick)
    out, errs = [], []
    train_cues = set(P.NEG_CUES["train"]) | set(P.TIME_CUES["train"]) | set(P.CURRENT_CUES["train"])
    for _, new in SYNONYMS:
        assert not set(new.lower().split()) & train_cues and new.lower() not in train_cues
    for t in pick:
        g = groups[t]
        rid = g[0]["rid"]
        new, old = paraphrase(rid, struct[rid]), lib[rid]
        for r in g:
            ov = r["meta"].get("overrides") or {}
            if old.rule_text(ov) != r["rule_text"].strip():
                errs.append(f"{r['iid']}: library text differs from the record's rule text")
            ms = tuple(R.Mention(**m) for m in r["state"])
            cid = r["cid"]
            if r["case_kind"] != "missing":
                a_, b_ = old.label(ms, cid, ov), new.label(ms, cid, ov)
                if a_ != b_:
                    errs.append(f"{r['iid']}: programs differ")
                if r["claim_type"] == "conclusion" and int(a_ == (r["claim_role"] == "s_prime")) != r["label"]:
                    errs.append(f"{r['iid']}: program output is not the record's label")
            x = dict(r)
            x["set"] = SET
            x["rule_text"] = new.rule_text(ov)
            x["meta"] = {**r["meta"], "xp": {"parent": PARENT, "order": order(rid, len(struct[rid][5])),
                                             "transforms": ["reorder", "move", "synonyms"], "parent_text_sha": sha(r["rule_text"])}}
            x["crit"] = {"source": "stated", "provenance": "program-preserving paraphrase of the rule_v1 rule text", "text_sha": sha(x["rule_text"])}
            x["cluster"] = rid
            x["ledger"] = [{k: e[k] for k in schema.LEDGER_KEYS} for e in r["ledger"]]   # key order lost by sort_keys on disk
            schema.validate(x)
            if x["rule_text"] == r["rule_text"] or "{" in x["rule_text"]:
                errs.append(f"{r['iid']}: text unchanged or unfilled")
            out.append(x)
    fam = Counter(groups[t][0]["family"] for t in pick)
    print(f"eligible groups {len(eligible)}; picked {len(pick)} {dict(fam)}; records {len(out)}; rules {len({groups[t][0]['rid'] for t in pick})}; errors {len(errs)}")
    for e in errs[:8]:
        print("  ", e)
    ex = out[0]
    print("ORIGINAL:", groups[ex["tid"]][0]["rule_text"])
    print("PARAPHRASE:", ex["rule_text"])
    text = "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in out)
    name = f"{SET}/test"
    if a.restore:
        if sha(text) != registry[name]["sha256"]:
            sys.exit("rebuild does not match the frozen sha256")
        (ROOT / "data" / registry[name]["path"]).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / "data" / registry[name]["path"]).write_text(text, encoding="utf-8", newline="\n")
        return print("restored")
    if not a.freeze:
        return
    if errs:
        sys.exit("not frozen: check failed")
    if registry.get(name, {}).get("frozen"):
        sys.exit("refusing to rebuild: xp_v1 is frozen (use --restore)")
    d = ROOT / "data" / SET / "test"
    d.mkdir(parents=True, exist_ok=True)
    (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
    today = datetime.date.today().isoformat()
    manifest = {"set": SET, "created": today, "seed": SEED, "derived_from": PARENT, "parent_sha256": registry[PARENT]["sha256"],
                "purpose": "Program-preserving paraphrases of the rule text (stage 2, secondary analysis 6: rate of changed verdicts against rule_v1/test_L2, paired by iid)",
                "n_groups": len(pick), "n_records": len(out), "n_rules": len({groups[t][0]["rid"] for t in pick}),
                "by_family": dict(fam), "eligible_groups": len(eligible), "transforms": ["reorder", "move", "synonyms"],
                "synonyms": [list(s) for s in SYNONYMS], "sha256": sha(text),
                "check": "reordered program equals the original program on every state of every group, and equals the record labels: 0 violations",
                "shortcut_validation": "not applicable: cases, claims and labels are those of rule_v1/test_L2 (validated there)",
                "note": "Restricted to grammar-sampled rules with two or more conditions; hand-written rules keep their text. The claims still say 'Prescribe ...' while the paraphrase says 'give'.",
                "analysis_plan_sha256": hashlib.sha256((ROOT / "docs/ANALYSIS_PLAN_STAGE2.md").read_bytes()).hexdigest()}
    (ROOT / "data" / SET / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    registry[name] = {"path": f"{SET}/test/records.jsonl", "split": "test", "level": "L2", "tier": "paraphrase", "n_groups": len(pick),
                      "n_records": len(out), "sha256": sha(text), "manifest": f"{SET}/MANIFEST.json", "created": today, "frozen": True}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print("frozen and registered:", name)


if __name__ == "__main__":
    main()
