#!/bin/sh
# One GPU pod per pool (role D, D-POOL-* and the scores behind D-CAL / D-SEL-*): generate the
# candidate pool, then score every trace with each scorer, one process after another so each
# model leaves the GPU before the next loads. Every step is skipped when its output exists,
# so a re-run resumes. Usage (GPU Job, code dir as working dir):
#   sh k8s/pool_pipeline_d.sh <pool> <tp> [--ext] [scorers...]
# scorers: medprm medprm-swap ledger2-triplets ledger2-triplets-swap ledger2-blocks (default: all)
# With --ext after <tp>: extend the pool by samples 16-63 for its subset (medqa_kp: 150 whole key pairs)
# and score only those (outputs <scorer>.ext.jsonl).
set -eu
POOL=$1; TP=$2; shift 2
EXT=0
if [ "${1:-}" = "--ext" ]; then EXT=1; shift; fi
SCORERS=${*:-"medprm medprm-swap ledger2-triplets ledger2-triplets-swap ledger2-blocks"}
PY=/opt/selrm-env/venv/bin/python
POOLS=/pvc/pools; OUT=/pvc/scores/$POOL
MEDPRM=/pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0
mkdir -p "$OUT"
MODEL=/pvcb/selrm/models/unsloth--Qwen3.5-9B
[ -d "$MODEL" ] || MODEL=/pvc/selrm/models/unsloth--Qwen3.5-9B     # central site: B's files under /pvc/selrm
if [ "$EXT" = 1 ]; then
  $PY -u scripts/make_pool.py --pool "$POOL" --out $POOLS --model "$MODEL" --tp "$TP" --extend subset
  X="--ext"; SUF=".ext"
else
  $PY -u scripts/make_pool.py --pool "$POOL" --out $POOLS --model "$MODEL" --tp "$TP"
  X=""; SUF=""
fi
for s in $SCORERS; do
  f=$OUT/$s$SUF.jsonl
  [ -f "$f.meta.json" ] && { echo "exists: $f"; continue; }
  case $s in
    medprm)       $PY -u scripts/score_pool.py medprm --pool $POOLS/$POOL --model $MEDPRM --out "$f.tmp" $X ;;
    medprm-swap)  $PY -u scripts/score_pool.py medprm --pool $POOLS/$POOL --model $MEDPRM --out "$f.tmp" --swap $X ;;
    ledger2-triplets)      $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-triplets-s0 --tp "$TP" --out "$f.tmp" $X ;;
    ledger2-triplets-swap) $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-triplets-s0 --tp "$TP" --out "$f.tmp" --swap $X ;;
    ledger2-blocks)        $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-F-ledger2-blocks-s0 --tp "$TP" --out "$f.tmp" $X ;;
    ledger2-tripclin)      $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-TR-tripclin-s0 --tp "$TP" --out "$f.tmp" $X ;;
    ledger2-tripclin-swap) $PY -u scripts/score_pool.py ledger --pool $POOLS/$POOL --model /pvc/merged/B-TR-tripclin-s0 --tp "$TP" --out "$f.tmp" --swap $X ;;
    *) echo "unknown scorer $s"; exit 2 ;;
  esac
  mv "$f.tmp" "$f"; mv "$f.tmp.meta.json" "$f.meta.json"
  echo "scored $s"
done
echo "PIPELINE DONE $POOL"
