"""Med-PRM (Yun et al., EMNLP 2025) used as released: the model card's input template, the released Llama-3.1 chat
template and the model's own '+'/'-' logits at the step marker ' ки', where the card and the official scoring code
read the step reward. One forward pass per record; u = log-odds of the PRM's P('+')."""
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

NAME = "med-prm"
HF_ID = "dmis-lab/llama-3.1-medprm-reward-v1.0"
REVISION = "6948b9e942fa0275dff8ff902a1833f1298974d4"  # HF head, re-checked 2026-10-03 UTC; MIT (card), not gated
# Full fine-tune of meta-llama/Llama-3.1-8B-Instruct (repo scripts/2_training.sh): nothing is loaded under it.
BASE_ID = None
BASE_REVISION = None
CODE = "github.com/eth-medical-ai-lab/Med-PRM @ 3a7256faf0af185f4a36a4f3503775c056afc29f"  # head, re-checked 2026-10-03 UTC
PROMPT_NOTE = (
    "Input is the template of the model card's Quick Start (huggingface.co/dmis-lab/llama-3.1-medprm-reward-v1.0 @ "
    "6948b9e), which is also the RAG mode of the official scorer (github.com/eth-medical-ai-lab/Med-PRM @ 3a7256f, "
    "python/4_scoring_PRM.py) and the mode the released model was trained in (scripts/2_training.sh, use_rag=yes): "
    "messages [system: the card's system_prompt verbatim, 'You are an evaluator assessing the logicality and validity "
    "of the reasoning in each step of the given explanation. In order to support the evaluation, the relevant "
    "documents, the question, and the explanation are provided sequentially. If the reasoning contains errors, output "
    "- after that step. If the reasoning in a step is logical and valid, output + after that step. '; user: the card's "
    "f\"{doc_block}Question: {question}\\n\\nExplanation: {explanation}\"] with question = 'Rule: {rule_text}\\n\\n"
    "Case:\\n{case_text}' ('{case_text}' when rule_text is empty) and explanation = 'Step 1: {claim_text} ки', i.e. "
    "the official prm_process_solution (python/3_test_dataset_sampling.py, copied verbatim below) applied to a one-step "
    "solution in the 'Step {number}:' format that the policy prompt imposes on every Med-PRM solution; ' ки' is the "
    "added step token (id 128256). The one deviation: no retrieval, so doc_block = '' (the card joins 'Document k: "
    "...' passages there; the system prompt is kept as released). Rendered with the released tokenizer's Llama-3.1 "
    "chat template (tokenize=False, add_generation_prompt=True; the template trims both contents and inserts its "
    "'Cutting Knowledge Date: December 2023 / Today Date: 26 Jul 2024' header) and tokenized with "
    "add_special_tokens=True as the card and the official get_prob do, so the ids start with two <|begin_of_text|>. "
    "Readout: logits of ' +' (489) and ' -' (482), the ids tokenizer(' +' / ' -', add_special_tokens=False)[0] as in "
    "the card, at the position of the step's ' ки' token, the position get_prob reads; u = logit(' +') - "
    "logit(' -'), which equals log p - log(1-p) for the card's step reward p = softmax(+, -)[+]; the two logits are "
    "computed in float32 from the bf16 final hidden state and u is clipped to +-30. Batches are right-padded (the "
    "marker is not the last token, so every read position keeps its unpadded index). Not generative: max_new_tokens "
    "is unused. Attention is the transformers default (sdpa) instead of the official flash_attention_2."
)

# Quoted from the model card's Quick Start (MIT); identical to RAG_SYSTEM_PROMPT in python/4_scoring_PRM.py.
SYSTEM_PROMPT = (
        "You are an evaluator assessing the logicality and validity of the reasoning in each step of the given explanation. "
        "In order to support the evaluation, the relevant documents, the question, and the explanation are provided sequentially. "
        "If the reasoning contains errors, output - after that step. If the reasoning in a step is logical and valid, output + after that step. "
)
STEP_TAG = " ки"


