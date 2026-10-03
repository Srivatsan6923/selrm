"""H1 result: the authors' answers (audit/h1/answers_<authorN>.csv) against the program's (audit/h1/key.csv).

  python scripts/h1_aggregate.py     # writes results/A-H1/summary.json and audit/h1/disagreements.csv

Agreement with the program's answer and the share of cases whose facts the author confirmed, overall
and by set, near-miss kind and case kind. Every disagreement and every row with a reported problem
or note is listed for review. Answers outside the allowed values stop the script with the rows to
correct, so nothing is scored silently. Numbers reach the paper only through
results/A-H1/summary.json (sum/A-H1/<field>).
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "audit" / "h1"
AUTHORS = ("author1", "author2", "author3", "author4")


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def norm(x):
    """Spelling variants of an allowed answer (curly or prime apostrophe, capitals, a final full stop)."""
    x = re.sub(r"[’‘′´`]", "'", (x or "").strip().lower()).rstrip(".").strip()
    return {"s_prime": "s'", "sprime": "s'", "s prime": "s'", "s '": "s'", "yes": "y", "no": "n"}.get(x, x)


def invalid(r, k):
    """The answer fields of row r that hold no allowed value."""
    q1, q2, q3 = norm(r.get("q1_facts_ok")), norm(r.get("q2_conclusion")), norm(r.get("q3_criterion"))
    bad = [f"q1_facts_ok={r.get('q1_facts_ok')!r}"] if q1 not in ("y", "n") else []
    bad += [f"q2_conclusion={r.get('q2_conclusion')!r}"] if q2 not in ("s", "s'", "neither") else []
    if k["criterion_answer"] and q3 not in ("s", "s'", "neither"):
        bad.append(f"q3_criterion={r.get('q3_criterion')!r} (this row has criterion claims)")
    elif not k["criterion_answer"] and q3:
        bad.append(f"q3_criterion={r.get('q3_criterion')!r} (leave blank: no criterion claims)")
    return bad


def main():
    key = {r["case"]: r for r in csv.DictReader(open(H1 / "key.csv", encoding="utf-8-sig", newline=""))}
    files = sorted(H1.glob("answers_*.csv"))
    named = [f.name for f in files if f.stem[len("answers_"):] not in AUTHORS]
    if named:
        sys.exit(f"rename to answers_<authorN>.csv (one of {', '.join(AUTHORS)}): {', '.join(named)}")
    rows, errors = [], []
    for f in files:
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")):
            if not any((r.get(q) or "").strip() for q in ("q1_facts_ok", "q2_conclusion", "q3_criterion")):
                continue                                # not answered yet
            if r.get("case") not in key:
                errors.append(f"{f.name}: unknown case {r.get('case')!r}")
                continue
            bad = invalid(r, key[r["case"]])
            if bad:
                errors.append(f"{f.name} {r['case']}: " + ", ".join(bad))
            rows.append((f.stem[len("answers_"):], r, key[r["case"]]))
    if errors:
        sys.exit("answers to correct (allowed: y/n for q1; s, s' or neither for q2 and q3):\n" + "\n".join(errors))
    out = {"run_id": "A-H1", "answer_files": [f.name for f in files], "rows": len(rows)}
    by = defaultdict(lambda: Counter())
    review = []
    for who, r, k in rows:
        q1, q2, q3 = norm(r.get("q1_facts_ok")), norm(r.get("q2_conclusion")), norm(r.get("q3_criterion"))
        for dim in ("all", f"set={k['set'].split('/')[-1]}", f"nm_kind={k['near_miss_kind']}",
                    f"case_kind={k['case_kind']}", f"author={who}"):
            c = by[dim]
            c["n"] += 1
            c["q1_yes"] += q1 == "y"
            c["q2_agree"] += q2 == k["conclusion_answer"]
            if k["criterion_answer"]:
                c["q3_n"] += 1
                c["q3_agree"] += q3 == k["criterion_answer"]
        disagree = q1 == "n" or q2 != k["conclusion_answer"] or (k["criterion_answer"] and q3 != k["criterion_answer"])
        reported = (r.get("problem_type") or "").strip() or (r.get("note") or "").strip()
        if disagree or reported:
            review.append({"author": who, "case": r["case"], "tid": k["tid"], "case_kind": k["case_kind"],
                           "why": "disagreement" if disagree else "reported problem",
                           "program_conclusion": k["conclusion_answer"], "author_conclusion": q2,
                           "program_criterion": k["criterion_answer"], "author_criterion": q3, "q1_facts_ok": q1,
                           "problem_type": (r.get("problem_type") or "").strip(), "note": (r.get("note") or "").strip()})
    for dim, c in by.items():
        out[dim.replace("/", "~")] = {"n": c["n"], "q1_facts_ok_pct": pct(c["q1_yes"], c["n"]),
                                      "q2_agree_pct": pct(c["q2_agree"], c["n"]),
                                      "q3_agree_pct": pct(c["q3_agree"], c["q3_n"]), "q3_n": c["q3_n"]}
    out["problem_types"] = dict(Counter((r.get("problem_type") or "").strip().lower() for _, r, _ in rows
                                        if (r.get("problem_type") or "").strip()))
    out["disagreements"] = sum(d["why"] == "disagreement" for d in review)
    out["reported_problems_without_disagreement"] = sum(d["why"] == "reported problem" for d in review)
    d = ROOT / "results" / "A-H1"
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
    (d / "DONE").write_text("", encoding="utf-8")
    with open(H1 / "disagreements.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["author", "case", "tid", "case_kind", "why", "program_conclusion",
                                          "author_conclusion", "program_criterion", "author_criterion",
                                          "q1_facts_ok", "problem_type", "note"])
        w.writeheader()
        w.writerows(review)
    print(json.dumps({k: out[k] for k in ("rows", "disagreements", "reported_problems_without_disagreement")}
                     | {"all": out.get("all")}))


if __name__ == "__main__":
    main()
