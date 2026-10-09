"""rewrite_v1 (A-D11): test_L2 triplets rewritten as clinical notes by an open LLM, kept only
where two extractors from other model families recover the full state.

  python scripts/rewrite_tier.py --n 1000              # API calls (OPENROUTER_API_KEY), cached
  python scripts/rewrite_tier.py --n 1000 --freeze     # also register rewrite_v1/test (frozen)
  python scripts/rewrite_tier.py --selftest            # acceptance and ledger logic, no API

A group (base, flip, near, pres of one test_L2 triplet) is accepted only if, for every
case, both extractors return exactly the case's mentions: concept, value, subject,
status and time (a generic absence line may be omitted or read as the patient's
absence; a delabelled allergy may be read as present-past or absent). Labels stay the
program's on the unchanged state; ledger quotes are re-anchored in the rewritten text.
Rejected groups are an audit file (data/rewrite_v1/rejected.jsonl: notes, extractions, reason) and are
never scored. Every API response is cached under data/rewrite_v1/cache/ (one JSON per call,
keyed by a hash of model, messages and parameters), so the set rebuilds from the
cache without calls. The acceptance rate is written to results/A-D11/summary.json.
"""
import argparse
import concurrent.futures as cf
import datetime
import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm.rules import FIRST_DEGREE  # noqa: E402
from selrm.schema import LEDGER_KEYS, validate  # noqa: E402
from selrm.smoke import ledger_to_prose  # noqa: E402

API = "https://openrouter.ai/api/v1/chat/completions"
REWRITER = "google/gemma-4-31b-it"                               # verified on openrouter.ai/api/v1/models, 2 Oct 2026
EXTRACTORS = ("deepseek/deepseek-v4-pro", "openai/gpt-oss-120b")  # two families, neither the rewriter's
# Provider routing per model: the cheapest endpoints that serve the published weights (cost plan of 3 Oct 2026,
# prices from openrouter.ai/api/v1/models/<id>/endpoints); re-quantised endpoints are excluded.
ROUTES = {
    "google/gemma-4-31b-it": {"provider": {"order": ["crusoe/bf16", "parasail/fp8", "deepinfra/fp8"],
                                           "allow_fallbacks": True, "quantizations": ["bf16", "fp8"],
                                           "ignore": ["chutes", "novita", "siliconflow"]}},
    "deepseek/deepseek-v4-pro": {"provider": {"order": ["streamlake/fp8", "parasail/fp8"], "allow_fallbacks": True,
                                              "quantizations": ["fp8"],
                                              "max_price": {"prompt": 0.5, "completion": 3.5}},
                                 "reasoning": {"enabled": False}},
    "openai/gpt-oss-120b": {"provider": {"order": ["coreweave/fp4", "dekallm/bf16", "akashml/bf16"],
                                         "allow_fallbacks": True, "ignore": ["google-vertex", "deepinfra"]},
                            "reasoning": {"effort": "low"}},
}
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "rewrite_v1"
CASES = ("base", "flip", "near", "pres")

REWRITE = (
    "Rewrite the patient case below as a realistic clinical note, the way a clinician would write it: free "
    "text, common abbreviations allowed, sentences may be merged or reordered. Keep every fact exactly as "
    "stated: every number and unit, who each fact concerns (the patient, or a named relative or other "
    "person), whether something is present or explicitly denied or absent, and when it applies (now, or in "
    "the past with its year or time phrase). Do not add, drop, generalise or infer any finding, value, "
    "diagnosis, explanation or plan. Return only the note.\n\nCase:\n{case}")
EXTRACT = (
    "Read the clinical note and list every statement it makes about the concepts below (and nothing else).\n"
    "Concepts:\n{concepts}\n\n"
    "For each statement give: concept (one of the ids above); quote (the exact words of the note that make "
    "the statement, copied character for character); value (the number for a measurement, else null); "
    "subject (\"patient\", or the relation of the other person, e.g. \"sister\", \"coworker\"); status "
    "(\"present\", \"absent\" if the note denies it, \"unknown\" if the note says it is not known); time "
    "(\"current\" for now or this visit, \"past\" for an earlier time, including a value replaced by a newer "
    "one). Include denials, other people's conditions and earlier values. Answer with JSON only: "
    "{{\"mentions\": [{{\"concept\": ..., \"quote\": ..., \"value\": ..., \"subject\": ..., \"status\": ..., "
    "\"time\": ...}}]}}\n\nNote:\n{note}")


