"""In-domain sets for the auxiliary-supervision analysis (docs/AUX_PROTOCOL.md S1; NEXT_TASKS_C item 2). No GPU.
  python scripts/aux_sets.py [--out data]
- clin_v1/trialgpt_cv: the TrialGPT test portion (43 patients, 801 items) with a patient fold 0-4 in meta.fold
  (patients sorted, random.Random(SEED).shuffle, fold = position mod 5); the 10 development patients
  (clin_v1/trialgpt_dev) stay out and serve as the development split. New tids/iids (prefix trialgptcv_), split 'cv'.
  Labels as in the zero-shot set: met (s 1, s' 0), not met (0, 1), NEI and N/A (0, 0).
- clin_v1/medeinst_train: registry alias of clin_v1/clinpairs_medeinst (the 7,807 MedEinst reference pairs as
  canonical records; base = control, flip = trap; claims 'The most likely diagnosis is <y>.'); same file and sha256."""
import argparse, collections, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED, K = 20261004, 5


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.metrics import prf
    from selrm.schema import validate
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    reg = json.load(open(regp, encoding="utf-8"))

    # TrialGPT folds by patient
    src = load(f"{a.out}/clin_v1/trialgpt_test/records.jsonl")
    dev_patients = {r["meta"]["patient_id"] for r in load(f"{a.out}/clin_v1/trialgpt_dev/records.jsonl")}
    patients = sorted({r["meta"]["patient_id"] for r in src}, key=str)
    assert not set(patients) & dev_patients
    order = list(patients)
    random.Random(SEED).shuffle(order)
    fold = {p: i % K for i, p in enumerate(order)}
    recs = []
    for r in src:
        tid = r["tid"].replace("trialgpt_", "trialgptcv_", 1)
        recs.append(r | {"tid": tid, "iid": r["iid"].replace(r["tid"], tid, 1), "split": "cv",
                         "meta": r["meta"] | {"fold": fold[r["meta"]["patient_id"]], "source_tid": r["tid"]}})
    for r in recs:
        validate(r)
    d = f"{a.out}/clin_v1/trialgpt_cv"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    sha = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
    items = [r for r in recs if r["claim_role"] == "s"]
    by_fold = {k: {"patients": sum(v == k for v in fold.values()), "items": sum(r["meta"]["fold"] == k for r in items),
                   "categories": dict(collections.Counter(r["meta"]["category"] for r in items if r["meta"]["fold"] == k))}
               for k in range(K)}
    # case-blind predictors per held-out fold: the type prior from the other folds (shortcut validation)
    sv = {}
    for k in range(K):
        tr = [r for r in items if r["meta"]["fold"] != k and r["meta"]["category"] != "na"]
        te = [r for r in items if r["meta"]["fold"] == k and r["meta"]["category"] != "na"]
        prior = {t: collections.Counter(r["meta"]["category"] for r in tr if r["family"] == t).most_common(1)[0][0]
                 for t in ("inclusion", "exclusion")}
        m = prf([r["meta"]["category"] for r in te], [prior[r["family"]] for r in te], ("met", "not_met", "nei"))
        sv[f"fold {k}"] = {"type_prior": prior, "macroF1": m["macroF1"], "acc": m["acc"], "n": len(te)}
    old = json.load(open(f"{d}/MANIFEST.json", encoding="utf-8")) if os.path.exists(f"{d}/MANIFEST.json") else {}
    man = {"name": "clin_v1/trialgpt_cv", "source": "clin_v1/trialgpt_test (frozen; same items, new ids)",
           "source_sha256": reg["clin_v1/trialgpt_test"]["sha256"], "folds": K, "fold_rule":
           f"patients sorted, random.Random({SEED}).shuffle, fold = position mod {K}",
           "development_split": "clin_v1/trialgpt_dev (10 patients, never in a fold)", "by_fold": by_fold,
           "shortcut_validation": {"case_blind_type_prior_on_held_out_fold": sv},
           "labels": "met (s 1, s_prime 0); not met (0, 1); NEI and N/A (0, 0)",
           "n_records": len(recs), "n_groups": len(items), "sha256": sha, "git_commit": commit,
           "python": sys.version.split()[0],
           "created": old["created"] if old.get("sha256") == sha else time.strftime("%Y-%m-%d"), "frozen": True}
    json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
    reg["clin_v1/trialgpt_cv"] = {"path": "clin_v1/trialgpt_cv/records.jsonl", "split": "cv", "level": "external",
                                  "tier": "external", "n_groups": len(items), "n_records": len(recs),
                                  "manifest": "clin_v1/trialgpt_cv/MANIFEST.json", "frozen": True,
                                  "created": man["created"], "sha256": sha}
    print("trialgpt_cv", len(items), "items", {k: (v["patients"], v["items"]) for k, v in by_fold.items()}, sha[:12])

    # MedEinst training pairs: alias of the clinical pairs set (same file)
    reg["clin_v1/medeinst_train"] = dict(reg["clin_v1/clinpairs_medeinst"]) | {"alias_of": "clin_v1/clinpairs_medeinst"}
    print("medeinst_train -> alias of clinpairs_medeinst", reg["clin_v1/medeinst_train"]["sha256"][:12])
    json.dump(reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
