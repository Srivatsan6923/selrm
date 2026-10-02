# Running on Google Colab with Unsloth

## Workflow (Colab or SSH; same scripts)
- Code lives in a private GitHub repo. Claude Code writes and tests code
  (laptop or Colab terminal); Colab notebooks `git pull` and run `scripts/`.
- Notebooks are thin: setup, then one `!python scripts/...` call per step.
  Logic never lives only in a notebook.
- All persistent state on Drive: `/content/drive/MyDrive/selrm/{data,cache,
  ckpt,results,logs}`. The Colab VM disk is wiped on disconnect.

## Runtimes
| Job | Runtime |
|---|---|
| Data generation, API audits (E1-E3, E5 via API) | CPU runtime (no GPU units spent) |
| Fine-tuning | RTX PRO 6000 96 GB (measured) or A100; smaller cards only for smoke tests |
| Local model eval, reranking, policy sampling | L4 or A100 |
| T4 | Avoid except for tiny smoke tests |

## Rules that save the week
1. **Timing test first**: train 200 steps of one E4 config, log tokens/s and
   peak memory; extrapolate per-run hours into docs/RUN_MATRIX.csv before
   queueing anything.
2. **Resumable everything**: `save_steps` every ~20 minutes of training to
   Drive, `resume_from_checkpoint=True`; API runs append to a JSONL cache and
   skip keys already done.
3. **One run per session** for long jobs; write `results/<run_id>/DONE` when
   finished so the matrix can be updated automatically.
4. **Pin versions**: record `pip freeze`, GPU name, Unsloth/TRL/transformers
   versions, model ID and revision hash in each run's `meta.json`.
5. **Seeds**: data seed, LoRA init seed and data-order seed all set from the
   run's seed column.
6. Never store API keys in notebooks; use Colab Secrets (`userdata.get`).

## Unsloth notes (verify against current Unsloth docs before coding)
- Load with `FastLanguageModel.from_pretrained(...)`, add LoRA with
  `FastLanguageModel.get_peft_model(...)`, train with TRL `SFTTrainer`,
  mask prompts (train on responses only). APIs change; check the docs and
  pin the version that works.
- Model IDs: `unsloth/Qwen3.5-9B` is the backbone (verified 2 Oct, see
  docs/MEASURED_FACTS.md). Verify any other ID before use. Do not guess IDs.
- Use bf16 LoRA on A100; 4-bit loading only if memory forces it, and then use
  it for every run of that experiment so runs stay comparable.
- For log-prob scoring use a plain forward pass (no sampling); batch it.
- For reader generation use greedy decoding with a fixed max length.

## API models (E1-E3, E5)
- One OpenAI-compatible client (`base_url` + key from Colab Secrets):
  OpenRouter, Z.ai, Moonshot, NVIDIA, or a local vLLM server.
- Confirm exact model IDs for Kimi K3, GLM-5.3, Nemotron 3 Ultra/Super and
  the current closed flagships from the provider pages; record ID, provider
  and access date in configs/models.json.
- Fix reasoning effort per model and record it. Print a token/cost estimate
  before every run; run the 300-triplet pilot before the full set.

## Shared Drive for four people
- One shared Google Drive folder `selrm/`, shared with all four accounts.
  Each person adds a shortcut to it in their own My Drive so it mounts at
  `/content/drive/MyDrive/selrm`. Confirm you can read a file another person
  wrote before relying on it.
- Drive sync between accounts can lag by minutes. Claim files and DONE files
  are tiny; write them first, wait 60 seconds, re-check for a competing
  claim, then start.
- Space: adapters are deleted after evaluation unless listed in
  `configs/keep_adapters.json`. Keep `scores_*.jsonl` (small) for every run.
- If Drive is unavailable to someone, results (JSON only) may be pushed to
  the repo under `results_git/<run_id>/` as a fallback.
