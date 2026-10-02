def finished_rule_runs():
    """[(run_id, meta, {set: eval seconds})] for every finished rule_v1 training run in results_git."""
    out = []
    for d in sorted(os.listdir(RG)):
        m = load(d, "meta.json")
        if not (m and os.path.exists(f"{RG}/{d}/DONE") and str(m.get("corpus", "")).startswith("rule_v1")
                and m.get("train", {}).get("train_seconds")):
            continue
        per = {}
        for s in m["eval_sets"]:
            summ = load(d, f"summary_{s.replace('/', '~')}.json")
            per[s.split("/", 1)[1]] = (summ or {}).get("eval", {}).get("seconds")
        out.append((d, m, per))
    return out


def timesplit():
    """GPU-hours on training and on evaluation per finished rule_v1 run (meta.json), and evaluation seconds per
    set (summary_<set>.json eval.seconds). A resumed run reports its last attempt."""
    runs = finished_rule_runs()
    sets = sorted({s for _, _, per in runs for s in per})
    print("| run | GPU | train GPU-h | eval GPU-h | other GPU-h | total GPU-h | " + " | ".join(f"eval s {s}" for s in sets) + " |")
    print("|---|---|---|---|---|---|" + "---|" * len(sets))
    for rid, m, per in runs:
        tr, ev, wall = m["train"]["train_seconds"], m["eval_seconds"], m["wall_seconds"]
        print(f"| {rid} | {m['gpu'].split(',')[0]} | {tr / 3600:.2f} | {ev / 3600:.2f} | {(wall - tr - ev) / 3600:.2f} | "
              f"{wall / 3600:.2f} | " + " | ".join(f"{per[s]:.0f}" if per.get(s) is not None else "-" for s in sets) + " |")


# Projection model. Evaluation kind of each format: runs of one kind cost the same per evaluated record.
EVAL_KIND = {"verdict": "verdict", "verdict_bt": "verdict", "rationale": "rationale", "genprm": "genprm",
             "summary2": "summary2", "value2": "value2", "ledger2": "ledger2", "ledger2_dec": "ledger2",
             "dec_judge": "ledger2", "bit_reader": "ledger2", "ledger2_verify": "ledger2"}
SXM = "NVIDIA A100-SXM4-80GB"     # reference card: every rate is measured on it, capacity is converted to it


def kubectl_sh(cmd):
    import subprocess
    return subprocess.run(["kubectl", "-n", "ecepxie", "exec", "selrm-b-sync", "--", "sh", "-c", cmd],
                          capture_output=True, text=True).stdout


def pvc_runs():
    """{run_id: {owner, gpu, tok_s, sets {set: s}, done, claimed (unix), heartbeat (unix)}} for every run directory on
    the PVC (running or finished), plus the cluster time. GPU of a running run: its pod's node label."""
    import subprocess
    out = kubectl_sh(
        "cd /pvc/selrm/results && for d in */; do r=${d%/}; case $r in aborted-*) continue;; esac; "
        "echo \"RUN $r $(cut -d' ' -f1 $d/CLAIMED_B 2>/dev/null) $(stat -c %Y $d/CLAIMED_B 2>/dev/null || echo 0) "
        "$(stat -c %Y $d/HEARTBEAT 2>/dev/null || echo 0) $(test -f $d/DONE && echo 1 || echo 0)\"; "
        "grep -o '\"gpu\": \"[^,\"]*' $d/meta.json 2>/dev/null | head -1 | sed 's/^/GPU /'; "
        "grep -ho 'trained [0-9]* steps in [0-9.]* min, [0-9.]* tok/s' $d/run.log 2>/dev/null | tail -1 | sed 's/^/TRN /'; "
        "for s in $d/summary_*.json; do [ -f $s ] && echo \"SUM $(basename $s) "
        "$(tr -d '\\n ' < $s | grep -o '\"seconds\":[0-9.]*' | tail -1 | cut -d: -f2)\"; done; done; echo NOW $(date +%s)")
    runs, cur, now = {}, None, 0
    for line in out.splitlines():
        p = line.split()
        if not p:
            continue
        if p[0] == "RUN":
            owner = p[2] if len(p) == 6 else None
            claimed, hb, done = (int(x) for x in p[-3:])
            cur = runs[p[1]] = {"owner": owner, "gpu": None, "tok_s": None, "sets": {}, "done": done == 1,
                                "claimed": claimed, "heartbeat": hb}
        elif p[0] == "GPU" and cur is not None:
            cur["gpu"] = line.split('"gpu": "', 1)[1]
        elif p[0] == "TRN" and cur is not None:
            cur["tok_s"] = float(p[-2])
        elif p[0] == "SUM" and cur is not None and len(p) == 3 and p[2]:
            name = p[1][len("summary_"):-len(".json")].replace("~", "/")
            if not name.endswith(("/swap", "/edit")) and "~swap" not in p[1] and "~edit" not in p[1]:
                cur["sets"][name] = float(p[2])
        elif p[0] == "NOW":
            now = int(p[1])
    pods = json.loads(subprocess.run(["kubectl", "-n", "ecepxie", "get", "pods", "-l", "app=selrm-b", "-o", "json"],
                                     capture_output=True, text=True).stdout or '{"items": []}')["items"]
    node_of = {p["metadata"]["name"]: p["spec"].get("nodeName") for p in pods}
    model = {}
    for r in runs.values():
        if r["gpu"] is None and node_of.get(r["owner"]):
            n = node_of[r["owner"]]
            if n not in model:
                model[n] = subprocess.run(["kubectl", "get", "node", n, "-o",
                                           "jsonpath={.metadata.labels.nvidia\\.com/gpu\\.product}"],
                                          capture_output=True, text=True).stdout.replace("-", " ", 1).strip()
            r["gpu"] = model[n].replace("NVIDIA ", "NVIDIA ").replace("A100 ", "A100-") if model[n] else None
    return runs, now


