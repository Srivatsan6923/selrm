"""Concept scorer (B-AB-concept, Table 9: "fields predicted by linear heads and a linear
verdict"). Frozen backbone (no LoRA); feature = final hidden state at the end of the
reader prompt (rule, case, condition). Linear heads predict the concepts of the gold
ledger; a linear verdict on the predicted concept probabilities only (a bottleneck)
predicts whether the condition holds; claims are scored from that probability as the
program does on a bit (claim s is correct iff the condition does not hold):
u(s) = -logit(p), u(s_prime) = +logit(p).
Run through train_eval_job with a spec {"kind": "concept", "corpus": <train set>, ...}."""
import json, os, sys, time
import numpy as np
import torch
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.formats import dataset_path, holds, reader_unit, reader_units

CONCEPTS = ("mentioned", "subject_patient", "status_present", "time_current", "patient_present_current")


def concepts(rec):
    """Concept labels from the gold ledger: first entry's fields, plus whether any entry is a
    present, current finding of the patient."""
    led = rec["ledger"]
    e = led[0]
    return [int(e["found"] != "not mentioned"), int(e["subject"] == "patient"), int(e["status"] == "present"),
            int(e["time"] == "current"),
            int(any(x["subject"] == "patient" and x["status"] == "present" and x["time"] == "current"
                    and x["found"] != "not mentioned" for x in led))]


@torch.no_grad()
def features(model, seqs, pad, dev, bs=64):
    import finetune
    out = torch.zeros((len(seqs), model.config.get_text_config().hidden_size), dtype=torch.float32)
    order = sorted(range(len(seqs)), key=lambda i: len(seqs[i]))
    for k in range(0, len(order), bs):
        b = order[k:k + bs]
        L = max(len(seqs[i]) for i in b)
        ids = torch.full((len(b), L), pad, dtype=torch.long)
        att = torch.zeros((len(b), L), dtype=torch.long)
        for j, i in enumerate(b):
            ids[j, L - len(seqs[i]):] = torch.tensor(seqs[i])
            att[j, L - len(seqs[i]):] = 1
        out[b] = finetune.last_hidden(model, ids.to(dev), att.to(dev)).float().cpu()
    return out


def logreg(X, y, seed=0, steps=300, l2=1e-3, dev="cpu"):
    """Logistic regression with Adam on standardised inputs -> (w, b, mean, std)."""
    torch.manual_seed(seed)
    X, y = X.to(dev), y.float().to(dev)
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Z = (X - mu) / sd
    w = torch.zeros(Z.shape[1], device=dev, requires_grad=True)
    b = torch.zeros((), device=dev, requires_grad=True)
    opt = torch.optim.Adam([w, b], lr=0.05)
    for _ in range(steps):
        opt.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(Z @ w + b, y) + l2 * (w ** 2).sum()
        loss.backward()
        opt.step()
    return w.detach(), b.detach(), mu, sd


def predict(head, X):
    w, b, mu, sd = head
    return torch.sigmoid(((X.to(w.device) - mu) / sd) @ w + b)


def run(spec, root, model, tok, sc, out_dir, log, tag):
    """Fit heads on the training corpus units, score every eval set. -> {set: summary}."""
    import eval_local
    from pretok import chat, tok_ids
    from selrm.prompts import reader_prompt
    dev, t0 = next(model.parameters()).device, time.time()
    train = [r for r in reader_units(eval_local.load_jsonl(dataset_path(root, spec["corpus"]))) if holds(r) is not None]
    Xtr = features(model, tok_ids(tok, [chat(tok, reader_prompt(r)) for r in train]), sc.pad, dev)
    C = torch.tensor([concepts(r) for r in train])
    heads = [logreg(Xtr, C[:, k], seed=spec.get("seed", 0), dev=dev) for k in range(len(CONCEPTS))]
    P = torch.stack([predict(h, Xtr) for h in heads], 1).cpu()
    verdict = logreg(P, torch.tensor([holds(r) for r in train]), seed=spec.get("seed", 0))
    acc = {c: round(float(((P[:, k] > 0.5).long() == C[:, k]).float().mean()) * 100, 2) for k, c in enumerate(CONCEPTS)}
    log(f"concept heads fitted on {len(train)} units in {time.time() - t0:.0f} s; train accuracy {acc}")
    out = {}
    for set_name in spec["eval_sets"]:
        t1 = time.time()
        recs = eval_local.load_jsonl(dataset_path(root, set_name))
        units = reader_units(recs)
        seqs, keys = eval_local.unpack(f"{root}/tok/{tag}/eval/{set_name}/reader_ledger.npz", len(tok))
        assert keys == ["/".join(r["iid"].split("/")[:2]) for r in units], "eval prompts out of sync"
        X = features(model, seqs, sc.pad, dev)
        p = predict(verdict, torch.stack([predict(h, X) for h in heads], 1).cpu()).clamp(1e-6, 1 - 1e-6)
        lp = {reader_unit(r): float(torch.log(q / (1 - q))) for r, q in zip(units, p)}
        rows = [{"iid": r["iid"], "u": -lp[reader_unit(r)] if r["claim_role"] == "s" else lp[reader_unit(r)]} for r in recs]
        name = set_name.replace("/", "~")
        with open(f"{out_dir}/scores_{name}.jsonl", "w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")
        summ = eval_local.summarize(recs, [row["u"] for row in rows], spec["run_id"], set_name)
        summ["eval"] = {"seconds": round(time.time() - t1, 1), "concept_train_acc": acc, "units": len(units)}
        json.dump(summ, open(f"{out_dir}/summary_{name}.json", "w"), indent=1)
        a = summ.get("all", {})
        log(f"{spec['run_id']} {set_name}: TA {a.get('TA', float('nan')):.1f} n={a.get('n')} (concept scorer)")
        out[set_name] = summ
    return out
