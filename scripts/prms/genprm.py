"""GenPRM-7B (Zhao et al., 2025) used as released: the official repository's process-supervision call for one
paragraph (critique in <analyze>, Python check in <verify> that is executed and its output appended, verdict in
<output>), generated greedily with transformers; the official reward, P('Yes') against P('No') at the verdict token,
is read with one extra forward pass and u is its log-odds.

Code marked 'official' is copied or adapted from github.com/RyanLiu112/GenPRM @ a08da3f6b636be370e0d53f9bdbdc455cdece939
(src/prm_evaluation/genprm_inference.py, src/utils/util.py), MIT License, Copyright (c) 2025 GenPRM Team."""
import concurrent.futures
import json
import re
import subprocess
import sys
import tempfile
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList

NAME = "genprm-7b"
HF_ID = "GenPRM/GenPRM-7B"
REVISION = "0ea3fa755896b5448a33458fd0b010501dbea21e"  # HF head, re-checked 2026-10-02; MIT (card), not gated
# Full fine-tune of deepseek-ai/DeepSeek-R1-Distill-Qwen-7B (card metadata): nothing is loaded under it.
BASE_ID = None
BASE_REVISION = None
CODE = "github.com/RyanLiu112/GenPRM @ a08da3f6b636be370e0d53f9bdbdc455cdece939"  # head, re-checked 2026-10-02
MAX_TOKENS = 2048  # official max_tokens: GenPRM.inference default, and the value prm_evaluate.py passes
PROMPT_NOTE = (
    "Input is the official process-supervision call for paragraph 1, GenPRM.inference(messages, cur_step=1, "
    "code_executor=CodeExecutor()) with its defaults (github.com/RyanLiu112/GenPRM @ a08da3f, "
    "src/prm_evaluation/genprm_inference.py, as in the README quick start and src/example/demo.ipynb): messages "
    "[system 'You are a math teacher. Your task is to review and critique the paragraphs in solution step by step.', "
    "user 'Question: {problem}\\n\\n{step}'], the format of the model card (huggingface.co/GenPRM/GenPRM-7B @ "
    "0ea3fa7) and of the demo, with problem = 'Rule: {rule_text}\\n\\nCase:\\n{case_text}' ('{case_text}' when "
    "rule_text is empty) and step = claim_text. The prompt is the official build_prompt (released chat template with "
    "add_generation_prompt=False: the text ends with the user turn and has no Assistant tag, as the demo's printed "
    "requests show; the card's own snippet uses add_generation_prompt=True but reads no verdict), tokenized as the "
    "pinned vLLM 0.7.1 does it (tokenizer.encode puts a BOS before the template's BOS: two BOS tokens). The model "
    "then continues the official stage templates: '<analyze>\\nLet's analyze the Paragraph 1 step by step: ' until "
    "'</analyze>\\n'; then '<verify>\\nLet's use python code to find any potential error:\\n```python\\n' until "
    "'\\n```\\n' or '</output>\\n'; when such a call ends any other way than '</output>\\n', the last ```python block "
    "of the critique is executed and '[Code Output]\\n\\n```\\n{output}\\n```\\n' appended, for up to 3 rounds; when "
    "the rounds or the budget run out, the analysis is kept and '<output>\\n**Judgement**: $\\\\boxed' is continued "
    "for 20 tokens. Budget: max_new_tokens defaults to 2048, the official max_tokens (GenPRM.inference default and "
    "the value prm_evaluate.py passes); it caps the analysis call and all assistant-side text including code outputs, "
    "so a record generates at most about 2,048 + 20 tokens (the card's 8,192 belongs to its single free-running "
    "call). Decoding is greedy "
    "(deviation from the card's and the repo's temperature 0.6, top_p 0.95, top_k 20 sampling, for determinism). Code "
    "runs in a fresh subprocess of the same Python (any installed import, as the official in-process exec allows), "
    "with the record's earlier blocks replayed first to rebuild the namespace the official executor shares between "
    "blocks, under one limit of 5 s x blocks (CodeExecutor: 5 s per block), at most 2 subprocesses at a time."
)

