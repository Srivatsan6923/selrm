"""CPU check of scripts/prms/genprm.py. Run: python tests/test_prm_genprm.py
(a) build_inputs and the rendered prompt against the official demo's printed request, string level, with the released
tokenizer; (b) the stop-string criterion on token ids; (c) load() + score() end to end on a tiny random
Qwen2ForCausalLM (2 layers, hidden 64) saved with the released tokenizer and generation-config files, greedy batched
generation against one row at a time and an argmax loop, and the verdict read-out against an unpadded forward pass;
(d) the official stage loop with a scripted stand-in model and the subprocess executor. Downloads the released
tokenizer/config files only, never the weights."""
import json, math, os, shutil, sys, tempfile, types

import torch
from huggingface_hub import snapshot_download
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "prms"))
import genprm as G  # noqa: E402

TOKENIZER_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"]
# src/example/demo.ipynb @ a08da3f, cell "Pass@1 inference for single step": the question and its first paragraph,
# and the prompt it printed for request 1 (cprint shows each newline as \n).
DEMO_QUESTION = ("Jo adds up all the positive integers from 1 to 100. Kate does a similar thing with the first 100 "
                 "positive integers; however, she first rounds every integer to its nearest multiple of 10 (rounding "
                 "5s up) and then adds the 100 values. What is the positive difference between Jo's sum and Kate's "
                 "sum?")
DEMO_STEP = (r"First, we need to calculate Jo's sum, which is the sum of all positive integers from 1 to 100. This can "
             r"be directly computed using the formula for the sum of the first \(n\) positive integers, which is "
             r"\(\frac{n(n+1)}{2}\). For \(n = 100\), Jo's sum is \(\frac{100 \cdot 101}{2} = 5050\).")
DEMO_REQUEST_1 = (
    r"<｜begin▁of▁sentence｜>You are a math teacher. Your task is to review and critique the paragraphs in solution step "
    r"by step.<｜User｜>Question: Jo adds up all the positive integers from 1 to 100. Kate does a similar thing with the "
    r"first 100 positive integers; however, she first rounds every integer to its nearest multiple of 10 (rounding 5s "
    r"up) and then adds the 100 values. What is the positive difference between Jo's sum and Kate's sum?\n\nFirst, we "
    r"need to calculate Jo's sum, which is the sum of all positive integers from 1 to 100. This can be directly "
    r"computed using the formula for the sum of the first \(n\) positive integers, which is \(\frac{n(n+1)}{2}\). For "
    r"\(n = 100\), Jo's sum is \(\frac{100 \cdot 101}{2} = 5050\).<analyze>\nLet's analyze the Paragraph 1 step by "
    r"step: ")
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


def released_files():
    return snapshot_download(G.HF_ID, revision=G.REVISION,
                             allow_patterns=TOKENIZER_FILES + ["config.json", "generation_config.json"])


def test_build_inputs():
    demo = {"rule_text": "", "case_text": DEMO_QUESTION, "claim_text": DEMO_STEP}
    assert G.build_inputs(demo) == [{"role": "system", "content": G.SYSTEM},
                                    {"role": "user", "content": f"Question: {DEMO_QUESTION}\n\n{DEMO_STEP}"}]
    assert G.build_inputs(RECS[0])[1]["content"] == f"Question: Rule: {RULE}\n\nCase:\n{CASE}\n\nPrescribe cephalexin."
    tok = AutoTokenizer.from_pretrained(released_files())
    text = G.build_prompt(G.build_inputs(demo), tok) + G.ANALYZE_START
    assert text.replace("\n", "\\n") == DEMO_REQUEST_1
    assert G._encode(tok, text)[:3] == [151646, 151646, 2610]  # two BOS, as vLLM 0.7.1 encodes it, then 'You'
    assert [tok.encode(w)[-1] for w in ("Yes", "No")] == [9454, 2753]


def test_stop_strings():
    """_Stop as vLLM: a stop string counts only inside the generated text (the prompt's trailing newline does not
    complete '\\n```\\n'), and the row stops at the token that completes it ('>\\n\\n' completes '</analyze>\\n')."""
    tok = AutoTokenizer.from_pretrained(released_files())
    for prompt, gen, stops, want in [
            ("a", "Fine.\n</analyze>\n", ["</analyze>\n"], "Fine.\n</analyze>\n"),
            ("x```python\n", "```\nprint(1)\n```\nmore", ["\n```\n", "</output>\n"], "```\nprint(1)\n```\n"),
            ("a", "done.</analyze>\n\nmore", ["</analyze>\n"], "done.</analyze>\n\n")]:
        p, g = (tok.encode(s, add_special_tokens=False) for s in (prompt, gen))
        crit = G._Stop(tok, stops, len(p), [10 ** 6])
        k = next(k for k in range(1, len(g) + 1) if crit(torch.tensor([p + g[:k]]), None)[0])
        assert tok.decode(g[:k]) == want, (gen, tok.decode(g[:k]))


