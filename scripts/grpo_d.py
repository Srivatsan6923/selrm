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
  summary2-triplets  the same with the two-stage prose-summary model trained on triplets (reader writes a
                prose summary of the evidence; no structure check), served the same way
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


def make_ledger_reward(url, model_name, recs_by_iid, fmt="ledger2"):
    """Two-stage process reward (Ledger-RM, fmt ledger2; prose summary, fmt summary2) through a vLLM
    OpenAI-compatible server (raw-logit logprobs), with the reader and judge prompts of scripts/score_pool.py."""
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
            reads = post({"model": model_name, "prompt": [chat(P.reader_prompt(x, prose=fmt == "summary2")) for _, x in jobs],
                          "max_tokens": 384, "temperature": 0, "stop_token_ids": [248046, 248044]})
            texts = [ch["text"] for ch in sorted(reads, key=lambda ch: ch["index"])]
            ok = [F.well_formed(t, x["case_text"], fmt) for t, (_, x) in zip(texts, jobs)]
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


def outcome_monitor(completions, gold, **_):
    """The rule program's outcome on the training rollouts, logged with weight 0 (reward against program accuracy)."""
    return outcome_reward(completions, gold)


def with_group_log(reward, out_dir, group):
    """Per reward call (completions come in consecutive groups of one prompt): the share of groups whose rewards
    vary (GRPO learns only from those) and the mean within-group Pearson correlation of the reward with the rule
    program's outcome (the collinearity check before each run; reward exploitation during it) -> groups.jsonl."""
    import statistics

    def f(**kw):
        r = reward(**kw)
        o = outcome_reward(kw["completions"], kw["gold"])
        vary, corr = 0, []
        for i in range(0, len(r), group):
            rg, og = r[i:i + group], o[i:i + group]
            if len(set(rg)) > 1:
                vary += 1
                if len(set(og)) > 1:
                    corr.append(statistics.correlation(rg, og))
        n = max(1, len(r) // group)
        with open(os.path.join(out_dir, "groups.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"groups": n, "share_varying": vary / n, "n_corr": len(corr),
                                 "corr_with_outcome": statistics.fmean(corr) if corr else None}) + "\n")
        return r
    f.__name__ = reward.__name__
    return f


def make_stepcheck_reward(medprm_dir, recs_by_iid, device="cuda:0"):
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
def evaluate(model, tok, items, max_new=512, bs=32, out=None):
    """Greedy answers judged by the rule program's labels: accuracy per case kind, on base-flip pairs
    (both right; v13's policy-training metric) and on whole triplets. With out: one line per task
    {tid, case_kind, gold, answer, correct, text} (per-example outputs of every evaluation)."""
    import torch
    model.eval()
    tok.padding_side = "left"
    per, rows = {}, []
    for i in range(0, len(items), bs):
        batch = items[i:i + bs]
        texts = [tok.apply_chat_template(x["prompt"], tokenize=False, add_generation_prompt=True,
                                         enable_thinking=False) for x in batch]
        enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
        with torch.no_grad():
            gen = model.generate(**enc, max_new_tokens=max_new, do_sample=False)
        for x, g in zip(batch, gen[:, enc["input_ids"].shape[1]:]):
            text = tok.decode(g, skip_special_tokens=True)
            ans = answer(text)
            per.setdefault(x["tid"], {})[x["case_kind"]] = ans == x["gold"]
            rows.append({"tid": x["tid"], "case_kind": x["case_kind"], "gold": x["gold"], "answer": ans,
                         "correct": ans == x["gold"], "iid_a": x["iid_a"], "iid_b": x["iid_b"], "text": text})
    if out:
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.writelines(json.dumps(r) + "\n" for r in rows)
    model.train()
    return accuracy(rows)


def accuracy(rows):
    """Rows {tid, case_kind, correct} -> accuracy per case kind, on base-flip pairs and on whole triplets."""
    per = {}
    for r in rows:
        per.setdefault(r["tid"], {})[r["case_kind"]] = r["correct"]
    pct = lambda xs: 100.0 * sum(xs) / len(xs) if xs else None
    acc = {k: pct([t[k] for t in per.values() if k in t]) for k in ("base", "flip", "near")}
    acc["all"] = pct([v for t in per.values() for v in t.values()])
    acc["pair"] = pct([t["base"] and t["flip"] for t in per.values() if {"base", "flip"} <= set(t)])
    acc["triplet"] = pct([all(t.values()) for t in per.values() if len(t) == 3])
    return acc


