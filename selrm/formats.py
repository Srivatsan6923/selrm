"""Training examples and reader-output checks for the five formats (ROLE.md,
Formats). Owner B. Prompt text comes only from selrm.prompts; this module only
decides which prompt goes with which target and how the example budget is split.

verdict    verdict_prompt -> answer                      (one per record)
rationale  rationale_prompt -> ledger text \n answer     (one per record)
summary2   reader(prose) -> prose; judge(prose) -> answer
value2     reader -> ledger cut to need/found; judge(that text) -> answer
ledger2    reader -> ledger_to_text(ledger); judge(that text) -> answer
Two-stage budget: n//2 reader examples (one per case and condition, cycled when
there are fewer units) and n//2 judge examples (both claims of a case and claim
type). Ledger resampling implements the draft's q(.|x): with probability
resample_p a selected judge pair (x, claim type) is replaced by the pair of x'
drawn uniformly from N(x), the other training cases of the same rule and condition
(twins included); claim texts are identical within (rule, condition, claim type),
so the judge sees the claim with x' 's ledger and the verdict that ledger implies.

Decision-bit ablations (Table 9; the bit is "applies: yes|no|unknown", A's
meta.criterion_holds = 1|0|None, None for missing input):
ledger2_dec  reader -> ledger + bit line; judge sees both           (+ decision field)
dec_judge    reader -> ledger + bit line; judge sees the bit line only (decision field only)
bit_reader   reader -> bit line only;     judge sees the bit line    (reader writes bit only)
ledger2_verify  ledger2 examples + verification examples (one ledger entry and the case -> + if every
             field is as the case records it, - for an entry with one corrupted field), B-AB-verify
verdict_bt   verdict prompts of the two claims of a case; Bradley-Terry loss on u(correct) - u(wrong)
             (B-AB-pairwise; n//2 pairs = n sequences; missing-input cases have no preferred claim)
conddrv      ledger2 whose reader gets the claim instead of the condition under test and names the condition
             itself in need (B-AB-conddrv, v13 "condition derived": the reader is given the rule and the claim);
             one reader output per record, the judge as in ledger2
ledger2_case ledger2 whose judge also sees the case (JUDGE_CASE: rule, case, ledger, claim; B-LC, NEXT_TASKS_B 2)
ledger_g     stage-2 record (STAGE2_SPEC 3; v2_reader): each entry = the five ledger fields, an optional
             `concept: <ontology id>` line and `applies: yes|no`; the judge prompts of one adapter are record-only
             (JUDGE) and record plus case (JUDGE_CASE), half each
genprm       GENPRM prompt -> ```python check``` + its output + answer (B-TR-genprm; the check is A's
             render_check_code, A-D13, rendered by scripts/render_checks.py; one per record)
"""
from __future__ import annotations

import random

from selrm.prompts import (answer, judge_prompt, ledger_to_text, rationale_prompt,
                           reader_prompt, verdict_prompt)

FORMATS = ("verdict", "rationale", "summary2", "summary2_case", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader",
           "verdict_bt", "ledger2_verify", "genprm", "conddrv", "ledger2_case", "ledger_g")
