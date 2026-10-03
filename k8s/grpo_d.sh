#!/bin/sh
# One policy-training run (D-RL-*; App. G "Policy training"): scripts/grpo_d.py on Qwen3.5-4B with LoRA.
# Usage (GPU Job, code dir as working dir; extra arguments go to grpo_d.py):
#   sh k8s/grpo_d.sh <reward> <run_id> [--seed K --steps N --overfit 64 ...]
# outcome, refgraph, stepcheck (Med-PRM next to the policy): one GPU. ledger2-blocks, ledger2-triplets: the
# merged ledger model is served by vLLM on the second GPU with the settings of scripts/score_pool.py (raw
# logits, 20 logprobs, vLLM's own generation defaults); the policy trains on the first.
# Output: /pvc/grpo/<run_id>/ (summary_rule_v1~test_L2.json, curve.jsonl, groups.jsonl, meta.json, DONE).
set -eu
R=$1; RUN=$2; shift 2
PY=/opt/selrm-env/venv/bin/python
OUT=/pvc/grpo/$RUN
mkdir -p "$OUT"
EXTRA=""
case " $* " in
  *" --eval-from "*)    # evaluation only (finished run): no reward model, no ledger server
    $PY -u scripts/grpo_d.py --reward "$R" --policy /pvcb/selrm/models/unsloth--Qwen3.5-4B --data /pvcb/selrm/data \
        --out "$OUT" "$@"
    echo "GRPO EVAL DONE $RUN"; exit 0 ;;
esac
[ -f "$OUT/DONE" ] && { echo "exists: $OUT"; exit 0; }
case $R in
  ledger2-blocks|ledger2-triplets)
    M=/pvc/merged/B-F-$R-s0
    # two GPUs: the server owns the second; one GPU (80-96 GB): the server takes 22% of it first and the
    # rollout engine 25% instead of 35% (memory only: same model, prompts and sampling)
    if [ "$(nvidia-smi -L | wc -l)" -ge 2 ]; then G=1; SM=0.9; else G=0; SM=0.22; EXTRA="--vllm-mem 0.25"; fi
    CUDA_VISIBLE_DEVICES=$G /opt/selrm-env/venv/bin/vllm serve "$M" --port 8001 --dtype bfloat16 --max-model-len 8192 \
        --logprobs-mode raw_logits --max-logprobs 20 --generation-config vllm --enable-prefix-caching --seed 0 \
        --gpu-memory-utilization $SM --limit-mm-per-prompt '{"image": 0, "video": 0}' > "$OUT/vllm_server.log" 2>&1 &
    n=0   # server start-up: poll its model list, at most 10 minutes
    until $PY -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8001/v1/models', timeout=5)" 2>/dev/null; do
      n=$((n + 1)); [ $n -gt 120 ] && { echo "ledger server did not start"; tail -20 "$OUT/vllm_server.log"; exit 1; }
      sleep 5
    done
    EXTRA="$EXTRA --ledger-url http://127.0.0.1:8001 --ledger-model $M"
    export CUDA_VISIBLE_DEVICES=0 ;;
  stepcheck) EXTRA="--medprm /pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0" ;;
esac
$PY -u scripts/grpo_d.py --reward "$R" --policy /pvcb/selrm/models/unsloth--Qwen3.5-4B --data /pvcb/selrm/data \
    --out "$OUT" $EXTRA "$@"
echo "GRPO DONE $RUN"