# ------------------------------------------------------------------ API and cache
def _key(model, messages, params):
    return hashlib.sha256(json.dumps([model, messages, params], sort_keys=True).encode()).hexdigest()


def call(model, prompt, params, cache=OUT / "cache", tries=6):
    params = {**params, **ROUTES.get(model, {})}       # the model's provider routing is part of the cache key
    messages = [{"role": "user", "content": prompt}]
    path = cache / f"{_key(model, messages, params)}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))["content"]
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set (COMPUTE REQUEST); cached responses only")
    body = json.dumps({"model": model, "messages": messages, **params}).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(API, body, {"Authorization": f"Bearer {key}",
                                                     "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                resp = json.loads(r.read())
            content = resp["choices"][0]["message"]["content"]
            cache.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"model": model, "params": params, "content": content,
                                        "provider_model": resp.get("model"), "provider": resp.get("provider"),
                                        "usage": resp.get("usage"),
                                        "date": datetime.date.today().isoformat()}), encoding="utf-8")
            return content
        except Exception as e:                     # rate limits, timeouts, provider errors
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt + random.random())


# ------------------------------------------------------------------ acceptance
def _norm_subject(s):
    s = re.sub(r"^(the |his |her |patient's |pt's )", "", str(s).strip().lower())
    return "patient" if s in ("patient", "pt", "the patient", "self") else s


def _value(m, decimals):
    v = m.get("value")
    if v is None or v is True or v in ("", "null"):  # not `in (None, True, ...)`: 1.0 == True in Python
        return None
    try:
        return round(float(m["value"]), decimals)
    except (TypeError, ValueError):
        return "bad"


def gold_mentions(rec, decimals):
    """(concept, subject, status, time, value, form) of the named mentions of a case."""
    return [(m["concept"], m["subject"], m["status"], m["time"],
             round(m["value"], decimals[m["concept"]]) if m["kind"] == "numeric" else None, m["form"])
            for m in rec["state"] if m["form"] != "generic"]


def accepts(rec, mentions, decimals):
    """True if the extracted mentions are exactly the case's named mentions."""
    gold = gold_mentions(rec, decimals)
    concepts = set(decimals)
    generic = {m["concept"] for m in rec["state"] if m["form"] == "generic"}
    named = {g[0] for g in gold}
    got = []
    for m in mentions:
        c = m.get("concept")
        if c not in concepts:
            continue
        e = (c, _norm_subject(m.get("subject")), str(m.get("status")).lower(), str(m.get("time")).lower(),
             _value(m, decimals[c]))
        if e[1:4] == ("patient", "absent", "current") and e[4] is None and c not in named and \
                (c in generic or c not in named):
            continue                               # a generic absence (or closed world) read as absence
        got.append(e)
    want = Counter(g[:5] for g in gold if g[5] != "delabelled")
    dl = [g for g in gold if g[5] == "delabelled"]
    for g in dl:                                   # allergy removed after testing: present-past or absent
        alts = [(g[0], g[1], "present", "past", None), (g[0], g[1], "absent", "past", None),
                (g[0], g[1], "absent", "current", None)]
        hit = next((a for a in alts if a in got), None)
        if hit is None:
            return False
        got.remove(hit)
    return Counter(got) == want


def anchored_ledger(rec, note, mentions, crit, decimals):
    """The case's ledger with each finding quote re-anchored in the note (numbers stay
    values); None if a quote is not a substring of the note or a value is not in it.
    Entries come back in the schema's key order (records read from disk have sorted keys,
    which selrm.schema.validate rejects)."""
    out = _anchored(rec, note, mentions, crit)
    return None if out is None else [{k: e[k] for k in LEDGER_KEYS} for e in out]


