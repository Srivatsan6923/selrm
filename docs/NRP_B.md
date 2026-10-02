# Role B on NRP Nautilus: setup a new session can resume from

Cluster access: kubeconfig context `nautilus` (OIDC), namespace **ecepxie** (shared with other
users; touch only objects labelled `app=selrm-b` / named `selrm-b-*`). Laptop tools: kubectl,
git, python (no GPU needed locally). Policy pages read 2 Oct 2026 (policies, gpu-pods, jobs,
storage); the rules below follow them and the portal source (prp/k8s_portal).

## Rules that shape everything (do not relax)
- A pod is "violating" if GPU util < 40% of requested GPUs (1-day mean; startup counts), CPU
  median outside 20-200% of request (if request > 1 core), RSS median outside 20-150% of request
  (if request > 2 GiB). More than 4 violating pods blocks new Jobs. GPU idle < 40% over 3 h ->
  warning email; over 6 h -> admin deletes the whole Job and records a strike; 3 strikes = account
  flagged. Pods are judged after 30 min.
- Jobs must end by themselves; never `sleep`, `while true`, `tail -f`, `infinity`, `bash ... -i`
  in Job command/args/env (scanner). Sleep only in bare interactive pods (<= 6 h, 2 GPUs).
- Requests == limits (Guaranteed QoS; also required above ~100 Jobs). <= 400 Jobs at once.
- **No pip/conda/venv on CephFS.** The env lives on the PVC only as one tarball.
- `kubectl cp`/exec streams only for small files (code ~0.2 MB, results JSON); bulk data is
  generated or downloaded inside the cluster.
- GPU types: A100 = `nvidia.com/a100` (namespace quota 9; 80 GB SXM4/PCIe and 40 GB PCIe),
  A40 = `nvidia.com/a40`, RTX A6000 = `nvidia.com/rtxa6000`, L40/L40S = `nvidia.com/gpu` +
  affinity on `nvidia.com/gpu.product`. H100/H200 only as `priorityClassName: opportunistic`.
  Never tolerate reservation/system/issue taints.

## Image and environment
- Image (all pods): `nvcr.io/nvidia/cuda:13.0.3-cudnn-devel-ubuntu24.04` (public NGC, no Docker
  Hub limits; has gcc for Triton, nvcc 13.0.88, tar; no python/curl/git/zstd).
- Env tarball `/pvc/selrm/env/selrm-env-<tag>.tar` built by CPU Job `k8s/build_env.sh <tag>`:
  uv 0.12.22, CPython 3.12 (uv-managed) + venv at `/opt/selrm-env` (same path in every pod),
  torch 2.11.0+cu130, torchvision 0.26.0+cu130, unsloth 2026.9.14, unsloth_zoo 2026.9.9,
  transformers 5.5.0, trl 0.24.0, datasets 4.3.0, flash-linear-attention/fla-core 0.5.2,
  causal-conv1d 1.7.0 compiled for sm 8.0/8.6/8.9/9.0. Freeze: `selrm-env-<tag>.freeze.txt`.
- Node guard: `nvidia.com/cuda.driver.major Gt 579` (cu130 needs driver >= 580; all GPU nodes
  had 580+ on 2 Oct).

## PVC layout (`selrm-b`, rook-cephfs = US West CephFS, RWX, 200 Gi)
```
/pvc/selrm/code/<sha12>/        code snapshots (selrm, scripts, k8s, configs, tests + COMMIT)
/pvc/selrm/env/                 selrm-env-<tag>.tar + .freeze.txt
/pvc/selrm/models/<id-->/       pinned HF snapshots + REVISION (configs/models_b.json)
/pvc/selrm/data/<set>/<name>.jsonl  datasets (smoke_v2 rebuilt in-cluster, hashes checked)
/pvc/selrm/data/REGISTRY.json + data/<set>/<name>/records.jsonl   A's frozen sets (rebuilt in-cluster, sha256 checked)
/pvc/selrm/tok/<base>/train/<key>/       pre-tokenised corpora (train.npz, stats.json, READY); key has format,
                                         corpus, n, p, construction seed, max_len, formats.VERSION
/pvc/selrm/tok/<base>/eval/<set>/<kind>.npz   pre-tokenised eval prompts (kind verdict|rationale|reader_*)
/pvc/selrm/queue/<name>.json    queue files (run specs)
/pvc/selrm/results/<run_id>/    CLAIMED_B, HEARTBEAT, DONE/FAILED_n/KILLED_n, meta.json, summary_*, scores_*, gpu_util.csv, run.log
/pvc/selrm/ckpt/<run_id>/       trainer checkpoints (deleted after the run) + adapter of non-kept runs
/pvc/selrm/adapters/<run_id>/   kept adapters (configs/keep_adapters.json)
/pvc/selrm/logs/<pod>/          runner.log, gpu_util.csv per pod
```
Each file has one writer (per-run or per-pod paths); pods never write shared files.

