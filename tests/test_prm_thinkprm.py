"""CPU check of scripts/prms/thinkprm.py. Run: python tests/test_prm_thinkprm.py
(a) build_inputs, rendered, against the official usage example (the README's Basic Usage: ThinkPRM.process_example
and format_verification_cot_for_thinkprm, copied verbatim) at string level with the tokenizer class load() uses, and
the prompt ids against the raw tokenizers library on the released tokenizer.json with the BOS that vLLM 0.6.4.post1
adds; (b) the forced verdict against vLLM's stop-string semantics; (c) load() + score() end to end on a tiny random
Qwen2ForCausalLM (2 layers, hidden 64) saved with the released tokenizer and generation-config files: greedy despite
the released sampling defaults, and with scripted chains the read-out (last ' Yes'/' No' of a finished chain; forced
verdict of a cut chain and of a finished chain without a decision, one BOS) against an unpadded forward pass.
Downloads the released tokenizer/config files only, never the weights."""
import json, math, os, shutil, sys, tempfile

import torch
from huggingface_hub import snapshot_download
from tokenizers import Tokenizer
from transformers import AutoConfig, AutoModelForCausalLM, PreTrainedTokenizerFast

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "prms"))
import thinkprm as T  # noqa: E402

TOKENIZER_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"]
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
YES, NO = 7414, 2308  # ' Yes', ' No' in the released tokenizer.json


# ---- Verbatim from github.com/mukhal/ThinkPRM @ 045b1ae (MIT, Copyright (c) 2026 Muhammad Khalifa): utils/helper.py
## main template used in the paper
def format_verification_cot_for_thinkprm(tokenizer, problem, solution, cot=None, long_cot=False, instruction=None):
    #TODO: pass template as argument
    _instruction = instruction if instruction is not None else "Review and critique each step in the proposed solution to determine whether each step is correct. If the solution is incomplete, only verify the provided steps." ## default instruction (models were trained with this)

    instruction_template = """You are given a math problem and a proposed step-by-step solution:

[Math Problem]

{problem}

[Solution]

{solution}

{_instruction}
""".strip()

    s = tokenizer.apply_chat_template([
        {'role': "user", "content": instruction_template.replace('{problem}', problem).replace('{solution}', solution).replace('{_instruction}', _instruction)}
    ], tokenize=False, add_generation_prompt=True)

    return s


def official_input(tokenizer, question, prefix_steps):
    """ThinkPRM.process_example (prm/thinkprm.py), verbatim but for self."""
    # Format steps with tags
    formatted_steps = ''
    for sdx, step in enumerate(prefix_steps):
        formatted_steps += f'Step {sdx+1}: {step}\n'

    formatted_steps = formatted_steps.strip()
    # Format prompt with tagged response
    input_text = format_verification_cot_for_thinkprm(tokenizer, question, formatted_steps)
    return input_text


def released_files():
    return snapshot_download(T.HF_ID, revision=T.REVISION,
                             allow_patterns=TOKENIZER_FILES + ["config.json", "generation_config.json"])


def test_build_inputs():
    src = released_files()
    tok = PreTrainedTokenizerFast.from_pretrained(src)  # the class T.load uses
    raw = Tokenizer.from_file(os.path.join(src, "tokenizer.json"))  # what LlamaTokenizerFast wraps in vLLM's stack
    render = lambda rec: tok.apply_chat_template(T.build_inputs(rec), tokenize=False, add_generation_prompt=True)
    readme = {"rule_text": "", "case_text": "What is 15% of 200?",  # the README's Basic Usage, its first step
              "claim_text": "To find 15% of 200, I need to multiply 200 by 0.15"}
    for rec, q, steps in [(readme, "What is 15% of 200?", [readme["claim_text"]]),
                          (RECS[0], f"Rule: {RULE}\n\nCase:\n{CASE}", ["Prescribe cephalexin."]),
                          (RECS[2], RECS[2]["case_text"], [RECS[2]["claim_text"]])]:
        text = official_input(tok, q, steps)
        assert render(rec) == text
        # vLLM 0.6.4.post1 encodes a text prompt with tokenizer.encode(text): add_bos_token puts a BOS before the
        # template's own
        assert T._encode(tok, T.build_inputs(rec)) == [151646] + raw.encode(text, add_special_tokens=False).ids
    assert render(readme).endswith("Step 1: To find 15% of 200, I need to multiply 200 by 0.15\n\nReview and critique "
                                   "each step in the proposed solution to determine whether each step is correct. If "
                                   "the solution is incomplete, only verify the provided steps.<｜Assistant｜><think>\n")
    assert T._encode(tok, T.build_inputs(readme))[:3] == [151646, 151646, 151644]  # two BOS as vLLM encodes, <｜User｜>
    assert [tok.encode(t, add_special_tokens=False) for t in (T.CORRECT, T.INCORRECT)] == [[YES], [NO]]


