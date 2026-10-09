# Token and GPU estimates for the remaining work (3 Oct 2026)

Estimates, not measurements. Basis: set sizes on the status board, about
450 input tokens per rule-tier judgment (longer notes included), the
two-order choice format for API models (2 calls per case), and the measured
run times (verdict about 2.2 GPU-hours, two-stage about 2.8, with full
evaluation). Replace them with the first measured batch.

## A. API tokens per model (OpenRouter)
"Out (plain)" assumes a short answer; "out (reasoning)" assumes about 150
hidden reasoning tokens per call at the lowest setting. Check each model's
actual reasoning use on 100 calls first.

| Job | Calls | Input | Out (plain) | Out (reasoning) |
|---|---|---|---|---|
| L2 triplets, 1,000 (base, flip, near, presentation, missing) | 10,000 | 4.5M | 0.06M | 1.5M |
| xr_v1, 400 items | 4,800 | 1.7M | 0.03M | 0.7M |
| MedEinst, 1,000 pairs | 4,000 | 2.0M | 0.02M | 0.6M |
| Key pairs, 582 pairs | 2,300 | 0.9M | 0.01M | 0.35M |
| TrialGPT, 759 items | 1,500 | 0.85M | 0.01M | 0.25M |
| **Audit per model** | **22,600** | **10M** | **0.15M** | **3.4M** |
| + prompted two-stage on L2 (reader + judge) | 15,000 | 4.8M | 0.45M | 2.7M |

Models: three closed flagships, Kimi K3, Llama-3.3-70B; optional GLM-5.3,
Nemotron 3, Qwen3.5-27B. Each costs one "audit per model" row (plus the
two-stage row if run).

One closed judge only:
| Job | Calls | Input | Output |
|---|---|---|---|
| Reference rows and rule ladder (300 triplets per level) | 15,000 | 6.8M | 0.1M-2.3M |
| Extraction for the extraction + program row | 5,000 | 2.3M | 0.5M |
| Table 5 closed-judge row, full (MedQA, CareQA, key pairs, MedEinst; 16 traces each) | 64,000 | 45M | 0.4M-10M |
| Table 5 closed-judge row, subsampled (500 MedQA questions) | 8,000 | 5.6M | 0.05M-1.2M |

Rewriting (cheap open models):
| Job | Calls | Input | Output |
|---|---|---|---|
| rewrite_v1 test: rewriter | 4,000 | 1.2M | 1.0M |
| rewrite_v1 test: two extractors | 8,000 | 2.8M | 1.0M |
| Training-side rewrites: rewriter | 7,000 | 2.1M | 1.8M |
| Training-side rewrites: two extractors | 14,000 | 4.9M | 1.7M |

Cost = input tokens x input price + output tokens x output price, per
model. Totals to plug prices into:
- three closed flagships, audit only: 30M input, 0.5M-10M output;
- one closed judge, extras with the subsampled Table 5 row: about 15M
  input, 0.7M-4M output (55M input with the full Table 5 row);
- each open model through the API: 10M-15M input, 0.2M-6M output;
- rewriting: about 11M input, 5.5M output.

## B. GPU hours (80 GB-class card; a 24-48 GB card runs the 9B jobs slower)
| Owner | Job | Runs | GPU-hours |
|---|---|---|---|
| B | Case-visible judge variants | 7 | 20 |
| B | Auxiliary grid: NLI4CT 12, MedEinst 15, TrialGPT 20 short runs | 47 | 45 |
| B | Leave-one-kind-out seeds and decision-bit runs | 15 | 30 |
| B | Training with rewritten notes | 4 | 10 |
| B | Remaining v10 rows (4B cells, clinical-pairs ledger, GenPRM-style, folds) | 10 | 28 |
| B | Scoring kept adapters on new sets | - | 10 |
| C | Zero-shot external scoring of new systems; baselines on new sets | - | 15 |
| C | ThinkPRM and GenPRM audit parts | 2 | 24 |
| C | 27B and 70B judges locally (0 if done through the API) | 2 | 10 |
| C | Trial-level eligibility (optional) | - | 8 |
| D | Policy training: 3 running + summary reward + 4 seed-1 runs | 8 | 46 |
| D | Scoring policies on held-out rules, xr_v1, ec_v1, TrialGPT | 9 | 9 |
| | **Total** | | **about 255** |

Rent cost = GPU-hours x hourly rate. Wall-clock to the run freeze
(Wed 7 Oct 23:59 UTC) is about 96 hours, so 255 GPU-hours needs three GPUs
running continuously; plan for four to six to absorb failures and queues.
Dropping the optional rows and the remaining v10 rows saves about 45 hours.
