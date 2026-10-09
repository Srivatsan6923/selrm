"""CPU check of scripts/prms/medprm.py. Run: python tests/test_prm_medprm.py
(a) build_inputs against the format of the model card's Quick Start (string level) and the released tokenizer;
(b) load() + score() end to end on a tiny random LlamaForCausalLM (2 layers, hidden 64) saved with the released
tokenizer files, cross-checked against the official single-sequence get_prob. Downloads the released
tokenizer/config files only, never the weights."""
import math, os, shutil, sys, tempfile

import torch
from huggingface_hub import snapshot_download
from tokenizers import Tokenizer
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "prms"))
import medprm as M  # noqa: E402

TOKENIZER_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"]
# The card's Quick Start, quoted (huggingface.co/dmis-lab/llama-3.1-medprm-reward-v1.0 @ 6948b9e, README.md).
CARD_SYSTEM_PROMPT = (
        "You are an evaluator assessing the logicality and validity of the reasoning in each step of the given explanation. "
        "In order to support the evaluation, the relevant documents, the question, and the explanation are provided sequentially. "
        "If the reasoning contains errors, output - after that step. If the reasoning in a step is logical and valid, output + after that step. "
)
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


def card_messages(rec):
    """The card's construction with doc_block = '' (no retrieval), written independently of the module."""
    question = f"Rule: {rec['rule_text']}\n\nCase:\n{rec['case_text']}" if rec["rule_text"] else rec["case_text"]
    explanation = f"Step 1: {rec['claim_text']} ки"
    doc_block = ""
    user_content = f"{doc_block}Question: {question}\n\nExplanation: {explanation}"
    return [{"role": "system", "content": CARD_SYSTEM_PROMPT}, {"role": "user", "content": user_content}]


def official_get_prob(model, tokenizer, text):
    plus_id = tokenizer(" +", add_special_tokens=False)["input_ids"][0]
    minus_id = tokenizer(" -", add_special_tokens=False)["input_ids"][0]

    # ---- Verbatim from eth-medical-ai-lab/Med-PRM @ 3a7256f, python/4_scoring_PRM.py (nested in main() there; no
    # ---- LICENSE file in the repo). The card's copy indexes offsets[0] of an unbatched encoding and cannot run.
    def get_prob(text, special_char=" ки"):
        encoded = tokenizer(
            text, return_tensors="pt", return_offsets_mapping=True,
            add_special_tokens=True
        )
        input_ids = encoded["input_ids"].to(model.device)
        attention_mask = encoded["attention_mask"].to(model.device)
        offsets = encoded["offset_mapping"][0]

        with torch.no_grad():
            logits = model(input_ids, attention_mask=attention_mask).logits[0]

        positions = [i for i, (s, e) in enumerate(offsets)
                     if text[s:e] == special_char]

        plus_probs, min_plus, final_plus = [], None, None
        for pos in positions:
            if pos >= logits.size(0):
                continue
            two = torch.stack([logits[pos][plus_id], logits[pos][minus_id]])
            probs = torch.softmax(two, dim=0)
            plus_probs.append(probs[0])
        if plus_probs:
            min_plus = torch.min(torch.stack(plus_probs)).item()
            final_plus = plus_probs[-1].item()

        return {
            "plus_probs": plus_probs,
            "min_plus_prob": min_plus,
            "final_plus_prob": final_plus
        }
    # ---- End of the verbatim code.
    return get_prob(text)


def released_files():
    return snapshot_download(M.HF_ID, revision=M.REVISION, allow_patterns=TOKENIZER_FILES + ["config.json"])


def test_build_inputs():
    for rec in RECS:  # RECS[2] has no rule: the question is the case alone
        assert M.build_inputs(rec) == card_messages(rec), rec
    src = released_files()
    tok = AutoTokenizer.from_pretrained(src)
    # transformers 5.x rebuilt its tokenizer classes; the ids must stay those of the release-era fast tokenizer
    # (transformers 4.51 PreTrainedTokenizerFast = tokenizer.json through the tokenizers library), double BOS included
    fast = Tokenizer.from_file(os.path.join(src, "tokenizer.json"))
    for rec in RECS:
        t = tok.apply_chat_template(M.build_inputs(rec), tokenize=False, add_generation_prompt=True)
        assert tok(t, add_special_tokens=True)["input_ids"] == fast.encode(t).ids, rec
    text = tok.apply_chat_template(M.build_inputs(RECS[0]), tokenize=False, add_generation_prompt=True)
    assert text == (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\n"
        "Today Date: 26 Jul 2024\n\n" + CARD_SYSTEM_PROMPT.strip() + "<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n\nQuestion: Rule: " + RULE + "\n\nCase:\n" + CASE
        + "\n\nExplanation: Step 1: Prescribe cephalexin. ки<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n")
    # ids as the official get_prob makes them: two <|begin_of_text|>, one step marker, read where its offsets put it
    ids = tok(text, add_special_tokens=True)["input_ids"]
    assert ids[:2] == [128000, 128000] and ids.count(128256) == 1 and tok.convert_tokens_to_ids(M.STEP_TAG) == 128256
    offsets = tok(text, return_offsets_mapping=True, add_special_tokens=True)["offset_mapping"]
    assert [i for i, (s, e) in enumerate(offsets) if text[s:e] == M.STEP_TAG] == [ids.index(128256)] == [len(ids) - 6]
    assert [tok(c, add_special_tokens=False)["input_ids"][0] for c in (" +", " -")] == [489, 482]  # as in PROMPT_NOTE


def test_score_end_to_end():
    src = released_files()
    with tempfile.TemporaryDirectory(prefix="tiny-medprm-", ignore_cleanup_errors=True) as d:
        cfg = AutoConfig.from_pretrained(src, num_hidden_layers=2, hidden_size=64, intermediate_size=128,
                                         num_attention_heads=4, num_key_value_heads=2, head_dim=16)
        torch.manual_seed(0)
        AutoModelForCausalLM.from_config(cfg, dtype=torch.float32).save_pretrained(d)
        for f in TOKENIZER_FILES:
            shutil.copy(os.path.join(src, f), d)
        model, tok = M.load(d, device="cpu")  # default bfloat16, as on the GPU
        assert type(model).__name__ == "LlamaForCausalLM" and len(tok) == cfg.vocab_size == 128257
        u = M.score(model, tok, RECS, batch_size=2)
        assert len(u) == len(RECS) and all(isinstance(v, float) and math.isfinite(v) and abs(v) <= 30 for v in u), u
        # float32: batched, right-padded scores = the official get_prob on the card template, one sequence at a time
        model, tok = M.load(d, device="cpu", dtype="float32")
        u = M.score(model, tok, RECS, batch_size=2)
        print("u", u)
        for rec, v in zip(RECS, u):
            text = tok.apply_chat_template(card_messages(rec), tokenize=False, add_generation_prompt=True)
            p = official_get_prob(model, tok, text)
            assert len(p["plus_probs"]) == 1, p
            p = p["final_plus_prob"]
            assert abs(math.log(p) - math.log(1 - p) - v) < 1e-4, (p, v)


if __name__ == "__main__":
    test_build_inputs()
    test_score_end_to_end()
    print("ok")
