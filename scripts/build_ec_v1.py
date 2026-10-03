"""ec_v1: registered eligibility criteria (FINAL_TASKS A P0.5).

  python scripts/build_ec_v1.py prepare   # ec_v1/formalized.json -> unsigned records, sign-off sheet, exclusions
  python scripts/build_ec_v1.py freeze    # keeps the criteria both authors approved in docs/EC_SIGNOFF.csv

Pipeline: scripts/ec_mine.py (ClinicalTrials.gov, TrialGPT trials and texts excluded) -> formalisation by
model agents with two adversarial verifiers (ec_v1/formalized.json; a criterion is kept only if both
confirm) -> this script (render, check, sheet) -> two authors sign off each program and its rendered
cases (H3) -> freeze. Nothing is scored before the freeze.
"""
import csv
import datetime
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import ec  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KIT, SHEET = ROOT / "ec_v1", ROOT / "docs" / "EC_SIGNOFF.csv"
COLS = ["crit_id", "nct_id", "criterion_type", "original_text", "rule_text_shown", "simplifications",
        "never_mentioned_disjuncts", "program", "executed_tests", "near_miss_kinds", "groups",
        "example_base", "example_flip", "example_near", "example_answers",
        "reviewer_1", "program_ok_1", "cases_ok_1", "comment_1", "reviewer_2", "program_ok_2", "cases_ok_2", "comment_2"]


def guard(f):
    """Reasons the code itself excludes an accepted formalisation."""
    if f["subjects"] == "family" and re.search(r"(?i)family history", f["rule_text"]):
        return "family history counts relatives only; the program's family scope also counts the patient"
    if f["times"] == "window" and f["concept"] not in ec.xr.EVENTS:
        return "window criterion on a concept without dated-event wording"
    if f["input"] == "numeric" and f["concept"] not in ec.NUM:
        return "measurement the generator cannot render"
    if not ec.kinds(f):
        return "no near-miss kind is unambiguous for this criterion"
    return None


def shortcut_check(recs):
    """always-default TA 0 and Hold 100; concept named TA 0; program TA 100 (decisions on conclusion claims)."""
    def named(r):
        hit = any(k in r["case_text"].lower() for k in r["meta"]["keywords"])
        return float((r["claim_role"] == "s_prime") == hit)
    fns = {"always_default": lambda r: float(r["claim_role"] == "s"), "concept_named": named,
           "program": lambda r: float(r["label"])}
    res = {k: summarise(decisions(recs, [f(r) for r in recs]), by=("nm_kind",))["all"] for k, f in fns.items()}
    ok = (res["always_default"]["TA"] == 0 and res["always_default"]["Hold"] == 100 and res["program"]["TA"] == 100
          and res["concept_named"]["TA"] == 0)
    return ok, {k: {m: v[m] for m in ("TA", "Rev", "Hold", "n")} for k, v in res.items()}


def render(items):
    keep, out, excl = [], [], []
    for f in items:
        if f["final"] != "accept":
            excl.append((f, f["exclusion_reason"] or "; ".join(v["reason"] for v in f["verdicts"] if v["verdict"] == "reject")
                         or "not confirmed by both verifiers"))
            continue
        why = guard(f)
        if why:
            excl.append((f, why))
            continue
        try:
            recs = ec.groups(f)
        except (RuntimeError, ValueError, KeyError, StopIteration) as e:
            excl.append((f, f"not renderable: {str(e)[:160]}"))
            continue
        bad = ec.rendered_ok(recs)
        if bad:
            excl.append((f, f"rendering check failed: {bad[0]}"))
            continue
        keep.append(f)
        out += recs
    return keep, out, excl


def sheet_row(f, recs):
    first = min(r["tid"] for r in recs)
    case = {r["case_kind"]: r for r in recs if r["tid"] == first and r["claim_role"] == "s_prime"}
    tests = "; ".join(f"{lab} -> {'met' if y else 'not met'}" for lab, y in ec.boundary_tests(f))
    return {"crit_id": f["cand"], "nct_id": f["nct_id"], "criterion_type": f["criterion_type"],
            "original_text": f["original_text"], "rule_text_shown": ec.full_text(f),
            "simplifications": " | ".join(f["simplifications"]) or "none",
            "never_mentioned_disjuncts": ", ".join(f["other_disjuncts"]) or "none", "program": ec.program_text(f),
            "executed_tests": tests, "near_miss_kinds": ", ".join(ec.kinds(f)),
            "groups": len({r["tid"] for r in recs}),
            "example_base": case["base"]["case_text"], "example_flip": case["flip"]["case_text"],
            "example_near": case["near"]["case_text"],
            "example_answers": f"near-miss kind {case['near']['nm_kind']}: base not met, flip met, near-miss not met",
            **{c: "" for c in COLS[15:]}}


