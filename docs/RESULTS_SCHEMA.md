# Results schema

```
results/<run_id>/
  meta.json            model ID + revision, provider, access date, reasoning
                       setting, format, corpus, seed, versions, GPU, git
                       commit, wall time, tokens, cost
  CLAIMED_<role>, HEARTBEAT, DONE
  scores_<set>.jsonl   {iid, u}  (+ reader_output for two-stage runs;
                       + raw, parsed, order for API choice calls)
  summary_<set>.json   selrm.metrics.summarise(...) + CIs (see below)
adapters/<run_id>/     only for runs in configs/keep_adapters.json
tables/*.tex, figures/*.pdf   written by scripts/make_tables.py
```

## summary_<set>.json
```
{ "run_id": ..., "set": ..., "claim_type": "conclusion",
  "all": {"Rev": x, "Hold": x, "TA": x, "PresHold": x, "BaseAcc": x,
          "Tie": x, "n": N},
  "nm_kind=numeric": {...}, "nm_kind=boundary": {...}, "tier=long": {...},
  "level=L2": {...}, "family=...": {...},
  "CI95": {"TA": [lo, hi], "Rev": [lo, hi], "Hold": [lo, hi]},
  "MR": x, "FR": x, "threshold": t,                (missing twins)
  "step": {"criterion": {...}, "applicability": {...},
           "CorrectRevision": x, "UnnecessaryRevision": x} }
```
Clinical sets: MedEinst `{"Reversal": x, "CI95": [...], "n_pairs": N,
"control_acc": x, "trap_acc": x}`; key pairs `{"Reversal": x, ...}`;
NLI4CT-P `{"macroF1": x, "faithfulness": x, "consistency": x}` from the task
scorer; selection `{"acc": x, "pair_acc": x, "swapped_acc": x, "N": n}`.

## Which runs feed which table
See docs/PAPER_CONTEXT.md section 4. Seeds are aggregated as mean and s.d.;
CIs are computed on pooled per-triplet outcomes with rules as the unit.
