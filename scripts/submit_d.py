"""Role-D launcher for NRP Nautilus (namespace ecepxie). Laptop side only; builds the
Kubernetes objects as JSON and applies them with kubectl.

  python scripts/submit_d.py pvc                       # once: PVC selrm-d (rook-cephfs, RWX)
  python scripts/submit_d.py sync-up | sync-down       # small CPU pod for copies (<= 6 h)
  python scripts/submit_d.py push-code                 # code snapshot -> /pvc/code/<sha12>
  python scripts/submit_d.py build-env TAG             # CPU Job: env tarball (k8s/build_env_d.sh)
  python scripts/submit_d.py gpu NAME --gpu a40 --hours 6 [--models DIR,DIR] -- scripts/make_pool.py ...
  python scripts/submit_d.py cpu NAME --mem 64Gi --hours 2 -- scripts/merge_adapter.py ...
  python scripts/submit_d.py pull REMOTE LOCAL         # copy a result directory from the PVC
  python scripts/submit_d.py ls [PATH]

Rules (docs/NRP_B.md, binding for D too): objects are named selrm-d-* and labelled
app=selrm-d; one GPU per Job; requests == limits; no sleep in Jobs; CPU Jobs off GPU
nodes; prefer 48 GB cards (a40, a6000, l40) because B holds the A100 quota; GPU Jobs
must keep the GPU busy (vLLM generation does) and end by themselves. D's PVC is mounted
at /pvc; B's PVC selrm-b read-only at /pvcb (base weights, kept adapters, data).
"""
import argparse
import io
import json
import os
import subprocess
import sys
import tarfile
import time

NS, PVC, PVC_B = "ecepxie", "selrm-d", "selrm-b"
IMAGE = "nvcr.io/nvidia/cuda:13.0.3-cudnn-devel-ubuntu24.04"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIRS = ("selrm", "scripts", "k8s", "configs")
LABELS = {"app": "selrm-d"}
GPU = {"a40": ("nvidia.com/a40", None), "a6000": ("nvidia.com/rtxa6000", None),
       "l40": ("nvidia.com/gpu", ["NVIDIA-L40", "NVIDIA-L40S"]),
       "a100": ("nvidia.com/a100", ["NVIDIA-A100-SXM4-80GB", "NVIDIA-A100-80GB-PCIe", "NVIDIA-A100-PCIE-40GB"]),
       "24gb": ("nvidia.com/gpu", ["NVIDIA-GeForce-RTX-3090", "NVIDIA-A10", "NVIDIA-GeForce-RTX-4090", "NVIDIA-RTX-A5000"]),
       "pro6000": ("nvidia.com/gpu", ["NVIDIA-RTX-PRO-6000-Blackwell-Max-Q-Workstation-Edition"])}
CPU_ONLY = {"key": "feature.node.kubernetes.io/pci-10de.present", "operator": "NotIn", "values": ["true"]}
DRIVER = {"key": "nvidia.com/cuda.driver.major", "operator": "Gt", "values": ["579"]}
VOLS = [{"name": "pvc", "persistentVolumeClaim": {"claimName": PVC}},
        {"name": "pvcb", "persistentVolumeClaim": {"claimName": PVC_B, "readOnly": True}}]
MNTS = [{"name": "pvc", "mountPath": "/pvc"}, {"name": "pvcb", "mountPath": "/pvcb", "readOnly": True}]


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


def sha():
    return subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True,
                          text=True, check=True).stdout.strip()


def job(name, pod, hours, role):
    labels = LABELS | {"role": role}
    return {"apiVersion": "batch/v1", "kind": "Job", "metadata": {"name": name, "namespace": NS, "labels": labels},
            "spec": {"backoffLimit": 1, "ttlSecondsAfterFinished": 259200, "activeDeadlineSeconds": int(hours * 3600),
                     "template": {"metadata": {"labels": labels}, "spec": pod}}}


def cpu_job(name, command, cpu=8, mem="32Gi", eph="80Gi", hours=2):
    pod = {"restartPolicy": "Never", "affinity": affinity([CPU_ONLY]),
           "containers": [{"name": "main", "image": IMAGE, "command": command, "resources": res(cpu, mem, eph),
                           "volumeMounts": MNTS}], "volumes": VOLS}
    return job(name, pod, hours, "cpu")


