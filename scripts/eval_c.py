"""Role-C GPU runner. Scores base models and B's adapters with B's scoring code
(eval_local.Scorer / evaluate: frozen prompts, u = logit("+") - logit("-") at the answer
position, two-stage reader generated once per (case, condition), malformed ledger -> u = -20),
so C's rows and B's rows come from one code path (INTERFACES 3).
  python scripts/eval_c.py --root ROOT --broot BROOT --bcode BCODE --tasks TASKS.json
Task file: {"runs": [{"run_id", "format", "adapter": null | path, "sets": [...], "priority",
            "max_new": 384, "min_gb": 0, "nocase": false, "rejudge_from": null, "hp": {...}}]}
Sets named rule_v1* are read from B's root (records and pre-tokenised prompts, read-only);
other sets (clin_v1/..., xr_v1/...) from C's root, pre-tokenised here on first use with B's
functions (same tokenizer, same chat template). Outputs per run:
ROOT/results/<run_id>/{meta.json, scores_<set>.jsonl, summary_<set>.json, run.log, gpu_util.csv, DONE}.
nocase: score copies of the sets with case_text "" (default correction, u(s, no case)).
rejudge_from: no generation; the source run's reader outputs are normalised by lenient_ledger()
(format-normalised readout of untrained readers) and judged; claimable once the source is DONE.
Runs with these options go in task files that only runners with this code read."""
import argparse, gc, json, os, re, socket, sys, time, traceback

KEYS = ("need", "found", "subject", "status", "time")
GEN = 3     # runner capability generation: runs with min_gen > GEN are skipped (3: topk, n_groups subsets, budgets)
LENIENT_VERSION = 2      # 2: markdown tables (decided on the development sets, 3 Oct, before any test scoring)


def table_entries(text):
    """Entries of a markdown table whose header names the five fields (any order, any case), or None."""
    rows = [l.strip() for l in text.replace("\r", "").split("\n") if l.strip().startswith("|")]
    if len(rows) < 2:
        return None
    head = [c.strip().strip("*").strip().lower() for c in rows[0].strip("|").split("|")]
    if not set(KEYS) <= set(head):
        return None
    entries = []
    for row in rows[1:]:
        cells = [c.strip() for c in row.strip("|").split("|")]
        if all(re.fullmatch(r"[\s:\-]*", c) for c in cells):          # separator row
            continue
        if len(cells) != len(head):
            return None
        entries.append({k: cells[head.index(k)].replace("**", "").strip() for k in KEYS})
    return entries


