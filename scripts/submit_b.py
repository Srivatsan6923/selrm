"""Role-B launcher for NRP Nautilus (namespace ecepxie, PVC selrm-b). Builds the
Kubernetes objects as JSON and applies them with kubectl. Laptop side only.
  python scripts/submit_b.py sync-up | sync-down          # short interactive CPU pod for copies
  python scripts/submit_b.py push-code                    # code snapshot -> /pvc/selrm/code/<sha>
  python scripts/submit_b.py push-queue QUEUE.json        # -> /pvc/selrm/queues/<name>
  python scripts/submit_b.py build-env TAG                # CPU Job: env tarball
  python scripts/submit_b.py prep QUEUE_NAME              # CPU Job: data, weights, pretok
  python scripts/submit_b.py runners QUEUE_NAME --n 3 --gpu a100 --max-runs 3 --hours 4
  python scripts/submit_b.py pull RUN_ID [RUN_ID ...]     # results -> results_git/<run_id>/
  python scripts/submit_b.py push-ref origin/role-a       # A's code (+ data/REGISTRY.json) -> /pvc/selrm/code/<sha>
  python scripts/submit_b.py build-data <A_sha12> [--fold N]   # CPU: rebuild A's sets, verify sha256, publish
  python scripts/submit_b.py restore-data <A_sha12> xr_v1/test scripts/build_xr_v1.py   # CPU: sets with own builder
Policy built in (docs/NRP_B.md): one GPU per Job, requests == limits, no sleep in Jobs,
CPU Jobs kept off GPU nodes, runner exits when its queue has no claimable run."""
import argparse, io, json, os, subprocess, sys, tarfile, time

NS, PVC = "ecepxie", "selrm-b"
IMAGE = "nvcr.io/nvidia/cuda:13.0.3-cudnn-devel-ubuntu24.04"
SMALL_IMAGE = "nvcr.io/nvidia/cuda:13.0.3-base-ubuntu24.04"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIRS = ("selrm", "scripts", "k8s", "configs", "tests")
GPU = {   # kind -> (resource, gpu.product values or None, priorityClassName or None)
    "a100": ("nvidia.com/a100", ["NVIDIA-A100-SXM4-80GB", "NVIDIA-A100-80GB-PCIe", "NVIDIA-A100-PCIE-40GB"], None),
    "a100-80": ("nvidia.com/a100", ["NVIDIA-A100-SXM4-80GB", "NVIDIA-A100-80GB-PCIe"], None),
    "l40": ("nvidia.com/gpu", ["NVIDIA-L40", "NVIDIA-L40S"], None),
    "a6000": ("nvidia.com/rtxa6000", None, None),
    "a40": ("nvidia.com/a40", None, None),
    "h100-opp": ("nvidia.com/h100", None, "opportunistic"),
    "h200-opp": ("nvidia.com/h200", None, "opportunistic"),
    "rtx8000": ("nvidia.com/rtx8000", None, None),      # 48 GB
}
CPU_ONLY = {"key": "feature.node.kubernetes.io/pci-10de.present", "operator": "NotIn", "values": ["true"]}
DRIVER = {"key": "nvidia.com/cuda.driver.major", "operator": "Gt", "values": ["579"]}   # cu130 needs >= 580


def kubectl(*args, inp=None, check=True):
    r = subprocess.run(["kubectl", "-n", NS, *args], input=inp, capture_output=True)
    if check and r.returncode:
        sys.exit(f"kubectl {' '.join(args)} failed: {r.stderr.decode(errors='replace')}")
    return r.stdout.decode(errors="replace")


def apply(obj):
    print(kubectl("apply", "-f", "-", inp=json.dumps(obj).encode()).strip())


def affinity(terms):
    return {"nodeAffinity": {"requiredDuringSchedulingIgnoredDuringExecution": {
        "nodeSelectorTerms": [{"matchExpressions": terms}]}}}


def res(cpu, mem, eph, extra=None):
    r = {"cpu": str(cpu), "memory": mem, "ephemeral-storage": eph} | (extra or {})
    return {"requests": r, "limits": dict(r)}


VOL_PVC = {"name": "pvc", "persistentVolumeClaim": {"claimName": PVC}}
MNT_PVC = {"name": "pvc", "mountPath": "/pvc"}


def sha():
    return subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True,
                          text=True, check=True).stdout.strip()


