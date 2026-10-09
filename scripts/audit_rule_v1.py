"""Audit of the frozen rule_v1 (FINAL_TASKS A, P0.1). Reads frozen files only; writes no data set.

  python scripts/audit_rule_v1.py            # then: python scripts/render_docs.py

Writes
  tables/data_stats.json            every number of the audit
  data/rule_v1/RULE_MANIFEST.json   one entry per rule: source or specification, displayed text,
                                    program, applicability semantics, tests, version, provenance
  data/rule_v1/KNOWN_ISSUES.json    violations found by re-executing the programs on every test group
  audit/fidelity_author{1..4}.csv   the authors' reading sheets (H1): 300 groups, 75 per author
  audit/fidelity_sheets.md          the same groups, readable
Sources of hand-written rules are read from data/rule_v1/RULE_SOURCES.json when it exists.
"""
import csv
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import engine as E  # noqa: E402
from selrm import folds as FD  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm import rules as R0, rules_constraint as RC, rules_grammar as RG, rules_score as RS  # noqa: E402
from selrm.library import LIBRARY  # noqa: E402
from selrm.rules import FIRST_DEGREE, Mention  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REG = json.loads((DATA / "REGISTRY.json").read_text(encoding="utf-8"))
INVENTED = D.register(RG.invented_rules())
RB = D.RULES_BY_ID
FOLDS = json.loads((DATA / "rule_v1" / "FOLDS.json").read_text(encoding="utf-8"))
F1 = FOLDS["folds"]["1"]
CASES = ("base", "flip", "near", "pres")
TRAIN_MAIN = [f"rule_v1/train_{k}" for k in ("natural", "balanced", "blocks", "triplets")]
TEST_SETS = sorted(n for n, v in REG.items() if v["split"] in ("test", "dev") and n.startswith("rule_v1"))
TRIPLET_SETS = [n for n in TEST_SETS if not n.endswith(("missing", "readapply"))]
DECISION = re.compile(r"\b(prescribe|counts?|holds?|points?)\b")
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:6.0f}s] {msg}", file=sys.stderr, flush=True)