def tokens_by_key():
    """{(tokenizer tag, train key): (tokens, completion tokens)} from the pre-tokenised sets on the PVC."""
    out = kubectl_sh("cd /pvc/selrm/tok && for f in */train/*/stats.json; do echo \"$f $(tr -d '\\n ' < $f | "
                     "grep -o '\"tokens\":[0-9]*\\|\"completion_tokens\":[0-9]*' | tr '\\n' ' ')\"; done")
    tok = {}
    for line in out.splitlines():
        p = line.split()
        if len(p) >= 3:
            vals = dict(x.strip('"').split('":') for x in p[1:] if '":' in x)
            parts = p[0].split("/")
            tok[(parts[0], parts[2])] = (int(vals.get("tokens", 0)), int(vals.get("completion_tokens", 0)))
    return tok


def gpus_by_model(hours=6):
    """{GPU model: mean count held by B's runner pods over the last hours (steps without any count as 0)}."""
    import urllib.parse, urllib.request
    q = lambda e: json.load(urllib.request.urlopen("https://thanos.nrp-nautilus.io/api/v1/query?" + urllib.parse.urlencode(
        {"query": e}), timeout=60))["data"]["result"]
    sel = 'DCGM_FI_DEV_GPU_UTIL{namespace="ecepxie",pod=~"selrm-b-run.*"}'
    models = [r["metric"].get("modelName") for r in q(f"count by (modelName) (count_over_time({sel}[{hours}h]))")]
    out = {}
    for m in models:
        e = f'(count({sel[:-1]},modelName="{m}"}}) or vector(0))'
        res = q(f"avg_over_time({e}[{hours}h:5m])")
        out[m] = float(res[0]["value"][1]) if res else 0.0
    return out


