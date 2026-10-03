"""Role-D launcher for NRP Nautilus (namespace ecepxie). Laptop side only; builds the
Kubernetes objects as JSON and applies them with kubectl. In Git Bash set MSYS_NO_PATHCONV=1.

  python scripts/submit_d.py pvc [--site central]       # once per site: D's PVC (RWX CephFS of that region)
  python scripts/submit_d.py sync-up | sync-down [--site central]   # small CPU pod for copies (<= 6 h)
  python scripts/submit_d.py push-code [--site central]  # code snapshot -> /pvc/code/<sha12>
  python scripts/submit_d.py build-env TAG               # CPU Job: env tarball (k8s/build_env_d.sh)
  python scripts/submit_d.py mirror-central              # CPU Job: copy/download what GPU jobs read to central
  python scripts/submit_d.py gpu NAME --gpu 24gb --n-gpu 2 [--site central] -- scripts/score_pool.py ...
  python scripts/submit_d.py cpu NAME --mem 64Gi --hours 2 -- scripts/merge_adapter.py ...
  python scripts/submit_d.py pull REMOTE LOCAL [--site central]
  python scripts/submit_d.py ls [PATH] [--site central]

Sites. Each job reads a PVC of its own region: reading 19 GB of weights across regions took
about an hour (3 Oct). west: D's PVC selrm-d at /pvc and B's PVC selrm-b read-only at /pvcb
(base weights, kept adapters, data). central: D's PVC selrm-d-central at /pvc only (one mount);
k8s/mirror_central_d.sh puts B's files under /pvc/selrm/..., so a west path /pvcb/selrm/x is
/pvc/selrm/x there (k8s/pool_pipeline_d.sh falls back to it).

Rules (docs/NRP_B.md, binding for D too): objects are named selrm-d-* and labelled
app=selrm-d; requests == limits; no sleep in Jobs; CPU Jobs off GPU nodes; B holds the
A100 quota; GPU Jobs keep the GPU busy (vLLM does) and end by themselves.
"""
import argparse
import io
import json
import os
import subprocess
import sys
import tarfile
import time

NS = "ecepxie"
IMAGE = "nvcr.io/nvidia/cuda:13.0.3-cudnn-devel-ubuntu24.04"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIRS = ("selrm", "scripts", "k8s", "configs",
             "data/xr_v1/KNOWN_ISSUES.json")   # read by jobs that score xr_v1 (a job failed without it, 3 Oct)
LABELS = {"app": "selrm-d"}
SITES = {"west": {"pvc": "selrm-d", "pvcb": "selrm-b", "region": "us-west", "storage": "rook-cephfs",
                  "sync": "selrm-d-sync"},
         "central": {"pvc": "selrm-d-central", "pvcb": None, "region": "us-central",
                     "storage": "rook-cephfs-central", "sync": "selrm-d-sync-c"}}
SITE = SITES["west"]
GPU = {"a40": ("nvidia.com/a40", None), "a6000": ("nvidia.com/rtxa6000", None),
       "l40": ("nvidia.com/gpu", ["NVIDIA-L40", "NVIDIA-L40S"]),
       "a100": ("nvidia.com/a100", ["NVIDIA-A100-SXM4-80GB", "NVIDIA-A100-80GB-PCIe", "NVIDIA-A100-PCIE-40GB"]),
       "24gb": ("nvidia.com/gpu", ["NVIDIA-GeForce-RTX-3090", "NVIDIA-A10", "NVIDIA-GeForce-RTX-4090", "NVIDIA-RTX-A5000"]),
       "pro6000": ("nvidia.com/gpu", ["NVIDIA-RTX-PRO-6000-Blackwell-Max-Q-Workstation-Edition"]),
       # opportunistic H100s (priorityClassName opportunistic, as role B; preemptible: every step is resumable)
       "h100-opp": ("nvidia.com/h100", None)}
OPPORTUNISTIC = {"h100-opp"}
CPU_ONLY = {"key": "feature.node.kubernetes.io/pci-10de.present", "operator": "NotIn", "values": ["true"]}
DRIVER = {"key": "nvidia.com/cuda.driver.major", "operator": "Gt", "values": ["579"]}


def vols():
    v = [{"name": "pvc", "persistentVolumeClaim": {"claimName": SITE["pvc"]}}]
    return v + ([{"name": "pvcb", "persistentVolumeClaim": {"claimName": SITE["pvcb"], "readOnly": True}}]
                if SITE["pvcb"] else [])


def mnts():
    m = [{"name": "pvc", "mountPath": "/pvc"}]
    return m + ([{"name": "pvcb", "mountPath": "/pvcb", "readOnly": True}] if SITE["pvcb"] else [])


