"""CPU end-to-end check of B's pipeline with a tiny random Qwen3.5 text model and
the real tokenizer: pretok -> queue runner (train 2 steps, evaluate) for all five
formats. Numbers are meaningless; this only checks that every path runs and
writes meta/scores/summaries/DONE. Needs transformers with Qwen3.5 and peft.
  python scripts/cpu_selftest_b.py TOKENIZER_DIR [WORK_DIR]"""
import json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from selrm.formats import FORMATS

tok_dir = sys.argv[1]
root = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "scratch/selftest")
shutil.rmtree(root, ignore_errors=True)
os.makedirs(f"{root}/data/mini", exist_ok=True)

# tiny model with the real vocabulary
from transformers import AutoTokenizer, Qwen3_5ForCausalLM, Qwen3_5TextConfig
tok = AutoTokenizer.from_pretrained(tok_dir)
cfg = Qwen3_5TextConfig(vocab_size=len(tok), hidden_size=64, intermediate_size=128, num_hidden_layers=2,
                        layer_types=["linear_attention", "full_attention"], num_attention_heads=2,
                        num_key_value_heads=1, head_dim=32, linear_num_key_heads=2, linear_num_value_heads=2,
                        linear_key_head_dim=16, linear_value_head_dim=16, linear_conv_kernel_dim=4,
                        eos_token_id=tok.eos_token_id, pad_token_id=tok.pad_token_id)
mdir = f"{root}/models/tiny--qwen35"
Qwen3_5ForCausalLM(cfg).save_pretrained(mdir)
tok.save_pretrained(mdir)

# tiny data: first records of the smoke sets
src = os.path.join(os.path.dirname(HERE), "data", "smoke_v2")
for name, n_groups in (("train_triplets", 60), ("test_heldout_rules", 12)):
    keep, out = set(), []
    for line in open(f"{src}/{name}.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["tid"] not in keep and len(keep) >= n_groups:
            continue
        keep.add(r["tid"]); out.append(line)
    open(f"{root}/data/mini/{name}.jsonl", "w", encoding="utf-8").writelines(out)

hp = {"backend": "hf", "bf16": False, "per_device": 4, "batch": 8, "save_every_s": 0, "workers": 0}
runs = [{"run_id": f"SELFTEST-{f}", "format": f, "corpus": "mini/train_triplets", "seed": 0,
         "max_steps": 2, "base_model": "tiny/qwen35", "hp": hp, "keep_adapter": f == "ledger2",
         "eval": {"bs_score": 8, "bs_gen": 8, "max_new": 24},
         "eval_sets": ["mini/test_heldout_rules"]} for f in FORMATS]
json.dump({"runs": runs}, open(f"{root}/queue.json", "w"), indent=1)

py = sys.executable
subprocess.run([py, f"{HERE}/pretok.py", "--root", root, "--queue", f"{root}/queue.json",
                "--tokenizer", mdir], check=True)
subprocess.run([py, f"{HERE}/train_eval_job.py", "--root", root, "--queue", f"{root}/queue.json"], check=True)

for r in runs:
    d = f"{root}/results/{r['run_id']}"
    assert os.path.exists(f"{d}/DONE"), f"{r['run_id']} not done: {os.listdir(d)}"
    meta = json.load(open(f"{d}/meta.json"))
    summ = json.load(open(f"{d}/summary_mini~test_heldout_rules.json"))
    n = sum(1 for _ in open(f"{d}/scores_mini~test_heldout_rules.jsonl"))
    assert "all" in summ and n > 0 and meta["train"]["steps"] == 2
    print("ok", r["run_id"], "TA", round(summ["all"]["TA"], 1), "eval", summ["eval"])
assert os.path.isdir(f"{root}/adapters/SELFTEST-ledger2") and not os.path.exists(f"{root}/ckpt/SELFTEST-verdict")
print("CPU SELFTEST PASS")