def load(name):
    with open(DATA / REG[name]["path"], encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def grouped(name):
    G = defaultdict(list)
    for r in load(name):
        G[r["tid"]].append(r)
    return G


def case_of(recs, kind):
    return next((r for r in recs if r["case_kind"] == kind and r["claim_type"] == "conclusion"
                 and r["claim_role"] == "s"), None)


def state(rec):
    return [Mention(**m) for m in rec["state"]]


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()


# ------------------------------------------------------------------ keys
def scope(c):
    return "+".join(["patient"] + ["family"] * c.counts_family) + "/" + ("ever" if c.counts_past else "current")


def crit_key(c):
    return (c.concept, c.kind, c.op, c.threshold, scope(c), c.points)


def program_key(r):
    return (r.kind, r.logic, r.cutoff, tuple(sorted(map(crit_key, r.criteria), key=str)))


def structure_key(r):
    """Names and constants removed: rule kind, logic, and per criterion its input type,
    operator and applicability scope."""
    return (r.kind, r.logic if r.kind == "constraint" else "sum",
            tuple(sorted((c.kind, c.op or "", scope(c)) for c in r.criteria)))


def module_of(rid):
    for name, rs in (("pilot", R0.RULES), ("constraint", RC.RULES), ("score", RS.RULES),
                     ("grammar_curated", RG.RULES), ("grammar_sampled", RG.SAMPLED)):
        if any(r.rid == rid for r in rs):
            return name
    return "invented" if rid.startswith("inv") else "?"


# ------------------------------------------------------------------ units
def unit_of(concept):
    """Unit strings that follow the value in the concept's numeric templates."""
    out = set()
    for form in ("current", "past", "superseded"):
        for t in P.BANKS[concept].get(form, []):
            m = re.search(r"\{v\}(?:/\{dia\})?\s?([^\s;,]+?)(?=[\s;,]|\.?$|\.\s)", t)
            u = m.group(1).rstrip(".") if m else ""
            u = u + " m2" if u.endswith("1.73") else u
            if u and not u.isalpha() or u in ("C", "cm", "kg", "mmHg", "years"):
                out.add(u)
    return sorted(out)            # [] for a dimensionless input (INR, pH)


def unit_stated(u, text):
    return bool(re.search(r"(?<![A-Za-z])" + re.escape(u) + r"(?![A-Za-z])", text))


# ------------------------------------------------------------------ manifest
def manifest(sources):
    head = git("rev-parse", "HEAD")
    role = {**{x: "train" for x in F1["train_rules"]}, **{x: "L1" for x in F1["l1_rules"]},
            **{x: "L2" for x in F1["l2_rules"]}}
    out = []
    for r in list(LIBRARY) + list(INVENTED):
        prog = {"kind": r.kind, "logic": r.logic, "cutoff": r.cutoff,
                "verb": r.verb if r.kind == "constraint" else None,
                "default": r.default, "alternative": r.alternative,
                "criteria": [{"cid": c.cid, "concept": c.concept, "input": c.kind, "label": c.label,
                              "keywords": list(c.keywords), "op": c.op, "threshold": c.threshold,
                              "alt_threshold": c.alt_threshold, "decimals": c.decimals, "points": c.points,
                              "counts_past": c.counts_past, "counts_family": c.counts_family,
                              "unit": (unit_of(c.concept) or [None])[0] if c.kind == "numeric" else None}
                             for c in r.criteria]}
        app = [{"cid": c.cid,
                "subjects": "the patient or a first-degree relative (" + ", ".join(sorted(FIRST_DEGREE)) + ")"
                if c.counts_family else "the patient only",
                "times": "current or past" if c.counts_past else "current only",
                "status": "a counted mention with status present makes it hold; absent or unknown do not",
                "values": None if c.kind == "finding" else
                "the patient's one current value, compared with the stated threshold by the stated operator"}
               for c in r.criteria]
        mod = module_of(r.rid)
        src = sources.get(r.rid)
        prov = src["provenance"] if src else ("synthetic" if mod in ("grammar_sampled", "invented") else "unreviewed")
        spec = ("sampled from the typed grammar in selrm/rules_grammar.py" if mod == "grammar_sampled" else
                "sampled from the typed grammar over invented conditions and orders (rules_grammar.INVENTED)"
                if mod == "invented" else "hand-written in selrm/" + {"pilot": "rules.py", "constraint": "rules_constraint.py",
                                                                    "score": "rules_score.py",
                                                                    "grammar_curated": "rules_grammar.py"}[mod])
        library_tests = mod != "invented"          # tests/test_library.py covers the library, not L3-inv
        tests = (["tests/test_library.py: every threshold executed one step below, at and above (and at the"
                  " altered threshold)"] * (library_tests and any(c.kind == "numeric" for c in r.criteria))
                 + ["tests/test_library.py: the stated operator wording matches the program"] * library_tests
                 + ["engine.check on every generated group: executed labels, a flip that changes exactly the"
                    " target criterion, unchanged near-miss and presentation, keyword pattern, ledger quotes"])
        out.append({"rid": r.rid, "module": mod, "kind": r.kind, "family": r.family, "signature_class": FD.sig_class(r),
                    "fold1_role": role.get(r.rid, "L3-inv" if mod == "invented" else None),
                    "text": r.rule_text(), "setting": r.setting,
                    "alt_texts": {c.cid: r.rule_text({c.cid: c.alt_threshold}) for c in r.criteria
                                  if c.alt_threshold is not None},
                    "program": prog, "applicability": app, "tests": tests,
                    "version": {"commit": head, "sha256": hashlib.sha256(json.dumps(
                        [r.text, prog], sort_keys=True, default=str).encode()).hexdigest()[:16]},
                    "provenance": prov, "specification": spec, "source": src})
    return out


# ------------------------------------------------------------------ target-claim check
def check_triplet(rule, crit, ov, cases):
    """Violations of one triplet group, re-executing the program on the stored states."""
    v, ev = [], {}
    for k, rec in cases.items():
        st = state(rec)
        try:
            lab = E.case_labels(rule, crit, ov, st)
            ev[k] = [c.evaluate(st, ov.get(c.cid)) for c in rule.criteria]
        except ValueError as e:
            v.append((k, "program", str(e)))
            continue
        if set(lab.values()) != {E.WANT[k]}:
            v.append((k, "label", f"executes to {lab}, want {E.WANT[k]}"))
        for c in rule.criteria:                    # counted present and absent for one subject and time
            cnt = [m for m in st if c.applies(m)]
            if {m.status for m in cnt} >= {"present", "absent"} and \
                    len({(m.subject, m.time) for m in cnt}) < len(cnt):
                v.append((k, "inconsistent", c.concept))
    if "base" in ev and "flip" in ev:
        changed = [c.cid for c, a, b in zip(rule.criteria, ev["base"], ev["flip"]) if a != b]
        if changed != [crit.cid]:
            v.append(("flip", "flip", f"changes {changed}"))
        for k in ("near", "pres"):
            if k in ev and ev[k] != ev["base"]:
                v.append((k, "unchanged", "a criterion changes"))
    for k, rec in cases.items():                  # Proposition 1 keyword pattern, ledger, prose
        named = any(kw in rec["case_text"].lower() for kw in crit.keywords)
        if named != (crit.kind == "numeric" or k in ("flip", "near")):
            v.append((k, "keyword", "named" if named else "not named"))
        target_lines = [ln for i, ln in mention_lines(rec).items() if ln
                        and rec["state"][i]["concept"] == crit.concept]
        for e in rec["ledger"]:                    # a quote must come from a line that renders the target
            if e["found"] != "not mentioned" and not any(e["found"] in ln for ln in target_lines):
                v.append((k, "ledger", e["found"][:60]))
        if DECISION.search(re.sub(r'"[^"]*"', "", rec["prose"]).replace(rec["condition"], "").lower()):
            v.append((k, "prose", "decision word"))
    return v


def check_records(recs, rule, crit, ov, n=None):
    """Every stored label equals the executed one; a reading claim is correct iff the line it
    quotes is a line of the case."""
    v = []
    for r in recs:
        if r["case_kind"] == "read":
            m = re.match(r'The case states: "(.*)"$', r["claim_text"], re.S)
            y = int(bool(m) and m.group(1) in r["case_text"].split("\n"))
            if n is not None:
                n["read_labels"] += 1
            if r["label"] != y:
                v.append(("read", "stored label", r["iid"]))
            continue
        if r["case_kind"] not in CASES + ("apply",):
            continue
        st = state(r)
        y = rule.label(st, crit.cid, ov) if r["case_kind"] == "apply" else \
            E.case_labels(rule, crit, ov, st)[r["claim_type"]]
        if n is not None:
            n["stored_labels"] += 1
        if r["label"] != int((r["claim_role"] == "s_prime") == (y == 1)):
            v.append((r["case_kind"], "stored label", r["iid"]))
    return v


def check_missing(rule, crit, ov, recs):
    """The missing twin: both claims 0, and completions of the decisive input reach both outcomes."""
    miss = [r for r in recs if r["case_kind"] == "missing"]
    if not miss:
        return []
    v = [("missing", "label", "a claim is not 0")] * any(r["label"] != 0 for r in miss)
    st = [m for m in state(miss[0]) if m.concept != crit.concept]
    comps = ([[Mention(crit.concept, "numeric", x)] for x in (crit.default_range[0], crit.flip_range[0])]
             if crit.kind == "numeric" else [[], [Mention(crit.concept, "finding")]])
    outs = defaultdict(set)                         # per claim type, as engine._check_missing requires
    for comp in comps:
        try:
            for t, y in E.case_labels(rule, crit, ov, st + comp).items():
                outs[t].add(y)
        except ValueError:
            pass
    return v + [("missing", "determined", f"completions give one outcome for {t}")
                for t in ("conclusion", "criterion") if t in outs and outs[t] != {0, 1}] + \
        [("missing", "determined", "no completion executes")] * (not outs)


def target_claim_check():
    """Re-executes the programs on every registered rule_v1 test and development set. Coverage is
    counted per check: stored labels (base, flip, near, pres, apply records), reading labels,
    triplet invariants (groups with base, flip and near; pres when present), missing twins."""
    issues, n_groups, n_records, cov, tids = [], Counter(), Counter(), Counter(), set()
    for name in TEST_SETS:
        for tid, recs in grouped(name).items():
            r0 = recs[0]
            rule, ov = RB[r0["rid"]], r0["meta"]["overrides"]
            crit = rule.crit(r0["cid"])
            n_groups[name] += 1
            n_records[name] += len(recs)
            tids.add(tid)
            v = check_records(recs, rule, crit, ov, cov)
            kinds = {r["case_kind"] for r in recs}
            if {"base", "flip", "near"} <= kinds:
                cov["triplet_groups"] += 1
                v += check_triplet(rule, crit, ov, {k: case_of(recs, k) for k in CASES if k in kinds})
            if "missing" in kinds:
                cov["missing_twins"] += 1
            v += check_missing(rule, crit, ov, recs)
            issues += [{"set": name, "tid": tid, "case": k, "check": c, "detail": d} for k, c, d in v]
        log(f"target-claim check: {name}")
    cov["distinct_groups"] = len(tids)
    return issues, dict(n_groups), dict(n_records), dict(cov)


# ------------------------------------------------------------------ rejects
def rejects():
    """Rejected proposals logged in the manifests, by reason; and the missing twins regenerated
    from their frozen seeds to count proposals rejected only because of the twin."""
    out, unlogged = {}, []
    for name, v in REG.items():
        if not name.startswith("rule_v1") or v.get("alias_of"):
            continue
        m = json.loads((DATA / v["manifest"]).read_text(encoding="utf-8"))
        rj = m.get("rejects")
        if rj:                                     # the logs keep only the text before ':' of each error
            reasons = Counter()
            for k, n in rj["by_reason"].items():
                reasons[k.split()[-1]] += n
            out[name] = {"proposed": rj["proposed"], "rejected": rj["rejected"], "by_reason": dict(reasons)}
        else:
            unlogged.append(name)
    twins = {}
    for name, level, tpl in (("rule_v1/missing", "L2", None), ("rule_v1/dev_missing", "L0", "test")):
        st = Counter()
        tids = list(grouped(name))
        for tid in tids:
            _, split, rid, cid, nm, tier, seed = tid.split(".")
            E.make_group(rid, cid, nm, tier, split, int(seed), "rule_v1", level, stats=st, tpl_split=tpl,
                         missing=True)
        reasons = Counter()
        for k, n in st.items():
            if k.startswith("reject "):
                reasons[k.split()[-1]] += n
        twins[name] = {"groups": len(tids), "proposed": st["proposed"], "rejected": st["rejected"],
                       "by_reason": dict(reasons)}
        log(f"rejects regenerated: {name}")
    return {"logged": out, "sets_without_reject_log": sorted(unlogged), "missing_twins_regenerated": twins}


# ------------------------------------------------------------------ structure statistics
def judgment_rows(groups):
    """One row per judgment (the conclusion claim of a group)."""
    rows = []
    for recs in groups.values():
        r0 = recs[0]
        rule = RB[r0["rid"]]
        crit = rule.crit(r0["cid"])
        needed = rule.criteria if rule.kind == "constraint" else [crit]
        concepts = {c.concept for c in needed}
        sts = [state(c) for c in (case_of(recs, k) for k in ("base", "flip", "near")) if c]
        tgt = [[m for m in st if m.concept == crit.concept] for st in sts]
        rows.append({"rid": rule.rid, "family": rule.family, "class": FD.sig_class(rule),
                     "structure": structure_key(rule), "conditions": len(needed),
                     "depth": 1 if (rule.kind == "score" or len(rule.criteria) == 1) else 2,
                     "mentions": sum(sum(m.concept in concepts for m in st) for st in sts) / max(1, len(sts)),
                     "competing": any(len({(m.subject, m.status, m.time) for m in t}) >= 2 for t in tgt),
                     "temporal": any(m.time == "past" for st in sts for m in st if m.concept in concepts),
                     "numeric": any(c.kind == "numeric" for c in needed),
                     "exception": rule.kind == "constraint"})
    return rows


def summarize(rows):
    n = len(rows)
    if not n:
        return {}
    share = lambda key: pct(sum(r[key] for r in rows), n)  # noqa: E731
    return {"judgments": n, "rules": len({r["rid"] for r in rows}),
            "distinct_structures": len({r["structure"] for r in rows}),
            "signature_classes": len({r["class"] for r in rows}),
            "conditions_mean": round(sum(r["conditions"] for r in rows) / n, 2),
            "conditions_max": max(r["conditions"] for r in rows),
            "depth_mean": round(sum(r["depth"] for r in rows) / n, 2), "depth_max": max(r["depth"] for r in rows),
            "evidence_mentions_mean": round(sum(r["mentions"] for r in rows) / n, 2),
            "competing_mentions_pct": share("competing"), "temporal_pct": share("temporal"),
            "numeric_pct": share("numeric"), "exception_pct": share("exception")}


# ------------------------------------------------------------------ overlap
def alternation(words, pre=r"\b", post=r"\b"):
    return re.compile(pre + "(" + "|".join(sorted(map(re.escape, words), key=len, reverse=True)) + ")" + post)


CUE_RE = {s: alternation({w for lex in (P.NEG_CUES, P.TIME_CUES, P.CURRENT_CUES) for w in lex[s]})
          for s in ("train", "test")}
PERSON_RE = {s: alternation(P.by_split(P.PERSONS, s), r"(?<![\w-])", r"(?![\w-])") for s in ("train", "test")}


def hits(rx, texts):
    found = [set(rx.findall(t.lower())) for t in texts]
    return pct(sum(map(bool, found)), len(found)), sorted(set().union(*found)) if found else []


def source_tokens(src):
    """Document identifiers in a source record: DOIs, PMIDs, URLs, NICE guidance codes."""
    ids = re.findall(r"(?i)(10\.\d{4,9}/[^\s;,)]+|pmid:?\s*\d+|https?://[^\s;,)]+|\b(?:ng|cg|ta)\d{2,4}\b)",
                     src.get("source_identifier") or "")
    return {re.sub(r"\s+", "", t).lower().rstrip(".") for t in ids}


def patient_state(rec):
    """The case's mentions without the rule: a patient state that could recur under another rule."""
    return tuple(sorted((m["concept"], str(m["value"]), m["subject"], m["status"], m["time"]) for m in rec["state"]))


def base_state_key(rec):
    return (rec["rid"], patient_state(rec))


def overlap(train_rules, train_tpl, train_states, train_sources, sets, sources, train_patients=frozenset()):
    tr_prog = {program_key(r) for r in train_rules}
    tr_struct = {structure_key(r) for r in train_rules}
    tr_crit = {crit_key(c) for r in train_rules for c in r.criteria}
    tr_text = {t.rule_text() for t in train_rules}
    out = {}
    for name, recs in sets.items():
        rules = [RB[x] for x in sorted({r["rid"] for r in recs})]
        crits = [crit_key(c) for r in rules for c in r.criteria]
        cases = [r for r in recs if r["claim_type"] == "conclusion" and r["claim_role"] == "s"]
        texts = [r["case_text"] for r in cases]
        tpl = {tuple(t) for r in cases for t in r["meta"]["tpl"]}
        bases = {base_state_key(r) for r in cases if r["case_kind"] == "base"}
        patients = {patient_state(r) for r in cases if r["case_kind"] == "base"}
        cue_pct, cue_words = hits(CUE_RE["train"], texts)
        rel_pct, rel_words = hits(PERSON_RE["train"], texts)
        srcd = [r for r in rules if sources.get(r.rid, {}).get("source_identifier")]
        by_tid = defaultdict(dict)
        for r in cases:
            by_tid[r["tid"]][r["case_kind"]] = r["case_text"].splitlines()
        edits = {k: [ln for g in by_tid.values() if k in g and "base" in g for ln in set(g[k]) - set(g["base"])]
                 for k in ("flip", "near")}
        out[name] = {
            "rules": len(rules), "cases": len(texts),
            "program_pct": pct(sum(program_key(r) in tr_prog for r in rules), len(rules)),
            "structure_pct": pct(sum(structure_key(r) in tr_struct for r in rules), len(rules)),
            "subexpression_pct": pct(sum(k in tr_crit for k in crits), len(crits)),
            "rule_text_pct": pct(sum(r.rule_text() in tr_text for r in rules), len(rules)),
            "templates_shared": len(tpl & train_tpl), "templates": len(tpl),
            "cases_with_train_cue_pct": cue_pct, "train_cue_words_seen": cue_words,
            "cases_with_train_relative_pct": rel_pct, "train_relatives_seen": rel_words,
            "flip_lines_with_train_cue_pct": hits(CUE_RE["train"], edits["flip"])[0],
            "near_lines_with_train_cue_pct": hits(CUE_RE["train"], edits["near"])[0],
            "near_line_train_cue_words": hits(CUE_RE["train"], edits["near"])[1],
            "near_lines_with_train_relative_pct": hits(PERSON_RE["train"], edits["near"])[0],
            "base_states_shared": len(bases & train_states), "base_states": len(bases),
            "patient_states_shared_any_rule": len(patients & train_patients), "patient_states": len(patients),
            "rules_with_source": len(srcd),
            "source_shared_with_train_pct": pct(sum(bool(source_tokens(sources[r.rid]) & train_sources)
                                                    for r in srcd), len(srcd))}
    return out


# ------------------------------------------------------------------ L3-alt, requirements
def l3alt(G):
    rows = []
    for recs in G.values():
        r0 = recs[0]
        c = RB[r0["rid"]].crit(r0["cid"])
        fv = next(m["value"] for m in case_of(recs, "flip")["state"]
                  if m["concept"] == c.concept and m["time"] == "current")
        rows.append({"rid": r0["rid"], "cid": c.cid, "concept": c.concept, "kind": r0["nm_kind"],
                     "moved": "lower" if c.alt_threshold < c.threshold else "higher",
                     "between": min(c.threshold, c.alt_threshold) <= fv <= max(c.threshold, c.alt_threshold),
                     "thresholds_moved": len(r0["meta"]["overrides"])})
    return {"groups": len(rows), "rules": len({r["rid"] for r in rows}),
            "criteria": len({(r["rid"], r["cid"]) for r in rows}),
            "near_miss_kinds": dict(Counter(r["kind"] for r in rows)),
            "threshold_moved": dict(Counter(r["moved"] for r in rows)),
            "thresholds_moved_per_group": dict(Counter(r["thresholds_moved"] for r in rows)),
            "concepts": dict(Counter(r["concept"] for r in rows).most_common()),
            "flips_between_thresholds_pct": pct(sum(r["between"] for r in rows), len(rows))}


PAST_ELSEWHERE = {c.concept for r in LIBRARY for c in r.criteria if c.counts_past}
FAMILY_ELSEWHERE = {c.concept for r in LIBRARY for c in r.criteria if c.counts_family}


def requirements(G):
    n = Counter()
    for recs in G.values():
        r0 = recs[0]
        rule = RB[r0["rid"]]
        c, kind = rule.crit(r0["cid"]), r0["nm_kind"]
        sts = {k: state(case_of(recs, k)) for k in ("base", "flip", "near")}
        fv = [m.value for m in sts["flip"] if m.concept == c.concept and m.time == "current"]
        near_subj = [m.subject for m in sts["near"] if m.concept == c.concept]
        req = {
            "rule_dependent_time_scope": kind == "time" and c.kind == "finding" and c.concept in PAST_ELSEWHERE,
            "rule_dependent_subject_scope": kind == "subject" and c.concept in FAMILY_ELSEWHERE
            and any(s in FIRST_DEGREE for s in near_subj),
            "competing_mentions": any(len([m for m in st if m.concept == c.concept]) >= 2 for st in sts.values()),
            "temporal_selection": c.kind == "numeric" and kind == "time",
            "composition": rule.kind == "constraint" and len(rule.criteria) >= 2,
            "composition_with_other_condition_met": rule.kind == "constraint" and any(
                o.evaluate(sts["base"], r0["meta"]["overrides"].get(o.cid)) for o in rule.criteria if o is not c),
            "numerical_semantics": kind == "boundary" or (
                c.kind == "numeric" and bool(fv) and c.op in (">=", "<=")
                and fv[0] == r0["meta"]["overrides"].get(c.cid, c.threshold)),
            "long_note": r0["tier"] == "long",
            "superseded_value": r0["tier"] == "superseded",
            "delabelled": r0["tier"] == "delabelled",
            "altered_threshold": r0["tier"] == "alt"}
        n["groups"] += 1
        n.update(k for k, x in req.items() if x)
        n["none_of_these"] += not any(req.values())
    return dict(n)


# ------------------------------------------------------------------ semantics actually implemented
YEAR = re.compile(r"\b(19[5-9]\d|20[0-4]\d)\b")
WINDOW = re.compile(r"\b(within|in the (?:past|last)|months? before|weeks? before|days? before|since)\b", re.I)
SCOPE_WORDS = re.compile(r"(?i)any time|history|past|ever|previous|prior|relative|family")


NEG_WORD = re.compile(r"(?i)\b(no|not|none|never|without|negative|free of|denies|denied|nil|ruled out|absent)\b")


def mention_lines(rec):
    """state index -> the case line that renders that mention (meta.tpl lists the body lines in order;
    the case text is header, setting, body)."""
    body = rec["case_text"].split("\n")[2:]
    out, k = {}, 0
    for j, t in enumerate(rec["meta"]["tpl"]):
        if not t.startswith("filler/"):
            out[k] = body[j] if j < len(body) else None
            k += 1
    return out


def semantics(sets):
    s = Counter()
    years = Counter()
    flips = {r["tid"]: r for recs in sets.values() for r in recs
             if r["case_kind"] == "flip" and r["claim_type"] == "conclusion" and r["claim_role"] == "s"}
    for recs in sets.values():
        for rec in recs:
            if rec["claim_type"] != "conclusion" or rec["claim_role"] != "s":
                continue
            st = state(rec)
            rule = RB[rec["rid"]]
            target = rule.crit(rec["cid"])
            s["cases"] += 1
            for c in rule.criteria:
                ms = [m for m in st if m.concept == c.concept]
                if c.kind == "numeric":
                    s["numeric_inputs"] += 1
                    s["numeric_inputs_one_counted_value"] += sum(c.applies(m) for m in ms) == 1
                    s["numeric_inputs_with_older_value"] += any(m.time == "past" for m in ms)
                else:
                    s["finding_inputs"] += 1
                    s["finding_inputs_unmentioned"] += not ms
                    s["finding_inputs_two_or_more_mentions"] += len(ms) >= 2
                    if c is not target:
                        s["context_finding_inputs"] += 1
                        s["context_finding_inputs_unmentioned"] += not ms
            years.update(int(y) for y in YEAR.findall(rec["case_text"]))
            s["past_mentions"] += sum(m.time == "past" for m in st)
            s["past_mentions_with_year"] += sum(m.time == "past" and m.year is not None for m in st)
            if WINDOW.search(rule.rule_text()) and rec["case_kind"] == "base":
                s["groups_rule_text_names_a_window"] += 1
                s["groups_rule_text_names_a_window_time_near_miss"] += rec["nm_kind"] == "time"
            s["cases_naming_year_2025_or_2026"] += bool(re.search(r"\b202[56]\b", rec["case_text"]))
            s["cases_stating_a_reference_date"] += bool(re.search(
                r"(?i)reference date|today is|date of (?:this )?visit", rec["case_text"]))
            if rec["case_kind"] == "base":
                c = rule.crit(rec["cid"])
                if c.kind == "finding":
                    tg = [m for m in st if m.concept == c.concept]
                    s["finding_bases"] += 1
                    s["finding_bases_generic_absence_line"] += any(m.form == "generic" for m in tg)
                    s["finding_bases_no_line"] += not tg
                    s["finding_bases_naming_concept"] += any(k in rec["case_text"].lower() for k in c.keywords)
                    line = mention_lines(rec).get(next((i for i, m in enumerate(st) if m.form == "generic"
                                                        and m.concept == c.concept), -1))
                    s["finding_bases_generic_line_with_negation"] += bool(line and NEG_WORD.search(line))
            if rec["case_kind"] == "flip":
                c = rule.crit(rec["cid"])
                if c.kind == "numeric":
                    thr = rec["meta"]["overrides"].get(c.cid, c.threshold)
                    fv = [m.value for m in st if m.concept == c.concept and m.time == "current"]
                    s["numeric_flips"] += 1
                    s[f"numeric_flips_{'inclusive' if c.op in ('>=', '<=') else 'strict'}"] += 1
                    at = bool(fv) and fv[0] == thr and c.op in (">=", "<=")
                    s["numeric_flips_at_inclusive_threshold"] += at
                    s["numeric_flips_at_inclusive_threshold_outside_alt"] += at and rec["tier"] != "alt"
                    s["numeric_flips_inclusive_outside_alt"] += c.op in (">=", "<=") and rec["tier"] != "alt"
            if rec["case_kind"] == "near" and rec["nm_kind"] == "negation":
                c = rule.crit(rec["cid"])
                flip = flips.get(rec["tid"])
                if flip is not None:
                    fm = [m for m in state(flip) if m.concept == c.concept]
                    nm = [m for m in st if m.concept == c.concept]
                    if fm and nm:
                        diff = sum(getattr(fm[0], a) != getattr(nm[0], a) for a in ("subject", "status", "time"))
                        s["negation_near_misses"] += 1
                        s["negation_near_misses_differing_in_more_than_status"] += diff > 1
    out = dict(s)
    out["dated_years_min"], out["dated_years_max"] = (min(years), max(years)) if years else (None, None)
    out["generator_reference_year"] = E.NOW
    return out


def library_semantics():
    out = {}
    crits = [c for r in LIBRARY for c in r.criteria]
    num = [c for c in crits if c.kind == "numeric"]
    out["criteria"] = len(crits)
    out["criteria_past_or_family_pct"] = pct(sum(c.counts_past or c.counts_family for c in crits), len(crits))
    out["finding_criteria"] = sum(c.kind == "finding" for c in crits)
    out["finding_criteria_past_or_family_pct"] = pct(sum(c.counts_past or c.counts_family for c in crits
                                                         if c.kind == "finding"), out["finding_criteria"])
    out["criteria_counting_past"] = sum(c.counts_past for c in crits)
    out["criteria_counting_family"] = sum(c.counts_family for c in crits)
    out["numeric_criteria"] = len(num)
    out["numeric_criteria_counting_past"] = sum(c.counts_past for c in num)
    out["numeric_criteria_by_operator"] = dict(Counter(c.op for c in num))
    units = {c: unit_of(c) for c in sorted({c.concept for c in num})}
    out["numeric_concepts"] = len(units)
    out["numeric_concepts_one_unit"] = sum(len(u) == 1 for u in units.values())
    out["numeric_concepts_dimensionless"] = sorted(c for c, u in units.items() if not u)
    out["units"] = units
    with_unit = [(r.rid, c.cid, units[c.concept][0]) for r in LIBRARY for c in r.criteria
                 if c.kind == "numeric" and units[c.concept] and units[c.concept][0] not in ("", "years")]
    stated = [x for x in with_unit if unit_stated(x[2], RB[x[0]].rule_text())]
    out["numeric_criteria_with_a_unit"] = len(with_unit)
    out["numeric_criteria_unit_in_rule_text"] = len(stated)
    out["numeric_criteria_unit_not_in_rule_text"] = sorted(f"{a}.{b} ({u})" for a, b, u in set(with_unit) - set(stated))
    out["rule_texts_with_time_window"] = sorted(r.rid for r in LIBRARY if WINDOW.search(r.rule_text()))
    diffs = [abs(len(a.split()) - len(b.split())) for a, b in
             (r.claims(r.criteria[0].cid) for r in LIBRARY if r.kind == "constraint")]
    out["constraint_rules"] = len(diffs)
    out["constraint_claim_word_diff_max"] = max(diffs)
    out["constraint_claim_word_diff_le2_pct"] = pct(sum(d <= 2 for d in diffs), len(diffs))
    return out


def kinds_table(G):
    c = Counter(recs[0]["nm_kind"] for recs in G.values())
    n = sum(c.values())
    return {"groups": n, **{k: {"n": v, "pct": pct(v, n)} for k, v in sorted(c.items())}}


# ------------------------------------------------------------------ reviewers
def reviewers():
    p = ROOT / "audit" / "model_review" / "reviews.json"
    if not p.exists():
        return None
    rows = []
    for r in json.loads(p.read_text(encoding="utf-8")):
        sample = (ROOT / r["sample_file"]).read_text(encoding="utf-8")
        rows.append({"round": r["round"], "reader": r["reader"], "started_utc": r["started_utc"],
                     "groups": len(re.findall(r"(?m)^## \d+\.\d+ ", sample)), "reviewer": r["reviewer"]})
    return {"sessions": len(rows), "people": 0, "groups": sum(r["groups"] for r in rows),
            "groups_round1": sum(r["groups"] for r in rows if r["round"] == 1),
            "groups_round2": sum(r["groups"] for r in rows if r["round"] == 2),
            "rounds": dict(Counter(r["round"] for r in rows)), "per_session": rows}


# ------------------------------------------------------------------ authors' sample sheets (H1)
def facts(rec, rule):
    """The case's facts about the rule's conditions, each with the line that states it. Generic absence
    lines never name the concept by design; unmentioned conditions are listed with their convention."""
    lines, out = mention_lines(rec), []
    for i, m in enumerate(rec["state"]):
        c = next((x for x in rule.criteria if x.concept == m["concept"]), None)
        what = neutral(c) if c else m["concept"]
        q = f' [line: "{lines[i]}"]' if lines.get(i) else ""
        who = "patient" if m["subject"] == "patient" else m["subject"]
        when = "current" if m["time"] == "current" else "past"     # the quoted line says when (a year may be an end year)
        if m["status"] == "unknown":
            out.append(f"{what}: stated as unknown{q}")
        elif m["form"] == "generic":
            out.append(f"{what}: not named; a general line implies absence (counts as absent){q}")
        elif m["kind"] == "numeric":
            out.append(f"{who}: {what} = {E.fmt(m['value'], c) if c else m['value']} ({when}){q}")
        elif m["status"] == "absent":
            out.append(f"{who}: {what} denied by name{q}")     # the quoted line sets the scope ('never', 'now')
        elif m["form"] == "delabelled":
            out.append(f"{who}: {what} label removed (de-labelled; not allergic now){q}")
        else:
            out.append(f"{who}: {what} present ({when}){q}")
    named = {m["concept"] for m in rec["state"]}
    out += [f"{neutral(c)}: not mentioned ({'counts as absent' if c.kind == 'finding' else 'unknown'})"
            for c in rule.criteria if c.concept not in named]
    return out


def neutral(c):
    """The condition's name without the rule's scope words (a past mention of 'active cancer' is cancer)."""
    return re.sub(r"\s*\(patient or first-degree relative\)|^(current|active) | at any time$", "", c.label)


H1_README = """# H1: rendering fidelity (authors)

Each of you reads 75 groups: `sheet_authorN.csv`, or the same rows in `sheets_authorN.md`.

Before you type anything, save a copy of your sheet as `audit/h1/answers_authorN.csv`, with your
assigned id and not your name, and answer only in that copy: regenerating the kit rewrites the
sheets. In Excel, save as "CSV UTF-8 (comma delimited)". No script ever writes the answers file.
Do not open `key.csv` until you have finished; it holds the program's answers. Afterwards,
`python scripts/h1_aggregate.py` compares your answers with the key.

## How to read a row
- Read the case text and answer q2 and q3 first. Only then read Facts and answer q1. Facts are the
  program's reading of the case, so reading them first would steer your answers. The CSV columns
  come in this order.
- The cases of a group share most lines: two cases differ in one line (replaced or added), and one
  case rewords and reorders another. Some groups have a fifth case in which the decisive line is
  missing or says the value is unknown; there the answer is usually "neither". Check the shared
  lines once per group.

## Conventions the labels follow
- A history item (a finding) that is not mentioned is absent. A measurement that is not mentioned is
  unknown. A line saying a condition is unknown, not obtained or unclear makes it unknown.
- Only the patient counts, unless the rule says that relatives (parent, sibling, child) count.
- Only current findings and values count, unless the rule says that past ones count. A value given
  with a year, or described as earlier, replaced or yesterday, is not current.
- Numbers are compared with the stated operator: "above"/"below" are strict, "or more"/"or less"
  are inclusive.
- General lines such as "Walks independently, with no recent trips or slips." do not name the
  condition. Facts lists them as "not named; a general line implies absence (counts as absent)",
  and class-level denials such as "Drug allergies: none known." the same way. Answer q1 = y for
  them, and do not report them as a missing fact.
- Conditions that the case does not mention are listed as "not mentioned", with "(counts as
  absent)" for a finding and "(unknown)" for a measurement.
- "Denied by name" covers whatever the quoted line covers, for example "never" or "now".
- The condition in a criterion claim is the rule's condition with the rule's time and person
  scope: in a rule that counts past heart failure, "heart failure" holds for a patient who had it
  years ago.

## Questions (one row per case; the cases of a group appear in random order)
- **q2_conclusion (s / s' / neither).** Under the rule as stated, which conclusion claim is
  correct? Answer "neither" when the case does not decide it, for example when a needed value is
  unknown.
- **q3_criterion (s / s' / neither, or blank).** The same for the criterion claim. Answer q3
  whenever the row has criterion claims (criterion_s is filled); leave it blank when criterion_s
  is empty.
- **q1_facts_ok (y/n).** Do the quoted lines state exactly the listed facts about the rule's
  conditions: value (in the rule's unit), person, current or past, denial? And does no other line
  of the case bear on a condition of the rule? The header, the setting and unrelated lines are out
  of scope unless they bear on a condition.
- **problem_type** when q1 is n or an answer is unclear: one of dropped negation, wrong subject,
  ambiguous time, conflicting lines, wording, other. Add a note. Answer q1, q2 and q3 even then.

Write the answers exactly as shown: y or n for q1; s, s' or neither for q2 and q3; problem_type
from the list above, required when q1 is n. The script refuses any other value and lists the rows
to correct.
"""
CLASH = ("angioedema", "Face and neck without swelling on examination.", "neck_nodes")


def clashes():
    """Cases whose general line for one condition contradicts a met condition: the angioedema line
    'Face and neck without swelling' next to swollen neck lymph nodes (phrases.OVERLAP has no
    angioedema/neck_nodes group). Labels are unaffected; angioedema counts as absent either way."""
    out = defaultdict(set)
    for n in TEST_SETS:
        for r in load(n):
            if r["claim_type"] == "conclusion" and r["claim_role"] == "s" and CLASH[1] in r["case_text"].split("\n") \
                    and any(m["concept"] == CLASH[2] and m["status"] == "present" and m["subject"] == "patient"
                            and m["time"] == "current" for m in r["state"]):
                out[r["tid"]].add(r["case_kind"])
    return {t: sorted(k) for t, k in sorted(out.items())}


def sample_sheets(out_dir, missing, known=None, seed=2026):
    """The authors' H1 sample: 300 groups (the same selection as before), 75 per author, written to
    out_dir/h1. Sheets carry no program answer; key.csv does. Answer files are never written here.
    The case comes before the program's facts, so the authors answer from the text first. known maps
    tids with a known contradiction to their case kinds; the README lists the affected case ids."""
    plan = [("rule_v1/test_L2", 150), ("rule_v1/test_hard", 50), ("rule_v1/test_L3alt", 30),
            ("rule_v1/test_L3inv", 30), ("rule_v1/test_L1", 20), ("rule_v1/test_L0", 20)]
    rng, picked = random.Random(seed), []
    for name, k in plan:
        G = grouped(name)
        by = defaultdict(list)
        for tid in sorted(G):
            by[G[tid][0]["nm_kind"]].append(tid)
        kinds = sorted(by)
        for kd in kinds:
            rng.shuffle(by[kd])
        i = got = 0
        while got < k:
            kd = kinds[i % len(kinds)]
            if by[kd]:
                picked.append((name, by[kd].pop(), G))
                got += 1
            i += 1
    rng.shuffle(picked)
    h1 = out_dir / "h1"
    h1.mkdir(parents=True, exist_ok=True)
    answers = ["q1_facts_ok", "q2_conclusion", "q3_criterion", "problem_type", "note"]
    for old in sorted(h1.glob("sheet_author*.csv")):     # answers typed into a sheet would be overwritten
        if any(any((r.get(a) or "").strip() for a in answers)
               for r in csv.DictReader(open(old, encoding="utf-8-sig", newline=""))):
            sys.exit(f"refusing to rewrite {old.name}: it holds answers; save it as "
                     f"{old.name.replace('sheet_', 'answers_')} first")
    cols = ["author", "row", "group", "case", "set", "rule_text", "conclusion_s", "conclusion_s_prime",
            "criterion_s", "criterion_s_prime", "context", "case_text", "q2_conclusion", "q3_criterion", "facts",
            "q1_facts_ok", "problem_type", "note"]          # the case and q2/q3 before the program's facts
    sheets, keys, md = defaultdict(list), [], defaultdict(list)
    order_rng = random.Random(seed + 1)
    for gno, (name, tid, G) in enumerate(picked):
        author = f"author{gno % 4 + 1}"
        group = f"G{gno // 4 + 1:02d}"
        recs = G[tid] + missing.get(tid, [])
        rule = RB[recs[0]["rid"]]
        kinds = list(CASES) + ["missing"] * (tid in missing)
        order_rng.shuffle(kinds)
        md[author].append(f"\n## {group}\n\nRule: {recs[0]['rule_text']}\n")
        for j, k in enumerate(kinds):
            claim = {(r["claim_type"], r["claim_role"]): r for r in recs if r["case_kind"] == k}
            c = claim[("conclusion", "s")]
            body = c["case_text"].split("\n")
            fl = facts(c, rule)
            ans = {t: ("neither" if k == "missing" else "s'" if claim[(t, "s_prime")]["label"] else "s")
                   for t in ("conclusion", "criterion") if (t, "s") in claim}
            case_id = f"A{gno % 4 + 1}-{group}-C{j + 1}"      # unique across the four sheets
            row = {"author": author, "row": len(sheets[author]) + 1, "group": group, "case": case_id, "set": name,
                   "rule_text": c["rule_text"], "conclusion_s": c["claim_text"],
                   "conclusion_s_prime": claim[("conclusion", "s_prime")]["claim_text"],
                   "criterion_s": claim.get(("criterion", "s"), {}).get("claim_text", ""),
                   "criterion_s_prime": claim.get(("criterion", "s_prime"), {}).get("claim_text", ""),
                   "facts": " | ".join(fl), "context": f"header: {body[0]} / setting: {body[1]}",
                   "case_text": c["case_text"], **{x: "" for x in answers}}
            sheets[author].append(row)
            keys.append({"author": author, "case": case_id, "tid": tid, "set": name, "case_kind": k,
                         "near_miss_kind": c["nm_kind"], "tier": c["tier"], "level": c["level"],
                         "conclusion_answer": ans["conclusion"], "criterion_answer": ans.get("criterion", "")})
            md[author].append(f"**{case_id}**\n\nClaims: s = {row['conclusion_s']} | s' = {row['conclusion_s_prime']}"
                              + (f"\n\nCriterion claims: s = {row['criterion_s']} | s' = {row['criterion_s_prime']}"
                                 if row["criterion_s"] else "") + f"\n```\n{c['case_text']}\n```\n"
                              + "\nFacts (for q1, after q2 and q3):\n" + "".join(f"- {x}\n" for x in fl))
    flagged = [k["case"] for k in keys if k["case_kind"] in (known or {}).get(k["tid"], ())]
    note = (f"\n## Known issue in these sheets\nCases {', '.join(flagged)} contain the general line "
            f"\"{CLASH[1]}\", which contradicts their swollen neck lymph nodes. Answer q1 = n with "
            f"problem_type 'conflicting lines', and answer q2 and q3 by the conventions (the general line "
            f"counts as absence of angioedema).\n") if flagged else ""
    (h1 / "README.md").write_text(H1_README + note, encoding="utf-8")
    for author, rows in sheets.items():
        with open(h1 / f"sheet_{author}.csv", "w", encoding="utf-8-sig", newline="") as f:   # BOM: Excel reads UTF-8
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
        (h1 / f"sheets_{author}.md").write_text(f"# H1 sheet {author} (75 groups)\n\nRead `README.md` first.\n"
                                                 + "\n".join(md[author]), encoding="utf-8")
    with open(h1 / "key.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(keys[0]))
        w.writeheader()
        w.writerows(keys)
    return {"groups": len(picked), "per_set": dict(Counter(p[0] for p in picked)),
            "per_kind": dict(Counter(p[2][p[1]][0]["nm_kind"] for p in picked)),
            "with_missing_twin": sum(p[1] in missing for p in picked),
            "rows_per_author": {a: len(r) for a, r in sorted(sheets.items())},
            "rows_with_criterion_claims": sum(bool(k["criterion_answer"]) for k in keys),
            "rows_with_known_contradiction": len(flagged)}


# ------------------------------------------------------------------ main
def main():
    src_path = DATA / "rule_v1" / "RULE_SOURCES.json"
    sources = {s["rid"]: s for s in json.loads(src_path.read_text(encoding="utf-8"))} if src_path.exists() else {}
    man = manifest(sources)
    (DATA / "rule_v1" / "RULE_MANIFEST.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    hand = [m for m in man if m["module"] in ("pilot", "constraint", "score", "grammar_curated")]
    dirty = git("status", "--porcelain", "--", "selrm", "scripts", "tests")
    classes = {"score": {m["signature_class"] for m in man if m["kind"] == "score" and m["module"] != "invented"},
               "constraint_hand_written": {m["signature_class"] for m in hand if m["kind"] == "constraint"},
               "constraint_sampled": {m["signature_class"] for m in man if m["module"] == "grammar_sampled"},
               "library": {m["signature_class"] for m in man if m["module"] != "invented"}}
    stats = {"commit": git("rev-parse", "HEAD"), "code_modified_since_commit": bool(dirty),
             "rules": {"library": len(LIBRARY), "invented_test_only": len(INVENTED),
                       "by_module": dict(Counter(m["module"] for m in man)),
                       "hand_written": len(hand),
                       "hand_written_by_kind": dict(Counter(m["kind"] for m in hand)),
                       "sampled_by_kind": dict(Counter(m["kind"] for m in man if m["module"] == "grammar_sampled")),
                       "provenance": dict(Counter(m["provenance"] for m in man if m["module"] != "invented")),
                       "hand_written_provenance": dict(Counter(m["provenance"] for m in hand)),
                       "hand_written_provenance_by_kind": {k: dict(Counter(m["provenance"] for m in hand
                                                                           if m["kind"] == k))
                                                           for k in ("constraint", "score")},
                       "signature_classes_by_row": {k: len(v) for k, v in classes.items()},
                       "sources_checked": len(sources),
                       "sources_verified_online": sum(bool(s.get("source_verified")) for s in sources.values()),
                       "sources_with_contradictions": sum(bool(s.get("contradictions")) for s in sources.values()),
                       "sources_simplifications_listed": sum(len(s.get("simplifications", [])) for s in sources.values()),
                       "signature_classes": len(FOLDS["classes"]), "folds": len(FOLDS["folds"]),
                       "fold1": {k: len(F1[k]) for k in ("train_rules", "l1_rules", "l2_rules")},
                       "fold1_l2_classes": F1["l2_classes"]},
             "library_semantics": library_semantics(),
             "training_corpora_records": {n.split("/")[-1]: REG[n]["n_records"] for n in TRAIN_MAIN},
             "lexicons": {**{name: {"train": len(lex["train"]), "test": len(lex["test"]),
                                    "shared": len(set(lex["train"]) & set(lex["test"]))}
                             for name, lex in (("negation_cues", P.NEG_CUES), ("time_cues", P.TIME_CUES),
                                               ("current_cues", P.CURRENT_CUES))},
                          "persons": {"train": len(P.by_split(P.PERSONS, "train")),
                                      "test": len(P.by_split(P.PERSONS, "test")),
                                      "shared": len(set(P.by_split(P.PERSONS, "train"))
                                                    & set(P.by_split(P.PERSONS, "test")))}}}
    log("manifest")

    issues, n_groups, n_records, cov = target_claim_check()
    stats["target_claim_check"] = {"sets": TEST_SETS, "groups": n_groups, "groups_total": sum(n_groups.values()),
                                   "records": n_records, "records_total": sum(n_records.values()),
                                   "coverage": cov, "violations": len(issues),
                                   "by_check": dict(Counter(i["check"] for i in issues))}
    window_tids = sorted({r["tid"] for n in TRIPLET_SETS for r in load(n)
                          if WINDOW.search(RB[r["rid"]].rule_text())})
    clash = clashes()
    unscoped = sorted(f"{rule.rid}.{c.cid}" for rule in list(LIBRARY) + list(INVENTED) for c in rule.criteria
                      if c.kind == "finding" and (c.counts_past or c.counts_family)
                      and not SCOPE_WORDS.search(E.condition_text(c, c.threshold)))
    invented_ids = {r.rid for r in INVENTED}
    stats["known_semantic_limits"] = {
        "general_line_contradicts_condition": {"groups": len(clash), "cases": sum(len(k) for k in clash.values())},
        "criterion_claim_without_scope": len(unscoped),
        "criterion_claim_without_scope_invented": sum(u.split(".")[0] in invented_ids for u in unscoped)}
    (DATA / "rule_v1" / "KNOWN_ISSUES.json").write_text(json.dumps(
        {"generated_by": "scripts/audit_rule_v1.py", "commit": stats["commit"], "checked_sets": TEST_SETS,
         "issues": issues,
         "semantic_limits": [
             {"id": "rule_text_names_a_window", "tids": window_tids,
              "reason": "The rule text names a window ('in the six months before this admission'); the program "
                        "counts current mentions only and past mentions are dated or 'years ago'. With no visit "
                        "date in the case, these labels rely on the unstated year."},
             {"id": "negation_near_miss_two_attributes",
              "reason": "On criteria that count past or family mentions, a negation near-miss (the patient's "
                        "current denial) differs from a past or relative flip in time or subject as well as "
                        "status; counts in tables/data_stats.json (semantics)."},
             {"id": "general_line_contradicts_condition", "cases": clash,
              "reason": f"The angioedema general line '{CLASH[1]}' can sit next to the met condition 'Tender, "
                        "swollen lymph nodes in the front of the neck.' (phrases.OVERLAP has no angioedema/"
                        "neck_nodes group). Labels are unaffected: angioedema counts as absent either way. For "
                        "new sets, add the pair to OVERLAP."},
             {"id": "criterion_claim_without_scope", "criteria": unscoped,
              "reason": "The criterion claim names the condition without the rule's time or person scope (the "
                        "condition 'heart failure' holds) although the criterion counts past or family mentions; "
                        "the claim is read under the rule, which states the scope. For new sets, put the scope "
                        "in the label."},
             {"id": "presentation_diastolic",
              "reason": "Presentation edits may switch between 'blood pressure x/y' and systolic-only templates, "
                        "so a derived diastolic value can appear or disappear; the state is unchanged."}]},
        indent=1), encoding="utf-8")

    stats["rejects"] = rejects()

    tr = judgment_rows(grouped("rule_v1/train_triplets"))
    l2 = judgment_rows(grouped("rule_v1/test_L2"))
    stats["structure"] = {"train_triplets": summarize(tr), "test_L2": summarize(l2),
                          "per_family": {sp: {f: summarize([r for r in rows if r["family"] == f])
                                              for f in sorted({r["family"] for r in rows})}
                                         for sp, rows in (("train_triplets", tr), ("test_L2", l2))}}
    log("structure")

    sets = {n: list(load(n)) for n in TRIPLET_SETS}
    stats["overlap"] = {}
    for fold, prefix, corpora in (("1", "rule_v1/", TRAIN_MAIN),
                                  ("2", "rule_v1_fold2/", ["rule_v1_fold2/train_blocks", "rule_v1_fold2/train_triplets"]),
                                  ("3", "rule_v1_fold3/", ["rule_v1_fold3/train_blocks", "rule_v1_fold3/train_triplets"])):
        train_rules = [RB[x] for x in FOLDS["folds"][fold]["train_rules"]]
        train_tpl, train_states, train_patients, texts = set(), set(), set(), set()
        for n in corpora:
            for r in load(n):
                train_tpl.update(tuple(t) for t in r["meta"]["tpl"])
                if r["case_kind"] == "base":
                    train_states.add(base_state_key(r))
                    train_patients.add(patient_state(r))
                texts.add(r["case_text"])
        if fold == "1":
            train_texts = texts
        train_sources = {t for r in train_rules if r.rid in sources for t in source_tokens(sources[r.rid])}
        stats["overlap"].update(overlap(train_rules, train_tpl, train_states, train_sources,
                                        {n: v for n, v in sets.items() if n.startswith(prefix)}, sources,
                                        train_patients))
        log(f"overlap fold {fold}")
    tc_pct, tc_words = hits(CUE_RE["test"], train_texts)
    tr_pct, tr_words = hits(PERSON_RE["test"], train_texts)
    stats["overlap_train_side"] = {"distinct_train_case_texts": len(train_texts), "cases_with_test_cue_pct": tc_pct,
                                   "test_cue_words_seen": tc_words, "cases_with_test_relative_pct": tr_pct,
                                   "test_relatives_seen": tr_words}
    log("overlap")

    stats["l3alt"] = l3alt(grouped("rule_v1/test_L3alt"))
    stats["requirements"] = {n: requirements(grouped(n)) for n in TRIPLET_SETS}
    stats["near_miss_kinds"] = {n: kinds_table(grouped(n)) for n in TRIPLET_SETS}
    stats["semantics"] = {"test_L2": semantics({"rule_v1/test_L2": sets["rule_v1/test_L2"]}),
                          "all_test_and_dev": semantics(sets)}
    log("requirements and semantics")
    stats["reviewers"] = reviewers()
    miss = defaultdict(list)
    for r in load("rule_v1/missing"):
        if r["case_kind"] == "missing":
            miss[r["tid"]].append(r)
    stats["sample_sheets"] = sample_sheets(ROOT / "audit", miss, clash)
    (ROOT / "tables").mkdir(exist_ok=True)
    (ROOT / "tables" / "data_stats.json").write_text(json.dumps(stats, indent=1, default=str), encoding="utf-8")
    log("done")
    print(json.dumps({k: stats[k] for k in ("rules", "target_claim_check")}, indent=1, default=str))


if __name__ == "__main__":
    main()