# ---- Official constants: genprm_inference.py (GenPRM.inference defaults with cur_step=1, CodeExecutor) and the
# ---- analyze/verify system prompt of prm_evaluate.py (identical to the card's and the demo's).
SYSTEM = "You are a math teacher. Your task is to review and critique the paragraphs in solution step by step."
ANALYZE_START = "<analyze>\nLet's analyze the Paragraph {cur_step} step by step: ".format(cur_step=1)
VERIFY_START = "<verify>\nLet's use python code to find any potential error:\n```python\n"
OUTPUT_START = "<output>\n**Judgement**: $\\boxed"
TIME_LIMIT = 3  # verify-stage generation rounds
FALLBACK_TOKENS = 20
EXEC_SECONDS = 5  # CodeExecutor: timeout(seconds=5) per block
# ponytail: children run 2 at a time, the runner pods' CPU limit (scripts/submit_c.py). The official executor runs
# blocks one at a time in a warm process. A child per record of a batch at once (8 cold 'import sympy' children on
# 2 CPUs took 4.2 s of the 5 s) pushes blocks into spurious time-outs. Raise it with the pod's CPU limit.
EXEC_WORKERS = 2
CODE_PATTERN = re.compile(r'```python\s*(.*?)\s*```', re.DOTALL)

LAST_OUTPUTS = []  # assistant-side critique per record of the last score() call, same order (keep as reader output)


def build_prompt(messages, tokenizer):  # official, verbatim from src/utils/util.py
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    if prompt.endswith(f"{tokenizer.eos_token}\n"):
        prompt = prompt[:-len(f"{tokenizer.eos_token}\n")]
    elif prompt.endswith(tokenizer.eos_token):
        prompt = prompt[:-len(tokenizer.eos_token)]
    return prompt


def load(model_dir, base_dir=None, device="cuda", dtype="bfloat16"):
    """Full fine-tuned checkpoint, no adapter: base_dir is unused. model_dir is a local copy or HF_ID (pinned)."""
    rev = REVISION if model_dir == HF_ID else None
    tok = AutoTokenizer.from_pretrained(model_dir, revision=rev)
    probe = "Question: Rule: a b\n\nCase:\n  c."  # transformers 5 reads the declared 'LlamaTokenizer' (byte-level BPE)
    assert tok.decode(tok.encode(probe, add_special_tokens=False)) == probe, \
        "tokenizer drops spaces: load it from a directory that has the released config.json"
    model = AutoModelForCausalLM.from_pretrained(model_dir, revision=rev, dtype=getattr(torch, dtype))
    return model.to(device).eval(), tok