VERSION = 2                  # bump when example construction changes (part of the pretok key)
TWO_STAGE = ("summary2", "summary2_case", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader", "ledger2_verify", "conddrv", "ledger2_case", "ledger_g")
PROSE = ("summary2", "summary2_case")       # reader writes free prose (never malformed)
# summary pipeline whose judge also sees the case (FINAL_TASKS_B P0.4; B-defined prompt: the frozen JUDGE has no case)
JUDGE_CASE = ("Rule: {rule}\n\nCase:\n{case}\n\nEvidence record:\n{record}\n\nClaim: {claim}\n\n"
              "Is the claim correct for this case under the stated rule? Answer + or -.")
# condition derived by the reader (Table 9 ablation; B-defined prompt, READER_LEDGER without the condition)
READER_DERIVE = ("Rule: {rule}\n\nCase:\n{case}\n\nClaim: {claim}\n\n"
                 "Find the condition of the rule that this claim depends on, then write the evidence ledger for "
                 "it: one entry per relevant mention in the case, with the fields need, found, subject, status, "
                 "time. Quote the case verbatim in 'found' (or give the value). If nothing is mentioned, write "
                 "found: not mentioned. Record facts only; do not decide the claim.")
# verification pass (Table 9 "+ verification pass"; B-defined prompt, the frozen prompts have none)
VERIFY = ("Rule: {rule}\n\nCase:\n{case}\n\nCondition under test: {condition}\n\nLedger entry:\n{entry}\n\n"
          "Is every field of this entry (found, subject, status, time) as the case records it? Answer + or -.")
# GenPRM-style verifier (Table 4; B-defined prompt): the generated check is executed and its output
# is shown before the answer is read
GENPRM = ("Rule: {rule}\n\nCase:\n{case}\n\nClaim: {claim}\n\n"
          "Write a short Python check that records the case's values for every criterion of the rule, "
          "applies the stated rule and prints + if the claim is correct, else -. The check is run and its "
          "output is shown after it; then answer + or - on a new line.")
FIELDS = {"ledger2": ("need", "found", "subject", "status", "time"), "value2": ("need", "found")}
BITS = {1: "applies: yes", 0: "applies: no", None: "applies: unknown"}
NOT_MENTIONED = "not mentioned"
MALFORMED_U = -20.0          # INTERFACES 3: malformed ledger -> u = -20 for both claims


def holds(rec: dict):
    """Decision bit of the case: A's meta.criterion_holds (1, 0, None for missing input);
    smoke records lack it and get it from their own label (claim s is correct iff the
    condition does not hold, claim s_prime iff it holds)."""
    if "criterion_holds" in rec["meta"]:
        return rec["meta"]["criterion_holds"]
    if rec["case_kind"] == "missing":
        return None
    return 1 - rec["label"] if rec["claim_role"] == "s" else rec["label"]


def gold_record(rec: dict, fmt: str) -> str:
    """What the reader should write for this case: program ledger, prose or decision bit."""
    if fmt in PROSE:
        return rec["prose"]
    if fmt == "bit_reader":
        return BITS[holds(rec)]
    if fmt == "ledger_g":
        return "\n\n".join(entry_g(e) for e in rec["ledger"])
    if fmt == "value2":
        return "\n\n".join("\n".join(f"{k}: {e[k]}" for k in FIELDS[fmt]) for e in rec["ledger"])
    text = ledger_to_text(rec["ledger"])            # ledger2, ledger2_verify, decision-bit formats
    return text + "\n\n" + BITS[holds(rec)] if fmt in ("ledger2_dec", "dec_judge") else text


def entry_text(e: dict) -> str:
    return "\n".join(f"{k}: {e[k]}" for k in ("need", "found", "subject", "status", "time"))


def entry_g(e: dict) -> str:
    """Stage-2 entry: the five fields, `concept` when the entry links a term, then the applies bit."""
    lines = [f"{k}: {e[k]}" for k in ("need", "found", "subject", "status", "time")]
    return "\n".join(lines + ([f"concept: {e['concept']}"] if e.get("concept") else []) + [f"applies: {e.get('applies', 'no')}"])


def parse_entries(text: str) -> list:
    """Entries of a well-formed ledger2 text as dicts."""
    return [dict(line.split(": ", 1) for line in block.split("\n")) for block in text.strip().split("\n\n")]


def verify_prompt(rec: dict, entry: dict) -> str:
    return VERIFY.format(rule=rec["rule_text"], case=rec["case_text"], condition=rec["condition"],
                         entry=entry_text(entry))


def corrupt(e: dict, case_text: str, rng: random.Random) -> dict:
    """The entry with one field made wrong: subject, status, time or found."""
    e, k = dict(e), rng.choice(("subject", "status", "time", "found"))
    if k == "subject":
        e["subject"] = "other (mother)" if e["subject"] == "patient" else "patient"
    elif k == "status":
        e["status"] = "absent" if e["status"] == "present" else "present"
    elif k == "time":
        e["time"] = "past (2015)" if e["time"] == "current" else "current"
    else:
        lines = [l.strip() for l in case_text.split("\n")[1:] if l.strip() and l.strip() != e["found"]
                 and e["found"] not in l]
        e["found"] = rng.choice(lines) if lines else (NOT_MENTIONED if e["found"] != NOT_MENTIONED else "present")
    return e


def genprm_prompt(rec: dict) -> str:
    return GENPRM.format(rule=rec["rule_text"], case=rec["case_text"], claim=rec["claim_text"])


def genprm_target(code: str, out: str) -> str:
    """Check block + its output line; the answer follows on the next line (in training, the output)."""
    return "```python\n" + code + "```\nOutput: " + out + "\n"


def reader_for(rec: dict, fmt: str) -> str:
    """Reader prompt of a format: the frozen ledger or prose reader, or READER_DERIVE for conddrv."""
    if fmt == "conddrv":
        return READER_DERIVE.format(rule=rec["rule_text"], case=rec["case_text"], claim=rec["claim_text"])
    return reader_prompt(rec, prose=fmt in PROSE)


def judge_for(rec: dict, text: str, fmt: str) -> str:
    """Judge prompt for a reader output: the frozen JUDGE (rule, record, claim), or JUDGE_CASE (the judge also sees
    the case) for summary2_case and ledger2_case."""
    if fmt in ("summary2_case", "ledger2_case"):
        return JUDGE_CASE.format(rule=rec["rule_text"], case=rec["case_text"], record=text, claim=rec["claim_text"])
    return judge_prompt(rec, judge_view(text, fmt))


def judge_view(text: str, fmt: str) -> str:
    """What the judge sees given the reader's text (gold in training, generated at eval)."""
    return text.strip().split("\n")[-1] if fmt == "dec_judge" else text


def read_bit(text: str):
    """1 / 0 / None from a decision line at the end of a reader output; 'bad' otherwise."""
    if text.startswith("need: ") and "\napplies: " in text:      # stage-2 record: applies if any entry does
        return int(any(e.get("applies") == "yes" for e in parse_entries(text)))
    last = text.strip().split("\n")[-1] if text.strip() else ""
    return next((h for h, line in BITS.items() if line == last), "bad")


def reader_unit(rec: dict, fmt: str = "") -> tuple:
    """One reader output per (case, condition); conddrv's reader sees the claim: one per record."""
    return (rec["iid"],) if fmt == "conddrv" else (rec["tid"], rec["case_kind"], rec["condition"])


def unit_key(rec: dict, fmt: str = "") -> str:
    """Key of a reader prompt in the pre-tokenised eval file."""
    return rec["iid"] if fmt == "conddrv" else "/".join(rec["iid"].split("/")[:2])


def reader_units(records, fmt: str = "") -> list:
    """One representative record per reader unit, in file order."""
    units = {}
    for r in records:
        units.setdefault(reader_unit(r, fmt), r)
    return list(units.values())


def well_formed(text: str, case_text: str, fmt: str) -> bool:
    """Ledger check (INTERFACES 3): every entry has exactly the format's fields in
    order, and every found is 'not mentioned' or a verbatim substring of the case.
    Prose (summary2) has no structure to check."""
    if fmt in PROSE:
        return True
    text = text.strip()
    if fmt == "bit_reader":
        return text in BITS.values()
    if fmt == "ledger_g":
        for entry in text.split("\n\n"):
            kv = [line.partition(": ") for line in entry.split("\n")]
            if [k for k, _, _ in kv] not in (list(FIELDS["ledger2"]) + ["applies"],
                                             list(FIELDS["ledger2"]) + ["concept", "applies"]):
                return False
            if any(not sep or not v.strip() for _, sep, v in kv) or kv[-1][2] not in ("yes", "no"):
                return False
            if kv[1][2] != NOT_MENTIONED and kv[1][2] not in case_text:
                return False
        return True
    if fmt in ("ledger2_verify", "conddrv", "ledger2_case"):
        fmt = "ledger2"
    if fmt in ("ledger2_dec", "dec_judge"):
        head, sep, last = text.rpartition("\n\n")
        return bool(sep) and last in BITS.values() and well_formed(head, case_text, "ledger2")
    keys = FIELDS[fmt]
    if not text:
        return False
    for entry in text.split("\n\n"):
        lines = entry.split("\n")
        if len(lines) != len(keys):
            return False
        vals = []
        for k, line in zip(keys, lines):
            head, sep, val = line.partition(": ")
            if head != k or not sep or not val.strip():
                return False
            vals.append(val)
        if vals[1] != NOT_MENTIONED and vals[1] not in case_text:
            return False
    return True


def _take(items: list, k: int, rng: random.Random) -> list:
    """k items: every item once per pass (fresh shuffle each pass), last pass partial."""
    if k and not items:
        raise ValueError("nothing to sample from")
    out = []
    while len(out) < k:
        batch = list(items)
        rng.shuffle(batch)
        out += batch[:k - len(out)]
    return out


def build_examples(records, fmt: str, n: int | None = None, resample_p: float = 0.3,
                   seed: int = 0, pair_weights: dict | None = None, codes: dict | None = None):
    """-> (examples, stats). Each example: {prompt, completion, part, src}.
    n is the example budget (default len(records)); seed fixes the selection,
    which is shared by all training seeds of a cell (seeds vary order and LoRA init).
    codes: {iid: check code} for genprm (scripts/render_checks.py)."""
    if fmt not in FORMATS:
        raise ValueError(f"unknown format {fmt}")
    if fmt == "ledger2_verify":       # the ledger2 examples, plus verification examples on top (n // 6)
        ex, st = build_examples(records, "ledger2", n, resample_p, seed, pair_weights)
        rng = random.Random(f"verify.{seed}")
        units = reader_units(records)
        for r in _take(units, (n or len(records)) // 6, rng):
            e = rng.choice(r["ledger"])
            bad = rng.random() < 0.5
            ex.append({"prompt": verify_prompt(r, corrupt(e, r["case_text"], rng) if bad else e),
                       "completion": "-" if bad else "+", "part": "verify", "src": "/".join(r["iid"].split("/")[:2])})
        return ex, st | {"n": len(ex), "verify": len(ex) - st["n"]}
    rng, n = random.Random(seed), n or len(records)
    if fmt in ("verdict", "rationale", "genprm"):
        ex = []
        for r in _take(records, n, rng):
            if fmt == "verdict":
                p, c = verdict_prompt(r), answer(r)
            elif fmt == "genprm":         # the check reproduces the label, so its output is the answer
                p, c = genprm_prompt(r), genprm_target(codes[r["iid"]], answer(r)) + answer(r)
            else:
                p, c = rationale_prompt(r), ledger_to_text(r["ledger"]) + "\n" + answer(r)
            ex.append({"prompt": p, "completion": c, "part": fmt, "src": r["iid"]})
        return ex, {"n": len(ex), "label1": sum(e["completion"].endswith("+") for e in ex)}
    if fmt == "verdict_bt":
        both = {}
        for r in records:
            both.setdefault((r["tid"], r["case_kind"], r["claim_type"]), {})[r["label"]] = r
        prefs = sorted(k for k, v in both.items() if set(v) == {0, 1})
        ex = [{"prompt": verdict_prompt(both[k][1]), "prompt_b": verdict_prompt(both[k][0]), "completion": "",
               "part": "pair", "src": both[k][1]["iid"]} for k in _take(prefs, n // 2, rng)]
        return ex, {"n": 2 * len(ex), "pairs": len(ex), "pairs_available": len(prefs)}

    pairs = {}
    for r in records:
        pairs.setdefault((r["tid"], r["case_kind"], r["claim_type"]), {})[r["claim_role"]] = r
    pairs = {k: v for k, v in pairs.items() if len(v) == 2}
    groups = {}                                   # N(x): same rule, condition and claim type
    for key, v in pairs.items():
        groups.setdefault((v["s"]["rid"], v["s"]["condition"], key[2]), []).append(key)
    n_pairs = (n - n // 2) // 2
    n_reader = n - 2 * n_pairs
    ex = [{"prompt": reader_for(r, fmt), "completion": gold_record(r, fmt), "part": "reader", "src": unit_key(r, fmt)}
          for r in _take(reader_units(records, fmt), n_reader, rng)]
    sel, swapped = [], 0
    keys = sorted(pairs)
    if pair_weights is not None:        # probe re-weighting: judge pairs drawn in proportion to their group's weight
        anchors = rng.choices(keys, weights=[pair_weights.get(k[0], 1.0) for k in keys], k=n_pairs)
    else:
        anchors = _take(keys, n_pairs, rng)
    for key in anchors:
        if rng.random() < resample_p:
            v = pairs[key]["s"]
            group = groups[(v["rid"], v["condition"], key[2])]
            if len(group) > 1:
                other = key
                while other == key:
                    other = rng.choice(group)
                key, swapped = other, swapped + 1
        sel.append(key)
        jf = "ledger2_case" if fmt == "ledger_g" and len(sel) % 2 == 0 else fmt     # ledger_g: half the pairs with the case
        for role in ("s", "s_prime"):
            r = pairs[key][role]
            ex.append({"prompt": judge_for(r, gold_record(r, fmt), jf), "completion": answer(r),
                       "part": "judge", "src": r["iid"]})
    stats = {"n": len(ex), "reader": n_reader, "judge": 2 * n_pairs, "pairs_swapped": swapped,
             "unique_judge_pairs": len(set(sel)), "reader_units": len(reader_units(records, fmt)),
             "judge_pairs_available": len(pairs), "resample_groups": len(groups),
             "label1": sum(e["completion"] == "+" for e in ex if e["part"] == "judge")}
    return ex, stats


def dataset_path(root: str, name: str) -> str:
    """Records file of a dataset: the REGISTRY.json path (A's layout
    data/<set>/<name>/records.jsonl) if registered, else data/<name>.jsonl (smoke)."""
    import json, os
    reg = f"{root}/data/REGISTRY.json"
    if os.path.exists(reg):
        entry = json.load(open(reg, encoding="utf-8")).get(name)
        if entry:
            return f"{root}/data/{entry['path']}"
    return f"{root}/data/{name}.jsonl"
