"""Role-C launcher for NRP Nautilus (namespace ecepxie). Laptop side only. Pattern and
policy follow role B's launcher (docs/NRP_B.md on role-b, binding for C):
one GPU per Job, requests == limits, no sleep in Jobs, CPU Jobs off GPU nodes, a runner
exits when its task list has nothing claimable. C's objects are named selrm-c-* with
label app=selrm-c; C writes only its own PVC selrm-c (mounted at /pvc) and mounts B's
PVC selrm-b read-only at /pvcb (env tarball, base weights, rule_v1 data, adapters).
  python scripts/submit_c.py sync-up | sync-down
  python scripts/submit_c.py push-code                  # HEAD snapshot -> /pvc/selrmc/code/<sha12>
  python scripts/submit_c.py push FILE DEST             # small file -> /pvc/selrmc/DEST
  python scripts/submit_c.py sh "CMD"                   # run a shell command in the sync pod
  python scripts/submit_c.py runner TASKS.json --gpu l40 --hours 8 [--bcode SHA] [--n 1]
  python scripts/submit_c.py pull [RUN_ID ...]          # finished runs -> results_git/<run_id>/ (as role B)
"""
import argparse, io, json, os, subprocess, sys, tarfile, time

NS, PVC, PVCB = "ecepxie", "selrm-c", "selrm-b"
ROOT = "/pvc/selrmc"                     # C's root on its own volume
BROOT = "/pvcb/selrm"                    # B's root, read-only
IMAGE = "nvcr.io/nvidia/cuda:13.0.3-cudnn-devel-ubuntu24.04"
SMALL_IMAGE = "nvcr.io/nvidia/cuda:13.0.3-base-ubuntu24.04"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIRS = ("selrm", "scripts", "k8s", "configs", "tests")
GPU = {   # kind -> (resource, gpu.product values or None)
    "a100": ("nvidia.com/a100", ["NVIDIA-A100-SXM4-80GB", "NVIDIA-A100-80GB-PCIe", "NVIDIA-A100-PCIE-40GB"]),
    "l40": ("nvidia.com/gpu", ["NVIDIA-L40", "NVIDIA-L40S"]),
    "a6000": ("nvidia.com/rtxa6000", None),
    "a40": ("nvidia.com/a40", None),
    "32gb": ("nvidia.com/gpu", ["NVIDIA-RTX-5000-Ada-Generation"]),
    "24gb": ("nvidia.com/gpu", ["NVIDIA-A10", "NVIDIA-GeForce-RTX-3090", "NVIDIA-L4", "NVIDIA-GeForce-RTX-4090",
                                "NVIDIA-RTX-A5000", "NVIDIA-TITAN-RTX", "Quadro-RTX-6000"]),   # verdict runs only
}
CPU_ONLY = {"key": "feature.node.kubernetes.io/pci-10de.present", "operator": "NotIn", "values": ["true"]}
DRIVER = {"key": "nvidia.com/cuda.driver.major", "operator": "Gt", "values": ["579"]}   # cu130 needs >= 580
VOLS = [{"name": "pvc", "persistentVolumeClaim": {"claimName": PVC}},
        {"name": "pvcb", "persistentVolumeClaim": {"claimName": PVCB, "readOnly": True}}]
MNTS = [{"name": "pvc", "mountPath": "/pvc"}, {"name": "pvcb", "mountPath": "/pvcb", "readOnly": True}]


def kubectl(*args, inp=None, check=True):
    r = subprocess.run(["kubectl", "-n", NS, *args], input=inp, capture_output=True)
    if check and r.returncode:
        sys.exit(f"kubectl {' '.join(args[:3])} failed: {r.stderr.decode(errors='replace')}")
    return r.stdout.decode(errors="replace")


def apply(obj):
    print(kubectl("apply", "-f", "-", inp=json.dumps(obj).encode()).strip())


def affinity(terms):
    return {"nodeAffinity": {"requiredDuringSchedulingIgnoredDuringExecution": {
        "nodeSelectorTerms": [{"matchExpressions": terms}]}}}


def res(cpu, mem, eph, extra=None):
    r = {"cpu": str(cpu), "memory": mem, "ephemeral-storage": eph} | (extra or {})
    return {"requests": r, "limits": dict(r)}


def sha():
    return subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True,
                          text=True, check=True).stdout.strip()


