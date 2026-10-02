# Measured facts (2 Oct, teammate's Colab notebook)

- GPU: NVIDIA RTX PRO 6000 Blackwell, 96 GB. torch 2.11.0+cu130,
  unsloth 2026.9.14, transformers 5.5.0, trl 0.24.0, datasets 4.3.0.
- Verified Unsloth IDs: Qwen3.5-0.8B, -2B, -4B, -9B, -27B (and -Base
  variants); list in `configs/qwen35_lookup.json`.
- Qwen3.5-9B bf16: 18.8 GB loaded; LoRA r=64 on attention+MLP: 116M
  trainable parameters.
- Training: batch 64, max length 1024, lr 1e-4 cosine: about 0.44 steps/s.
  18k examples x 2 epochs = about 21 minutes. Loss reaches ~0 by step 60 on
  in-distribution data -> 1 epoch is enough; watch for memorisation.
- `SFTConfig(completion_only_loss=True)` with prompt/completion columns
  works; `group_by_length` is ignored by this version.
- Chat template: `apply_chat_template(..., enable_thinking=False)` ends with
  `<think>\n\n</think>\n\n`; "+" and "-" are single tokens.
- flash-linear-attention installs; causal-conv1d build was cancelled. Both
  must be installed BEFORE loading the model, then restart the runtime;
  otherwise the slow torch path is used.
- Zero-shot Qwen3.5-9B on an in-distribution smoke dev set (278 triplets):
  Rev 82.0, Hold 85.3, TA 70.9; numeric near-miss Hold 63.2. After training
  on triplets: 100/100/100 on the same in-distribution dev. Neither number is
  reportable: dev shared 176 of 178 line templates with training.
- Numeric near-misses in that run included values exactly at the threshold;
  report those as the separate kind `boundary`.
