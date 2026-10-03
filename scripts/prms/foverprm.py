"""FoVer PRM (Kamoi et al., ACL 2026 Findings) used as released: FoVer's input format, the released Llama-3.1 chat
template and the model's own 'correct'/'incorrect' next-token logits at the position FoVer's extract_fover_scores
reads. One forward pass per record; u = log-odds of the PRM's P(correct)."""
from typing import Literal

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

NAME = "fover-prm"
HF_ID = "ryokamoi/Llama-3.1-8B-FoVer-PRM-2026"
REVISION = "964c5c779d8e6ee4907e2b38c914cb3972e06c36"  # HF head, re-checked 2026-10-03 UTC; llama3.1 licence, not gated
# Full fine-tune of meta-llama/Llama-3.1-8B-Instruct (card base_model): nothing is loaded under it.
BASE_ID = None
BASE_REVISION = None
CODE = "github.com/psunlpgroup/FoVer @ 6fc639c46e7c2e9a0786c10238ac8bbc2c6f287f"  # GitHub head, re-checked 2026-10-03 UTC
PROMPT_NOTE = (
    "Input is FoVer's own step format, taken from the usage example on the model card "
    "(huggingface.co/ryokamoi/Llama-3.1-8B-FoVer-PRM-2026 @ 964c5c7) and the helper it imports, get_fover_input_format "
    "(github.com/psunlpgroup/FoVer @ 6fc639c, src/prm/preprocessing.py, copied verbatim below): conversation = "
    "get_fover_input_format(problem=P, solution_steps=[claim_text]) with P = 'Rule: {rule_text}\\n\\nCase:\\n{case_text}' "
    "('{case_text}' when rule_text is empty), i.e. one user turn '** Problem **\\n{P}\\n\\n** Task **\\nYour task is to "
    "evaluate the accuracy of each step in the provided solution to the above question. For each step, respond with "
    "\"correct\" if [...] Respond with \"incorrect\" if the step includes any errors or flawed logic.\\n\\n** Sotluion "
    "**\\n{claim_text}' (sic) followed by the dummy assistant turn 'correct' that FoVer uses at inference, rendered by "
    "the released tokenizer's Llama-3.1 chat template with its defaults (no system message, so the template's own "
    "'Cutting Knowledge Date: December 2023 / Today Date: 26 Jul 2024' header; no generation prompt) and tokenized "
    "without added special tokens (the same ids as tokenizer.apply_chat_template(conversation)). Readout: FoVer's "
    "get_step_token_position (src/prm/postprocessing.py, verbatim) gives the '\\n\\n' token after "
    "'assistant<|end_header_id|>', the position whose next-token logits extract_fover_scores reads; there u = "
    "logit('correct') - logit('incorrect') (ids 20523 and 63054: the first token of each word, as in "
    "extract_fover_scores), which equals log p - log(1-p) for FoVer's score p = softmax(incorrect, correct)[correct]; "
    "computed in float32 from the final hidden state and those two lm_head rows (weights in bf16 as stored, as in the "
    "authors' own vLLM evaluation; the card's snippet would load float32 under its pinned transformers 4.50.3) and "
    "clipped to +-30. One forward pass per record; batches are right-padded "
    "(the position is found on the unpadded ids and every pad comes after it); no generation, so max_new_tokens is "
    "unused."
)


# ---- Verbatim from psunlpgroup/FoVer @ 6fc639c, src/prm/preprocessing.py (the reasoning-variant helpers omitted).
# ---- FoVer code is released under the Apache License 2.0 (repo LICENSE.md), https://www.apache.org/licenses/LICENSE-2.0
tempalte_for_first_step_of_multi_turn_data = """** Problem **
{problem}

** Task **
Your task is to evaluate the accuracy of each step in the provided solution to the above question. For each step, respond with "correct" if the reasoning is logically valid and mathematically sound, or if the step is a general statement or transition that does not contain reasoning. Respond with "incorrect" if the step includes any errors or flawed logic.

** Sotluion **
{first_step}"""
    

