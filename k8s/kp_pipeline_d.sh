#!/bin/sh
# Key-pair pool medqa_kp (Table 5 Key column, Fig. 3 right): 16 samples per question scored by every
# scorer, then samples 16-63 scored by the two scorers the selection-pressure curve needs.
# Usage (GPU Job, code dir as working dir): sh k8s/kp_pipeline_d.sh <tp>
set -eu
sh k8s/pool_pipeline_d.sh medqa_kp "$1"
sh k8s/pool_pipeline_d.sh medqa_kp "$1" --ext medprm ledger2-triplets
