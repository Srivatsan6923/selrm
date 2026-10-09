"""kb_v1: support check and knowledge-base triplets from DDXPlus patients (STAGE2_TASKS_A, A2.3-5).

A case is a DDXPlus patient written as sex, age and one line per finding (question, answer). The criterion
is selrm.kb_criterion.render(A, B); labels follow from its procedure: a finding listed for one diagnosis only
excludes the other; findings of both exclusive lists, or of neither, leave the pair undecided.
"""
import ast
import csv
import hashlib
import io
import re
import zipfile

from selrm import kb_criterion as K

SET = "kb_v1"
RELATIVES = ("sister", "father")
FAMILY_Q = re.compile(r"\bfamil|\brelative|\bparent|\bsibling", re.I)
PAST_Q = re.compile(r"\bever\b|\bin the past\b|\bprevious|\bhistory\b|\balready\b|\bin the last\b|\bwithin the last\b|\brecent", re.I)
SUBJECT_PREFIX = "About the patient's {rel}: "


def patients(split):
    """Rows of release_<split>_patients.zip as dicts with parsed evidences; pid = row number in the file."""
    with zipfile.ZipFile(K.EXT / f"release_{split}_patients.zip") as z:
        with z.open(z.namelist()[0]) as f:
            for pid, r in enumerate(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8"))):
                yield {"pid": pid, "age": int(r["AGE"]), "sex": r["SEX"], "pathology": r["PATHOLOGY"],
                       "evidences": ast.literal_eval(r["EVIDENCES"])}


def answers(evidences):
    """{evidence code: True | value code | [value codes]} of a patient, in the order of first appearance."""
    ev = K.kb()[1]
    out = {}
    for e in evidences:
        code, _, val = e.partition("_@_")
        t = ev[code]["data_type"]
        if t == "B":
            out[code] = True
        elif t == "C":
            out[code] = val
        else:
            out.setdefault(code, []).append(val)
    return out


def present(ans):
    """Codes that count as present: binary yes; a categorical or multi-choice answer other than the default."""
    ev = K.kb()[1]
    out = set()
    for code, v in ans.items():
        if v is True:
            out.add(code)
        elif v is not False and v is not None:
            vals = v if isinstance(v, list) else [v]
            if any(str(x) != str(ev[code]["default_value"]) for x in vals):
                out.add(code)
    return out


def decide(codes, a, b):
    """The procedure on a set of present codes: a, b, or None (undecided)."""
    only_a, only_b, _ = K.lists(a, b)
    in_a, in_b = bool(codes & set(only_a)), bool(codes & set(only_b))
    return a if in_a and not in_b else b if in_b and not in_a else None


def _value(code, v):
    ev = K.kb()[1][code]
    m = ev["value_meaning"].get(str(v))
    return m["en"] if m else str(v)


def line(code, v, rel=None):
    ev = K.kb()[1]
    q = ev[code]["question_en"]
    if v is True:
        a = "Yes"
    elif v is False:
        a = "No"
    else:
        a = "; ".join(_value(code, x) for x in v) if isinstance(v, list) else _value(code, v)
    return (SUBJECT_PREFIX.format(rel=rel) if rel else "") + f"{q} {a}"


def case_text(p, ans, extra=()):
    """Sex, age, then one line per finding; extra lines (code, value, relative) follow in the given order."""
    head = f"Sex: {p['sex']}, Age: {p['age']}"
    return "\n".join([head] + [line(c, v) for c, v in ans.items()] + [line(c, v, rel) for c, v, rel in extra])


def read_case(text):
    """Present codes of the patient from a case text (the executor's reading): the inverse of case_text.
    A line about a relative and a line answered No do not count."""
    ev = K.kb()[1]
    by_q = {}
    for code, e in ev.items():
        by_q.setdefault(e["question_en"], []).append(code)
    ans = {}
    for ln in text.split("\n")[1:]:
        if ln.startswith("About the patient's"):
            continue
        q = next((q for q in sorted(by_q, key=len, reverse=True) if ln.startswith(q + " ")), None)
        if q is None:
            raise ValueError(f"unreadable line: {ln}")
        a = ln[len(q) + 1:]
        for code in by_q[q]:
            e = ev[code]
            if e["data_type"] == "B":
                ans[code] = a == "Yes"
            else:
                names = {m["en"]: v for v, m in e["value_meaning"].items()}
                vals = [names.get(x, x) for x in a.split("; ")]
                ans[code] = vals if e["data_type"] == "M" else vals[0]
    return present(ans)


def _h(*parts):
    return int(hashlib.sha256("/".join(str(x) for x in parts).encode("utf-8")).hexdigest(), 16)


def scope(code):
    q = K.kb()[1][code]["question_en"]
    return "family" if FAMILY_Q.search(q) else "past" if PAST_Q.search(q) else "plain"


def triplets(p, a, b, seed):
    """The triplet groups of patient p (pathology a) against b, or [] if the patient does not qualify.

    Base: the patient (decided for a). Flip: a-only findings removed, one or two b-only binary findings
    affirmed (decided for b). Near-miss: one b-only binary finding answered No (negation), or affirmed for a
    relative (subject; only for questions that are not themselves about the family).
    """
    ev = K.kb()[1]
    only_a, only_b, _ = K.lists(a, b)
    ans = answers(p["evidences"])
    codes = present(ans)
    if decide(codes, a, b) != a:
        return []
    addable = [c for c in only_b if ev[c]["data_type"] == "B" and c not in ans]
    if not addable:
        return []
    addable.sort(key=lambda c: _h(seed, p["pid"], a, b, c))
    n_add = 1 + _h(seed, p["pid"], a, b, "n") % 2
    added = addable[:n_add]
    flip_ans = {c: v for c, v in ans.items() if c not in only_a}
    flip_text = case_text(p, flip_ans, [(c, True, None) for c in added])
    flip_codes = (codes - set(only_a)) | set(added)
    if decide(flip_codes, a, b) != b:
        return []
    out = []
    near_code = added[0]
    plans = [("negation", (near_code, False, None))]
    if scope(near_code) != "family":
        plans.append(("subject", (near_code, True, RELATIVES[_h(seed, p["pid"], a, b, "rel") % len(RELATIVES)])))
    for kind, extra in plans:
        near_text = case_text(p, ans, [extra])
        out.append({"kind": kind, "base": (case_text(p, ans), codes), "flip": (flip_text, flip_codes),
                    "near": (near_text, codes), "added": added, "near_code": near_code,
                    "flip_scope": sorted({scope(c) for c in added})})
    return out


def records(p, a, b, split, seed):
    first, second = sorted((a, b))
    rule = K.render(a, b)
    out = []
    for g in triplets(p, a, b, seed):
        tid = f"kb_{split}_{p['pid']:06d}_{_h(a, b) % 10 ** 6:06d}_{g['kind']}"
        for ck in ("base", "flip", "near"):
            text, codes = g[ck]
            truth = decide(codes, a, b)
            for role, dx in (("s", a), ("s_prime", b)):
                out.append({
                    "iid": f"{tid}/{ck}/conclusion/{role}", "tid": tid, "set": SET, "split": split, "tier": "external",
                    "level": "external", "rid": f"{a} -> {b}", "cid": "diagnosis", "family": a, "nm_kind": g["kind"],
                    "case_kind": ck, "rule_text": rule, "case_text": text,
                    "condition": f"the most likely diagnosis: {first} or {second}", "claim_type": "conclusion",
                    "claim_role": role, "claim_text": f"The most likely diagnosis is {dx}.", "label": int(truth == dx),
                    "state": [{"code": c} for c in sorted(codes)], "ledger": [], "prose": "",
                    "meta": {"pid": p["pid"], "pathology": a, "other": b, "added": g["added"], "near_code": g["near_code"],
                             "flip_scope": g["flip_scope"], "source": "DDXPlus " + split + " patients"},
                    "crit": {"source": "derived", "provenance": K.PIN["source"] + "; selrm.kb_criterion.render",
                             "text_sha": K.text_sha(a, b)},
                    "cluster": f"p{p['pid']}", "struct": {"only_a": K.lists(a, b)[0], "only_b": K.lists(a, b)[1]},
                })
    return out
