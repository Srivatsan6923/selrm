"""Shortcut scorers with known outcomes. Must pass on every dataset before use.
Usage: python scripts/validate_shortcuts.py data/smoke_v2/test_heldout_rules.jsonl"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.metrics import decisions, summarise
from selrm.rules import RULES_BY_ID

recs = [json.loads(l) for l in open(sys.argv[1])]

def always_default(r): return 1.0 if r["claim_role"] == "s" else 0.0
def oracle(r):         return float(r["label"])
def concept_named(r):
    kws = RULES_BY_ID[r["rid"]].crit(r["cid"]).keywords if r["rid"] in RULES_BY_ID else r["meta"]["keywords"]
    named = any(k in r["case_text"].lower() for k in kws)
    return 1.0 if (r["claim_role"] == "s_prime") == named else 0.0

res = {}
for name, fn in (("always_default", always_default), ("concept_named", concept_named), ("oracle", oracle)):
    S = summarise(decisions(recs, [fn(r) for r in recs]), by=("nm_kind",))
    res[name] = S
    print(f"{name:15s} " + " | ".join(f"{k}: Rev {v['Rev']:.0f} Hold {v['Hold']:.0f} TA {v['TA']:.0f} (n={v['n']})"
                                      for k, v in sorted(S.items())))
ok = (res["always_default"]["all"]["TA"] == 0 and res["always_default"]["all"]["Hold"] == 100
      and res["concept_named"]["all"]["TA"] == 0 and res["oracle"]["all"]["TA"] == 100)
print("SHORTCUT VALIDATION:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
