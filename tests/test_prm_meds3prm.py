"""CPU check of scripts/prms/meds3prm.py. Run: python tests/test_prm_meds3prm.py
(a) build_inputs against the format of the model card's usage example (string level) and the released tokenizer;
(b) load() + score() end to end on a tiny random Llama (2 layers, hidden 64) laid out like the release: a base folder
with full weights plus its own LoRA (as pixas/MedSSS_Policy) and a TOKEN_CLS LoRA adapter with a 2-class 'score' head
saved with the released tokenizer files (as pixas/MedSSS_PRM), cross-checked against the official single-sequence
obtain_prm_value_for_single_pair on the base weights + PRM adapter. Downloads tokenizer/config files only, never
the weights."""
import json, math, os, shutil, sys, tempfile
from itertools import chain

import torch
from huggingface_hub import snapshot_download
from peft import LoraConfig, PeftModel, get_peft_model
from transformers import AutoConfig, AutoModelForCausalLM, AutoModelForTokenClassification, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "prms"))
import meds3prm as M  # noqa: E402

TOKENIZER_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"]
TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]  # both released LoRAs
# The card's usage example, quoted (huggingface.co/pixas/MedSSS_PRM @ c9e7871, README.md).
CARD_INPUT = "How to stop a cough?"
CARD_STEPS = "Step 0: Let's break down this problem step by step.\n\nStep 1: First [omitted]"
RULE = ("For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe "
        "clindamycin instead: the patient has ever had a peptic ulcer (current or past); the patient or a first-degree "
        "relative (parent, sibling or child) has had diabetes at any time; the patient has ever had coronary artery "
        "disease (current or past).")
CASE = ("Male patient of 62 years.\nSpreading redness and warmth of the right shin for two days.\nOwns a bicycle.\n"
        "Had diabetes years ago that went into remission on a low-calorie diet.")
RECS = [  # a rule_v1 dev record (gs027 base, conclusion claim s), its s', and a clinical record without a rule
    {"rule_text": RULE, "case_text": CASE, "claim_text": "Prescribe cephalexin.", "claim_role": "s", "label": 1},
    {"rule_text": RULE, "case_text": CASE, "claim_text": "Prescribe clindamycin.", "claim_role": "s_prime", "label": 0},
    {"rule_text": "", "case_text": "A 30-year-old man has fever, neck stiffness and photophobia for one day.",
     "claim_text": "The most likely diagnosis is bacterial meningitis.", "claim_role": "s", "label": 1},
]


# ---- Verbatim from pixas/MedSSS @ 8238225 (MIT, Copyright (c) 2025 Shuyang Jiang): obtain_prm_value_for_single_pair
# ---- from Evol_Instruct/solver/sc_vm_solver.py without its 'prm-bi' branch (sequence-classification value models),
# ---- and ValueModel.forward_token / __call__ from Evol_Instruct/models/modeling_value_llama.py around a merged model.
def obtain_prm_value_for_single_pair(tokenizer, value_model, inputs, outputs, server):
    response = outputs


    messages = [
        {"role": "user", "content": inputs},
        {"role": "assistant", "content": response}
    ]

    prompt_text = tokenizer.apply_chat_template(messages[:-1], tokenize=False, add_generation_prompt=True)
    completions = ["Step" + completion if not completion.startswith("Step") else completion for completion in response.split("\n\nStep")]



    completion_ids = [
        tokenizer(completion + "\n\n", add_special_tokens=False)['input_ids'] for completion in completions
    ]
    response_id = list(chain(*completion_ids))
    pre_response_id = tokenizer(prompt_text, add_special_tokens=False)['input_ids']

    input_ids = pre_response_id + response_id

    value = value_model(input_ids=torch.tensor(input_ids).unsqueeze(0).to(value_model.device), return_all=True)  # [1, N]

    completion_index = []
    for i, completion in enumerate(completion_ids):
        if i == 0:
            completion_index.append(len(completion) + len(pre_response_id) - 1)
        else:
            completion_index.append(completion_index[-1] + len(completion))

    step_value = value[0, completion_index].cpu().numpy().tolist()
    return step_value


class ValueModel:
    model_type = "prm"

    def __init__(self, model):  # the official __init__ loads base + PRM LoRA and merges; here: already merged
        self.model = model

    @property
    def device(self):
        return self.model.device

    def forward_token(self, input_ids, attention_mask=None, return_all=False):
        with torch.inference_mode():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        if return_all:
            probs = torch.softmax(outputs[0], dim=-1)
        else:

            probs = torch.softmax(outputs[0][:, -1], dim=-1)
        score = probs[..., 1] # [B, N] or [B, ]
        return score

    def __call__(self, input_ids, attention_mask=None, **kwargs):
        return self.forward_token(input_ids=input_ids, attention_mask=attention_mask, **kwargs)
# ---- End of the verbatim code.


def released(repo, revision, files):
    return snapshot_download(repo, revision=revision, allow_patterns=files)


