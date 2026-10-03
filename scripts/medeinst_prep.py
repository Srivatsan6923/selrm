"""clin_v1/medeinst_{test,ref_dev,ref_train}: MedEinst pairs as canonical records (C-CL-medeinst).
  python scripts/medeinst_prep.py [--out data]
Source: zhui711/MedEinst (Hugging Face, pinned revision, CC BY 4.0; derived from DDXPlus, CC BY 4.0).
A pair = control case (ground truth y_gt) and trap case (ground truth y_bias), same case_id.
Records: one block per pair: base = control, flip = trap; claims s = "The most likely diagnosis is
<y_gt>." (correct on the control), s_prime = the same with <y_bias> (correct on the trap); rule_text ""
(no rule is stated); condition (shown to readers) = "the most likely diagnosis: <y_gt> or <y_bias>"
(the set of candidate answers, v13 Sec. 5). Narratives are whitespace-normalised (trailing spaces
removed per line): the release marks most trap narratives, and no control, with Markdown trailing
double spaces, a label leak. Flags in meta: no_content_diff (control and trap identical after
normalisation; unsolvable) and overlap_ref (a narrative of the pair occurs verbatim in the reference
file). Reference pairs (train.jsonl) that share a narrative with any test pair are dropped; the rest
are split, random.Random(SEED), into ref_dev (DEV_N pairs: development choices) and ref_train (C's
clinical training pairs for B are built from it, never from test)."""
import argparse, collections, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = "zhui711/MedEinst"
REVISION = "354f4b527e764a8f2bebea8f71be55e0a6966402"
SHA = {"test.jsonl": "b6b688fa41f788c17cdbf5076b5215782c9eb00efec1a3d3384c002836550a57",
       "train.jsonl": "f3e8a72d321d9dff7b9d0fda5bf28bb5ecdf5705bfa0ba088acabb9ea1712de8"}
SEED, DEV_N = 20261003, 500


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def norm(text):
    return "\n".join(line.rstrip() for line in text.replace("\r", "").split("\n")).strip()


def load(cache, name):
    from huggingface_hub import hf_hub_download
    p = hf_hub_download(DATASET, name, repo_type="dataset", revision=REVISION, local_dir=cache)
    if sha256(p) != SHA[name]:
        sys.exit(f"{name}: sha256 differs from the pinned release")
    rows = [json.loads(l) for l in open(p, encoding="utf-8")]
    pairs = collections.defaultdict(dict)
    for r in rows:
        pairs[r["case_id"]][r["case_type"]] = r
    bad = [k for k, v in pairs.items() if set(v) != {"control", "trap"}]
    if bad:
        sys.exit(f"{name}: {len(bad)} case_ids without exactly one control and one trap")
    return pairs, p


def claim(dx):
    return f"The most likely diagnosis is {dx}."


def records_of(cid, pair, split, flags):
    c, t = pair["control"], pair["trap"]
    ygt, ybias = c["ground_truth"], t["ground_truth"]
    tid = f"medeinst_{split}_{cid}"
    base = {"tid": tid, "set": "clin_v1", "split": split, "tier": "external", "level": "external",
            "rid": f"{ygt} -> {ybias}", "cid": cid, "family": ygt, "nm_kind": "none", "rule_text": "",
            "condition": f"the most likely diagnosis: {ygt} or {ybias}", "claim_type": "conclusion",
            "state": [], "ledger": [], "prose": "",
            "meta": {"source": f"{DATASET}@{REVISION[:7]}", "case_id": cid, "y_gt": ygt, "y_bias": ybias,
                     "age": c["age"], "sex": c["sex"]} | flags}
    out = []
    for kind, row in (("base", c), ("flip", t)):
        for role, dx in (("s", ygt), ("s_prime", ybias)):
            label = int((kind == "base") == (role == "s"))
            out.append(base | {"iid": f"{tid}/{kind}/conclusion/{role}", "case_kind": kind,
                               "case_text": norm(row["narrative"]), "claim_role": role, "claim_text": claim(dx),
                               "label": label, "meta": base["meta"] | {"case_type": row["case_type"]}})
    return out


def write(out, name, recs, man):
    d = f"{out}/clin_v1/{name}"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    man |= {"name": f"clin_v1/{name}", "n_records": len(recs), "n_pairs": len(recs) // 4,
            "sha256": sha256(f"{d}/records.jsonl"), "created": time.strftime("%Y-%m-%d"), "frozen": True}
    json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(name, man["n_pairs"], "pairs", man["sha256"][:12])
    return {"path": f"clin_v1/{name}/records.jsonl", "split": man["split"], "level": "external", "tier": "external",
            "n_groups": man["n_pairs"], "n_records": len(recs), "manifest": f"clin_v1/{name}/MANIFEST.json",
            "frozen": True, "created": man["created"], "sha256": man["sha256"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--cache", default=f"{REPO}/data/clin_v1/medeinst_raw")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    test, ptest = load(a.cache, "test.jsonl")
    ref, pref = load(a.cache, "train.jsonl")
    ref_texts = {norm(r["narrative"]) for p in ref.values() for r in p.values()}
    test_texts = {norm(r["narrative"]) for p in test.values() for r in p.values()}
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    common = {"source": DATASET, "revision": REVISION, "licence": "CC BY 4.0 (MedEinst; DDXPlus CC BY 4.0)",
              "git_commit": commit, "python": sys.version.split()[0],
              "claims": "s = 'The most likely diagnosis is <y_gt>.', s_prime = same with <y_bias>; base = control, flip = trap",
              "normalisation": "trailing whitespace removed per line (Markdown double-space leak on trap narratives)"}
    recs, flags = [], collections.Counter()
    for cid in sorted(test, key=lambda k: int(k.split("_")[-1])):
        p = test[cid]
        f = {"no_content_diff": norm(p["control"]["narrative"]) == norm(p["trap"]["narrative"]),
             "overlap_ref": any(norm(r["narrative"]) in ref_texts for r in p.values())}
        flags.update(k for k, v in f.items() if v)
        recs += records_of(cid, p, "test", f)
    for r in recs:
        validate(r)
    reg = {"clin_v1/medeinst_test": write(a.out, "medeinst_test", recs, common | {
        "split": "test", "source_file": "test.jsonl", "source_sha256": SHA["test.jsonl"], "flags": dict(flags),
        "labels": len({r["meta"]["y_gt"] for r in recs} | {r["meta"]["y_bias"] for r in recs})})}
    keep = sorted((k for k, p in ref.items() if not any(norm(r["narrative"]) in test_texts for r in p.values())),
                  key=lambda k: int(k.split("_")[-1]))
    dev = set(random.Random(SEED).sample(keep, DEV_N))
    for name, ids in (("medeinst_ref_dev", [k for k in keep if k in dev]), ("medeinst_ref_train", [k for k in keep if k not in dev])):
        rr = []
        for cid in ids:
            p = ref[cid]
            rr += records_of(cid, p, "dev" if name.endswith("dev") else "train",
                             {"no_content_diff": norm(p["control"]["narrative"]) == norm(p["trap"]["narrative"])})
        reg[f"clin_v1/{name}"] = write(a.out, name, rr, common | {
            "split": "dev" if name.endswith("dev") else "train", "source_file": "train.jsonl",
            "source_sha256": SHA["train.jsonl"], "ref_pairs_released": len(ref),
            "ref_pairs_dropped_overlap_test": len(ref) - len(keep),
            "split_rule": f"random.Random({SEED}).sample(kept reference pairs, {DEV_N}) -> ref_dev; rest -> ref_train"})
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    old = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    json.dump(old | reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
