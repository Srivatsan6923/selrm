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

    def __len__(self):
        return len(self.npr)

    def __getitem__(self, i):
        return {"input_ids": self.ids[self.off[i]:self.off[i + 1]], "npr": int(self.npr[i])}

    def tokens(self):
        return int(self.off[-1])


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
        from transformers import AutoModelForCausalLM, AutoTokenizer
        dt = torch.bfloat16 if hp.get("bf16", True) else torch.float32
        model = AutoModelForCausalLM.from_pretrained(base_dir, dtype=dt, local_files_only=True)
        return model.to("cuda" if torch.cuda.is_available() else "cpu"), AutoTokenizer.from_pretrained(base_dir)
    from unsloth import FastLanguageModel
    model, tok = FastLanguageModel.from_pretrained(base_dir, max_seq_length=max_len, dtype=torch.bfloat16,
                                                   load_in_4bit=False, load_in_8bit=False,
                                                   full_finetuning=False, local_files_only=True)
    return model, tok


def add_lora(model, seed, hp=HP):
    if hp.get("backend", "unsloth") == "hf":
        from peft import LoraConfig, get_peft_model
        torch.manual_seed(seed)
        return get_peft_model(model, LoraConfig(r=hp["lora_r"], lora_alpha=hp["lora_alpha"],
                                                lora_dropout=hp["lora_dropout"], bias="none",
                                                target_modules=hp["target_modules"], task_type="CAUSAL_LM"))
    from unsloth import FastLanguageModel
    return FastLanguageModel.get_peft_model(model, r=hp["lora_r"], lora_alpha=hp["lora_alpha"],
                                            lora_dropout=hp["lora_dropout"], bias="none",
                                            target_modules=hp["target_modules"],
                                            use_gradient_checkpointing="unsloth", random_state=seed)


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
    if os.path.exists(done):                       # a retry after training finished: evaluate only
        from peft import PeftModel
        log(f"adapter already trained ({done}); skipping training")
        return PeftModel.from_pretrained(model, paths["adapter"]), tok, json.load(open(done))
    model = add_lora(model, seed, hp)
    ds = TokDataset(paths["data"])
    acc = hp["batch"] // hp["per_device"]
    assert acc * hp["per_device"] == hp["batch"]

    class TimedSave(TrainerCallback):
        last = time.time()

        def on_step_end(self, args, state, control, **kw):
            if time.time() - self.last > hp["save_every_s"]:
                control.should_save, self.last = True, time.time()

        def on_log(self, args, state, control, logs=None, **kw):
            if logs:
                log(f"step {state.global_step}/{state.max_steps} " + " ".join(
                    f"{k}={v:.4g}" if isinstance(v, float) else f"{k}={v}" for k, v in logs.items()))

    total = spec.get("max_steps") or -(-len(ds) // hp["batch"]) * hp["epochs"]
    args = TrainingArguments(
        output_dir=paths["ckpt"], per_device_train_batch_size=hp["per_device"],
        gradient_accumulation_steps=acc, learning_rate=hp["lr"], lr_scheduler_type="cosine",
        warmup_steps=round(hp["warmup_ratio"] * total), weight_decay=hp["weight_decay"], optim=hp["optim"],
        max_grad_norm=hp["max_grad_norm"], num_train_epochs=hp["epochs"],
        max_steps=spec.get("max_steps") or -1, bf16=hp.get("bf16", True), logging_steps=10, save_strategy="no",
        save_total_limit=1, seed=seed, data_seed=seed, report_to=[], dataloader_num_workers=hp.get("workers", 2),
        dataloader_pin_memory=True, remove_unused_columns=False, disable_tqdm=True)
    trainer = Trainer(model=model, args=args, train_dataset=ds, data_collator=Collate(tok.pad_token_id),
                      callbacks=[TimedSave()])
    resume = any(d.startswith("checkpoint-") for d in os.listdir(paths["ckpt"])) if os.path.isdir(paths["ckpt"]) else False
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    t0 = time.time()
    out = trainer.train(resume_from_checkpoint=True if resume else None)
    secs = time.time() - t0
    steps = trainer.state.global_step
    frac = steps / max(1, trainer.state.max_steps)
    info = {"train_seconds": round(secs, 1), "steps": steps, "resumed": resume,
            "train_loss": out.training_loss, "examples": len(ds), "tokens": ds.tokens(),
            "tokens_per_s": round(ds.tokens() * frac / secs, 1) if secs else None,
            "s_per_step": round(secs / max(1, steps), 3),
            "peak_mem_gb": round(torch.cuda.max_memory_allocated() / 2**30, 2) if torch.cuda.is_available() else None,
            "trainable_params": sum(p.numel() for p in model.parameters() if p.requires_grad),
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
