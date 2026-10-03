"""Smoke-data generator in the CANONICAL schema, built on mini_engine.

Purpose: let training, evaluation and downstream code be written and tested
against the final record format before the real engine (owner A) is frozen.
It already holds out rendering templates and whole rules, so the first
flips-vs-triplets comparison can be run on it. It is NOT the paper's dataset:
11 rules, short notes, no hard tiers, no ladder, no missing twins.
"""
from __future__ import annotations

import random
from dataclasses import asdict

from selrm import mini_engine as E
from selrm.rules import RULES

OPW = {"<": "below", "<=": "at or below", ">": "above", ">=": "at least"}
HELDOUT_RULES = ("migraine_cad", "contra_vte", "vte_platelets")
TRAIN_TPL, TEST_TPL = (0, 1), (2,)       # every template bank has 3 variants


def condition_text(c) -> str:
    if c.kind == "finding":
        return c.label
    thr = f"{c.threshold:.{c.decimals}f}" if c.decimals else f"{int(c.threshold)}"
    return f"{c.label} {OPW[c.op]} {thr}"


def make_ledger(rule, c, state, tpl) -> list:
    out = []
    for m in state:
        if m.concept != c.concept:
            continue
        found = E._fmt(c, m.value) if m.kind == "numeric" else E._line(rule, m, tpl)
        out.append({"need": condition_text(c), "found": found,
                    "subject": "patient" if m.subject == "patient" else f"other ({m.subject})",
                    "status": m.status,
                    "time": "current" if m.time == "current" else f"past ({m.year})"})
    if not out:
        out.append({"need": condition_text(c), "found": "not mentioned",
                    "subject": "patient", "status": "absent", "time": "current"})
    return out


def ledger_to_prose(ledger) -> str:
    sents = []
    for e in ledger:
        if e["found"] == "not mentioned":
            sents.append(f"The note records no value for {e['need']}; the input is unknown."
                         if e["status"] == "unknown" else f"The note does not mention {e['need']}.")
            continue
        who = "the patient" if e["subject"] == "patient" else e["subject"].replace("other (", "the patient's ").rstrip(")")
        when = "at present" if e["time"] == "current" else "in the " + e["time"]
        sents.append(f"For {e['need']}, the note states \"{e['found']}\"; this concerns {who}, "
                     f"is recorded as {e['status']}, {when}.")
    return " ".join(sents)


def claim_pairs(rule, c) -> dict:
    pairs = {"conclusion": rule.claims(c.cid)}
    if rule.kind == "constraint":
        cond = condition_text(c)
        pairs["criterion"] = (f"Under the rule, the condition \"{cond}\" does not hold for this patient.",
                              f"Under the rule, the condition \"{cond}\" holds for this patient.")
    return pairs


def make_triplet(rng, rule, set_name, split, tpl_choices, tid, level="smoke"):
    c = rng.choice(rule.criteria)
    nm_kind = rng.choice(c.nm_kinds())
    states = E._states(rng, rule, c, nm_kind)
    if [rule.label(s, c.cid) for s in states] != [0, 1, 0]:
        return None
    age = rng.randint(*rule.age_range)
    sex = rule.sex or rng.choice(["male", "female"])
    bg = rng.sample(E.BG_POOL, rng.randint(0, 3))
    style = {"tpl": rng.choice(tpl_choices), "hdr": rng.choice(tpl_choices), "bg": bg,
             "pos": rng.randint(0, len(bg))}
    bg2 = bg[:]
    rng.shuffle(bg2)
    style_p = {"tpl": rng.choice(tpl_choices), "hdr": rng.choice(tpl_choices), "bg": bg2,
               "pos": rng.randint(0, len(bg2))}
    cases = (("base", states[0], style), ("flip", states[1], style),
             ("near", states[2], style), ("pres", states[0], style_p))
    recs = []
    for kind, st, sty in cases:
        y_concl = rule.label(st, c.cid)
        y_crit = int(c.evaluate(st))
        ledger = make_ledger(rule, c, st, sty["tpl"])
        base = dict(tid=tid, set=set_name, split=split, tier="easy", level=level,
                    rid=rule.rid, cid=c.cid, family=rule.family, nm_kind=nm_kind,
                    case_kind=kind, rule_text=rule.rule_text(),
                    case_text=E.render(rule, st, age, sex, sty),
                    condition=condition_text(c), state=[asdict(m) for m in st],
                    ledger=ledger, prose=ledger_to_prose(ledger),
                    meta={"tpl": sty["tpl"], "hdr": sty["hdr"]})
        for ctype, (s, s2) in claim_pairs(rule, c).items():
            y = y_concl if ctype == "conclusion" else y_crit
            for role, text, ok in (("s", s, y == 0), ("s_prime", s2, y == 1)):
                recs.append(dict(base, iid=f"{tid}/{kind}/{ctype}/{role}", claim_type=ctype,
                                 claim_role=role, claim_text=text, label=int(ok)))
    return recs


def generate(n_triplets, seed, rules, set_name, split, tpl_choices):
    rng, out, n = random.Random(seed), [], 0
    while n < n_triplets:
        recs = make_triplet(rng, rng.choice(rules), set_name, split, tpl_choices,
                            f"{split}{seed}_{n:06d}")
        if recs is None:
            continue
        out.append(recs)
        n += 1
    return out


def corpus(triplets, kind, pres_share=0.15, seed=0):
    """blocks: base+flip per group.  triplets: flip + (base or near, alternating).
    Both add the presentation case for a pres_share of groups; same size."""
    rng, out = random.Random(seed), []
    for i, recs in enumerate(triplets):
        keep = {"flip", "base"} if kind == "blocks" or i % 2 == 0 else {"flip", "near"}
        if rng.random() < pres_share:
            keep = keep | {"pres"}
        out += [r for r in recs if r["case_kind"] in keep]
    return out


def split_rules(heldout=HELDOUT_RULES):
    return ([r for r in RULES if r.rid not in heldout], [r for r in RULES if r.rid in heldout])
