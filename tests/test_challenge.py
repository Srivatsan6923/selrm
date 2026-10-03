import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("ch", Path(__file__).parents[1] / "scripts" / "challenge_v1.py")
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


def _line(text, keywords, concept):
    """A mock author line: the fact itself, with a required word where it is missing."""
    return text if ch.names(text, keywords, concept) else f"{text} ({keywords[0].strip()})"


def _notes(s):
    crit = ch.D.RULES_BY_ID[s["rid"]].crit(s["cid"])
    n = {"header": f"{s['patient']}.", "reason": s["setting"], "extra": []}
    for f in s["facts"]:
        own = f["mention"]["concept"] == crit.concept
        n[f"fact {f['n']}"] = _line(f["text"], s["keywords"], crit.concept) if own else f["text"]
    n["FLIP"] = _line(s["edits"]["flip"]["text"], s["keywords"], crit.concept)
    n["NEAR"] = _line(s["edits"]["near"]["text"], s["keywords"], crit.concept)
    n["check_ok"] = "yes " + ch.fingerprint(n, s)
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
    for a in ch.AUTHORS:                            # each group in its writer's file
        (tmp_path / f"notes_{a}.md").write_text("\n".join(_form(s["gid"], _notes(s)) for s in S if s["author"] == a),
                                                encoding="utf-8")
    recs, report = ch.assemble(kit_dir=tmp_path)
    assert report[-1].strip().startswith("accepted 160, awaiting check 0, rejected 0"), report[:5]
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


def test_checks_wording_and_approval(tmp_path):
    S = ch.specs()

    def errs(s, **lines):
        n = _notes(s)
        n.update(lines)
        return ch.check(s, n)

    def near(s, attr):
        return s["edits"]["near"]["mention"][attr]

    def has(es, word):
        return any(word in e for e in es)

    age = next(s for s in S if near(s, "concept") == "age")
    wt = next(s for s in S if near(s, "concept") == "weight" and near(s, "time") == "current")
    temp = next(s for s in S if near(s, "concept") == "temperature")
    v = {s["gid"]: ch.E.fmt(near(s, "value"), ch.D.RULES_BY_ID[s["rid"]].crit(s["cid"])) for s in (age, wt, temp)}
    assert not has(errs(age, NEAR=f"Age {v[age['gid']]}."), "value")             # a full stop after the number
    assert not has(errs(wt, NEAR=f"Weight {v[wt['gid']]}kg."), "unit")            # a unit straight after it
    assert not has(errs(temp, NEAR=f"Temperature {v[temp['gid']]}ºC."), "unit")
    assert has(errs(wt, NEAR=f"Weight 50 kg, previously {v[wt['gid']]} kg."), "exactly as given")

    over = next(s for s in S if near(s, "time") == "past" and near(s, "concept") == "pen_allergy")
    assert has(errs(over, NEAR="Penicillin allergy years ago."), "over")             # a date alone is not enough
    assert has(errs(over, NEAR="Still allergic to penicillin, as years ago."), "over")
    ok = errs(over, NEAR="Penicillin allergy as a child, outgrown.")              # 'child' is the patient's past
    assert len(ok) == 1 and has(ok, "awaiting the second author")

    rel = next(s for s in S if near(s, "subject") != "patient" and near(s, "concept") == "confusion")
    who = near(rel, "subject")
    assert has(errs(rel, NEAR=f"His {who} reports new confusion."), "not report it")
    assert not has(errs(rel, NEAR=f"His {who} has new confusion."), "report")
    assert not has(errs(rel, FLIP="New confusion, not his baseline."), "denial")      # denial after the name
    assert has(errs(rel, FLIP="No confusion."), "denial")

    neg = next(s for s in S if near(s, "status") == "absent" and near(s, "kind") == "finding")
    kw = neg["keywords"][0].strip()
    assert not has(errs(neg, NEAR=f"Non-{kw}."), "denial") and not has(errs(neg, NEAR=f"{kw.title()} absent."), "denial")
    assert has(errs(neg, extra=[f"Keen gardener; {kw}."]), "extra lines")

    male = next(s for s in S if s["patient"].endswith(" male") and s["patient"][0].isdigit())
    age_m = male["patient"].split("-")[0]
    assert not has(errs(male, header=f"{age_m}M."), "sex") and has(errs(male, header=f"Woman, {age_m}."), "sex")

    n = _notes(age)
    assert ch.check(age, n) == []
    n["reason"] += " Seen today."                   # any edit after approval needs a new check
    assert has(ch.check(age, n), "awaiting the second author")
    n["check_ok"] = "no"
    assert has(ch.check(age, n), "answered no")

    with open(tmp_path / "specs.jsonl", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(s) + "\n" for s in S)
    (tmp_path / "notes_alice.md").write_text(_form(age["gid"], _notes(age)), encoding="utf-8")
    assert any("rename it" in line for line in ch.assemble(kit_dir=tmp_path)[1])


