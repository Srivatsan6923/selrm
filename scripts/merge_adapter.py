"""Merge one of B's kept LoRA adapters into the base weights, so vLLM can serve the
ledger model for selection scoring without LoRA support for this architecture.

  python scripts/merge_adapter.py --base DIR --adapter DIR --out DIR

The merged model is validated against B's own scores before any use
(score_pool.py validate). Writes MERGED.json (adapter run id, sha256 of the adapter
weights, base revision, library versions).
"""
import argparse
import hashlib
import json
import os
import shutil

import peft
import torch
import transformers
from transformers.models.qwen3_5.modeling_qwen3_5 import Qwen3_5ForConditionalGeneration


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--adapter", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if os.path.exists(os.path.join(a.out, "MERGED.json")):
        print("exists:", a.out)
        return
    model = Qwen3_5ForConditionalGeneration.from_pretrained(a.base, dtype=torch.bfloat16)
    model = peft.PeftModel.from_pretrained(model, a.adapter).merge_and_unload()
    os.makedirs(a.out, exist_ok=True)
    model.save_pretrained(a.out, safe_serialization=True, max_shard_size="5GB")
    for f in os.listdir(a.base):           # tokenizer, chat template, processor configs
        if not f.endswith(".safetensors") and f not in ("model.safetensors.index.json", "config.json") \
                and os.path.isfile(os.path.join(a.base, f)):
            shutil.copy(os.path.join(a.base, f), a.out)
    h = hashlib.sha256(open(os.path.join(a.adapter, "adapter_model.safetensors"), "rb").read()).hexdigest()
    rev = open(os.path.join(a.base, "REVISION")).read().strip() if os.path.exists(os.path.join(a.base, "REVISION")) else None
    json.dump({"adapter": os.path.basename(a.adapter.rstrip("/")), "adapter_sha256": h, "base": a.base,
               "base_revision": rev, "torch": torch.__version__, "transformers": transformers.__version__,
               "peft": peft.__version__, "dtype": "bfloat16"},
              open(os.path.join(a.out, "MERGED.json"), "w"), indent=1)
    print("merged", a.adapter, "->", a.out)


if __name__ == "__main__":
    main()
