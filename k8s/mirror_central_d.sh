#!/bin/sh
# Lay out D's central PVC (selrm-d-central, us-central CephFS) like the two west PVCs, so GPU jobs in
# us-central read only local storage: /pvc has D's paths and, mounted again read-only as /pvcb, B's paths.
# Weights come from Hugging Face at the pinned revisions; the two kept adapters are copied (0.5 GB each)
# and merged here with the same script and environment as in the west; the central merged copies are
# validated against B's scores before use, like the west ones.
# Usage (CPU Job in us-central; /src = west selrm-d read-only, /srcb = west selrm-b read-only,
# /pvc = central read-write):  sh mirror_central_d.sh <code_sha>
set -eu
CODE=$1
mkdir -p /pvc/env /pvc/code /pvc/merged /pvc/models /pvc/selrm/models /pvc/selrm/adapters \
         /pvc/selrm/data/rule_v1/test_L2 /pvc/selrm/results/B-F-ledger2-triplets-s0
for t in v1 v2; do
  [ -f /pvc/env/selrm-d-env-$t.tar.gz ] || cp /src/env/selrm-d-env-$t.tar.gz /pvc/env/
done
cp -rn /src/code/. /pvc/code/
[ -f /pvc/selrm/data/rule_v1/test_L2/records.jsonl ] || \
  cp /srcb/selrm/data/rule_v1/test_L2/records.jsonl /pvc/selrm/data/rule_v1/test_L2/
f="/pvc/selrm/results/B-F-ledger2-triplets-s0/scores_rule_v1~test_L2.jsonl"
[ -f "$f" ] || cp "/srcb/selrm/results/B-F-ledger2-triplets-s0/scores_rule_v1~test_L2.jsonl" "$f"
for r in B-F-ledger2-triplets-s0 B-F-ledger2-blocks-s0; do
  [ -d /pvc/selrm/adapters/$r ] || cp -r /srcb/selrm/adapters/$r /pvc/selrm/adapters/
done
echo "copied from the west PVCs"
tar -xzf /pvc/env/selrm-d-env-v1.tar.gz -C /opt
PY=/opt/selrm-env/venv/bin/python
cd /pvc/code/$CODE
$PY scripts/download_model.py unsloth/Qwen3.5-9B 005429cee5cb648998cf2b70eebdd83175989c9a \
    /pvc/selrm/models/unsloth--Qwen3.5-9B
$PY scripts/download_model.py dmis-lab/llama-3.1-medprm-reward-v1.0 6948b9e942fa0275dff8ff902a1833f1298974d4 \
    /pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0
for r in B-F-ledger2-triplets-s0 B-F-ledger2-blocks-s0; do
  $PY scripts/merge_adapter.py --base /pvc/selrm/models/unsloth--Qwen3.5-9B --adapter /pvc/selrm/adapters/$r \
      --out /pvc/merged/$r
done
echo "MIRROR OK"