def lenient_ledger(text, case_text):
    """Canonical ledger text from a reader output with markdown noise, or None.
    A markdown table with the five fields as columns gives one entry per row. Otherwise:
    strips code fences, bullets, numbering and bold/italic markers; reads 'key: value'
    lines whose key is a ledger field (any case); a 'need' line opens an entry; other
    lines are ignored. Every entry needs the five fields in order; a quoted found is
    unquoted; found must be 'not mentioned' or a verbatim substring of the case, as in
    the strict check. ponytail: line-based; a value continued on a second line is cut."""
    entries, cur = table_entries(text), None
    for raw in ([] if entries else text.replace("\r", "").split("\n")):
        line = raw.strip().strip("`").strip()
        line = re.sub(r"^(?:[-*\u2022+]|\d+[.)])\s+", "", line).replace("**", "").replace("__", "")
        line = re.sub(r"^[*_]+([A-Za-z]+)[*_]+\s*:", r"\1:", line)
        m = re.match(r"^([A-Za-z]+)\s*:\s*(.*)$", line)
        if not m or m.group(1).lower() not in KEYS:
            continue
        k, v = m.group(1).lower(), m.group(2).strip()
        if k == "need":
            cur = {}
            entries = (entries or []) + [cur]
        if cur is None or k in cur:
            return None
        cur[k] = v
    if not entries:
        return None
    for e in entries:
        if tuple(e) != KEYS or not all(e.values()):
            return None
        f = e["found"]
        if len(f) >= 2 and f[0] == f[-1] and f[0] in "\"'":
            f = f[1:-1].strip()
        if f.lower().rstrip(".") == "not mentioned":
            f = "not mentioned"
        elif not f or f not in case_text:
            return None
        e["found"] = f
    return "\n\n".join("\n".join(f"{k}: {e[k]}" for k in KEYS) for e in entries)


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def rejudge(sc, root, rid, set_name, src_dir, out_dir, log):
    """Format-normalised readout of another run's reader outputs (lenient_ledger, LENIENT_VERSION):
    the judge reads the normalised ledger; judge forward passes only, nothing is regenerated.
    Malformed after normalisation -> u = -20 for both claims, as in the strict check."""
    import eval_local
    from selrm.formats import MALFORMED_U, dataset_path, reader_unit
    from selrm.prompts import judge_prompt
    t0 = time.time()
    recs = load_jsonl(dataset_path(root, set_name))
    name = set_name.replace("/", "~")
    out = {r["iid"]: r["reader_output"] for r in load_jsonl(f"{src_dir}/scores_{name}.jsonl")}
    norm = {}
    for r in recs:
        k = reader_unit(r)
        if k not in norm:
            norm[k] = lenient_ledger(out[r["iid"]], r["case_text"])
    idx = [i for i, r in enumerate(recs) if norm[reader_unit(r)] is not None]
    u = [MALFORMED_U] * len(recs)
    if idx:
        got = sc.score(eval_local.chat_ids(sc.tok, [judge_prompt(recs[i], norm[reader_unit(recs[i])]) for i in idx]))
        for i, x in zip(idx, got):
            u[i] = float(x)
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/scores_{name}.jsonl", "w", encoding="utf-8") as f:
        for r, x in zip(recs, u):
            f.write(json.dumps({"iid": r["iid"], "u": x, "reader_output": out[r["iid"]],
                                "ledger_lenient": norm[reader_unit(r)]}) + "\n")
    summ = eval_local.summarize(recs, u, rid, set_name)
    bad = sum(v is None for v in norm.values())
    summ["eval"] = {"reader_units": len(norm), "malformed_units": bad, "malformed_rate": round(bad / max(1, len(norm)), 4),
                    "seconds": round(time.time() - t0, 1), "mode": "rejudge", "lenient_version": LENIENT_VERSION,
                    "source_run": os.path.basename(src_dir)}
    json.dump(summ, open(f"{out_dir}/summary_{name}.json", "w"), indent=1)
    a = summ.get("all", {})
    log(f"{rid} {set_name} rejudge (lenient v{LENIENT_VERSION}): TA {a.get('TA', float('nan')):.1f} malformed {bad}/{len(norm)}")
    return summ