def test_score_end_to_end():
    src = released_files()
    with tempfile.TemporaryDirectory(prefix="tiny-genprm-", ignore_cleanup_errors=True) as d:
        with open(os.path.join(src, "config.json"), encoding="utf-8") as f:
            cfg = json.load(f)
        cfg.update(num_hidden_layers=2, max_window_layers=2, hidden_size=64, intermediate_size=128,
                   num_attention_heads=4, num_key_value_heads=2)
        torch.manual_seed(0)
        AutoModelForCausalLM.from_config(AutoConfig.for_model(**cfg), dtype=torch.float32).save_pretrained(d)
        for f in TOKENIZER_FILES + ["generation_config.json"]:  # the released sampling defaults must be overridden
            shutil.copy(os.path.join(src, f), d)
        model, tok = G.load(d, device="cpu")  # default bfloat16, as on the GPU
        assert type(model).__name__ == "Qwen2ForCausalLM" and model.config.vocab_size == 152064
        u = G.score(model, tok, RECS, batch_size=2, max_new_tokens=24)
        assert len(u) == len(RECS) and all(isinstance(v, float) and math.isfinite(v) and abs(v) <= 30 for v in u), u
        # 24 tokens of random analysis exhaust the budget: each record ends in the official fallback verdict call
        assert len(G.LAST_OUTPUTS) == len(RECS)
        assert all(o.startswith(G.ANALYZE_START) and "</analyze>\n" + G.OUTPUT_START in o for o in G.LAST_OUTPUTS)
        # float32: the batched, left-padded read-out = logit(Yes) - logit(No) where an unpadded pass predicts the
        # verdict token; a Yes and a No verdict of different context lengths, and a critique without a verdict
        model, tok = G.load(d, device="cpu", dtype="float32")
        # greedy although the released generation_config samples; a left-padded batch = each row alone = argmax
        texts = [G.build_prompt(G.build_inputs(r), tok) + G.ANALYZE_START for r in RECS]
        batched = G._generate(model, tok, texts, ["</analyze>\n"], [8] * len(texts))
        assert batched == [G._generate(model, tok, [t], ["</analyze>\n"], [8])[0] for t in texts]
        ids, greedy = G._encode(tok, texts[1]), []
        with torch.no_grad():
            for _ in range(8):
                greedy.append(int(model(torch.tensor([ids + greedy])).logits[0, -1].argmax()))
        assert batched[1][1] == greedy, (batched[1][1], greedy)
        ctx = G._encode(tok, G.build_prompt(G.build_inputs(RECS[0]), tok) + G.ANALYZE_START + "Fine.\n</analyze>\n"
                        + G.OUTPUT_START)
        items = [(ctx, tok.encode("{Yes}$\n</output>\n", add_special_tokens=False), "$\\boxed{Yes}$"),
                 (ctx[:-30], tok.encode("{No}$\n</output>\n", add_special_tokens=False), "$\\boxed{No}$"),
                 (ctx, tok.encode("{maybe}$\n</output>\n", add_special_tokens=False), "$\\boxed{maybe}$")]
        u = G._verdict_logodds(model, tok, items)
        assert u[2] == 0.0, u
        for (p, g, _), v, w in zip(items, u, ("Yes", "No")):
            k = g.index(tok.encode(w)[-1])
            with torch.no_grad():
                ref = model(torch.tensor([p + g])).logits[0, len(p) + k - 1]
            assert v != 0.0 and abs((ref[9454] - ref[2753]).item() - v) < 1e-4, (w, v, ref[[9454, 2753]])


class Scripted:
    """Stand-in model for the official stage loop: a fixed continuation per stage template the prompt ends with, run
    past its stop string ('Junk' must be cut off); its logits favour 'No' over 'Yes' by 2 everywhere."""
    device = torch.device("cpu")

    def __init__(self, tok):
        self.tok = tok

    def generate(self, input_ids, **kwargs):
        conts = []
        for row in input_ids.tolist():
            text = self.tok.decode(row)
            cont = ("361 is not below 50.\n</analyze>\n\nJunk" if text.endswith(G.ANALYZE_START) else
                    "print(361 < 50)\n```\nJunk" if text.endswith(G.VERIFY_START) else
                    "</verify>\n<output>\n**Judgement**: $\\boxed{No}$\n</output>\nJunk")
            conts.append(self.tok.encode(cont, add_special_tokens=False) + [self.tok.eos_token_id])
        n = max(map(len, conts))
        return torch.cat([input_ids, torch.tensor([c + [self.tok.pad_token_id] * (n - len(c)) for c in conts])], 1)

    def __call__(self, input_ids, **kwargs):
        logits = torch.zeros(len(input_ids), 1, len(self.tok))
        logits[:, :, self.tok.encode("No")[-1]] = 2.0
        return types.SimpleNamespace(logits=logits)


def test_official_flow():
    tok = AutoTokenizer.from_pretrained(released_files())
    assert G.score(Scripted(tok), tok, RECS[:2], batch_size=2) == [-2.0, -2.0]
    assert G.LAST_OUTPUTS[0] == (
        G.ANALYZE_START + "361 is not below 50.\n</analyze>\n" + G.VERIFY_START + "print(361 < 50)\n```\n"
        "[Code Output]\n\n```\nFalse\n```\n</verify>\n<output>\n**Judgement**: $\\boxed{No}$\n</output>\n")
    assert G._run_code(["x = 41", "print(x + 1)"]) == "42"  # earlier blocks rebuild the namespace
    assert G._run_code(["1/0"]) == "Code execute Error: ZeroDivisionError: division by zero"
    assert G._run_code(["while True: pass"], seconds=1) == "Code execute time out: Code execution timed out"


if __name__ == "__main__":
    test_build_inputs()
    test_stop_strings()
    test_score_end_to_end()
    test_official_flow()
    print("ok")
