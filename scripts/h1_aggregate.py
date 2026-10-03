"""H1 result: the authors' answers (audit/h1/answers_<authorN>.csv) against the program's (audit/h1/key.csv).

  python scripts/h1_aggregate.py     # writes results/A-H1/summary.json and audit/h1/disagreements.csv

Agreement with the program's answer and the share of cases whose facts the author confirmed, overall
and by set, near-miss kind and case kind. Every disagreement and every row with a reported problem
or note is listed for review. A file with answers outside the allowed values, duplicated cases or
another author's cases is listed with the rows to correct and left out; the others are still scored.
The summary says per author how many of the key's rows are answered, and DONE is written only when
every row of the key is answered exactly once and no file was left out. Numbers reach the paper only
through results/A-H1/summary.json (sum/A-H1/<field>).
"""
import csv
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "audit" / "h1"
AUTHORS = ("author1", "author2", "author3", "author4")
QUESTIONS = ("q1_facts_ok", "q2_conclusion", "q3_criterion")
PROBLEMS = ("dropped negation", "wrong subject", "ambiguous time", "conflicting lines", "wording", "other")


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def norm(x):
    """Spelling variants of an allowed answer (curly or prime apostrophe, capitals, a final full stop)."""
    x = re.sub(r"[’‘′´`]", "'", (x or "").strip().lower()).rstrip(".").strip()
    return {"s_prime": "s'", "sprime": "s'", "s prime": "s'", "s '": "s'", "yes": "y", "no": "n"}.get(x, x)


def problem(x):
    """A problem type in its listed spelling ('Conflicting-lines' -> 'conflicting lines'), or the raw text."""
    x = re.sub(r"[\s_-]+", " ", (x or "").strip().lower()).rstrip(".")
    return next((p for p in PROBLEMS if x in (p, p + "s")), x)


def invalid(r, k):
    """The fields of answered row r that hold no allowed value."""
    q1, q2, q3 = (norm(r.get(q)) for q in QUESTIONS)
    p = problem(r.get("problem_type"))
    bad = [f"q1_facts_ok={r.get('q1_facts_ok')!r}"] if q1 not in ("y", "n") else []
    bad += [f"q2_conclusion={r.get('q2_conclusion')!r}"] if q2 not in ("s", "s'", "neither") else []
    if k["criterion_answer"] and q3 not in ("s", "s'", "neither"):
        bad.append(f"q3_criterion={r.get('q3_criterion')!r} (this row has criterion claims)")
    elif not k["criterion_answer"] and q3:
        bad.append(f"q3_criterion={r.get('q3_criterion')!r} (leave blank: no criterion claims)")
    if p and p not in PROBLEMS:
        bad.append(f"problem_type={r.get('problem_type')!r} (one of: {', '.join(PROBLEMS)})")
    if q1 == "n" and not p:
        bad.append("q1_facts_ok is n but problem_type is empty")
    return bad


