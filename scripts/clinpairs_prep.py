"""Clinical training pairs for B (C-CL-clinpairs) and the MedEinst disease-held-out split (v13 App. External tiers).
  python scripts/clinpairs_prep.py [--out data] [--medqa-run results_git/C-CP-medqa-train-reader]
1. clin_v1/clinpairs_medeinst: MedEinst reference pairs (clin_v1/medeinst_ref_train, never test) with ledger
   targets: for each case, one entry per narrative line that the other case of the pair lacks (line diff after
   whitespace normalisation): need = the condition (the two candidate diagnoses), found = that line. The release
   has no structured evidence for trap cases, so the diff is the only source. subject, status and time are not
   supervised here (v13): they are set to 'unknown' and meta.supervised_fields = [need, found]; prose targets
   state only the quoted lines. Pairs where either case has no line of its own are skipped (counted).
2. clin_v1/clinpairs_medqa: MedQA-train key pairs whose ledgers were generated once (greedy) by the frozen
   rule-trained reader (B-F-ledger2-triplets-s0, run C-CP-medqa-train-reader) and kept if every quote occurs in
   the case (well-formed) and the frozen judge prefers the keyed answer on both questions (all four cells).
   The kept set is fixed and shared by every ledger format; prose rendered from the kept ledgers.
3. Disease-held-out split: 12 of the 46 diagnoses that occur, random.Random(SEED).sample(sorted names, 12):
   clin_v1/medeinst_dis_test = test pairs whose two diagnoses are both held out; clin_v1/clinpairs_medeinst_dis
   = training pairs (as 1) whose two diagnoses are both training diseases.
clin_v1/clinpairs_train = clinpairs_medeinst + clinpairs_medqa (all records)."""
import argparse, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED, N_HELD = 20261003, 12


def load_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def lines(text):
    return [l.strip() for l in text.split("\n") if l.strip() and set(l.strip()) != {"-"}]


def prose(entries):
    return " ".join(f"For {e['need']}, the note states \"{e['found']}\"." for e in entries)


def medeinst_pairs(recs):
    by = {}
    for r in recs:
        by.setdefault(r["tid"], []).append(r)
    out, skipped = [], 0
    for tid, rs in by.items():
        case = {k: next(r["case_text"] for r in rs if r["case_kind"] == k) for k in ("base", "flip")}
        own = {k: [l for l in lines(case[k]) if l not in set(lines(case["flip" if k == "base" else "base"]))]
               for k in ("base", "flip")}
        if not own["base"] or not own["flip"]:
            skipped += 1
            continue
        for r in rs:
            ent = [{"need": r["condition"], "found": l, "subject": "unknown", "status": "unknown", "time": "unknown"}
                   for l in own[r["case_kind"]]]
            out.append(r | {"ledger": ent, "prose": prose(ent),
                            "meta": r["meta"] | {"supervised_fields": ["need", "found"], "ledger_source": "line diff"}})
    return out, skipped


def medqa_pairs(recs, run_dir):
    sc = {r["iid"]: r for r in load_jsonl(f"{run_dir}/scores_clin_v1~keypairs_medqa_train.jsonl")}
    by = {}
    for r in recs:
        by.setdefault(r["tid"], []).append(r)
    out, kept, total = [], 0, 0
    for tid, rs in by.items():
        total += 1
        u = {(r["case_kind"], r["claim_role"]): sc[r["iid"]]["u"] for r in rs}
        ok = u[("base", "s")] > u[("base", "s_prime")] and u[("flip", "s_prime")] > u[("flip", "s")] \
            and all(v > -20 for v in u.values())                       # -20: malformed ledger
        if not ok:
            continue
        kept += 1
        for r in rs:
            text = sc[r["iid"]]["reader_output"].strip()
            ent = [dict(line.split(": ", 1) for line in block.split("\n")) for block in text.split("\n\n")]
            out.append(r | {"ledger": ent, "prose": prose(ent),
                            "meta": r["meta"] | {"ledger_source": "frozen reader B-F-ledger2-triplets-s0 (greedy), "
                                                                  "kept: well formed and keyed verdict on all four cells"}})
    return out, kept, total


def write(out, name, recs, man, reg):
    d = f"{out}/clin_v1/{name}"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    sha = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
    split = recs[0]["split"] if recs else "train"
    man |= {"name": f"clin_v1/{name}", "n_records": len(recs), "n_groups": len({r['tid'] for r in recs}),
            "sha256": sha, "created": time.strftime("%Y-%m-%d"), "frozen": True}
    json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
    reg[f"clin_v1/{name}"] = {"path": f"clin_v1/{name}/records.jsonl", "split": split, "level": "external",
                              "tier": "external", "n_groups": man["n_groups"], "n_records": len(recs),
                              "manifest": f"clin_v1/{name}/MANIFEST.json", "frozen": True, "created": man["created"],
                              "sha256": sha}
    print(name, man["n_groups"], "groups", len(recs), "records", sha[:12])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--medqa-run", default=f"{REPO}/results_git/C-CP-medqa-train-reader")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    common = {"git_commit": commit, "python": sys.version.split()[0], "builder": "scripts/clinpairs_prep.py"}
    reg = {}
    ref = load_jsonl(f"{a.out}/clin_v1/medeinst_ref_train/records.jsonl")
    me, skipped = medeinst_pairs(ref)
    for r in me:
        validate(r)
    write(a.out, "clinpairs_medeinst", me, common | {"source": "clin_v1/medeinst_ref_train", "skipped_no_own_line": skipped},
          reg)
    test = load_jsonl(f"{a.out}/clin_v1/medeinst_test/records.jsonl")
    dis = sorted({r["meta"][k] for r in ref + test for k in ("y_gt", "y_bias")})
    held = set(random.Random(SEED).sample(dis, N_HELD))
    rule = f"held-out diseases = random.Random({SEED}).sample({len(dis)} sorted diagnosis names, {N_HELD})"
    write(a.out, "medeinst_dis_test", [r for r in test if r["meta"]["y_gt"] in held and r["meta"]["y_bias"] in held],
          common | {"split_rule": rule, "held_out_diseases": sorted(held), "source": "clin_v1/medeinst_test"}, reg)
    write(a.out, "clinpairs_medeinst_dis", [r for r in me if r["meta"]["y_gt"] not in held and r["meta"]["y_bias"] not in held],
          common | {"split_rule": rule, "held_out_diseases": sorted(held), "source": "clinpairs_medeinst"}, reg)
    allrec = list(me)
    if os.path.exists(f"{a.medqa_run}/DONE"):
        mq, kept, total = medqa_pairs(load_jsonl(f"{a.out}/clin_v1/keypairs_medqa_train/records.jsonl"), a.medqa_run)
        for r in mq:
            validate(r)
        write(a.out, "clinpairs_medqa", mq, common | {"source": "clin_v1/keypairs_medqa_train", "reader_run": a.medqa_run,
                                                     "pairs_total": total, "pairs_kept": kept,
                                                     "kept_share": round(kept / max(1, total), 4)}, reg)
        allrec += mq
    else:
        print("MedQA-train reader run not DONE yet: clinpairs_medqa not built")
    write(a.out, "clinpairs_train", allrec, common | {"parts": ["clinpairs_medeinst"] +
                                                               (["clinpairs_medqa"] if len(allrec) > len(me) else [])}, reg)
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    old = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    json.dump(old | reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
