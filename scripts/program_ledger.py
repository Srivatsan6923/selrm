"""Rule program applied to the predicted ledger (Table 9 'program on predicted ledger'; FINAL_TASKS_B P0.1).
For every record, the reader's ledger for its (case, condition) replaces the case's mentions of the condition's
concept: an entry is matched to a case mention by its quote (exact, or one contains the other) or, for a
measurement, by the formatted value; the mention then takes the entry's subject, status and time. Entries that match
no mention and 'not mentioned' entries add nothing. A's rule program then labels the record; a ledger after which the
program has no answer (a measurement with no or two applicable values) or a malformed ledger rejects both claims.
u = +10 if the program finds the claim correct, else -10. Runs with role A's frozen code on PYTHONPATH and imports
nothing from B (both packages are named selrm):
  PYTHONPATH=<A code dir> python scripts/program_ledger.py RECORDS.jsonl SCORES.jsonl OUT_SCORES.jsonl OUT_META.json"""
import json, sys
from dataclasses import replace

from selrm.engine import fmt
from selrm.reference import _rule, mentions_with_quotes

U = 10.0


def parse(text):
    """Entries of a ledger text, or None if it is not a list of 5-field entries."""
    out = []
    for block in text.strip().split("\n\n"):
        e = {}
        for line in block.split("\n"):
            k, sep, v = line.partition(": ")
            if not sep:
                return None
            e[k.strip()] = v.strip()
        if set(e) != {"need", "found", "subject", "status", "time"}:
            return None
        out.append(e)
    return out


def apply_entry(m, e):
    subj = e["subject"]
    subject = "patient" if subj == "patient" else subj[len("other ("):-1] if subj.startswith("other (") else subj
    t = e["time"]
    time, year = ("current", None) if t == "current" else ("past", int(t[6:10])) if t.startswith("past (") and t[6:10].isdigit() \
        else ("past", None)
    return replace(m, subject=subject, status=e["status"], time=time, year=year)


def label(rec, entries, stats):
    rule, ov = _rule(rec), rec["meta"]["overrides"]
    c = rule.crit(rec["cid"])
    ms = mentions_with_quotes(rec)
    target = [i for i, (m, _) in enumerate(ms) if m.concept == c.concept]
    kept = [m for i, (m, _) in enumerate(ms) if i not in target]
    used = set()
    for e in entries:
        if e["found"] == "not mentioned":
            continue
        hit = None
        for i in target:
            m, q = ms[i]
            if i in used:
                continue
            if c.kind == "numeric" and e["found"] == fmt(m.value, c):
                hit = i
            elif e["found"] == q or (e["found"] and (e["found"] in q or q in e["found"])):
                hit = i
            if hit is not None:
                break
        if hit is None:
            stats["unmatched"] += 1
            continue
        used.add(hit)
        stats["matched"] += 1
        kept.append(apply_entry(ms[hit][0], e))
    try:
        if rec["claim_type"] == "criterion":
            return int(c.evaluate(kept, ov.get(c.cid)))
        return rule.label(kept, c.cid, ov)
    except ValueError:
        stats["no_answer"] += 1
        return None


def main():
    rec_path, scores_path, out_scores, out_meta = sys.argv[1:5]
    S = {r["iid"]: r for r in map(json.loads, open(scores_path, encoding="utf-8"))}
    stats = {"matched": 0, "unmatched": 0, "no_answer": 0, "malformed": 0, "records": 0}
    seen = {}
    with open(out_scores, "w", encoding="utf-8", newline="\n") as f:
        for line in open(rec_path, encoding="utf-8"):
            rec = json.loads(line)
            row = S.get(rec["iid"])
            if row is None:
                continue
            stats["records"] += 1
            unit = "/".join(rec["iid"].split("/")[:2]) + "|" + rec["claim_type"]
            if unit not in seen:
                entries = parse(row.get("reader_output", ""))
                if entries is None:
                    stats["malformed"] += 1
                    seen[unit] = None
                else:
                    seen[unit] = label(rec, entries, stats)
            lab = seen[unit]
            ok = lab is not None and lab == (1 if rec["claim_role"] == "s_prime" else 0)
            f.write(json.dumps({"iid": rec["iid"], "u": U if ok else -U}) + "\n")
    json.dump(stats, open(out_meta, "w"), indent=1)
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
