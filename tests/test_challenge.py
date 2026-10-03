import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("ch", Path(__file__).parents[1] / "scripts" / "challenge_v1.py")
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


def _line(text, keywords, concept):
    """A mock author line: the fact itself, with a required word where it is missing."""
    return text if ch.names(text, keywords, concept) else f"{text} ({keywords[0].strip()})"


def _notes(s):
    crit = ch.D.RULES_BY_ID[s["rid"]].crit(s["cid"])
    n = {"header": f"{s['patient']}.", "reason": s["setting"], "extra": [], "check_ok": "yes"}
    for f in s["facts"]:
        own = f["mention"]["concept"] == crit.concept
        n[f"fact {f['n']}"] = _line(f["text"], s["keywords"], crit.concept) if own else f["text"]
    n["FLIP"] = _line(s["edits"]["flip"]["text"], s["keywords"], crit.concept)
    n["NEAR"] = _line(s["edits"]["near"]["text"], s["keywords"], crit.concept)
    return n


def _form(gid, n):
    return "\n".join([f"## {gid}", f"header: {n['header']}", f"reason: {n['reason']}"]
                     + [f"{k}: {v}" for k, v in n.items() if k.startswith("fact ")]
                     + [f"FLIP: {n['FLIP']}", f"NEAR: {n['NEAR']}", f"check_ok: {n['check_ok']}", ""])


def test_mock_notes_assemble_with_program_labels(tmp_path):
    S = ch.specs()
    assert len(S) == 160 and {s["nm_kind"] for s in S} == {"numeric", "boundary", "subject", "negation", "time"}
    with open(tmp_path / "specs.jsonl", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(s) + "\n" for s in S)
    (tmp_path / "notes_mock.md").write_text("\n".join(_form(s["gid"], _notes(s)) for s in S), encoding="utf-8")
    recs, report = ch.assemble(kit_dir=tmp_path)
    assert report[-1].strip().startswith("accepted 160, rejected 0"), report[:5]
    by = {s["gid"]: s for s in S}
    for r in recs:
        if r["claim_type"] == "conclusion" and r["claim_role"] == "s_prime":
            assert r["label"] == by[r["tid"].split(".")[-1]]["labels"][r["case_kind"]]["conclusion"]
        for e in r["ledger"]:                       # base ledgers never quote the near-miss line
            assert e["found"] == "not mentioned" or e["found"] in r["case_text"]


def test_checks_reject_wrong_notes():
    S = ch.specs()
    num = next(s for s in S if s["nm_kind"] == "numeric")
    n = _notes(num)
    v = ch.E.fmt(num["edits"]["flip"]["mention"]["value"], ch.D.RULES_BY_ID[num["rid"]].crit(num["cid"]))
    n["FLIP"] = n["FLIP"].replace(v, "1" + v)
    assert any("value" in e for e in ch.check(num, n))
    neg = next(s for s in S if s["nm_kind"] == "negation")
    n = _notes(neg)
    n["NEAR"] = f"Has {neg['keywords'][0].strip()} at present."
    assert any("denial" in e for e in ch.check(neg, n))
    for s in S:                                     # a criterion the form leaves unmentioned, named in FLIP
        rule = ch.D.RULES_BY_ID[s["rid"]]
        stated = {m["concept"] for m in s["states"]["flip"] if m["form"] != "generic"}
        other = [c for c in rule.criteria if c.cid != s["cid"] and c.kind == "finding" and c.concept not in stated]
        if other:
            n = _notes(s)
            n["FLIP"] += f" Also has {other[0].keywords[0].strip()}."
            assert any("leaves unmentioned" in e for e in ch.check(s, n))
            break
    else:
        raise AssertionError("no group with an unmentioned criterion")
