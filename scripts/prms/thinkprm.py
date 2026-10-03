"""ThinkPRM (Khalifa et al., 2025, arXiv 2504.16828) used as released: the official scoring prompt in the released chat
template, the verification chain generated greedily with transformers, and the official score, P(' Yes') against
P(' No') at the chain's answer to 'Is the solution correct?', read with one extra forward pass; u is its log-odds.
The model size (1.5B, 7B, 14B) is a load() argument; the audit row is 14B.

Code marked 'official' is copied or adapted from github.com/mukhal/ThinkPRM @ 045b1aed5d72301690a8fc08e846c90b757672c8
(utils/helper.py, prm/thinkprm.py), MIT License, Copyright (c) 2026 Muhammad Khalifa."""
import time

import torch
from transformers import AutoModelForCausalLM, PreTrainedTokenizerFast

NAME = "thinkprm"
SIZES = {  # HF heads re-checked 2026-10-02; apache-2.0 (cards), not gated
    "1.5B": ("launch/ThinkPRM-1.5B", "fcf2c6f6ca28ac2b901206609d8714845290f72e"),
    "7B": ("launch/ThinkPRM-7B", "b61c5be0cfaa4b2851590c0e99a514e1f8379312"),
    "14B": ("launch/ThinkPRM-14B", "1d1b415037cccf826fab6cc1b02c1dac199c0c0f"),
}
HF_ID, REVISION = SIZES["14B"]
# Full fine-tunes of deepseek-ai/DeepSeek-R1-Distill-Qwen-{1.5B,7B,14B} (cards): nothing is loaded under them.
BASE_ID = None
BASE_REVISION = None
CODE = "github.com/mukhal/ThinkPRM @ 045b1aed5d72301690a8fc08e846c90b757672c8"  # head, re-checked 2026-10-02
MAX_NEW_TOKENS = 2048
PROMPT_NOTE = (
    "Input is the official scoring prompt, format_verification_cot_for_thinkprm (github.com/mukhal/ThinkPRM @ 045b1ae, "
    "utils/helper.py, 'main template used in the paper'), which both of the repo's scoring classes use: ThinkPRM "
    "(prm/thinkprm.py, the README's Basic Usage) and APIThinkPRMVerifier (prm/thinkprm_api.py, the test-time-scaling "
    "runs). One user turn 'You are given a math problem and a proposed step-by-step solution:\\n\\n[Math Problem]\\n\\n"
    "{problem}\\n\\n[Solution]\\n\\n{solution}\\n\\nReview and critique each step in the proposed solution to determine "
    "whether each step is correct. If the solution is incomplete, only verify the provided steps.' in the released "
    "chat template with add_generation_prompt=True, so the text ends '<｜Assistant｜><think>\\n'; problem = 'Rule: "
    "{rule_text}\\n\\nCase:\\n{case_text}' ('{case_text}' when rule_text is empty) and solution = 'Step 1: "
    "{claim_text}' (the official process_example). Tokenized as the repo's pinned vLLM 0.6.4.post1 does it "
    "(tokenizer.encode(text) puts a BOS before the template's BOS: two BOS tokens). Not the model card's quick-start "
    "variant (instruction without the final '.', then \"\\nLet's verify step by step:\" after the template): after the "
    "template's '<think>\\n' it makes '<think>\\n\\n', and on ThinkPRM-1.5B (greedy, 12 rule_v1 dev and 4 MedEinst "
    "reference records) 7 of 16 chains were empty and 2 more were one line, against none with the repo prompt (with "
    "it, 26 of 28 such records ended with the verdict line within 2048 tokens, 2 were forced at the cap). Decoding "
    "is greedy (the card's temperature 0.0) for at most max_new_tokens new tokens, 2048 by default (the card's "
    "max_tokens and the class's max_length are 4096; 2048 covers 96% of the 1,000 released training chains, "
    "launch/thinkprm-1K-verification-cots @ c0b1da4, and 89% of its 26 one-step chains). Score as in the official "
    "ThinkPRM.predict_correctness_batch: every generated ' Yes' or ' No' token (ids 7414, 2308) is a decision on 'Is "
    "the solution correct?', and the last one gives the prefix score p = P(' Yes') / (P(' Yes') + P(' No')) at "
    "decision_temperature 1.0; u = log p - log(1-p) = logit(' Yes') - logit(' No') at that position, read with one "
    "extra left-padded forward pass over the prompt and the chain before that token, in float32 from the bf16 final "
    "hidden state, clipped to +-30. A chain that reaches the budget (where the official class, with its larger budget, "
    "would read its last ' Yes'/' No' wherever it stands) or that ends without such a token (the official class "
    "returns -1) gets the official forced verdict of ThinkPRM.predict_correctness_batch_sequential_scaling, emulated "
    "on the same greedy chain: the chain stops at the first 'Is the solution correct?' in its text (that path's vLLM "
    "stop string), a finished chain keeps its EOS id (vLLM's token_ids do), the string is appended unless the ids end "
    "with its last 3 ids, and u is read at the next token over the prompt re-tokenized without special tokens (one "
    "BOS, as that path's decision call has it); the number of forced verdicts is logged."
)

