"""Queue runner for one GPU (INTERFACES 7). Loop: claim the highest-priority
claimable run -> train -> evaluate on every eval set of the run -> write
meta/scores/summaries -> DONE -> delete adapter and checkpoints unless the run is
kept -> next run. Exits when no claimable run is left. Never waits for an input:
a run whose pre-tokenised data is missing is skipped. A monitor thread logs GPU
utilisation every 30 s into results/<run_id>/gpu_util.csv, heartbeats the claim,
and aborts the process if utilisation stays below 5% for 10 minutes.
  python scripts/train_eval_job.py --root ROOT --queue QUEUE.json [--queue ...]"""
import argparse, gc, json, os, shutil, socket, subprocess, sys, time, traceback
from importlib import metadata
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selrm import runq
from pretok import eval_path, tok_tag, train_dir, train_key

BASE = "unsloth/Qwen3.5-9B"
PKGS = ("torch", "transformers", "unsloth", "unsloth_zoo", "trl", "peft", "accelerate",
        "flash-linear-attention", "fla-core", "causal-conv1d", "triton", "numpy")


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def keep_adapter(spec):
    """Kept if the queue says so or configs/keep_adapters.json (snapshot shipped with the code) lists it."""
    keep = json.load(open(f"{REPO}/configs/keep_adapters.json"))["keep"]
    return bool(spec.get("keep_adapter")) or spec["run_id"] in keep


def paths(root, spec):
    """Base weights come from SELRM_MODELS (local NVMe copy made by k8s/stage.sh) if set."""
    rid, base = spec["run_id"], spec.get("base_model", BASE)
    keep = keep_adapter(spec)
    models = os.environ.get("SELRM_MODELS", f"{root}/models")
    return {"base": f"{models}/{base.replace('/', '--')}",
            "data": f"{train_dir(root, spec)}/train.npz",
            "ckpt": f"{root}/ckpt/{rid}",
            "adapter": f"{root}/adapters/{rid}" if keep else f"{root}/ckpt/{rid}/adapter",
            "results": f"{root}/results/{rid}"}


def ready(root, spec):
    P = paths(root, spec)
    return (os.path.exists(os.path.dirname(P["data"]) + "/READY") and os.path.isdir(P["base"])
            and all(os.path.exists(eval_path(root, spec, s)) for s in spec["eval_sets"]))


def load_runs(queues):
    runs = []
    for q in queues:
        for i, r in enumerate(json.load(open(q))["runs"]):
            runs.append((r.get("priority", 9), q, i, r))
    return [r for *_, r in sorted(runs, key=lambda x: x[:3])]


def versions():
    out = {}
    for p in PKGS:
        try:
            out[p] = metadata.version(p)
        except metadata.PackageNotFoundError:
            pass
    smi = subprocess.run(["nvidia-smi", "--query-gpu=name,driver_version,memory.total",
                          "--format=csv,noheader"], capture_output=True, text=True).stdout.strip()
    return out, smi


def max_rss_gb():
    try:
        import resource                      # Linux pods; absent on the Windows laptop self-test
        return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20, 2)
    except ImportError:
        return None


