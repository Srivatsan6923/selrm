"""Offline checks of selrm/judges.py with a fake client. Run: python tests/test_judges.py"""
import os, re, shutil, sys, tempfile, types
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import judges as J
from selrm import metrics as M


def rec(tid, kind, role, label, case):
    return {"iid": f"{tid}/{kind}/conclusion/{role}", "tid": tid, "case_kind": kind, "claim_role": role,
            "claim_type": "conclusion", "label": label, "rule_text": "Rule.", "case_text": case,
            "claim_text": "Give drug X." if role == "s" else "Do not give drug X.", "rid": "r", "nm_kind": "time",
            "tier": "easy", "level": "L2", "family": "f", "condition": "c"}


class Fake:
    """Answers from a truth table {case_text: correct claim text}; mode 'perfect' or 'first' (always A)."""

    def __init__(self, truth, mode):
        self.truth, self.mode, self.n = truth, mode, 0
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self.create))

    def create(self, model, messages, **kw):
        self.n += 1
        text = messages[-1]["content"]
        case = re.search(r"Case:\n(.*?)\n\n", text, re.S).group(1)
        if "Which statement" in text:
            a = re.search(r"\nA\. (.*)\n", text).group(1)
            ans = "A" if (self.mode == "first" or a == self.truth[case]) else "B"
            content = f"Reasoning...\n**Answer: {ans}**"
        else:
            claim = re.search(r"Claim: (.*)\n", text).group(1)
            content = "+" if self.truth.get(case) == claim else "-"
        msg = types.SimpleNamespace(content=content, reasoning=None)
        ch = types.SimpleNamespace(message=msg, finish_reason="stop", logprobs=None)
        return types.SimpleNamespace(choices=[ch], usage=types.SimpleNamespace(prompt_tokens=10, completion_tokens=5, cost=0.001),
                                     model=model)


def setup():
    recs, truth = [], {}
    for i in range(6):
        for kind, ok_s in (("base", True), ("flip", False), ("near", True)):
            case = f"Case {i} {kind}."
            truth[case] = "Give drug X." if ok_s else "Do not give drug X."
            recs += [rec(f"t{i}", kind, "s", int(ok_s), case), rec(f"t{i}", kind, "s_prime", int(not ok_s), case)]
        case = f"Case {i} missing."
        recs += [rec(f"t{i}", "missing", "s", 0, case), rec(f"t{i}", "missing", "s_prime", 0, case)]
    return recs, truth


def run(mode):
    recs, truth = setup()
    tmp = tempfile.mkdtemp()
    try:
        cfg = {"name": "fake", "id": "fake/model", "readout": "choice", "params": {}, "price_in": 1, "price_out": 1}
        fake = Fake(truth, mode)
        judge = J.Judge(cfg, fake, J.Cache(tmp), workers=4)
        pairs = [(recs[j], recs[j + 1]) for j in range(0, len(recs), 2) if recs[j]["case_kind"] != "missing"]
        res = judge.score_pairs(pairs)
        u = {}
        for (s, sp), r in zip(pairs, res):
            u[s["iid"]], u[sp["iid"]] = r["d"] / 2, -r["d"] / 2
        point = [r for r in recs if r["case_kind"] == "missing"]
        for r, x in zip(point, judge.score_pointwise(point)):
            u[r["iid"]] = x["u"]
        calls = fake.n
        judge.score_pairs(pairs)                                  # second pass: all from the cache
        assert fake.n == calls and judge.usage["cached"] == len(pairs) * 2
        T = M.decisions(recs, [u[r["iid"]] for r in recs])
        return M.summarise(T)["all"], M.missing_rejection(recs, [u[r["iid"]] for r in recs], 0.0)
    finally:
        shutil.rmtree(tmp)


def test_parsers():
    assert J.parse_choice("blah\nAnswer: B") == "B" and J.parse_choice("**Answer: a**") == "A"
    assert J.parse_choice("Answer: A ... wait. Answer: B") == "B" and J.parse_choice("I pick B") is None
    assert J.parse_sign("+") == "+" and J.parse_sign("- because") == "-" and J.parse_sign("text\n+") == "+"
    assert J.parse_sign("Answer: -") == "-" and J.parse_sign("maybe") is None


def test_perfect_and_order_biased():
    allm, mr = run("perfect")
    assert allm["TA"] == 100.0 and allm["Tie"] == 0.0 and mr["MR"] == 100.0
    allm, _ = run("first")                                        # always 'A': split decisions -> ties
    assert allm["TA"] == 0.0 and allm["Tie"] == 100.0


def test_cost():
    cfg = {"price_in": 2.0, "price_out": 10.0}
    c = J.estimate_cost(cfg, ["x" * 350] * 10, 100)
    assert abs(c - (10 * 108 * 2.0 + 10 * 100 * 10.0) / 1e6) < 1e-12


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
