"""clin_v1/nli4ct_{test,dev}: NLI4CT-P (SemEval-2024 Task 2) as canonical records (C-CL-nli4ct).
  python scripts/nli4ct_prep.py [--out data]
Source: GitHub ai-systems/Task-2-SemEval-2024 at commit 7f32fa6c (data files unchanged since 267230cc), files
pinned by sha256: gold_test.json (5,500 statements: 500 originals + 5,000 contrast statements with Intervention
and Causal_type), gold_practice_test.json (2,142: the 200 dev originals + their contrast statements) and
training_data.zip (the 999 clinical trial reports, 'CT json/NCT*.json'). No licence is stated by the organisers;
records are not redistributed (not in git), only rebuilt.
Record per statement: case_text = the section of the trial report the statement is about (both trials for a
Comparison statement, each headed by its NCT id), claim_text = the statement, rule_text '' (no rule), condition
(shown to readers) = the statement, label 1 for Entailment and 0 for Contradiction, claim_role s. A system
predicts Entailment iff u > 0 (fixed before scoring; the verdict prompt asks + or -). Metrics come from the
task's own scorer (scripts/eval_clinical.py nli4ct)."""
import argparse, hashlib, io, json, os, subprocess, sys, time, urllib.request, zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "https://raw.githubusercontent.com/ai-systems/Task-2-SemEval-2024/7f32fa6c7db43e577f22e9fc6c28eef1cc6d223e/"
SHA = {"gold_test.json": "fd2360a8a2077e9fc56e6c5e8128d698d05e0be9492682578b0768f0a222ed93",
       "gold_practice_test.json": "557583292755b76caed8229f2cfbe15c316cca3805aff7bbff72902de4859785",
       "training_data.zip": "ed3d9819cfebd2d1d5d70fd786323c904b341470f8dc173af39946f70a0e5b9f"}


def fetch(name, cache):
    os.makedirs(cache, exist_ok=True)
    path = f"{cache}/{name}"
    if not os.path.exists(path):
        urllib.request.urlretrieve(SRC + name, path)
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if h != SHA[name]:
        sys.exit(f"{name}: sha256 {h} differs from the pinned release")
    return path


def ctrs(zpath):
    out = {}
    with zipfile.ZipFile(zpath) as z:
        for n in z.namelist():
            base = os.path.basename(n)
            if "__MACOSX" in n or not base.startswith("NCT") or not base.endswith(".json"):
                continue
            out[base[:-5]] = json.loads(z.read(n).decode("utf-8"))
    return out


def section(ctr, name):
    return "\n".join(line.strip() for line in ctr[name])


def case_text(st, docs):
    sec = st["Section_id"]
    if st["Type"] == "Single":
        return f"{sec} section of clinical trial {st['Primary_id']}:\n{section(docs[st['Primary_id']], sec)}"
    return (f"{sec} section of clinical trial 1 ({st['Primary_id']}):\n{section(docs[st['Primary_id']], sec)}\n\n"
            f"{sec} section of clinical trial 2 ({st['Secondary_id']}):\n{section(docs[st['Secondary_id']], sec)}")


def records(stmts, docs, split):
    out = []
    for uuid, st in sorted(stmts.items()):
        tid = f"nli4ct_{split}_{uuid}"
        ct = st.get("Causal_type") or [None, None]
        out.append({"iid": f"{tid}/base/conclusion/s", "tid": tid, "set": "clin_v1", "split": split, "tier": "external",
                    "level": "external", "rid": st["Primary_id"], "cid": uuid, "family": st["Section_id"], "nm_kind": "none",
                    "case_kind": "base", "rule_text": "", "case_text": case_text(st, docs), "condition": st["Statement"],
                    "claim_type": "conclusion", "claim_role": "s", "claim_text": st["Statement"],
                    "label": int(st["Label"] == "Entailment"), "state": [], "ledger": [], "prose": "",
                    "meta": {"uuid": uuid, "type": st["Type"], "section": st["Section_id"],
                             "intervention": st.get("Intervention", "Original"), "causal_type": ct[0],
                             "original_uuid": ct[1], "label_name": st["Label"]}})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{REPO}/data")
    ap.add_argument("--cache", default=f"{REPO}/data/clin_v1/nli4ct_raw")
    a = ap.parse_args()
    sys.path.insert(0, REPO)
    from selrm.schema import validate
    docs = ctrs(fetch("training_data.zip", a.cache))
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    reg = {}
    zpath = fetch("training_data.zip", a.cache)
    for name, split, f in (("nli4ct_test", "test", "gold_test.json"), ("nli4ct_dev", "dev", "gold_practice_test.json"),
                           ("nli4ct_train", "train", "training_data.zip:train.json")):
        if f.startswith("training_data.zip:"):     # the released training statements (in-domain training, AUX S1)
            with zipfile.ZipFile(zpath) as z:
                stmts = json.loads(z.read(f.split(":", 1)[1]).decode("utf-8"))
        else:
            stmts = json.load(open(fetch(f, a.cache), encoding="utf-8"))
        recs = records(stmts, docs, split)
        for r in recs:
            validate(r)
        d = f"{a.out}/clin_v1/{name}"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as fh:
            for r in recs:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        sha = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
        old = json.load(open(f"{d}/MANIFEST.json", encoding="utf-8")) if os.path.exists(f"{d}/MANIFEST.json") else {}
        if old.get("sha256") == sha:             # unchanged frozen set: its manifest stays as written
            reg[f"clin_v1/{name}"] = {"path": f"clin_v1/{name}/records.jsonl", "split": split, "level": "external",
                                      "tier": "external", "n_groups": len(recs), "n_records": len(recs),
                                      "manifest": f"clin_v1/{name}/MANIFEST.json", "frozen": True,
                                      "created": old["created"], "sha256": sha}
            print(name, len(recs), "unchanged", sha[:12])
            continue
        man = {"name": f"clin_v1/{name}", "source": "github.com/ai-systems/Task-2-SemEval-2024", "revision": "7f32fa6c",
               "source_file": f, "source_sha256": SHA[f.split(":")[0]], "ctr_files": len(docs), "licence": "none stated by the organisers",
               "n_records": len(recs), "split": split,
               "by_intervention": {k: sum(r["meta"]["intervention"] == k for r in recs)
                                   for k in sorted({r["meta"]["intervention"] for r in recs})},
               "entailment": sum(r["label"] for r in recs), "prediction_rule": "Entailment iff u > 0",
               "shortcut_validation": {"note": "a constant predictor: all-Entailment gives Control F1 0.667 (binary, "
                                               "official scorer); all-Contradiction gives Faithfulness 1.0 and F1 0.0"},
               "git_commit": commit, "python": sys.version.split()[0], "sha256": sha,
               "created": time.strftime("%Y-%m-%d"), "frozen": True}
        json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
        reg[f"clin_v1/{name}"] = {"path": f"clin_v1/{name}/records.jsonl", "split": split, "level": "external",
                                  "tier": "external", "n_groups": len(recs), "n_records": len(recs),
                                  "manifest": f"clin_v1/{name}/MANIFEST.json", "frozen": True,
                                  "created": man["created"], "sha256": sha}
        print(name, len(recs), man["by_intervention"], sha[:12])
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    old = json.load(open(regp, encoding="utf-8")) if os.path.exists(regp) else {}
    json.dump(old | reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
