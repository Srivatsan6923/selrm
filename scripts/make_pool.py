r"""Candidate pools for answer selection (D-POOL-*; Table 5, Fig. 3 right).

  python scripts/make_pool.py --pool medqa_test --out /pvc/selrm-d/pools [--model DIR] [--limit 20]

A frozen policy (configs/datasets_d.json "policy") samples chains of thought with
numbered steps and a final line "Final answer: <letter>" for every question of a pinned
dataset. Pools are nested: every question gets N samples (16), and a fixed subset of
questions (300 of MedQA test) gets 64, of which samples 0-15 are the 16-sample pool, so
every selector and every N sees identical candidates. A sample is eligible if it has a
final answer among the options; the share that is not is reported.

Output (one directory per pool): questions.jsonl {qid, question, options{letter: text},
answer, meta}, samples.jsonl {qid, sample, text, steps[], final, eligible, n_tokens},
MANIFEST.json (source, revision, sha256, prompt, sampling parameters, seeds, counts,
vLLM version, model revision, GPU, wall time) and DONE. Re-running skips a finished pool.
"""
import argparse
import hashlib
import io
import json
import os
import random
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "configs", "datasets_d.json"), encoding="utf-8"))

PROMPT = ("Answer the following medical exam question. Reason step by step in numbered steps "
          "(1., 2., 3., ...), one statement per step. End with a separate line of the form "
          "'Final answer: X', where X is the letter of the correct option.\n\n"
          "Question:\n{question}\n\nOptions:\n{options}")
# The pinned snapshot has no generation_config.json: stop tokens <|im_end|> and <|endoftext|>
# are given explicitly (configs/models_b.json note) and vLLM's own defaults are used.
SAMPLING = {"temperature": 0.7, "top_p": 0.95, "max_tokens": 1536, "stop_token_ids": [248046, 248044]}
POOLS = {   # name: (dataset key in configs/datasets_d.json, split rows, N, subset size with 64 samples)
    "medqa_test": ("medqa_test", None, 16, 300),
    "medqa_dev": ("medqa_dev", 500, 16, 0),     # calibration pool (D-CAL); first 500 questions
    "careqa_en": ("careqa_en", None, 16, 0),
}
STEP = re.compile(r"^\s*(?:Step\s*)?(\d{1,2})[.):]\s+(.*\S)")
FINAL = re.compile(r"Final answer:\s*\**\s*\(?([A-Ea-e])\)?(?![A-Za-z])")


def fetch(spec):
    url = f"https://huggingface.co/datasets/{spec['hf_dataset']}/resolve/{spec['revision']}/{spec['file']}"
    data = urllib.request.urlopen(url, timeout=120).read()
    got = hashlib.sha256(data).hexdigest()
    if got != spec["sha256"]:
        sys.exit(f"sha256 mismatch for {url}: {got}")
    return data


def questions(key, rows):
    spec = CFG[key]
    data = fetch(spec)
    out = []
    if spec["file"].endswith(".parquet"):
        import pandas as pd
        df = pd.read_parquet(io.BytesIO(data))
        for i, r in df.iterrows():
            opts = {o["key"]: o["value"] for o in r["options"]}
            out.append({"qid": f"{key}-{i:05d}", "question": r["question"], "options": opts,
                        "answer": r["answer_idx"], "meta": {"meta_info": r.get("meta_info")}})
    else:   # CareQA: list of {question, op1..op4, cop (1-based), exam_id, year, category, unique_id}
        for i, r in enumerate(json.loads(data)):
            opts = {"ABCD"[k]: r[f"op{k + 1}"] for k in range(4)}
            out.append({"qid": f"{key}-{i:05d}", "question": r["question"], "options": opts,
                        "answer": "ABCD"[int(r["cop"]) - 1],
                        "meta": {k: r.get(k) for k in ("exam_id", "year", "category", "unique_id")}})
    return out[:rows] if rows else out


