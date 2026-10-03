"""CPU check of scripts/prms/foverprm.py. Run: python tests/test_prm_foverprm.py
(a) build_inputs and the verbatim FoVer helper against the format of the official usage example (string level);
(b) load() + score() end to end on a tiny random LlamaForCausalLM (2 layers, hidden 64) saved with the released
tokenizer files, cross-checked against the card's single-sequence route (apply_chat_template, model(inputs),
extract_fover_scores). Downloads the released tokenizer/config files only, never the weights."""
import math, os, shutil, sys, tempfile

import torch
from huggingface_hub import snapshot_download
from tokenizers import Tokenizer
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "prms"))
import foverprm as F  # noqa: E402

TOKENIZER_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"]
TASK = ('Your task is to evaluate the accuracy of each step in the provided solution to the above question. For each '
        'step, respond with "correct" if the reasoning is logically valid and mathematically sound, or if the step is '
        'a general statement or transition that does not contain reasoning. Respond with "incorrect" if the step '
        'includes any errors or flawed logic.')
HEAD = ("<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\n"
        "Today Date: 26 Jul 2024\n\n<|eot_id|>")
RECS = [
    {"rule_text": "Give drug X only if the eGFR is at least 30 mL/min/1.73m2.",
     "case_text": "Woman, 72 years.\neGFR today: 24 mL/min/1.73m2.\nNo known drug allergies.",
     "claim_text": "Do not give drug X."},
    {"rule_text": "Give drug X only if the eGFR is at least 30 mL/min/1.73m2.",
     "case_text": "Woman, 72 years.\neGFR in 2019: 24 mL/min/1.73m2.\neGFR today: 41 mL/min/1.73m2.\n"
                  "Walks daily.\nNo known drug allergies.\nLives with her daughter.",
     "claim_text": "The eGFR criterion is met."},
    {"rule_text": "", "case_text": "A 30-year-old man has fever, neck stiffness and photophobia for one day.",
     "claim_text": "The most likely diagnosis is bacterial meningitis."},
]


def turn(role, text):
    return f"<|start_header_id|>{role}<|end_header_id|>\n\n{text}<|eot_id|>"


def user(problem, step):
    return f"** Problem **\n{problem}\n\n** Task **\n{TASK}\n\n** Sotluion **\n{step}"


def released_files():
    return snapshot_download(F.HF_ID, revision=F.REVISION, allow_patterns=TOKENIZER_FILES + ["config.json"])


def test_build_inputs():
    src = released_files()
    tok = AutoTokenizer.from_pretrained(src)
    # the card's usage example through the verbatim helper and the released chat template
    card = F.get_fover_input_format(problem="Calculate (1+1)*(1+2)", solution_steps=["1+1=2", "1+2=3", "2*3=8"])
    assert tok.apply_chat_template(card, tokenize=False) == (
        HEAD + turn("user", user("Calculate (1+1)*(1+2)", "1+1=2")) + turn("assistant", "correct")
        + turn("user", "1+2=3") + turn("assistant", "correct") + turn("user", "2*3=8") + turn("assistant", "correct"))
    # one record = the same format with the claim as the single step
    r = RECS[0]
    want = user(f"Rule: {r['rule_text']}\n\nCase:\n{r['case_text']}", r["claim_text"])
    assert F.build_inputs(r) == [{"role": "user", "content": want}, {"role": "assistant", "content": "correct"}]
    text = tok.apply_chat_template(F.build_inputs(r), tokenize=False)
    assert text == HEAD + turn("user", want) + turn("assistant", "correct")
    assert F.build_inputs(RECS[2])[0]["content"] == user(RECS[2]["case_text"], RECS[2]["claim_text"])  # no rule
    # ids as in the released tokenizer.json; both verdict words are single tokens (ids quoted in PROMPT_NOTE)
    raw = Tokenizer.from_file(os.path.join(src, "tokenizer.json"))
    assert tok(text, add_special_tokens=False)["input_ids"] == raw.encode(text, add_special_tokens=False).ids
    assert tok.encode("correct", add_special_tokens=False) == [20523]
    assert tok.encode("incorrect", add_special_tokens=False) == [63054]


def test_score_end_to_end():
    src = released_files()
    # "llama" in the directory name: the official extract_fover_scores infers the model type from it
    with tempfile.TemporaryDirectory(prefix="tiny-llama-fover-", ignore_cleanup_errors=True) as d:
        cfg = AutoConfig.from_pretrained(src, num_hidden_layers=2, hidden_size=64, intermediate_size=128,
                                         num_attention_heads=4, num_key_value_heads=2, head_dim=16)
        torch.manual_seed(0)
        AutoModelForCausalLM.from_config(cfg, dtype=torch.float32).save_pretrained(d)
        for f in TOKENIZER_FILES:
            shutil.copy(os.path.join(src, f), d)
        model, tok = F.load(d, device="cpu", dtype="float32")
        assert type(model).__name__ == "LlamaForCausalLM"
        u = F.score(model, tok, RECS, batch_size=2)
        assert len(u) == len(RECS) and all(isinstance(v, float) and math.isfinite(v) and abs(v) <= 30 for v in u)
        print("u", u)
        # official route, one sequence at a time: same position, same value up to float error
        for rec, v in zip(RECS, u):
            enc = tok.apply_chat_template(F.build_inputs(rec), return_tensors="pt")
            ids = enc["input_ids"] if hasattr(enc, "keys") else enc  # transformers 5 returns a BatchEncoding
            # independent of FoVer's helper: '\n\n' after <|start_header_id|>assistant<|end_header_id|>, then 'correct'
            at = F.get_step_token_position(ids[0].numpy(), tok, "llama")
            assert len(at) == 1 and ids[0, at[0] - 3:at[0] + 2].tolist() == [128006, 78191, 128007, 271, 20523], at
            with torch.no_grad():
                p = F.extract_fover_scores(tokenized_prompt=ids[0].numpy(), logits=model(ids).logits[0], tokenizer=tok)
            assert len(p) == 1 and abs(math.log(p[0] / (1 - p[0])) - v) < 1e-4, (p, v)
        # the GPU default (bf16 weights, fp32 head rows) runs and stays close to the float32 run
        u16 = F.score(F.load(d, device="cpu")[0], tok, RECS, batch_size=2)
        print("u bf16", u16)
        assert all(abs(a - b) < 0.05 for a, b in zip(u16, u)), (u16, u)


if __name__ == "__main__":
    test_build_inputs()
    test_score_end_to_end()
    print("ok")
