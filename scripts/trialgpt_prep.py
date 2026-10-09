"""clin_v1/trialgpt_{dev,test}: the TrialGPT criterion-level annotations as canonical
records (docs/TRIALGPT_PROTOCOL.md). CPU only; deterministic.
  python scripts/trialgpt_prep.py [--out data]
Source: ncbi/TrialGPT-Criterion-Annotations (Hugging Face, pinned revision, public domain).
Inputs kept: patient note as released (numbered sentences), criterion text and type.
Targets: expert_eligibility; expert_sentences (evidence selection only). Never kept:
gpt4_explanation, gpt4_sentences, gpt4_eligibility, explanation_correctness.
One item = one annotation; two records per item (claim s: the patient meets the criterion;
claim s_prime: the patient does not meet it). Labels: met -> (1, 0); not met -> (0, 1);
not enough information and not applicable -> (0, 0), category in meta.
Split: patient-disjoint; DEV_N patients drawn with random.Random(SEED) from the sorted ids.
Writes <out>/clin_v1/trialgpt_{dev,test}/{records.jsonl, MANIFEST.json},
<out>/clin_v1/REGISTRY_C.json and configs/trialgpt_exclusions.json (trial ids and criterion
texts that role A excludes from ec_v1)."""
import argparse, collections, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = "ncbi/TrialGPT-Criterion-Annotations"
REVISION = "1cfcafde94a1560a33b4addc1638664fe28fc059"
PARQUET = "data/train-00000-of-00001.parquet"
SEED, DEV_N = 20261003, 10
GPT4_FIELDS = ("gpt4_explanation", "gpt4_sentences", "gpt4_eligibility", "explanation_correctness")
CATEGORY = {("inclusion", "included"): "met", ("inclusion", "not included"): "not_met",
            ("exclusion", "excluded"): "met", ("exclusion", "not excluded"): "not_met"}
CLAIMS = {"s": "The patient meets this criterion.", "s_prime": "The patient does not meet this criterion."}
LABELS = {"met": (1, 0), "not_met": (0, 1), "nei": (0, 0), "na": (0, 0)}


def category(ctype, elig):
    if elig == "not enough information":
        return "nei"
    if elig == "not applicable":
        return "na"
    return CATEGORY[(ctype, elig)]


def rule_text(ctype, text):
    return f"{ctype.capitalize()} criterion: {text}"


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load(cache):
    from huggingface_hub import hf_hub_download
    import pandas as pd
    p = hf_hub_download(DATASET, PARQUET, repo_type="dataset", revision=REVISION, local_dir=cache)
    return pd.read_parquet(p), p


