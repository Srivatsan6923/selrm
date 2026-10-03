"""challenge_v1: author-written cases from state specifications (FINAL_TASKS A P0.3; HUMAN_TASKS H2).

  python scripts/challenge_v1.py kit        # specs + writing forms in challenge_v1/
  python scripts/challenge_v1.py assemble   # notes_<name>.md -> notes_<name>.jsonl -> records, report
  python scripts/challenge_v1.py assemble --freeze   # register data/challenge_v1/test when complete

160 groups on L2 rules (fold 1), 32 per near-miss kind, easy tier. A group's states come from the
engine (same programs and invariants as rule_v1), but the authors never see generated text: the
form lists the facts of each case in plain words. Labels are computed by executing the rule
program on the specified states. A group enters the set only if its notes pass the assembler's
checks and a second author has marked it correct.
"""
import argparse
import datetime
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import engine as E  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm import rules_grammar as RG  # noqa: E402
from selrm.schema import validate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "challenge_v1"
SET, N, AUTHORS = "challenge_v1", 160, ("author1", "author2", "author3", "author4")
NAME = {"aspirin": "daily aspirin use", "bleeding": "a major bleed", "cad": "coronary artery disease",
        "cancer": "cancer", "chf": "heart failure", "confusion": "new confusion", "crc": "colorectal cancer",
        "diabetes": "diabetes", "exudate": "tonsillar exudate", "fall": "a fall",
        "hemoptysis": "coughing up blood (hemoptysis)", "mech_valve": "a mechanical heart valve",
        "neck_nodes": "tender anterior cervical lymph nodes", "pen_allergy": "a penicillin allergy",
        "peptic_ulcer": "a peptic ulcer", "rlq_tenderness": "right lower quadrant tenderness",
        "sulfa_allergy": "a sulfonamide allergy", "supp_oxygen": "supplemental oxygen",
        "vascular": "a myocardial infarction or peripheral artery disease", "warfarin": "warfarin treatment",
        "vte": "a venous thromboembolism (DVT or pulmonary embolism)", "stroke": "a stroke or TIA",
        "pregnancy": "pregnancy", "clarithromycin": "clarithromycin treatment", "hit": "heparin-induced thrombocytopenia"}


def unit(concept):
    if concept in RG.NUMERIC_NAMES:
        return RG.NUMERIC_NAMES[concept][1]
    t = P.BANKS[concept]["current"][0]
    m = re.search(r"\{v\}\s?([^\s;,]+)", t)
    u = m.group(1).rstrip(".") if m else ""
    return u if u and not u.isalpha() or u in ("kg", "cm", "mmHg") else ""


def name(c):
    if c.kind == "numeric":
        return c.label
    return NAME.get(c.concept) or re.sub(r"\s*\(patient or first-degree relative\)|^(current|active) | at any time$",
                                         "", c.label)


def fact(m, by_concept):
    """A mention of the state in plain words (None: not stated; the closed world makes it absent)."""
    c = by_concept[m["concept"]]
    who = "the patient" if m["subject"] == "patient" else f"the patient's {m['subject']}"
    if m["kind"] == "numeric":
        u = unit(c.concept)
        v = E.fmt(m["value"], c) + ("" if not u or u[0] in "/%" else " ") + u
        if m["time"] == "current":
            return f"{name(c)}: {v}, the current value"
        if m["form"] == "superseded":
            return f"an earlier {name(c)} of {v}, measured yesterday and replaced by today's value"
        return f"an earlier {name(c)} of {v}, measured in {m['year']}" if m["year"] else \
            f"an earlier {name(c)} of {v}, measured years ago"
    when = f"in {m['year']}" if m["year"] else "years ago"
    if c.concept == "fall":                       # an event, counted in the months before admission
        if m["status"] == "absent":
            return None if m["form"] == "generic" else \
                f"{who} explicitly has not fallen in the past six months (a clear denial)"
        if m["time"] == "current":
            return f"{who} fell once at home in the weeks before this admission"
        return f"{who} fell {when}, long before the past six months"
    if m["status"] == "absent":
        return None if m["form"] == "generic" else f"{who} explicitly does not have {name(c)} (a clear denial)"
    if m["time"] == "current":
        return f"{who} has {name(c)} now"
    return f"{who} had {name(c)} in the past ({when}); it is over or resolved, not current"


PERSON_WORDS = sorted(set(P.PERSONS) | {"son", "daughter", "mother", "father", "sister", "brother", "wife", "husband",
                                       "partner", "parent", "sibling", "child", "aunt", "uncle", "cousin", "niece",
                                       "nephew", "grandmother", "grandfather", "friend", "neighbor", "neighbour"})
