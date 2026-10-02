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
type; with probability resample_p the case is swapped for another case of the
same group, so the judge sees one claim under different ledgers).
"""
from __future__ import annotations

import random

from selrm.prompts import (answer, judge_prompt, ledger_to_text, rationale_prompt,
                           reader_prompt, verdict_prompt)

FORMATS = ("verdict", "rationale", "summary2", "value2", "ledger2")
VERSION = 1                  # bump when example construction changes (part of the pretok key)
TWO_STAGE = ("summary2", "value2", "ledger2")
FIELDS = {"ledger2": ("need", "found", "subject", "status", "time"), "value2": ("need", "found")}
NOT_MENTIONED = "not mentioned"
MALFORMED_U = -20.0          # INTERFACES 3: malformed ledger -> u = -20 for both claims


def gold_record(rec: dict, fmt: str) -> str:
    """What the reader should write for this case: program ledger or prose."""
    if fmt == "summary2":
        return rec["prose"]
    if fmt == "ledger2":
        return ledger_to_text(rec["ledger"])
    return "\n\n".join("\n".join(f"{k}: {e[k]}" for k in FIELDS[fmt]) for e in rec["ledger"])


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
    keys, text = FIELDS[fmt], text.strip()
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
    siblings = {}
    for tid, ck, ct in pairs:
        siblings.setdefault((tid, ct), []).append(ck)
    n_pairs = (n - n // 2) // 2
    n_reader = n - 2 * n_pairs
    ex = [{"prompt": reader_prompt(r, prose=fmt == "summary2"), "completion": gold_record(r, fmt),
           "part": "reader", "src": "/".join(r["iid"].split("/")[:2])}
          for r in _take(reader_units(records), n_reader, rng)]
    swapped = 0
    for tid, ck, ct in _take(sorted(pairs), n_pairs, rng):
        if rng.random() < resample_p:
            others = [k for k in siblings[(tid, ct)] if k != ck]
            if others:
                ck, swapped = rng.choice(others), swapped + 1
        for role in ("s", "s_prime"):
            r = pairs[(tid, ck, ct)][role]
            ex.append({"prompt": judge_prompt(r, gold_record(r, fmt)), "completion": answer(r),
                       "part": "judge", "src": r["iid"]})
    stats = {"n": len(ex), "reader": n_reader, "judge": 2 * n_pairs, "pairs_swapped": swapped,
             "reader_units": len(reader_units(records)), "judge_pairs_available": len(pairs)}
    return ex, stats