def region():
    return {"key": "topology.kubernetes.io/region", "operator": "In", "values": [SITE["region"]]}


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


def cpu_job(name, command, cpu=8, mem="32Gi", eph="80Gi", hours=2, extra_vols=(), extra_mnts=()):
    pod = {"restartPolicy": "Never", "affinity": affinity([CPU_ONLY, region()]),
           "containers": [{"name": "main", "image": IMAGE, "command": command, "resources": res(cpu, mem, eph),
                           "volumeMounts": mnts() + list(extra_mnts)}], "volumes": vols() + list(extra_vols)}
    return job(name, pod, hours, "cpu")


def gpu_job(name, code, env_tag, gpu, hours, args, cpu=3, mem="24Gi", models=("/pvcb/selrm/models/unsloth--Qwen3.5-9B",),
            n_gpu=1, eph="40Gi"):
    resource, products = GPU[gpu]
    terms = [DRIVER] + ([{"key": "nvidia.com/gpu.product", "operator": "In", "values": products}] if products else [])
    if gpu not in OPPORTUNISTIC:      # read the site's own PVC; the opportunistic H100s are at SDSC (us-west)
        terms.append(region())
    env = f"/pvc/env/selrm-d-env-{env_tag}.tar"     # the gzip copy halves the bytes read from CephFS
    stage = (f"set -e; if [ -f {env}.gz ]; then tar -xzf {env}.gz -C /opt; else tar -xf {env} -C /opt; fi; "
             f"cp -r /pvc/code/{code} /work/code; "
             "mkdir -p /work/models; " + " ".join(f"cp -r {m} /work/models/;" for m in models if m)
             + " echo staged")
    work = [{"name": "work", "mountPath": "/work"}, {"name": "env", "mountPath": "/opt/selrm-env"}]
    pod = {"restartPolicy": "Never", "affinity": affinity(terms),
           "initContainers": [{"name": "stage", "image": IMAGE, "command": ["sh", "-c", stage],
                               "resources": res(2, "8Gi", eph), "volumeMounts": mnts() + work}],
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
                           "volumeMounts": mnts() + work + [{"name": "dshm", "mountPath": "/dev/shm"}]}],
           "volumes": vols() + [{"name": "work", "emptyDir": {}}, {"name": "env", "emptyDir": {}},
                                {"name": "dshm", "emptyDir": {"medium": "Memory", "sizeLimit": "8Gi"}}]}
    if gpu in OPPORTUNISTIC:
        pod["priorityClassName"] = "opportunistic"
    return job(name, pod, hours, "gpu")


def sync_pod():
    return {"apiVersion": "v1", "kind": "Pod",
            "metadata": {"name": SITE["sync"], "namespace": NS, "labels": LABELS | {"role": "sync"}},
            "spec": {"restartPolicy": "Never", "activeDeadlineSeconds": 21600,
                     "affinity": affinity([CPU_ONLY, region()]),
                     "containers": [{"name": "main", "image": IMAGE, "command": ["sleep", "21000"],
                                     "resources": res(1, "2Gi", "10Gi"), "volumeMounts": mnts()}],
                     "volumes": vols()}}


def exec_sync(*cmd, inp=None):
    return kubectl("exec", "-i", SITE["sync"], "--", *cmd, inp=inp)


def push_code():
    """Code snapshot of HEAD -> /pvc/code/<sha12> (the directories jobs run from)."""
    code, buf = sha(), io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        for d in CODE_DIRS:
            t.add(os.path.join(REPO, d), arcname=d, filter=lambda x: None if "__pycache__" in x.name else x)
    exec_sync("sh", "-c", f"mkdir -p /pvc/code/{code} && tar -xzf - -C /pvc/code/{code} && echo {code} > /pvc/code/{code}/COMMIT",
              inp=buf.getvalue())
    print("pushed", code, "to", SITE["pvc"])


def ensure_code(code):
    """A job's code snapshot must be on the PVC; HEAD's is pushed when missing (a job failed staging on 3 Oct)."""
    if exec_sync("sh", "-c", f"test -d /pvc/code/{code} && echo yes || echo no").strip() != "yes":
        if code != sha():
            sys.exit(f"code snapshot {code} is not on {SITE['pvc']}; push it from a checkout of that commit")
        push_code()


