"""Ledger-RM-G (STAGE2_SPEC 7; STAGE2_TASKS_B B3): assemble the composite from stored scores. Per item, the score
of the gate run (routes gate and judge_case) or, for the routes fallback_none and fallback_malformed, the score of
the verdict-only adapter of the same seed. Variants: gate (parsed criterion), gate_struct (constraints from
struct), reader_bit (no gate: the reader's own record, judge without the case; malformed -> fallback).
Writes results_git/B-S2-<set>-ledger_rm_g-<variant>-s<k>/{scores_<set>.jsonl, summary_<set>.json, meta.json, DONE}
for every set whose records are in the local data copy and whose source scores exist.
  python scripts/assemble_rmg.py SEED [SEED ...]            # assemble
  python scripts/assemble_rmg.py --validate SEED [...]      # B3.2: development sets only; exit 1 if a check fails"""
import collections, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from eval_local import summarize
from report_b import DATA, RG
from resummarize_b import KEEP

MARGIN = 0.5
SRC = {"gate": "B-S2G-gate-s{k}-{part}", "gate_struct": "B-S2G-struct-s{k}-{part}"}


def rows(run, set_name):
    p = f"{RG}/{run}/scores_{set_name.replace('/', '~')}.jsonl"
    return {r["iid"]: r for r in map(json.loads, open(p, encoding="utf-8"))} if os.path.exists(p) else None


def first(runs, set_name):
    return next((r for r in (rows(x, set_name) for x in runs) if r), None)


def ta(run, set_name):
    p = f"{RG}/{run}/summary_{set_name.replace('/', '~')}.json"
    return json.load(open(p))["all"]["TA"] if os.path.exists(p) else None


def assemble(k, set_name, variant, recs):
    part = "dev" if set_name.endswith("/dev") else "test"
    reader, verdict = f"B-V2-reader-triplets-s{k}", f"B-V2-verdict-triplets-s{k}"
    src = (first([reader, f"B-S2G-bit-s{k}-dev"], set_name) if variant == "reader_bit"
           else rows(SRC[variant].format(k=k, part=part), set_name))
    fb = first([verdict, f"B-S2G-verdict-s{k}-dev"], set_name)
    if src is None or fb is None:
        return None
    out, routes = [], collections.Counter()
    for r in recs:
        s = src[r["iid"]]
        route = s.get("route") or ("fallback_none" if not r.get("rule_text", "x") else "reader_bit")
        if variant == "reader_bit" and s["u"] <= -19.9:      # MALFORMED_U: the stage-1 rejection becomes the fallback
            route = "fallback_malformed"
        fall = route.startswith("fallback")
        routes[route] += 1
        out.append({"iid": r["iid"], "u": fb[r["iid"]]["u"] if fall else s["u"], "route": route}
                   | ({"checks": s["checks"]} if "checks" in s else {}))
    rid = f"B-S2-{set_name.replace('/', '.')}-ledger_rm_g-{variant}-s{k}"
    d = f"{RG}/{rid}"
    os.makedirs(d, exist_ok=True)
    name = set_name.replace("/", "~")
    with open(f"{d}/scores_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
        f.writelines(json.dumps(x) + "\n" for x in out)
    summ = summarize(recs, [x["u"] for x in out], rid, set_name)
    n = len(out)
    summ["eval"] = {"routes": dict(routes), "fallback_rate": round(sum(v for r, v in routes.items() if r.startswith("fallback")) / n, 4),
                    "gate_coverage": round(routes["gate"] / n, 4), "malformed_rate": round(routes["fallback_malformed"] / n, 4)}
    json.dump(summ, open(f"{d}/summary_{name}.json", "w", encoding="utf-8", newline="\n"), indent=1)
    json.dump({"run_id": rid, "system": f"ledger_rm_g_s{k}", "variant": variant, "seed": k, "reader": reader,
               "fallback": verdict, "set": set_name}, open(f"{d}/meta.json", "w", newline="\n"), indent=1)
    open(f"{d}/DONE", "w").write("assembled\n")
    return summ


def main():
    validate, seeds = "--validate" in sys.argv, [int(a) for a in sys.argv[1:] if a.isdigit()]
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    sets = [s for s in ("rule_v2/dev", "rule_v1/dev", "cls_v1/dev", "rule_v2/test_L2", "rule_v1/test_L2", "xr_v1/test",
                        "cls_v1/test") if s in reg and (s.endswith("/dev") or not validate)]
    ok = True
    for set_name in sets:
        recs = [{k: r.get(k) for k in KEEP + ("rule_text",)} for r in map(json.loads, open(f"{DATA}/{reg[set_name]['path']}", encoding="utf-8"))]
        for k in seeds:
            for variant in ("gate", "gate_struct", "reader_bit"):
                s = assemble(k, set_name, variant, recs)
                if s is None:
                    print(f"s{k} {set_name} {variant}: source scores missing")
                    ok &= not (variant == "gate" and set_name in ("rule_v2/dev", "rule_v1/dev"))   # nothing validated
                    continue
                t = s["all"]["TA"]
                print(f"s{k} {set_name} {variant}: TA {t:.2f} {s['eval']}")
                ref = {"rule_v2/dev": f"B-V2-reader-triplets-s{k}", "rule_v1/dev": f"B-F-ledger2-triplets-s{k}"}.get(set_name)
                if validate and variant == "gate" and ref:
                    r = ta(ref, set_name)
                    good = r is not None and t >= r - MARGIN
                    ok &= good
                    print(f"  VALIDATION s{k} {set_name}: composite {t:.2f} vs {ref} {r} (margin {MARGIN}): {'pass' if good else 'FAIL'}")
    sys.exit(0 if ok or not validate else 1)


if __name__ == "__main__":
    main()