def projection(freeze="2026-10-07T23:59:00Z"):
    """GPU-hours of the revised queue (queued + running + rows not yet queued), in A100-SXM4-80GB hours, against what
    B's runners deliver until the run freeze at the GPUs held over the last 6 hours (per GPU model, converted with
    measured speeds)."""
    import csv, datetime, glob, re
    import make_queue_b as Q
    reg = json.load(open(f"{ROOT}/scratch/registry_rule_v1.json"))
    nrec = {n: v["n_records"] for n, v in reg.items()}
    runs, now_ts = pvc_runs()
    tok = tokens_by_key()
    queued = {}
    for f in sorted(glob.glob(f"{ROOT}/configs/queues/**/*.json", recursive=True)):
        if not re.search(r"b_(smoke|t0b|val\d*)\.json$", f):
            for r in json.load(open(f))["runs"]:
                queued.setdefault(r["run_id"], r)
    fmt_of = {rid: r["format"] for rid, r in queued.items()}
    for d in os.listdir(RG):
        m = load(d, "meta.json")
        if m:
            fmt_of.setdefault(d, m.get("format"))
    mean = lambda v: sum(v) / len(v) if v else None
    # rates on the reference card
    tps, spr, speed_obs = {}, {}, {}
    for rid, r in runs.items():
        f = fmt_of.get(rid)
        if not f or rid.startswith("B-C0") or "~" in rid:
            continue
        k = EVAL_KIND.get(f, "ledger2")
        if rid.startswith(("C-TF", "B-AE")) or queued.get(rid, {}).get("train") is False:
            k = "verdict" if rid.startswith(("C-TF", "B-AE-oracle", "B-AE-field")) else k
        if r["tok_s"] and r["gpu"]:
            (tps.setdefault(f, []) if r["gpu"] == SXM else speed_obs.setdefault((r["gpu"], f), [])).append(r["tok_s"])
        if r["gpu"] == SXM:
            for s, sec in r["sets"].items():
                if s in nrec and nrec[s]:
                    spr.setdefault(k, []).append(sec / nrec[s])
    tps = {f: mean(v) for f, v in tps.items()}
    tps_all = mean(list(tps.values()))
    spr = {k: mean(v) for k, v in spr.items()}
    speed = {g: mean([v / tps[f] for v in vs]) for (g, f), vs in speed_obs.items() if f in tps}
    speed = {g: mean([s for (gg, _), s in [((g2, f2), mean([v / tps[f2] for v in vs])) for (g2, f2), vs in speed_obs.items() if f2 in tps] if gg == g])
             for g in {g for g, _ in speed_obs}}
    t0 = {f: load(f"B-T0-{f}", "meta.json")["eval_seconds"] for f in FMTS}
    rel = {"summary2": t0["summary2"] / t0["ledger2"], "value2": t0["value2"] / t0["ledger2"],
           "rationale": t0["rationale"] / t0["ledger2"]}
    key = lambda f, c: (f, c)
    comp = {k: v[1] for (tag, k), v in tok.items() if tag == "unsloth--Qwen3.5-9B"}
    g_comp = [v for k, v in comp.items() if k.startswith("genprm__rule_v1~train_triplets__")]
    r_comp = [v for k, v in comp.items() if k.startswith("rationale__rule_v1~train_triplets__")]
    gen_ratio = g_comp[0] / r_comp[0] if g_comp and r_comp else None

    def kind_spr(k):
        if k in spr:
            return spr[k], "measured"
        if k == "genprm":
            base, how = kind_spr("rationale")
            return base * gen_ratio, f"rationale x {gen_ratio:.2f} ({how})"
        return spr["ledger2"] * rel[k], f"ledger2 x B-T0 {rel[k]:.2f}"

    notes = {}

    def eval_seconds(r):
        f = r["format"]
        k = EVAL_KIND.get(f, "ledger2")
        if r["run_id"].startswith(("C-TF", "B-AE-oracle", "B-AE-field")) or r.get("kind") == "concept":
            k = "verdict"
        v, how = kind_spr(k)
        notes[k] = how
        return sum(v * nrec.get(s, nrec["rule_v1/dev"]) for s in r["eval_sets"])

    def train_seconds(r):
        if r.get("train") is False or r.get("kind") == "concept":
            return 0.0
        tag = r.get("base_model", "unsloth/Qwen3.5-9B").replace("/", "--")
        pre = f"{r['format']}__{r['corpus'].replace('/', '~')}__n{r.get('n_examples') or 'all'}"
        hits = [v[0] for (t, k), v in tok.items() if t == tag and k.startswith(pre)]
        if not hits:
            hits = [v[0] for (t, k), v in tok.items() if t == "unsloth--Qwen3.5-9B" and k.startswith(
                f"{r['format']}__rule_v1~train_triplets__n60000")] or [13.1e6]
        return hits[0] / (tps.get(r["format"]) or tps_all)

    other = mean([m["wall_seconds"] - m["train"]["train_seconds"] - m["eval_seconds"]
                  for _, m, _ in finished_rule_runs() if m["gpu"].startswith(SXM)]) or 0.0
    rows = []
    for rid, r in queued.items():
        st = runs.get(rid)
        if st and st["done"]:
            continue
        est = (train_seconds(r) + eval_seconds(r) + other) / 3600
        state = "queued"
        if st and st["owner"] and now_ts - st["heartbeat"] < 900:
            state, est = "running", max(0.0, est - (now_ts - st["claimed"]) / 3600 * speed.get(st["gpu"], 1.0))
        rows.append((r["priority"], rid, state, est))
    extra = {}
    for gen in (lambda: Q.factorial({1, 2, 3, 4}, f"{ROOT}/scratch/registry_rule_v1.json", "rule_v1"),
                lambda: Q.transfer({0, 1, 2, 3, 4}, None, "rule_v1"),
                lambda: Q.backbones({0, 1, 2}, None, "rule_v1"),
                lambda: Q.extras({0, 1, 2}, f"{ROOT}/scratch/registry_rule_v1.json", "rule_v1")):
        for s in gen():
            extra.setdefault(s["run_id"], s)
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        rid = r["run_id"]
        if rid in queued or r["status"] in ("done", "dropped") or r["runtime"] != "GPU" or (runs.get(rid) or {}).get("done"):
            continue
        seed = int(r["seed"]) if r["seed"].isdigit() else 0
        spec = extra.get(rid) or {"run_id": rid, "format": "ledger2", "corpus": "rule_v1/train_triplets",
                                  "n_examples": 60000, "train": r["kind"] != "eval",
                                  "eval_sets": [f"rule_v1/{s}" for s in (Q.TRANSFER if rid.startswith("B-TR") else Q.REDUCED)]}
        blocked = rid not in extra
        est = (train_seconds(spec) + eval_seconds(spec) + other) / 3600
        rows.append((Q.priority(rid, seed, r["priority"]), rid, "blocked" if blocked else "not queued", est))
    now = datetime.datetime.now(datetime.timezone.utc)
    left = (datetime.datetime.fromisoformat(freeze.replace("Z", "+00:00")) - now).total_seconds() / 3600
    held = gpus_by_model()
    cap_raw = sum(held.values()) * left
    cap = sum(c * speed.get(g, 1.0) for g, c in held.items()) * left
    print(f"Generated {now:%Y-%m-%d %H:%M} UTC by scripts/report_b.py projection. Hours are A100-SXM4-80GB hours: "
          "training = pre-tokenised tokens / tokens per second of the format, evaluation = seconds per evaluated record "
          "of the run's evaluation kind x records of each set, both measured on A100-SXM4-80GB runs of rule_v1 (finished "
          "or running; PVC run logs and summaries). Training tokens/s: " + ", ".join(f"{f} {v:.0f}" for f, v in sorted(tps.items())) +
          "; evaluation kinds: " + ", ".join(f"{k} {h}" for k, h in sorted(notes.items())) + "." + NL)
    print("Measured speed of other cards (training tokens/s relative to A100-SXM4-80GB, same format): " +
          (", ".join(f"{g} {s:.2f}" for g, s in sorted(speed.items())) or "none yet") + "; unmeasured cards count as 1.00." + NL)
    print(f"Capacity until {freeze} (UTC; the plan gives no time zone): {left:.1f} h x GPUs held by B's runners over the "
          "last 6 h (mean, steps without a GPU count as 0): " + ", ".join(f"{g} {c:.2f}" for g, c in sorted(held.items())) +
          f" = {cap_raw:.0f} GPU-h, {cap:.0f} A100-SXM4-80GB hours." + NL)
    print("| priority | group | runs | A100-80GB h | cumulative | fits |")
    print("|---|---|---|---|---|---|")
    groups = {}
    for p, rid, state, est in sorted(rows):
        g = re.sub(r"-s\d+$", "", rid)
        g = "B-F" if rid.startswith("B-F-") else "-".join(g.split("-")[:2])
        groups.setdefault((p, g, state), []).append(est)
    cum = 0.0
    for (p, g, state), v in sorted(groups.items()):
        cum += sum(v)
        print(f"| {p} | {g} ({state}) | {len(v)} | {sum(v):.1f} | {cum:.1f} | {'yes' if cum <= cap else 'no'} |")
    print(NL + f"Total {cum:.1f} A100-80GB hours for {len(rows)} runs (blocked rows wait for other roles' data); "
          f"capacity {cap:.0f} A100-80GB hours. Cut order if it does not fit (plan): B-DIV seeds 1-2, then B-DIV seed 0.")


