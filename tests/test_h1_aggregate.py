import csv
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("h1", Path(__file__).parents[1] / "scripts" / "h1_aggregate.py")
h1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h1)

KEY = [{"author": "author1", "case": f"A1-G01-C{i}", "tid": "t1", "set": "rule_v1/test_L2", "case_kind": k,
        "near_miss_kind": "negation", "tier": "easy", "level": "L2", "conclusion_answer": a, "criterion_answer": c}
       for i, (k, a, c) in enumerate((("base", "s", "s"), ("flip", "s'", "s'"), ("near", "s", "")), 1)]


def _write(path, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:         # Excel's 'CSV UTF-8' adds a BOM
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def _run(tmp_path, monkeypatch, answers, name="answers_author1.csv"):
    monkeypatch.setattr(h1, "ROOT", tmp_path)
    monkeypatch.setattr(h1, "H1", tmp_path)
    _write(tmp_path / "key.csv", KEY)
    _write(tmp_path / name, [{"case": c, "q1_facts_ok": a, "q2_conclusion": b, "q3_criterion": q, "problem_type": p,
                              "note": ""} for c, a, b, q, p in answers])
    h1.main()
    return json.loads((tmp_path / "results" / "A-H1" / "summary.json").read_text(encoding="utf-8")), \
        list(csv.DictReader(open(tmp_path / "disagreements.csv", encoding="utf-8")))


def test_agreeing_rows_with_a_problem_are_listed(tmp_path, monkeypatch):
    out, review = _run(tmp_path, monkeypatch, [("A1-G01-C1", "Y", "s", "s", "wording"),
                                               ("A1-G01-C2", "y", "S’", "s′", ""),        # curly and prime apostrophes
                                               ("A1-G01-C3", "y", "neither.", "", "")])
    assert out["all"]["q2_agree_pct"] == 66.7 and out["all"]["q3_agree_pct"] == 100.0
    assert out["problem_types"] == {"wording": 1} and out["reported_problems_without_disagreement"] == 1
    assert {r["case"]: r["why"] for r in review} == {"A1-G01-C1": "reported problem", "A1-G01-C3": "disagreement"}


@pytest.mark.parametrize("answers", [[("A1-G01-C1", "y", "maybe", "s", "")],      # not an allowed value
                                     [("A1-G01-C1", "y", "s", "", "")],           # q3 left blank on a criterion row
                                     [("A1-G01-C3", "y", "s", "s", "")]])         # q3 on a row without criterion claims
def test_invalid_answers_stop_the_script(tmp_path, monkeypatch, answers):
    with pytest.raises(SystemExit):
        _run(tmp_path, monkeypatch, answers)


def test_named_answer_files_are_refused(tmp_path, monkeypatch):
    with pytest.raises(SystemExit, match="rename"):
        _run(tmp_path, monkeypatch, [("A1-G01-C1", "y", "s", "s", "")], name="answers_alice.csv")
