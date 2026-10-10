"""One-off: add the stage-2 record format ledger_g to selrm/formats.py, scripts/pretok.py, scripts/eval_local.py."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def patch(path, rep):
    s = open(path, encoding="utf-8").read()
    for a, b in rep:
        assert a in s, (path, a[:60])
        s = s.replace(a, b, 1)
    open(path, "w", encoding="utf-8", newline="\n").write(s)


patch("selrm/formats.py", [
    ('''genprm       GENPRM prompt''', '''ledger_g     stage-2 record (STAGE2_SPEC 3; v2_reader): each entry = the five ledger fields, an optional
             `concept: <ontology id>` line and `applies: yes|no`; the judge prompts of one adapter are record-only
             (JUDGE) and record plus case (JUDGE_CASE), half each
genprm       GENPRM prompt'''),
    ('''"genprm", "conddrv", "ledger2_case")
VERSION''', '''"genprm", "conddrv", "ledger2_case", "ledger_g")
VERSION'''),
    ('''"ledger2_verify", "conddrv", "ledger2_case")
PROSE''', '''"ledger2_verify", "conddrv", "ledger2_case", "ledger_g")
PROSE'''),
    ('''    if fmt == "bit_reader":
        return BITS[holds(rec)]
    if fmt == "value2":''', '''    if fmt == "bit_reader":
        return BITS[holds(rec)]
    if fmt == "ledger_g":
        return "\\n\\n".join(entry_g(e) for e in rec["ledger"])
    if fmt == "value2":'''),
    ('''def parse_entries(text: str) -> list:''', '''def entry_g(e: dict) -> str:
    """Stage-2 entry: the five fields, `concept` when the entry links a term, then the applies bit."""
    lines = [f"{k}: {e[k]}" for k in ("need", "found", "subject", "status", "time")]
    return "\\n".join(lines + ([f"concept: {e['concept']}"] if e.get("concept") else []) + [f"applies: {e.get('applies', 'no')}"])


def parse_entries(text: str) -> list:'''),
    ('''    if fmt in ("ledger2_verify", "conddrv", "ledger2_case"):
        fmt = "ledger2"''', '''    if fmt == "ledger_g":
        for entry in text.split("\\n\\n"):
            kv = [line.partition(": ") for line in entry.split("\\n")]
            if [k for k, _, _ in kv] not in (list(FIELDS["ledger2"]) + ["applies"],
                                             list(FIELDS["ledger2"]) + ["concept", "applies"]):
                return False
            if any(not sep or not v.strip() for _, sep, v in kv) or kv[-1][2] not in ("yes", "no"):
                return False
            if kv[1][2] != NOT_MENTIONED and kv[1][2] not in case_text:
                return False
        return True
    if fmt in ("ledger2_verify", "conddrv", "ledger2_case"):
        fmt = "ledger2"'''),
    ('''    last = text.strip().split("\\n")[-1] if text.strip() else ""
    return next(''', '''    if text.startswith("need: ") and "\\napplies: " in text:      # stage-2 record: applies if any entry does
        return int(any(e.get("applies") == "yes" for e in parse_entries(text)))
    last = text.strip().split("\\n")[-1] if text.strip() else ""
    return next('''),
    ('''        for role in ("s", "s_prime"):
            r = pairs[key][role]
            ex.append({"prompt": judge_for(r, gold_record(r, fmt), fmt), "completion": answer(r),''',
     '''        jf = "ledger2_case" if fmt == "ledger_g" and len(sel) % 2 == 0 else fmt     # ledger_g: half the pairs with the case
        for role in ("s", "s_prime"):
            r = pairs[key][role]
            ex.append({"prompt": judge_for(r, gold_record(r, fmt), jf), "completion": answer(r),'''),
])
patch("scripts/pretok.py", [('"conddrv": "reader_derive", "ledger2_case": "reader_ledger"}',
                             '"conddrv": "reader_derive", "ledger2_case": "reader_ledger", "ledger_g": "reader_ledger"}')])
patch("scripts/eval_local.py", [
    ('"conddrv": "reader_derive", "ledger2_case": "reader_ledger"}',
     '"conddrv": "reader_derive", "ledger2_case": "reader_ledger", "ledger_g": "reader_ledger"}'),
    ('''    assert fmt in ("ledger2_dec",), fmt
    out = {}''', '''    assert fmt in ("ledger2_dec", "ledger_g"), fmt
    g_fmt = fmt == "ledger_g"            # stage-2 record: the bit is a line of every entry
    opath = f"{ROOT}/data/onto_v1/classes.json"
    onto = load_onto(opath) if os.path.exists(opath) else None
    out = {}'''),
    ('''        head, _, last = rec_text.strip().rpartition("\\n\\n")
        cons = r.get("struct") if mode == "gate_struct" else parse_criterion(r["rule_text"], r["condition"])
        g = gate(parse_entries(head), cons, r["case_text"], r.get("ref_date"))   # ponytail: no onto yet (onto_v1 from A)
        done = g["applies"] is not None
        out[reader_unit(r, fmt)] = {"route": "gate" if done else "judge_case", "checks": g["checks"],
                                    "applies_reader": read_bit(rec_text), "applies_gate": g["applies"],
                                    "record": head + "\\n\\n" + BITS[g["applies"]] if done else rec_text.strip()}''',
     '''        head = rec_text.strip() if g_fmt else rec_text.strip().rpartition("\\n\\n")[0]
        entries = parse_entries(head)
        cons = (from_struct(r.get("struct")) if mode == "gate_struct"
                else parse_criterion(r["rule_text"], r["condition"], onto and onto["classes"]))
        g = gate(entries, cons, r["case_text"], r.get("ref_date"), onto)
        done = g["applies"] is not None
        if not done:
            record = rec_text.strip()                    # the reader's bit stands; the judge also sees the case
        elif g_fmt:                                      # each entry's bit is replaced by the gate's value for it
            record = "\\n\\n".join(entry_g(e | {"applies": "yes" if v == 1 else "no"}) for e, v in zip(entries, g["entries"]))
        else:
            record = head + "\\n\\n" + BITS[g["applies"]]
        out[reader_unit(r, fmt)] = {"route": "gate" if done else "judge_case", "checks": g["checks"],
                                    "applies_reader": read_bit(rec_text), "applies_gate": g["applies"], "record": record}'''),
    ('from selrm.crit_parse import parse_criterion\n', 'from selrm.crit_parse import from_struct, parse_criterion\nfrom selrm.link import load_onto\n'),
    ('from selrm.formats import (BITS, MALFORMED_U,', 'from selrm.formats import (BITS, MALFORMED_U, entry_g,'),
])
patch("scripts/train_eval_job.py", [('GEN = 6       # 5:', 'GEN = 7       # 7: format ledger_g (stage-2 record); 5:')])
patch("scripts/make_queue_b.py", [('"conddrv": 3, "ledger2_case": 4}', '"conddrv": 3, "ledger2_case": 4, "ledger_g": 7}')])
print("patched")