def _anchored(rec, note, mentions, crit):
    out = []
    for e in rec["ledger"]:
        if e["found"] == "not mentioned":
            out.append(e)
            continue
        if crit["kind"] == "numeric":
            if e["found"] not in note:
                return None
            out.append(e)
            continue
        subj = "patient" if e["subject"] == "patient" else e["subject"][len("other ("):-1]
        time_ = "current" if e["time"] == "current" else "past"
        q = next((m.get("quote") for m in mentions if m.get("concept") == crit["concept"]
                  and _norm_subject(m.get("subject")) == subj and str(m.get("time")).lower() == time_
                  and isinstance(m.get("quote"), str) and m["quote"] and m["quote"] in note), None)
        if q is None:
            return None
        out.append(dict(e, found=q))
    return out


# ------------------------------------------------------------------ build
def groups_of(path):
    G = defaultdict(list)
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        G[r["tid"]].append(r)
    return G


def pick(G, n, seed=11):
    """n test_L2 groups, stratified by near-miss kind."""
    by = defaultdict(list)
    for tid in sorted(G):
        by[G[tid][0]["nm_kind"]].append(tid)
    rng, out, kinds = random.Random(seed), [], sorted(by)
    for k in kinds:
        rng.shuffle(by[k])
    while len(out) < n and any(by.values()):
        for k in kinds:
            if by[k] and len(out) < n:
                out.append(by[k].pop())
    return out


def concepts_text(rule):
    return "\n".join(f"- {c.concept}: {c.label}" + (" (a measurement)" if c.kind == "numeric" else "")
                     for c in rule.criteria)


def process(tid, recs, rp, ep):
    """Rewrite the four cases of a group, extract with both models, decide acceptance."""
    rule = D.RULES_BY_ID[recs[0]["rid"]]
    crit = rule.crit(recs[0]["cid"])
    decimals = {c.concept: c.decimals for c in rule.criteria}
    case = {r["case_kind"]: r for r in recs if r["claim_type"] == "conclusion" and r["claim_role"] == "s"}
    notes, ok, why, ext = {}, True, "", {}
    for k in CASES:
        notes[k] = call(REWRITER, REWRITE.format(case=case[k]["case_text"]), rp).strip()
        for x in EXTRACTORS:
            raw = call(x, EXTRACT.format(concepts=concepts_text(rule), note=notes[k]), ep)
            try:
                ms = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["mentions"]
            except (ValueError, KeyError, TypeError):
                ok, why = False, f"{k}: {x} unparsable"
                break
            ext[(k, x)] = ms
            if not accepts(case[k], ms, decimals):
                ok, why = False, f"{k}: {x} state differs"
                break
        if not ok:
            break
    out = []
    if not ok:
        return tid, False, why, [{"source_tid": tid, "reason": why, "notes": notes,
                                  "extractions": {f"{k}|{x}": v for (k, x), v in ext.items()}}]
    if ok:
        cdict = {"kind": crit.kind, "concept": crit.concept}
        for r in recs:
            led = anchored_ledger(r, notes[r["case_kind"]], ext[(r["case_kind"], EXTRACTORS[0])], cdict, decimals)
            if led is None:
                why = f"{r['case_kind']}: ledger quote not in note"
                return tid, False, why, [{"source_tid": tid, "reason": why, "notes": notes,
                                          "extractions": {f"{k}|{x}": v for (k, x), v in ext.items()}}]
            meta = dict(r["meta"], tpl=[], rewritten={"from_tier": r["tier"], "rewriter": REWRITER,
                                                      "extractors": list(EXTRACTORS), "source_tid": tid})
            new_tid = tid.replace("rule_v1.", "rewrite_v1.", 1)
            out.append(dict(r, set="rewrite_v1", tid=new_tid, iid=r["iid"].replace(tid, new_tid, 1), tier="rewritten",
                            case_text=notes[r["case_kind"]], ledger=led, prose=ledger_to_prose(led), meta=meta))
    return tid, ok, why, out


