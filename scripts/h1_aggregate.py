"""H1 result: the authors' answers (audit/h1/answers_<name>.csv) against the program's (audit/h1/key.csv).

  python scripts/h1_aggregate.py     # writes results/A-H1/summary.json and audit/h1/disagreements.csv

Agreement with the program's answer and the share of cases whose facts the author confirmed, overall
and by set, near-miss kind and case kind; every disagreement and every reported problem is listed for
review. Numbers reach the paper only through results/A-H1/summary.json (sum/A-H1/<field>).
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "audit" / "h1"


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def norm(x):
    x = (x or "").strip().lower().replace("’", "'")
    return {"s'": "s'", "s_prime": "s'", "sprime": "s'", "s": "s", "neither": "neither", "y": "y", "yes": "y",
            "n": "n", "no": "n"}.get(x, x)


def main():
    key = {r["case"]: r for r in csv.DictReader(open(H1 / "key.csv", encoding="utf-8"))}
    rows = []
    for f in sorted(H1.glob("answers_*.csv")):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r["case"] in key and (r.get("q1_facts_ok") or r.get("q2_conclusion")):
                rows.append((f.stem[len("answers_"):], r, key[r["case"]]))
    out = {"run_id": "A-H1", "answer_files": sorted(f.name for f in H1.glob("answers_*.csv")), "rows": len(rows)}
    by = defaultdict(lambda: Counter())
    dis = []
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
        if q1 == "n" or q2 != k["conclusion_answer"] or (k["criterion_answer"] and q3 != k["criterion_answer"]):
            dis.append({"author": who, "case": r["case"], "tid": k["tid"], "case_kind": k["case_kind"],
                        "program_conclusion": k["conclusion_answer"], "author_conclusion": q2,
                        "program_criterion": k["criterion_answer"], "author_criterion": q3, "q1_facts_ok": q1,
                        "problem_type": r.get("problem_type", ""), "note": r.get("note", "")})
    for dim, c in by.items():
        out[dim.replace("/", "~")] = {"n": c["n"], "q1_facts_ok_pct": pct(c["q1_yes"], c["n"]),
                                      "q2_agree_pct": pct(c["q2_agree"], c["n"]),
                                      "q3_agree_pct": pct(c["q3_agree"], c["q3_n"]), "q3_n": c["q3_n"]}
    out["problem_types"] = dict(Counter(d["problem_type"] for d in dis if d["problem_type"]))
    out["disagreements"] = len(dis)
    d = ROOT / "results" / "A-H1"
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
    (d / "DONE").write_text("", encoding="utf-8")
    with open(H1 / "disagreements.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["author", "case", "tid", "case_kind", "program_conclusion",
                                          "author_conclusion", "program_criterion", "author_criterion",
                                          "q1_facts_ok", "problem_type", "note"])
        w.writeheader()
        w.writerows(dis)
    print(json.dumps({k: out[k] for k in ("rows", "disagreements")} | {"all": out.get("all")}))


if __name__ == "__main__":
    main()