# ---- Verbatim from eth-medical-ai-lab/Med-PRM @ 3a7256f, python/3_test_dataset_sampling.py. The repository has no
# ---- LICENSE file (re-checked 2026-10-03 UTC); the released model is MIT per its card.
STEP_PATTERN = r'(?:## )?Step \d+:'

def prm_process_solution(txt: str):
    no_nl = txt.replace("\n", " ")
    mts = list(re.finditer(STEP_PATTERN, no_nl))
    if not mts:
        return no_nl.strip() + " ки" if no_nl.strip() else ""
    head = no_nl[:mts[0].start()].strip()
    steps = []
    for i, m in enumerate(mts):
        start = m.start()
        end   = mts[i+1].start() if i+1 < len(mts) else len(no_nl)
        steps.append(no_nl[start:end].strip().replace("## ", "") + " ки")
    if head:
        steps.insert(0, head)
    return " ".join(steps)
# ---- End of the verbatim Med-PRM code.


def load(model_dir, base_dir=None, device="cuda", dtype="bfloat16"):
    """Full fine-tuned checkpoint, no adapter: base_dir is unused. model_dir is a local copy or HF_ID (pinned)."""
    rev = REVISION if model_dir == HF_ID else None
    tok = AutoTokenizer.from_pretrained(model_dir, revision=rev)
    # straight onto the device: an 8B bf16 copy in host memory would exceed the runner pod's 12 GiB
    model = AutoModelForCausalLM.from_pretrained(model_dir, revision=rev, dtype=getattr(torch, dtype), device_map=device)
    return model.eval(), tok


def build_inputs(rec):
    """The chat messages fed to apply_chat_template for one record (card template, no documents, one step)."""
    question = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec.get("rule_text") else rec["case_text"]
    explanation = prm_process_solution(f"Step 1: {rec['claim_text']}")
    doc_block = ""  # the one deviation: no retrieved documents
    user_content = f"{doc_block}Question: {question}\n\nExplanation: {explanation}"
    return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_content}]


def score(model, tok, records, batch_size=8, max_new_tokens=None, log=print):
    """u per record, same order: logit(' +') - logit(' -') at the step's ' ки' token, clipped to +-30."""
    if not records:
        return []
    plus_id = tok(" +", add_special_tokens=False)["input_ids"][0]  # as in the card and the official get_prob
    minus_id = tok(" -", add_special_tokens=False)["input_ids"][0]
    tag_id = tok.convert_tokens_to_ids(STEP_TAG)
    head = model.lm_head.weight[[plus_id, minus_id]].float()
    raws = [tok.apply_chat_template(build_inputs(r), tokenize=False, add_generation_prompt=True) for r in records]
    log(f"[{NAME}] {len(raws)} records; ' +'={plus_id} ' -'={minus_id} step tag={tag_id}")
    u = [0.0] * len(raws)
    order = sorted(range(len(raws)), key=lambda i: len(raws[i]))  # length-sorted batches: less padding
    with torch.no_grad():
        for b in range(0, len(order), batch_size):
            idx = order[b:b + batch_size]
            enc = tok([raws[i] for i in idx], add_special_tokens=True, padding=True, padding_side="right",
                      return_tensors="pt").to(model.device)
            ids = enc["input_ids"]
            is_tag = ids == tag_id
            assert is_tag.any(1).all(), "step marker ' ки' missing"
            pos = (is_tag * torch.arange(ids.shape[1], device=ids.device)).argmax(1)  # last marker = the step's
            h = model.model(input_ids=ids, attention_mask=enc["attention_mask"], use_cache=False).last_hidden_state
            pair = h[torch.arange(len(idx), device=h.device), pos].float() @ head.T  # logits of ' +', ' -'
            for i, v in zip(idx, (pair[:, 0] - pair[:, 1]).clamp(-30, 30).tolist()):
                u[i] = v
            if b == 0:  # ascii(): logs stay printable on a cp1252 console
                log(f"[{NAME}] reads at {tok.decode(ids[0, pos[0] - 3:pos[0] + 1])!a} "
                    f"(next {tok.decode(ids[0, pos[0] + 1:pos[0] + 6])!a})")
            if (b // batch_size) % 50 == 0:
                log(f"[{NAME}] {b + len(idx)}/{len(raws)}")
    return u
