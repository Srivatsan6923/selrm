"""Build, validate and register reg_v1: registered eligibility criteria (evaluation only; STAGE2_TASKS_A, A6).

  python scripts/build_reg_v1.py                 # candidates, checks, counts (model check from cache only)
  python scripts/build_reg_v1.py --model-check   # run the two model sessions (API, cached)
  python scripts/build_reg_v1.py --freeze | --restore

Structure comes from the published annotation of the Leaf corpus and of Chia (selrm/reg.py); cases come from
selrm/engine2.py with dates. Three groups per criterion; near-misses: a value toward the threshold (numeric),
an event before the window, the event in a relative, the event denied (window).
"""
import argparse
import collections
import csv
import datetime
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from selrm import engine2 as E  # noqa: E402
from selrm import reg  # noqa: E402
from selrm.mcv import fidelity as F  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

SET, SEED = "reg_v1", 20261009
OUT = ROOT / "data" / SET
CHECK = OUT / "MODEL_CHECK.jsonl"
PINS = {"lct_corpus.tar.gz": ("Leaf Clinical Trials corpus, figshare doi 10.6084/m9.figshare.17209610.v2, CC BY 4.0",
                              "fa875243c14295adf6b5c431e1998c1b074ee010c9787a3bf2e30cd0fe075211"),
        "chia_with_scope.zip": ("Chia, figshare doi 10.6084/m9.figshare.11855817.v2, CC BY 4.0",
                                "b51ec05ba42a3805daf9581dd22a305986f7c5ae3ca4dad36b70d37970fb69b2")}
PROMPT = """A script read one eligibility criterion of a clinical trial and wrote down what it means.

Criterion as registered: {text}

Reading by the script: {reading}

Is the reading the same condition as the criterion: the same quantity or event, the same direction of comparison, the same number and the same unit, with nothing of the criterion left out? A criterion that also requires something else (a second condition, a qualifier such as severity or cause, a different reference point than the visit) is NOT the same.
Reply with JSON only: {{"same": true or false, "why": "<a few words>"}}"""


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def candidates():
    """Compiled criteria that pass the text check, with drop counts per step."""
    ex = json.loads((OUT / "trialgpt_exclusions.json").read_text(encoding="utf-8"))
    ex_trials, ex_texts = set(ex["trial_ids"]), {norm(t) for t in ex["criterion_texts"]}
    steps, out, seen = collections.OrderedDict(), [], set()
    for src, fn in (("LCT", reg.lct_candidates), ("Chia", reg.chia_candidates)):
        C = fn()
        st = steps.setdefault(src, collections.OrderedDict())
        st["annotated_lines"] = len(C)
        st["trials"] = len({r["trial"] for r, _, _ in C if r}) and None
        ok = [r for r, _, _ in C if r]
        st["single_condition_compiled"] = len(ok)
        st["dropped_by_reason"] = dict(collections.Counter(w for r, w, _ in C if not r).most_common())
        del st["trials"]
        keep = []
        drops = collections.Counter()
        for r in ok:
            thr = float(r["value"])
            if not reg.text_check(r):
                drops["a number, unit or operator of the structure is not in the criterion text"] += 1
            elif r["trial"] in ex_trials or norm(r["text"]) in ex_texts:
                drops["trial or criterion text of the TrialGPT annotations"] += 1
            elif norm(r["text"]) in seen:
                drops["duplicate criterion text"] += 1
            elif thr <= 0 or len(r["text"]) > 200 or len(r["name"]) < 2:
                drops["threshold not positive, text over 200 characters or name under 2 characters"] += 1
            elif re.search(r"[0-9<>=≤≥]|\b(and|or|but|to)\b", r.get("unit", ""), re.I) or re.search(r"[<>=≤≥]", r["name"]):
                drops["unit or name carries a second number, comparator or conjunction (a range or a second condition)"] += 1
            else:
                seen.add(norm(r["text"]))
                r["crit_id"] = f"{src.lower()}_{r['trial']}_{r['section'][:3]}{r['line']:03d}"
                keep.append(r)
        st["dropped_after_compilation"] = dict(drops)
        st["candidates"] = len(keep)
        st["candidates_by_kind"] = dict(collections.Counter(r["kind"] for r in keep))
        out += keep
    return out, steps


