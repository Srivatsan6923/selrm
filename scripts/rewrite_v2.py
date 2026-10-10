"""rewrite_v2: the rewritten tier with the acceptance and anchoring rule fixed on rule_v1/dev (9-10 Oct 2026).

  python scripts/rewrite_v2.py --dev               # acceptance on rule_v1/dev by near-miss kind (rule development)
  python scripts/rewrite_v2.py --n 1000 [--freeze] # the same 1,000 test_L2 groups as rewrite_v1; notes from the cache

Same rewriter, extractors and parameters as rewrite_v1 (scripts/rewrite_tier.py). What differs from
rewrite_v1, all chosen on dev:
  0b. The extractors are told what `time` means for a condition listed under the history (EXTRACT below).
  0. The rewriter is told to keep the time of every fact unmistakable (REWRITE below); the notes are therefore new.
  1. Ledger quotes are anchored with either extractor's quote; an absent mention is matched without its time
     (rewrite_v1 used the first extractor only and required the time, which an absence does not have).
  2. A value is anchored in any equivalent written form (13, 13.0).
  3. A quote that occurs in the note in another letter case is taken from the note.
rewrite_v1 stays frozen and is not replaced.
"""
import argparse
import concurrent.futures as cf
import datetime
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("rewrite_tier", ROOT / "scripts" / "rewrite_tier.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)
D = RT.D
OUT = ROOT / "data" / "rewrite_v2"
# The rewriter's instruction of rewrite_v1 plus one sentence, added after rule_v1/dev showed that current findings
# were rewritten as history ("PMH notable for", "h/o"), which a reader can take for the past.
REWRITE = RT.REWRITE.replace(
    " Do not add, drop, generalise or infer",
    " Keep the time of every fact unmistakable: something the case states for now must read as present now (do not "
    "file it under 'history of', 'h/o', 'PMH' or 'known'), and something the case places in the past must stay "
    "explicitly past, with its year or time phrase. Do not add, drop, generalise or infer")
assert REWRITE != RT.REWRITE
# The extraction instruction of rewrite_v1 with the meaning of `time` spelled out (on dev one extractor read a
# condition the patient still has as past whenever the note filed it under the history).
EXTRACT = RT.EXTRACT.replace(
    "(\"current\" for now or this visit, \"past\" for an earlier time, including a value replaced by a newer one)",
    "(\"current\" if it holds now or at this visit: a condition the patient still has is current even when the note "
    "lists it under the history, e.g. 'history of heart failure, on diuretics'; \"past\" only if the note places it at "
    "an earlier time or says it has ended, resolved or was stopped, and for a value replaced by a newer one)")
assert EXTRACT != RT.EXTRACT


def _find(quote, note):
    """The quote as it stands in the note (exact, else the same words in another letter case), or None."""
    if not isinstance(quote, str) or not quote.strip():
        return None
    if quote in note:
        return quote
    i = note.lower().find(quote.lower())
    return note[i:i + len(quote)] if i >= 0 else None


def _value_forms(found):
    try:
        v = float(found)
    except ValueError:
        return [found]
    forms = {found, repr(v), f"{v:g}", str(int(v)) if v.is_integer() else found}
    return sorted(forms, key=len, reverse=True)


def anchored(rec, note, mention_lists, crit):
    """The case's ledger re-anchored in the note; mention_lists: the extractions of both extractors."""
    out = []
    for e in rec["ledger"]:
        if e["found"] == "not mentioned":
            out.append(e)
            continue
        if crit["kind"] == "numeric":
            form = next((f for f in _value_forms(e["found"]) if re.search(rf"(?<![\d.]){re.escape(f)}(?![\d]|\.\d)", note)), None)
            if form is None:
                return None
            out.append(dict(e, found=form))
            continue
        subj = "patient" if e["subject"] == "patient" else e["subject"][len("other ("):-1]
        time_ = "current" if e["time"] == "current" else "past"
        q = None
        for ms in mention_lists:
            for m in ms:
                if not isinstance(m, dict) or m.get("concept") != crit["concept"] or RT._norm_subject(m.get("subject")) != subj:
                    continue
                status = str(m.get("status")).lower()
                if status != e["status"] or (status != "absent" and str(m.get("time")).lower() != time_):
                    continue
                q = _find(m.get("quote"), note)
                if q:
                    break
            if q:
                break
        if q is None:
            return None
        out.append(dict(e, found=q))
    return [{k: x[k] for k in RT.LEDGER_KEYS} for x in out]


def process(tid, recs, rp, ep, set_name):
    rule = D.RULES_BY_ID[recs[0]["rid"]]
    crit = rule.crit(recs[0]["cid"])
    decimals = {c.concept: c.decimals for c in rule.criteria}
    case = {r["case_kind"]: r for r in recs if r["claim_type"] == "conclusion" and r["claim_role"] == "s"}
    notes, ext = {}, {}
    for k in RT.CASES:
        notes[k] = RT.call(RT.REWRITER, REWRITE.format(case=case[k]["case_text"]), rp).strip()
        for x in RT.EXTRACTORS:
            raw = RT.call(x, EXTRACT.format(concepts=RT.concepts_text(rule), note=notes[k]), ep)
            try:
                ext[(k, x)] = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["mentions"]
            except (ValueError, KeyError, TypeError):
                return tid, False, f"{k}: {x} unparsable", [{"source_tid": tid, "notes": notes}]
            if not RT.accepts(case[k], ext[(k, x)], decimals):
                return tid, False, f"{k}: {x} state differs", [{"source_tid": tid, "reason": f"{k}: {x} state differs", "notes": notes,
                                                                 "extractions": {f"{a}|{b}": v for (a, b), v in ext.items()}}]
    out, cdict = [], {"kind": crit.kind, "concept": crit.concept}
    new_tid = tid.replace("rule_v1.", f"{set_name}.", 1)
    for r in recs:
        k = r["case_kind"]
        led = anchored(r, notes[k], [ext[(k, x)] for x in RT.EXTRACTORS], cdict)
        if led is None:
            why = f"{k}: ledger quote not in note"
            return tid, False, why, [{"source_tid": tid, "reason": why, "notes": notes,
                                      "extractions": {f"{a}|{b}": v for (a, b), v in ext.items()}}]
        meta = dict(r["meta"], tpl=[], rewritten={"from_tier": r["tier"], "rewriter": RT.REWRITER, "extractors": list(RT.EXTRACTORS),
                                                  "source_tid": tid})
        out.append(dict(r, set=set_name, tid=new_tid, iid=r["iid"].replace(tid, new_tid, 1), tier="rewritten", case_text=notes[k],
                        ledger=led, prose=RT.ledger_to_prose(led), meta=meta))
    return tid, True, "", out


def run(G, tids, workers, set_name):
    rp = {"temperature": 0.7, "seed": 2026, "max_tokens": 900}
    ep = {"temperature": 0, "seed": 2026, "max_tokens": 2000, "response_format": {"type": "json_object"}}
    res = {}
    with cf.ThreadPoolExecutor(workers) as pool:
        for tid, ok, why, recs in pool.map(lambda t: process(t, G[t], rp, ep, set_name), tids):
            res[tid] = (ok, why, recs)
    by = defaultdict(Counter)
    for t in tids:
        for key in ("nm_kind", "tier"):
            by[key][(G[t][0][key], res[t][0])] += 1
    acc = [t for t in tids if res[t][0]]
    summary = {"groups_tried": len(tids), "groups_accepted": len(acc), "acceptance_rate": round(100.0 * len(acc) / len(tids), 2),
               "by": {key: {v: {"tried": c[(v, True)] + c[(v, False)], "accepted": c[(v, True)]} for v in sorted({v for v, _ in c})}
                      for key, c in by.items()},
               "reasons": dict(Counter(res[t][1].split(":")[-1].strip() for t in tids if not res[t][0])),
               "reasons_by_kind": {k: dict(Counter(res[t][1].split(": ")[-1] for t in tids if not res[t][0] and G[t][0]["nm_kind"] == k))
                                   for k in sorted({G[t][0]["nm_kind"] for t in tids})},
               "rewriter": RT.REWRITER, "extractors": list(RT.EXTRACTORS), "rewrite_params": rp, "extract_params": ep,
               "date": datetime.date.today().isoformat()}
    return res, acc, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dev", action="store_true")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--workers", type=int, default=48)
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    if a.dev:
        G = RT.groups_of(ROOT / "data" / "rule_v1" / "dev" / "records.jsonl")
        res, acc, s = run(G, sorted(G), a.workers, "rewrite_dev")
        print(json.dumps({k: s[k] for k in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons")}))
        print(json.dumps(s["by"]["nm_kind"]))
        print(json.dumps(s["reasons_by_kind"]))
        (ROOT / "results" / "A-D11-v2-dev").mkdir(parents=True, exist_ok=True)
        (ROOT / "results" / "A-D11-v2-dev" / "summary.json").write_text(json.dumps({"run_id": "A-D11-v2-dev", **s}, indent=1), encoding="utf-8")
        return
    G = RT.groups_of(ROOT / "data" / "rule_v1" / "test_L2" / "records.jsonl")
    tids = RT.pick(G, a.n)
    res, acc, s = run(G, tids, a.workers, "rewrite_v2")
    recs = [r for t in acc for r in res[t][2]]
    for r in recs:
        RT.validate(r)
    summary = {"run_id": "A-D11-v2", **s}
    print(json.dumps({k: s[k] for k in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons")}))
    print(json.dumps(s["by"]["nm_kind"]))
    reg_path = ROOT / "data" / "REGISTRY.json"
    reg = json.loads(reg_path.read_text(encoding="utf-8"))
    if reg.get("rewrite_v2/test", {}).get("frozen"):
        sys.exit("rewrite_v2/test is frozen")
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "rejected.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(json.dumps(x, sort_keys=True) + "\n" for t in tids if not res[t][0] for x in res[t][2])
    info = {"set": "rewrite_v2", "split": "test", "level": "L2", "templates": "rewritten", "frozen": a.freeze, "created": s["date"],
            "generator": "scripts/rewrite_v2.py", "derived_from": "rule_v1/test_L2 (the 1,000 groups of rewrite_v1)",
            "rule": "acceptance as rewrite_v1; ledger quotes anchored with either extractor's quote, an absence matched without its time, values in any equivalent written form; fixed on rule_v1/dev (results/A-D11-v2-dev)",
            "rewritten": {k: summary[k] for k in ("rewriter", "extractors", "groups_tried", "groups_accepted", "acceptance_rate",
                                                  "rewrite_params", "extract_params")}}
    m = D.write(OUT, "test", iter(recs), info, validate=True)
    d = ROOT / "results" / "A-D11-v2"
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    (d / "DONE").write_text("")
    reg["rewrite_v2/test"] = {"path": "rewrite_v2/test/records.jsonl", "split": "test", "level": "L2", "tier": "rewritten",
                              "n_groups": m["n_groups"], "n_records": m["n_records"], "manifest": "rewrite_v2/test/MANIFEST.json",
                              "frozen": a.freeze, "created": s["date"], "sha256": m["sha256"], "audit_file": "rewrite_v2/rejected.jsonl"}
    reg_path.write_text(json.dumps(reg, indent=1, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