def test_build_inputs():
    # the card's example is a record without a rule whose claim is the card's Step 1
    card = M.build_inputs({"rule_text": "", "case_text": CARD_INPUT, "claim_text": "First [omitted]"})
    assert card == [{"role": "user", "content": CARD_INPUT}, {"role": "assistant", "content": CARD_STEPS}]
    msgs = M.build_inputs(RECS[0])
    assert msgs == [{"role": "user", "content": "Rule: " + RULE + "\n\nCase:\n" + CASE},
                    {"role": "assistant", "content": CARD_STEPS.replace("First [omitted]", "Prescribe cephalexin.")}]
    assert M.build_inputs(RECS[2])[0]["content"] == RECS[2]["case_text"]
    tok = AutoTokenizer.from_pretrained(released(M.HF_ID, M.REVISION, TOKENIZER_FILES))
    ids, index = M.encode(tok, msgs[0]["content"], msgs[1]["content"])
    assert tok.decode(ids, clean_up_tokenization_spaces=False) == (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\n"
        "Today Date: 26 Jul 2024\n\n<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nRule: " + RULE
        + "\n\nCase:\n" + CASE + "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        "Step 0: Let's break down this problem step by step.\n\nStep 1: Prescribe cephalexin.\n\n")
    # one <|begin_of_text|>; each step's value sits on its '\n\n'-terminated last token, Step 1's on the last token
    assert ids.count(128000) == 1 and len(index) == 2 and index[-1] == len(ids) - 1
    assert [tok.decode(ids[i]) for i in index] == [".\n\n", ".\n\n"], [tok.decode(ids[i]) for i in index]
    assert tok.pad_token_id == 128004  # <|finetune_right_pad_id|>, the pad id the official ValueModel sets


def test_score_end_to_end():
    tok_src = released(M.HF_ID, M.REVISION, TOKENIZER_FILES)
    cfg_src = released(M.BASE_ID, M.BASE_REVISION, ["config.json"])
    with tempfile.TemporaryDirectory(prefix="tiny-meds3-", ignore_cleanup_errors=True) as d:
        base, clean, pol, prm = (os.path.join(d, x) for x in ("base", "clean", "pol", "prm"))
        cfg = AutoConfig.from_pretrained(cfg_src, num_hidden_layers=2, hidden_size=64, intermediate_size=128,
                                         num_attention_heads=4, num_key_value_heads=2, head_dim=16)
        torch.manual_seed(0)
        lm = AutoModelForCausalLM.from_config(cfg, dtype=torch.float32)
        lm.save_pretrained(base)
        lm.save_pretrained(clean)
        # the base repo's own LoRA beside its full weights, with the released policy LoRA's (gated) base name
        get_peft_model(lm, LoraConfig(r=4, lora_alpha=8, target_modules=TARGETS, task_type="CAUSAL_LM",
                                      init_lora_weights=False)).save_pretrained(pol)
        shutil.copy(os.path.join(pol, "adapter_model.safetensors"), base)
        with open(os.path.join(pol, "adapter_config.json"), encoding="utf-8") as f:
            ac = json.load(f)
        with open(os.path.join(base, "adapter_config.json"), "w", encoding="utf-8") as f:
            json.dump(dict(ac, base_model_name_or_path="meta-llama/Llama-3.1-8B-Instruct"), f)
        # the PRM adapter: TOKEN_CLS LoRA + saved 2-class 'score' head, with the released tokenizer files
        tc = AutoModelForTokenClassification.from_pretrained(clean, num_labels=2)
        tc.score.bias.data = torch.tensor([0.25, -0.25])  # init leaves it 0; a dropped or flipped bias must fail
        get_peft_model(tc, LoraConfig(r=4, lora_alpha=8, target_modules=TARGETS, task_type="TOKEN_CLS",
                                      modules_to_save=["classifier", "score"],
                                      init_lora_weights=False)).save_pretrained(prm)
        for f in TOKENIZER_FILES:
            shutil.copy(os.path.join(tok_src, f), prm)

        model, tok = M.load(prm, base, device="cpu")  # default bfloat16, as on the GPU
        assert type(model).__name__ == "LlamaForTokenClassification", type(model)
        assert not any("lora" in n for n, _ in model.named_modules())
        u16 = M.score(model, tok, RECS, batch_size=2)
        assert len(u16) == len(RECS) and all(isinstance(v, float) and math.isfinite(v) and abs(v) <= 30 for v in u16)
        # float32: batched, left-padded u = log-odds of the official step value of Step 1 on base weights + PRM
        # adapter only (the base folder's own LoRA must not count), one unpadded sequence at a time
        model, tok = M.load(prm, base, device="cpu", dtype="float32")
        u = M.score(model, tok, RECS, batch_size=2)
        print("u", u, "bf16", u16)
        assert max(abs(a - b) for a, b in zip(u, u16)) < 0.02, (u, u16)  # bf16 run: same quantity (0.005 measured)
        ref = ValueModel(PeftModel.from_pretrained(AutoModelForTokenClassification.from_pretrained(clean, num_labels=2),
                                                   prm).merge_and_unload().eval())
        for rec, v in zip(RECS, u):
            msgs = M.build_inputs(rec)
            p = obtain_prm_value_for_single_pair(tok, ref, msgs[0]["content"], msgs[1]["content"], None)
            assert len(p) == 2, p
            assert abs(math.log(p[-1]) - math.log(1 - p[-1]) - v) < 1e-4, (p, v)


if __name__ == "__main__":
    test_build_inputs()
    test_score_end_to_end()
    print("ok")