def gpu_job(name, code, env_tag, gpu, hours, args, cpu=3, mem="24Gi", models=("/pvcb/selrm/models/unsloth--Qwen3.5-9B",),
            n_gpu=1, eph="40Gi"):
    resource, products = GPU[gpu]
    terms = [DRIVER] + ([{"key": "nvidia.com/gpu.product", "operator": "In", "values": products}] if products else [])
    if gpu == "24gb":       # 36 of 48 RTX 3090 nodes are in us-west, next to the CephFS: reading 19 GB of weights
        terms.append({"key": "topology.kubernetes.io/region", "operator": "In", "values": ["us-west"]})  # elsewhere takes ~1 h
    env = f"/pvc/env/selrm-d-env-{env_tag}.tar"     # the gzip copy halves the bytes read from CephFS
    stage = (f"set -e; if [ -f {env}.gz ]; then tar -xzf {env}.gz -C /opt; else tar -xf {env} -C /opt; fi; "
             f"cp -r /pvc/code/{code} /work/code; "
             "mkdir -p /work/models; " + " ".join(f"cp -r {m} /work/models/;" for m in models if m)
             + " echo staged")
    work = [{"name": "work", "mountPath": "/work"}, {"name": "env", "mountPath": "/opt/selrm-env"}]
    aff = affinity(terms)       # prefer us-west: the CephFS pools (PVCs) are there; reads elsewhere are slower
    aff["nodeAffinity"]["preferredDuringSchedulingIgnoredDuringExecution"] = [{"weight": 100, "preference": {
        "matchExpressions": [{"key": "topology.kubernetes.io/region", "operator": "In", "values": ["us-west"]}]}}]
    pod = {"restartPolicy": "Never", "affinity": aff,
           "initContainers": [{"name": "stage", "image": IMAGE, "command": ["sh", "-c", stage],
                               "resources": res(2, "8Gi", eph), "volumeMounts": MNTS + work}],
           "containers": [{"name": "main", "image": IMAGE, "workingDir": "/work/code",
                           "command": ["sh", *args] if args[0].endswith(".sh") else
                                      ["/opt/selrm-env/venv/bin/python", "-u", *args],
                           "env": [{"name": k, "value": v} for k, v in {
                               "HF_HOME": "/work/hf", "TRITON_CACHE_DIR": "/work/triton", "VLLM_CACHE_ROOT": "/work/vllm",
                               "PYTHONPYCACHEPREFIX": "/work/pycache", "TOKENIZERS_PARALLELISM": "false",
                               "OMP_NUM_THREADS": "4", "SELRM_MODELS": "/work/models",
                               # FlashInfer's sampler JIT-compiles at start-up (needs ninja); torch sampling instead
                               "VLLM_USE_FLASHINFER_SAMPLER": "0",
                               "PATH": "/opt/selrm-env/venv/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/bin:/bin"}.items()],
                           "resources": res(cpu, mem, eph, {resource: str(n_gpu)}),
                           "volumeMounts": MNTS + work + [{"name": "dshm", "mountPath": "/dev/shm"}]}],
           "volumes": VOLS + [{"name": "work", "emptyDir": {}}, {"name": "env", "emptyDir": {}},
                              {"name": "dshm", "emptyDir": {"medium": "Memory", "sizeLimit": "8Gi"}}]}
    return job(name, pod, hours, "gpu")


def sync_pod():
    return {"apiVersion": "v1", "kind": "Pod",
            "metadata": {"name": "selrm-d-sync", "namespace": NS, "labels": LABELS | {"role": "sync"}},
            "spec": {"restartPolicy": "Never", "activeDeadlineSeconds": 21600, "affinity": affinity([CPU_ONLY]),
                     "containers": [{"name": "main", "image": IMAGE, "command": ["sleep", "21000"],
                                     "resources": res(1, "2Gi", "10Gi"), "volumeMounts": MNTS}],
                     "volumes": VOLS}}