def test_verdict_tail():
    tok = PreTrainedTokenizerFast.from_pretrained(released_files())
    enc = lambda s: tok.encode(s, add_special_tokens=False)
    eos, pre = tok.eos_token_id, enc(T.PREDECISION)
    assert pre == [3872, 279, 6291, 4396, 30]
    tail = lambda ids, finished: T._verdict_tail(ids, finished, YES, NO, pre, tok.decode)
    done = enc("Step 1: fine. No error.\n</think>\nIs the solution correct? Yes") + [eos]
    assert tail(done, True) == (done[:-2], False)  # finished: before its last decision, ' Yes' (not ' No' in 'No error')
    assert tail(done[:-1], False) == (done[:-2], True)  # budget hit: stops at the stop string, nothing appended
    plain = enc("Step 1: fine.\n</think>\nThe solution is fine.") + [eos]
    assert tail(plain, True) == (plain + pre, True)  # no decision: EOS kept (vLLM token_ids), string appended
    assert tail(plain[:5], False) == (plain[:5] + pre, True)
    spaced = enc("x. Is the solution correct? yes") + [eos]  # ' Is' != 'Is': only the text-level stop finds it
    assert tail(spaced, True) == (spaced[:-2], True)
    merged = enc("x\nIs the solution correct?\n\nYes") + [eos]  # '?\n\n' completes it: cut there, then re-appended
    assert tail(merged, True) == (merged[:-2] + pre, True)


def test_score_end_to_end():
    src = released_files()
    with tempfile.TemporaryDirectory(prefix="tiny-thinkprm-", ignore_cleanup_errors=True) as d:
        with open(os.path.join(src, "config.json"), encoding="utf-8") as f:
            cfg = json.load(f)
        cfg.update(num_hidden_layers=2, max_window_layers=2, hidden_size=64, intermediate_size=128,
                   num_attention_heads=4, num_key_value_heads=2)
        torch.manual_seed(0)
        AutoModelForCausalLM.from_config(AutoConfig.for_model(**cfg), dtype=torch.float32).save_pretrained(d)
        for f in TOKENIZER_FILES + ["generation_config.json"]:  # the released sampling defaults must be overridden
            shutil.copy(os.path.join(src, f), d)
        model, tok = T.load(d, device="cpu")  # default bfloat16, as on the GPU
        assert type(model).__name__ == "Qwen2ForCausalLM" and model.config.vocab_size == 152064
        assert model.generation_config.do_sample  # released default (temperature 0.6, top_p 0.95)
        u = T.score(model, tok, RECS, batch_size=2, max_new_tokens=8)
        assert len(u) == len(RECS) and all(isinstance(v, float) and math.isfinite(v) and abs(v) <= 30 for v in u), u
        outs = list(T.LAST_OUTPUTS)  # 8 random tokens, no end token: every verdict is forced
        assert len(outs) == len(RECS) and all(o.endswith(T.PREDECISION) for o in outs), outs
        assert T.score(model, tok, RECS, batch_size=2, max_new_tokens=8) == u and T.LAST_OUTPUTS == outs  # greedy

        # float32, scripted chains: u against an unpadded pass over the ids the verdict is read after
        model, tok = T.load(d, device="cpu", dtype="float32")
        enc = lambda s: tok.encode(s, add_special_tokens=False)
        eos, pre = tok.eos_token_id, enc(T.PREDECISION)
        script = enc("Let's verify step by step:\n\nStep 1: fine. No error.\n\nThe step is \\boxed{correct}\n"
                     "</think>\nIs the solution correct? Yes")
        cut = enc("Let's verify step by step:\n\nStep 1: fine.\n</think>\nIs the solution correct?")
        plain = enc("Let's verify step by step:\n\nStep 1: fine.\n</think>\nThe solution is fine.")
        assert script[-1] == YES and NO in script and not {YES, NO} & set(cut + plain)
        cases = [  # (generated ids, reader output, forced verdicts, ids the verdict follows given the prompt ids p)
            (script + [eos] * 2, script + [eos], 0, lambda p: p + script[:-1]),  # its last ' Yes'/' No'; two BOS
            (cut + enc(" Wait, let me"), cut, 2, lambda p: p[1:] + cut),  # budget hit: stop string; one BOS
            (plain + [eos] * 2, plain + [eos] + pre, 2, lambda p: p[1:] + plain + [eos] + pre),  # no decision
        ]
        for gen, out, forced, before in cases:
            model.generate = lambda input_ids, gen=gen, **kw: torch.cat(
                [input_ids, torch.tensor([gen] * len(input_ids))], 1)
            logs = []
            u = T.score(model, tok, RECS[:2], batch_size=2, log=logs.append)  # prompts of different lengths: left pad
            assert T.LAST_OUTPUTS == [tok.decode(out)] * 2 and logs[-1].endswith(f"forced verdicts {forced}"), logs
            for r, v in zip(RECS[:2], u):
                with torch.no_grad():
                    ref = model(torch.tensor([before(T._encode(tok, T.build_inputs(r)))])).logits[0, -1]
                assert abs((ref[YES] - ref[NO]).item() - v) < 1e-4, (v, ref[[YES, NO]])


if __name__ == "__main__":
    test_build_inputs()
    test_verdict_tail()
    test_score_end_to_end()
    print("ok")
