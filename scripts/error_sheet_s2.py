"""Failure sheet for stage 2 (H4; STAGE2_TASKS_D D8): 100 failures of the best system on MedCalc-V edits.

  python scripts/error_sheet_s2.py

System: the verdict-only verifier trained on rule triplets (C-S2-mcv-verdict-triplets-s0..4), set
mcv_v1/edits_test, human-written notes. A triplet fails unless d(base) > 0, d(flip) < 0 and d(near) > 0 on its
criterion claim (d = u(s) - u(s_prime), from the run's per-example scores; a tie is a failure). 50 failures per
edit type (value, sentence), dealt round robin over the five seeds, drawn with random.Random("error-sheet-s2").
Needs the frozen records (python scripts/build_mcv_v1.py --restore). Writes audit/s2/error_sheet_mcv.csv and
audit/s2/error_sheet_mcv_part{1..4}.csv (25 rows each, one per author). Coding columns are left empty; the
categories are those of audit/ERROR_CODING.md.
"""
import csv
import difflib
import hashlib
import json
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from selrm.metrics import _flags, decisions  # noqa: E402

SET, PER_TYPE, PARTS = "mcv_v1/edits_test", 50, 4
RUNS = [f"C-S2-mcv-verdict-triplets-s{k}" for k in range(5)]
CODING = ("category", "subcategory_or_note", "coder", "second_coder_category", "agreed")


def changed(base, other):
    """the sentences of `other` that are not in `base` (the edit), and the sentences of `base` it replaced"""
    split = lambda s: [x for x in re.split(r"(?<=[.!?])\s+|\n", s) if x]      # notes are long paragraphs: by sentence
    a, b = split(base), split(other)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out += [f"- {x}" for x in a[i1:i2]] + [f"+ {x}" for x in b[j1:j2]]
    return "\n".join(out)


def main():
    reg = json.load(open(f"{ROOT}/data/REGISTRY.json", encoding="utf-8"))[SET]
    path = f"{ROOT}/data/{reg['path']}"
    assert hashlib.sha256(open(path, "rb").read()).hexdigest() == reg["sha256"], "records differ from the registry"
    recs = [json.loads(line) for line in open(path, encoding="utf-8")]
    recs = [r for r in recs if r["note_type"] == "human"]
    by = {(r["tid"], r["case_kind"], r["claim_role"]): r for r in recs}
    avail = {"value": [], "sentence": []}
    T = {}
    for run in RUNS:
        assert os.path.exists(f"{ROOT}/results_git/{run}/DONE"), run
        S = {x["iid"]: x["u"] for x in map(json.loads, open(
            f"{ROOT}/results_git/{run}/scores_{SET.replace('/', '~')}.jsonl", encoding="utf-8"))}
        T[run] = decisions(recs, [S[r["iid"]] for r in recs], claim_type="criterion")
        for tid, t in sorted(T[run].items()):
            f = _flags(t)
            if f is not None and not f["TA"]:
                avail[by[tid, "base", "s"]["edit_type"]].append((run, tid))
    rng = random.Random("error-sheet-s2")
    picked = []
    for et in ("value", "sentence"):
        per_run = {run: [x for x in avail[et] if x[0] == run] for run in RUNS}
        for v in per_run.values():
            rng.shuffle(v)
        take = []
        while len(take) < PER_TYPE and any(per_run.values()):      # round robin over the seeds
            for run in RUNS:
                if per_run[run] and len(take) < PER_TYPE:
                    take.append(per_run[run].pop())
        picked += [(et, run, tid) for run, tid in take]
    rows = []
    for n, (et, run, tid) in enumerate(picked):
        d = T[run][tid]["d"]
        r = {c: by[tid, c, "s"] for c in ("base", "flip", "near")}
        failed = [c + (" (tie)" if d[c] == 0 else "") for c, ok in
                  (("base", d["base"] > 0), ("flip", d["flip"] < 0), ("near", d["near"] > 0)) if not ok]
        rows.append({"sheet_id": f"M{n + 1:03d}", "part": n % PARTS + 1, "run_id": run, "tid": tid,
                     "score": r["base"]["family"], "item": r["base"]["condition"], "edit_type": et,
                     "nm_kind": r["base"]["nm_kind"], "stratum": r["base"]["stratum"],
                     "failed_conditions": ", ".join(failed),
                     "d_base": round(d["base"], 3), "d_flip": round(d["flip"], 3), "d_near": round(d["near"], 3),
                     "claim_s": r["base"]["claim_text"], "claim_s_prime": by[tid, "base", "s_prime"]["claim_text"],
                     "values": json.dumps(r["base"]["meta"].get("value"), ensure_ascii=False),
                     "rule_text": r["base"]["rule_text"], "case_text_base": r["base"]["case_text"],
                     "edit_flip": changed(r["base"]["case_text"], r["flip"]["case_text"]),
                     "edit_near": changed(r["base"]["case_text"], r["near"]["case_text"])} | dict.fromkeys(CODING, ""))
    out = f"{ROOT}/audit/s2"
    os.makedirs(out, exist_ok=True)
    for name, sel in [("error_sheet_mcv.csv", rows)] + [
            (f"error_sheet_mcv_part{p}.csv", [r for r in rows if r["part"] == p]) for p in range(1, PARTS + 1)]:
        with open(f"{out}/{name}", "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(sel)
    n_all = {et: len(v) for et, v in avail.items()}
    print(f"{len(rows)} rows; failures available: {n_all}; triplets per run: {len(T[RUNS[0]])}")
    assert len(rows) == 2 * PER_TYPE and all(r["failed_conditions"] for r in rows)


if __name__ == "__main__":
    main()
