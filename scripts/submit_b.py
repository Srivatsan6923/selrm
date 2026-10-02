"""Role-B launcher for NRP Nautilus (namespace ecepxie, PVC selrm-b). Builds the
Kubernetes objects as JSON and applies them with kubectl. Laptop side only.
  python scripts/submit_b.py sync-up | sync-down          # short interactive CPU pod for copies
  python scripts/submit_b.py push-code                    # code snapshot -> /pvc/selrm/code/<sha>
  python scripts/submit_b.py push-queue QUEUE.json        # -> /pvc/selrm/queue/<name>
  python scripts/submit_b.py build-env TAG                # CPU Job: env tarball
  python scripts/submit_b.py prep QUEUE_NAME              # CPU Job: data, weights, pretok
  python scripts/submit_b.py runners QUEUE_NAME --n 3 --gpu a100 --max-runs 3 --hours 4
  python scripts/submit_b.py pull RUN_ID [RUN_ID ...]     # results -> results_git/<run_id>/
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


def runner_job(name, queue, code, env_tag, gpu, max_runs, hours, cpu=3, mem="24Gi", models=("unsloth--Qwen3.5-9B",)):
    resource, products, prio = GPU[gpu]
    terms = [DRIVER] + ([{"key": "nvidia.com/gpu.product", "operator": "In", "values": products}] if products else [])
    pod = {"restartPolicy": "Never", "affinity": affinity(terms),
           "initContainers": [{"name": "stage", "image": IMAGE,
                               "command": ["sh", f"/pvc/selrm/code/{code}/k8s/stage.sh", env_tag, code, *models],
                               "resources": res(3, "8Gi", "64Gi"),
                               "volumeMounts": [MNT_PVC, {"name": "work", "mountPath": "/work"},
                                                {"name": "env", "mountPath": "/opt/selrm-env"}]}],
           "containers": [{"name": "runner", "image": IMAGE, "workingDir": "/work",
                           "command": ["/opt/selrm-env/venv/bin/python", "-u", "/work/code/scripts/train_eval_job.py",
                                       "--root", "/pvc/selrm", "--queue", f"/pvc/selrm/queue/{queue}",
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
            "spec": {"restartPolicy": "Never", "activeDeadlineSeconds": 3600,
                     "affinity": affinity([CPU_ONLY, {"key": "topology.kubernetes.io/region", "operator": "In",
                                                      "values": ["us-west"]}]),
                     "containers": [{"name": "sync", "image": SMALL_IMAGE, "command": ["sh", "-c", "sleep 3000"],
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


def exec_sync(*cmd, inp=None):
    return kubectl("exec", *(["-i"] if inp is not None else []), "selrm-b-sync", "--", *cmd, inp=inp)


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
        if os.path.exists(f"{REPO}/results_git/{rid}/DONE"):
            continue
        data = subprocess.run(["kubectl", "-n", NS, "exec", "selrm-b-sync", "--", "sh", "-c",
                               f"cd /pvc/selrm/results && tar -czf - {rid}/meta.json {rid}/DONE "
                               f"$(ls {rid}/summary_*.json {rid}/scores_*.jsonl {rid}/gpu_util.csv 2>/dev/null)"],
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
    ap.add_argument("--cpu", type=int, default=3)
    ap.add_argument("--mem", default="24Gi")
    ap.add_argument("--code", default=None)
    a = ap.parse_args()
    if a.cmd == "sync-up":
        apply(sync_pod()); wait_running("selrm-b-sync"); print("selrm-b-sync running")
    elif a.cmd == "sync-down":
        print(kubectl("delete", "pod", "selrm-b-sync", "--wait=false", check=False))
    elif a.cmd == "push-code":
        push_code()
    elif a.cmd == "push-queue":
        src = a.args[0]
        name = os.path.basename(src)
        exec_sync("sh", "-c", f"mkdir -p /pvc/selrm/queue && cat > /pvc/selrm/queue/{name}.tmp && "
                              f"mv /pvc/selrm/queue/{name}.tmp /pvc/selrm/queue/{name}", inp=open(src, "rb").read())
        print(f"queue {name} pushed")
    elif a.cmd == "build-env":
        code = a.code or sha()
        apply(cpu_job(f"selrm-b-build-env-{a.args[0]}", ["bash", f"/pvc/selrm/code/{code}/k8s/build_env.sh", a.args[0]],
                      cpu=6, mem="12Gi", eph="80Gi", hours=2))   # compile uses ~3-6 cores; usage must stay >=20% of request
    elif a.cmd == "prep":
        code = a.code or sha()
        q = a.args[0]
        apply(cpu_job(f"selrm-b-prep-{q.replace('_', '-').replace('.json', '')}-{int(time.time()) % 100000}",
                      ["bash", f"/pvc/selrm/code/{code}/k8s/prep.sh", a.env, code, q], cpu=2, mem="16Gi",
                      eph="40Gi", hours=2))      # mostly single-threaded: keep median usage >= 20% of request
    elif a.cmd == "runners":
        code = a.code or sha()
        q = a.args[0]
        stem = q.replace("_", "-").replace(".json", "")
        for i in range(a.n):
            apply(runner_job(f"selrm-b-run-{stem}-{a.gpu}-{int(time.time()) % 100000}-{i}", q, code, a.env,
                             a.gpu, a.max_runs, a.hours, a.cpu, a.mem))
    elif a.cmd == "pull":
        pull(a.args)
    elif a.cmd == "ls":       # claim/heartbeat/done state of every run on the PVC
        print(exec_sync("sh", "-c", "cd /pvc/selrm/results 2>/dev/null && for d in */; do "
                                    "echo \"$d $(ls $d | grep -E '^(CLAIMED_|DONE|FAILED_)' | tr '\\n' ' ')\"; done"))
    else:
        sys.exit(f"unknown command {a.cmd}")


if __name__ == "__main__":
    main()