def read(path):
    """Rows of a CSV saved by Excel or an editor: UTF-8 (with or without BOM), else Windows-1252."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252", errors="replace")
    return list(csv.DictReader(io.StringIO(text, newline="")))


def main():
    key = {r["case"]: r for r in read(H1 / "key.csv")}
    files = sorted(H1.glob("answers_*.csv"))
    named = [f.name for f in files if f.stem[len("answers_"):] not in AUTHORS]
    if named:
        sys.exit(f"rename to answers_<authorN>.csv (one of {', '.join(AUTHORS)}): {', '.join(named)}")
    rows, errors, left_out = [], [], []
    for f in files:
        who = f.stem[len("answers_"):]
        recs = read(f)
        missing = [c for c in ("case",) + QUESTIONS if recs and c not in recs[0]]
        if not recs or missing:
            errors.append(f"{f.name}: no rows or missing columns {missing}; save as 'CSV UTF-8 (comma delimited)' "
                          f"with the sheet's header")
            left_out.append(f.name)
            continue
        mine, bad = [], []
        seen = Counter((r.get("case") or "").strip() for r in recs if (r.get("case") or "").strip())
        bad += [f"{c} appears {n} times" for c, n in seen.items() if n > 1]
        for r in recs:
            c = (r.get("case") or "").strip()
            answered = any((r.get(q) or "").strip() for q in QUESTIONS + ("problem_type", "note"))
            if not answered:
                continue                                # not answered yet
            if c not in key:
                bad.append(f"unknown case {c!r}")
            elif key[c]["author"] != who:
                bad.append(f"{c} belongs to {key[c]['author']}")
            else:
                bad += [f"{c}: {b}" for b in invalid(r, key[c])]
                mine.append((who, r, key[c]))
        if bad:
            errors += [f"{f.name}: {b}" for b in bad]
            left_out.append(f.name)
        else:
            rows += mine
    for sheet in sorted(H1.glob("sheet_author*.csv")):  # answers typed into the sheet itself are not read
        who = sheet.stem[len("sheet_"):]
        if not (H1 / f"answers_{who}.csv").exists() and any(any((r.get(q) or "").strip() for q in QUESTIONS)
                                                            for r in read(sheet)):
            errors.append(f"{sheet.name} holds answers but answers_{who}.csv does not exist; save it under that name")
    expected = Counter(k["author"] for k in key.values())
    answered = Counter(who for who, _, _ in rows)
    out = {"run_id": "A-H1", "answer_files": [f.name for f in files], "files_left_out": left_out, "rows": len(rows),
           "rows_expected": len(key), "answered_by_author": {a: f"{answered[a]}/{expected[a]}" for a in sorted(expected)},
           "complete": len(rows) == len(key) and not left_out}
    by = defaultdict(lambda: Counter())
    review = []
    for who, r, k in rows:
        q1, q2, q3 = (norm(r.get(q)) for q in QUESTIONS)
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
        reported = problem(r.get("problem_type")) or (r.get("note") or "").strip()
        if disagree or reported:
            review.append({"author": who, "case": r["case"], "tid": k["tid"], "case_kind": k["case_kind"],
                           "why": "disagreement" if disagree else "reported problem",
                           "program_conclusion": k["conclusion_answer"], "author_conclusion": q2,
                           "program_criterion": k["criterion_answer"], "author_criterion": q3, "q1_facts_ok": q1,
                           "problem_type": problem(r.get("problem_type")), "note": (r.get("note") or "").strip()})
    for dim, c in by.items():
        out[dim.replace("/", "~")] = {"n": c["n"], "q1_facts_ok_pct": pct(c["q1_yes"], c["n"]),
                                      "q2_agree_pct": pct(c["q2_agree"], c["n"]),
                                      "q3_agree_pct": pct(c["q3_agree"], c["q3_n"]), "q3_n": c["q3_n"]}
    out["problem_types"] = dict(Counter(problem(r.get("problem_type")) for _, r, _ in rows
                                        if problem(r.get("problem_type"))))
    out["disagreements"] = sum(d["why"] == "disagreement" for d in review)
    out["reported_problems_without_disagreement"] = sum(d["why"] == "reported problem" for d in review)
    d = ROOT / "results" / "A-H1"
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
    (d / "DONE").unlink(missing_ok=True)
    if out["complete"]:
        (d / "DONE").write_text("", encoding="utf-8")
    with open(H1 / "disagreements.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["author", "case", "tid", "case_kind", "why", "program_conclusion",
                                          "author_conclusion", "program_criterion", "author_criterion",
                                          "q1_facts_ok", "problem_type", "note"])
        w.writeheader()
        w.writerows(review)
    print(json.dumps({k: out[k] for k in ("rows", "rows_expected", "answered_by_author", "complete", "disagreements",
                                          "reported_problems_without_disagreement")} | {"all": out.get("all")}))
    if errors:
        sys.exit("answers to correct (allowed: y/n for q1; s, s' or neither for q2 and q3; problem_type from the "
                 "README list, required when q1 is n); files with errors were left out:\n" + "\n".join(errors))


if __name__ == "__main__":
    main()
