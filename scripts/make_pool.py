r"""Candidate pools for answer selection (D-POOL-*; Table 5, Fig. 3 right).

  python scripts/make_pool.py --pool medqa_test --out /pvc/selrm-d/pools [--model DIR] [--limit 20]

A frozen policy (configs/datasets_d.json "policy") samples chains of thought with
numbered steps and a final line "Final answer: <letter>" for every question of a pinned
dataset. Pools are nested: every question gets N = 16 samples; for the selection-pressure
curve, `--extend subset` later adds samples 16-63 for 300 questions of the pool medqa_kp
(150 whole key pairs drawn once from C's MedQA key pairs, configs/keypairs_d.json; Fig. 3 right
plots key-pair accuracy), with their own seeds, in samples_ext.jsonl; samples 0-15 stay the 16-sample pool, so every selector and
every N sees identical candidates. A sample is eligible if it has a final answer among the options;
the share that is not is reported.

Output (one directory per pool): questions.jsonl {qid, question, options{letter: text},
answer, meta}, samples.jsonl {qid, sample, text, steps[], final, eligible, n_tokens},
MANIFEST.json (source, revision, sha256, prompt, sampling parameters, seeds, counts,
vLLM version, model revision, GPU, wall time) and DONE; an extension writes
questions_ext.jsonl, samples_ext.jsonl, MANIFEST_ext.json and EXTENDED. Re-running skips
finished work.
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
POOLS = {   # name: (dataset key in configs/datasets_d.json, first rows, N, subset size with 64 samples,
           #        random sample of questions)
    "medqa_test": ("medqa_test", None, 16, 0, 0),
    "medqa_dev": ("medqa_dev", 500, 16, 0, 0),       # calibration pool (D-CAL); first 500 questions
    # the 714 questions of C's MedQA key pairs (configs/keypairs_d.json; test and validation rows);
    # + 48 samples for 150 whole pairs (300 questions) for the selection-pressure curve (--extend subset)
    "medqa_kp": (("medqa_test", "medqa_dev"), None, 16, 300, 0),
    "careqa_en": ("careqa_en", None, 16, 0, 1000),   # a fixed random 1,000 of 5,621 (scoring cost; DECISIONS_D)
    "medeinst_test": ("medeinst_test", None, 16, 0, 0),   # a fixed random 500 pairs, control + trap (questions())
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


def medeinst_questions(data, n_pairs):
    """A fixed random sample of MedEinst pairs; each pair gives its control and its trap case as two
    questions with the pair's two diagnoses as options (one option order per pair, so the letters
    carry no information). Narratives are whitespace-normalised as in C's clin_v1/medeinst_test."""
    pairs = {}
    for line in data.decode("utf-8").splitlines():
        r = json.loads(line)
        pairs.setdefault(r["case_id"], {})[r["case_type"]] = r
    ids = sorted(k for k, v in pairs.items() if set(v) == {"control", "trap"})
    keep = sorted(random.Random("pool-sample-v1.medeinst_test").sample(ids, n_pairs))
    out = []
    for cid in keep:
        c, t = pairs[cid]["control"], pairs[cid]["trap"]
        ygt, ybias = c["ground_truth"], t["ground_truth"]
        flip = int(hashlib.sha256(f"medeinst|{cid}".encode()).hexdigest(), 16) % 2
        opts = {"A": ybias, "B": ygt} if flip else {"A": ygt, "B": ybias}
        for row in (c, t):
            narrative = "\n".join(ln.rstrip() for ln in row["narrative"].replace("\r", "").split("\n")).strip()
            out.append({"qid": f"medeinst_test-{cid}-{row['case_type']}",
                        "question": narrative + "\n\nWhat is the most likely diagnosis?", "options": opts,
                        "answer": next(k for k, v in opts.items() if v == row["ground_truth"]),
                        "meta": {"case_id": cid, "case_type": row["case_type"], "tid": f"medeinst_test_{cid}",
                                 "y_gt": ygt, "y_bias": ybias}})
    return out


