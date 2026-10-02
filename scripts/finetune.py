"""LoRA fine-tuning on a pre-tokenised corpus (ROLE.md: 1 epoch over the example
budget, effective batch 64, lr 1e-4 cosine, LoRA r=64, bf16, loss on the
response tokens only). Seeds set data order and LoRA initialisation.
  python scripts/finetune.py --root ROOT --spec SPEC.json
(the queue runner train_eval_job.py imports train() and keeps the model for eval)."""
import argparse, json, os, sys, time
import numpy as np
import torch
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Fixed for every run of an experiment; recorded in meta.json. per_device x accum = 64.
HP = {"lr": 1e-4, "batch": 64, "per_device": 16, "epochs": 1, "max_len": 1024, "lora_r": 64,
      "lora_alpha": 64, "lora_dropout": 0.0, "warmup_ratio": 0.03, "weight_decay": 0.0,
      "optim": "adamw_torch_fused", "max_grad_norm": 1.0, "save_every_s": 1200,
      "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]}


class TokDataset(torch.utils.data.Dataset):
    def __init__(self, path):
        z = np.load(path)
        self.ids, self.off, self.npr = z["ids"], z["off"], z["npr"]
        self.vocab = int(z["vocab"]) if "vocab" in z else None

    def __len__(self):
        return len(self.npr)

    def __getitem__(self, i):
        return {"input_ids": self.ids[self.off[i]:self.off[i + 1]], "npr": int(self.npr[i])}

    def tokens(self):
        return int(self.off[-1])


class PairDataset(TokDataset):
    """verdict_bt: item i = (correct-claim prompt, wrong-claim prompt) = sequences 2i, 2i+1."""

    def __len__(self):
        return len(self.npr) // 2

    def __getitem__(self, i):
        a, b = super().__getitem__(2 * i), super().__getitem__(2 * i + 1)
        return {"a": a["input_ids"], "b": b["input_ids"]}


class PairCollate:
    """Left padding so the last position is the answer position of every sequence;
    rows alternate correct / wrong."""

    def __init__(self, pad_id):
        self.pad = pad_id

    def __call__(self, batch):
        seqs = [s for b in batch for s in (b["a"], b["b"])]
        L = max(len(s) for s in seqs)
        ids = torch.full((len(seqs), L), self.pad, dtype=torch.long)
        att = torch.zeros((len(seqs), L), dtype=torch.long)
        for j, s in enumerate(seqs):
            ids[j, L - len(s):] = torch.from_numpy(s.astype(np.int64))
            att[j, L - len(s):] = 1
        return {"input_ids": ids, "attention_mask": att}


def last_hidden(model, ids, att):
    """Final (normed) hidden state at the last position, from the decoder without lm_head."""
    base = model.get_base_model() if hasattr(model, "get_base_model") else model
    out = base.model(input_ids=ids, attention_mask=att, use_cache=False)
    return out.last_hidden_state[:, -1, :]


def bt_trainer_cls():
    from transformers import Trainer
    import torch.nn.functional as F

    class BTTrainer(Trainer):
        """Bradley-Terry loss on the two claims: -log sigmoid(u(correct) - u(wrong)),
        u = h_last . (W[+] - W[-]) in fp32 (the same u the scorer reads)."""
        wdiff = None

        def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
            u = last_hidden(model, inputs["input_ids"], inputs["attention_mask"]).float() @ self.wdiff
            loss = -F.logsigmoid(u[0::2] - u[1::2]).mean()
            return (loss, None) if return_outputs else loss

    return BTTrainer


class Collate:
    """Right padding; labels = -100 on prompt and padding (loss on the response only)."""

    def __init__(self, pad_id):
        self.pad = pad_id

    def __call__(self, batch):
        L = max(len(b["input_ids"]) for b in batch)
        ids = torch.full((len(batch), L), self.pad, dtype=torch.long)
        lab = torch.full((len(batch), L), -100, dtype=torch.long)
        att = torch.zeros((len(batch), L), dtype=torch.long)
        for j, b in enumerate(batch):
            s = torch.from_numpy(b["input_ids"].astype(np.int64))
            ids[j, :len(s)], att[j, :len(s)] = s, 1
            lab[j, b["npr"]:len(s)] = s[b["npr"]:]
        return {"input_ids": ids, "attention_mask": att, "labels": lab}


def load_base(base_dir, max_len, hp=HP):
    """backend 'unsloth' (default) or 'hf' (plain transformers + PEFT: CPU self-test
    and fallback path; same LoRA and optimiser settings)."""
    if hp.get("backend", "unsloth") == "hf":
        from transformers import AutoConfig, AutoModelForCausalLM, AutoModelForImageTextToText, AutoTokenizer
        dt = torch.bfloat16 if hp.get("bf16", True) else torch.float32
        # the full qwen3_5 checkpoint must load as Qwen3_5ForConditionalGeneration (as Unsloth does), or
        # LoRA module paths (model.language_model.layers.N vs model.layers.N) differ from Unsloth adapters
        multimodal = getattr(AutoConfig.from_pretrained(base_dir), "vision_config", None) is not None
        cls = AutoModelForImageTextToText if multimodal else AutoModelForCausalLM
        model = cls.from_pretrained(base_dir, dtype=dt, local_files_only=True)
        return model.to("cuda" if torch.cuda.is_available() else "cpu"), AutoTokenizer.from_pretrained(base_dir)
    from unsloth import FastLanguageModel
    # Unsloth's Qwen3.5 guide flags for 16-bit LoRA; qwen3_5 is routed to FastModel (VLM path)
    model, tok = FastLanguageModel.from_pretrained(base_dir, max_seq_length=max_len, dtype=None,
                                                   load_in_4bit=False, load_in_16bit=True,
                                                   full_finetuning=False, local_files_only=True)
    tok = getattr(tok, "tokenizer", tok)     # FastModel returns a processor for VLM checkpoints
    preflight()
    return model, tok


def preflight():
    """Fail fast instead of silently training on the slow torch Gated DeltaNet path."""
    import transformers.models.qwen3_5.modeling_qwen3_5 as mq
    fast = {n: getattr(mq, n, None) is not None for n in
            ("causal_conv1d_fn", "causal_conv1d_update", "chunk_gated_delta_rule", "fused_recurrent_gated_delta_rule")}
    if not all(fast.values()):
        raise RuntimeError(f"Qwen3.5 fast path incomplete: {fast}")
    from causal_conv1d import causal_conv1d_fn
    x = torch.randn(2, 64, 16, device="cuda", dtype=torch.bfloat16)
    causal_conv1d_fn(x, torch.randn(64, 4, device="cuda", dtype=torch.bfloat16), None, activation="silu")
    torch.cuda.synchronize()
    return fast


def add_lora(model, seed, hp=HP):
    if hp.get("backend", "unsloth") == "hf":
        from peft import LoraConfig, get_peft_model
        torch.manual_seed(seed)
        return get_peft_model(model, LoraConfig(r=hp["lora_r"], lora_alpha=hp["lora_alpha"],
                                                lora_dropout=hp["lora_dropout"], bias="none",
                                                target_modules=hp["target_modules"], task_type="CAUSAL_LM"))
    from unsloth import FastLanguageModel
    model = FastLanguageModel.get_peft_model(model, r=hp["lora_r"], lora_alpha=hp["lora_alpha"],
                                             lora_dropout=hp["lora_dropout"], bias="none",
                                             target_modules=hp["target_modules"],
                                             use_gradient_checkpointing="unsloth", random_state=seed)
    lora = [n for n, _ in model.named_modules() if n.endswith("lora_A")]
    assert lora and not any(".visual." in n for n in lora), "LoRA must cover language-model modules only"
    return model


def for_inference(model, hp=HP):
    model.eval()
    if hp.get("backend", "unsloth") != "hf":
        from unsloth import FastLanguageModel
        FastLanguageModel.for_inference(model)
    return model


def load_for_eval(base_dir, adapter_dir=None, max_len=2048, hp=HP):
    model, tok = load_base(base_dir, max_len, hp)
    if adapter_dir:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, adapter_dir)
    return for_inference(model, hp), tok


