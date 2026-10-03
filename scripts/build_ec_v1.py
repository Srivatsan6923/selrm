"""ec_v1: registered eligibility criteria (FINAL_TASKS A P0.5).

  python scripts/build_ec_v1.py prepare   # ec_v1/formalized.json -> unsigned records, sign-off sheet, exclusions
  python scripts/build_ec_v1.py freeze    # keeps the criteria two reviewers approved in docs/ec_signoff/

Pipeline: scripts/ec_mine.py (ClinicalTrials.gov, TrialGPT trials and texts excluded) -> formalisation by
model agents with two adversarial verifiers (ec_v1/formalized.json; a criterion is kept only if both
confirm) -> this script (render, check, sheet) -> two authors sign off each program and its rendered
cases, each in their own file docs/ec_signoff/<authorN>.csv (H3) -> freeze. Nothing is scored before
the freeze.
"""
import csv
import datetime
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import ec  # noqa: E402
from selrm.metrics import decisions, summarise  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KIT, SHEET, REVIEWS = ROOT / "ec_v1", ROOT / "docs" / "EC_SIGNOFF.csv", ROOT / "docs" / "ec_signoff"
AUTHORS = ("author1", "author2", "author3", "author4")
COLS = ["crit_id", "nct_id", "criterion_type", "original_text", "rule_text_shown", "simplifications",
        "text_edits", "never_mentioned_disjuncts", "registry_context", "program", "executed_tests", "near_miss_kinds", "groups",
        "verification", "cases", "fingerprint"]
REVIEW_COLS = ["crit_id", "fingerprint", "program_ok", "cases_ok", "comment"]


# Accepted by the formalizer and rejected by the verifier(s) only for a near-miss kind (one verifier for the
# pregnancy rows, both for k005), each naming the kinds under which it accepts (quoted). Restricting the
# kinds cannot add an ambiguous case. The sign-off sheet marks these rows (column verification).
RESCUE = {
    "k005": (["numeric", "boundary"], "Re-submit with near_kinds ['numeric','boundary']."),
    "k216": (["subject", "negation"], "time near-miss ambiguous (a past delivery leaves 'breastfeeding' open); "
                                      "subject and negation confirmed by both verifiers"),
    "k218": (["subject", "negation"], "It would be acceptable with near_kinds = [subject, negation]."),
    "k219": (["subject", "negation"], "It would be acceptable with near_kinds = [subject, negation]."),
    "k220": (["subject", "negation"], "It would be acceptable with near_kinds = [subject, negation]."),
    "k221": (["subject", "negation"], "It would be acceptable with near_kinds = [subject, negation]."),
}
QUALIFIER = re.compile(r"(?i)history|presence|within|up to|before|after|prior|previous|since|during|such as|doubt")


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def post(items, ctx):
    """Rescues, registry context (section and nesting) and duplicates, in that order; every change is
    recorded on the item (rescued, exclusion_reason, simplifications, registry_parent)."""
    def drop(f, why):
        f["final"], f["exclusion_reason"] = "exclude", why
    for f in items:
        if f["cand"] in RESCUE and f["decision"] == "accept" and f["final"] != "accept":
            kinds, quote = RESCUE[f["cand"]]
            f.update(near_kinds=kinds, final="accept", rescued=f"near-miss kinds restricted to {kinds} as the "
                                                                f"rejecting verifier specified: {quote}")
        c = ctx.get(f["cand"])
        if f["final"] != "accept" or not c:
            continue
        parent = c.get("parent") or ""
        if c.get("not_found"):
            drop(f, "the line was not found in the live registry record")
        elif c.get("type_mismatch"):
            drop(f, f"the registry lists it under {c['section']}, not {c['mined_type']}")
        elif c.get("under_intro") and f["criterion_type"] == "inclusion":
            drop(f, f"one condition of a compound inclusion criterion ('{parent}'): necessary, not sufficient")
        elif c.get("under_intro") and QUALIFIER.search(parent):
            drop(f, f"the parent line ('{parent}') qualifies its items")
        elif c.get("under_intro"):
            f["registry_parent"] = parent
            f["simplifications"] = f["simplifications"] + [
                f"shown alone: one item of the compound exclusion criterion '{parent}', any item of which excludes"]
    seen = {}
    for f in sorted(items, key=lambda f: f["cand"]):
        if f["final"] != "accept":
            continue
        key = (norm(f["rule_text"]), f["criterion_type"], f["concept"], f["op"], f["threshold"], f["times"],
               f["subjects"], f["window_n"], f["window_unit"])
        if key in seen:
            drop(f, f"duplicate of {seen[key]} (same text and program, another trial or arm)")
        else:
            seen[key] = f["cand"]
    return items


