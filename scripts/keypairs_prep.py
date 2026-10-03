"""Key pairs (C-CL-keypairs): two exam questions whose keyed answers each occur among the other's
options (v13 Sec. 3.2 and App. External tiers). CPU only; deterministic.
  python scripts/keypairs_prep.py [--out data]
Sources (pinned): MedQA USMLE 4-option English (bigbio/med_qa, config med_qa_en_4options_source; test for
evaluation, train for C's clinical training pairs) and CareQA English (HPAI-BSC/CareQA, CareQA_en; test only).
Questions kept: a case description (a patient vignette: an age or patient noun and at least one sentence
before the final question), a lead-in that is not negatively phrased (except, not, least, false, incorrect,
untrue, cannot, never, contraindicated as the asked property), no option that refers to other options
(all/none/both/neither of the above/following, 'A and B'), stem of at least 8 tokens. Candidate pairs within
one split: keys differ and each key occurs (normalised text) among the other's options. One-to-one matching:
greedy by TF-IDF cosine of the stems, highest first, each question in at most one pair (ties: smaller ids).
Records: block per pair, base = question 1, flip = question 2; case_text = the complete question stem; claims
s = 'The answer is <key 1>.' and s_prime = 'The answer is <key 2>.'; rule_text ''; reader condition = the two
candidate answers. meta: ids, stem similarity and its tercile, category / exam step.
Variant 'oneway' (proposed to the lead, 3 Oct: the v13 definition yields 13 MedQA-test and 3 CareQA pairs): at
least one key is among the other's options; MedQA test and validation pooled (validation is used by no role);
CareQA without the case-description requirement (most CareQA items are knowledge questions).
Writes <out>/clin_v1/keypairs_{medqa,careqa,medqa_train,medqa_oneway,careqa_oneway}/{records.jsonl, MANIFEST.json}
and registry entries."""
import argparse, collections, hashlib, json, os, re, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDQA = ("bigbio/med_qa", "484a6c066fe8e75c83edea0c88b5169316714fcd", "med_qa_en_4options_source/{split}-00000-of-00001.parquet")
CAREQA = ("HPAI-BSC/CareQA", "1d976cc544ccb9dfc96e14439e6840e8a810cec5", "CareQA_en.json")
NEG = re.compile(r"\b(except|not|least|false|incorrect|untrue|cannot|never)\b", re.I)
REFER = re.compile(r"\b(all|none|both|neither) of the (above|following|options|answers)\b|^both\b|^neither\b|"
                   r"\b[A-E] (and|or) [A-E]\b", re.I)
PATIENT = re.compile(r"\b\d+[- ](year|month|week|day)s?[- ]old\b|\b(patient|man|woman|boy|girl|infant|newborn|child|"
                     r"neonate|adolescent|mother|father|male|female|gentleman|lady|baby)\b", re.I)
SENT = re.compile(r"(?<=[.!?])\s+")


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def norm(t):
    return re.sub(r"\s+", " ", str(t)).strip().lower().rstrip(".")


def lead_in(stem):
    parts = [p for p in SENT.split(stem.strip()) if p]
    return parts[-1] if parts else stem, parts[:-1]


def keep(q, case_filter=True):
    """-> None if kept, else the exclusion reason."""
    lead, before = lead_in(q["stem"])
    if len(q["stem"].split()) < 8:
        return "short stem"
    if NEG.search(lead):
        return "negative lead-in"
    if any(REFER.search(o) for o in q["options"]):
        return "option refers to other options"
    if case_filter and (not before or not PATIENT.search(q["stem"])):
        return "no case description"
    return None


def medqa(split, cache):
    import pandas as pd
    from huggingface_hub import hf_hub_download
    f = MEDQA[2].format(split=split)
    p = hf_hub_download(MEDQA[0], f, repo_type="dataset", revision=MEDQA[1], local_dir=cache)
    df = pd.read_parquet(p)
    out = []
    for i, r in df.iterrows():
        opts = {o["key"]: o["value"] for o in r["options"]}
        out.append({"id": f"medqa-{split}-{i:05d}", "stem": r["question"], "options": list(opts.values()),
                    "key": opts[r["answer_idx"]], "category": r["meta_info"]})
    return out, f, sha256(p)


def careqa(cache):
    from huggingface_hub import hf_hub_download
    p = hf_hub_download(CAREQA[0], CAREQA[2], repo_type="dataset", revision=CAREQA[1], local_dir=cache)
    rows = json.load(open(p, encoding="utf-8"))
    rows = rows if isinstance(rows, list) else rows.get("test", rows)
    out = []
    for r in rows:
        opts = [r[f"op{k}"] for k in range(1, 5)]
        out.append({"id": f"careqa-{r['unique_id']}", "stem": r["question"], "options": opts, "key": opts[int(r["cop"]) - 1],
                    "category": r["category"], "year": r.get("year")})
    return out, CAREQA[2], sha256(p)


