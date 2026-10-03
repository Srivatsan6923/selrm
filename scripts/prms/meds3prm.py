"""MedS3 PRM (Jiang et al., AAAI 2026) used as released: the official step-wise input built on the release's Llama-3.1
chat template, and the 2-class token-classification head of the PEFT adapter (merged into its base, as the official
loader does) read at the last token of the claim step. One forward pass per record; u = log-odds of the PRM's own
step value P(class 1)."""
import os
from itertools import chain

import torch
from peft import PeftModel
from transformers import AutoModelForTokenClassification, AutoTokenizer

NAME = "meds3-prm"
HF_ID = "pixas/MedSSS_PRM"
REVISION = "c9e78716a50f54295977ec3155d45304cad6bc02"  # HF head, re-checked 2026-10-02; MIT (card), not gated
# PEFT LoRA (TOKEN_CLS, r=32, alpha=64, modules_to_save score) whose adapter_config names this base. The base repo
# holds full bf16 weights (its training_args.bin: the "DPO-full-ITER2" run) plus its own SFT LoRA (r=16, CAUSAL_LM,
# base meta-llama/Llama-3.1-8B-Instruct); the PRM runs on the full weights only, see load().
BASE_ID = "pixas/MedSSS_Policy"
BASE_REVISION = "5025016086dd2d3e018bc84dd25de344952fec27"  # HF head, re-checked 2026-10-02; MIT (card), not gated
CODE = "github.com/pixas/MedSSS @ 82382258a963052263fc723d65ed4e9938beece0"  # GitHub head, re-checked 2026-10-02; MIT
# Step 0 of every MedS3 policy output and of every PRM training trajectory: the MCTS root step,
# Evol_Instruct/prompts/prompt_template.py mcts_prompts['break_down'] (quoted).
STEP0 = "Let's break down this problem step by step."
PROMPT_NOTE = (
    "Input is the official MedS3 PRM format, taken from obtain_prm_value_for_single_pair in the usage example of the "
    "model card (huggingface.co/pixas/MedSSS_PRM @ c9e7871; the same code is in github.com/pixas/MedSSS @ 8238225, "
    "Evol_Instruct/solver/sc_vm_solver.py, copied verbatim below) and from the PRM training code "
    "(Evol_Instruct/training/prm_train.py, format_one_item and tokenize_fn): messages [user: P, assistant: R] with "
    "P = 'Rule: {rule_text}\\n\\nCase:\\n{case_text}' ('{case_text}' when rule_text is empty) and R = 'Step 0: Let's "
    "break down this problem step by step.\\n\\nStep 1: {claim_text}', the shape of the card's step_wise_generation. "
    "The prompt is the user turn alone rendered by the release's own Llama-3.1 chat template (tokenize=False, "
    "add_generation_prompt=True, no system message, so the template trims P and inserts its 'Cutting Knowledge Date: "
    "December 2023 / Today Date: 26 Jul 2024' header): '<|begin_of_text|><|start_header_id|>system<|end_header_id|>"
    "\\n\\nCutting Knowledge Date: December 2023\\nToday Date: 26 Jul 2024\\n\\n<|eot_id|><|start_header_id|>user"
    "<|end_header_id|>\\n\\n{P}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\\n\\n'; R is split on "
    "'\\n\\nStep' and each step + '\\n\\n' is tokenized separately (add_special_tokens=False) and appended to the "
    "separately tokenized prompt, so the text is the prompt followed by 'Step 0: ...step by step.\\n\\nStep 1: "
    "{claim_text}\\n\\n'. Step 0 is the fixed MCTS root step that opens every MedS3 policy output and every PRM "
    "training trajectory (labels are put on steps >= 1 only, and the official selection rules drop the step-0 value), "
    "so the claim is the one scored step, Step 1. Readout: the official completion_index of Step 1, i.e. its last "
    "token ('\\n\\n'-terminated, the last token of the input), where the official step value is "
    "p = softmax(logits)[..., 1] of the 2-class head (card; ValueModel.forward_token in "
    "Evol_Instruct/models/modeling_value_llama.py); u = logit_1 - logit_0 = log p - log(1-p), with the released "
    "head (score weight and bias) applied in float32 to the final hidden state, clipped to +-30. Batches are "
    "left-padded with position ids restarted at each sequence's first real token, so every row matches the official "
    "unpadded call. Not generative: max_new_tokens is unused. Weights: the PRM adapter "
    "merged into the full weights of pixas/MedSSS_Policy @ 5025016 without that repo's own SFT LoRA, which the "
    "official loader attaches and then overwrites with the PRM adapter (see load()); bfloat16 by default, where the "
    "official rescoring merges in bfloat16 and then casts the model to float16 (dtype='float16' approximates that; "
    "it merges in float16)."
)