def guard(f):
    """Reasons the code itself excludes an accepted formalisation."""
    p = f.get("population") or {}
    if p.get("max_age") is not None and p["max_age"] < 23:
        return f"the trial enrols children or young people (registered age up to {p['max_age']:g} years); adult " \
               f"cases would cover fewer than five years of age"
    if f["input"] == "numeric" and f["concept"] in ec.SOFT:
        slo, shi = ec.SOFT[f["concept"]]
        nd, t = ec.NUM[f["concept"]][1], f["threshold"]
        if not slo + nd <= t <= shi - nd:
            return f"the threshold {t:g} lies at or outside the plausible range {slo:g}-{shi:g}, so the cases on " \
                   f"one side would be implausible for a screening visit"
    if f["subjects"] == "family" and re.search(r"(?i)family history", f["rule_text"]):
        return "family history counts relatives only; the program's family scope also counts the patient"
    if f["times"] == "window" and f["concept"] not in ec.xr.EVENTS:
        return "window criterion on a concept without dated-event wording"
    if f["input"] == "numeric" and f["concept"] not in ec.NUM:
        return "measurement the generator cannot render"
    if not ec.kinds(f):
        return "no near-miss kind is unambiguous for this criterion"
    return None


def shortcut_check(recs):
    """always-default TA 0 and Hold 100; concept named TA 0; program TA 100 (decisions on conclusion claims)."""
    def named(r):
        hit = any(k in r["case_text"].lower() for k in r["meta"]["keywords"])
        return float((r["claim_role"] == "s_prime") == hit)
    fns = {"always_default": lambda r: float(r["claim_role"] == "s"), "concept_named": named,
           "program": lambda r: float(r["label"])}
    res = {k: summarise(decisions(recs, [f(r) for r in recs]), by=("nm_kind",))["all"] for k, f in fns.items()}
    ok = (res["always_default"]["TA"] == 0 and res["always_default"]["Hold"] == 100 and res["program"]["TA"] == 100
          and res["concept_named"]["TA"] == 0)
    return ok, {k: {m: v[m] for m in ("TA", "Rev", "Hold", "n")} for k, v in res.items()}


def render(items):
    keep, out, excl = [], [], []
    for f in items:
        if f["final"] != "accept":
            excl.append((f, f["exclusion_reason"] or "; ".join(v["reason"] for v in f["verdicts"] if v["verdict"] == "reject")
                         or "not confirmed by both verifiers"))
            continue
        why = guard(f)
        if why:
            excl.append((f, why))
            continue
        try:
            recs = ec.groups(f)
        except (RuntimeError, ValueError, KeyError, StopIteration) as e:
            excl.append((f, f"not renderable: {str(e)[:160]}"))
            continue
        bad = ec.rendered_ok(recs)
        if bad:
            excl.append((f, f"rendering check failed: {bad[0]}"))
            continue
        keep.append(f)
        out += recs
    return keep, out, excl