PERSON_RE = re.compile(r"(?i)(?<![\w-])(" + "|".join(map(re.escape, PERSON_WORDS)) + r")s?(?![\w-])")
DENIAL = re.compile(r"(?i)\b(no|not|never|denies|denied|without|negative|free of|ruled out|none|nor)\b|n't\b")
PAST = re.compile(r"(?i)\b(ago|previous(ly)?|history|resolved|until|former(ly)?|past|earlier|used to|had|"
                  r"recovered|outgrew|outgrown|was|were|stopped|discontinued|yesterday|replaced|(19|20)\d\d)\b")
SEX = re.compile(r"(?i)\b(woman|man|female|male|lady|gentleman)\b")
FALL = re.compile(r"(?i)\bf(a|e)ll(s|en|ing)?\b")
UNIT_RE = {"mg/dL": r"mg\s*/\s*dl", "mmol/L": r"mmol\s*/\s*l|meq\s*/\s*l", "x10^9/L": r"10\s*\^?\s*9|10⁹|×\s*10",
           "mL/min/1.73 m2": r"ml\s*/\s*min", "g/dL": r"g\s*/\s*dl", "mmHg": r"mm\s*hg", "/min": r"/\s*min|per minute|bpm|breaths|beats",
           "C": r"°\s*c\b|\bc\b|celsius|degrees", "%": r"%|percent", "kg": r"\bkg\b|kilogram", "kg/m2": r"kg\s*/\s*m",
           "U/L": r"u\s*/\s*l|units", "years": r"year|\byrs?\b|\baged?\b", "cm": r"\bcm\b|centimet"}


def kw_pattern(kw):
    """Keywords are lower-case stems matched at the start of a word; a trailing space marks a whole word."""
    return re.compile(r"(?i)\b" + re.escape(kw.strip()) + (r"\b" if kw.endswith(" ") else ""))


def names(text, keywords, concept=None):
    return bool(concept == "fall" and FALL.search(text)) or any(kw_pattern(k).search(text) for k in keywords)


def shown(keywords, concept=None):
    return " | ".join(f"'{k.strip()}'" for k in keywords) + (" | 'fell' | 'fall'" if concept == "fall" else "")


def _diff(base, other):
    return [m for m in base if m not in other], [m for m in other if m not in base]


# ---------------------------------------------------------------- kit
def specs():
    F = json.loads((ROOT / "data" / "rule_v1" / "FOLDS.json").read_text(encoding="utf-8"))["folds"]["1"]
    cells = D.sample_specs([D.RULES_BY_ID[x] for x in F["l2_rules"]], N, SET, tier_w={"easy": 1})
    out = []
    for i, (rid, cid, nm, tier) in enumerate(cells):
        recs = E.make_group(D.RULES_BY_ID[rid], cid, nm, tier, "test", i, SET, "L2")
        rule, crit = D.RULES_BY_ID[rid], D.RULES_BY_ID[rid].crit(cid)
        by_concept = {c.concept: c for c in rule.criteria}
        st = {k: next(r["state"] for r in recs if r["case_kind"] == k) for k in ("base", "flip", "near")}
        head = next(r["case_text"] for r in recs if r["case_kind"] == "base").split("\n")[0]
        age = re.search(r"\d+", head)
        sex = "female" if re.search(r"(?i)\b(woman|female)\b", head) else "male"
        facts = [{"mention": m, "text": fact(m, by_concept)} for m in st["base"]]
        stated = [f for f in facts if f["text"]]
        edits = {}
        for k in ("flip", "near"):
            removed, added = _diff(st["base"], st[k])
            assert len(added) == 1 and len(removed) <= 1, (rid, k)
            idx = next((j for j, f in enumerate(stated) if removed and f["mention"] == removed[0]), None)
            edits[k] = {"op": "replace" if idx is not None else "add", "fact": None if idx is None else idx + 1,
                        "text": fact(added[0], by_concept), "mention": added[0]}
        out.append({"gid": f"c{i + 1:03d}", "tid": recs[0]["tid"], "rid": rid, "cid": cid, "nm_kind": nm, "tier": tier,
                    "rule_text": recs[0]["rule_text"], "setting": rule.setting,
                    "patient": (f"{age.group(0)}-year-old " if age else "adult ") + sex, "sex": sex,
                    "facts": [{"n": j + 1, "text": f["text"], "mention": f["mention"]} for j, f in enumerate(stated)],
                    "edits": edits, "states": st, "concept": name(crit), "keywords": list(crit.keywords),
                    "other_keywords": sorted({k for c in rule.criteria if c is not crit for k in c.keywords}),
                    "labels": {k: E.case_labels(rule, crit, recs[0]["meta"]["overrides"], E.state_from_json(st[k]))
                               for k in st}})
    rng = random.Random(SET)
    by_kind = defaultdict(list)
    for s in out:
        by_kind[s["nm_kind"]].append(s)
    for kind in sorted(by_kind):                    # 8 groups of every kind per author
        g = by_kind[kind]
        rng.shuffle(g)
        for j, s in enumerate(g):
            s["author"] = AUTHORS[j % 4]
            s["checker"] = AUTHORS[(j + 1) % 4]
    return out