def sync_pod():
    """Bare helper pod for copies (sleep is allowed only in bare pods; NRP cap 6 h; 1 CPU / 1 GiB)."""
    return {"apiVersion": "v1", "kind": "Pod",
            "metadata": {"name": "selrm-c-sync", "namespace": NS, "labels": {"app": "selrm-c", "role": "sync"}},
            "spec": {"restartPolicy": "Never", "activeDeadlineSeconds": 21600,
                     "affinity": affinity([CPU_ONLY, {"key": "topology.kubernetes.io/region", "operator": "In",
                                                      "values": ["us-west"]}]),
                     "containers": [{"name": "sync", "image": SMALL_IMAGE, "command": ["sh", "-c", "sleep 21000"],
                                     "resources": res(1, "1Gi", "2Gi"), "volumeMounts": MNTS}],
                     "volumes": VOLS}}


def exec_sync(*cmd, inp=None, check=True):
    return kubectl("exec", *(["-i"] if inp is not None else []), "selrm-c-sync", "--", *cmd, inp=inp, check=check)


def wait_running(pod, timeout=600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        if kubectl("get", "pod", pod, "-o", "jsonpath={.status.phase}", check=False) == "Running":
            return
        time.sleep(5)
    sys.exit(f"{pod} not running after {timeout} s")


def push_code():
    """Snapshot of the committed tree (git archive HEAD of CODE_DIRS): uncommitted files are never pushed."""
    code = sha()
    data = subprocess.run(["git", "-C", REPO, "archive", "--format=tar", "HEAD", *CODE_DIRS],
                          capture_output=True, check=True).stdout
    dest = f"{ROOT}/code/{code}"
    exec_sync("sh", "-c", f"mkdir -p {dest}.tmp && tar -xf - -C {dest}.tmp && echo {code} > {dest}.tmp/COMMIT && "
                          f"rm -rf {dest} && mv {dest}.tmp {dest}", inp=data)
    print(f"code {code} -> {dest} ({len(data)} bytes)")
    return code


def runner_job(name, tasks, code, bcode, env_tag, gpu, hours, cpu=2, mem="12Gi", models=("unsloth--Qwen3.5-9B",),
               formats="", online=False):
    """GPU runner: init container stages env, B's and C's code and the base weights on local NVMe;
    main container runs scripts/eval_c.py over a task list (claim -> evaluate -> DONE -> next)."""
    resource, products = GPU[gpu]
    # us-west / us-central only (staging 20+ GB from the us-west CephFS pool to a us-east node took > 40 min, and
    # some remote nodes lack its CSI driver); us-west preferred
    terms = [DRIVER, {"key": "topology.kubernetes.io/region", "operator": "In", "values": ["us-west", "us-central"]}] \
        + ([{"key": "nvidia.com/gpu.product", "operator": "In", "values": products}] if products else [])
    mounts = MNTS + [{"name": "work", "mountPath": "/work"}, {"name": "env", "mountPath": "/opt/selrm-env"}]
    aff = affinity(terms)
    aff["nodeAffinity"]["preferredDuringSchedulingIgnoredDuringExecution"] = [{"weight": 100, "preference": {
        "matchExpressions": [{"key": "topology.kubernetes.io/region", "operator": "In", "values": ["us-west"]}]}}]
    pod = {"restartPolicy": "Never", "affinity": aff,
           "initContainers": [{"name": "stage", "image": IMAGE,
                               "command": ["sh", f"{ROOT}/code/{code}/k8s/stage_c.sh", env_tag, bcode, code, *models],
                               "resources": res(3, "8Gi", "64Gi"), "volumeMounts": mounts}],
           "containers": [{"name": "runner", "image": IMAGE, "workingDir": "/work",
                           "command": ["/opt/selrm-env/venv/bin/python", "-u", "/work/code/scripts/eval_c.py",
                                       "--root", ROOT, "--broot", BROOT, "--bcode", "/work/bcode",
                                       "--tasks", f"{ROOT}/tasks/{tasks}", "--formats", formats],
                           "env": [{"name": k, "value": v} for k, v in {
                               "SELRM_MODELS": "/work/models", "HF_HOME": "/work/hf",
                               "HF_HUB_OFFLINE": "0" if online else "1", "TRANSFORMERS_OFFLINE": "0" if online else "1",
                               "TRITON_CACHE_DIR": "/work/triton",
                               "PYTHONPYCACHEPREFIX": "/work/pycache", "OMP_NUM_THREADS": "3",
                               "MKL_NUM_THREADS": "3", "TOKENIZERS_PARALLELISM": "false",
                               "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True"}.items()]
                           + [{"name": "POD_NAME", "valueFrom": {"fieldRef": {"fieldPath": "metadata.name"}}},
                              {"name": "NODE_NAME", "valueFrom": {"fieldRef": {"fieldPath": "spec.nodeName"}}}],
                           "resources": res(cpu, mem, "64Gi", {resource: "1"}),
                           "volumeMounts": mounts + [{"name": "dshm", "mountPath": "/dev/shm"}]}],
           "volumes": VOLS + [{"name": "work", "emptyDir": {}}, {"name": "env", "emptyDir": {}},
                              {"name": "dshm", "emptyDir": {"medium": "Memory", "sizeLimit": "4Gi"}}]}
    labels = {"app": "selrm-c", "role": "runner", "gpu": gpu}
    return {"apiVersion": "batch/v1", "kind": "Job", "metadata": {"name": name, "namespace": NS, "labels": labels},
            "spec": {"backoffLimit": 1, "ttlSecondsAfterFinished": 259200, "activeDeadlineSeconds": int(hours * 3600),
                     "template": {"metadata": {"labels": labels}, "spec": pod}}}


def pull(run_ids):
    """Finished runs (DONE) -> results_git/<run_id>/ (meta, summaries, scores, DONE, logs), as role B."""
    have = exec_sync("sh", "-c", f"cd {ROOT}/results 2>/dev/null && ls -d */DONE 2>/dev/null | cut -d/ -f1").split()
    want = [r for r in (run_ids or have) if r in have]
    for rid in want:
        local = f"{REPO}/results_git/{rid}/DONE"
        if os.path.exists(local) and open(local).read() == exec_sync("cat", f"{ROOT}/results/{rid}/DONE"):
            continue
        data = subprocess.run(["kubectl", "-n", NS, "exec", "selrm-c-sync", "--", "sh", "-c",
                               f"cd {ROOT}/results && tar -czf - {rid}/meta.json {rid}/DONE "
                               f"$(ls {rid}/summary_*.json {rid}/scores_*.jsonl {rid}/gpu_util.csv {rid}/run.log 2>/dev/null)"],
                              capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            tar.extractall(f"{REPO}/results_git", filter="data")
        print(f"pulled {rid} ({len(data)} bytes gz)")
    print("not DONE on the PVC:", " ".join(sorted(set(run_ids or []) - set(have))) or "-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--gpu", default="l40", choices=sorted(GPU))
    ap.add_argument("--hours", type=float, default=8)
    ap.add_argument("--env", default="v1")
    ap.add_argument("--bcode", default=None, help="B's code snapshot (sha12 under /pvcb/selrm/code)")
    ap.add_argument("--code", default=None)
    ap.add_argument("--models", default="unsloth--Qwen3.5-9B")
    ap.add_argument("--formats", default="", help="runner claims only runs of these formats (comma list)")
    ap.add_argument("--online", action="store_true", help="Hub access on (PRM runs download their weights)")
    a = ap.parse_args()
    if a.cmd == "sync-up":
        apply(sync_pod()); wait_running("selrm-c-sync"); print("selrm-c-sync running")
    elif a.cmd == "sync-down":
        print(kubectl("delete", "pod", "selrm-c-sync", "--wait=false", check=False))
    elif a.cmd == "push-code":
        push_code()
    elif a.cmd == "push":
        src, dest = a.args
        exec_sync("sh", "-c", f"mkdir -p $(dirname {ROOT}/{dest}) && cat > {ROOT}/{dest}.tmp && "
                              f"mv {ROOT}/{dest}.tmp {ROOT}/{dest}", inp=open(src, "rb").read())
        print(f"{src} -> {ROOT}/{dest}")
    elif a.cmd == "sh":
        print(exec_sync("sh", "-c", a.args[0]), end="")
    elif a.cmd == "runner":
        code = a.code or sha()
        # a Job started on a snapshot that is not on the PVC fails at once in its init container
        if subprocess.run(["kubectl", "-n", NS, "exec", "selrm-c-sync", "--", "test", "-d", f"{ROOT}/code/{code}"],
                          capture_output=True).returncode:
            if code != sha():
                sys.exit(f"code snapshot {code} is not on the PVC")
            push_code()
        if not a.bcode:
            sys.exit("--bcode (B's code snapshot under /pvcb/selrm/code) is required")
        stem = a.args[0].replace("_", "-").replace(".json", "")
        for i in range(a.n):
            apply(runner_job(f"selrm-c-run-{stem}-{a.gpu}-{int(time.time()) % 100000}-{i}", a.args[0], code, a.bcode,
                             a.env, a.gpu, a.hours, models=tuple(m for m in a.models.split(",") if m),
                             formats=a.formats, online=a.online))
    elif a.cmd == "pull":
        pull(a.args)
    else:
        sys.exit(f"unknown command {a.cmd}")


if __name__ == "__main__":
    main()
