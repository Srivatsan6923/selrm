"""Role-C GPU runner. Scores base models and B's adapters with B's scoring code
(eval_local.Scorer / evaluate: frozen prompts, u = logit("+") - logit("-") at the answer
position, two-stage reader generated once per (case, condition), malformed ledger -> u = -20),
so C's rows and B's rows come from one code path (INTERFACES 3).
  python scripts/eval_c.py --root ROOT --broot BROOT --bcode BCODE --tasks TASKS.json
Task file: {"runs": [{"run_id", "format", "adapter": null | path, "sets": [...], "priority",
            "max_new": 384, "lenient": false, "hp": {...}}]}
Sets named rule_v1* are read from B's root (records and pre-tokenised prompts, read-only);
other sets (clin_v1/...) from C's root, pre-tokenised here on first use with B's
pretok.build_eval (same tokenizer, same chat template). Outputs per run:
ROOT/results/<run_id>/{meta.json, scores_<set>.jsonl, summary_<set>.json, run.log,
gpu_util.csv, DONE}; with lenient=true (ledger2 only) also scores_<set>~lenient.jsonl and
summary_<set>~lenient.json: the same reader outputs, normalised by lenient_ledger() before
the malformed check, judged again."""
import argparse, gc, json, os, re, socket, sys, time, traceback

KEYS = ("need", "found", "subject", "status", "time")


def lenient_ledger(text, case_text):
    """Canonical ledger text from a reader output with markdown noise, or None.
    Strips code fences, bullets, numbering and bold/italic markers; reads 'key: value'
    lines whose key is a ledger field (any case); a 'need' line opens an entry; other
    lines are ignored. Every entry needs the five fields in order; a quoted found is
    unquoted; found must be 'not mentioned' or a verbatim substring of the case, as in
    the strict check. ponytail: line-based; a value continued on a second line is cut."""
    entries, cur = [], None
    for raw in text.replace("\r", "").split("\n"):
        line = raw.strip().strip("`").strip()
        line = re.sub(r"^(?:[-*•+]|\d+[.)])\s+", "", line).replace("**", "").replace("__", "")
        line = re.sub(r"^[*_]+([A-Za-z]+)[*_]+\s*:", r"\1:", line)
        m = re.match(r"^([A-Za-z]+)\s*:\s*(.*)$", line)
        if not m or m.group(1).lower() not in KEYS:
            continue
        k, v = m.group(1).lower(), m.group(2).strip()
        if k == "need":
            cur = {}
            entries.append(cur)
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


def lenient_pass(sc, root, rid, set_name, out_dir, log):
    """Judge again on the leniently normalised reader outputs of the strict pass."""
    import eval_local
    from selrm.formats import MALFORMED_U, dataset_path, reader_unit
    from selrm.prompts import judge_prompt
    t0 = time.time()
    recs = load_jsonl(dataset_path(root, set_name))
    name = set_name.replace("/", "~")
    out = {r["iid"]: r["reader_output"] for r in load_jsonl(f"{out_dir}/scores_{name}.jsonl")}
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
    with open(f"{out_dir}/scores_{name}~lenient.jsonl", "w", encoding="utf-8") as f:
        for r, x in zip(recs, u):
            f.write(json.dumps({"iid": r["iid"], "u": x, "ledger_lenient": norm[reader_unit(r)]}) + "\n")
    summ = eval_local.summarize(recs, u, rid, set_name + "~lenient")
    bad = sum(v is None for v in norm.values())
    summ["eval"] = {"reader_units": len(norm), "malformed_units": bad, "malformed_rate": round(bad / max(1, len(norm)), 4),
                    "seconds": round(time.time() - t0, 1), "mode": "lenient"}
    json.dump(summ, open(f"{out_dir}/summary_{name}~lenient.json", "w"), indent=1)
    a = summ.get("all", {})
    log(f"{rid} {set_name} lenient: TA {a.get('TA', float('nan')):.1f} malformed {bad}/{len(norm)}")
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


def run_one(spec, a, mon, log, owner):
    import torch
    import eval_local, finetune, runq
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
        sc = eval_local.Scorer(model, tok, spec.get("bs_score", 64), spec.get("bs_gen", 128), spec.get("max_new", 384), log)
        tag = spec.get("base_model", "unsloth/Qwen3.5-9B").replace("/", "--")
        summ, secs = {}, {}
        for s in spec["sets"]:
            root = a.broot if s.startswith("rule_v1") else a.root
            if root == a.root:                    # C's sets: pre-tokenise once, same code and tokenizer as B
                log(f"{rid} {s} prompts: {build_eval_c(a.root, spec['format'], tag, s, tok)}")
            summ[s] = eval_local.evaluate(sc, root, rid, spec["format"], s, rdir, log, tag, spec.get("mode"))
            secs[s] = summ[s].get("eval", {}).get("seconds")
            if spec.get("lenient") and spec["format"] == "ledger2":
                summ[s + "~lenient"] = lenient_pass(sc, root, rid, s, rdir, log)
        vers, gpu = __import__("train_eval_job").versions()
        meta = {"run_id": rid, "role": "C", "model": spec.get("base_model", "unsloth/Qwen3.5-9B"),
                "model_revision": open(f"{base}/REVISION").read().strip() if os.path.exists(f"{base}/REVISION") else None,
                "adapter": spec.get("adapter"), "adapter_run": spec.get("adapter_run"),
                "provider": "local (NRP Nautilus)", "access_date": time.strftime("%Y-%m-%d"),
                "reasoning": "chat template with enable_thinking=False", "format": spec["format"],
                "mode": spec.get("mode"), "lenient": bool(spec.get("lenient")), "sets": spec["sets"],
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
    a = ap.parse_args()
    sys.path[:0] = [a.bcode, f"{a.bcode}/scripts"]        # B's selrm package and scoring scripts
    import unsloth  # noqa: F401  (before transformers)
    import finetune, runq
    from train_eval_job import Log
    runq.ROLE = "C"
    try:
        print("preflight:", finetune.preflight(), flush=True)
    except Exception as e:
        print(f"PREFLIGHT FAILED: {type(e).__name__}: {e}", flush=True)
        sys.exit(4)
    owner = os.environ.get("POD_NAME", socket.gethostname())
    log = Log(f"{a.root}/logs/{owner}/runner.log")
    mon = runq.GpuMonitor(f"{a.root}/logs/{owner}/gpu_util.csv", log=log)
    mon.start()
    while True:
        runs = sorted(json.load(open(a.tasks))["runs"], key=lambda r: r.get("priority", 9))
        pick = next((r for r in runs if runq.state(f"{a.root}/results/{r['run_id']}") == "free"
                     and runq.claim(f"{a.root}/results/{r['run_id']}", owner)), None)
        if pick is None:
            log("nothing claimable; exiting")
            break
        log(f"claimed {pick['run_id']}")
        run_one(pick, a, mon, log, owner)


if __name__ == "__main__":
    main()