def prepare():
    src = json.loads((KIT / "formalized.json").read_text(encoding="utf-8"))
    sel = {json.loads(l)["cand"]: json.loads(l) for l in open(KIT / "selected.jsonl", encoding="utf-8")}
    items = [dict(f, original_text=sel[f["cand"]]["text"], nct_id=sel[f["cand"]]["nct_id"],
                  criterion_type=sel[f["cand"]]["type"]) for f in src["items"]]
    keep, recs, excl = render(items)
    ok, sc = shortcut_check(recs)
    with open(SHEET, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for f in keep:
            w.writerow(sheet_row(f, [r for r in recs if r["rid"] == f"ec_{f['cand']}"]))
    with open(KIT / "EXCLUSIONS.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["crit_id", "nct_id", "type", "original_text", "reason"])
        for f, why in excl:
            w.writerow([f["cand"], f["nct_id"], f["criterion_type"], f["original_text"], why])
    d = ROOT / "data" / "ec_v1" / "unsigned"
    d.mkdir(parents=True, exist_ok=True)
    (d / "records.jsonl").write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs), encoding="utf-8",
                                     newline="\n")
    summary = {"candidates": len(items), "accepted_by_agents": sum(f["final"] == "accept" for f in items),
               "kept": len(keep), "excluded": len(excl), "groups": len({r["tid"] for r in recs}),
               "records": len(recs), "by_concept": dict(Counter(f["concept"] for f in keep)),
               "by_type": dict(Counter(f["criterion_type"] for f in keep)),
               "by_times": dict(Counter(f["times"] for f in keep if f["input"] == "finding")),
               "by_kind": dict(Counter(r["nm_kind"] for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s")),
               "trials": len({f["nct_id"] for f in keep}), "shortcut_validation": {"result": "PASS" if ok else "FAIL",
                                                                                     "scorers": sc}}
    (KIT / "prepare_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))
    if not ok:
        sys.exit("shortcut validation FAILED")


def freeze():
    rows = list(csv.DictReader(open(SHEET, encoding="utf-8")))
    yes = lambda v: v.strip().lower() in ("yes", "y", "ok")  # noqa: E731
    approved = {r["crit_id"] for r in rows if r["reviewer_1"].strip() and r["reviewer_2"].strip()
                and r["reviewer_1"].strip() != r["reviewer_2"].strip()
                and all(yes(r[c]) for c in ("program_ok_1", "cases_ok_1", "program_ok_2", "cases_ok_2"))}
    pending = [r["crit_id"] for r in rows if not (r["program_ok_1"].strip() and r["program_ok_2"].strip())]
    if pending:
        sys.exit(f"refusing to freeze: {len(pending)} criteria lack two sign-offs")
    src = json.loads((KIT / "formalized.json").read_text(encoding="utf-8"))
    sel = {json.loads(l)["cand"]: json.loads(l) for l in open(KIT / "selected.jsonl", encoding="utf-8")}
    items = [dict(f, original_text=sel[f["cand"]]["text"], nct_id=sel[f["cand"]]["nct_id"],
                  criterion_type=sel[f["cand"]]["type"]) for f in src["items"] if f["cand"] in approved]
    keep, recs, _ = render(items)
    ok, sc = shortcut_check(recs)
    if not ok:
        sys.exit("shortcut validation FAILED")
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    if registry.get("ec_v1/test", {}).get("frozen"):
        sys.exit("refusing to rebuild: ec_v1/test is frozen")
    d = ROOT / "data" / "ec_v1" / "test"
    d.mkdir(parents=True, exist_ok=True)
    lines = "".join(json.dumps(r, sort_keys=True) + "\n" for r in recs)
    (d / "records.jsonl").write_text(lines, encoding="utf-8", newline="\n")
    sha = hashlib.sha256(lines.encode("utf-8")).hexdigest()
    created = datetime.date.today().isoformat()
    man = {"name": "test", "set": "ec_v1", "split": "test", "level": "registered", "created": created, "frozen": True,
           "generator": "scripts/build_ec_v1.py (selrm/ec.py)", "criteria": len(keep),
           "trials": len({f["nct_id"] for f in keep}), "n_groups": len({r["tid"] for r in recs}), "n_records": len(recs),
           "sha256": sha, "git_commit": D.git_commit(), "signed_off": sorted(approved),
           "rejected_at_signoff": sorted(r["crit_id"] for r in rows if r["crit_id"] not in approved),
           "shortcut_validation": {"result": "PASS", "scorers": sc}}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    registry["ec_v1/test"] = {"path": "ec_v1/test/records.jsonl", "split": "test", "level": "registered",
                              "tier": "easy", "n_groups": man["n_groups"], "n_records": len(recs),
                              "manifest": "ec_v1/test/MANIFEST.json", "frozen": True, "created": created, "sha256": sha}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(f"ec_v1/test frozen: {len(keep)} criteria, {man['n_groups']} groups, sha256 {sha[:16]}")


if __name__ == "__main__":
    {"prepare": prepare, "freeze": freeze}[sys.argv[1]]()
