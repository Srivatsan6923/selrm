"""Gate on the gold records of a development set (STAGE2_TASKS_B B1): parser coverage, and agreement of the gate's
`applies` with the rule program's applicability (meta.criterion_holds), over the distinct (case, condition) units.
Development portions only. Writes results_git/B-S2-gate-dev/summary_<set>.json; prints disagreements with -v.
  python scripts/gate_dev.py rule_v1/dev [-v]"""
import collections, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from selrm.crit_parse import parse_criterion
from selrm.gate import gate
from report_b import DATA, RG


def main():
    set_name, verbose = sys.argv[1], "-v" in sys.argv
    assert set_name.split("/")[1].startswith(("dev", "adapt")), "development portions only"
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    n = collections.Counter()
    seen, by_kind, unparsed = set(), collections.defaultdict(collections.Counter), set()
    for r in map(json.loads, open(f"{DATA}/{reg[set_name]['path']}", encoding="utf-8")):
        unit = (r["tid"], r["case_kind"], r["condition"])
        if unit in seen:
            continue
        seen.add(unit)
        n["units"] += 1
        cons = parse_criterion(r["rule_text"], r["condition"])
        if cons is None:
            unparsed.add((r["rule_text"], r["condition"]))
            continue
        n["parsed"] += 1
        g = gate(r["ledger"], cons, r["case_text"], r.get("ref_date"))
        gold = r["meta"]["criterion_holds"]
        n["computed"] += g["applies"] is not None
        ok = g["applies"] == gold
        n["agree"] += ok
        by_kind[r["nm_kind"]]["n"] += 1
        by_kind[r["nm_kind"]]["agree"] += ok
        if verbose and not ok:
            print(json.dumps({"cond": r["condition"], "rule": r["rule_text"], "cons": cons, "ledger": r["ledger"],
                              "gate": g, "gold": gold, "kind": r["case_kind"]}, ensure_ascii=False))
    pct = lambda a, b: round(100.0 * a / b, 2) if b else None
    out = {"set": set_name, **n, "parser_coverage": pct(n["parsed"], n["units"]),
           "gate_coverage": pct(n["computed"], n["units"]), "agreement_on_parsed": pct(n["agree"], n["parsed"]),
           "by_nm_kind": {k: {**v, "agreement": pct(v["agree"], v["n"])} for k, v in sorted(by_kind.items())},
           "unparsed": sorted(c for _, c in unparsed)}
    d = f"{RG}/B-S2-gate-dev"
    os.makedirs(d, exist_ok=True)
    json.dump(out, open(f"{d}/summary_{set_name.replace('/', '~')}.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "unparsed"}), len(out["unparsed"]), "unparsed pairs")


if __name__ == "__main__":
    main()
