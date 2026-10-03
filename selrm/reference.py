"""Program views of a record (A-D13).

render_check_code(rec): Python source that states the case's values for every
criterion of the rule, applies the stated rule and prints "+" if the record's
claim is correct, else "-" (GenPRM-style verifier targets; B).
reference_graph(rec): decisive findings and criteria as nodes, with the
mentions that do or do not count for each criterion (graph reward; D).
Both execute the same program as the labels: running the code reproduces
rec["label"] (tests/test_reference.py).
"""
from __future__ import annotations

from selrm.rules import Mention

_RULES = {}


def _rule(rec):
    if not _RULES:
        from selrm.datasets import RULES_BY_ID
        _RULES.update(RULES_BY_ID)
    return _RULES[rec["rid"]]


def mentions_with_quotes(rec):
    """[(Mention, quoted line)] in case order (case lines align with meta.tpl)."""
    lines = rec["case_text"].split("\n")[2:]          # after header and setting
    state = iter(rec["state"])
    return [(Mention(**next(state)), line) for line, t in zip(lines, rec["meta"]["tpl"])
            if not t.startswith("filler/")]


def _claim_value(rule, rec):
    """What the claim asserts: 1 = the flipped answer (s'), 0 = the default (s)."""
    return int(rec["claim_role"] == "s_prime")


def render_check_code(rec):
    rule, ov = _rule(rec), rec["meta"]["overrides"]
    ms = mentions_with_quotes(rec)
    out = [f"# Rule: {rec['rule_text']}", f"# Claim: {rec['claim_text']}", ""]
    if rec["case_kind"] == "missing":
        out += ["# The decisive input is not recorded in the case, so neither claim is supported.",
                'print("-")']
        return "\n".join(out) + "\n"
    names = []
    for c in rule.criteria:
        var = f"c_{c.cid}"
        names.append((c, var))
        mine = [(m, q) for m, q in ms if m.concept == c.concept]
        out.append(f"# Criterion {c.cid}: {c.label}")
        for m, q in mine:
            counts = c.applies(m) and m.status == "present"
            why = "counts" if counts else (
                "another person" if m.subject != "patient" and not c.applies(m) else
                "past, not counted" if m.time == "past" and not c.applies(m) else "absent")
            out.append(f"#   {q!r}: {why}")
        if c.kind == "numeric":
            thr = ov.get(c.cid, c.threshold)
            vals = [m.value for m, _ in mine if c.applies(m) and m.status == "present"]
            out.append(f"value_{c.cid} = {vals[0]!r}")
            out.append(f"{var} = value_{c.cid} {c.op} {thr!r}")
        else:
            hit = any(c.applies(m) and m.status == "present" for m, _ in mine)
            out.append(f"{var} = {hit!r}")
        out.append("")
    if rule.kind == "score":
        c = rule.crit(rec["cid"])
        out.append(f"answer = int(c_{c.cid})   # 1: the criterion contributes {c.points}, 0: none")
    elif rule.logic == "any":
        out.append(f"answer = int({' or '.join(v for _, v in names)})")
    elif rule.logic == "all":
        out.append(f"answer = int({' and '.join(v for _, v in names)})")
    else:
        pts = " + ".join(f"{c.points} * {v}" for c, v in names)
        out.append(f"answer = int({pts} >= {rule.cutoff})")
    if rec["claim_type"] == "criterion":
        out.append(f"answer = int(c_{rec['cid']})")
    out.append(f"claim = {_claim_value(rule, rec)}   # 1: the claim asserts the flipped answer")
    out.append('print("+" if answer == claim else "-")')
    return "\n".join(out) + "\n"


def reference_graph(rec):
    rule, ov = _rule(rec), rec["meta"]["overrides"]
    ms = mentions_with_quotes(rec)
    nodes, edges = [], []
    for c in rule.criteria:
        mine = [(i, m, q) for i, (m, q) in enumerate(ms) if m.concept == c.concept]
        known = rec["case_kind"] != "missing" or c.cid != rec["cid"]
        holds = bool(c.evaluate([m for _, m, _ in mine], ov.get(c.cid))) if known else None
        nodes.append({"id": f"c:{c.cid}", "type": "criterion", "text": c.label, "holds": holds,
                      "decisive": c.cid == rec["cid"]})
        for i, m, q in mine:
            if not any(n["id"] == f"m:{i}" for n in nodes):
                nodes.append({"id": f"m:{i}", "type": "mention", "quote": q, "subject": m.subject,
                              "status": m.status, "time": m.time})
            edges.append({"from": f"m:{i}", "to": f"c:{c.cid}",
                          "relation": "counts" if c.applies(m) and m.status == "present" else "does not count"})
        edges.append({"from": f"c:{c.cid}", "to": "conclusion", "relation": "input"})
    nodes.append({"id": "conclusion", "type": "conclusion", "claim": rec["claim_text"],
                  "correct": bool(rec["label"])})
    return {"iid": rec["iid"], "nodes": nodes, "edges": edges}
