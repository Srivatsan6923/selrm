"""Role D checks: selection on a synthetic pool, key resolution of make_tables, prose
preservation of update_paper. python -m pytest -q tests/test_role_d.py"""
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "scripts", f"{name}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def write_pool(d, qs, samples):
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "questions.jsonl"), "w") as f:
        f.writelines(json.dumps(q) + "\n" for q in qs)
    with open(os.path.join(d, "samples.jsonl"), "w") as f:
        f.writelines(json.dumps(s) + "\n" for s in samples)
    open(os.path.join(d, "DONE"), "w").close()


def test_selection(tmp_path):
    se = load("select_eval")
    qs = [{"qid": f"q{i}", "answer": "A", "options": {"A": 1, "B": 2}} for i in range(4)]
    # sample 0 wrong everywhere, sample 1 right; sample 2 ineligible
    ss = [{"qid": f"q{i}", "sample": k, "final": "B" if k == 0 else "A", "eligible": k != 2, "steps": ["x"]}
          for i in range(4) for k in range(3)]
    write_pool(tmp_path / "pools" / "medqa_test", qs, ss)
    write_pool(tmp_path / "pools" / "medqa_dev", qs, ss)
    for pool in ("medqa_test", "medqa_dev"):
        d = tmp_path / "scores" / pool
        os.makedirs(d, exist_ok=True)
        for n, good in (("medprm", 1), ("ledger2-triplets", 0), ("ledger2-blocks", 1)):
            with open(d / f"{n}.jsonl", "w") as f:   # 'good' scorers prefer the right sample
                f.writelines(json.dumps({"qid": s["qid"], "sample": s["sample"],
                                         "score": (2.0 if (s["sample"] == 1) == bool(good) else -2.0)}) + "\n"
                             for s in ss)
    sys.argv = ["x", "--pools", str(tmp_path / "pools"), "--scores", str(tmp_path / "scores"),
                "--out", str(tmp_path / "res"), "--pool", "medqa_test"]
    se.main()
    acc = {r: json.load(open(tmp_path / "res" / r / "summary_sel~medqa_test.json"))["acc"]
           for r in ("D-SEL-single", "D-SEL-oracle", "D-SEL-stepcheck", "D-SEL-ledger", "D-SEL-combined")}
    # the ledger scorer prefers the wrong sample; the minimum with a good step check still picks right
    assert acc == {"D-SEL-single": 0.0, "D-SEL-oracle": 100.0, "D-SEL-stepcheck": 100.0,
                   "D-SEL-ledger": 0.0, "D-SEL-combined": 100.0}, acc


def test_keys():
    mt = load("make_tables")
    assert mt.resolve("run/no-such-run/L2/all/TA")[1] == mt.TBD
    assert mt.resolve("bad/key")[1] == mt.TBD
    assert mt.fmt(0.0017, "pct2") == "0.17" and mt.fmt(1234, "int") == "1{,}234"


def test_update_paper_keeps_prose():
    up = load("update_paper")
    t = "a\n% <tables:x>\nold\n% </tables:x>\nb\n\\placeholderstrue"
    t2 = "a\n% <tables:x>\nnew\nrows\n% </tables:x>\nb\n\\placeholdersfalse"
    assert up.outside(t) == up.outside(t2)
    assert up.outside(t) != up.outside(t.replace("b", "c"))
