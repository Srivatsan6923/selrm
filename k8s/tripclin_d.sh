#!/bin/sh
# Table 5 with the clinical-pairs ledger model (DECISIONS_D 3 Oct): merge B-TR-tripclin-s0 into the base weights,
# validate the merged vLLM path against B's own test_L2 scores with the criteria fixed for the first validation
# (preference-sign agreement >= 99%, TA within 0.5 points, reader output identical for >= 90% of records), and only
# then score every pool with it (swapped vignettes on the test pools; the key-pair extension for Fig. 3 right).
# Every step is skipped when its output exists, so a re-run resumes.
# Usage (GPU Job, code dir as working dir): sh k8s/tripclin_d.sh <tp> [pools...]
set -eu
TP=$1; shift
POOLS=${*:-"medqa_dev medqa_test careqa_en medeinst_test medqa_kp"}
PY=/opt/selrm-env/venv/bin/python
R=B-TR-tripclin-s0
M=/pvc/merged/$R
V=/pvc/val/D-VAL-tripclin-s0
[ -f "$M/MERGED.json" ] || $PY -u scripts/merge_adapter.py --base /pvcb/selrm/models/unsloth--Qwen3.5-9B \
    --adapter /pvcb/selrm/adapters/$R --out $M
[ -f "$V/summary.json" ] || $PY -u scripts/score_pool.py validate --model $M --fmt ledger2 --tp "$TP" \
    --records /pvcb/selrm/data/rule_v1/test_L2/records.jsonl \
    --b-scores "/pvcb/selrm/results/$R/scores_rule_v1~test_L2.jsonl" --out $V
$PY - "$V/summary.json" <<'EOF'
import json, sys
s = json.load(open(sys.argv[1]))
ok = (s["preference_sign_agreement"] >= 0.99 and abs(s["vllm"]["TA"] - s["b"]["TA"]) <= 0.5
      and s["reader_output_identical"] / s["records"] >= 0.90)
print("validation", "PASSED" if ok else "FAILED", s["preference_sign_agreement"], s["vllm"]["TA"], s["b"]["TA"],
      s["reader_output_identical"] / s["records"], flush=True)
sys.exit(0 if ok else 3)
EOF
for p in $POOLS; do
  case $p in
    medqa_dev) sh k8s/pool_pipeline_d.sh $p "$TP" ledger2-tripclin ;;
    *) sh k8s/pool_pipeline_d.sh $p "$TP" ledger2-tripclin ledger2-tripclin-swap ;;
  esac
done
case " $POOLS " in *" medqa_kp "*) sh k8s/pool_pipeline_d.sh medqa_kp "$TP" --ext ledger2-tripclin ;; esac
echo "TRIPCLIN DONE"
