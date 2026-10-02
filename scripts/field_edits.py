"""Field interventions (B-AE-field-edit, Sec. 7.4): for every conclusion record of a set whose
condition under test has a mention in the case, the program's ledger with one field of the first
such mention edited (subject, status or time), and the record label the rule program gives after
the same edit to the case state. Edits: subject patient <-> mother; status present <-> absent;
time current <-> past (2015). Edits after which the program has no answer (a measurement with no
applicable value) are left out. Runs with role A's frozen code on PYTHONPATH and imports nothing
from B (both packages are named selrm):
  PYTHONPATH=<A code dir> python scripts/field_edits.py RECORDS.jsonl OUT.jsonl"""
import json, os, sys
from dataclasses import replace

from selrm.engine import ledger
from selrm.reference import _rule, mentions_with_quotes

EDIT = {"subject": lambda m: replace(m, subject="mother" if m.subject == "patient" else "patient"),
        "status": lambda m: replace(m, status="absent" if m.status == "present" else "present"),
        "time": lambda m: replace(m, time="past", year=2015) if m.time == "current" else replace(m, time="current", year=None)}


def edits(rec):
    rule, ov = _rule(rec), rec["meta"]["overrides"]
    c = rule.crit(rec["cid"])
    ms = mentions_with_quotes(rec)
    target = [i for i, (m, _) in enumerate(ms) if m.concept == c.concept]
    if rec["case_kind"] == "missing" or rec["claim_type"] != "conclusion" or not target:
        return []
    thr = ov.get(c.cid, c.threshold) if c.kind == "numeric" else None
    old = rule.label([m for m, _ in ms], c.cid, ov)
    out = []
    for field, fn in EDIT.items():
        new_ms = [(fn(m) if i == target[0] else m, q) for i, (m, q) in enumerate(ms)]
        try:
            new = rule.label([m for m, _ in new_ms], c.cid, ov)
        except ValueError:                # e.g. a measurement left without an applicable value
            continue
        entries = ledger(c, thr, [(q, m) for m, q in new_ms])
        correct = int(new == (1 if rec["claim_role"] == "s_prime" else 0))
        out.append({"iid": rec["iid"], "field": field, "ledger": entries, "label": correct,
                    "changed": int(new != old)})
    return out


def main():
    src, out = sys.argv[1], sys.argv[2]
    n = 0
    with open(out + ".tmp", "w", encoding="utf-8", newline="\n") as f:
        for line in open(src, encoding="utf-8"):
            for e in edits(json.loads(line)):
                f.write(json.dumps(e) + "\n")
                n += 1
    os.replace(out + ".tmp", out)
    print(f"{n} field edits -> {out}")


if __name__ == "__main__":
    main()
