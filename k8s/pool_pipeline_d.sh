#!/bin/sh
# One GPU pod per pool (role D, D-POOL-* and the scores behind D-CAL / D-SEL-*): generate the
# candidate pool, then score every trace with each scorer, one process after another so each
# model leaves the GPU before the next loads. Every step is skipped when its output exists,
# so a re-run resumes. Usage (GPU Job, code dir as working dir):
#   sh k8s/pool_pipeline_d.sh <pool> <tp> [scorers...]
# scorers: medprm medprm-swap ledger2-triplets ledger2-triplets-swap ledger2-blocks (default: all)
set -eu
POOL=$1; TP=$2; shift 2
SCORERS=${*:-"medprm medprm-swap ledger2-triplets ledger2-triplets-swap ledger2-blocks"}
PY=/opt/selrm-env/venv/bin/python
POOLS=/pvc/pools; OUT=/pvc/scores/$POOL
MEDPRM=/pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0
mkdir -p "$OUT"
$PY -u scripts/make_pool.py --pool "$POOL" --out $POOLS --model /work/models/unsloth--Qwen3.5-9B --tp "$TP"
for s in $SCORERS; do
  f=$OUT/$s.jsonl
  [ -f "$f.meta.json" ] && { echo "exists: $f"; continue; }
  case $s in
    medprm)       $PY -u scripts/score_pool.py medprm --pool $POOLS/$POOL --model $MEDPRM --out "$f.tmp" ;;
    medprm-swap)  $PY -u scripts/score_pool.py medprm --pool $POOLS/$POOL --model $MEDPRM --out "$f.tmp" --swap ;;
    ledger2-triplets)      $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-triplets-s0 --tp "$TP" --out "$f.tmp" ;;
    ledger2-triplets-swap) $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-triplets-s0 --tp "$TP" --out "$f.tmp" --swap ;;
    ledger2-blocks)        $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-blocks-s0 --tp "$TP" --out "$f.tmp" ;;
    *) echo "unknown scorer $s"; exit 2 ;;
  esac
  mv "$f.tmp" "$f"; mv "$f.tmp.meta.json" "$f.meta.json"
  echo "scored $s"
done
echo "PIPELINE DONE $POOL"
