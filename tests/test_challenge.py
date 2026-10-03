import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("ch", Path(__file__).parents[1] / "scripts" / "challenge_v1.py")
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


def _line(text, keywords):
    """A mock author line: the fact itself, with a required string where it is missing."""
    return text if any(k in text.lower() for k in keywords) else f"{text} ({keywords[0]})"


def test_mock_notes_assemble_with_program_labels(tmp_path):
    S = ch.specs()
    assert len(S) == 160 and {s["nm_kind"] for s in S} == {"numeric", "boundary", "subject", "negation", "time"}
    with open(tmp_path / "specs.jsonl", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(s) + "\n" for s in S)
    form = []
    for s in S:
        target = s["states"]["base"] and ch.D.RULES_BY_ID[s["rid"]].crit(s["cid"]).concept
        form += [f"## {s['gid']}", f"header: {s['patient']}.", f"reason: {s['setting']}"]
        for f in s["facts"]:
            kw = s["keywords"] if f["mention"]["concept"] == target else ["x"]
            form.append(f"fact {f['n']}: " + (_line(f["text"], kw) if kw != ["x"] else f["text"]))
        form += [f"FLIP: {_line(s['edits']['flip']['text'], s['keywords'])}",
                 f"NEAR: {_line(s['edits']['near']['text'], s['keywords'])}", "check_ok: yes", ""]
    (tmp_path / "notes_mock.md").write_text("\n".join(form), encoding="utf-8")
    recs, report = ch.assemble(kit_dir=tmp_path)
    assert report[-1].strip().startswith("accepted 160, rejected 0"), report[:5]
    by = {s["gid"]: s for s in S}
    for r in recs:
        if r["claim_type"] == "conclusion" and r["claim_role"] == "s_prime":
            assert r["label"] == by[r["tid"].split(".")[-1]]["labels"][r["case_kind"]]["conclusion"]
