r"""Policy training against one reward (D-RL-*; App. G "Policy training"), TRL GRPO.

  python scripts/grpo_d.py --reward outcome|refgraph|ledger2-blocks|ledger2-triplets|stepcheck \
      --policy DIR --data DIR --out DIR [--seed 0] [--steps 1000] [--ledger-url URL] [--medprm DIR]

This is the only experiment in which a policy is optimised against a learned reward, and the
only basis for statements about reward exploitation (v13 App. G). Policy: Qwen3.5-4B with LoRA
(ROLE.md). Prompts: rule-application tasks built from rule_v1/train_triplets (training rules
only): a case, its stated rule and its two conclusion claims as options A and B (order fixed by
a seeded coin per case), "decide and justify in numbered steps; end with 'Final answer: A|B'".
Rewards (one per run):
  outcome       1 if the final answer is the claim the rule program labels correct, else 0
  refgraph      reference-graph coverage after MedCEG: 0.5 if a decisive mention of the reference
                graph (selrm.reference.reference_graph) is quoted in the steps, + 0.5 for the correct
                final answer; like the outcome reward it uses the answer of each case
  ledger2-*     Ledger-RM as a process reward: every step is read and judged as in selection
                (scripts/score_pool.py: reader on case + rule + step, judge on rule + ledger + step),
                trace score = minimum u over steps, reward = sigmoid(score); served by vLLM (--ledger-url)
  stepcheck     the step check (released Med-PRM, model-card readout): minimum plus-probability over steps
Evaluation, every --eval-every steps and at the end: greedy answers on a fixed sample of
rule_v1/test_L2 triplets (held-out signature classes), accuracy of the chosen claim by the rule
program on base, flip and near cases; with the mean training reward of the same window this is the
reward-against-accuracy curve. Output: OUT/summary_rule_v1~test_L2.json, OUT/curve.jsonl, OUT/meta.json, DONE.
"""
import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

TASK = ("Rule: {rule}\n\nCase:\n{case}\n\nWhich statement is correct for this patient under the rule?\n"
        "A. {a}\nB. {b}\n\nDecide and justify in numbered steps (1., 2., ...), one statement per step. "
        "End with a separate line of the form 'Final answer: A' or 'Final answer: B'.")
FINAL = re.compile(r"Final answer:\s*\**\s*\(?([AB])\)?(?![A-Za-z])")
STEP = re.compile(r"^\s*(?:Step\s*)?(\d{1,2})[.):]\s+(.*\S)")


def load(path):
    return [json.loads(line) for line in open(path, encoding="utf-8")]


def tasks(records, kinds=("base", "flip", "near"), tag="train"):
    """One task per (tid, case_kind): both conclusion claims as A/B, gold = the letter of the label-1 claim."""
    by = {}
    for r in records:
        if r["claim_type"] == "conclusion" and r["case_kind"] in kinds:
            by.setdefault((r["tid"], r["case_kind"]), {})[r["claim_role"]] = r
    out = []
    for (tid, kind), cl in sorted(by.items()):
        if set(cl) != {"s", "s_prime"}:
            continue
        s, sp = cl["s"], cl["s_prime"]
        flip = int(hashlib.sha256(f"{tag}|{tid}|{kind}".encode()).hexdigest(), 16) % 2
        a, b = (sp, s) if flip else (s, sp)
        gold = "A" if a["label"] == 1 else "B"
        out.append({"prompt": [{"role": "user", "content": TASK.format(rule=s["rule_text"], case=s["case_text"],
                                                                       a=a["claim_text"], b=b["claim_text"])}],
                    "gold": gold, "tid": tid, "case_kind": kind, "iid_a": a["iid"], "iid_b": b["iid"]})
    return out


def text_of(completion):
    return completion[-1]["content"] if isinstance(completion, list) else completion


def answer(text):
    m = FINAL.findall(text)
    return m[-1] if m else None


def steps_of(text):
    return [m.group(2) for m in (STEP.match(ln) for ln in text.split("\n")) if m]


# ------------------------------------------------------------------ rewards
def outcome_reward(completions, gold, **_):
    return [float(answer(text_of(c)) == g) for c, g in zip(completions, gold)]


def make_refgraph_reward(recs_by_iid):
    from selrm.reference import reference_graph

    def words(q):
        return {w for w in re.findall(r"[a-z0-9.]+", q.lower()) if len(w) > 3}

    def reward(completions, gold, iid_a, **_):
        out = []
        for c, g, ia in zip(completions, gold, iid_a):
            t = text_of(c)
            graph = reference_graph(recs_by_iid[ia])
            decisive = {e["from"] for e in graph["edges"] if e["to"].startswith("c:")
                        and any(n["id"] == e["to"] and n.get("decisive") for n in graph["nodes"])}
            quotes = [n["quote"] for n in graph["nodes"] if n["id"] in decisive]
            tw = words(" ".join(steps_of(t)))
            covered = any(words(q) and len(words(q) & tw) / len(words(q)) >= 0.6 for q in quotes)
            out.append(0.5 * covered + 0.5 * float(answer(t) == g))
        return out
    return reward