# ---- Statements copied verbatim from obtain_prm_value_for_single_pair (non-'prm-bi' branch) in pixas/MedSSS @
# ---- 8238225, Evol_Instruct/solver/sc_vm_solver.py (MIT, Copyright (c) 2025 Shuyang Jiang; same code in the model
# ---- card). Ours: the name, the signature and the return; dropped: the value_model(...) call between input_ids and
# ---- the completion_index loop and the final read, both done batched in score().
def encode(tokenizer, inputs, outputs):
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

    completion_index = []
    for i, completion in enumerate(completion_ids):
        if i == 0:
            completion_index.append(len(completion) + len(pre_response_id) - 1)
        else:
            completion_index.append(completion_index[-1] + len(completion))
    return input_ids, completion_index
# ---- End of the verbatim MedS3 code.


def load(model_dir, base_dir=None, device="cuda", dtype="bfloat16"):
    """model_dir: local copy of HF_ID (else the pinned release is downloaded); base_dir: local copy of BASE_ID (else
    its config and full weights are downloaded, pinned, without the repo's own LoRA files).

    As the official ValueModel (model_type 'prm', Evol_Instruct/models/modeling_value_llama.py): 2-label
    AutoModelForTokenClassification on the base, then the PRM adapter (LoRA + its saved 'score' head) merged in.
    If base_dir also holds the policy repo's own LoRA, transformers attaches it as adapter 'default' and the PRM
    adapter, also 'default', overwrites it, exactly as in the official loader and in the PRM training code
    (prm_train.py, trl get_peft_model on the same base): the PRM runs on the full weights only (checked on a tiny
    model in tests/test_prm_meds3prm.py). The base is never given as a hub id: transformers would then load the
    gated meta-llama base named in that LoRA's config instead of the repo's weights."""
    from huggingface_hub import snapshot_download
    if not os.path.isdir(model_dir or ""):
        model_dir = snapshot_download(HF_ID, revision=REVISION)
    if not os.path.isdir(base_dir or ""):
        base_dir = snapshot_download(BASE_ID, revision=BASE_REVISION,
                                     allow_patterns=["config.json", "model*.safetensors*"])
    tok = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForTokenClassification.from_pretrained(
        base_dir, num_labels=2, pad_token_id=tok.pad_token_id,  # 128004 <|finetune_right_pad_id|>, as ValueModel sets
        dtype=getattr(torch, dtype) if isinstance(dtype, str) else dtype, device_map=device)
    model = PeftModel.from_pretrained(model, model_dir).merge_and_unload()
    return model.eval(), tok


def build_inputs(rec):
    """The official messages [user: problem, assistant: step-wise response] for one record (one scored step)."""
    problem = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec.get("rule_text") else rec["case_text"]
    return [{"role": "user", "content": problem},
            {"role": "assistant", "content": f"Step 0: {STEP0}\n\nStep 1: {rec['claim_text']}"}]


def score(model, tok, records, batch_size=8, max_new_tokens=None, log=print):
    """u per record, same order: logit_1 - logit_0 of the 2-class head at Step 1's last token, clipped to +-30.
    The head (model.score, as in its forward; dropout is off in eval) is applied in float32 to the final hidden
    state: bf16 logits keep 8 significant bits (a 0.03 grid at |logit| 4-8), so their difference can tie s with s'."""
    W, B = model.score.weight.float(), model.score.bias.float()
    dw, db = W[1] - W[0], B[1] - B[0]
    enc = []
    for rec in records:
        msgs = build_inputs(rec)
        ids, index = encode(tok, msgs[0]["content"], msgs[1]["content"])
        assert len(index) == 2 and index[-1] == len(ids) - 1, "claim must be one step, the last one"
        enc.append(ids)
    log(f"[{NAME}] {len(enc)} records")
    u = [0.0] * len(enc)
    order = sorted(range(len(enc)), key=lambda i: len(enc[i]))  # length-sorted batches: less padding
    with torch.no_grad():
        for b in range(0, len(order), batch_size):
            idx = order[b:b + batch_size]
            width = max(len(enc[i]) for i in idx)
            ids = torch.tensor([[tok.pad_token_id] * (width - len(enc[i])) + enc[i] for i in idx], device=model.device)
            mask = torch.tensor([[0] * (width - len(enc[i])) + [1] * len(enc[i]) for i in idx], device=model.device)
            h = model.model(input_ids=ids, attention_mask=mask, position_ids=(mask.cumsum(1) - 1).clamp(min=0),
                            use_cache=False).last_hidden_state[:, -1].float()
            for i, v in zip(idx, (h @ dw + db).clamp(-30, 30).tolist()):
                u[i] = v
            if b == 0:  # ascii(): logs stay printable on a cp1252 console
                log(f"[{NAME}] reads at {tok.decode(ids[0, -6:])!a}")
            if (b // batch_size) % 50 == 0:
                log(f"[{NAME}] {b + len(idx)}/{len(enc)}")
    return u