def form(s):
    lines = [f"## {s['gid']}   (writer: {s['author']}; checker: {s['checker']})", "",
             f"Rule, for context only (do not refer to it in the note): {s['rule_text']}", "",
             f"Patient: {s['patient']}. Reason for the visit: {s['setting']}", "",
             "BASE note: one line for each fact below, in this order, in your own words."]
    lines += [f"  fact {f['n']}: {f['text']}" for f in s["facts"]]
    if not s["facts"]:
        lines.append("  (no fact to state beyond the patient and the reason for the visit)")
    if D.RULES_BY_ID[s["rid"]].crit(s["cid"]).kind == "finding":
        lines.append(f"  Do not mention {s['concept']} in the base note at all, not even to deny it.")
    for k, lab in (("flip", "FLIP"), ("near", "NEAR-MISS")):
        e = s["edits"][k]
        where = f"replaces your line for fact {e['fact']}" if e["op"] == "replace" else "is added to the base note"
        lines.append(f"{lab}: one line that {where}, stating: {e['text']}.")
    lines += [f"Every line that mentions {s['concept']} must contain one of these words (a longer word that starts "
              f"with one is fine): {shown(s['keywords'], D.RULES_BY_ID[s['rid']].crit(s['cid']).concept)}.", "",
              "header: ", "reason: "] + [f"fact {f['n']}: " for f in s["facts"]] + \
             ["extra: ", "FLIP: ", "NEAR: ", "check_ok: ", "check_comment: ", ""]
    return "\n".join(lines)


def kit():
    S = specs()
    KIT.mkdir(exist_ok=True)
    with open(KIT / "specs.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for s in S:
            f.write(json.dumps(s, sort_keys=True) + "\n")
    for a in AUTHORS:
        mine = sorted((s for s in S if s["author"] == a), key=lambda s: s["gid"])
        head = (f"# challenge_v1 writing form: {a}\n\nRead `challenge_v1/WRITING_GUIDE.md` first. Fill in every "
                f"field after the colon. Save this file as `challenge_v1/notes_<your name>.md`.\n"
                f"{len(mine)} groups; your second author fills `check_ok` and `check_comment`.\n\n")
        (KIT / f"form_{a}.md").write_text(head + "\n".join(form(s) for s in mine), encoding="utf-8")
    print(json.dumps({"groups": len(S), "by_kind": Counter(s["nm_kind"] for s in S),
                      "by_author": Counter(s["author"] for s in S),
                      "by_author_kind": Counter((s["author"], s["nm_kind"]) for s in S).most_common(3)}, default=str))


# ---------------------------------------------------------------- assemble
FIELD = re.compile(r"^(header|reason|fact \d+|extra|FLIP|NEAR|check_ok|check_comment):[ \t]*(.*)$")


def parse(md):
    """{gid: {field: value}} from a filled form (extra may repeat)."""
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r"^## (c\d{3})\b", line)
        if m:
            cur = out.setdefault(m.group(1), {"extra": []})
            continue
        m = FIELD.match(line)
        if cur is not None and m:
            k, v = m.group(1), m.group(2).strip()
            if k == "extra":
                if v:
                    cur["extra"].append(v)
            else:
                cur[k] = v
    return out