def make_ledger_reward(url, model_name, recs_by_iid):
    """Ledger-RM process reward through a vLLM OpenAI-compatible server (raw-logit logprobs)."""
    import urllib.request
    from transformers import AutoTokenizer
    from selrm import formats as F
    from selrm import prompts as P
    tok = AutoTokenizer.from_pretrained(model_name)

    def chat(t):
        return tok.apply_chat_template([{"role": "user", "content": t}], tokenize=False, add_generation_prompt=True,
                                       enable_thinking=False)

    def post(body):
        req = urllib.request.Request(url + "/v1/completions", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req, timeout=600))["choices"]

    def reward(completions, iid_a, **_):
        jobs = []
        for j, (c, ia) in enumerate(zip(completions, iid_a)):
            r = recs_by_iid[ia]
            for st in steps_of(text_of(c)):
                jobs.append((j, {"rule_text": r["rule_text"], "case_text": r["case_text"], "condition": st,
                                 "claim_text": st}))
        u = [[] for _ in completions]
        if jobs:
            reads = post({"model": model_name, "prompt": [chat(P.reader_prompt(x)) for _, x in jobs],
                          "max_tokens": 384, "temperature": 0, "stop_token_ids": [248046, 248044]})
            texts = [ch["text"] for ch in sorted(reads, key=lambda ch: ch["index"])]
            ok = [F.well_formed(t, x["case_text"], "ledger2") for t, (_, x) in zip(texts, jobs)]
            idx = [i for i, k in enumerate(ok) if k]
            if idx:
                judged = post({"model": model_name, "prompt": [chat(P.judge_prompt(jobs[i][1], texts[i])) for i in idx],
                               "max_tokens": 1, "temperature": 0, "logprobs": 20})
                for i, ch in zip(idx, sorted(judged, key=lambda ch: ch["index"])):
                    top = ch["logprobs"]["top_logprobs"][0]
                    lo = min(top.values())
                    u[jobs[i][0]].append(top.get("+", lo) - top.get("-", lo))
            for i, k in enumerate(ok):
                if not k:
                    u[jobs[i][0]].append(F.MALFORMED_U)
        return [1 / (1 + math.exp(-min(x))) if x else 0.0 for x in u]
    return reward


def make_stepcheck_reward(medprm_dir, recs_by_iid, device="cuda:1"):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    from score_pool import MEDPRM_SYSTEM
    tok = AutoTokenizer.from_pretrained(medprm_dir)
    model = AutoModelForCausalLM.from_pretrained(medprm_dir, dtype=torch.bfloat16).to(device).eval()
    plus = tok(" +", add_special_tokens=False)["input_ids"][0]
    minus = tok(" -", add_special_tokens=False)["input_ids"][0]

    def reward(completions, prompts, **_):
        out = []
        for c, p in zip(completions, prompts):
            st = steps_of(text_of(c))
            if not st:
                out.append(0.0)
                continue
            q = (p[-1]["content"] if isinstance(p, list) else p).split("\n\nDecide and justify")[0]
            expl = " ".join(f"Step {i + 1}:  {s} ки" for i, s in enumerate(st))
            t = tok.apply_chat_template([{"role": "system", "content": MEDPRM_SYSTEM},
                                         {"role": "user", "content": f"Question: {q}\n\nExplanation: {expl}"}],
                                        tokenize=False, add_generation_prompt=True)
            enc = tok(t, return_tensors="pt", return_offsets_mapping=True)
            offs = enc.pop("offset_mapping")[0].tolist()
            with torch.no_grad():
                lg = model(**{k: v.to(device) for k, v in enc.items()}).logits[0].float()
            pos = [i for i, (s0, e0) in enumerate(offs) if t[s0:e0] == " ки"]
            pr = torch.softmax(lg[pos][:, [plus, minus]], dim=-1)[:, 0]
            out.append(float(pr.min()) if len(pos) else 0.0)
        return out
    return reward


