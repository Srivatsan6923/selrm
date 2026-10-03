"""CPU end-to-end check of scripts/eval_c.py with a tiny random Qwen3.5 model and the real
tokenizer (numbers are meaningless; it checks that every path runs and writes its files):
verdict, prompted ledger with the lenient pass, prompted summary, an adapter-free TrialGPT
run with rule_v1/dev_missing, reading rule_v1 sets from a B-style root and clin_v1 sets from
a C root that is pre-tokenised on first use.
  python tests/selftest_eval_c.py BCODE_DIR TOKENIZER_DIR RULE_V1_DATA_DIR [WORK_DIR]
BCODE_DIR: role B's code snapshot (e.g. git archive ac524e8); RULE_V1_DATA_DIR: A's layout
with REGISTRY.json and rule_v1/dev_missing/records.jsonl."""
import json, os, shutil, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bcode, tok_dir, rv1 = (os.path.abspath(x) for x in sys.argv[1:4])
work = os.path.abspath(sys.argv[4] if len(sys.argv) > 4 else f"{REPO}/scratch/selftest_c")
shutil.rmtree(work, ignore_errors=True)
broot, croot = f"{work}/broot", f"{work}/croot"
sys.path[:0] = [bcode, f"{bcode}/scripts"]

from transformers import AutoTokenizer, Qwen3_5ForCausalLM, Qwen3_5TextConfig
tok = AutoTokenizer.from_pretrained(tok_dir)
cfg = Qwen3_5TextConfig(vocab_size=len(tok), hidden_size=64, intermediate_size=128, num_hidden_layers=2,
                        layer_types=["linear_attention", "full_attention"], num_attention_heads=2,
                        num_key_value_heads=1, head_dim=32, linear_num_key_heads=2, linear_num_value_heads=2,
                        linear_key_head_dim=16, linear_value_head_dim=16, linear_conv_kernel_dim=4,
                        eos_token_id=tok.eos_token_id, pad_token_id=tok.pad_token_id)
mdir = f"{work}/models/tiny--qwen35"
Qwen3_5ForCausalLM(cfg).save_pretrained(mdir)
tok.save_pretrained(mdir)


def head(src, dst, n_groups):
    keep, out = set(), []
    for line in open(src, encoding="utf-8"):
        r = json.loads(line)
        if r["tid"] not in keep and len(keep) >= n_groups:
            continue
        keep.add(r["tid"]); out.append(line)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8", newline="\n").writelines(out)


# B-style root: rule_v1/dev_missing (first 20 groups) and its pre-tokenised prompts (B's pretok)
head(f"{rv1}/rule_v1/dev_missing/records.jsonl", f"{broot}/data/rule_v1/dev_missing/records.jsonl", 20)
json.dump({"rule_v1/dev_missing": {"path": "rule_v1/dev_missing/records.jsonl"}}, open(f"{broot}/data/REGISTRY.json", "w"))
import pretok
for fmt in ("verdict", "ledger2", "summary2"):
    print(*pretok.build_eval(broot, {"format": fmt, "base_model": "tiny/qwen35"}, "rule_v1/dev_missing", tok))
# C root: TrialGPT dev (first 6 items), not pre-tokenised
head(f"{REPO}/data/clin_v1/trialgpt_dev/records.jsonl", f"{croot}/data/clin_v1/trialgpt_dev/records.jsonl", 6)
json.dump({"clin_v1/trialgpt_dev": {"path": "clin_v1/trialgpt_dev/records.jsonl"}}, open(f"{croot}/data/REGISTRY.json", "w"))

hp = {"backend": "hf", "bf16": False}
sets = ["rule_v1/dev_missing", "clin_v1/trialgpt_dev"]
runs = [{"run_id": "ST-verdict", "priority": 1, "format": "verdict", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "sets": sets},
        {"run_id": "ST-ledger", "priority": 2, "format": "ledger2", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "bs_gen": 8, "max_new": 16, "sets": sets},
        {"run_id": "ST-ledger-lenient", "priority": 5, "format": "ledger2", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "rejudge_from": "ST-ledger", "sets": sets},
        {"run_id": "ST-summary", "priority": 3, "format": "summary2", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "bs_gen": 8, "max_new": 16, "sets": sets},
        {"run_id": "ST-nocase", "priority": 4, "format": "verdict", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "nocase": True, "sets": sets},
        {"run_id": "ST-sub", "priority": 6, "format": "verdict", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "bs_score": 8, "n_groups": 10, "claim_types": ["conclusion"], "sets": ["rule_v1/dev_missing"]},
        {"run_id": "ST-skipped", "priority": 0, "format": "rationale", "adapter": None, "base_model": "tiny/qwen35",
         "hp": hp, "sets": sets}]