def selftest():
    """Acceptance and ledger logic on gold extractions (no API)."""
    G = groups_of(ROOT / "data" / "rule_v1" / "test_L2" / "records.jsonl")
    n = 0
    for tid in sorted(G)[:300]:
        recs = G[tid]
        rule = D.RULES_BY_ID[recs[0]["rid"]]
        decimals = {c.concept: c.decimals for c in rule.criteria}
        for r in recs:
            if r["claim_type"] != "conclusion" or r["claim_role"] != "s" or r["case_kind"] not in CASES:
                continue
            perfect = [{"concept": m["concept"], "value": m["value"] if m["kind"] == "numeric" else None,
                        "subject": m["subject"], "status": m["status"], "time": m["time"]}
                       for m in r["state"] if m["form"] != "generic"]
            assert accepts(r, perfect, decimals), (tid, r["case_kind"])
            if perfect:                            # any changed attribute is rejected
                for field, new in (("subject", "neighbor"), ("status", "unknown"), ("time", "future")):
                    bad = [dict(perfect[0], **{field: new})] + perfect[1:]
                    assert not accepts(r, bad, decimals), (tid, field)
                assert not accepts(r, perfect[1:], decimals) or len(perfect) == 0
            n += 1
    print(f"selftest OK on {n} cases")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    G = groups_of(ROOT / "data" / "rule_v1" / "test_L2" / "records.jsonl")
    tids = pick(G, a.n)
    rp = {"temperature": 0.7, "seed": 2026, "max_tokens": 900}
    ep = {"temperature": 0, "seed": 2026, "max_tokens": 2000, "response_format": {"type": "json_object"}}
    results = {}
    with cf.ThreadPoolExecutor(a.workers) as pool:
        for tid, ok, why, recs in pool.map(lambda t: process(t, G[t], rp, ep), tids):
            results[tid] = (ok, why, recs)
    acc = [t for t in tids if results[t][0]]
    recs = [r for t in acc for r in results[t][2]]
    for r in recs:
        validate(r)
    by = defaultdict(Counter)
    for t in tids:
        k = G[t][0]
        for key in ("nm_kind", "tier"):
            by[key][(k[key], results[t][0])] += 1
    summary = {"run_id": "A-D11", "groups_tried": len(tids), "groups_accepted": len(acc),
               "acceptance_rate": 100.0 * len(acc) / len(tids),
               "by": {key: {v: {"tried": c[(v, True)] + c[(v, False)], "accepted": c[(v, True)]}
                            for v in sorted({v for v, _ in c})} for key, c in by.items()},
               "reasons": dict(Counter(results[t][1].split(":")[-1].strip() for t in tids if not results[t][0])),
               "rewriter": REWRITER, "extractors": list(EXTRACTORS), "routes": ROUTES, "rewrite_params": rp,
               "extract_params": ep, "date": datetime.date.today().isoformat()}
    rejected = [x for t in tids if not results[t][0] for x in results[t][2]]
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "rejected.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(json.dumps(x, sort_keys=True) + "\n" for x in rejected)
    info = {"set": "rewrite_v1", "split": "test", "level": "L2", "templates": "rewritten",
            "frozen": a.freeze, "created": summary["date"], "generator": "scripts/rewrite_tier.py",
            "rewritten": {k: summary[k] for k in ("rewriter", "extractors", "groups_tried", "groups_accepted",
                                                  "acceptance_rate", "rewrite_params", "extract_params")}}
    m = D.write(OUT, "test", iter(recs), info, validate=True)
    res = ROOT / "results" / "A-D11"
    res.mkdir(parents=True, exist_ok=True)
    (res / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    (res / "DONE").write_text("")
    reg_path = ROOT / "data" / "REGISTRY.json"
    reg = json.loads(reg_path.read_text())
    if reg.get("rewrite_v1/test", {}).get("frozen"):
        sys.exit("rewrite_v1/test is frozen")
    reg["rewrite_v1/test"] = {"path": "rewrite_v1/test/records.jsonl", "split": "test", "level": "L2",
                              "tier": "rewritten", "n_groups": m["n_groups"], "n_records": m["n_records"],
                              "manifest": "rewrite_v1/test/MANIFEST.json", "frozen": a.freeze,
                              "created": summary["date"], "sha256": m["sha256"],
                              "audit_file": "rewrite_v1/rejected.jsonl"}
    reg_path.write_text(json.dumps(reg, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons")}))


if __name__ == "__main__":
    main()
