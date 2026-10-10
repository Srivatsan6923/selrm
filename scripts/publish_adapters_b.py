"""Publish kept adapters (configs/keep_adapters.json) from the PVC to a private
Hugging Face repo, one folder per run_id, and print the configs/adapters.json
entries (INTERFACES 6) for the laptop to commit. Runs in a CPU Job with HF_TOKEN
from a Kubernetes secret (never printed). Only adapters whose run is DONE and whose
TRAINED.json exists are uploaded; an existing identical upload is skipped.
  python scripts/publish_adapters_b.py --root /pvc/selrm --repo <owner>/selrm-adapters"""
import argparse, json, os, sys

SYSTEMS = {"B-F-ledger2-triplets-s0": "ledger2_triplets", "B-F-ledger2-blocks-s0": "ledger2_blocks",
           "B-F-verdict-triplets-s0": "verdict_triplets", "B-F-verdict-blocks-s0": "verdict_blocks",
           "B-PRM": "stepcheck"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--repo", required=True)
    a = ap.parse_args()
    from huggingface_hub import HfApi
    api = HfApi()                                   # HF_TOKEN from the environment
    api.create_repo(a.repo, private=True, exist_ok=True)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    keep = json.load(open(f"{repo_root}/configs/keep_adapters.json"))["keep"]
    out = {}
    for rid in keep:
        ad, res = f"{a.root}/adapters/{rid}", f"{a.root}/results/{rid}"
        if not (os.path.exists(f"{res}/DONE") and os.path.exists(f"{ad}/TRAINED.json")):
            print(f"skip {rid}: not finished", file=sys.stderr)
            continue
        meta = json.load(open(f"{res}/meta.json"))
        # PEFT's generated README.md names the pod-local base path as base_model, which the Hub rejects as metadata
        info = api.upload_folder(repo_id=a.repo, folder_path=ad, path_in_repo=rid, ignore_patterns=["README.md"],
                                 commit_message=f"{rid} ({meta['format']}, {meta.get('corpus')}, seed {meta.get('seed')})")
        out[SYSTEMS.get(rid, rid)] = {"run_id": rid, "path": f"hf://{a.repo}/{rid}", "repo": a.repo,
                                      "revision": info.oid, "base_model": meta["model"],
                                      "base_revision": meta.get("model_revision"), "format": meta["format"],
                                      "corpus": meta.get("corpus"), "seed": meta.get("seed"),
                                      "load_note": "base must be loaded as Qwen3_5ForConditionalGeneration (Unsloth "
                                                   "FastLanguageModel or AutoModelForImageTextToText); prompts from "
                                                   "selrm/prompts.py with enable_thinking=False"}
        print(f"uploaded {rid} -> {a.repo}@{info.oid}", file=sys.stderr)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