ROUND3 = [  # (gid, field, line, accepted?) from the third review of the kit
    ("c132", "FLIP", "Temperature today 39 °C.", False),            # a value written without its trailing zero
    ("c132", "FLIP", "Temperature today 39.0 °C.", True),
    ("c126", "fact 2", "SaO2 94% on room air.", True),              # digits inside SaO2 are not the value
    ("c029", "FLIP", "Has non-small cell lung cancer.", True),       # 'non-' is not a denial of cancer
    ("c026", "FLIP", "Diabetes: none.", False),                      # a denial after the name
    ("c049", "NEAR", "Heart failure, not decompensated.", False),    # not a denial of heart failure
    ("c075", "FLIP", "Never had a heart attack.", False),            # a counted past fact written as a denial
    ("c002", "NEAR", "New confusion, per his wife.", False),         # the wife only reports
    ("c002", "NEAR", "His wife has new confusion.", True),
    ("c032", "FLIP", "Her child has a peptic ulcer.", False),
    ("c055", "FLIP", "History of heart failure.", False),            # a current fact written as past
    ("c055", "FLIP", "Heart failure since 2019.", True),
    ("c016", "NEAR", "Heart rate 101/min today; it was 78/min in 2019.", False),
    ("c070", "NEAR", "No longer allergic to penicillin.", True),     # over, in words
    ("c008", "FLIP", "His father had diabetes years ago.", False),   # wrong pronoun for a woman
    ("c009", "extra", ["Lives alone in a bungalow."], True),          # 'bungalow' does not name BUN
    ("c124", "extra", ["Uses home oxygen at night."], False),
    ("c007", "header", "Elderly woman.", False),                     # age words on an 'adult' form
]


@pytest.mark.parametrize("gid, field, line, ok", ROUND3)
def test_round3_wording(gid, field, line, ok):
    s = next(x for x in ch.specs() if x["gid"] == gid)
    n = _notes(s)
    n[field] = line
    n["check_ok"] = "yes " + ch.fingerprint(n, s)
    assert (ch.check(s, n) == []) == ok, ch.check(s, n)


def test_owner_file_no_and_encoding(tmp_path):
    S = ch.specs()
    s = S[0]
    with open(tmp_path / "specs.jsonl", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(x) + "\n" for x in S)
    other = next(a for a in ch.AUTHORS if a != s["author"])
    (tmp_path / f"notes_{other}.md").write_text(_form(s["gid"], _notes(s)), encoding="utf-8")
    assert any("belongs to" in line for line in ch.assemble(kit_dir=tmp_path)[1])
    (tmp_path / f"notes_{other}.md").unlink()
    n = _notes(s)
    n["check_ok"] = "no " + ch.fingerprint(n, s)
    assert "answered no" in ch.check(s, n)[0]
    n["reason"] += " Seen today."                   # a revision voids the 'no': the group awaits a new check
    assert ch.check(s, n)[0].startswith("passes the checks")
    (tmp_path / f"notes_{s['author']}.md").write_bytes(_form(s["gid"], _notes(s)).replace("\n", " °\n", 1).encode("cp1252"))
    assert any("not saved as UTF-8" in line for line in ch.assemble(kit_dir=tmp_path)[1])