def build_eval_c(root, fmt, tag, set_name, tok):
    """pretok.build_eval for C's sets: same prompts, chat template and packing; without the
    gold-ledger check, since external sets (clin_v1) carry no program ledger."""
    import numpy as np, pretok
    from selrm.formats import dataset_path, reader_units
    spec = {"format": fmt, "base_model": tag.replace("--", "/")}
    path = pretok.eval_path(root, spec, set_name)
    if os.path.exists(path):
        return path, "exists"
    kind = pretok.EVAL_KIND[fmt]
    recs = load_jsonl(dataset_path(root, set_name))
    if kind in pretok.PROMPT:
        keys, texts = [r["iid"] for r in recs], [pretok.PROMPT[kind](r) for r in recs]
    else:
        from selrm.prompts import reader_prompt
        units = reader_units(recs)
        keys = ["/".join(r["iid"].split("/")[:2]) for r in units]
        texts = [reader_prompt(r, prose=kind == "reader_prose") for r in units]
    ids, off = pretok.pack(pretok.tok_ids(tok, [pretok.chat(tok, t) for t in texts]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pretok.save_npz(path, ids=ids, off=off, keys=np.asarray(keys), vocab=np.asarray(len(tok)))
    return path, f"built {len(keys)} prompts, max {int(np.diff(off).max())} tokens"


def subset(recs, n=0, claim_types=("conclusion",)):
    """Records of the given claim types; with n, the fixed group subset of scripts/run_judge.py (n / #kinds groups
    per near-miss kind, random.Random(0) over sorted group ids), so audit rows share their items."""
    import random
    recs = [r for r in recs if r["claim_type"] in claim_types]
    if not n:
        return recs
    by = {}
    for r in recs:
        by.setdefault(r["nm_kind"], set()).add(r["tid"])
    keep = set()
    for kind in sorted(by):
        keep |= set(random.Random(0).sample(sorted(by[kind]), min(len(by[kind]), n // len(by))))
    return [r for r in recs if r["tid"] in keep]


def run_prm(spec, a, mon, log, owner):
    """A released PRM as released (scripts/prms/<module>.py: load, score), weights downloaded at their pinned
    revision to local disk (the Job runs with the Hub online). Scores the step = claim after rule and case."""
    import importlib.util, torch
    import eval_local
    from selrm import runq
    from selrm.formats import dataset_path
    rid = spec["run_id"]
    rdir = f"{a.root}/results/{rid}"
    log.paths.append(f"{rdir}/run.log")
    mon.start_run(rdir)
    t0, model = time.time(), None
    try:
        from huggingface_hub import snapshot_download
        here = os.path.dirname(os.path.abspath(__file__))
        ms = importlib.util.spec_from_file_location(spec["prm"], f"{here}/prms/{spec['prm']}.py")
        mod = importlib.util.module_from_spec(ms)
        ms.loader.exec_module(mod)
        hf_id, rev = spec.get("hf_id", mod.HF_ID), spec.get("revision", mod.REVISION)
        mdir = snapshot_download(hf_id, revision=rev, local_dir=f"/work/prm/{hf_id.replace('/', '--')}", max_workers=4)
        bdir = None
        if getattr(mod, "BASE_ID", None):
            bdir = snapshot_download(mod.BASE_ID, revision=mod.BASE_REVISION,
                                     local_dir=f"/work/prm/{mod.BASE_ID.replace('/', '--')}", max_workers=4)
        log(f"downloaded {hf_id}@{rev} (base {getattr(mod, 'BASE_ID', None)}) in {time.time() - t0:.0f} s")
        model, tok = mod.load(mdir, bdir)
        summ, secs = {}, {}
        for s in spec["sets"]:
            root = a.broot if s.startswith("rule_v1") else a.root
            recs = subset(load_jsonl(dataset_path(root, s)), spec.get("n_groups", 0), tuple(spec.get("claim_types", ["conclusion"])))
            ts = time.time()
            # length tiers keep long inputs (MedEinst, NLI4CT-P) in small batches; the wrapper batches within a tier
            u, outs = [0.0] * len(recs), [None] * len(recs)
            size = lambda r: len(r["rule_text"]) + len(r["case_text"]) + len(r["claim_text"])
            for lo, hi, div in ((0, 3000, 1), (3000, 8000, 2), (8000, 10**9, 8)):
                idx = [i for i, r in enumerate(recs) if lo <= size(r) < hi]
                if not idx:
                    continue
                part = mod.score(model, tok, [recs[i] for i in idx], batch_size=max(1, spec.get("bs", 8) // div),
                                 max_new_tokens=spec.get("max_new"), log=log)
                po = getattr(mod, "LAST_OUTPUTS", None)
                for k, i in enumerate(idx):
                    u[i] = part[k]
                    if po is not None and len(po) == len(idx):
                        outs[i] = po[k]
            outs = outs if any(o is not None for o in outs) else None
            name = s.replace("/", "~")
            os.makedirs(rdir, exist_ok=True)
            with open(f"{rdir}/scores_{name}.jsonl", "w", encoding="utf-8") as f:
                for i, (r, x) in enumerate(zip(recs, u)):
                    row = {"iid": r["iid"], "u": float(x)}
                    if outs is not None and len(outs) == len(recs):
                        row["reader_output"] = outs[i]
                    f.write(json.dumps(row) + "\n")
            summ[s] = eval_local.summarize(recs, list(u), rid, s)
            secs[s] = round(time.time() - ts, 1)
            summ[s]["eval"] = {"seconds": secs[s], "n_records": len(recs), "n_groups": spec.get("n_groups") or "all",
                               "claim_types": spec.get("claim_types", ["conclusion"])}
            json.dump(summ[s], open(f"{rdir}/summary_{name}.json", "w"), indent=1)
            log(f"{rid} {s}: TA {summ[s].get('all', {}).get('TA', float('nan')):.1f} ({secs[s]} s, {len(recs)} records)")
        vers, gpu = __import__("train_eval_job").versions()
        meta = {"run_id": rid, "role": "C", "model": hf_id, "model_revision": rev, "base": getattr(mod, "BASE_ID", None),
                "base_revision": getattr(mod, "BASE_REVISION", None), "prm_module": spec["prm"],
                "prompt_note": getattr(mod, "PROMPT_NOTE", None), "provider": "local (NRP Nautilus), as released",
                "access_date": time.strftime("%Y-%m-%d"), "sets": spec["sets"], "n_groups": spec.get("n_groups") or "all",
                "max_new": spec.get("max_new"), "eval_seconds_by_set": secs, "versions": vers, "gpu": gpu,
                "node": os.environ.get("NODE_NAME"), "pod": owner, "wall_seconds": round(time.time() - t0, 1),
                "eval_peak_mem_gb": round(torch.cuda.max_memory_reserved() / 2**30, 2) if torch.cuda.is_available() else None,
                "summaries": {s: (v or {}).get("all") for s, v in summ.items()}}
        meta |= mon.end_run()
        json.dump(meta, open(f"{rdir}/meta.json", "w"), indent=1)
        runq.release(rdir, ok=True)
        log(f"DONE {rid} in {meta['wall_seconds'] / 60:.1f} min")
    except Exception:
        tb = traceback.format_exc()
        log(f"FAILED {rid}\n{tb}")
        runq.release(rdir, ok=False, reason=json.dumps(mon.end_run()) + "\n" + tb)
        if "CUDA" in tb or "out of memory" in tb:
            os._exit(2)
    finally:
        log.paths = log.paths[:1]
        model = None
        gc.collect()
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def topk_pass(sc, root, rid, set_name, out_dir, log, tag, k=50):
    """Verdict prompts of a set: the top-k next-token logits (fp32) at the answer position, per record, for an
    exact offline simulation of a sampled readout (scripts/noise_check.py). Same pre-tokenised prompts as the
    log-odds readout; one forward pass per record."""
    import torch
    import eval_local
    from selrm.formats import dataset_path
    t0 = time.time()
    recs = load_jsonl(dataset_path(root, set_name))
    seqs, keys = eval_local.unpack(f"{root}/tok/{tag}/eval/{set_name}/verdict.npz", len(sc.tok))
    assert keys == [r["iid"] for r in recs], "eval prompts out of sync with records"
    rows = [None] * len(seqs)
    with torch.no_grad():
        for b in sc._batches(seqs, sc.bs_score):
            ids, att = sc._left_pad([seqs[i] for i in b])
            lg = sc.model(input_ids=ids, attention_mask=att, logits_to_keep=1, use_cache=False).logits[:, -1, :].float()
            if sc.scale != 1.0:
                lg = lg * sc.scale
            v, ix = lg.topk(k, dim=-1)
            lse = torch.logsumexp(lg, dim=-1)
            for j, i in enumerate(b):
                rows[i] = {"iid": recs[i]["iid"], "top_ids": ix[j].tolist(), "top_logits": [round(x, 4) for x in v[j].tolist()],
                           "logsumexp": float(lse[j]), "plus": float(lg[j, sc.plus]), "minus": float(lg[j, sc.minus])}
    name = set_name.replace("/", "~")
    with open(f"{out_dir}/topk_{name}.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    log(f"{rid} {set_name} top-{k} logits for {len(rows)} records ({time.time() - t0:.0f} s)")
    return {"set": set_name, "n": len(rows), "k": k, "eval": {"seconds": round(time.time() - t0, 1), "mode": "topk"}}


def budget_scorer(eval_local, model, tok, bs_score, bs_gen, max_new, log, gb):
    """B's Scorer whose batches also respect a token budget (prompt tokens, plus max_new when generating), set
    from GPU memory: long prompts (MedEinst, NLI4CT-P) at a fixed batch size ran 24 GB cards out of memory.
    Batch composition changes speed only (B's left-padding self-check runs as before)."""
    budget = None if gb >= 60 else (12000 if gb < 30 else 40000)

    class BudgetScorer(eval_local.Scorer):
        def _batches(self, seqs, bs):
            if budget is None or self.pad_ok is False:
                return super()._batches(seqs, bs)
            extra = self.max_new if bs == self.bs_gen else 0
            order = sorted(range(len(seqs)), key=lambda i: (len(seqs[i]), i))
            out, cur = [], []
            for i in order:                       # ascending length: the new item is the longest in the batch
                if cur and (len(cur) == bs or (len(cur) + 1) * (len(seqs[i]) + extra) > budget):
                    out.append(cur)
                    cur = []
                cur.append(i)
            return out + ([cur] if cur else [])

    sc = BudgetScorer(model, tok, bs_score, bs_gen, max_new, log)
    log(f"token budget per batch: {budget}")
    return sc


def run_one(spec, a, mon, log, owner):
    import torch
    import eval_local, finetune
    from selrm import runq
    rid = spec["run_id"]
    rdir = f"{a.root}/results/{rid}"
    log.paths.append(f"{rdir}/run.log")
    mon.start_run(rdir)
    t0, model, sc = time.time(), None, None
    try:
        hp = finetune.HP | {"max_len": 4096} | spec.get("hp", {})
        base = f"{os.environ.get('SELRM_MODELS', a.broot + '/models')}/{spec.get('base_model', 'unsloth/Qwen3.5-9B').replace('/', '--')}"
        model, tok = finetune.load_for_eval(base, spec.get("adapter"), hp["max_len"], hp)
        log(f"loaded base {base}, adapter {spec.get('adapter')}")
        bs_score, bs_gen = spec.get("bs_score", 64), spec.get("bs_gen", 128)
        mem = torch.cuda.get_device_properties(0).total_memory / 2**30 if torch.cuda.is_available() else 99
        if mem < 30:                              # 24 GB cards: 18.8 GB of weights
            bs_score, bs_gen = min(bs_score, 16), min(bs_gen, 16)
        elif mem < 40:                            # 32 GB cards
            bs_score, bs_gen = min(bs_score, 64), min(bs_gen, 64)
        sc = budget_scorer(eval_local, model, tok, bs_score, bs_gen, spec.get("max_new", 384), log, mem)
        tag = spec.get("base_model", "unsloth/Qwen3.5-9B").replace("/", "--")
        summ, secs = {}, {}
        for s in spec["sets"]:
            root = a.broot if s.startswith("rule_v1") else a.root
            if spec.get("nocase"):                # default correction: u(s, no case); copies with case_text ""
                src = load_jsonl(__import__("selrm.formats", fromlist=["dataset_path"]).dataset_path(root, s))
                s, root = f"nocase/{s}", a.root
                path = f"{a.root}/data/{s}.jsonl"
                if not os.path.exists(path):
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    with open(f"{path}.{os.getpid()}.tmp", "w", encoding="utf-8") as f:
                        for r in src:
                            f.write(json.dumps(r | {"case_text": ""}) + "\n")
                    os.replace(f"{path}.{os.getpid()}.tmp", path)
            if spec.get("rejudge_from"):          # format-normalised readout of another run's reader outputs
                summ[s] = rejudge(sc, root, rid, s, f"{a.root}/results/{spec['rejudge_from']}", rdir, log)
                secs[s] = summ[s]["eval"]["seconds"]
                continue
            if spec.get("topk"):                  # sampling-noise check: next-token distribution, verdict format
                os.makedirs(rdir, exist_ok=True)
                summ[s] = topk_pass(sc, root, rid, s, rdir, log, tag, spec["topk"])
                secs[s] = summ[s]["eval"]["seconds"]
                continue
            orig = s
            if (spec.get("n_groups") or spec.get("claim_types")) and not spec.get("nocase"):
                # fixed subset (same rule as run_judge.py and the PRM runs); outputs keep the original set name
                cts = tuple(spec.get("claim_types", ["conclusion", "criterion", "applicability"]))
                s = f"sub/{spec.get('n_groups', 0)}_{'-'.join(cts)}/{orig}"
                path = f"{a.root}/data/{s}.jsonl"
                if not os.path.exists(path):
                    from selrm.formats import dataset_path
                    part = subset(load_jsonl(dataset_path(root, orig)), spec.get("n_groups", 0), cts)
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    with open(f"{path}.{os.getpid()}.tmp", "w", encoding="utf-8") as f:
                        for r in part:
                            f.write(json.dumps(r) + "\n")
                    os.replace(f"{path}.{os.getpid()}.tmp", path)
                root = a.root
            if root == a.root:                    # C's sets: pre-tokenise once, same code and tokenizer as B
                log(f"{rid} {s} prompts: {build_eval_c(a.root, spec['format'], tag, s, tok)}")
            summ[s] = eval_local.evaluate(sc, root, rid, spec["format"], s, rdir, log, tag, spec.get("mode"))
            secs[s] = summ[s].get("eval", {}).get("seconds")
            if s != orig and s.startswith("sub/"):
                for kind in ("scores", "summary"):
                    ext = "jsonl" if kind == "scores" else "json"
                    os.replace(f"{rdir}/{kind}_{s.replace('/', '~')}.{ext}", f"{rdir}/{kind}_{orig.replace('/', '~')}.{ext}")
                summ[orig] = summ.pop(s) | {"set": orig, "subset": {"n_groups": spec.get("n_groups") or "all",
                                                                    "claim_types": spec.get("claim_types")}}
                json.dump(summ[orig], open(f"{rdir}/summary_{orig.replace('/', '~')}.json", "w"), indent=1)
                secs[orig] = secs.pop(s)
        vers, gpu = __import__("train_eval_job").versions()
        meta = {"run_id": rid, "role": "C", "model": spec.get("base_model", "unsloth/Qwen3.5-9B"),
                "model_revision": open(f"{base}/REVISION").read().strip() if os.path.exists(f"{base}/REVISION") else None,
                "adapter": spec.get("adapter"), "adapter_run": spec.get("adapter_run"),
                "provider": "local (NRP Nautilus)", "access_date": time.strftime("%Y-%m-%d"),
                "reasoning": "chat template with enable_thinking=False", "format": spec["format"],
                "mode": spec.get("mode"), "rejudge_from": spec.get("rejudge_from"),
                "lenient_version": LENIENT_VERSION if spec.get("rejudge_from") else None, "sets": spec["sets"],
                "max_new": sc.max_new, "eval_batch": {"score": sc.bs_score, "generate": sc.bs_gen},
                "hp": {k: hp[k] for k in ("max_len",)}, "eval_seconds_by_set": secs,
                "eval_generated_tokens": sc.gen_tokens, "pad_check_ok": sc.pad_ok, "eval_u_path": sc.u_path,
                "eval_peak_mem_gb": round(torch.cuda.max_memory_reserved() / 2**30, 2) if torch.cuda.is_available() else None,
                "versions": vers, "gpu": gpu, "node": os.environ.get("NODE_NAME"), "pod": owner,
                "scoring_code": f"role-b {open(a.bcode + '/COMMIT').read().strip() if os.path.exists(a.bcode + '/COMMIT') else '?'}",
                "git_commit": open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/COMMIT").read().strip()
                if os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/COMMIT") else None,
                "wall_seconds": round(time.time() - t0, 1),
                "summaries": {s: (v or {}).get("all") for s, v in summ.items()}}
        meta |= mon.end_run()
        meta["gpu_hours"] = round(meta["wall_seconds"] / 3600, 3)
        json.dump(meta, open(f"{rdir}/meta.json", "w"), indent=1)
        runq.release(rdir, ok=True)
        log(f"DONE {rid} in {meta['wall_seconds'] / 60:.1f} min, GPU util mean {meta['gpu_util_mean']}")
    except Exception:
        tb = traceback.format_exc()
        log(f"FAILED {rid}\n{tb}")
        st = mon.end_run()
        runq.release(rdir, ok=False, reason=json.dumps(st) + "\n" + tb)
        if "CUDA" in tb or "out of memory" in tb:
            os._exit(2)
    finally:
        log.paths = log.paths[:1]
        sc = model = None
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--broot", required=True)
    ap.add_argument("--bcode", required=True)
    ap.add_argument("--tasks", required=True)
    ap.add_argument("--formats", default="", help="comma list: claim only runs of these formats (default all)")
    a = ap.parse_args()
    only = set(filter(None, a.formats.split(",")))
    sys.path[:0] = [a.bcode, f"{a.bcode}/scripts"]        # B's selrm package and scoring scripts
    gpu = os.environ.get("SELRM_BACKEND", "unsloth") == "unsloth"
    if gpu:
        import unsloth  # noqa: F401  (before transformers)
    import finetune
    from selrm import runq
    from train_eval_job import Log
    runq.ROLE = "C"
    if gpu:
        try:
            print("preflight:", finetune.preflight(), flush=True)
        except Exception as e:
            print(f"PREFLIGHT FAILED: {type(e).__name__}: {e}", flush=True)
            sys.exit(4)
    owner = os.environ.get("POD_NAME", socket.gethostname())
    log = Log(f"{a.root}/logs/{owner}/runner.log")
    mon = runq.GpuMonitor(f"{a.root}/logs/{owner}/gpu_util.csv", log=log)
    mon.start()
    import torch
    gb = torch.cuda.get_device_properties(0).total_memory / 2**30 if torch.cuda.is_available() else 0
    while True:
        runs = sorted(json.load(open(a.tasks))["runs"], key=lambda r: r.get("priority", 9))
        pick = next((r for r in runs if (not only or r["format"] in only) and (not gpu or gb >= r.get("min_gb", 0))
                     and r.get("min_gen", 0) <= GEN
                     and (not r.get("rejudge_from") or os.path.exists(f"{a.root}/results/{r['rejudge_from']}/DONE"))
                     and runq.state(f"{a.root}/results/{r['run_id']}") == "free"
                     and runq.claim(f"{a.root}/results/{r['run_id']}", owner)), None)
        if pick is None:
            log("nothing claimable; exiting")
            break
        log(f"claimed {pick['run_id']}")
        (run_prm if pick.get("prm") else run_one)(pick, a, mon, log, owner)


if __name__ == "__main__":
    main()