os.makedirs(f"{croot}/tasks", exist_ok=True)
json.dump({"runs": runs}, open(f"{croot}/tasks/t.json", "w"), indent=1)
env = os.environ | {"SELRM_BACKEND": "hf", "SELRM_MODELS": f"{work}/models", "HF_HUB_OFFLINE": "1"}
r = subprocess.run([sys.executable, f"{REPO}/scripts/eval_c.py", "--root", croot, "--broot", broot, "--bcode", bcode,
                    "--tasks", f"{croot}/tasks/t.json", "--formats", "verdict,ledger2,summary2"], env=env)
assert r.returncode == 0, r.returncode
for run in ("ST-verdict", "ST-ledger", "ST-summary"):
    d = f"{croot}/results/{run}"
    files = sorted(os.listdir(d))
    print(run, files)
    assert "DONE" in files and "meta.json" in files, files
    for s in ("rule_v1~dev_missing", "clin_v1~trialgpt_dev"):
        assert f"scores_{s}.jsonl" in files and f"summary_{s}.json" in files, (run, s)

assert not os.path.exists(f"{croot}/results/ST-skipped/DONE")
lj = sorted(os.listdir(f"{croot}/results/ST-ledger-lenient"))
print("ST-ledger-lenient", lj)
assert "DONE" in lj and "scores_rule_v1~dev_missing.jsonl" in lj and "scores_clin_v1~trialgpt_dev.jsonl" in lj
row = json.loads(open(f"{croot}/results/ST-ledger-lenient/scores_rule_v1~dev_missing.jsonl", encoding="utf-8").readline())
assert "reader_output" in row and "ledger_lenient" in row
sys.path.insert(0, f"{REPO}/scripts")
import eval_c
case = "Female, 30 years.\nSerum potassium today: 5.3 mmol/L\nRecords from 2007 list serum potassium at 4.6 mmol/L."
tab = ("| need | found | subject | status | time |\n| :--- | :--- | :--- | :--- :--- |\n"
       "| potassium above 5.0 | 5.3 mmol/L | patient | present | current |\n"
       "| potassium above 5.0 | **4.6 mmol/L** | patient | present | past (2007) |")
got = eval_c.lenient_ledger(tab, case)
assert got and got.count("need:") == 2 and "found: 4.6 mmol/L" in got, got
assert eval_c.lenient_ledger(tab.replace("4.6", "9.9"), case) is None
sb = sorted(os.listdir(f"{croot}/results/ST-sub"))
print("ST-sub", sb)
assert "scores_rule_v1~dev_missing.jsonl" in sb
sub_rows = [json.loads(l) for l in open(f"{croot}/results/ST-sub/scores_rule_v1~dev_missing.jsonl", encoding="utf-8")]
assert sub_rows and all(r["iid"].split("/")[2] == "conclusion" for r in sub_rows)
assert json.load(open(f"{croot}/results/ST-sub/summary_rule_v1~dev_missing.json"))["subset"]["n_groups"] == 10
nc = sorted(os.listdir(f"{croot}/results/ST-nocase"))
print("ST-nocase", nc)
assert "scores_nocase~rule_v1~dev_missing.jsonl" in nc and "scores_nocase~clin_v1~trialgpt_dev.jsonl" in nc
assert all(json.loads(l)["case_text"] == "" for l in open(f"{croot}/data/nocase/rule_v1/dev_missing.jsonl", encoding="utf-8"))
assert os.path.exists(f"{croot}/tok/tiny--qwen35/eval/clin_v1/trialgpt_dev/reader_ledger.npz")
print("selftest_eval_c OK")