def parse(text, options):
    steps = [m.group(2) for m in (STEP.match(ln) for ln in text.split("\n")) if m]
    finals = FINAL.findall(text)
    final = finals[-1].upper() if finals else None
    return steps, final, bool(final and final in options and steps)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", required=True, choices=sorted(POOLS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", help="local snapshot of the policy (default: download the pinned revision)")
    ap.add_argument("--limit", type=int, default=0, help="first k questions only (smoke test)")
    ap.add_argument("--tp", type=int, default=1)
    a = ap.parse_args()
    key, rows, n, n_sub = POOLS[a.pool]
    out = os.path.join(a.out, a.pool + (f"_limit{a.limit}" if a.limit else ""))
    if os.path.exists(os.path.join(out, "DONE")):
        print("exists:", out)
        return
    os.makedirs(out, exist_ok=True)
    qs = questions(key, rows)[: a.limit or None]
    rng = random.Random(f"pool-subset-v1.{a.pool}")
    sub = set(rng.sample([q["qid"] for q in qs], min(n_sub, len(qs)))) if n_sub else set()

    import torch
    import vllm
    from transformers import AutoTokenizer
    pol = CFG["policy"]
    model = a.model or pol["model"]
    tok = AutoTokenizer.from_pretrained(model, revision=None if a.model else pol["revision"])
    llm = vllm.LLM(model=model, revision=None if a.model else pol["revision"], dtype="bfloat16",
                   tensor_parallel_size=a.tp, seed=0, enable_prefix_caching=True, max_model_len=4096,
                   generation_config="vllm", limit_mm_per_prompt={"image": 0, "video": 0})
    prompts, params = [], []
    for q in qs:
        user = PROMPT.format(question=q["question"],
                             options="\n".join(f"{k}. {v}" for k, v in q["options"].items()))
        ids = tok.apply_chat_template([{"role": "user", "content": user}], add_generation_prompt=True,
                                      enable_thinking=False, tokenize=True)
        seed = int(hashlib.sha256(f"{a.pool}|{q['qid']}".encode()).hexdigest()[:8], 16)
        prompts.append({"prompt_token_ids": ids})
        params.append(vllm.SamplingParams(n=64 if q["qid"] in sub else n, seed=seed, **SAMPLING))
    t0 = time.time()
    res = llm.generate(prompts, params)
    wall = time.time() - t0
    n_s = n_el = n_tok = 0
    with open(os.path.join(out, "questions.jsonl"), "w", encoding="utf-8", newline="\n") as fq, \
            open(os.path.join(out, "samples.jsonl"), "w", encoding="utf-8", newline="\n") as fs:
        for q, r in zip(qs, res):
            fq.write(json.dumps(q | {"subset64": q["qid"] in sub}) + "\n")
            for k, o in enumerate(r.outputs):
                steps, final, ok = parse(o.text, q["options"])
                fs.write(json.dumps({"qid": q["qid"], "sample": k, "text": o.text, "steps": steps,
                                     "final": final, "eligible": ok, "n_tokens": len(o.token_ids),
                                     "finish": o.finish_reason}) + "\n")
                n_s, n_el, n_tok = n_s + 1, n_el + ok, n_tok + len(o.token_ids)
    man = {"pool": a.pool, "dataset": CFG[key], "policy": pol, "model_path": model, "prompt": PROMPT,
           "chat_template": "tokenizer.apply_chat_template(enable_thinking=False)", "sampling": SAMPLING,
           "n_per_question": n, "subset64": sorted(sub), "seed_rule": "sha256(pool|qid)[:8] per question",
           "n_questions": len(qs), "n_samples": n_s, "eligible": n_el,
           "ineligible_share": round(1 - n_el / max(1, n_s), 4), "generated_tokens": n_tok,
           "wall_seconds": round(wall, 1), "vllm": vllm.__version__, "torch": torch.__version__,
           "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
           "step_regex": STEP.pattern, "final_regex": FINAL.pattern}
    json.dump(man, open(os.path.join(out, "MANIFEST.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    open(os.path.join(out, "DONE"), "w").close()
    print(json.dumps({k: man[k] for k in ("pool", "n_questions", "n_samples", "eligible", "ineligible_share",
                                          "generated_tokens", "wall_seconds")}))


if __name__ == "__main__":
    main()