def model_check(cands, run):
    """Two model sessions read criterion and program; {crit_id: {model: answer}} (cached answers only unless run)."""
    api = F._api()
    done = {}
    if CHECK.exists():
        for ln in open(CHECK, encoding="utf-8"):
            d = json.loads(ln)
            done[d["crit_id"]] = d
    todo = [r for r in cands if r["crit_id"] not in done or done[r["crit_id"]]["text_sha"] != sha(r["text"] + reg.describe(r))]
    if run and todo:
        def one(r):
            prompt = PROMPT.format(text=r["text"], reading=reg.describe(r))
            ans = {}
            for m in F.EXTRACTORS:
                try:
                    ans[m] = F.parse(api.call(m, prompt, {"temperature": 0, "max_tokens": 300}, cache=OUT / "cache"))
                except Exception as e:
                    ans[m] = {"error": type(e).__name__}
            return {"crit_id": r["crit_id"], "text_sha": sha(r["text"] + reg.describe(r)), "answers": ans,
                    "keep": all(isinstance(a, dict) and a.get("same") is True for a in ans.values())}
        with ThreadPoolExecutor(24) as ex:
            for d in ex.map(one, todo):
                done[d["crit_id"]] = d
        with open(CHECK, "w", encoding="utf-8", newline="\n") as f:
            for k in sorted(done):
                f.write(json.dumps(done[k], sort_keys=True, ensure_ascii=False) + "\n")
    return done


class RegRule(E.Rule2):
    """One registered criterion: the rule text is the registry text with the stated conventions."""
    def text(self):
        return self.source["rule_text"]

    def claims(self):
        return "The patient does not meet this criterion.", "The patient meets this criterion."


def cond(r):
    if r["kind"] == "window":
        return E.Cond("c1", "window", r["name"], n=int(r["value"]), unit=r["unit"])
    thr = float(r["value"])
    dec = len(r["value"].split(".")[1]) if "." in r["value"] else 0
    span = 12 if r["name"] == "age" else max(thr * 0.5, 5 * 10 ** -dec)      # at least five steps on each side
    lo, hi = max(thr - span, 0), thr + span
    return E.Cond("c1", "numeric", r["name"], op=r["op"], threshold=thr, decimals=dec, lo=round(lo, dec), hi=round(hi, dec), num_unit=r["unit"])


def groups(r, split, stats):
    c = cond(r)
    rule = RegRule(r["crit_id"], "any", (c,), "", "", "", "Screening visit for a clinical trial.", None, (30, 64),
                   family=f"reg|{r['kind']}", source={"rule_text": reg.rule_text(r), "trial": r["trial"], "section": r["section"],
                                                     "corpus": r["source"], "criterion_text": r["text"]})
    kinds = ("window", "subject", "negation") if r["kind"] == "window" else \
        ("numeric", "numeric", "boundary" if r["op"] in ("<", ">") else "numeric")
    out = []
    for g, nm in enumerate(kinds):
        recs = E.make_group(rule, "c1", nm, ("easy", "long", "easy")[g], split, g, SET, "external", tpl_split="test", stats=stats,
                            cluster=r["trial"])
        for x in recs:
            if x["case_kind"] in ("base", "flip", "near") and x["claim_type"] == "conclusion":
                x = dict(x, claim_type="criterion", iid=x["iid"].replace("/conclusion/", "/criterion/"), struct=reg.struct(r),
                         condition=r["text"], tier="external")
                x["crit"] = {"source": "stated", "provenance": f"{r['source']} annotation of the registered criterion ({r['trial']})",
                             "text_sha": sha(x["rule_text"])}
                E.validate2(x)
                out.append(x)
    return out


def validate(recs):
    def named(r):
        return r["ledger"][0]["found"] != "not mentioned" and r["struct"]["kind"] == "window"
    fns = {"always_default": lambda r: float(r["claim_role"] == "s"),
           "concept_named": lambda r: float((r["claim_role"] == "s_prime") == (named(r) or r["struct"]["kind"] == "numeric")),
           "program": lambda r: float(r["label"])}
    out = {}
    for name, fn in fns.items():
        S = summarise(decisions(recs, [fn(r) for r in recs], claim_type="criterion"), by=("nm_kind",))
        out[name] = {k: {m: round(v[m], 2) for m in ("TA", "Rev", "Hold", "n")} for k, v in sorted(S.items())}
    ok = out["program"]["all"]["TA"] == 100 and out["always_default"]["all"]["TA"] == 0 and out["concept_named"]["all"]["TA"] == 0
    return out, ok