# ------------------------------------------------------------------ evaluation by the rule program
def evaluate(model, tok, items, max_new=512, bs=32):
    import torch
    model.eval()
    tok.padding_side = "left"
    right = {"base": [], "flip": [], "near": []}
    for i in range(0, len(items), bs):
        batch = items[i:i + bs]
        texts = [tok.apply_chat_template(x["prompt"], tokenize=False, add_generation_prompt=True,
                                         enable_thinking=False) for x in batch]
        enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
        with torch.no_grad():
            gen = model.generate(**enc, max_new_tokens=max_new, do_sample=False)
        for x, g in zip(batch, gen[:, enc["input_ids"].shape[1]:]):
            right[x["case_kind"]].append(answer(tok.decode(g, skip_special_tokens=True)) == x["gold"])
    model.train()
    acc = {k: 100.0 * sum(v) / len(v) for k, v in right.items() if v}
    acc["all"] = 100.0 * sum(sum(v) for v in right.values()) / sum(len(v) for v in right.values())
    return acc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reward", required=True, choices=["outcome", "refgraph", "ledger2-blocks", "ledger2-triplets",
                                                        "stepcheck"])
    ap.add_argument("--policy", required=True)
    ap.add_argument("--data", required=True, help="dir with rule_v1/<set>/records.jsonl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--steps", type=int, default=1000)
    ap.add_argument("--eval-every", dest="eval_every", type=int, default=200)
    ap.add_argument("--eval-triplets", dest="eval_triplets", type=int, default=150)
    ap.add_argument("--ledger-url", dest="ledger_url", default="http://127.0.0.1:8001")
    ap.add_argument("--ledger-model", dest="ledger_model", default=None)
    ap.add_argument("--medprm", default=None)
    ap.add_argument("--overfit", type=int, default=0, help="train on this many prompts only (64: setup check)")
    a = ap.parse_args()
    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoTokenizer, TrainerCallback
    from trl import GRPOConfig, GRPOTrainer
    os.makedirs(a.out, exist_ok=True)
    if os.path.exists(os.path.join(a.out, "DONE")):
        print("exists:", a.out)
        return
    train = load(os.path.join(a.data, "rule_v1", "train_triplets", "records.jsonl"))
    test = load(os.path.join(a.data, "rule_v1", "test_L2", "records.jsonl"))
    recs_by_iid = {r["iid"]: r for r in train}
    tr = tasks(train)
    rng = random.Random(f"grpo.{a.seed}")
    rng.shuffle(tr)
    if a.overfit:
        tr = tr[:a.overfit]
    tids = sorted({r["tid"] for r in test})
    keep = set(random.Random("grpo-eval-v1").sample(tids, min(a.eval_triplets, len(tids))))
    ev = tasks([r for r in test if r["tid"] in keep], tag="eval")
    reward = {"outcome": lambda: outcome_reward, "refgraph": lambda: make_refgraph_reward(recs_by_iid),
              "ledger2-blocks": lambda: make_ledger_reward(a.ledger_url, a.ledger_model, recs_by_iid),
              "ledger2-triplets": lambda: make_ledger_reward(a.ledger_url, a.ledger_model, recs_by_iid),
              "stepcheck": lambda: make_stepcheck_reward(a.medprm, recs_by_iid)}[a.reward]()
    reward.__name__ = a.reward.replace("-", "_")
    tok = AutoTokenizer.from_pretrained(a.policy)
    cfg = GRPOConfig(output_dir=os.path.join(a.out, "ckpt"), seed=a.seed, max_steps=a.steps, learning_rate=1e-5,
                     per_device_train_batch_size=8, gradient_accumulation_steps=1, num_generations=8,
                     max_completion_length=512, temperature=1.0, beta=0.0, logging_steps=10, save_steps=a.steps,
                     bf16=True, report_to=[], chat_template_kwargs={"enable_thinking": False},
                     model_init_kwargs={"dtype": torch.bfloat16}, remove_unused_columns=False)
    curve = []

    class Eval(TrainerCallback):
        def on_step_end(self, args, state, control, model=None, **kw):
            if state.global_step % a.eval_every == 0 or state.global_step == a.steps:
                rew = [h.get("reward") for h in state.log_history[-max(1, a.eval_every // 10):] if "reward" in h]
                acc = evaluate(model, tok, ev)
                row = {"step": state.global_step, "reward": sum(rew) / len(rew) if rew else None} | acc
                curve.append(row)
                with open(os.path.join(a.out, "curve.jsonl"), "a", encoding="utf-8") as f:
                    f.write(json.dumps(row) + "\n")
                print("eval", row, flush=True)

    t0 = time.time()
    trainer = GRPOTrainer(model=a.policy, reward_funcs=[reward], args=cfg, train_dataset=Dataset.from_list(tr),
                          processing_class=tok, callbacks=[Eval()],
                          peft_config=LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM",
                                                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj",
                                                                 "up_proj", "down_proj"]))
    start = evaluate(trainer.model, tok, ev)
    curve.insert(0, {"step": 0, "reward": None} | start)
    trainer.train()
    final = curve[-1]
    run_id = os.path.basename(a.out.rstrip("/"))
    json.dump({"run_id": run_id, "set": "rule_v1/test_L2", "metric": "accuracy of the chosen claim by the rule program",
               "n_triplets": len(keep), "start": start, "final": {k: v for k, v in final.items() if k != "step"},
               "top": None} | {f"acc_{k}": v for k, v in final.items() if k not in ("step", "reward")},
              open(os.path.join(a.out, "summary_rule_v1~test_L2.json"), "w", encoding="utf-8"), indent=1)
    json.dump({"run_id": run_id, "reward": a.reward, "policy": a.policy, "seed": a.seed, "steps": a.steps,
               "train_tasks": len(tr), "eval_tasks": len(ev), "group_size": 8, "lora_r": 16, "lr": 1e-5,
               "wall_seconds": round(time.time() - t0, 1), "gpu": torch.cuda.get_device_name(0)},
              open(os.path.join(a.out, "meta.json"), "w", encoding="utf-8"), indent=1)
    open(os.path.join(a.out, "DONE"), "w").close()


if __name__ == "__main__":
    main()
