"""Build, validate and register cls_v1: class triplets on classes held out from training (STAGE2_TASKS_A, A4.5-6).

  python scripts/build_cls_v1.py [--freeze | --restore]

One constraint rule per group with a single class condition (selrm/engine2.py). Base: no member. Flip: a
member under its ingredient, brand, label or synonym name. Near-miss: a member of a sibling class, or the
parent term, which is too general to establish membership. The rule names the class and lists no member
(closed book); meta.views holds the texts for C's criterion views: `stated` = the rule plus the member list
(open book), `wrong` = the rule naming a sibling class.
"""
import argparse
import collections
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import cls as C  # noqa: E402
from selrm import engine2 as E  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

SET, SEED = "cls_v1", 20261008
PER_DOMAIN = {"dev": 100, "test": 400}
TIERS = ("easy", "easy", "long")


def h(*x):
    return hashlib.sha256("/".join(map(str, x)).encode()).hexdigest()


def build(split):
    recs, stats, per = [], collections.Counter(), {}
    for domain in ("drug", "phenotype", "disease"):
        conds = C.conditions(split, domain)
        n = PER_DOMAIN[split]
        per[domain] = {"classes": len(conds), "groups": 0}
        for g in range(n):                                   # round-robin over the classes of the domain
            cond, fam, c = conds[g % len(conds)]
            wrong = wrong_class(cond, fam, c, conds)
            rule = C.rule(cond, f"{split}_{domain[:3]}_{g % len(conds):03d}", f"{SEED}/{cond.key}/{g // len(conds)}",
                          source={"class_id": cond.key, "class_name": cond.name, "domain": domain,
                                  "agreement": c.get("agreement"), "n_members": len(cond.members)})
            rs = E.make_group(rule, "c1", "class", TIERS[int(h(SEED, cond.key, g), 16) % 3], split, g, SET, "L2",
                              tpl_split="test", stats=stats, cluster=cond.key)
            views = {"stated": rule.text() + " " + C.member_list(cond),
                     "wrong": rule.text().replace(f"\"{cond.name}\"", f"\"{wrong}\"")}
            for r in rs:
                if r["case_kind"] in ("base", "flip", "near"):   # triplets only: no presentation or missing cases
                    r["meta"]["views"] = views
                    r["meta"]["wrong_class"] = wrong
                    recs.append(r)
            per[domain]["groups"] += 1
    return recs, dict(stats), per


def wrong_class(cond, fam, c, conds):
    """The class the `wrong` view names: a sibling class (ontologies), or the selected class of a near-miss
    ingredient, else the next drug class of the split."""
    if cond.domain != "drug":
        return next(o["name"] for o in fam["classes"] if o is not c)
    owners = {m.get("member_of") for m in c["siblings"]} - {None}
    by_id = {x[2]["id"]: x[2]["name"] for x in conds}
    for o in sorted(owners):
        if o in by_id:
            return by_id[o]
    names = [x[0].name for x in conds]
    return names[(names.index(cond.name) + 1) % len(names)]


def scorers(recs):
    members = {}
    for split in ("dev", "test"):
        for domain in ("drug", "phenotype", "disease"):
            for cond, _, _ in C.conditions(split, domain):
                members[cond.key] = [n.lower() for _, ns in cond.members for n in ns]

    def target_line(r):                                       # a line that is not in the base case of the group
        return r["ledger"][0]["found"] != "not mentioned"

    def closure(r):                                           # the program's reading of the text with the closure table
        low = r["case_text"].lower()
        hit = any(re.search(rf"(?<![a-z0-9]){re.escape(n)}(?![a-z0-9])", low) for n in members[r["meta"]["class_id"]])
        return float((r["claim_role"] == "s_prime") == hit)

    def class_word(r):                                        # matches words of the class name in the case
        words = [w for w in re.findall(r"[a-z]{5,}", r["meta"]["class_name"].lower())]
        hit = any(w in r["case_text"].lower() for w in words)
        return float((r["claim_role"] == "s_prime") == hit)
    return {"always_default": lambda r: float(r["claim_role"] == "s"),
            "concept_named": lambda r: float((r["claim_role"] == "s_prime") == target_line(r)),
            "claim_only": lambda r: float(len(r["claim_text"]) % 7) / 7,
            "class_word_in_case": class_word, "closure_on_text": closure}


