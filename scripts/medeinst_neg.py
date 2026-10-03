"""clin_v1/medeinst_neg (test) and clin_v1/medeinst_neg_train (reference pairs): MedEinst control cases plus one
line that explicitly denies the finding that distinguishes the trap (docs/AUX_PROTOCOL.md S2; NEXT_TASKS_C item 3).
  python scripts/medeinst_neg.py --bank BANK.json [--out data] [--freeze]
BANK: {"train": [templates], "test": [templates], "source": ...}; each template has one slot {x} that takes the
finding line verbatim (role A's negation phrase bank; train-split phrases for the reference pairs, test-split
phrases for the test pairs). Without --freeze the sets are written unfrozen and are not registered (provisional
bank: nothing may be scored on them).
Finding: MedEinst has no structured findings, so the distinguishing finding is the trap narrative's single added
top-level line ('- ...' present in the trap, absent from the control); pairs with no such line or with more than
one are left out and counted. The denial '- <template with x>' is inserted at the end of the control's section
(Symptoms / Antecedents) that holds the line in the trap. The control diagnosis stays correct by construction:
the finding was already absent from the control. Records: one case per pair (case_kind 'near'), claims
s = 'The most likely diagnosis is <y_gt>.' (label 1) and s_prime = '... <y_bias>.' (label 0); meta.source_tid
joins the MedEinst pair. Metric (hold): share of items with d = u(s) - u(s_prime) > 0; ties fail."""
import argparse, collections, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20261004
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


def build(pairs, templates, split):
    out, skipped = [], collections.Counter()
    for tid, p in sorted(pairs.items()):
        c, t = p["base"]["case_text"].split("\n"), p["flip"]["case_text"].split("\n")
        cs = set(c)
        added = [i for i, l in enumerate(t) if l.startswith("- ") and l not in cs]
        if len(added) != 1:
            skipped["no single added finding line" if not added else "more than one added finding line"] += 1
            continue
        x = t[added[0]][2:]
        k = random.Random(f"{SEED}|{tid}").randrange(len(templates))
        line = "- " + templates[k].format(x=x)
        case = "\n".join(insert(c, section_header(t, added[0]), line))
        y_gt, y_bias = p["base"]["meta"]["y_gt"], p["base"]["meta"]["y_bias"]
        ntid = f"medeinstneg_{split}_{tid}"
        for role, y, lab in (("s", y_gt, 1), ("s_prime", y_bias, 0)):
            src = p[("base", role)]
            out.append(src | {"iid": f"{ntid}/near/conclusion/{role}", "tid": ntid, "split": split, "case_kind": "near",
                              "nm_kind": "negation", "case_text": case, "claim_text": f"The most likely diagnosis is {y}.",
                              "label": lab, "meta": src["meta"] | {"source_tid": tid, "denied_line": x, "template": k,
                                                                    "inserted": line, "y_gt": y_gt, "y_bias": y_bias,
                                                                    # a past-history line can name a diagnosis itself
                                                                    "diagnosis_named": any(y.lower() in line.lower()
                                                                                           for y in (y_gt, y_bias))}})
    return out, skipped


def validation(recs):
    items = [r for r in recs if r["claim_role"] == "s"]
    named = sum(r["meta"]["denied_line"] in r["case_text"] for r in items)
    leak = sum(any(y.lower() in r["meta"]["inserted"].lower() for y in (r["meta"]["y_gt"], r["meta"]["y_bias"])) for r in items)
    return {"items": len(items), "finding_named_in_case": named,
            "named_finding_prefers_trap_scorer_hold": 0.0 if named == len(items) else None,
            "note": "the denied finding is named in every case, and the control diagnosis is correct, so a scorer that "
                    "prefers the trap diagnosis whenever its finding is named holds on no item",
            "diagnosis_name_in_inserted_line": leak, "label1_share": 100.0 * sum(r["label"] for r in recs) / len(recs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True)
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    bank = json.load(open(a.bank, encoding="utf-8"))
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    reg = json.load(open(regp, encoding="utf-8"))
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    for name, (src_set, split) in SOURCES.items():
        pairs = collections.defaultdict(dict)
        for r in load(f"{a.out}/{reg[src_set]['path']}"):
            pairs[r["tid"]][r["case_kind"]] = r
            pairs[r["tid"]][(r["case_kind"], r["claim_role"])] = r
        recs, skipped = build(pairs, bank[split], split)
        for r in recs:
            validate(r)
        d = f"{a.out}/clin_v1/{name}"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        sha = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
        man = {"name": f"clin_v1/{name}", "source_set": src_set, "source_sha256": reg[src_set]["sha256"],
               "bank": os.path.relpath(a.bank, REPO).replace(os.sep, "/"), "bank_source": bank.get("source"),
               "bank_sha256": hashlib.sha256(open(a.bank, "rb").read()).hexdigest(), "templates_used": f"{split} split",
               "pairs_in_source": len(pairs), "pairs_kept": len(recs) // 2, "pairs_left_out": dict(skipped),
               "shortcut_validation": validation(recs), "metric": "hold = share of items with d > 0 (ties fail)",
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