CORRECT, INCORRECT = " Yes", " No"  # official: ThinkPRM.correct_token / incorrect_token, "for the whole prefix"
PREDECISION = "Is the solution correct?"  # official: predict_correctness_batch_sequential_scaling
LAST_OUTPUTS = []  # generated chain per record of the last score() call, same order (keep as reader output)

# ---- Official, verbatim from utils/helper.py, format_verification_cot_for_thinkprm: its default instruction and its
# ---- template. build_inputs fills the template as the helper does; score() renders it with the helper's
# ---- apply_chat_template call (split because build_inputs gets no tokenizer).
_instruction = "Review and critique each step in the proposed solution to determine whether each step is correct. If the solution is incomplete, only verify the provided steps." ## default instruction (models were trained with this)

instruction_template = """You are given a math problem and a proposed step-by-step solution:

[Math Problem]

{problem}

[Solution]

{solution}

{_instruction}
""".strip()


def build_inputs(rec):
    """The chat messages of the official format_verification_cot_for_thinkprm for one record."""
    problem = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec.get("rule_text") else rec["case_text"]
    solution = f"Step 1: {rec['claim_text']}\n".strip()  # official process_example: f'Step {sdx+1}: {step}\n', strip()
    return [
        {'role': "user", "content": instruction_template.replace('{problem}', problem).replace('{solution}', solution).replace('{_instruction}', _instruction)}
    ]


def load(model_dir=None, base_dir=None, device="cuda", dtype="bfloat16", size="14B"):
    """model_dir: local copy of a ThinkPRM checkpoint; None loads launch/ThinkPRM-<size> at its pinned revision.
    Full fine-tune, no adapter: base_dir is unused. The tokenizer is read from tokenizer.json as
    PreTrainedTokenizerFast: the declared tokenizer_class 'LlamaTokenizer' drops spaces under transformers 5 when no
    config.json sits next to it (' Yes' -> 'Yes'), so the declared class is not used and a round trip is checked."""
    src, rev = (model_dir, None) if model_dir else SIZES[size]
    tok = PreTrainedTokenizerFast.from_pretrained(src, revision=rev)
    probe = PREDECISION + CORRECT
    assert tok.decode(tok.encode(probe, add_special_tokens=False)) == probe, "tokenizer does not round-trip"
    assert all(len(tok.encode(t, add_special_tokens=False)) == 1 for t in (CORRECT, INCORRECT))
    model = AutoModelForCausalLM.from_pretrained(src, revision=rev, dtype=getattr(torch, dtype), device_map=device)
    return model.eval(), tok


def _encode(tok, messages):
    """Ids of the rendered prompt as vLLM 0.6.4.post1 makes them from text: tokenizer.encode(text) adds a BOS before
    the template's own."""
    text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)  # official
    return [tok.bos_token_id] + tok.encode(text, add_special_tokens=False)


def _pad(seqs, pad_id, device):
    """Left padding: the last position of every row is its last token."""
    n = max(map(len, seqs))
    ids = torch.tensor([[pad_id] * (n - len(s)) + s for s in seqs], device=device)
    mask = torch.tensor([[0] * (n - len(s)) + [1] * len(s) for s in seqs], device=device)
    return ids, mask