def cpu_job(name, command, cpu=8, mem="32Gi", eph="60Gi", hours=2):
    return {"apiVersion": "batch/v1", "kind": "Job",
            "metadata": {"name": name, "namespace": NS, "labels": {"app": "selrm-b", "role": "cpu"}},
            "spec": {"backoffLimit": 1, "ttlSecondsAfterFinished": 259200,
                     "activeDeadlineSeconds": int(hours * 3600),
                     "template": {"metadata": {"labels": {"app": "selrm-b", "role": "cpu"}},
                                  "spec": {"restartPolicy": "Never",
                                           "affinity": affinity([CPU_ONLY, {"key": "topology.kubernetes.io/region",
                                                                            "operator": "In", "values": ["us-west"]}]),
                                           "containers": [{"name": "main", "image": IMAGE, "command": command,
                                                           "resources": res(cpu, mem, eph),
                                                           "env": [{"name": "HF_HUB_DISABLE_PROGRESS_BARS", "value": "1"}],
                                                           "volumeMounts": [MNT_PVC]}],
                                           "volumes": [VOL_PVC]}}}}


def runner_job(name, queue, code, env_tag, gpu, max_runs, hours, cpu=2, mem="12Gi", models=("unsloth--Qwen3.5-9B",)):
    resource, products, prio = GPU[gpu]
    terms = [DRIVER] + ([{"key": "nvidia.com/gpu.product", "operator": "In", "values": products}] if products else [])
    pod = {"restartPolicy": "Never", "affinity": affinity(terms),
           "initContainers": [{"name": "stage", "image": IMAGE,
                               # the GPU is already reserved while this runs: a staging step slower than 12 min fails the pod and frees it
                               "command": ["timeout", "720", "sh", f"/pvc/selrm/code/{code}/k8s/stage.sh", env_tag, code, *models],
                               "resources": res(3, "8Gi", "64Gi"),
                               "volumeMounts": [MNT_PVC, {"name": "work", "mountPath": "/work"},
                                                {"name": "env", "mountPath": "/opt/selrm-env"}]}],
           "containers": [{"name": "runner", "image": IMAGE, "workingDir": "/work",
                           "command": ["/opt/selrm-env/venv/bin/python", "-u", "/work/code/scripts/train_eval_job.py",
                                       "--root", "/pvc/selrm",
                                       *[x for q in queue.split(",") for x in ("--queue", "/pvc/selrm/queues" + ("" if q == "all" else f"/{q}"))],
                                       "--max_runs", str(max_runs)],
                           "env": [{"name": k, "value": v} for k, v in {
                               "SELRM_MODELS": "/work/models", "HF_HOME": "/work/hf", "HF_HUB_OFFLINE": "1",
                               "TRANSFORMERS_OFFLINE": "1", "TRITON_CACHE_DIR": "/work/triton",
                               "PYTHONPYCACHEPREFIX": "/work/pycache", "OMP_NUM_THREADS": "3",
                               "MKL_NUM_THREADS": "3", "TOKENIZERS_PARALLELISM": "false",
                               "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True"}.items()]
                           + [{"name": "POD_NAME", "valueFrom": {"fieldRef": {"fieldPath": "metadata.name"}}},
                              {"name": "NODE_NAME", "valueFrom": {"fieldRef": {"fieldPath": "spec.nodeName"}}}],
                           "resources": res(cpu, mem, "64Gi", {resource: "1"}),   # RSS median must stay >= 20% of mem
                           "volumeMounts": [MNT_PVC, {"name": "work", "mountPath": "/work"},
                                            {"name": "env", "mountPath": "/opt/selrm-env"},
                                            {"name": "dshm", "mountPath": "/dev/shm"}]}],
           "volumes": [VOL_PVC, {"name": "work", "emptyDir": {}}, {"name": "env", "emptyDir": {}},
                       {"name": "dshm", "emptyDir": {"medium": "Memory", "sizeLimit": "4Gi"}}]}
    if prio:
        pod["priorityClassName"] = prio
    labels = {"app": "selrm-b", "role": "runner", "gpu": gpu}
    return {"apiVersion": "batch/v1", "kind": "Job", "metadata": {"name": name, "namespace": NS, "labels": labels},
            "spec": {"backoffLimit": 2, "ttlSecondsAfterFinished": 259200, "activeDeadlineSeconds": int(hours * 3600),
                     "template": {"metadata": {"labels": labels}, "spec": pod}}}