def build_inputs(rec):
    """The chat messages for one record; build_prompt(messages) + ANALYZE_START is the text the model continues."""
    problem = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec.get("rule_text") else rec["case_text"]
    return [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Question: {problem}\n\n{rec['claim_text']}"}]


# Child process: the body of the official CodeExecutor.execute, run over the record's earlier blocks (replayed to
# rebuild the namespace the official executor keeps) and then the new block; it reports the last block's output.
_CHILD = r'''
import io, json, sys
from contextlib import redirect_stdout
namespace = {}
for code_block in json.loads(sys.stdin.read()):
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(code_block, namespace)
        actual = f.getvalue().strip()
    except BaseException as e:  # official: Exception (a SystemExit there ends the whole evaluation)
        actual = f"Code execute Error: {type(e).__name__}: {e}"
sys.__stdout__.write("\n@@GENPRM@@" + json.dumps(actual))
'''


def _run_code(blocks, seconds=EXEC_SECONDS):
    """Output of the last block, as the official executor words it. ponytail: one timeout of seconds x blocks for
    the replay instead of SIGALRM's 5 s per block (POSIX-only); a block that timed out is never replayed."""
    with tempfile.TemporaryDirectory(prefix="genprm-exec-", ignore_cleanup_errors=True) as cwd:
        try:
            r = subprocess.run([sys.executable, "-c", _CHILD], input=json.dumps(blocks), capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=seconds * len(blocks), cwd=cwd)
        except subprocess.TimeoutExpired:
            return "Code execute time out: Code execution timed out"
    _, mark, out = r.stdout.rpartition("\n@@GENPRM@@")
    return json.loads(out) if mark else f"Code execute Error: exit code {r.returncode}"


def _execute(done, text):
    """Official CodeExecutor.execute(text) for one record; done = its earlier blocks, extended in place."""
    try:
        code_block = CODE_PATTERN.findall(text)[-1].strip()
    except IndexError:
        return "Code format error: No code found."
    actual = _run_code(done + [code_block])
    if not actual.startswith("Code execute time out"):
        done.append(code_block)
    return actual


def _encode(tok, text):
    """Ids as the pinned vLLM 0.7.1 makes them from a text prompt: tokenizer.encode(text) prepends BOS although the
    chat template already starts with it, so the official input begins with two BOS tokens."""
    return [tok.bos_token_id] + tok(text, add_special_tokens=False)["input_ids"]


def _pad(seqs, pad_id, device):
    """Left padding: the last position of every row is its last token."""
    n = max(map(len, seqs))
    ids = torch.tensor([[pad_id] * (n - len(s)) + s for s in seqs], device=device)
    mask = torch.tensor([[0] * (n - len(s)) + [1] * len(s) for s in seqs], device=device)
    return ids, mask


class _Stop(StoppingCriteria):
    """vLLM's stop semantics: a stop string counts only inside the generated text; plus a token budget per row."""

    def __init__(self, tok, stops, start, budgets):
        self.tok, self.stops, self.start, self.budgets = tok, stops, start, budgets

    def __call__(self, input_ids, scores, **kwargs):
        new = input_ids[:, self.start:]
        tails = self.tok.batch_decode(new[:, -12:])  # the stop strings are ASCII, at most 10 characters
        return torch.tensor([new.shape[1] >= b or any(s in t for s in self.stops)
                             for t, b in zip(tails, self.budgets)], device=input_ids.device)


def _generate(model, tok, texts, stops, budgets):
    """Greedy continuation of each text: (text, generated ids) per row. The text is decoded without special tokens
    and cut after the first stop string found, as vLLM does with include_stop_str_in_output=True."""
    ids, mask = _pad([_encode(tok, t) for t in texts], tok.pad_token_id, model.device)
    start = ids.shape[1]
    with torch.inference_mode():
        out = model.generate(input_ids=ids, attention_mask=mask, max_new_tokens=max(budgets), do_sample=False,
                             temperature=None, top_p=None, top_k=None, use_cache=True,
                             pad_token_id=tok.pad_token_id, eos_token_id=tok.eos_token_id,
                             stopping_criteria=StoppingCriteriaList([_Stop(tok, stops, start, budgets)]))
    res = []
    for row in out[:, start:].tolist():
        for t in (tok.eos_token_id, tok.pad_token_id):
            row = row[:row.index(t)] if t in row else row
        text = tok.decode(row, skip_special_tokens=True)
        for s in stops:
            if s in text:
                text = text[:text.index(s) + len(s)]
                break
        res.append((text, row))
    return res


def _critique(model, tok, prompts, max_tokens):
    """Official GenPRM._single_inference (analyze, verify, execute; time_limit 3) for a batch in lockstep, greedy.
    Returns per record (assistant text before the final call, text of the final call, its generated ids)."""
    n = len(prompts)
    out1 = [t for t, _ in _generate(model, tok, [p + ANALYZE_START for p in prompts], ["</analyze>\n"],
                                    [max_tokens] * n)]
    cur = [ANALYZE_START + t + VERIFY_START for t in out1]
    final, blocks = [None] * n, [[] for _ in range(n)]
    for cur_time in range(TIME_LIMIT + 1):
        todo = [i for i in range(n) if final[i] is None]
        if not todo:
            break
        left = {i: max_tokens - len(tok.tokenize(cur[i])) for i in todo}
        normal = [i for i in todo if left[i] > 0 and cur_time < TIME_LIMIT]
        fallback = [i for i in todo if i not in normal]
        for i in fallback:  # official: degrade into analyze mode
            cur[i] = ANALYZE_START + out1[i].split('</analyze>')[0] + '</analyze>\n' + OUTPUT_START
        gen = {}
        if normal:
            gen.update(zip(normal, _generate(model, tok, [prompts[i] + cur[i] for i in normal],
                                             ["\n```\n", "</output>\n"], [left[i] for i in normal])))
        if fallback:
            gen.update(zip(fallback, _generate(model, tok, [prompts[i] + cur[i] for i in fallback],
                                               ["</output>\n"], [FALLBACK_TOKENS] * len(fallback))))
        # ponytail: the official loop repeats a fallback call until it ends with '</output>\n'; greedy decoding would
        # repeat it verbatim forever, so the first fallback call is final.
        for i in fallback + [i for i in normal if gen[i][0].endswith("</output>\n")]:
            final[i] = (cur[i], *gen[i])
        run = [i for i in normal if final[i] is None]
        if run:
            with concurrent.futures.ThreadPoolExecutor(EXEC_WORKERS) as ex:
                outs = list(ex.map(lambda i: _execute(blocks[i], cur[i] + gen[i][0]), run))
            for i, code_output in zip(run, outs):
                cur[i] += gen[i][0] + f"[Code Output]\n\n```\n{code_output}\n```\n"
    return final


def _verdict_logodds(model, tok, items, log=print):
    """Official get_reward_score: the decision is the first '(Yes|No)}' in the critique and is read at the last token
    of that word among the final call's generated ids, p = P(Yes) / (P(Yes) + P(No)) there. Here from the full logits
    of one left-padded forward pass over (final call's prompt ids + generated ids before that token):
    u = logit(Yes) - logit(No) = log p - log(1 - p), clipped to +-30. items: (prompt ids, ids, critique) per record."""
    yes_token = tok.encode('Yes')[-1]  # official
    no_token = tok.encode('No')[-1]
    u, ctx = [0.0] * len(items), {}
    for j, (prompt_ids, tokens, generated_text) in enumerate(items):
        boxed_match = re.search(r'(Yes|No)\}', generated_text, re.IGNORECASE)  # official
        if not boxed_match:
            log(f"[{NAME}] no boxed Yes/No in the critique: u = 0 (official reward 0.5)")
            continue
        token = yes_token if boxed_match.group(1).capitalize() == "Yes" else no_token
        if token not in tokens:  # the official tokens[::-1].index(...) raises here
            log(f"[{NAME}] verdict {boxed_match.group(1)!a} is not a generated token of the final call: u = 0")
            continue
        ctx[j] = prompt_ids + tokens[:len(tokens) - 1 - tokens[::-1].index(token)]  # official index
    if ctx:
        ids, mask = _pad(list(ctx.values()), tok.pad_token_id, model.device)
        with torch.inference_mode():
            logits = model(input_ids=ids, attention_mask=mask, position_ids=(mask.cumsum(-1) - 1).clamp(min=0),
                           logits_to_keep=1).logits[:, -1].float()
        for j, d in zip(ctx, (logits[:, yes_token] - logits[:, no_token]).clamp(-30, 30).tolist()):
            u[j] = d
    return u


def score(model, tok, records, batch_size=8, max_new_tokens=None, log=print):
    """u per record, same order: logit('Yes') - logit('No') at the official verdict token, clipped to +-30; 0 (a tie)
    when the critique has no verdict. max_new_tokens = the official max_tokens budget (default 2048). The critiques
    of this call are left in LAST_OUTPUTS."""
    max_tokens = max_new_tokens or MAX_TOKENS
    LAST_OUTPUTS.clear()
    u, t0 = [], time.time()
    for b in range(0, len(records), batch_size):
        prompts = [build_prompt(build_inputs(r), tok) for r in records[b:b + batch_size]]
        final = _critique(model, tok, prompts, max_tokens)
        u += _verdict_logodds(model, tok, [(_encode(tok, p + c), ids, c + t) for p, (c, t, ids) in zip(prompts, final)],
                              log)
        LAST_OUTPUTS.extend(c + t for c, t, _ in final)
        if b == 0:  # ascii(): logs stay printable on a cp1252 console
            log(f"[{NAME}] first record, model input: {prompts[0] + ANALYZE_START!a}")
            log(f"[{NAME}] critique: {LAST_OUTPUTS[0][len(ANALYZE_START):]!a}; u = {u[0]:.3f}")
        log(f"[{NAME}] {len(u)}/{len(records)} records, {time.time() - t0:.0f}s")
    return u