def validate(recs):
    out = {}
    for name, fn in scorers(recs).items():
        S = summarise(decisions(recs, [fn(r) for r in recs]), by=())["all"]
        out[name] = {k: round(S[k], 2) for k in ("TA", "Rev", "Hold", "n")}
    ok = out["closure_on_text"]["TA"] == 100 and all(out[k]["TA"] == 0 for k in ("always_default", "concept_named", "claim_only"))
    return out, ok


def counts(recs, per):
    base = [r for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s" and r["claim_type"] == "conclusion"]
    c = lambda f: dict(sorted(collections.Counter(str(f(r)) for r in base).items()))  # noqa: E731
    return {"records": len(recs), "groups": len(base), "classes": len({r["cluster"] for r in recs}), "by_domain": per,
            "by_tier": c(lambda r: r["tier"]), "flip_name_type": c(lambda r: r["meta"]["flip_name_type"]),
            "near_term_type": c(lambda r: r["meta"]["near_term"]["name_type"]),
            "drug_groups_with_atc_agreement": sum(r["meta"]["agreement"] is True for r in base)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    portions, info, val, ok, rej = {}, {}, {}, True, {}
    for split in ("dev", "test"):
        recs, stats, per = build(split)
        portions[split], info[split], rej[split] = recs, counts(recs, per), stats
        val[split], good = validate(recs)
        ok = ok and good
        print(split, {k: v for k, v in info[split].items()}, stats)
        for k, v in val[split].items():
            print(f"  {k:20s} {v}")
    print("VALIDATION:", "PASS" if ok else "FAIL")
    x = next(r for r in portions["test"] if r["case_kind"] == "near" and r["claim_role"] == "s")
    print(x["rule_text"], "\n", x["case_text"], "\n", x["meta"]["near_term"], "| wrong:", x["meta"]["wrong_class"])
    sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()  # noqa: E731
    texts = {p: "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in rs) for p, rs in portions.items()}
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    if a.restore:
        for p, t in texts.items():
            e = registry[f"{SET}/{p}"]
            if sha(t) != e["sha256"]:
                sys.exit(f"{p}: rebuild does not match the frozen sha256")
            (ROOT / "data" / e["path"]).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / "data" / e["path"]).write_text(t, encoding="utf-8", newline="\n")
        return print("restored")
    if not a.freeze:
        return
    if not ok:
        sys.exit("not frozen: validation failed")
    if any(registry.get(f"{SET}/{p}", {}).get("frozen") for p in portions):
        sys.exit("refusing to rebuild: cls_v1 is frozen (use --restore)")
    onto = json.loads((ROOT / "data/onto_v1/MANIFEST.json").read_text(encoding="utf-8"))
    today = datetime.date.today().isoformat()
    man = {"set": SET, "created": today, "seed": SEED, "onto_v1_classes_sha256": onto["classes_sha256"],
           "purpose": "Class triplets on classes held out from training (stage 2, comparison 10 and secondary analysis 10)",
           "engine": "selrm/engine2.py; one rule with a single class condition per group; test-split templates; tiers easy and long",
           "views": "rule_text is the closed-book rule (the class is named, no member list). meta.views.stated adds the member list (open book); meta.views.wrong names a sibling class.",
           "analysis_plan_sha256": hashlib.sha256((ROOT / "docs/ANALYSIS_PLAN_STAGE2.md").read_bytes()).hexdigest(),
           "change_request": "drug classes by FDA EPC classes with an ATC-agreement flag: docs/CHANGE_REQUESTS.md, approved 9 Oct 2026",
           "shortcut_validation": val, "rejects": rej, "portions": {},
           "note": "Membership is relative to the closure tables of onto_v1 (FDA EPC lists, HPO and Mondo releases of the snapshot). The base case does not mention the class or any member."}
    for p, t in texts.items():
        d = ROOT / "data" / SET / p
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(t, encoding="utf-8", newline="\n")
        man["portions"][p] = {**info[p], "sha256": sha(t)}
        registry[f"{SET}/{p}"] = {"path": f"{SET}/{p}/records.jsonl", "split": p, "level": "L2", "tier": "class", "n_groups": info[p]["groups"],
                                 "n_records": info[p]["records"], "sha256": sha(t), "manifest": f"{SET}/MANIFEST.json", "created": today, "frozen": True}
    (ROOT / "data" / SET / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print("frozen and registered:", ", ".join(f"{SET}/{p}" for p in portions))


if __name__ == "__main__":
    main()
