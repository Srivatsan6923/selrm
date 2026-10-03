"""Build, validate and register xr_v1 (rule-side items; selrm/xr.py).

  python scripts/build_xr_v1.py [--n 400] [--freeze]

Validation (all must hold, else nothing is registered):
  structure  the two rules of an item differ only in the applicability clause; the three cases and
             the conclusion claims are identical under both rules
  labels     contested 1/0, positive 1/1, negative 0/0 (rule that counts / rule that does not)
  scorers    XA = 0 for: always default, concept named, a scorer that ignores the rule text (it
             answers with the counting rule's label, or with the other rule's), never counting the
             contested form, always counting it; XA = 100 for the program
  rendering  no unfilled slot; every ledger quote occurs in the case; fillers name no target keyword
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import xr  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SEED = 2029


def scorers(recs):
    """Per-record scores u(claim) of the validation scorers (higher = claim judged correct)."""
    lab = {(r["meta"]["xr"]["item"], r["meta"]["xr"]["variant"], r["case_kind"], r["claim_type"], r["claim_role"]):
           r["label"] for r in recs}

    def under(variant):
        return lambda r: float(lab[(r["meta"]["xr"]["item"], variant, r["case_kind"], r["claim_type"], r["claim_role"])])

    def counting(contested_counts):
        def f(r):
            if r["case_kind"] != "contested":
                return float(r["label"])
            return float((r["claim_role"] == "s_prime") == contested_counts)
        return f

    def named(r):
        hit = any(k in r["case_text"].lower() for k in r["meta"]["keywords"])
        return float((r["claim_role"] == "s_prime") == hit)
    fns = {"program": lambda r: float(r["label"]),
           "always_default": lambda r: float(r["claim_role"] == "s"),
           "concept_named": named,
           "ignores_rule_text_counting_rule": under("count"),
           "ignores_rule_text_other_rule": under("nocount"),
           "never_counts_contested": counting(False),
           "always_counts_contested": counting(True)}
    return {k: [f(r) for r in recs] for k, f in fns.items()}


def validate(items, recs):
    errs = []
    for it in items:
        c, n = it["rules"]["count"], it["rules"]["nocount"]
        if c["text"].replace(c["condition"], "@") != n["text"].replace(n["condition"], "@") or c["text"] == n["text"]:
            errs.append(f"{it['item']}: rules differ outside the clause")
        want = {"contested": (1, 0), "positive": (1, 1), "negative": (0, 0)}
        for k, w in want.items():
            if (xr.label(it, "count", k), xr.label(it, "nocount", k)) != w:
                errs.append(f"{it['item']}: {k} labels")
    by = {}
    for r in recs:
        key = (r["meta"]["xr"]["item"], r["case_kind"], r["claim_type"], r["claim_role"])
        val = (r["case_text"], r["claim_text"] if r["claim_type"] == "conclusion" else None)
        if by.setdefault(key, val) != val:
            errs.append(f"{key}: case or conclusion claim differs between the rules")
        t = r["case_text"]
        if "None" in t or "{" in t or "}" in t:
            errs.append(f"{r['iid']}: unfilled slot")
        for e in r["ledger"]:
            if e["found"] != "not mentioned" and e["found"] not in t:
                errs.append(f"{r['iid']}: ledger quote not in case")
    for it in items:
        for k, case in it["cases"].items():
            fill = [ln for ln in case["text"].split("\n")[3:] if ln not in case["target_lines"]]
            if any(kw in ln.lower() for ln in fill for kw in it["keywords"]):
                errs.append(f"{it['item']}: a filler names the concept")
    res = {k: xr.crossed_accuracy(recs, s) for k, s in scorers(recs).items()}
    ok = res["program"]["XA"] == 100 and all(v["XA"] == 0 for k, v in res.items() if k != "program")
    return errs, res, ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true",
                    help="write the frozen records.jsonl (records are not in git) if the rebuild matches its sha256")
    a = ap.parse_args()
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    name = "xr_v1/test"
    items = xr.build(a.n, SEED)
    recs = [r for it in items for r in xr.records(it, SEED)]
    if registry.get(name, {}).get("frozen"):
        if not a.restore:
            sys.exit(f"refusing to rebuild: {name} is frozen (use --restore to write its records)")
        lines = [json.dumps(r, sort_keys=True) + "\n" for r in recs]
        got = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()
        if got != registry[name]["sha256"]:
            sys.exit(f"rebuild does not match the frozen sha256 ({got[:16]})")
        (ROOT / "data" / registry[name]["path"]).write_text("".join(lines), encoding="utf-8", newline="\n")
        sys.exit(print(f"restored {name}: sha256 matches") or 0)
    errs, res, ok = validate(items, recs)
    if errs or not ok:
        print("\n".join(errs[:30]))
        print(json.dumps(res, indent=1))
        sys.exit("xr_v1 validation FAILED")

    d = ROOT / "data" / "xr_v1" / "test"
    d.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    with open(d / "records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            line = json.dumps(r, sort_keys=True) + "\n"
            f.write(line)
            h.update(line.encode("utf-8"))
    created = datetime.date.today().isoformat()
    meta = [it["meta"] for it in items]
    man = {"name": "test", "set": "xr_v1", "split": "test", "level": "xr", "tier": "rule_side",
           "created": created, "generator": "scripts/build_xr_v1.py (selrm/xr.py)", "seed": SEED,
           "frozen": a.freeze, "n_items": len(items), "n_groups": len({r["tid"] for r in recs}),
           "n_records": len(recs), "sha256": h.hexdigest(), "git_commit": D.git_commit(),
           "python": sys.version.split()[0], "template_split_hash": D.template_split_hash(), "templates": "test",
           "by_dimension": dict(Counter(m["dimension"] for m in meta)),
           "by_concept": {dim: dict(Counter(m["concept"] for m in meta if m["dimension"] == dim))
                          for dim in xr.DIMS},
           "by_phrasing": dict(Counter(m["phrasing"] for m in meta)),
           "window_pairs": dict(Counter(m["pair"] for m in meta if "pair" in m)),
           "window_date_forms": dict(Counter(m["date_form"] for m in meta if "date_form" in m)),
           "inclusivity_directions": dict(Counter(m["direction"] for m in meta if "direction" in m)),
           "labels": dict(Counter(str(r["label"]) for r in recs)),
           "semantics": "Every case states a visit date. 'Within the W months before the visit date' counts an "
                        "event on or after the date exactly W calendar months before the visit; that boundary "
                        "day counts, and the rule text says so. Rendered events keep at least two months from "
                        "every window edge. All rules are synthetic (grammar scenarios); every item is a "
                        "synthetic intervention on the applicability clause.",
           "validation": {"result": "PASS", "crossed_accuracy": res}}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    registry[name] = {"path": "xr_v1/test/records.jsonl", "split": "test", "level": "xr", "tier": "rule_side",
                      "n_groups": man["n_groups"], "n_records": len(recs), "manifest": "xr_v1/test/MANIFEST.json",
                      "frozen": a.freeze, "created": created, "sha256": man["sha256"]}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(f"{name}: {len(items)} items, {len(recs)} records, sha256 {man['sha256'][:16]}, frozen={a.freeze}")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
