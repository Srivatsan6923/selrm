"""clin_v1/medeinst_neg (test) and clin_v1/medeinst_neg_train (reference pairs): MedEinst control cases plus one
line that explicitly denies the finding that distinguishes the trap (docs/AUX_PROTOCOL.md S2; NEXT_TASKS_C item 3).
  python scripts/medeinst_neg.py --bank negation_bank.py --bank-commit SHA [--out data] [--freeze]
--bank: role A's selrm/negation_bank.py (a copy at commit SHA): deny(finding, split, key) writes one explicit denial
of a named finding; test-split templates for the test pairs, train-split for the reference pairs (the splits share
no negation cue). Without --freeze the sets are written unfrozen and are not registered.
Finding: MedEinst has no structured findings, so the distinguishing finding is the trap narrative's single added
top-level line ('- ...' present in the trap, absent from the control); pairs with no such line or with more than
one are left out and counted, and so are findings that contain negation wording (denying them would assert their
opposite). The finding phrase is the line without its first-person or question frame (FRAMES). The denial
'- <deny(phrase)>' is inserted at the end of the control's section (Symptoms / Antecedents) that holds the line in
the trap. The control diagnosis stays correct by construction:
the finding was already absent from the control. Records: one case per pair (case_kind 'near'), claims
s = 'The most likely diagnosis is <y_gt>.' (label 1) and s_prime = '... <y_bias>.' (label 0); meta.source_tid
joins the MedEinst pair. Metric (hold): share of items with d = u(s) - u(s_prime) > 0; ties fail."""
import argparse, collections, hashlib, importlib.util, json, os, random, re, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20261004
# the finding as a noun phrase for A's templates ('Negative for {np}.'): the distinguishing line without its
# first-person or question frame; first matching rule wins (case-insensitive); A's deny() then drops a leading
# article and the final full stop
FRAMES = [(r"^do you have (.+?)\??$", r"\1"), (r"^have you (?:been|had) (.+?)\??$", r"\1"), (r"^have you (.+?)\??$", r"\1"),
          (r"^are you (.+?)\??$", r"\1"), (r"^do you (.+?)\??$", r"\1"), (r"^(?:is|does) (.+?)\??$", r"\1"),
          (r"^i(?: have|'ve) (?:noticed|had|been) (.+)$", r"\1"), (r"^i(?: have|'ve) (.+)$", r"\1"),
          (r"^i had (.+)$", r"\1"), (r"^i suffer from (.+)$", r"\1"), (r"^i feel (.+)$", r"feeling \1"),
          (r"^i(?: am|'m) (.+)$", r"\1"), (r"^my (.+)$", r"\1"), (r"^i (.+)$", r"\1")]


# negation wording of either split of A's bank, plus contracted negations: such findings are left out
NEGATED = re.compile(r"(?i)\b(?:not|no|never|without|absent|negative|free of|ruled out|denies|cannot)\b|n't\b")


def finding_np(line):
    """-> (noun phrase, rule index or -1). Mis-encoded apostrophes of the release ('I�ve') read as "'"."""
    s = line.strip().replace("�", "'")
    for k, (pat, rep) in enumerate(FRAMES):
        if re.match(pat, s, flags=re.I):
            return re.sub(pat, rep, s, flags=re.I).strip(), k
    return s, -1
SOURCES = {"medeinst_neg": ("clin_v1/medeinst_test", "test"), "medeinst_neg_train": ("clin_v1/clinpairs_medeinst", "train")}


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def section_header(lines, i):
    """The nearest header line above line i ('Symptoms:', 'Antecedents:'), or None."""
    for j in range(i - 1, -1, -1):
        s = lines[j]
        if s.endswith(":") and not s.startswith((" ", "-", "*")):
            return s
    return None


def insert(control, header, new):
    """Control lines with `new` added as the last line of the section under `header` (end of text if absent)."""
    if header in control:
        i = control.index(header) + 1
        while i < len(control) and control[i].strip() and not (control[i].endswith(":") and not control[i].startswith((" ", "-", "*"))):
            i += 1
        while i > 0 and not control[i - 1].strip():
            i -= 1
        return control[:i] + [new] + control[i:]
    return control + [new]