def sync_pod():
    """Interactive helper pod (no controller; sleep allowed there; <=1 CPU and 2 GiB, so
    exempt from CPU/RAM usage checks). Deleted after each copy session."""
    return {"apiVersion": "v1", "kind": "Pod",
            "metadata": {"name": "selrm-b-sync", "namespace": NS, "labels": {"app": "selrm-b", "role": "sync"}},
            "spec": {"restartPolicy": "Never", "activeDeadlineSeconds": 21600,     # NRP cap for bare pods
                     "affinity": affinity([CPU_ONLY, {"key": "topology.kubernetes.io/region", "operator": "In",
                                                      "values": ["us-west"]}]),
                     "containers": [{"name": "sync", "image": SMALL_IMAGE, "command": ["sh", "-c", "sleep 21000"],
                                     "resources": res(1, "1Gi", "2Gi"), "volumeMounts": [MNT_PVC]}],
                     "volumes": [VOL_PVC]}}


def wait_running(pod, timeout=600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        ph = kubectl("get", "pod", pod, "-o", "jsonpath={.status.phase}", check=False)
        if ph == "Running":
            return
        time.sleep(5)
    sys.exit(f"{pod} not running after {timeout} s")


def snapshot(code=None):
    """The code snapshot a Job runs: --code, else HEAD, pushed first when it is not on the PVC
    (a Job started on a missing snapshot fails at once)."""
    code = code or sha()
    if subprocess.run(["kubectl", "-n", NS, "exec", "selrm-b-sync", "--", "test", "-d", f"/pvc/selrm/code/{code}"],
                      capture_output=True).returncode:
        if code != sha():
            sys.exit(f"code snapshot {code} is not on the PVC")
        push_code()
    return code


def exec_sync(*cmd, inp=None):
    return kubectl("exec", *(["-i"] if inp is not None else []), "selrm-b-sync", "--", *cmd, inp=inp)


def push_ref(ref):
    """Snapshot of any git ref (e.g. role A's frozen commit) -> /pvc/selrm/code/<sha12>, via git archive."""
    full = subprocess.run(["git", "-C", REPO, "rev-parse", ref], capture_output=True, text=True, check=True).stdout.strip()
    data = subprocess.run(["git", "-C", REPO, "archive", "--format=tar", full], capture_output=True, check=True).stdout
    code, dest = full[:12], f"/pvc/selrm/code/{full[:12]}"
    exec_sync("sh", "-c", f"mkdir -p {dest}.tmp && tar -xf - -C {dest}.tmp && echo {full} > {dest}.tmp/COMMIT && "
                          f"rm -rf {dest} && mv {dest}.tmp {dest}", inp=data)
    print(f"{ref} = {full} -> {dest} ({len(data)} bytes)")
    return code


def push_code():
    code = sha()
    dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--", *CODE_DIRS],
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        sys.exit(f"commit first; uncommitted changes:\n{dirty}")
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tar:
        for d in CODE_DIRS:
            tar.add(os.path.join(REPO, d), arcname=d,
                    filter=lambda ti: None if "__pycache__" in ti.name or ti.name.endswith(".pyc") else ti)
        data = (code + "\n").encode()
        ti = tarfile.TarInfo("COMMIT"); ti.size = len(data)
        tar.addfile(ti, io.BytesIO(data))
    dest = f"/pvc/selrm/code/{code}"
    exec_sync("sh", "-c", f"mkdir -p {dest}.tmp && tar -xf - -C {dest}.tmp && rm -rf {dest} && mv {dest}.tmp {dest}",
              inp=buf.getvalue())
    print(f"code {code} -> {dest} ({len(buf.getvalue())} bytes)")
    return code


def pull(run_ids):
    """Copy finished runs (DONE) to results_git/<run_id>/: meta, summaries, scores
    (gzip-compressed in transit), DONE, gpu_util.csv. Returns the run_ids copied."""
    have = exec_sync("sh", "-c", "cd /pvc/selrm/results 2>/dev/null && ls -d */DONE 2>/dev/null | cut -d/ -f1").split()
    want = [r for r in (run_ids or have) if r in have]
    got = []
    for rid in want:
        local = f"{REPO}/results_git/{rid}/DONE"
        if os.path.exists(local) and open(local).read() == exec_sync("cat", f"/pvc/selrm/results/{rid}/DONE"):
            continue                       # same DONE stamp: nothing new (a re-run writes a new stamp)
        data = subprocess.run(["kubectl", "-n", NS, "exec", "selrm-b-sync", "--", "sh", "-c",
                               f"cd /pvc/selrm/results && tar -czf - {rid}/meta.json {rid}/DONE "
                               f"$(ls {rid}/summary_*.json {rid}/scores_*.jsonl {rid}/gpu_util.csv {rid}/run.log 2>/dev/null)"],
                              capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            tar.extractall(f"{REPO}/results_git", filter="data")
        got.append(rid)
        print(f"pulled {rid} ({len(data)} bytes gz)")
    missing = sorted(set(run_ids or []) - set(have))
    if missing:
        print("not DONE on the PVC yet:", " ".join(missing))
    return got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--gpu", default="a100", choices=sorted(GPU))
    ap.add_argument("--max-runs", type=int, default=3)
    ap.add_argument("--hours", type=float, default=4)
    ap.add_argument("--env", default="v1")
    ap.add_argument("--cpu", type=int, default=2)        # measured 1.0 core median on A100 training
    ap.add_argument("--mem", default="12Gi")             # measured RSS 2.9 GiB; RSS median must be >= 20% of this
    ap.add_argument("--code", default=None)
    ap.add_argument("--models", default="unsloth--Qwen3.5-9B", help="runners: base weights to stage (comma list)")
    ap.add_argument("--secret", default=None, help="NAME:KEY of the HF token secret (publish)")
    a = ap.parse_args()
    if a.cmd == "sync-up":
        apply(sync_pod()); wait_running("selrm-b-sync"); print("selrm-b-sync running")
    elif a.cmd == "sync-down":
        print(kubectl("delete", "pod", "selrm-b-sync", "--wait=false", check=False))
    elif a.cmd == "push-code":
        push_code()
    elif a.cmd == "push-queue":
        src = a.args[0]                   # path under configs/queues/ is kept (v2/...: queues for newer runners)
        name = os.path.relpath(os.path.abspath(src), f"{REPO}/configs/queues").replace(os.sep, "/")
        name = os.path.basename(src) if name.startswith("..") else name
        exec_sync("sh", "-c", f"mkdir -p $(dirname /pvc/selrm/queues/{name}) && cat > /pvc/selrm/queues/{name}.tmp && "
                              f"mv /pvc/selrm/queues/{name}.tmp /pvc/selrm/queues/{name}", inp=open(src, "rb").read())
        print(f"queue {name} pushed")
        marked = []                       # claim channel for the pooled rows (docs/CHANGE_REQUESTS.md, 2 Oct)
        import csv
        pooled = {r["run_id"] for r in csv.DictReader(open(f"{REPO}/docs/RUN_MATRIX_B.csv", encoding="utf-8"))
                  if r["pool"] == "yes"}
        for r in json.load(open(src))["runs"]:
            d = f"{REPO}/results_git/{r['run_id']}"
            if r["run_id"] in pooled and not os.path.exists(f"{d}/DONE") and not os.path.exists(f"{d}/CLAIMED_B"):
                os.makedirs(d, exist_ok=True)
                open(f"{d}/CLAIMED_B", "w", newline="\n").write(f"queued on NRP in {name} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
                marked.append(r["run_id"])
        if marked:
            print(f"marked {len(marked)} runs CLAIMED_B in results_git (commit and push to publish the claims)")
    elif a.cmd == "build-env":
        code = snapshot(a.code)
        apply(cpu_job(f"selrm-b-build-env-{a.args[0]}", ["bash", f"/pvc/selrm/code/{code}/k8s/build_env.sh", a.args[0]],
                      cpu=6, mem="12Gi", eph="80Gi", hours=2))   # compile uses ~3-6 cores; usage must stay >=20% of request
    elif a.cmd == "prep":
        code = snapshot(a.code)
        q = a.args[0]
        apply(cpu_job(f"selrm-b-prep-{q.replace('_', '-').replace('/', '-').replace('.json', '')}-{int(time.time()) % 100000}",
                      ["bash", f"/pvc/selrm/code/{code}/k8s/prep.sh", a.env, code, q], cpu=2, mem="16Gi",
                      eph="40Gi", hours=2))      # mostly single-threaded: keep median usage >= 20% of request
    elif a.cmd == "runners":
        code = snapshot(a.code)
        q = a.args[0]
        stem = q.split(",")[0].replace("_", "-").replace("/", "-").replace(".json", "")   # q: a queue, a comma list, or all (every queue file)
        for i in range(a.n):
            apply(runner_job(f"selrm-b-run-{stem}-{a.gpu}-{int(time.time()) % 100000}-{i}", q, code, a.env,
                             a.gpu, a.max_runs, a.hours, a.cpu, a.mem, tuple(a.models.split(","))))
    elif a.cmd == "push-ref":        # e.g. push-ref origin/role-a  (A's code + data/REGISTRY.json)
        push_ref(a.args[0])
    elif a.cmd == "build-data":      # build-data <A code sha12> [builder args...]: rebuild + sha256 check + publish
        code = a.args[0]
        apply(cpu_job(f"selrm-b-build-data-{code[:8]}-{int(time.time()) % 100000}",
                      ["bash", f"/pvc/selrm/code/{snapshot(a.code)}/k8s/build_data.sh", a.env, code, *a.args[1:]],
                      cpu=2, mem="12Gi", eph="60Gi", hours=3))
    elif a.cmd == "restore-data":    # restore-data <A code sha12> <set name> <builder script> [args...]
        code = a.args[0]
        apply(cpu_job(f"selrm-b-restore-data-{code[:8]}-{int(time.time()) % 100000}",
                      ["bash", f"/pvc/selrm/code/{snapshot(a.code)}/k8s/restore_data.sh", a.env, code, *a.args[1:]],
                      cpu=2, mem="12Gi", eph="20Gi", hours=2))
    elif a.cmd == "fetch-ref":       # fetch-ref <git ref> [path=url=sha256 ...]: snapshot fetched in the pod (read-only token)
        full = subprocess.run(["git", "-C", REPO, "rev-parse", a.args[0]], capture_output=True, text=True, check=True).stdout.strip()
        job = cpu_job(f"selrm-b-fetch-ref-{full[:8]}-{int(time.time()) % 100000}",
                      ["bash", "-c", f"tar -xf /pvc/selrm/env/selrm-env-{a.env}.tar -C /opt && /opt/selrm-env/venv/bin/python "
                                     f"/pvc/selrm/code/{snapshot(a.code)}/k8s/fetch_ref.py {full} " + " ".join(a.args[1:])],
                      cpu=1, mem="4Gi", eph="20Gi", hours=1)
        job["spec"]["template"]["spec"]["containers"][0]["env"].append(
            {"name": "GH_TOKEN", "valueFrom": {"secretKeyRef": {"name": "selrm-github-ro", "key": "token"}}})
        apply(job)
        print("code", full[:12])
    elif a.cmd == "copy-c":          # copy-c <C code sha12> <set> [...]: C's frozen clin_v1 sets, PVC selrm-c read-only
        job = cpu_job(f"selrm-b-copy-c-{int(time.time()) % 100000}",
                      ["bash", f"/pvc/selrm/code/{snapshot(a.code)}/k8s/copy_c_data.sh", a.env, *a.args],
                      cpu=1, mem="4Gi", eph="10Gi", hours=1)
        pod = job["spec"]["template"]["spec"]
        pod["volumes"].append({"name": "pvc-c", "persistentVolumeClaim": {"claimName": "selrm-c", "readOnly": True}})
        pod["containers"][0]["volumeMounts"].append({"name": "pvc-c", "mountPath": "/c", "readOnly": True})
        apply(job)
    elif a.cmd == "publish":         # publish <hf repo> --secret NAME:KEY  (only once the user confirmed the secret)
        name, key = a.secret.split(":")
        job = cpu_job(f"selrm-b-publish-{int(time.time()) % 100000}",
                      ["bash", "-c", f"tar -xf /pvc/selrm/env/selrm-env-{a.env}.tar -C /opt && "
                                     f"/opt/selrm-env/venv/bin/python /pvc/selrm/code/{snapshot(a.code)}/scripts/publish_adapters_b.py "
                                     f"--root /pvc/selrm --repo {a.args[0]}"], cpu=1, mem="2Gi", eph="20Gi", hours=1)
        job["spec"]["template"]["spec"]["containers"][0]["env"].append(
            {"name": "HF_TOKEN", "valueFrom": {"secretKeyRef": {"name": name, "key": key}}})
        apply(job)
    elif a.cmd == "pull":
        pull(a.args)
    elif a.cmd == "ls":       # claim/heartbeat/done state of every run on the PVC
        print(exec_sync("sh", "-c", "cd /pvc/selrm/results 2>/dev/null && now=$(date +%s) && for d in */; do "
                                    "hb=$(stat -c %Y $d/HEARTBEAT 2>/dev/null || echo $now); "
                                    "echo \"$d hb_age=$((now-hb))s $(ls $d | grep -E '^(CLAIMED_|DONE|FAILED_|KILLED_)' | tr '\\n' ' ')\"; done"))
    else:
        sys.exit(f"unknown command {a.cmd}")


if __name__ == "__main__":
    main()