def questions(key, rows):
    spec = CFG[key]
    data = fetch(spec)
    out = []
    if key == "medeinst_test":
        return medeinst_questions(data, 500)
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
    ap.add_argument("--extend", help="'subset' (medqa_kp: 150 whole key pairs) or a JSON list of qids: add "
                                     "samples 16-63 for them (selection pressure); written to samples_ext.jsonl, "
                                     "the 16-sample pool is not touched")
    a = ap.parse_args()
    key, rows, n, n_ext, n_sample = POOLS[a.pool]
    out = os.path.join(a.out, a.pool + (f"_limit{a.limit}" if a.limit else ""))
    done = "EXTENDED" if a.extend else "DONE"
    if os.path.exists(os.path.join(out, done)):
        print("exists:", out, done)
        return
    os.makedirs(out, exist_ok=True)
    pairs = json.load(open(os.path.join(ROOT, "configs", "keypairs_d.json"), encoding="utf-8"))["pairs"]
    if isinstance(key, tuple):   # medqa_kp: the key-pair questions of both files
        kp = {x for p in pairs for x in p}
        qs = [q for k in key for q in questions(k, rows) if q["qid"] in kp]
    else:
        qs = questions(key, rows)
    if n_sample:
        keep = set(random.Random(f"pool-sample-v1.{a.pool}").sample([q["qid"] for q in qs], n_sample))
        qs = [q for q in qs if q["qid"] in keep]
    qs = qs[: a.limit or None]
    sub = set()
    if a.extend:                 # the base pool must exist; extra samples get their own seeds
        if not os.path.exists(os.path.join(out, "DONE")):
            sys.exit("extend: the 16-sample pool is not finished")
        if a.extend == "subset":     # whole key pairs, a fixed random draw of n_ext questions
            want = {x for p in random.Random(f"pool-ext-v1.{a.pool}").sample(pairs, n_ext // 2) for x in p}
        else:
            want = set(json.load(open(a.extend, encoding="utf-8")))
        qs = [q for q in qs if q["qid"] in want]
        sub = {q["qid"] for q in qs}

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
        text = tok.apply_chat_template([{"role": "user", "content": user}], add_generation_prompt=True,
                                       enable_thinking=False, tokenize=False)
        ids = tok(text, add_special_tokens=False).input_ids     # as B's evaluation (eval_local.chat_ids)
        seed = int(hashlib.sha256(f"{a.pool}|{q['qid']}{'|ext64' if a.extend else ''}".encode()).hexdigest()[:8], 16)
        prompts.append({"prompt_token_ids": ids})
        params.append(vllm.SamplingParams(n=64 - n if a.extend else n, seed=seed, **SAMPLING))
    t0 = time.time()
    res = llm.generate(prompts, params)
    wall = time.time() - t0
    n_s = n_el = n_tok = 0
    first = n if a.extend else 0
    with open(os.path.join(out, "questions_ext.jsonl" if a.extend else "questions.jsonl"), "w", encoding="utf-8",
              newline="\n") as fq, \
            open(os.path.join(out, "samples_ext.jsonl" if a.extend else "samples.jsonl"), "w", encoding="utf-8",
                 newline="\n") as fs:
        for q, r in zip(qs, res):
            fq.write(json.dumps(q) + "\n")
            for k, o in enumerate(r.outputs, first):
                steps, final, ok = parse(o.text, q["options"])
                fs.write(json.dumps({"qid": q["qid"], "sample": k, "text": o.text, "steps": steps,
                                     "final": final, "eligible": ok, "n_tokens": len(o.token_ids),
                                     "finish": o.finish_reason}) + "\n")
                n_s, n_el, n_tok = n_s + 1, n_el + ok, n_tok + len(o.token_ids)
    man = {"pool": a.pool, "dataset": [CFG[k] for k in key] if isinstance(key, tuple) else CFG[key], "policy": pol, "model_path": model, "prompt": PROMPT,
           "chat_template": "tokenizer.apply_chat_template(enable_thinking=False)", "sampling": SAMPLING,
           "n_per_question": 64 - n if a.extend else n, "extension_of": "samples 0-15" if a.extend else None,
           "seed_rule": "sha256(pool|qid" + ("|ext64" if a.extend else "") + ")[:8] per question",
           "question_sample": {"n": n_sample, "seed": f"pool-sample-v1.{a.pool}"} if n_sample else None,
           "n_questions": len(qs), "n_samples": n_s, "eligible": n_el,
           "ineligible_share": round(1 - n_el / max(1, n_s), 4), "generated_tokens": n_tok,
           "wall_seconds": round(wall, 1), "vllm": vllm.__version__, "torch": torch.__version__,
           "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
           "step_regex": STEP.pattern, "final_regex": FINAL.pattern}
    json.dump(man, open(os.path.join(out, "MANIFEST_ext.json" if a.extend else "MANIFEST.json"), "w",
                        encoding="utf-8", newline="\n"), indent=1)
    open(os.path.join(out, done), "w").close()
    print(json.dumps({k: man[k] for k in ("pool", "n_questions", "n_samples", "eligible", "ineligible_share",
                                          "generated_tokens", "wall_seconds")}))


if __name__ == "__main__":
    main()