def get_fover_input_format(
        problem: str, solution_steps: list[str],
        reference_error_labels: list[bool] | None = None,
        user_role_name = "user", model_role_name = "assistant",
    ) -> list[dict]:
    
    # make solution steps in string
    if reference_error_labels is None:
        # this is a dummy labels we use for inference
        reference_error_labels_str = ["correct"] * len(solution_steps)
    else:
        reference_error_labels_str = [
            "correct" if label else "incorrect"
            for label in reference_error_labels
        ]
    
    # make the first step
    first_step = tempalte_for_first_step_of_multi_turn_data.format(
        problem=problem, first_step=solution_steps[0]
    )
    
    conversation = [
        {
            "role": user_role_name,
            "content": first_step
        },
        {
            "role": model_role_name,
            "content": reference_error_labels_str[0]
        }
    ]
    
    # make the rest of the steps
    for idx, step in enumerate(solution_steps[1:], start=1):
        conversation.append(
            {
                "role": user_role_name,
                "content": step
            }
        )
        
        conversation.append(
            {
                "role": model_role_name,
                "content": reference_error_labels_str[idx]
            }
        )
    
    return conversation


# ---- Verbatim from psunlpgroup/FoVer @ 6fc639c, src/prm/postprocessing.py (Apache License 2.0, as above).
def get_step_token_position(
        tokenized_prompt: np.ndarray,
        tokenizer: AutoTokenizer,
        model_type: Literal["llama", "qwen"],
    ) -> np.ndarray:
    # we get the feature for the last token in the tag for the assistant
    # conversation. It includes the prediction for the next token (the
    # first token in the assistant's response), which is the reward
    step_token_position_position_candidates = []

    # we use multiple tokens to detect the target token id because
    # target tokens can be also included in other parts
    if model_type == "llama":
        # target token id
        target_token_id = tokenizer.encode(
            "\n\n", add_special_tokens=False)[0]
        step_token_position_position_candidates.append(
            tokenized_prompt == target_token_id
        )

        # assistant id
        assistant_token_id = tokenizer.encode(
            "assistant", add_special_tokens=False)[0]
        ids = np.where(
            tokenized_prompt == assistant_token_id
        )[0] + 2
        mask = np.zeros_like(tokenized_prompt, dtype=bool)
        mask[ids] = True
        step_token_position_position_candidates.append(mask)

        # <|end_header_id|>
        end_header_id = tokenizer.encode(
            "<|end_header_id|>", add_special_tokens=False)[0]
        ids = np.where(
            tokenized_prompt == end_header_id
        )[0] + 1
        mask = np.zeros_like(tokenized_prompt, dtype=bool)
        mask[ids] = True
        step_token_position_position_candidates.append(mask)

    elif model_type == "qwen":
        # target token id
        target_token_id = tokenizer.encode(
            "\n", add_special_tokens=False)[0]
        step_token_position_position_candidates.append(
            tokenized_prompt == target_token_id
        )

        # assistant id
        assistant_token_id = tokenizer.encode(
            "assistant", add_special_tokens=False)[0]
        ids = np.where(
            tokenized_prompt == assistant_token_id
        )[0] + 1
        mask = np.zeros_like(tokenized_prompt, dtype=bool)
        mask[ids] = True
        step_token_position_position_candidates.append(mask)

        # <|im_start|>
        end_header_id = tokenizer.encode(
            "<|im_start|>", add_special_tokens=False)[0]
        ids = np.where(
            tokenized_prompt == end_header_id
        )[0] + 2
        mask = np.zeros_like(tokenized_prompt, dtype=bool)
        mask[ids] = True
        step_token_position_position_candidates.append(mask)

    else:
        raise NotImplementedError(
            f"This code does not support {model_type} model"
        )

    # take and
    step_token_position = np.where(
        np.logical_and.reduce(step_token_position_position_candidates)
    )[0]

    return step_token_position