def sheet(kept, n=50):
    pick = sorted(kept, key=lambda r: sha(f"{SEED}/sheet/{r['crit_id']}"))[:n]
    d = ROOT / "audit" / "s2"
    d.mkdir(parents=True, exist_ok=True)
    with open(d / "reg_criteria_sheet.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["case", "crit_id", "corpus", "trial", "section", "criterion_text", "reading_by_the_script", "rule_text_shown_to_models",
                    "q1_reading_is_the_criterion (yes/no)", "q2_what_is_missing_or_wrong"])
        for k, r in enumerate(pick, 1):
            w.writerow([k, r["crit_id"], r["source"], r["trial"], r["section"], r["text"], reg.describe(r), reg.rule_text(r), "", ""])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-check", action="store_true")
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    for name, (_, h) in PINS.items():
        got = hashlib.sha256((reg.EXT / name).read_bytes()).hexdigest()
        assert got == h, f"{name}: sha256 {got} differs from the pin"
    cands, steps = candidates()
    print(json.dumps({k: {x: y for x, y in v.items() if x != "dropped_by_reason"} for k, v in steps.items()}, indent=1))
    verdict = model_check(cands, a.model_check)
    checked = [r for r in cands if r["crit_id"] in verdict]
    kept = [r for r in checked if verdict[r["crit_id"]]["keep"]]
    print(f"model check: {len(checked)} of {len(cands)} read; kept {len(kept)}", dict(collections.Counter((r['source'], r['kind']) for r in kept)))
    if len(checked) < len(cands):
        print("model check incomplete: run with --model-check")
        return
    is_dev = lambda r: int(sha(f"{SEED}/dev/{r['trial']}"), 16) % 10 == 0  # noqa: E731
    portions, info, val, ok, stats = {}, {}, {}, True, collections.Counter()
    for split in ("dev", "test"):
        rs = [r for r in kept if is_dev(r) == (split == "dev")]
        recs, failed = [], []
        for r in rs:
            try:
                recs += groups(r, split, stats)
            except (RuntimeError, ValueError) as e:
                failed.append((r["crit_id"], str(e)[:80]))
        base = [x for x in recs if x["case_kind"] == "base" and x["claim_role"] == "s"]
        portions[split] = recs
        info[split] = {"records": len(recs), "groups": len(base), "criteria": len({x["rid"] for x in recs}), "trials": len({x["cluster"] for x in recs}),
                       "by_kind": dict(collections.Counter(x["struct"]["kind"] for x in base)),
                       "by_nm_kind": dict(collections.Counter(x["nm_kind"] for x in base)),
                       "by_corpus": dict(collections.Counter(x["meta"]["corpus"] for x in base)),
                       "by_section": dict(collections.Counter(x["meta"]["section"] for x in base)),
                       "criteria_without_a_valid_case": failed}
        val[split], good = validate(recs)
        ok = ok and good
        print(split, {k: v for k, v in info[split].items() if k != "criteria_without_a_valid_case"}, "failed", len(failed), failed[:3])
        print("  ", {k: v["all"] for k, v in val[split].items()})
    print("VALIDATION:", "PASS" if ok else "FAIL", dict(stats.most_common(4)))
    x = next(r for r in portions["test"] if r["case_kind"] == "near" and r["claim_role"] == "s" and r["struct"]["kind"] == "window")
    print(x["rule_text"], "\n---\n", x["case_text"])
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
        sys.exit("refusing to rebuild: reg_v1 is frozen (use --restore)")
    sheet(kept)
    today = datetime.date.today().isoformat()
    man = {"set": SET, "created": today, "seed": SEED, "sources": {k: {"source": v[0], "sha256": v[1]} for k, v in PINS.items()},
           "purpose": "Registered eligibility criteria with structure from published annotation (stage 2, secondary analysis 9); evaluation only",
           "selection": steps, "model_check": {"models": list(F.EXTRACTORS), "read": len(checked), "kept": len(kept),
                                               "file": "data/reg_v1/MODEL_CHECK.jsonl", "note": "these are model checks, not human checks; the authors' sheet is audit/s2/reg_criteria_sheet.csv"},
           "candidates_before_model_check": len(cands), "criteria_kept": len(kept),
           "conventions": reg.CONVENTIONS, "dev": "10% of the trials by a seeded hash of the trial id (for the criterion parser)",
           "cases": "selrm/engine2.py, test-split templates; three groups per criterion; numeric: value toward the threshold (and exactly at a strict threshold); window: event before the window, event in a relative, event denied",
           "excluded": "trials and criterion texts of the TrialGPT annotations (data/reg_v1/trialgpt_exclusions.json)",
           "analysis_plan_sha256": hashlib.sha256((ROOT / "docs/ANALYSIS_PLAN_STAGE2.md").read_bytes()).hexdigest(),
           "shortcut_validation": val, "portions": {},
           "note": "The rule text is the registered criterion followed by the stated conventions. Case values are drawn around the threshold (within half the threshold on each side, at least five steps; age within 12 years) and are not checked for clinical plausibility. No clinician read the criteria."}
    for p, t in texts.items():
        (OUT / p).mkdir(parents=True, exist_ok=True)
        (OUT / p / "records.jsonl").write_text(t, encoding="utf-8", newline="\n")
        man["portions"][p] = {**info[p], "sha256": sha(t)}
        registry[f"{SET}/{p}"] = {"path": f"{SET}/{p}/records.jsonl", "split": p, "level": "external", "tier": "external", "n_groups": info[p]["groups"],
                                 "n_records": info[p]["records"], "sha256": sha(t), "manifest": f"{SET}/MANIFEST.json", "created": today, "frozen": True}
    (OUT / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print("frozen and registered:", ", ".join(f"{SET}/{p}" for p in portions))


if __name__ == "__main__":
    main()