def check(s, n):
    """Problems of one filled group ([] if none). Each FLIP, NEAR and fact line is checked against its
    mention: required words, value as a number with its unit, year, person, denial, past; the base
    must not name the decisive finding, and no case may name a condition the specification leaves
    unmentioned; the header gives the stated age and sex."""
    errs = []
    need = ["header", "reason", "FLIP", "NEAR"] + [f"fact {f['n']}" for f in s["facts"]]
    errs += [f"{k} is empty" for k in need if not n.get(k)]
    if errs:
        return errs
    rule = D.RULES_BY_ID[s["rid"]]
    crit = rule.crit(s["cid"])
    hdr = n["header"]
    if s["patient"].startswith("adult"):
        if re.search(r"\d", hdr):
            errs.append("header: give no age here (the age is a fact of the rule)")
    elif not re.search(r"(?<!\d)" + re.match(r"\d+", s["patient"]).group(0) + r"(?!\d)", hdr):
        errs.append(f"header: the age {re.match(r'[0-9]+', s['patient']).group(0)} is not given")
    if not SEX.search(hdr):
        errs.append("header: the sex is not given")
    for k, t in assemble_texts(s, n).items():
        if crit.kind == "finding" and k == "base" and names(t, s["keywords"], crit.concept):
            errs.append(f"base: names {s['concept']}, which the base must not mention")
        stated = {m["concept"] for m in s["states"][k] if m["form"] != "generic"}
        for c in rule.criteria:
            if c is not crit and c.kind == "finding" and c.concept not in stated and names(t, c.keywords, c.concept):
                errs.append(f"{k}: mentions {c.label}, which the specification leaves unmentioned")
    lines = [(f"fact {f['n']}", f["mention"], n[f"fact {f['n']}"]) for f in s["facts"]] + \
            [(key, s["edits"][k]["mention"], n[key]) for k, key in (("flip", "FLIP"), ("near", "NEAR"))]
    for label, m, line in lines:
        c = next(x for x in rule.criteria if x.concept == m["concept"])
        if c is crit and not names(line, s["keywords"], crit.concept):
            errs.append(f"{label}: does not name {s['concept']} (use one of {shown(s['keywords'], crit.concept)})")
        if m["kind"] == "numeric":
            v, u = E.fmt(m["value"], c), unit(c.concept)
            if not re.search(r"(?<![\d.])" + re.escape(v) + r"(?![\d.])", line):
                errs.append(f"{label}: the value {v} is not in the line")
            if u and u in UNIT_RE and not re.search("(?i)" + UNIT_RE[u], line):
                errs.append(f"{label}: the unit {u} is not in the line")
        if m.get("year") and str(m["year"]) not in line:
            errs.append(f"{label}: the year {m['year']} is not in the line")
        if m["subject"] != "patient":
            if not re.search(r"(?i)(?<![\w-])" + re.escape(m["subject"]) + r"(?!-in-law)(?![\w-])", line):
                errs.append(f"{label}: the person '{m['subject']}' is not named")
        elif PERSON_RE.search(line):
            errs.append(f"{label}: names another person, but the fact is about the patient")
        if m["kind"] == "finding" and m["status"] == "absent" and not DENIAL.search(line):
            errs.append(f"{label}: should be a clear denial")
        if m["kind"] == "finding" and m["status"] == "present" and m["time"] == "current" and DENIAL.search(line):
            errs.append(f"{label}: reads as a denial, but the fact is present now")
        if m["status"] == "present" and m["time"] == "past" and not m.get("year") and not PAST.search(line):
            errs.append(f"{label}: does not read as past or earlier")
    if n.get("check_ok", "").lower() not in ("yes", "y", "ok"):
        errs.append("no second-author approval (check_ok: yes)")
    return errs


def assemble_texts(s, n):
    base = [n["header"], n["reason"]] + [n[f"fact {f['n']}"] for f in s["facts"]] + n["extra"]
    out = {"base": "\n".join(base)}
    for k, key in (("flip", "FLIP"), ("near", "NEAR")):
        e, ls = s["edits"][k], list(base)
        if e["op"] == "replace":
            ls[1 + e["fact"]] = n[key]
        else:
            ls.insert(random.Random(s["gid"]).randint(2, len(ls)), n[key])
        out[k] = "\n".join(ls)
    return out