## Pods and Jobs (all built by `scripts/submit_b.py`)
- `selrm-b-sync`: bare CPU pod (1 CPU, 1 Gi, `sleep 3000`, deadline 1 h) for code/queue pushes
  and result pulls; delete after use (`sync-down`).
- CPU Jobs (`build-env`, `prep`): off GPU nodes (`pci-10de.present NotIn true`), us-west.
  `prep` = rebuild smoke_v2 + hash check (configs/smoke_v2_sha256.json), download pinned
  weights, pre-tokenise the queue (`scripts/pretok.py`).
- GPU runner Jobs: one GPU each; init container `k8s/stage.sh` unpacks env + code + weights to
  local NVMe (emptyDirs); main container runs `scripts/train_eval_job.py --queue ... --max_runs K`
  (claim -> train -> eval -> results -> DONE -> next; exits when nothing is claimable).
  cpu 2, memory 12 Gi (measured: 1.0 core, RSS 2.9 GiB; the 19 GiB working set is page cache and is
  not judged), ephemeral 64 Gi, /dev/shm 4 Gi, backoffLimit 2, TTL 3 days, activeDeadlineSeconds =
  `--hours`. Exit codes: 3 watchdog (GPU < 5% for 10 min after 15 min grace; run gets FAILED_n),
  4 env preflight failed (no run charged), 5 previous model still on the GPU after gc (no run
  charged), 2 CUDA error inside a run. GPU monitor thread: nvidia-smi every 30 s ->
  results/<run>/gpu_util.csv, heartbeat; claim stale after 15 min without heartbeat/claim update
  (own) or 3 h (other roles); a taken-over own claim writes KILLED_n (run failed at 3).
- Resetting a run = delete results/<rid>, ckpt/<rid> and adapters/<rid> (adapters of another spec
  are moved aside as <dir>.stale-<ts>, never deleted automatically).

## Commands (laptop, repo root)
```
python scripts/submit_b.py sync-up && python scripts/submit_b.py push-code    # after git commit
python scripts/make_queue_b.py smoke configs/queues/b_smoke.json
python scripts/submit_b.py push-queue configs/queues/b_smoke.json
python scripts/submit_b.py build-env v1                    # once per env tag
python scripts/submit_b.py prep b_smoke.json --code <sha>  # CPU; wait for "PREP OK"
python scripts/submit_b.py runners b_smoke.json --n 3 --gpu a100 --max-runs 3 --hours 4
python scripts/submit_b.py ls                              # run states on the PVC
python scripts/submit_b.py pull                            # finished runs -> results_git/
python scripts/nrp_status_b.py                             # Thanos: GPU 1h/3h/6h/1d, CPU, RSS vs requests
python scripts/submit_b.py sync-down
kubectl -n ecepxie get pods -l app=selrm-b -o wide ; kubectl -n ecepxie logs -f <pod> [-c stage]
```
Monitoring every block: `scripts/nrp_status_b.py` (same formulas as the portal), Grafana
https://grafana.nrp-nautilus.io/d/dRG9q0Ymz/k8s-compute-resources-namespace-gpus?var-namespace=ecepxie
(anonymous), Violations card at https://nrp.ai/userinfo (needs the user's login).