def main():
    global SITE
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("rest", nargs="*")
    ap.add_argument("--site", default="west", choices=sorted(SITES))
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
    ap.add_argument("--exclude", action="append", default=[], help="pull: tar pattern to leave out (e.g. ckpt)")
    a, extra = ap.parse_known_args()
    if "--" in a.rest:                     # "... NAME -- script args": argparse keeps the separator
        i = a.rest.index("--")
        a.rest = a.rest[:i] + a.rest[i + 1:]
    extra = [x for x in extra if x != "--"]
    SITE = SITES[a.site]
    tag = "" if a.site == "west" else "c-"
    if a.cmd == "pvc":
        apply({"apiVersion": "v1", "kind": "PersistentVolumeClaim",
               "metadata": {"name": SITE["pvc"], "namespace": NS, "labels": LABELS},
               "spec": {"storageClassName": SITE["storage"], "accessModes": ["ReadWriteMany"],
                        "resources": {"requests": {"storage": "150Gi"}}}})
    elif a.cmd == "sync-up":
        apply(sync_pod())
        kubectl("wait", "--for=condition=Ready", f"pod/{SITE['sync']}", "--timeout=600s")
    elif a.cmd == "sync-down":
        print(kubectl("delete", "pod", SITE["sync"], "--wait=false", check=False))
    elif a.cmd == "push-code":
        push_code()
    elif a.cmd == "build-env":
        code = a.code or sha()
        apply(cpu_job(f"selrm-d-build-env-{a.rest[0]}", ["bash", f"/pvc/code/{code}/k8s/build_env_d.sh", a.rest[0]],
                      hours=2))
    elif a.cmd == "mirror-central":          # runs in us-central, reads the west PVCs once
        SITE = SITES["central"]
        code = a.code or sha()
        west = [{"name": "srcd", "persistentVolumeClaim": {"claimName": "selrm-d", "readOnly": True}},
                {"name": "srcb", "persistentVolumeClaim": {"claimName": "selrm-b", "readOnly": True}}]
        wm = [{"name": "srcd", "mountPath": "/src", "readOnly": True},
              {"name": "srcb", "mountPath": "/srcb", "readOnly": True}]
        apply(cpu_job(f"selrm-d-mirror-central-{int(time.time()) % 100000}",
                      ["sh", f"/src/code/{code}/k8s/mirror_central_d.sh", code], cpu=8, mem="64Gi", eph="80Gi",
                      hours=6, extra_vols=west, extra_mnts=wm))
    elif a.cmd == "gpu":
        name, args = a.rest[0], a.rest[1:] + extra
        models = a.models.split(",") if a.models is not None else ("/pvcb/selrm/models/unsloth--Qwen3.5-9B",)
        ensure_code(a.code or sha())
        apply(gpu_job(f"selrm-d-{tag}{name}-{int(time.time()) % 100000}", a.code or sha(), a.env, a.gpu, a.hours,
                      args, models=models, n_gpu=a.n_gpu, cpu=a.gpu_cpu, mem=a.gpu_mem))
    elif a.cmd == "cpu":        # a python (or .sh) script of the code snapshot, on a CPU node
        name, args, code = a.rest[0], a.rest[1:] + extra, a.code or sha()
        ensure_code(code)
        cmd = (f"set -e; cd /pvc/code/{code}; sh " + " ".join(args) if args[0].endswith(".sh") else
               f"set -e; tar -xf /pvc/env/selrm-d-env-{a.env}.tar -C /opt; cd /pvc/code/{code}; "
               "/opt/selrm-env/venv/bin/python -u " + " ".join(args))
        apply(cpu_job(f"selrm-d-{tag}{name}-{int(time.time()) % 100000}", ["sh", "-c", cmd], cpu=a.cpu, mem=a.mem,
                      hours=a.hours))
    elif a.cmd == "pull":
        remote, local = a.rest
        os.makedirs(local, exist_ok=True)
        # A raw tar stream of ~30 MB through kubectl exec was cut short on Windows (3 Oct): pack and checksum on
        # the pod, stream the gzip, compare the checksum, retry.
        tmp = f"/tmp/pull-{int(time.time())}.tgz"
        excl = " ".join(f"--exclude={e}" for e in a.exclude)
        want = exec_sync("sh", "-c", f"tar -czf {tmp} {excl} -C {os.path.dirname(remote)} {os.path.basename(remote)} && "
                                     f"sha256sum {tmp} | cut -d' ' -f1").strip()
        import hashlib
        for _ in range(5):
            data = subprocess.run(["kubectl", "-n", NS, "exec", SITE["sync"], "--", "cat", tmp], capture_output=True).stdout
            if hashlib.sha256(data).hexdigest() == want:
                break
        else:
            sys.exit(f"pull: checksum mismatch after 5 tries ({remote})")
        exec_sync("rm", "-f", tmp)
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as t:
            t.extractall(local)
        print("pulled", remote, "->", local, f"({len(data)} bytes gzip, sha256 ok)")
    elif a.cmd == "ls":
        print(exec_sync("sh", "-c", f"ls -la {a.rest[0] if a.rest else '/pvc'}"))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
