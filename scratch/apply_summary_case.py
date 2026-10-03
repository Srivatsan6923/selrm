"""Add the summary2_case format (FINAL_TASKS_B P0.4): the summary2 reader, a judge that sees rule, case, prose
record and claim (B-defined prompt; the frozen JUDGE prompt has no case)."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert s.count(old) == 1, (path, old[:80])
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8", newline="\n").write(s)


edit("selrm/formats.py", [
    ('''FORMATS = ("verdict", "rationale", "summary2", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader",''',
     '''FORMATS = ("verdict", "rationale", "summary2", "summary2_case", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader",'''),
    ('''TWO_STAGE = ("summary2", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader", "ledger2_verify")''',
     '''TWO_STAGE = ("summary2", "summary2_case", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader", "ledger2_verify")
PROSE = ("summary2", "summary2_case")       # reader writes free prose (never malformed)
# summary pipeline whose judge also sees the case (FINAL_TASKS_B P0.4; B-defined prompt: the frozen JUDGE has no case)
JUDGE_CASE = ("Rule: {rule}\\n\\nCase:\\n{case}\\n\\nEvidence record:\\n{record}\\n\\nClaim: {claim}\\n\\n"
              "Is the claim correct for this case under the stated rule? Answer + or -.")'''),
    ('''    if fmt == "summary2":
        return rec["prose"]''', '''    if fmt in PROSE:
        return rec["prose"]'''),
    ('''    ex = [{"prompt": reader_prompt(r, prose=fmt == "summary2"), "completion": gold_record(r, fmt),''',
     '''    ex = [{"prompt": reader_prompt(r, prose=fmt in PROSE), "completion": gold_record(r, fmt),'''),
    ('''            ex.append({"prompt": judge_prompt(r, judge_view(gold_record(r, fmt), fmt)), "completion": answer(r),''',
     '''            ex.append({"prompt": judge_for(r, gold_record(r, fmt), fmt), "completion": answer(r),'''),
    ('''def judge_view(text: str, fmt: str) -> str:''', '''def judge_for(rec: dict, text: str, fmt: str) -> str:
    """Judge prompt for a reader output: the frozen JUDGE (rule, record, claim), or JUDGE_CASE for summary2_case."""
    if fmt == "summary2_case":
        return JUDGE_CASE.format(rule=rec["rule_text"], case=rec["case_text"], record=text, claim=rec["claim_text"])
    return judge_prompt(rec, judge_view(text, fmt))


def judge_view(text: str, fmt: str) -> str:'''),
])
s = open("selrm/formats.py", encoding="utf-8").read()
i = s.index("def judge_view(text: str, fmt: str) -> str:")
j = s.index('    if fmt == "summary2":', i)
s = s[:j] + '    if fmt in PROSE:' + s[j + len('    if fmt == "summary2":'):]
open("selrm/formats.py", "w", encoding="utf-8", newline="\n").write(s)

edit("scripts/eval_local.py", [
    ('''        "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",''',
     '''        "summary2_case": "reader_prose", "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",'''),
    ('''            ok = (d or fmt == "summary2") and well_formed(out, r["case_text"], fmt)   # a cut-off ledger is unparsable''',
     '''            ok = (d or fmt in PROSE) and well_formed(out, r["case_text"], fmt)   # a cut-off ledger is unparsable'''),
    ('''                u[idx] = sc.score(chat_ids(sc.tok, [judge_prompt(recs[i], judge_view(text[reader_unit(recs[i])][0], fmt))''',
     '''                u[idx] = sc.score(chat_ids(sc.tok, [judge_for(recs[i], text[reader_unit(recs[i])][0], fmt)'''),
    ('''from selrm.formats import (MALFORMED_U, TWO_STAGE,''', '''from selrm.formats import (MALFORMED_U, PROSE, TWO_STAGE, judge_for,'''),
])
edit("scripts/pretok.py", [
    ('''             "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",''',
     '''             "summary2_case": "reader_prose", "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",'''),
    ('''            if f != "summary2" and not well_formed(gold_record(rs[0], f), rs[0]["case_text"], f):''',
     '''            if f not in PROSE and not well_formed(gold_record(rs[0], f), rs[0]["case_text"], f):'''),
    ('''    if spec["format"] not in ("verdict", "verdict_bt", "summary2", "genprm"):   # rationale targets carry ledger2 text''',
     '''    if spec["format"] not in ("verdict", "verdict_bt", "genprm", *PROSE):   # rationale targets carry ledger2 text'''),
    ('''from selrm.formats import (TWO_STAGE, VERSION,''', '''from selrm.formats import (PROSE, TWO_STAGE, VERSION,'''),
])
print("summary2_case added")
