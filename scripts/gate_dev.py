"""Gate on the gold records of a development set (STAGE2_TASKS_B B1): parser coverage, and agreement of the gate's
`applies` with the rule program's applicability (meta.criterion_holds), over the distinct (case, condition) units.
With --run RUN_ID the records are that run's reader outputs on the set instead of the gold ledgers (malformed
outputs are counted and left out). Development portions only. Writes results_git/B-S2-gate-dev/
summary_<set>[@RUN_ID].json; prints disagreements with -v.
  python scripts/gate_dev.py rule_v1/dev [-v] [--run B-F-ledger2-triplets-s0]"""
import collections, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from selrm.crit_parse import from_struct, parse_criterion, same
from selrm.formats import parse_entries, well_formed
from selrm.gate import gate
from selrm.link import load_onto
from report_b import DATA, RG


def main():
    set_name, verbose = sys.argv[1], "-v" in sys.argv
    assert set_name.split("/")[1].startswith(("dev", "adapt")), "development portions only"
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    run = sys.argv[sys.argv.index("--run") + 1] if "--run" in sys.argv else None
    out_of = run and {r["iid"]: r.get("reader_output") for r in map(json.loads, open(
        f"{RG}/{run}/scores_{set_name.replace('/', '~')}.jsonl", encoding="utf-8"))}
    onto = load_onto(f"{DATA}/onto_v1/classes.json") if os.path.exists(f"{DATA}/onto_v1/classes.json") else None
    classes = onto and onto["classes"]
    n = collections.Counter()
    seen, by_kind, unparsed = set(), collections.defaultdict(collections.Counter), set()
    for r in map(json.loads, open(f"{DATA}/{reg[set_name]['path']}", encoding="utf-8")):
        unit = (r["tid"], r["case_kind"], r["condition"])
        if unit in seen:
            continue
        seen.add(unit)
        n["units"] += 1
        gold = r["meta"].get("criterion_holds")
        if gold is None:                 # missing-input twins have no applicability
            n["units"] -= 1
            continue
        cons = parse_criterion(r["rule_text"], r["condition"], classes)
        st = from_struct(r.get("struct"))
        if st is not None and not run:   # reference variant: constraints from struct; parser precision against it
            n["struct_units"] += 1
            gs = gate(r["ledger"], st, r["case_text"], r.get("ref_date"), onto)
            n["struct_agree"] += gs["applies"] == gold
            n["parser_same_as_struct"] += same(cons, st)
            if verbose and cons is not None and not same(cons, st):
                print(json.dumps({"PARSER": cons, "STRUCT": st, "cond": r["condition"], "rule": r["rule_text"]}, ensure_ascii=False))
            if verbose and gs["applies"] != gold:
                print(json.dumps({"STRUCT GATE": gs, "gold": gold, "struct": st, "ledger": r["ledger"], "ref": r.get("ref_date")}, ensure_ascii=False))
        for e in ([] if run or not onto else r["ledger"]):      # linking: gold concept among the terms retrieved
            if e.get("concept"):
                cand = [c[0] for c in onto["linker"].in_text(e["found"])]
                n["link_mentions"] += 1
                n["link_top1"] += cand[:1] == [e["concept"]]
                n["link_top10"] += e["concept"] in cand
                n["link_none"] += not cand
        if cons is None:
            unparsed.add((r["rule_text"], r["condition"]))
            continue
        n["parsed"] += 1
        ledger = r["ledger"]
        if run:
            text = out_of.get(r["iid"]) or ""
            if not well_formed(text, r["case_text"], "ledger2"):
                n["malformed"] += 1
                continue
            ledger = parse_entries(text)
        g = gate(ledger, cons, r["case_text"], r.get("ref_date"), onto)
        n["computed"] += g["applies"] is not None
        ok = g["applies"] == gold
        n["agree"] += ok
        by_kind[r["nm_kind"]]["n"] += 1
        by_kind[r["nm_kind"]]["agree"] += ok
        if verbose and not ok:
            print(json.dumps({"cond": r["condition"], "rule": r["rule_text"], "cons": cons, "ledger": ledger,
                              "gate": g, "gold": gold, "kind": r["case_kind"]}, ensure_ascii=False))
    pct = lambda a, b: round(100.0 * a / b, 2) if b else None
    out = {"set": set_name, "records": run or "gold", **n, "parser_coverage": pct(n["parsed"], n["units"]),
           "gate_coverage": pct(n["computed"], n["units"]), "agreement_on_parsed": pct(n["agree"], n["parsed"] - n["malformed"]),
           "gate_struct_agreement": pct(n["struct_agree"], n["struct_units"]),
           "parser_precision_vs_struct": pct(n["parser_same_as_struct"], n["struct_units"]),
           "link_top1": pct(n["link_top1"], n["link_mentions"]), "link_top10": pct(n["link_top10"], n["link_mentions"]),
           "link_abstain": pct(n["link_none"], n["link_mentions"]),
           "by_nm_kind": {k: {**v, "agreement": pct(v["agree"], v["n"])} for k, v in sorted(by_kind.items())},
           "unparsed": sorted(c for _, c in unparsed)}
    d = f"{RG}/B-S2-gate-dev"
    os.makedirs(d, exist_ok=True)
    json.dump(out, open(f"{d}/summary_{set_name.replace('/', '~')}{'@' + run if run else ''}.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "unparsed"}), len(out["unparsed"]), "unparsed pairs")


if __name__ == "__main__":
    main()