def exec_sync(*cmd, inp=None):
    return kubectl("exec", "-i", "selrm-d-sync", "--", *cmd, inp=inp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("rest", nargs="*")
    ap.add_argument("--gpu", default="a40")
    ap.add_argument("--hours", type=float, default=6)
    ap.add_argument("--env", default="v1")
    ap.add_argument("--code", default=None)
    ap.add_argument("--models", default=None, help="comma-separated dirs copied to /work/models (gpu)")
    ap.add_argument("--cpu", type=int, default=8)
    ap.add_argument("--n-gpu", dest="n_gpu", type=int, default=1, help="GPUs per pod (e.g. 2 x 24gb with --tp 2)")
    ap.add_argument("--gpu-cpu", dest="gpu_cpu", type=int, default=3)
    ap.add_argument("--gpu-mem", dest="gpu_mem", default="24Gi")
    ap.add_argument("--mem", default="32Gi")
    a, extra = ap.parse_known_args()
    if "--" in a.rest:                     # "... NAME -- script args": argparse keeps the separator
        i = a.rest.index("--")
        a.rest = a.rest[:i] + a.rest[i + 1:]
    extra = [x for x in extra if x != "--"]
    if a.cmd == "pvc":
        apply({"apiVersion": "v1", "kind": "PersistentVolumeClaim",
               "metadata": {"name": PVC, "namespace": NS, "labels": LABELS},
               "spec": {"storageClassName": "rook-cephfs", "accessModes": ["ReadWriteMany"],
                        "resources": {"requests": {"storage": "150Gi"}}}})
    elif a.cmd == "sync-up":
        apply(sync_pod())
        kubectl("wait", "--for=condition=Ready", "pod/selrm-d-sync", "--timeout=600s")
    elif a.cmd == "sync-down":
        print(kubectl("delete", "pod", "selrm-d-sync", "--wait=false", check=False))
    elif a.cmd == "push-code":
        code, buf = sha(), io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as t:
            for d in CODE_DIRS:
                t.add(os.path.join(REPO, d), arcname=d,
                      filter=lambda x: None if "__pycache__" in x.name else x)
        exec_sync("sh", "-c", f"mkdir -p /pvc/code/{code} && tar -xzf - -C /pvc/code/{code} && echo {code} > /pvc/code/{code}/COMMIT",
                  inp=buf.getvalue())
        print("pushed", code)
    elif a.cmd == "build-env":
        code = a.code or sha()
        apply(cpu_job(f"selrm-d-build-env-{a.rest[0]}", ["bash", f"/pvc/code/{code}/k8s/build_env_d.sh", a.rest[0]],
                      hours=2))
    elif a.cmd == "gpu":
        name, args = a.rest[0], a.rest[1:] + extra
        models = a.models.split(",") if a.models is not None else ("/pvcb/selrm/models/unsloth--Qwen3.5-9B",)
        apply(gpu_job(f"selrm-d-{name}-{int(time.time()) % 100000}", a.code or sha(), a.env, a.gpu, a.hours, args,
                      models=models, n_gpu=a.n_gpu, cpu=a.gpu_cpu, mem=a.gpu_mem))
    elif a.cmd == "cpu":        # a python (or .sh) script of the code snapshot, on a CPU node
        name, args, code = a.rest[0], a.rest[1:] + extra, a.code or sha()
        cmd = (f"set -e; cd /pvc/code/{code}; sh " + " ".join(args) if args[0].endswith(".sh") else
               f"set -e; tar -xf /pvc/env/selrm-d-env-{a.env}.tar -C /opt; cd /pvc/code/{code}; "
               "/opt/selrm-env/venv/bin/python -u " + " ".join(args))
        apply(cpu_job(f"selrm-d-{name}-{int(time.time()) % 100000}", ["sh", "-c", cmd], cpu=a.cpu, mem=a.mem,
                      hours=a.hours))
    elif a.cmd == "pull":
        remote, local = a.rest
        os.makedirs(local, exist_ok=True)
        data = subprocess.run(["kubectl", "-n", NS, "exec", "selrm-d-sync", "--", "tar", "-cf", "-", "-C",
                               os.path.dirname(remote), os.path.basename(remote)], capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            t.extractall(local)
        print("pulled", remote, "->", local)
    elif a.cmd == "ls":
        print(exec_sync("sh", "-c", f"ls -la {a.rest[0] if a.rest else '/pvc'}"))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