def build(pairs, deny, split):
    out, skipped, rules = [], collections.Counter(), collections.Counter()
    for tid, p in sorted(pairs.items()):
        c, t = p["base"]["case_text"].split("\n"), p["flip"]["case_text"].split("\n")
        cs = set(c)
        added = [i for i, l in enumerate(t) if l.startswith("- ") and l not in cs]
        if len(added) != 1:
            skipped["no single added finding line" if not added else "more than one added finding line"] += 1
            continue
        x = t[added[0]][2:]
        if NEGATED.search(x.replace("�", "'")):   # denying a negative finding would assert its opposite
            skipped["finding contains negation wording"] += 1
            continue
        np_, k = finding_np(x)
        rules[k] += 1
        line = "- " + deny(np_, split, key=f"{split}|{tid}")
        case = "\n".join(insert(c, section_header(t, added[0]), line))
        y_gt, y_bias = p["base"]["meta"]["y_gt"], p["base"]["meta"]["y_bias"]
        ntid = f"medeinstneg_{split}_{tid}"
        for role, y, lab in (("s", y_gt, 1), ("s_prime", y_bias, 0)):
            src = p[("base", role)]
            out.append(src | {"iid": f"{ntid}/near/conclusion/{role}", "tid": ntid, "split": split, "case_kind": "near",
                              "nm_kind": "negation", "case_text": case, "claim_text": f"The most likely diagnosis is {y}.",
                              "label": lab, "meta": src["meta"] | {"source_tid": tid, "denied_line": x, "finding_np": np_, "np_rule": k,
                                                                    "inserted": line, "y_gt": y_gt, "y_bias": y_bias,
                                                                    # a past-history line can name a diagnosis itself
                                                                    "diagnosis_named": any(y.lower() in line.lower()
                                                                                           for y in (y_gt, y_bias))}})
    return out, skipped, rules


def validation(recs, np_of):
    items = [r for r in recs if r["claim_role"] == "s"]
    named = sum(np_of(r["meta"]["finding_np"]).lower() in r["meta"]["inserted"].lower() and r["meta"]["inserted"] in r["case_text"]
                for r in items)
    leak = sum(any(y.lower() in r["meta"]["inserted"].lower() for y in (r["meta"]["y_gt"], r["meta"]["y_bias"])) for r in items)
    return {"items": len(items), "finding_named_in_case": named,
            "named_finding_prefers_trap_scorer_hold": 0.0 if named == len(items) else None,
            "note": "the denied finding is named in every case, and the control diagnosis is correct, so a scorer that "
                    "prefers the trap diagnosis whenever its finding is named holds on no item",
            "diagnosis_name_in_inserted_line": leak, "label1_share": 100.0 * sum(r["label"] for r in recs) / len(recs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True, help="role A's selrm/negation_bank.py (a copy at a pinned commit)")
    ap.add_argument("--bank-commit", required=True, help="role A's commit of that file")
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    spec = importlib.util.spec_from_file_location("negation_bank", a.bank)
    bank = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bank)
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    reg = json.load(open(regp, encoding="utf-8"))
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    for name, (src_set, split) in SOURCES.items():
        pairs = collections.defaultdict(dict)
        for r in load(f"{a.out}/{reg[src_set]['path']}"):
            pairs[r["tid"]][r["case_kind"]] = r
            pairs[r["tid"]][(r["case_kind"], r["claim_role"])] = r
        recs, skipped, rules = build(pairs, bank.deny, split)
        for r in recs:
            validate(r)
        d = f"{a.out}/clin_v1/{name}"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        sha = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
        man = {"name": f"clin_v1/{name}", "source_set": src_set, "source_sha256": reg[src_set]["sha256"],
               "bank": "role A selrm/negation_bank.py deny(finding, split, key)", "bank_commit": a.bank_commit,
               "bank_sha256": hashlib.sha256(open(a.bank, "rb").read()).hexdigest(), "templates_used": f"{split} split",
               "finding_rule": "distinguishing line without its first-person or question frame (FRAMES in this script)",
               "finding_rule_counts": {str(k): v for k, v in sorted(rules.items())},
               "pairs_in_source": len(pairs), "pairs_kept": len(recs) // 2, "pairs_left_out": dict(skipped),
               "shortcut_validation": validation(recs, bank._np), "metric": "hold = share of items with d > 0 (ties fail)",
               "n_records": len(recs), "n_groups": len(recs) // 2, "sha256": sha, "git_commit": commit,
               "python": sys.version.split()[0], "created": time.strftime("%Y-%m-%d"), "frozen": a.freeze}
        json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
        if a.freeze:
            reg[f"clin_v1/{name}"] = {"path": f"clin_v1/{name}/records.jsonl", "split": split, "level": "external",
                                      "tier": "external", "n_groups": len(recs) // 2, "n_records": len(recs),
                                      "manifest": f"clin_v1/{name}/MANIFEST.json", "frozen": True,
                                      "created": man["created"], "sha256": sha}
        print(name, len(recs) // 2, "pairs kept", dict(skipped), sha[:12], "frozen" if a.freeze else "PROVISIONAL")
    if a.freeze:
        json.dump(reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
