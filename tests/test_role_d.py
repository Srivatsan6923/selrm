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
    for pool in ("medqa_test", "medqa_dev", "medqa_kp"):
        write_pool(tmp_path / "pools" / pool, qs, ss)
        json.dump({"n_questions": 4, "n_samples": 12, "ineligible_share": 0.3333},
                  open(tmp_path / "pools" / pool / "MANIFEST.json", "w"))
    for pool in ("medqa_test", "medqa_dev", "medqa_kp"):
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
    acc = {r: json.load(open(tmp_path / "res" / r / "summary_sel~medqa.json"))["acc"]
           for r in ("D-SEL-single", "D-SEL-oracle", "D-SEL-stepcheck", "D-SEL-ledger", "D-SEL-combined")}
    # the ledger scorer prefers the wrong sample; the minimum with a good step check still picks right
    assert acc == {"D-SEL-single": 0.0, "D-SEL-oracle": 100.0, "D-SEL-stepcheck": 100.0,
                   "D-SEL-ledger": 0.0, "D-SEL-combined": 100.0}, acc
    se.PAIRS, se.KPQ = [("q0", "q1"), ("q2", "q3")], {"q0"}   # key-pair pool; q0 leaves the calibration set
    sys.argv[-1] = "medqa_kp"
    se.main()
    kp = {r: json.load(open(tmp_path / "res" / r / "summary_sel~keypairs.json"))["pair_acc"]
          for r in ("D-SEL-single", "D-SEL-combined")}
    assert kp == {"D-SEL-single": 0.0, "D-SEL-combined": 100.0}, kp
    cal = json.load(open(tmp_path / "res" / "D-CAL" / "summary.json"))
    assert (cal["excluded_keypair_questions"], cal["n_traces"]) == (1, 6), cal
    cmp = json.load(open(tmp_path / "res" / "D-SEL-comparisons.json"))   # kept across the two runs
    assert cmp["sel-mqa-comb-step"]["diff"] == 0.0 and cmp["sel-key-comb-step"]["n_clusters"] == 2, cmp
    assert se.compare({"a": 1, "b": 0}, {"a": 0, "b": 0})["diff"] == 50.0
    se2 = load("select_eval")
    assert se2.keypair_acc([("a", "b"), ("c", "d"), ("e", "z")], {"a": 1, "b": 1, "c": 1, "d": 0, "e": 1}) == (50.0, 2)
    qs2 = {f"m-{c}-{t}": {"meta": {"case_id": c, "case_type": t}} for c in ("x", "y") for t in ("control", "trap")}
    rows = [{"qid": "m-x-control", "correct": True}, {"qid": "m-x-trap", "correct": True},
            {"qid": "m-y-control", "correct": True}, {"qid": "m-y-trap", "correct": False}]
    assert se2.pair_metrics(qs2, rows) == {"control_acc": 100.0, "trap_acc": 50.0, "pair_acc": 50.0, "n_pairs": 2}


def test_keys():
    mt = load("make_tables")
    assert mt.resolve("run/no-such-run/L2/all/TA")[1] == mt.TBD
    assert mt.resolve("bad/key")[1] == mt.TBD
    assert mt.fmt(0.0017, "pct2") == "0.17" and mt.fmt(1234, "int") == "1{,}234"


def test_update_paper_keeps_prose():
    g = load("grpo_d")   # base-flip pairs and whole triplets from per-example rows
    rows = [{"tid": "a", "case_kind": k, "correct": k != "near"} for k in ("base", "flip", "near")] + \
           [{"tid": "b", "case_kind": k, "correct": k == "flip"} for k in ("base", "flip", "near")]
    assert {k: g.accuracy(rows)[k] for k in ("pair", "triplet", "flip")} == {"pair": 50.0, "triplet": 0.0, "flip": 100.0}
    # xr_v1: one item = two rules x three cases; solved only if all six conclusion choices are right
    recs = [{"iid": f"{t}/{k}/conclusion/{role}", "tid": t, "case_kind": k, "claim_type": "conclusion",
             "claim_role": role, "label": int((role == "s") == (k != "negative")), "nm_kind": "window", "rid": t,
             "tier": "rule_side", "level": "xr", "family": "window", "meta": {"xr": {"item": 0}}}
            for t in ("r1", "r2") for k in g.XR_KINDS for role in ("s", "s_prime")]
    ans = [{"iid_a": f"{t}/{k}/conclusion/s", "iid_b": f"{t}/{k}/conclusion/s_prime",
            "answer": "A" if k != "negative" else "B"} for t in ("r1", "r2") for k in g.XR_KINDS]
    assert g.crossed(ans, recs)["XA"] == 100.0
    ans[0]["answer"] = None          # one unanswered cell is a tie and fails the item
    assert g.crossed(ans, recs)["XA"] == 0.0
    # TrialGPT: truth from the claim labels, N/A left out, no final answer = NEI
    tg = [{"tid": t, "iid": f"{t}/{r}", "claim_role": r, "label": lab, "meta": {"expert_eligibility": e}}
          for t, (ls, lp, e) in {"m": (1, 0, "included"), "n": (0, 1, "not included"), "x": (0, 0, "not enough information"),
                                 "na": (0, 0, "not applicable")}.items() for r, lab in (("s", ls), ("s_prime", lp))]
    rows = [{"tid": t, "iid_a": f"{t}/s", "iid_b": f"{t}/s_prime", "answer": a} for t, a in
            (("m", "A"), ("n", "A"), ("x", None), ("na", "A"))]
    assert g.tg_classes(rows, tg) == (["met", "not met", "NEI"], ["met", "met", "NEI"])
    up = load("update_paper")
    t = "a\n% <tables:x>\nold\n% </tables:x>\nb\n\\placeholderstrue"
    t2 = "a\n% <tables:x>\nnew\nrows\n% </tables:x>\nb\n\\placeholdersfalse"
    assert up.outside(t) == up.outside(t2)
    assert up.outside(t) != up.outside(t.replace("b", "c"))