def records(s, n, author):
    rule = D.RULES_BY_ID[s["rid"]]
    crit = rule.crit(s["cid"])
    thr, ov = crit.threshold, {}
    texts = assemble_texts(s, n)
    out = []
    for k, text in texts.items():
        st = E.state_from_json(s["states"][k])
        labels = E.case_labels(rule, crit, ov, st)
        ledger = E.ledger(crit, thr, [(_line_of(s, n, k, m), m) for m in st
                                      if m.concept == crit.concept and m.form != "generic"])   # no author line
        assert all(e["found"] == "not mentioned" or e["found"] in text for e in ledger), (s["gid"], k)
        common = dict(tid=f"{SET}.test.{s['gid']}", set=SET, split="test", tier="author", level="L2", rid=rule.rid,
                      cid=crit.cid, family=rule.family, nm_kind=s["nm_kind"], case_kind=k, rule_text=s["rule_text"],
                      case_text=text, condition=E.condition_text(crit, thr),
                      state=s["states"][k], ledger=ledger, prose=E.ledger_to_prose(ledger),
                      meta={"author": author, "checker": s["checker"], "check_comment": n.get("check_comment", ""),
                            "spec_tid": s["tid"], "tpl": [], "tpl_split": "author", "seed": int(s["gid"][1:]),
                            "overrides": ov, "keywords": s["keywords"],
                            "criterion_holds": int(crit.evaluate(st, None))})
        for ctype, (a, b) in E.claim_pairs(rule, crit, thr).items():
            for role, t in (("s", a), ("s_prime", b)):
                r = dict(common, iid=f"{common['tid']}/{k}/{ctype}/{role}", claim_type=ctype, claim_role=role,
                         claim_text=t, label=int((role == "s_prime") == (labels[ctype] == 1)))
                validate(r)
                out.append(r)
    return out


def _line_of(s, n, k, m):
    """The author's line that states mention m in case k."""
    for f in s["facts"]:
        if f["mention"] == {**m.__dict__}:
            line = n[f"fact {f['n']}"]
            for kk, key in (("flip", "FLIP"), ("near", "NEAR")):
                e = s["edits"][kk]
                if k == kk and e["op"] == "replace" and e["fact"] == f["n"]:
                    return n[key]
            return line
    return n["FLIP" if k == "flip" else "NEAR"]


def assemble(freeze=False, kit_dir=KIT):
    S = {json.loads(l)["gid"]: json.loads(l) for l in open(kit_dir / "specs.jsonl", encoding="utf-8")}
    report, recs, done = ["# challenge_v1 assembly report\n"], [], Counter()
    for md in sorted(kit_dir.glob("notes_*.md")):
        who = md.stem[len("notes_"):]
        notes = parse(md.read_text(encoding="utf-8"))
        with open(md.with_suffix(".jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for gid, n in sorted(notes.items()):
                f.write(json.dumps(dict(gid=gid, author=who, **n), sort_keys=True) + "\n")
        for gid, n in sorted(notes.items()):
            if gid not in S:
                report.append(f"- {who} {gid}: unknown group id")
                continue
            errs = check(S[gid], n)
            if errs:
                report.append(f"- {who} {gid}: " + "; ".join(errs))
                done["rejected"] += 1
            else:
                recs += records(S[gid], n, who)
                done["accepted"] += 1
    missing = sorted(set(S) - {r["tid"].split(".")[-1] for r in recs})
    report.append(f"\naccepted {done['accepted']}, rejected {done['rejected']}, not yet written or accepted {len(missing)}")
    (kit_dir / "ASSEMBLY_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(report[-1].strip())
    if freeze:
        if missing:
            sys.exit(f"refusing to freeze: {len(missing)} groups missing")
        _register(recs)
    return recs, report


def _register(recs):
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    name = f"{SET}/test"
    if registry.get(name, {}).get("frozen"):
        sys.exit(f"refusing to rebuild: {name} is frozen")
    d = ROOT / "data" / SET / "test"
    d.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(r, sort_keys=True) + "\n" for r in recs]
    (d / "records.jsonl").write_text("".join(lines), encoding="utf-8", newline="\n")
    sha = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()
    created = datetime.date.today().isoformat()
    man = {"name": "test", "set": SET, "split": "test", "level": "L2", "tier": "author", "created": created,
           "generator": "scripts/challenge_v1.py assemble", "frozen": True, "n_groups": len({r["tid"] for r in recs}),
           "n_records": len(recs), "sha256": sha, "git_commit": D.git_commit(),
           "by_kind": dict(Counter(r["nm_kind"] for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s"
                                   and r["claim_type"] == "conclusion")),
           "by_author": dict(Counter(r["meta"]["author"] for r in recs if r["case_kind"] == "base"
                                     and r["claim_role"] == "s" and r["claim_type"] == "conclusion")),
           "shortcut_validation": D.validate_shortcuts(d / "records.jsonl")}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    registry[name] = {"path": f"{SET}/test/records.jsonl", "split": "test", "level": "L2", "tier": "author",
                      "n_groups": man["n_groups"], "n_records": len(recs), "manifest": f"{SET}/test/MANIFEST.json",
                      "frozen": True, "created": created, "sha256": sha}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(f"{name} frozen: {man['n_groups']} groups, sha256 {sha[:16]}, shortcuts {man['shortcut_validation']['result']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("kit", "assemble"))
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    kit() if a.cmd == "kit" else assemble(a.freeze)