def _verdict_tail(chain, finished, yes, no, pre, decode):
    """(generated ids up to the verdict position, forced?). chain holds the generated ids as vLLM returns them: a
    finished chain ends with its EOS. A finished chain is read at its last ' Yes'/' No' (official
    _extract_score_from_logprobs: a position whose top token is ' Yes' or ' No' is a decision, and 'the last step
    score is the full prefix score'; greedy, so the top token is the generated one). A chain cut by the budget, or
    one without a decision, is forced as the official sequential-scaling path does it on the same greedy chain:
    generation stops at the first 'Is the solution correct?' in the text (vLLM stop string, matched on the
    detokenized text), and the ids, EOS included, get the string appended unless they end with its last 3 ids."""
    pos = [p for p, t in enumerate(chain) if t in (yes, no)] if finished else []
    if pos:
        return chain[:pos[-1]], False
    if PREDECISION in decode(chain):  # official stop string: cut after the first token that completes it
        lo, hi = 1, len(chain)
        while lo < hi:
            mid = (lo + hi) // 2
            lo, hi = (lo, mid) if PREDECISION in decode(chain[:mid]) else (mid + 1, hi)
        chain = chain[:lo]
    if pre[-3:] != chain[-3:]:  # official: add predecision string if not already present
        chain = chain + pre
    return chain, True


def _logodds(model, seqs, pad_id, w):
    """logit(' Yes') - logit(' No') for the token after each sequence, one left-padded forward pass; float32 from the
    final hidden state, since bf16 logits sit on a coarse grid that makes exact ties."""
    ids, mask = _pad(seqs, pad_id, model.device)
    h = model.model(input_ids=ids, attention_mask=mask, position_ids=(mask.cumsum(-1) - 1).clamp(min=0),
                    use_cache=False).last_hidden_state[:, -1]
    return (h.float() @ w).clamp(-30, 30).tolist()


@torch.no_grad()
def score(model, tok, records, batch_size=8, max_new_tokens=None, log=print):
    """u per record, same order: logit(' Yes') - logit(' No') at the verdict, clipped to +-30. The chains of this call
    are left in LAST_OUTPUTS (a finished chain ends with the EOS text; a forced verdict's chain ends with 'Is the
    solution correct?')."""
    cap = max_new_tokens or MAX_NEW_TOKENS
    yes, no = (tok.encode(t, add_special_tokens=False)[-1] for t in (CORRECT, INCORRECT))  # official
    pre = tok.encode(PREDECISION, add_special_tokens=False)
    head = model.get_output_embeddings().weight
    w = head[yes].float() - head[no].float()
    prompts = [_encode(tok, build_inputs(r)) for r in records]
    order = sorted(range(len(records)), key=lambda i: len(prompts[i]))  # less padding
    u, outs, new, forced, t0 = [0.0] * len(records), [None] * len(records), 0, 0, time.time()
    for k in range(0, len(order), batch_size):
        b = order[k:k + batch_size]
        ids, mask = _pad([prompts[i] for i in b], tok.pad_token_id, model.device)
        gen = model.generate(input_ids=ids, attention_mask=mask, max_new_tokens=cap, do_sample=False,
                             temperature=None, top_p=None, top_k=None, pad_token_id=tok.pad_token_id,
                             eos_token_id=tok.eos_token_id)[:, ids.shape[1]:].tolist()
        seqs = []
        for i, g in zip(b, gen):
            finished = tok.eos_token_id in g
            chain = g[:g.index(tok.eos_token_id) + 1] if finished else g  # vLLM's token_ids keep the EOS
            tail, f = _verdict_tail(chain, finished, yes, no, pre, tok.decode)
            # official forced decision: prompt text re-tokenized with add_special_tokens=False, so one BOS, not two
            seqs.append((prompts[i][1:] if f else prompts[i]) + tail)
            outs[i] = tok.decode(tail if f else chain)
            new, forced = new + len(chain), forced + f
        for i, x in zip(b, _logodds(model, seqs, tok.pad_token_id, w)):
            u[i] = x
        log(f"[{NAME}] {k + len(b)}/{len(records)} records, {new} new tokens ({new / max(time.time() - t0, 1e-6):.0f}/s), "
            f"forced verdicts {forced}")
    LAST_OUTPUTS[:] = outs
    return u