def records_of(row, split):
    cat = category(row["criterion_type"], row["expert_eligibility"])
    tid = f"trialgpt_{int(row['annotation_id']):04d}"
    base = {"tid": tid, "set": "clin_v1", "split": split, "tier": "external", "level": "external",
            "rid": row["trial_id"], "cid": str(int(row["annotation_id"])), "family": row["criterion_type"],
            "nm_kind": "none", "case_kind": "base",
            "rule_text": rule_text(row["criterion_type"], row["criterion_text"]),
            "case_text": row["note"], "condition": row["criterion_text"],
            "claim_type": "conclusion", "state": [], "ledger": [], "prose": "",
            "meta": {"source": f"{DATASET}@{REVISION[:7]}", "annotation_id": int(row["annotation_id"]),
                     "patient_id": row["patient_id"], "trial_id": row["trial_id"],
                     "criterion_type": row["criterion_type"], "expert_eligibility": row["expert_eligibility"],
                     "category": cat, "expert_sentences": json.loads(row["expert_sentences"]),
                     "source_training_flag": bool(row["training"])}}
    return [base | {"iid": f"{tid}/base/conclusion/{role}", "claim_role": role, "claim_text": CLAIMS[role],
                    "label": LABELS[cat][i]} for i, role in enumerate(("s", "s_prime"))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--cache", default=f"{REPO}/data/clin_v1/trialgpt_raw")
    a = ap.parse_args()
    df, src = load(a.cache)
    assert len(df) == 1015 and df.patient_id.nunique() == 53, (len(df), df.patient_id.nunique())
    empty = df.criterion_text.isna() | (df.criterion_text.fillna("").str.strip() == "")
    dropped = [{"annotation_id": int(r.annotation_id), "patient_id": r.patient_id, "trial_id": r.trial_id,
                "expert_eligibility": r.expert_eligibility, "reason": "no criterion text in the release"}
               for r in df[empty].itertuples()]
    df = df[~empty]
    patients = sorted(df.patient_id.unique())
    dev = set(random.Random(SEED).sample(patients, DEV_N))
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    reg = {}
    for split in ("dev", "test"):
        part = df[df.patient_id.isin(dev) == (split == "dev")].sort_values("annotation_id")
        recs = [r for _, row in part.iterrows() for r in records_of(row, split)]
        for r in recs:
            validate(r)
            assert not any(f in json.dumps(r) for f in GPT4_FIELDS)
        d = f"{a.out}/clin_v1/trialgpt_{split}"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        items = [r for r in recs if r["claim_role"] == "s"]
        man = {"name": f"clin_v1/trialgpt_{split}", "source": DATASET, "revision": REVISION,
               "source_file": PARQUET, "source_sha256": sha256(src), "licence": "public domain (NCBI notice in LICENSE)",
               "split_rule": f"patient-disjoint; dev = random.Random({SEED}).sample(sorted 53 patient ids, {DEV_N})",
               "patients": sorted({r["meta"]["patient_id"] for r in items}),
               "n_items": len(items), "n_records": len(recs), "n_trials": len({r["rid"] for r in items}),
               "by_category": dict(collections.Counter(r["meta"]["category"] for r in items)),
               "by_type_eligibility": dict(collections.Counter(f"{r['family']}|{r['meta']['expert_eligibility']}"
                                                               for r in items)),
               "inputs": "case_text = note as released; rule_text = '<Type> criterion: <criterion_text>'; "
                         "condition = criterion_text; claims fixed (meets / does not meet)",
               "dropped_fields": list(GPT4_FIELDS), "dropped_items": [x for x in dropped if (x["patient_id"] in dev) == (split == "dev")],
               "git_commit": commit,
               "python": sys.version.split()[0], "created": time.strftime("%Y-%m-%d"), "frozen": True}
        man["sha256"] = sha256(f"{d}/records.jsonl")
        json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
        reg[f"clin_v1/trialgpt_{split}"] = {"path": f"clin_v1/trialgpt_{split}/records.jsonl", "split": split,
                                            "level": "external", "tier": "external", "n_groups": len(items),
                                            "n_records": len(recs), "manifest": f"clin_v1/trialgpt_{split}/MANIFEST.json",
                                            "frozen": True, "created": man["created"], "sha256": man["sha256"]}
        print(split, man["n_items"], "items", man["n_records"], "records", man["by_category"], man["sha256"][:12])
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    old = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    json.dump(old | reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)
    excl = {"source": f"{DATASET}@{REVISION}", "date": time.strftime("%Y-%m-%d"),
            "use": "role A excludes these trials and criterion texts from ec_v1 (FINAL_TASKS_A P0.5)",
            "trial_ids": sorted(df.trial_id.unique()),
            "criterion_texts": sorted(df.criterion_text.str.strip().unique())}
    json.dump(excl, open(f"{REPO}/configs/trialgpt_exclusions.json", "w", encoding="utf-8", newline="\n"), indent=1,
              ensure_ascii=False)
    print("exclusions:", len(excl["trial_ids"]), "trials,", len(excl["criterion_texts"]), "criterion texts")


if __name__ == "__main__":
    main()