def extract_fover_scores(tokenized_prompt: np.ndarray,
        logits: torch.Tensor, tokenizer: AutoTokenizer) -> list[float]:
    
    model_type: Literal["llama", "qwen"] | None = None
    for model_type_candidate in ["qwen", "llama"]:
        if model_type_candidate in tokenizer.name_or_path.lower():
            model_type = model_type_candidate
            break
    if model_type is None:
        raise ValueError(
            f"Cannot find model type for {tokenizer.name_or_path}"
        )
    
    # get position of the step token ("correct" or "incorrect")
    step_token_position = get_step_token_position(
        tokenized_prompt=tokenized_prompt,
        tokenizer=tokenizer,
        model_type=model_type,
    )
    selected_logits = logits[step_token_position]

    # select the logits for the step token
    positive_token_id = tokenizer.encode(
        "correct", add_special_tokens=False)[0]
    negative_token_id = tokenizer.encode(
        "incorrect", add_special_tokens=False)[0]
    
    positive_logits = selected_logits[:, positive_token_id]
    negative_logits = selected_logits[:, negative_token_id]
    
    logits_pair = torch.stack([negative_logits, positive_logits], dim=1)
    scores = torch.nn.functional.softmax(logits_pair, dim=1)[:, 1].tolist()
    
    return scores
# ---- End of the verbatim FoVer code.


def load(model_dir, base_dir=None, device="cuda", dtype="bfloat16"):
    """Full fine-tuned checkpoint, no adapter: base_dir is unused. model_dir is a local copy or HF_ID (pinned)."""
    rev = REVISION if model_dir == HF_ID else None
    tok = AutoTokenizer.from_pretrained(model_dir, revision=rev)
    model = AutoModelForCausalLM.from_pretrained(model_dir, revision=rev, dtype=getattr(torch, dtype))
    return model.to(device).eval(), tok


def build_inputs(rec):
    """The chat messages fed to apply_chat_template for one record (FoVer format, the claim as the single step)."""
    problem = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec.get("rule_text") else rec["case_text"]
    return get_fover_input_format(problem=problem, solution_steps=[rec["claim_text"]])


def score(model, tok, records, batch_size=8, max_new_tokens=None, log=print):
    """u per record, same order: logit('correct') - logit('incorrect') at FoVer's read position, clipped to +-30."""
    if not records:
        return []
    pos_id = tok.encode("correct", add_special_tokens=False)[0]  # the ids extract_fover_scores uses
    neg_id = tok.encode("incorrect", add_special_tokens=False)[0]
    # Rendered string + tokenizing without added specials = apply_chat_template's ids, on transformers 4.x and 5.x.
    ids = [tok(tok.apply_chat_template(build_inputs(r), tokenize=False), add_special_tokens=False)["input_ids"]
           for r in records]
    at = []
    for x in ids:
        p = get_step_token_position(np.array(x), tok, "llama")  # model type fixed: no guess from the directory name
        assert len(p) == 1, f"expected one FoVer read position, got {p.tolist()}"
        at.append(int(p[0]))
    x0, p0 = ids[0], at[0]
    log(f"[{NAME}] {len(ids)} records; reads after {tok.decode(x0[p0 - 2:p0 + 1])!r} (next token "
        f"{tok.decode(x0[p0 + 1:p0 + 2])!r}); correct={pos_id} incorrect={neg_id}")
    u = [0.0] * len(ids)
    order = sorted(range(len(ids)), key=lambda i: len(ids[i]))  # length-sorted batches: less padding
    dev = model.device
    with torch.inference_mode():
        # The two lm_head rows in fp32: bf16 logits are rounded to 0.125-0.25 steps at |logit| 16-64, which would
        # turn small u(s) - u(s') gaps into exact ties (ties count as failures). Same readout as medprm.py.
        head = model.lm_head.weight[[pos_id, neg_id]].float()
        for b in range(0, len(order), batch_size):
            idx = order[b:b + batch_size]
            x = torch.zeros(len(idx), max(len(ids[i]) for i in idx), dtype=torch.long)  # right padding
            m = torch.zeros_like(x)
            for j, i in enumerate(idx):
                x[j, :len(ids[i])] = torch.tensor(ids[i])
                m[j, :len(ids[i])] = 1
            h = model.model(input_ids=x.to(dev), attention_mask=m.to(dev), use_cache=False).last_hidden_state
            pair = h[torch.arange(len(idx), device=dev), torch.tensor([at[i] for i in idx], device=dev)].float() @ head.T
            for i, v in zip(idx, (pair[:, 0] - pair[:, 1]).clamp(-30, 30).tolist()):
                u[i] = v
            if (b // batch_size) % 50 == 0:
                log(f"[{NAME}] {b + len(idx)}/{len(ids)}")
    return u