def mine(qs, mode="strict"):
    """One-to-one key pairs by greedy TF-IDF similarity of the stems. strict (v13): each key is among the
    other's options; oneway: at least one key is among the other's options."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    by_opt = collections.defaultdict(list)
    for i, q in enumerate(qs):
        for o in q["options"]:
            by_opt[norm(o)].append(i)
    cand = set()
    for i, q in enumerate(qs):
        for j in by_opt[norm(q["key"])]:
            if j != i and norm(qs[j]["key"]) != norm(q["key"]) and (
                    mode == "oneway" or norm(qs[j]["key"]) in {norm(o) for o in q["options"]}):
                cand.add((min(i, j), max(i, j)))
    if not cand:
        return []
    X = TfidfVectorizer(sublinear_tf=True).fit_transform([q["stem"] for q in qs])
    sim = {c: float((X[c[0]] @ X[c[1]].T).toarray()[0, 0]) for c in cand}
    used, pairs = set(), []
    for (i, j) in sorted(cand, key=lambda c: (-sim[c], c)):
        if i not in used and j not in used:
            used |= {i, j}
            pairs.append((i, j, sim[(i, j)]))
    return pairs


def records_of(name, split, qs, pairs):
    sims = sorted(s for _, _, s in pairs)
    cut = [sims[len(sims) // 3], sims[2 * len(sims) // 3]] if sims else [0, 0]
    out = []
    for i, j, s in pairs:
        q1, q2 = qs[i], qs[j]
        tid = f"kp_{name}_{q1['id']}_{q2['id']}"
        meta = {"q1": q1["id"], "q2": q2["id"], "similarity": round(s, 4),
                "tercile": 1 + (s >= cut[0]) + (s >= cut[1]), "category": [q1["category"], q2["category"]]}
        base = {"tid": tid, "set": "clin_v1", "split": split, "tier": "external", "level": "external", "rid": name,
                "cid": q1["id"], "family": str(q1["category"]), "nm_kind": "none", "rule_text": "",
                "condition": f"which answer is correct: {q1['key']} or {q2['key']}", "claim_type": "conclusion",
                "state": [], "ledger": [], "prose": "", "meta": meta}
        for kind, q in (("base", q1), ("flip", q2)):
            for role, k in (("s", q1["key"]), ("s_prime", q2["key"])):
                out.append(base | {"iid": f"{tid}/{kind}/conclusion/{role}", "case_kind": kind, "case_text": q["stem"],
                                   "claim_role": role, "claim_text": f"The answer is {k}.",
                                   "label": int((kind == "base") == (role == "s"))})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--cache", default=f"{REPO}/data/clin_v1/qa_raw")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    reg = {}
    def medqa_pool(*splits):
        parts = [medqa(s, a.cache) for s in splits]
        return [q for qs, _, _ in parts for q in qs], " + ".join(f for _, f, _ in parts), " ".join(h for _, _, h in parts)

    # (name, split, source, loader, mode, case filter); the v13 definition first, then the variant proposed to the lead
    jobs = [("keypairs_medqa", "test", MEDQA, lambda: medqa("test", a.cache), "strict", True),
            ("keypairs_careqa", "test", CAREQA, lambda: careqa(a.cache), "strict", True),
            ("keypairs_medqa_train", "train", MEDQA, lambda: medqa("train", a.cache), "strict", True),
            ("keypairs_medqa_oneway", "test", MEDQA, lambda: medqa_pool("test", "validation"), "oneway", True),
            ("keypairs_careqa_oneway", "test", CAREQA, lambda: careqa(a.cache), "oneway", False)]
    for name, split, src, load, mode, cf in jobs:
        qs, f, h = load()
        reasons = collections.Counter(keep(q, cf) or "kept" for q in qs)
        kept = [q for q in qs if keep(q, cf) is None]
        pairs = mine(kept, mode)
        recs = records_of(name.replace("keypairs_", ""), split, kept, pairs)
        for r in recs:
            validate(r)
        d = f"{a.out}/clin_v1/{name}"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as fh:
            for r in recs:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        cats = collections.Counter(c for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s"
                                   for c in r["meta"]["category"])
        man = {"name": f"clin_v1/{name}", "source": src[0], "revision": src[1], "source_file": f, "source_sha256": h,
               "split": split, "mode": mode, "case_description_required": cf,
               "questions": len(qs), "exclusions": dict(reasons), "questions_kept": len(kept),
               "n_pairs": len(pairs), "yield_questions_in_pairs": round(2 * len(pairs) / max(1, len(kept)), 4),
               "categories_in_pairs": dict(cats), "git_commit": commit, "python": sys.version.split()[0],
               "rule": __doc__.split("Questions kept:")[1].split("Writes")[0].strip(),
               "sha256": sha256(f"{d}/records.jsonl"), "created": time.strftime("%Y-%m-%d"), "frozen": True,
               "shortcut_validation": {"claim_only_reversal": 0.0,
                                       "note": "Proposition 1 (i): a claim-only scorer gives d(q1) = d(q2), so no pair reverses"}}
        json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
        reg[f"clin_v1/{name}"] = {"path": f"clin_v1/{name}/records.jsonl", "split": split, "level": "external",
                                  "tier": "external", "n_groups": len(pairs), "n_records": len(recs),
                                  "manifest": f"clin_v1/{name}/MANIFEST.json", "frozen": True,
                                  "created": man["created"], "sha256": man["sha256"]}
        print(name, len(qs), "questions,", len(kept), "kept,", len(pairs), "pairs", dict(reasons), dict(cats))
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    old = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    json.dump(old | reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
