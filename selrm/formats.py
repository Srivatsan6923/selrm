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
"""
from __future__ import annotations

import random

from selrm.prompts import (answer, judge_prompt, ledger_to_text, rationale_prompt,
                           reader_prompt, verdict_prompt)

FORMATS = ("verdict", "rationale", "summary2", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader")
VERSION = 2                  # bump when example construction changes (part of the pretok key)
TWO_STAGE = ("summary2", "value2", "ledger2", "ledger2_dec", "dec_judge", "bit_reader")
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
    if fmt == "summary2":
        return rec["prose"]
    if fmt == "bit_reader":
        return BITS[holds(rec)]
    if fmt == "value2":
        return "\n\n".join("\n".join(f"{k}: {e[k]}" for k in FIELDS[fmt]) for e in rec["ledger"])
    text = ledger_to_text(rec["ledger"])
    return text + "\n\n" + BITS[holds(rec)] if fmt in ("ledger2_dec", "dec_judge") else text


def judge_view(text: str, fmt: str) -> str:
    """What the judge sees given the reader's text (gold in training, generated at eval)."""
    return text.strip().split("\n")[-1] if fmt == "dec_judge" else text


def read_bit(text: str):
    """1 / 0 / None from a decision line at the end of a reader output; 'bad' otherwise."""
    last = text.strip().split("\n")[-1] if text.strip() else ""
    return next((h for h, line in BITS.items() if line == last), "bad")


def reader_unit(rec: dict) -> tuple:
    return rec["tid"], rec["case_kind"], rec["condition"]


def reader_units(records) -> list:
    """One representative record per (case, condition), in file order."""
    units = {}
    for r in records:
        units.setdefault(reader_unit(r), r)
    return list(units.values())


def well_formed(text: str, case_text: str, fmt: str) -> bool:
    """Ledger check (INTERFACES 3): every entry has exactly the format's fields in
    order, and every found is 'not mentioned' or a verbatim substring of the case.
    Prose (summary2) has no structure to check."""
    if fmt == "summary2":
        return True
    text = text.strip()
    if fmt == "bit_reader":
        return text in BITS.values()
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
                   seed: int = 0):
    """-> (examples, stats). Each example: {prompt, completion, part, src}.
    n is the example budget (default len(records)); seed fixes the selection,
    which is shared by all training seeds of a cell (seeds vary order and LoRA init)."""
    if fmt not in FORMATS:
        raise ValueError(f"unknown format {fmt}")
    rng, n = random.Random(seed), n or len(records)
    if fmt in ("verdict", "rationale"):
        ex = []
        for r in _take(records, n, rng):
            if fmt == "verdict":
                p, c = verdict_prompt(r), answer(r)
            else:
                p, c = rationale_prompt(r), ledger_to_text(r["ledger"]) + "\n" + answer(r)
            ex.append({"prompt": p, "completion": c, "part": fmt, "src": r["iid"]})
        return ex, {"n": len(ex), "label1": sum(e["completion"].endswith("+") for e in ex)}

    pairs = {}
    for r in records:
        pairs.setdefault((r["tid"], r["case_kind"], r["claim_type"]), {})[r["claim_role"]] = r
    pairs = {k: v for k, v in pairs.items() if len(v) == 2}
    groups = {}                                   # N(x): same rule, condition and claim type
    for key, v in pairs.items():
        groups.setdefault((v["s"]["rid"], v["s"]["condition"], key[2]), []).append(key)
    n_pairs = (n - n // 2) // 2
    n_reader = n - 2 * n_pairs
    ex = [{"prompt": reader_prompt(r, prose=fmt == "summary2"), "completion": gold_record(r, fmt),
           "part": "reader", "src": "/".join(r["iid"].split("/")[:2])}
          for r in _take(reader_units(records), n_reader, rng)]
    sel, swapped = [], 0
    for key in _take(sorted(pairs), n_pairs, rng):
        if rng.random() < resample_p:
            v = pairs[key]["s"]
            group = groups[(v["rid"], v["condition"], key[2])]
            if len(group) > 1:
                other = key
                while other == key:
                    other = rng.choice(group)
                key, swapped = other, swapped + 1
        sel.append(key)
        for role in ("s", "s_prime"):
            r = pairs[key][role]
            ex.append({"prompt": judge_prompt(r, judge_view(gold_record(r, fmt), fmt)), "completion": answer(r),
                       "part": "judge", "src": r["iid"]})
    stats = {"n": len(ex), "reader": n_reader, "judge": 2 * n_pairs, "pairs_swapped": swapped,
             "unique_judge_pairs": len(set(sel)), "reader_units": len(reader_units(records)),
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