def commit(code_dir):
    try:
        return subprocess.run(["git", "-C", code_dir, "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        f = f"{code_dir}/COMMIT"
        return open(f).read().strip() if os.path.exists(f) else "unknown"


class Log:
    def __init__(self, path):
        self.paths = [path]
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def __call__(self, msg):
        line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
        print(line, flush=True)
        for p in self.paths:
            try:
                with open(p, "a") as f:
                    f.write(line + "\n")
            except OSError:          # a vanished results dir must not turn a log line into a crash
                pass


def run_one(root, spec, mon, log, owner):
    import torch
    import eval_local, finetune
    rid, P = spec["run_id"], paths(root, spec)
    os.makedirs(P["results"], exist_ok=True)
    log.paths.append(f"{P['results']}/run.log")
    mon.start_run(P["results"])
    t0, model, sc = time.time(), None, None
    try:
        model, tok, tinfo = finetune.train(spec, P, log)
        finetune.for_inference(model, tinfo["hp"])
        ev = spec.get("eval", {})
        sc = eval_local.Scorer(model, tok, ev.get("bs_score", 64), ev.get("bs_gen", 64),
                               ev.get("max_new", 384), log)
        te = time.time()
        summ = {s: eval_local.evaluate(sc, root, rid, spec["format"], s, P["results"], log, tok_tag(spec))
                for s in spec["eval_sets"]}
        vers, gpu = versions()
        meta = {"run_id": rid, "model": spec.get("base_model", BASE),
                "model_revision": open(f"{P['base']}/REVISION").read().strip()
                if os.path.exists(f"{P['base']}/REVISION") else None,
                "provider": "local (NRP Nautilus)", "access_date": time.strftime("%Y-%m-%d"),
                "reasoning": "chat template with enable_thinking=False",
                "format": spec["format"], "corpus": spec["corpus"], "seed": spec["seed"],
                "provisional": spec.get("provisional", False), "timing_only": spec.get("timing", False),
                "eval_sets": spec["eval_sets"], "train_key": train_key(spec),
                "pretok_stats": json.load(open(os.path.dirname(P["data"]) + "/stats.json")),
                "train": tinfo, "eval_seconds": round(time.time() - te, 1),
                "eval_generated_tokens": sc.gen_tokens, "pad_check_ok": sc.pad_ok,
                "per_device_batch": tinfo["hp"]["per_device"], "grad_accum": tinfo["grad_accum"],
                "versions": vers, "gpu": gpu, "node": os.environ.get("NODE_NAME"),
                "pod": owner, "git_commit": commit(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                "wall_seconds": round(time.time() - t0, 1), "keep_adapter": keep_adapter(spec),
                "max_rss_gb": max_rss_gb(),
                "eval_u_path": sc.u_path,
                "adapter_path": P["adapter"] if keep_adapter(spec) else None,
                "summaries": {s: v.get("all") for s, v in summ.items()}}
        meta |= mon.end_run()
        meta["gpu_hours"] = round(meta["wall_seconds"] / 3600, 3)
        json.dump(meta, open(f"{P['results']}/meta.json", "w"), indent=1)
        shutil.rmtree(P["ckpt"], ignore_errors=True)       # holds the adapter unless the run is kept
        runq.release(P["results"], ok=True)
        log(f"DONE {rid} in {meta['wall_seconds']/60:.1f} min, GPU util mean {meta['gpu_util_mean']}")
        return True
    except Exception:
        tb = traceback.format_exc()
        log(f"FAILED {rid}\n{tb}")
        st = mon.end_run()
        runq.release(P["results"], ok=False, reason=json.dumps(st) + "\n" + tb)
        if "CUDA" in tb or "out of memory" in tb:
            log("CUDA error: exiting so the pod restarts with a clean process")
            os._exit(2)
        return False
    finally:
        log.paths = log.paths[:1]
        sc = model = None                 # the Scorer holds the model too; drop both before collecting
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--queue", required=True, action="append")
    ap.add_argument("--max_runs", type=int, default=0, help="stop after this many runs (0 = no limit)")
    a = ap.parse_args()
    if os.environ.get("SELRM_BACKEND", "unsloth") == "unsloth":
        import unsloth  # noqa: F401  (must precede transformers so its patches and GDN kernels apply)
        import finetune
        try:                              # a broken env/node must fail the pod, not be charged to runs
            print("preflight:", finetune.preflight(), flush=True)
        except Exception as e:
            print(f"PREFLIGHT FAILED: {type(e).__name__}: {e}", flush=True)
            sys.exit(4)
    owner = os.environ.get("POD_NAME", socket.gethostname())
    log = Log(f"{a.root}/logs/{owner}/runner.log")
    mon = runq.GpuMonitor(f"{a.root}/logs/{owner}/gpu_util.csv", log=log)
    mon.start()
    done = 0
    while not a.max_runs or done < a.max_runs:
        if done:                          # the previous run's model must be gone before the next load
            import torch
            gc.collect()
            torch.cuda.empty_cache()
            held = torch.cuda.memory_allocated() / 2**30
            log(f"GPU memory still allocated after run {done}: {held:.2f} GiB")
            if held > 2:
                log("previous model not freed; exiting so the Job starts a clean pod (no run claimed)")
                sys.exit(5)
        pick = None
        for spec in load_runs(a.queue):
            rdir = f"{a.root}/results/{spec['run_id']}"
            if runq.state(rdir) == "free" and ready(a.root, spec) and runq.claim(rdir, owner):
                pick = spec
                break
        if pick is None:
            log("no claimable run left; exiting")
            break
        log(f"claimed {pick['run_id']}")
        run_one(a.root, pick, mon, log, owner)
        done += 1


if __name__ == "__main__":
    main()