def records_sha(recs):
    return hashlib.sha256("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs).encode("utf-8")).hexdigest()


def fingerprint(f, recs):
    """What a reviewer signs: the rendered records, the rule text, the program and its never-mentioned
    disjuncts. Any change to one of them voids the sign-off."""
    parts = [records_sha(recs), ec.full_text(f), ec.program_text(f), ", ".join(f["other_disjuncts"])]
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()[:16]


def not_rendered(f):
    """Near-miss kinds the formalisation allows but the generator does not render, with the reason."""
    out = []
    for k in f["near_kinds"]:
        if k not in ec.kinds(f):
            why = "ages are in completed years, so a case at the threshold is arguable" if \
                k == "boundary" and f["concept"] == "age" else "a boundary case needs a strict threshold" if \
                k == "boundary" else "the generator cannot build it for this criterion"
            out.append(f"{k} ({why})")
    return out


def text_edits(original, shown):
    """Every word-level difference between the registered and the shown text (computed, so none is
    missed by the formaliser's own list)."""
    import difflib
    a, b = original.split(), shown.split()
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            out.append(f"'{' '.join(a[i1:i2])}' -> '{' '.join(b[j1:j2])}'")
    return "; ".join(out) or "none"


def verification(f):
    if f.get("rescued"):
        return "rescued: " + f["rescued"]
    return "confirmed by both model verifiers"


def sheet_row(f, recs):
    tests = "; ".join(f"{lab} -> {'met' if y else 'not met'}" for lab, y in ec.boundary_tests(f))
    if f["concept"] == "age" and f["op"] in ("<", ">"):
        tests += "; no case states the age at the threshold (ages are in completed years)"
    skipped = not_rendered(f)
    return {"crit_id": f["cand"], "nct_id": f["nct_id"], "criterion_type": f["criterion_type"],
            "original_text": f["original_text"], "rule_text_shown": ec.full_text(f),
            "simplifications": " | ".join(f["simplifications"]) or "none",
            "text_edits": text_edits(f["original_text"], f["rule_text"]),
            "never_mentioned_disjuncts": ", ".join(f["other_disjuncts"]) or "none",
            "registry_context": f.get("registry_parent") or "standalone item", "program": ec.program_text(f),
            "executed_tests": tests,
            "near_miss_kinds": ", ".join(ec.kinds(f)) + (f"; not rendered: {', '.join(skipped)}" if skipped else ""),
            "groups": len({r["tid"] for r in recs}), "verification": verification(f),
            "cases": f"ec_v1/SIGNOFF_CASES.md#{f['cand']}", "fingerprint": fingerprint(f, recs)}


def cases_md(keep, recs):
    """Every case of every group, by criterion: what the authors sign off as cases_ok."""
    out = ["# ec_v1: every rendered case, by criterion (H3)",
           "",
           "Answers are the program's: base, near-miss and presentation cases do not meet the criterion, the flip "
           "meets it. Sign off a criterion's cases only if every case below is unambiguous under its rule text."]
    for f in keep:
        rs = [r for r in recs if r["rid"] == f"ec_{f['cand']}" and r["claim_role"] == "s_prime"]
        out += ["", f'<a id="{f["cand"]}"></a>', f"## {f['cand']} ({f['nct_id']})", "", ec.full_text(f), "",
                f"Program: {ec.program_text(f)}"]
        for tid in sorted({r["tid"] for r in rs}):
            g = {r["case_kind"]: r for r in rs if r["tid"] == tid}
            out += ["", f"### near-miss kind: {g['base']['nm_kind']}"]
            for k in ("base", "flip", "near", "pres"):
                if k in g:
                    out += ["", f"**{k}** ({'meets' if g[k]['label'] else 'does not meet'})", "```",
                            g[k]["case_text"], "```"]
    return "\n".join(out) + "\n"


def load_items():
    """Agent formalisations (ec_v1/formalized.json) with the mined text, trial and type, after post()."""
    src = json.loads((KIT / "formalized.json").read_text(encoding="utf-8"))
    sel = {json.loads(l)["cand"]: json.loads(l) for l in open(KIT / "selected.jsonl", encoding="utf-8")}
    ctx = json.loads((KIT / "registry_context.json").read_text(encoding="utf-8"))
    pop = json.loads((KIT / "registry_population.json").read_text(encoding="utf-8"))
    items = [dict(f, original_text=sel[f["cand"]]["text"], nct_id=sel[f["cand"]]["nct_id"],
                  criterion_type=sel[f["cand"]]["type"], population=pop.get(sel[f["cand"]]["nct_id"]))
             for f in src["items"]]
    return post(items, ctx)


def reviewer_files():
    return [p for p in sorted(REVIEWS.glob("*.csv")) if p.stem != "TEMPLATE"]


def prepare(force=False):
    """Writes the sheet, every case and a blank review template. Refuses while reviewer files exist
    (unless force), so that the cases do not change under a sign-off in progress."""
    if reviewer_files() and not force:
        sys.exit(f"refusing to prepare: sign-off files exist in {REVIEWS.relative_to(ROOT)} "
                 f"({', '.join(p.name for p in reviewer_files())}); rerun with --force to regenerate the sheet, "
                 f"after which every changed fingerprint needs a new review")
    items = load_items()
    keep, recs, excl = render(items)
    ok, sc = shortcut_check(recs)
    REVIEWS.mkdir(parents=True, exist_ok=True)
    with open(SHEET, "w", encoding="utf-8", newline="") as fh, \
            open(REVIEWS / "TEMPLATE.csv", "w", encoding="utf-8", newline="") as th:
        w, t = csv.DictWriter(fh, fieldnames=COLS), csv.DictWriter(th, fieldnames=REVIEW_COLS)
        w.writeheader()
        t.writeheader()
        for f in keep:
            row = sheet_row(f, [r for r in recs if r["rid"] == f"ec_{f['cand']}"])
            w.writerow(row)
            t.writerow({"crit_id": row["crit_id"], "fingerprint": row["fingerprint"]})
    (KIT / "SIGNOFF_CASES.md").write_text(cases_md(keep, recs), encoding="utf-8")
    with open(KIT / "EXCLUSIONS.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["crit_id", "nct_id", "type", "original_text", "reason"])
        for f, why in excl:
            w.writerow([f["cand"], f["nct_id"], f["criterion_type"], f["original_text"], why])
    d = ROOT / "data" / "ec_v1" / "unsigned"
    d.mkdir(parents=True, exist_ok=True)
    (d / "records.jsonl").write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs), encoding="utf-8",
                                     newline="\n")
    summary = {"candidates": len(items), "accepted_by_agents": sum(f["decision"] == "accept" for f in items),
               "confirmed_by_both_verifiers": sum(bool(f["verdicts"]) and all(v["verdict"] == "confirm"
                                                                             for v in f["verdicts"])
                                                  and len(f["verdicts"]) == 2 for f in items),
               "rescued": sorted(f["cand"] for f in items if f.get("rescued")),
               "kept_as_exclusion_subitems": sorted(f["cand"] for f in items if f.get("registry_parent")
                                                    and f["final"] == "accept"),
               "kept": len(keep), "excluded": len(excl), "groups": len({r["tid"] for r in recs}),
               "records": len(recs), "by_concept": dict(Counter(f["concept"] for f in keep)),
               "by_type": dict(Counter(f["criterion_type"] for f in keep)),
               "by_times": dict(Counter(f["times"] for f in keep if f["input"] == "finding")),
               "by_kind": dict(Counter(r["nm_kind"] for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s")),
               "trials": len({f["nct_id"] for f in keep}), "shortcut_validation": {"result": "PASS" if ok else "FAIL",
                                                                                     "scorers": sc}}
    (KIT / "prepare_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))
    if not ok:
        sys.exit("shortcut validation FAILED")


def yes_no(v):
    return {"yes": "yes", "y": "yes", "no": "no", "n": "no"}.get((v or "").strip().lower())


def read_reviews():
    """{crit_id: [(reviewer, row)]} from docs/ec_signoff/<authorN>.csv, plus the problems found. A row
    with no decision and no comment is not a review (that reviewer left the criterion to others)."""
    out, bad = {}, []
    for p in reviewer_files():
        if p.stem not in AUTHORS:
            bad.append(f"{p.name}: rename it to <authorN>.csv (one of {', '.join(AUTHORS)})")
            continue
        try:
            rows = list(csv.DictReader(open(p, encoding="utf-8-sig", newline="")))
        except UnicodeDecodeError:
            bad.append(f"{p.name}: not UTF-8; save it as 'CSV UTF-8 (comma delimited)'")
            continue
        if rows and set(REVIEW_COLS) - set(rows[0]):
            bad.append(f"{p.name}: missing columns {sorted(set(REVIEW_COLS) - set(rows[0]))}")
            continue
        ids = Counter((r["crit_id"] or "").strip() for r in rows)
        bad += [f"{p.name}: {c} appears {n} times" for c, n in ids.items() if n > 1]
        for r in rows:
            if any((r[c] or "").strip() for c in ("program_ok", "cases_ok", "comment")):
                out.setdefault(r["crit_id"].strip(), []).append((p.stem, r))
    return out, bad


def freeze():
    """Keeps the criteria that two reviewers approved (program_ok and cases_ok yes from both). Refuses
    unless every presented criterion has exactly two reviews, each of the current fingerprint, with
    program_ok yes or no, cases_ok yes or no (blank allowed after program_ok no) and a comment for every
    no. Criteria not approved are listed in the manifest as rejected at sign-off."""
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    if registry.get("ec_v1/test", {}).get("frozen"):
        sys.exit("refusing to rebuild: ec_v1/test is frozen")
    keep_all, recs_all, _ = render(load_items())
    fps = {f["cand"]: fingerprint(f, [r for r in recs_all if r["rid"] == f"ec_{f['cand']}"]) for f in keep_all}
    reviews, bad = read_reviews()
    bad += [f"{c}: not a criterion on the sheet" for c in reviews if c not in fps]
    for c, fp in fps.items():
        rs = reviews.get(c, [])
        if len(rs) != 2:
            bad.append(f"{c}: {len(rs)} review(s) ({', '.join(w for w, _ in rs) or 'none'}); exactly two are needed")
            continue
        for who, r in rs:
            p, k = yes_no(r["program_ok"]), yes_no(r["cases_ok"])
            if (r["fingerprint"] or "").strip() != fp:
                bad.append(f"{c} ({who}): signed another version (fingerprint {r['fingerprint']!r}, now {fp}); "
                           f"review it again")
            if p is None or (k is None and not (p == "no" and not (r["cases_ok"] or "").strip())):
                bad.append(f"{c} ({who}): program_ok must be yes or no, cases_ok yes or no (blank only after "
                           f"program_ok no)")
            if "no" in (p, k) and not (r["comment"] or "").strip():
                bad.append(f"{c} ({who}): a no needs a comment")
    if bad:
        sys.exit("refusing to freeze:\n" + "\n".join(bad))
    approved = {c for c in fps if all(yes_no(r["program_ok"]) == yes_no(r["cases_ok"]) == "yes"
                                      for _, r in reviews[c])}
    if not approved:
        sys.exit("no criterion approved; nothing to freeze")
    keep = [f for f in keep_all if f["cand"] in approved]
    recs = [r for r in recs_all if r["rid"] in {f"ec_{c}" for c in approved}]
    with open(REVIEWS / "MERGED.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["crit_id", "fingerprint", "approved"] + [f"{x}_{i}" for i in (1, 2)
                                                             for x in ("reviewer", "program_ok", "cases_ok", "comment")])
        for c in fps:
            w.writerow([c, fps[c], "yes" if c in approved else "no"]
                       + [v for who, r in reviews[c] for v in (who, r["program_ok"], r["cases_ok"], r["comment"])])
    ok, sc = shortcut_check(recs)
    if not ok:
        sys.exit("shortcut validation FAILED")
    d = ROOT / "data" / "ec_v1" / "test"
    d.mkdir(parents=True, exist_ok=True)
    lines = "".join(json.dumps(r, sort_keys=True) + "\n" for r in recs)
    (d / "records.jsonl").write_text(lines, encoding="utf-8", newline="\n")
    sha = hashlib.sha256(lines.encode("utf-8")).hexdigest()
    created = datetime.date.today().isoformat()
    man = {"name": "test", "set": "ec_v1", "split": "test", "level": "registered", "created": created, "frozen": True,
           "generator": "scripts/build_ec_v1.py (selrm/ec.py)", "criteria": len(keep),
           "trials": len({f["nct_id"] for f in keep}), "n_groups": len({r["tid"] for r in recs}), "n_records": len(recs),
           "sha256": sha, "git_commit": D.git_commit(), "signed_off": sorted(f["cand"] for f in keep),
           "rejected_at_signoff": sorted(set(fps) - approved),
           "reviewers": {c: sorted(w for w, _ in reviews[c]) for c in sorted(fps)},
           "shortcut_validation": {"result": "PASS", "scorers": sc}}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    registry["ec_v1/test"] = {"path": "ec_v1/test/records.jsonl", "split": "test", "level": "registered",
                              "tier": "easy", "n_groups": man["n_groups"], "n_records": len(recs),
                              "manifest": "ec_v1/test/MANIFEST.json", "frozen": True, "created": created, "sha256": sha}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(f"ec_v1/test frozen: {len(keep)} criteria, {man['n_groups']} groups, sha256 {sha[:16]}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in ("prepare", "freeze"):
        sys.exit("usage: python scripts/build_ec_v1.py prepare [--force] | freeze")
    prepare("--force" in sys.argv) if cmd == "prepare" else freeze()