def train(spec, paths, log=print, hp=HP):
    """spec: run spec from the queue; paths: dict(base, data, ckpt, adapter).
    -> (model, tok, info) with the trained LoRA model still on the GPU."""
    from transformers import Trainer, TrainerCallback, TrainingArguments
    hp = hp | spec.get("hp", {})
    seed = int(spec["seed"])
    torch.manual_seed(seed)
    model, tok = load_base(paths["base"], hp["max_len"], hp)
    done = f"{paths['adapter']}/TRAINED.json"
    # what the adapter was trained on; the micro-batch split may change (e.g. after an OOM) and still resume
    key = {"train_data": paths["data"], "base": os.path.basename(paths["base"]), "seed": seed,
           "max_steps": spec.get("max_steps"),
           "hp": {k: v for k, v in hp.items() if k not in ("save_every_s", "per_device", "workers")}}
    if os.path.exists(done):                       # a retry after training finished: evaluate only
        info = json.load(open(done))
        if info.get("key") == key:
            from peft import PeftModel
            log(f"adapter already trained for this spec ({done}); skipping training")
            return PeftModel.from_pretrained(model, paths["adapter"]), tok, info
        stale = f"{paths['adapter']}.stale-{int(time.time())}"
        log(f"adapter at {paths['adapter']} was trained for another spec; moved to {stale}")
        os.replace(paths["adapter"], stale)
    os.makedirs(paths["ckpt"], exist_ok=True)
    kfile = f"{paths['ckpt']}/KEY.json"
    if os.path.exists(kfile) and json.load(open(kfile)) != key:   # checkpoints of another spec
        import shutil
        for d in os.listdir(paths["ckpt"]):
            if d.startswith("checkpoint-"):
                shutil.rmtree(f"{paths['ckpt']}/{d}", ignore_errors=True)
    json.dump(key, open(kfile, "w"))
    model = add_lora(model, seed, hp)
    pairwise = spec["format"] == "verdict_bt"
    ds = PairDataset(paths["data"]) if pairwise else TokDataset(paths["data"])
    if ds.vocab is not None and ds.vocab != len(tok):
        raise RuntimeError(f"{paths['data']} was tokenised with vocab {ds.vocab}, model tokenizer has {len(tok)}")
    # pairs count two sequences: 64 sequences per optimizer step = 32 pairs
    per_device = hp["per_device"] // 2 if pairwise else hp["per_device"]
    acc = (hp["batch"] // 2 if pairwise else hp["batch"]) // per_device
    assert acc * per_device == (hp["batch"] // 2 if pairwise else hp["batch"])

    class TimedSave(TrainerCallback):
        last = time.time()
        step0 = 0

        def on_train_begin(self, args, state, control, **kw):
            self.step0 = state.global_step

        def on_step_end(self, args, state, control, **kw):
            if time.time() - self.last > hp["save_every_s"]:
                control.should_save, self.last = True, time.time()

        def on_log(self, args, state, control, logs=None, **kw):
            if logs:
                log(f"step {state.global_step}/{state.max_steps} " + " ".join(
                    f"{k}={v:.4g}" if isinstance(v, float) else f"{k}={v}" for k, v in logs.items()))

    total = spec.get("max_steps") or -(-len(ds) // (hp["batch"] // 2 if pairwise else hp["batch"])) * hp["epochs"]
    args = TrainingArguments(
        output_dir=paths["ckpt"], per_device_train_batch_size=per_device,
        gradient_accumulation_steps=acc, learning_rate=hp["lr"], lr_scheduler_type="cosine",
        warmup_steps=round(hp["warmup_ratio"] * total), weight_decay=hp["weight_decay"], optim=hp["optim"],
        max_grad_norm=hp["max_grad_norm"], num_train_epochs=hp["epochs"],
        max_steps=spec.get("max_steps") or -1, bf16=hp.get("bf16", True), logging_steps=10, save_strategy="no",
        # unsloth checkpoints activations itself; the plain fallback needs torch checkpointing on a GPU
        gradient_checkpointing=hp.get("backend", "unsloth") == "hf" and torch.cuda.is_available(),
        gradient_checkpointing_kwargs={"use_reentrant": False},
        save_total_limit=1, seed=seed, data_seed=seed, report_to=[], dataloader_num_workers=hp.get("workers", 2),
        dataloader_pin_memory=True, remove_unused_columns=False, disable_tqdm=True)
    cb = TimedSave()
    if pairwise:
        cls = bt_trainer_cls()
        head = model.get_output_embeddings()
        cls.wdiff = (head.weight[tok.convert_tokens_to_ids("+")] - head.weight[tok.convert_tokens_to_ids("-")]).detach().float()
        trainer = cls(model=model, args=args, train_dataset=ds, data_collator=PairCollate(tok.pad_token_id), callbacks=[cb])
    else:
        trainer = Trainer(model=model, args=args, train_dataset=ds, data_collator=Collate(tok.pad_token_id),
                          callbacks=[cb])
    if hp.get("backend", "unsloth") == "hf":
        # transformers 5.0-5.5 scales the loss by 1/accumulation twice through accelerate's
        # GradientAccumulationPlugin; unsloth patches this, the plain path must clamp it
        trainer.accelerator.gradient_accumulation_steps = 1
    # resume from the newest COMPLETE checkpoint (trainer_state.json is written last); drop partial ones
    import shutil
    ck = sorted((d for d in os.listdir(paths["ckpt"]) if d.startswith("checkpoint-")),
                key=lambda d: int(d.split("-")[1]))
    good = [d for d in ck if os.path.exists(f"{paths['ckpt']}/{d}/trainer_state.json")]
    for d in ck:
        if d not in good[-1:]:
            shutil.rmtree(f"{paths['ckpt']}/{d}", ignore_errors=True)
    resume = f"{paths['ckpt']}/{good[-1]}" if good else None
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    t0 = time.time()
    out = trainer.train(resume_from_checkpoint=resume)
    secs = time.time() - t0
    steps = trainer.state.global_step
    n_now = steps - cb.step0                      # optimizer steps done in this attempt
    info = {"key": key, "train_seconds": round(secs, 1), "steps": steps, "steps_this_attempt": n_now,
            "resumed_from": resume, "examples": len(ds),
            # HF sums this attempt's losses but divides by all steps: rescale to this attempt
            "train_loss": out.training_loss * steps / max(1, n_now),
            "tokens": ds.tokens(), "tokens_per_s": round(ds.tokens() / max(1, len(ds)) * (hp["batch"] // 2 if pairwise else hp["batch"]) * n_now / secs, 1) if secs else None,
            "s_per_step": round(secs / max(1, n_now), 3),
            "peak_mem_gb": round(torch.cuda.max_memory_reserved() / 2**30, 2) if torch.cuda.is_available() else None,
            "peak_mem_allocated_gb": round(torch.cuda.max_memory_allocated() / 2**30, 2) if torch.cuda.is_available() else None,
            "trainable_params": sum(p.numel() for p in model.parameters() if p.requires_grad),
            "lora_modules": sum(1 for n, _ in model.named_modules() if n.endswith("lora_A")),
            "dtype": str(model.get_input_embeddings().weight.dtype),
            "hp": hp, "grad_accum": acc}
    model.save_pretrained(paths["adapter"])
    json.dump(info, open(done, "w"), indent=1)
    for d in os.listdir(paths["ckpt"]):            # optimizer checkpoints are no longer needed
        if d.startswith("checkpoint-"):
            import shutil
            shutil.rmtree(f"{paths['ckpt']}/{d}", ignore_errors=True)
    log(f"trained {steps} steps in {secs/60:.1f} min, {info['tokens_per_s']} tok/s, peak {info['peak_mem_gb']} GB")
    return model, tok, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--spec", required=True, help="JSON file with one run spec")
    a = ap.parse_args()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import train_eval_job as J
    spec = json.load(open(a.spec))
    model, tok, info = train(spec, J.paths(a.root, spec))
    print(json.dumps({k: v for k, v in info.items() if k != "hp"}, indent=1))


if __name__ == "__main__":
    main()