XR_KINDS = ("contested", "positive", "negative")     # xr_v1: two rules x these three cases per item


def crossed(rows, records, exclude=()):
    """XA of a policy on xr_v1 (selrm.metrics.crossed_accuracy, as C reports it): the chosen claim scores +1 and
    the other -1; no answer scores 0 for both, a tie, which fails the cell."""
    from selrm import metrics as M
    u = {}
    for r in rows:
        if r["answer"] in ("A", "B"):
            win, lose = (r["iid_a"], r["iid_b"]) if r["answer"] == "A" else (r["iid_b"], r["iid_a"])
            u[win], u[lose] = 1.0, -1.0
    return M.crossed_accuracy(records, [u.get(rec["iid"], 0.0) for rec in records], exclude=exclude)


def summarize_xr(out_dir, records, run_id):
    """summary_xr_v1~test.json from eval_xr_step<N>.jsonl: XA of the final policy on all 400 items (top level) and
    without A's known issues; the untrained policy's values under start*."""
    steps = sorted(int(m.group(1)) for m in (re.match(r"eval_xr_step(\d+)\.jsonl$", f) for f in os.listdir(out_dir)) if m)
    load_rows = lambda n: [json.loads(x) for x in open(os.path.join(out_dir, f"eval_xr_step{n}.jsonl"), encoding="utf-8")]
    known = {i for x in json.load(open(os.path.join(ROOT, "data", "xr_v1", "KNOWN_ISSUES.json"), encoding="utf-8"))["issues"]
             for i in x["items"]}
    final = load_rows(steps[-1])
    summ = {"run_id": run_id, "set": "xr_v1/test", "claim_type": "conclusion"} | crossed(final, records) | {
        "without_known_issues": crossed(final, records, exclude=known), "final_step": steps[-1],
        "from_files": [f"eval_xr_step{steps[-1]}.jsonl"]}
    if steps[0] == 0 and len(steps) > 1:     # the run also holds the untrained policy's answers
        start = load_rows(0)
        summ |= {"start": crossed(start, records), "start_without_known_issues": crossed(start, records, exclude=known)}
    json.dump(summ, open(os.path.join(out_dir, "summary_xr_v1~test.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    return summ


def tg_classes(rows, records):
    """TrialGPT criterion items (C's clin_v1/trialgpt_test; docs/TRIALGPT_PROTOCOL.md): truth from the claim labels
    (met: 'meets' claim labelled 1; not met: 'does not meet' labelled 1; NEI otherwise), N/A items left out; a
    policy's class from its choice, and NEI when it gives no final answer (a policy cannot abstain otherwise)."""
    by = {}
    for r in records:
        by.setdefault(r["tid"], {})[r["claim_role"]] = r
    gold, pred = [], []
    role = {r["iid"]: r["claim_role"] for r in records}
    for row in rows:
        c = by[row["tid"]]
        if c["s"]["meta"]["expert_eligibility"] == "not applicable":
            continue
        g = "met" if int(c["s"]["label"]) == 1 else "not met" if int(c["s_prime"]["label"]) == 1 else "NEI"
        ch = {"A": row["iid_a"], "B": row["iid_b"]}.get(row["answer"])
        gold.append(g)
        pred.append("NEI" if ch is None else "met" if role[ch] == "s" else "not met")
    return gold, pred


def summarize_tg(out_dir, records, run_id):
    """summary_clin_v1~trialgpt_test.json from eval_tg_step<N>.jsonl: macro-F1 over {met, not met, NEI} on the
    non-N/A items (primary, as C reports systems) and forced-choice accuracy on met / not-met items."""
    from selrm import metrics as M
    steps = sorted(int(m.group(1)) for m in (re.match(r"eval_tg_step(\d+)\.jsonl$", f) for f in os.listdir(out_dir)) if m)
    rows = [json.loads(x) for x in open(os.path.join(out_dir, f"eval_tg_step{steps[-1]}.jsonl"), encoding="utf-8")]
    gold, pred = tg_classes(rows, records)
    res = M.prf(gold, pred, labels=["met", "not met", "NEI"])
    fc = [p == g for g, p in zip(gold, pred) if g != "NEI"]
    summ = {"run_id": run_id, "set": "clin_v1/trialgpt_test", "macroF1": res["macroF1"], "acc": res["acc"],
            "per_class": res["per_class"], "confusion": res["confusion"], "n": res["n"],
            "forced_choice_acc": 100.0 * sum(fc) / len(fc) if fc else None, "n_forced": len(fc),
            "no_answer_share": 100.0 * sum(r["answer"] is None for r in rows) / len(rows),
            "final_step": steps[-1], "from_files": [f"eval_tg_step{steps[-1]}.jsonl"],
            "scoring": "no final answer = NEI; N/A items left out (docs/TRIALGPT_PROTOCOL.md classes)"}
    json.dump(summ, open(os.path.join(out_dir, "summary_clin_v1~trialgpt_test.json"), "w", encoding="utf-8",
                         newline="\n"), indent=1)
    return summ


def summarize(out_dir):
    """summary_rule_v1~test_L2.json from the run's per-example evaluation files: start = eval_step0.jsonl, final =
    the highest eval_step<N>.jsonl; the in-training curve (curve.jsonl) is kept as it is."""
    steps = sorted(int(m.group(1)) for m in (re.match(r"eval_step(\d+)\.jsonl$", f) for f in os.listdir(out_dir)) if m)
    load_rows = lambda n: [json.loads(x) for x in open(os.path.join(out_dir, f"eval_step{n}.jsonl"), encoding="utf-8")]
    start, final = accuracy(load_rows(0)), accuracy(load_rows(steps[-1]))
    p = os.path.join(out_dir, "summary_rule_v1~test_L2.json")
    old = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    # the training curve (curve.jsonl: in-training evaluation every --eval-every steps, training reward and the
    # rule program's outcome on the rollouts) as slices step=<n>; step 0 = the untrained policy of eval_step0
    cp = os.path.join(out_dir, "curve.jsonl")
    curve = [json.loads(x) for x in open(cp, encoding="utf-8")] if os.path.exists(cp) else []
    step = {"0": dict(start)} | {str(c["step"]): {k: v for k, v in c.items() if k != "step"} for c in curve}
    summ = {k: v for k, v in old.items() if not k.startswith("acc_")} | {
        "start": start, "final": final, "final_step": steps[-1], "n_triplets": len({r["tid"] for r in load_rows(0)}),
        "step": step,
        "from_files": ["eval_step0.jsonl", f"eval_step{steps[-1]}.jsonl"]} | {f"acc_{k}": v for k, v in final.items()} | {
        f"start_{k}": v for k, v in start.items()}
    json.dump(summ, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
    return summ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reward", required=True, choices=["outcome", "refgraph", "ledger2-blocks", "ledger2-triplets",
                                                        "summary2-triplets", "stepcheck"])
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
    ap.add_argument("--vllm-mem", dest="vllm_mem", type=float, default=0.35,
                    help="GPU memory share of the rollout engine (0.25 when the ledger server shares the GPU)")
    ap.add_argument("--overfit", type=int, default=0, help="train on this many prompts only (64: setup check)")
    ap.add_argument("--smoke", action="store_true", help="plumbing check on CPU with a small policy: groups of 4, "
                                                          "32-token completions; never a result")
    ap.add_argument("--eval-from", dest="eval_from", nargs="+", default=None,
                    help="no training: evaluate 'base' (the untrained policy) and/or LoRA checkpoint dirs of a run on "
                         "its evaluation triplets -> OUT/eval_step<N>.jsonl (N = 0 for base, else the checkpoint step)")
    ap.add_argument("--eval-sets", dest="eval_sets", nargs="+", default=["l2"], choices=["l2", "xr", "tg"],
                    help="with --eval-from: l2 = the run's held-out L2 triplets; xr = xr_v1 (all 400 items, "
                         "OUT/eval_xr_step<N>.jsonl and summary_xr_v1~test.json); tg = TrialGPT test criteria "
                         "(OUT/eval_tg_step<N>.jsonl and summary_clin_v1~trialgpt_test.json)")
    ap.add_argument("--tg-records", dest="tg_records", default="/pvc/data/clin_v1/trialgpt_test/records.jsonl")
    a = ap.parse_args()
    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoTokenizer, TrainerCallback
    from trl import GRPOConfig, GRPOTrainer
    os.makedirs(a.out, exist_ok=True)
    if not a.eval_from and os.path.exists(os.path.join(a.out, "DONE")):
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
    if a.eval_from:
        import transformers
        from peft import PeftModel
        from transformers import AutoConfig
        tok = AutoTokenizer.from_pretrained(a.policy)
        # the class TRL trained (Qwen3.5: the image-text wrapper, adapter keys model.language_model.*); the text-only
        # class matches none of the adapter's keys and PEFT then leaves the policy untrained without an error
        arch = AutoConfig.from_pretrained(a.policy).architectures[0]
        base = getattr(transformers, arch).from_pretrained(a.policy, dtype=torch.bfloat16).to("cuda")
        xr = load(os.path.join(a.data, "xr_v1", "test", "records.jsonl")) if "xr" in a.eval_sets else []
        tg = load(a.tg_records) if "tg" in a.eval_sets else []
        sets = {"l2": (ev, "eval_step"), "xr": (tasks(xr, kinds=XR_KINDS, tag="xr"), "eval_xr_step"),
                "tg": (tasks(tg, kinds=("base",), tag="tg"), "eval_tg_step")}
        for src in a.eval_from:
            m = re.search(r"checkpoint-(\d+)", src)
            model = base if src == "base" else PeftModel.from_pretrained(base, src)
            if src != "base" and not sum(float(p.abs().sum()) for n, p in model.named_parameters() if "lora_B" in n):
                sys.exit(f"adapter of {src} not applied (every lora_B is zero)")
            for name in a.eval_sets:
                items, stem = sets[name]
                acc = evaluate(model, tok, items, out=os.path.join(a.out, f"{stem}{m.group(1) if m else 0}.jsonl"))
                print("eval-from", src, name, json.dumps(acc), flush=True)
            if src != "base":
                base = model.unload()
        if a.eval_from == ["base"] and not os.path.exists(os.path.join(a.out, "DONE")):
            # the untrained policy as a run of its own (D-RL-untrained): the start of every reward, evaluated once
            json.dump({"run_id": os.path.basename(a.out.rstrip("/")), "policy": a.policy, "steps": 0,
                       "what": "untrained policy, greedy evaluation", "gpu": torch.cuda.get_device_name(0)},
                      open(os.path.join(a.out, "meta.json"), "w", encoding="utf-8", newline="\n"), indent=1)
            open(os.path.join(a.out, "DONE"), "w").close()
        if "l2" in a.eval_sets and os.path.exists(os.path.join(a.out, "DONE")):   # summary rests on these files
            print("summary", json.dumps(summarize(a.out)), flush=True)
        if xr:
            print("xr", json.dumps(summarize_xr(a.out, xr, os.path.basename(a.out.rstrip("/")))), flush=True)
        if tg:
            print("tg", json.dumps(summarize_tg(a.out, tg, os.path.basename(a.out.rstrip("/")))), flush=True)
        return
    reward = {"outcome": lambda: outcome_reward, "refgraph": lambda: make_refgraph_reward(recs_by_iid),
              "ledger2-blocks": lambda: make_ledger_reward(a.ledger_url, a.ledger_model, recs_by_iid),
              "ledger2-triplets": lambda: make_ledger_reward(a.ledger_url, a.ledger_model, recs_by_iid),
              "summary2-triplets": lambda: make_ledger_reward(a.ledger_url, a.ledger_model, recs_by_iid, "summary2"),
              "stepcheck": lambda: make_stepcheck_reward(a.medprm, recs_by_iid)}[a.reward]()
    reward.__name__ = a.reward.replace("-", "_")
    group = 4 if a.smoke else 8
    reward = with_group_log(reward, a.out, group)
    funcs = [reward] + ([outcome_monitor] if a.reward != "outcome" else [])
    tok = AutoTokenizer.from_pretrained(a.policy)
    cfg = GRPOConfig(output_dir=os.path.join(a.out, "ckpt"), seed=a.seed, max_steps=a.steps, learning_rate=1e-5,
                     # 16 x 4 = 64 completions per optimiser step = 8 prompts x group of 8
                     per_device_train_batch_size=4 if a.smoke else 16, gradient_accumulation_steps=1 if a.smoke else 4,
                     num_generations=group, max_completion_length=32 if a.smoke else 512,
                     # GRPO loss, advantages standardised within a group (v13 App. G); the outcome monitor has
                     # weight 0; rollouts from vLLM inside the training process (TRL 'colocate')
                     loss_type="grpo", scale_rewards="group", reward_weights=[1.0] + [0.0] * (len(funcs) - 1),
                     use_vllm=not a.smoke, vllm_mode="colocate", vllm_gpu_memory_utilization=a.vllm_mem,
                     vllm_max_model_length=4096,
                     # checkpoints at every evaluation: a preempted pod resumes from the last one (Job retry)
                     temperature=1.0, beta=0.0, logging_steps=1 if a.smoke else 10, save_steps=a.eval_every,
                     save_total_limit=1,
                     bf16=not a.smoke, report_to=[], chat_template_kwargs={"enable_thinking": False},
                     model_init_kwargs={"dtype": torch.bfloat16}, remove_unused_columns=False)
    curve = []

    def window(state, key):
        xs = [h[key] for h in state.log_history[-max(1, a.eval_every // 10):] if key in h]
        return sum(xs) / len(xs) if xs else None

    class Eval(TrainerCallback):
        def on_step_end(self, args, state, control, model=None, **kw):
            if state.global_step % a.eval_every == 0 or state.global_step == a.steps:
                acc = evaluate(model, tok, ev, *((32, 4) if a.smoke else ()),
                               out=os.path.join(a.out, f"eval_step{state.global_step}.jsonl"))
                row = {"step": state.global_step, "reward": window(state, "reward"),
                       "train_outcome": window(state, "rewards/outcome_monitor/mean" if a.reward != "outcome"
                                               else "rewards/outcome/mean")} | acc
                curve.append(row)
                with open(os.path.join(a.out, "curve.jsonl"), "a", encoding="utf-8") as f:
                    f.write(json.dumps(row) + "\n")
                print("eval", row, flush=True)

    t0 = time.time()
    trainer = GRPOTrainer(model=a.policy, reward_funcs=funcs, args=cfg, train_dataset=Dataset.from_list(tr),
                          processing_class=tok, callbacks=[Eval()],
                          peft_config=LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM",
                                                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj",
                                                                 "up_proj", "down_proj"]))
    start = evaluate(trainer.model, tok, ev, *((32, 4) if a.smoke else ()), out=os.path.join(a.out, "eval_step0.jsonl"))
    curve.insert(0, {"step": 0, "reward": None} | start)
    ck = os.path.join(a.out, "ckpt")
    trainer.train(resume_from_checkpoint=True if os.path.isdir(ck) and any(
        d.startswith("checkpoint-") for d in os.listdir(ck)) else None)
    run_id = os.path.basename(a.out.rstrip("/"))
    json.dump({"run_id": run_id, "set": "rule_v1/test_L2", "metric": "accuracy of the chosen claim by the rule program",
               "top": None}, open(os.path.join(a.out, "summary_rule_v1~test_L2.json"), "w", encoding="utf-8"), indent=1)
    summarize(a.out)
    json.dump({"run_id": run_id, "reward": a.reward, "policy": a.policy, "seed": a.seed, "steps": a.steps,
               "train_tasks": len(tr), "eval_tasks": len(ev), "group_size": 8, "lora_r": 16, "lr": 1e-5,
               "wall_seconds": round(time.time() - t0, 1), "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"},
              open(os.path.join(a.out, "meta.json"), "w", encoding="utf-8"), indent=1)
    open(os.path.join(a.out, "DONE"), "w").close()


if __name__ == "__main__":
    main()
