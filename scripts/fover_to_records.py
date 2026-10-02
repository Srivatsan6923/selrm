"""FoVer formal-verification step labels -> verdict-format training records (B-TR-fover).
Pinned dataset (configs/datasets_b.json, CC-BY-4.0): every row is a problem, its
solution steps and one correct/incorrect label per step. One record per row from the
final step (labels 50/50 by the dataset's design) plus earlier steps, 50/50, up to the
60k example budget. rule_text is empty (no stated rule, as in C's clinical sets);
case = problem + previous steps; claim = the step. Rows longer than MAX_CHARS are dropped.
  python scripts/fover_to_records.py OUT_DIR [N]      (writes OUT_DIR/train.jsonl + MANIFEST.json)"""
import json, os, random, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_CHARS = 2800                     # ~800 tokens of case + claim, inside max_len 1024 with the prompt


def records(rows, n, seed=0):
    rng = random.Random(seed)
    last, early = [], {True: [], False: []}
    for row in rows:
        steps, labels = list(row["solution_steps"]), [bool(x) for x in row["error_labels"]]
        for i, (step, ok) in enumerate(zip(steps, labels)):
            prev = "\n".join(steps[:i]) or "(none)"
            case = f"{row['problem']}\n\nPrevious steps:\n{prev}"
            if len(case) + len(step) > MAX_CHARS:
                continue
            rec = {"iid": f"fover/{row['id']}/{i}", "tid": f"fover/{row['id']}", "set": "fover_v1", "split": "train",
                   "tier": "fover", "level": "fover", "rid": f"fover_{row['base_dataset']}", "cid": "step",
                   "family": row["base_dataset"], "nm_kind": "none", "case_kind": "base", "rule_text": "",
                   "case_text": case, "condition": "", "claim_type": "conclusion", "claim_role": "s",
                   "claim_text": step, "label": int(ok), "state": [], "ledger": [], "prose": "",
                   "meta": {"source": row["base_dataset"], "row": row["id"], "step": i, "of": len(steps)}}
            (last if i == len(steps) - 1 else early[ok]).append(rec)
    k = max(0, n - len(last)) // 2
    extra = rng.sample(early[True], min(k, len(early[True]))) + rng.sample(early[False], min(k, len(early[False])))
    out = last + extra
    rng.shuffle(out)
    return out[:n], {"rows": len(rows), "last_step": len(last), "earlier": len(extra), "n": min(n, len(out)),
                     "label1": sum(r["label"] for r in out[:n])}


def main():
    out_dir, n = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    cfg = json.load(open(f"{REPO_ROOT}/configs/datasets_b.json"))["datasets"][0]
    from huggingface_hub import hf_hub_download
    import pandas as pd
    path = hf_hub_download(cfg["id"], "data/train-00000-of-00001.parquet", repo_type="dataset",
                           revision=cfg["revision"])
    rows = pd.read_parquet(path).to_dict("records")
    recs, stats = records(rows, n)
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/train.jsonl.tmp", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    os.replace(f"{out_dir}/train.jsonl.tmp", f"{out_dir}/train.jsonl")
    json.dump({"source": cfg["id"], "revision": cfg["revision"], "license": cfg.get("license"),
               "max_chars": MAX_CHARS, **stats}, open(f"{out_dir}/MANIFEST.json", "w"), indent=1)
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
