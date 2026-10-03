"""Write a queue file for B's runners (train_eval_job.py) from docs/RUN_MATRIX_B.csv.
  python scripts/make_queue_b.py smoke   OUT.json        # B-C0 smoke comparison + B-T0 timing
  python scripts/make_queue_b.py factorial OUT.json --seeds 0 [--registry data/REGISTRY.json] [--key_only]
  python scripts/make_queue_b.py transfer|extras|backbones|newexp OUT.json --seeds 0
  python scripts/make_queue_b.py critic OUT.json          # C-TF-critic (owner C, run by B's runners)
Revised plan (lead, 2 Oct evening): only the four key cells are evaluated on every frozen dev/test set
(every seed); every other run on dev, test_L2, dev_missing and missing (B-TR rows add test_L3alt; the new
experiments and folds use the sets the plan names; diversity curves the reduced sets). priority() encodes the
run order."""
import argparse, csv, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ("verdict", "rationale", "summary2", "value2", "ledger2")
PRIO = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
KEY_CELLS = {("verdict", "blocks"), ("verdict", "triplets"), ("ledger2", "blocks"), ("ledger2", "triplets")}
EVAL = {"bs_score": 128, "bs_gen": 256, "max_new": 384}    # B-T0b: 1.7x faster rationale eval than 64/64; capped at 128 below 60 GB
REDUCED = ("dev", "test_L2")          # FINAL_TASKS_B: non-core runs on dev and L2 (+ A's new sets, separate runs)
TRANSFER = ("dev", "test_L2", "test_L3alt", "dev_missing", "missing")   # Table 4 rows (B-TR): its L3-alt and MR columns
A_CODE = "e40789bd5d7a"     # role A's rule_v1 freeze: check-code renderer for genprm (snapshot under ROOT/code)
# adapters kept on the PVC for the clinical columns (C's eval_clinical.py, not yet available): Table 4 rows and
# the MedEinst column of Table 9; only configs/keep_adapters.json runs are published for C and D
CLINICAL_CELLS = {("verdict", "triplets"), ("summary2", "triplets"), ("rationale", "triplets"), ("value2", "triplets"),
                  ("ledger2", "balanced"), ("ledger2", "blocks"), ("ledger2", "triplets")}


CORE_CELLS = {(f, c) for f in ("verdict", "summary2", "ledger2") for c in ("blocks", "triplets")}
NEW_FAMILIES = ("xr_v1", "challenge_v1", "rewrite_v1", "ec_v1")     # A's new sets (FINAL_TASKS_B P0.6)
CLIN_TRAIN = "clin_v1/clinpairs_train"    # C's final clinical training pairs (MedEinst reference + MedQA-train key pairs), once frozen
ABL_ORDER = ("decfield", "bitonly-judge", "bitonly-reader", "conddrv", "verify", "concept", "premise-gate", "probe-rw",
             "nopres", "noresamp", "pairwise")       # FINAL_TASKS_B P1 order


def priority(rid, seed, mprio="P1"):
    """Run order of FINAL_TASKS_B (3 Oct; lower first, equal values in queue-file order). P0: eval-only runs of the
    analyses (program-supplied ledger, field interventions), summary x blocks s0, seeds 1-2 of the six core cells,
    the summary pipeline whose judge also sees the case, leave one near-miss kind out (subject, time, boundary),
    evaluations on A's new sets. P1: remaining seed-0 cells, seeds 3-4 of the core cells, ablations in the listed
    order, FoVer and GenPRM rows, medical-data rows, folds 2-3, diversity curves, second backbone. Rows the file does
    not list (dose curve, seeds 1-2 of non-core cells, P2 seeds of ablations) come after everything."""
    m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", rid)
    cell = (m[1], m[2]) if m else None
    if rid in ("B-AE-oracle-ledger", "B-AE-field-edit", "B-AE-field-swap"):
        return 0
    # NEXT_TASKS_B (3 Oct evening) order: case-visible judges (seed 0, then the triplets seeds 1-2), leave-one-kind-out
    # seeds 1-2 and the decision-bit reader, the auxiliary grid, rewritten notes, A's new sets, 4B cells, folds
    cv = re.fullmatch(r"B-(SC|LC)-\w+-\w+-s(\d)", rid)
    if cv:
        return 10 if cv[2] == "0" else 15
    if rid.startswith("B-LOKO-") and (seed > 0 or "-bit_reader-" in rid):
        return 20
    if rid.startswith("B-AUX-"):
        return 30
    if rid.startswith("B-RW-"):
        return 35
    if rid.startswith("B-BB-") and seed == 0:
        return 50
    if rid.startswith("B-FOLD"):
        return 55
    if rid == "B-F-summary2-blocks-s0":
        return 10
    if m and cell in CORE_CELLS and seed in (1, 2):
        return 20
    if rid.startswith("B-SC-"):
        return 30
    if rid.startswith("B-LOKO-"):
        return 40 + {"subject": 0, "time": 1, "boundary": 2}.get(rid.split("-")[2], 3)
    if rid.startswith("B-NS-"):
        return 45
    if m and seed == 0:
        return 50
    if m and cell in CORE_CELLS and seed in (3, 4):
        return 55
    a = re.fullmatch(r"B-AB-([\w-]+?)(-scores)?-s(\d)(-scores)?", rid)
    if a and int(a[3]) == 0 and a[1] in ABL_ORDER:
        return 60 + ABL_ORDER.index(a[1])
    if rid == "B-AE-pred-bit-program":
        return 60
    if rid.startswith("B-TR-fover"):
        return 72 + (seed > 0) * 20
    if rid.startswith("B-TR-genprm"):
        return 73 + (seed > 0) * 20
    if rid.startswith("B-DIS-"):
        return 74
    if rid.startswith("B-TR-"):
        return 74 + (seed > 0) * 20
    if rid.startswith("B-FOLD"):
        return 76 + (seed > 0)
    if rid.startswith("B-DIV-"):
        return 80 + (seed > 0)
    if rid.startswith("B-BB-"):
        return 85 + (seed > 0) * 10
    return 99


def keep_list():
    return set(json.load(open(f"{ROOT}/configs/keep_adapters.json"))["keep"])


def matrix():
    return list(csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")))


def frozen_evals(registry, version):
    reg = json.load(open(registry))
    return reg, sorted(n for n, v in reg.items() if n.startswith(version + "/") and v.get("frozen")
                       and v.get("split") in ("dev", "test"))


def smoke():
    runs = [{"run_id": f"B-C0-smoke-verdict-{c}-s0", "format": "verdict", "corpus": f"smoke_v2/train_{c}",
             "seed": 0, "priority": 0, "provisional": True,
             "eval_sets": ["smoke_v2/dev_seen_rules", "smoke_v2/test_heldout_rules"]}
            for c in ("blocks", "triplets")]
    runs += [{"run_id": f"B-T0-{f}", "format": f, "corpus": "smoke_v2/train_triplets", "seed": 0,
              "priority": 1, "provisional": True, "timing": True, "max_steps": 200,
              "eval_sets": ["smoke_v2/test_heldout_rules"]} for f in FMTS]
    return runs


def factorial(seeds, registry, version, key_only=False):
    reg, evals = frozen_evals(registry, version)
    keep, runs = keep_list(), []
    for r in matrix():
        m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", r["run_id"])
        if not m or int(m[3]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        if key_only and (m[1], m[2]) not in CORE_CELLS:
            continue
        corpus = f"{version}/train_{m[2]}"
        if corpus not in reg or not reg[corpus].get("frozen"):
            sys.exit(f"{corpus} not frozen in {registry}")
        full = (m[1], m[2]) in CORE_CELLS      # every frozen dev/test set: the six core cells, every seed
        runs.append({"run_id": r["run_id"], "format": m[1], "corpus": corpus, "seed": int(m[3]),
                     "n_examples": 60000, "priority": priority(r["run_id"], int(m[3]), r["priority"]),
                     "keep_adapter": r["run_id"] in keep or (m[1], m[2]) in CLINICAL_CELLS | CORE_CELLS, "eval": dict(EVAL),
                     "eval_sets": evals if full else [f"{version}/{s}" for s in REDUCED]})
    return runs


def transfer(seeds, registry, version):
    """B-TR rows that need no other role's data: fover (verdict on FoVer formal steps) and genprm
    (GenPRM-style verifier on rule triplets). Table 4 rows: reduced sets + test_L3alt."""
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-TR-(fover|genprm)-s(\d)", r["run_id"])
        if not m or int(m[2]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        seed = int(m[2])
        spec = ({"format": "verdict", "corpus": "fover_v1/train"} if m[1] == "fover" else
                {"format": "genprm", "corpus": f"{version}/train_triplets", "a_code": A_CODE, "min_gen": 2})
        runs.append({"run_id": r["run_id"], "seed": seed, "n_examples": 60000,
                     "priority": priority(r["run_id"], seed, r["priority"]),
                     "keep_adapter": True,   # Table 4 rows (clinical columns)
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in TRANSFER], **spec})
    # 'with medical data' rows: ledger2 on C's clinical pairs only, and on rule triplets + clinical pairs 1:1
    reg = json.load(open(registry))
    clin = CLIN_TRAIN if reg.get(CLIN_TRAIN, {}).get("frozen") else None
    for r in matrix():
        m = re.fullmatch(r"B-TR-(clinonly|tripclin)-s(\d)", r["run_id"])
        if m and clin and int(m[2]) in seeds and r["status"] not in ("done", "dropped", "deferred"):
            data = ({"corpus": clin} if m[1] == "clinonly" else
                    {"corpus": f"{version}/train_triplets", "mix": {"corpus": clin, "share": 0.5}})
            runs.append({"run_id": r["run_id"], "seed": int(m[2]), "format": "ledger2", "n_examples": 60000, **data,
                         "priority": priority(r["run_id"], int(m[2]), r["priority"]), "max_drop": 0.01,
                         "hp": {"per_device": 8},    # long clinical notes: 16 x 1024 tokens OOMs on 40 GB cards
                         "keep_adapter": True, "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in TRANSFER]})
    # MedEinst with diseases held out (FINAL_TASKS_B P1, 3 runs): ledger2 on C's training-disease pairs
    corpus = "clin_v1/clinpairs_medeinst_dis"
    if reg.get(corpus, {}).get("frozen"):
        for r in matrix():
            m = re.fullmatch(r"B-DIS-s(\d)", r["run_id"])
            if m and int(m[1]) in seeds and r["status"] not in ("done", "dropped", "deferred"):
                runs.append({"run_id": r["run_id"], "seed": int(m[1]), "format": "ledger2", "corpus": corpus,
                             "n_examples": 60000, "priority": priority(r["run_id"], int(m[1]), r["priority"]),
                             "max_drop": 0.01,     # long notes: 0.75% of examples exceed max_len 1024 (dropped)
                             "hp": {"per_device": 8},    # long notes: 16 x 1024 tokens OOMs on 40 GB cards (same batch 64)
                             "keep_adapter": True, "eval": dict(EVAL),
                             "eval_sets": ["clin_v1/medeinst_dis_test", f"{version}/dev", f"{version}/test_L2"]})
    return runs


BACKBONES = {"qwen3.5-4b": "unsloth/Qwen3.5-4B", "non-qwen-4to9b": "unsloth/granite-4.1-8b"}   # configs/models_b.json


def backbones(seeds, registry, version):
    """B-BB rows: the key cells on other base models (claimable only by runners that staged them,
    submit_b.py runners ... --models)."""
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-BB-(.+)-(verdict|ledger2)-(blocks|triplets)-s(\d)", r["run_id"])
        if not m or int(m[4]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        runs.append({"run_id": r["run_id"], "format": m[2], "corpus": f"{version}/train_{m[3]}", "seed": int(m[4]),
                     "n_examples": 60000, "base_model": BACKBONES[m[1]],
                     "priority": priority(r["run_id"], int(m[4]), r["priority"]), "keep_adapter": False,
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    return runs


# Table 9 ablations: changes against ledger2 x triplets (corpus names inside <version>/)
ABLATIONS = {"decfield": {"format": "ledger2_dec"}, "bitonly-judge": {"format": "dec_judge"},
             "bitonly-reader": {"format": "bit_reader"}, "conddrv": {"format": "conddrv", "min_gen": 3}, "verify": {"format": "ledger2_verify", "mode": "verify"},
             "concept": {"kind": "concept"}, "nopres": {"corpus": "abl_nopres_triplets"},
             "noresamp": {"resample_p": 0}, "pairwise": {"format": "verdict_bt"},
             "concl-only": {"corpus": "abl_conclusion_triplets"}}
# Table 9 / Sec. 7.4 evaluation-only rows: adapter run, format, eval mode, sets
EVAL_ONLY = {"oracle-ledger": ("B-F-ledger2-triplets-s0", "ledger2", "oracle_ledger", ("dev", "test_L2")),
             "pred-bit-program": ("B-AB-decfield-s0", "ledger2_dec", "program_bit", ("dev", "test_L2")),
             "field-swap": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_swap", ("dev", "test_L2")),
             "field-edit": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_edit", ("test_L2",))}   # newer runners (v2/)


def extras(seeds, registry, version):
    """B-AB ablations, B-AE evaluation-only rows, B-FOLD fold replications and B-DIV diversity curves
    whose inputs exist (change loss and the premise gate are queued by hand; probe re-weighting step 1 here,
    the weighted run in probe_rw())."""
    reg = json.load(open(registry))
    ok = lambda name: name in reg and reg[name].get("frozen")
    runs = []
    for r in matrix():
        rid, seed = r["run_id"], int(r["seed"]) if r["seed"].isdigit() else 0
        if seed not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        base = {"run_id": rid, "seed": seed, "priority": priority(rid, seed, r["priority"]), "eval": dict(EVAL)}
        if rid == "B-AB-probe-rw-s0":    # step 1 of 3 (then scripts/probe_weights.py, then the weighted run)
            runs.append({**base, "run_id": rid + "-scores", "format": "ledger2", "train": False,
                         "adapter": "adapters/B-F-ledger2-blocks-s0", "eval_sets": [f"{version}/abl_probe_blocks"]})
            continue
        m = re.fullmatch(r"B-AB-([\w-]+)-s\d", rid)
        if m and m[1] in ABLATIONS:
            ch = dict(ABLATIONS[m[1]])
            spec = {**base, "format": "ledger2", "corpus": f"{version}/train_triplets", "n_examples": 60000,
                    "keep_adapter": seed == 0, "eval_sets": [f"{version}/{s}" for s in REDUCED]}
            if "mode" in ch:
                spec["eval"]["mode"] = ch.pop("mode")
            if "corpus" in ch:
                ch["corpus"] = f"{version}/{ch['corpus']}"
            runs.append({**spec, **ch})
            continue
        m = re.fullmatch(r"B-AE-([\w-]+)", rid)
        if m and m[1] in EVAL_ONLY:
            src, fmt, mode, sets = EVAL_ONLY[m[1]]
            runs.append({**base, "format": fmt, "train": False, "adapter": f"adapters/{src}", "a_code": A_CODE,
                         "eval": {**EVAL, "mode": mode}, "eval_sets": [f"{version}/{s}" for s in sets]}
                        | ({"min_gen": 2} if mode == "ledger_edit" else {}))
            continue
        m = re.fullmatch(r"B-FOLD(\d)-(\w+)-(\w+)-s\d", rid)
        if m and ok(f"{version}_fold{m[1]}/train_{m[3]}"):
            v = f"{version}_fold{m[1]}"
            runs.append({**base, "format": m[2], "corpus": f"{v}/train_{m[3]}", "n_examples": 60000,
                         "keep_adapter": False, "eval_sets": [f"{v}/dev", f"{v}/test_L2"]})
            continue
        m = re.fullmatch(r"B-DIV-(\w+)-(\d+)-s\d", rid)
        if m and ok(f"{version}/div_{m[1]}_{m[2]}"):
            runs.append({**base, "format": "ledger2", "corpus": f"{version}/div_{m[1]}_{m[2]}", "n_examples": None,
                         "keep_adapter": False, "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    order = ("B-AB", "B-AE", "B-FOLD", "B-DIV")     # within a priority: Table 9 first, then folds, then curves
    return sorted(runs, key=lambda r: next(i for i, f in enumerate(order) if r["run_id"].startswith(f)))


def probe_rw(version):
    """Probe re-weighting step 3: ledger2 on abl_probe_blocks (probes are never trained on), judge pairs drawn
    by the weights that pretok derives from B-AB-probe-rw-s0-scores (step 2 runs inside prep)."""
    return [{"run_id": "B-AB-probe-rw-s0", "seed": 0, "priority": priority("B-AB-probe-rw-s0", 0), "format": "ledger2",
             "corpus": f"{version}/abl_probe_blocks", "n_examples": 60000,
             "pair_weights": "derived/probe_rw/B-F-ledger2-blocks-s0.json",
             "probe_scores": "B-AB-probe-rw-s0-scores", "probe_set": f"{version}/abl_probe_blocks",
             "keep_adapter": True, "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]}]


def critic(registry, version):
    """C-TF-critic (owner C, executed by B's runners): zero-shot base model, frozen verdict prompt, pointwise u,
    every frozen dev/test set."""
    _, evals = frozen_evals(registry, version)
    return [{"run_id": "C-TF-critic", "seed": 0, "priority": priority("C-TF-critic", 0), "format": "verdict",
             "train": False, "keep_adapter": False, "eval": dict(EVAL), "eval_sets": evals}]


def newexp(seeds, registry, version):
    """Leave one near-miss kind out (FINAL_TASKS_B P0.5): B-LOKO-<kind>-<format>-s0, format verdict, summary2 or
    ledger2, kind subject, time or boundary, on A's train_triplets_no_<kind> (queued once A registers it; dev,
    test_L2, test_L0, scored on the held-out kind). Near-miss dose (not in FINAL_TASKS_B; last): B-DOSE-<pct>-<format>-s0
    on train_dose_<pct> (dev, test_L2)."""
    reg = json.load(open(registry))
    frozen = {n for n, v in reg.items() if v.get("frozen")}
    runs = []
    for r in matrix():
        rid = r["run_id"]
        m = re.fullmatch(r"B-(LOKO|DOSE)-(\w+?)-(verdict|summary2|ledger2|bit_reader)-s(\d)", rid)
        if not m or int(m[4]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        if m[1] == "LOKO":
            hits = sorted(n for n in frozen if n.endswith(f"/train_triplets_no_{m[2]}"))
            if not hits:
                continue                                  # A has not registered the corpus yet
            corpus, sets = hits[0], ("dev", "test_L2", "test_L0")
        else:
            corpus, sets = f"{version}/train_dose_{m[2]}", ("dev", "test_L2")
            if corpus not in frozen:
                continue
        runs.append({"run_id": rid, "format": m[3], "corpus": corpus, "seed": int(m[4]), "n_examples": 60000,
                     "priority": priority(rid, int(m[4]), r["priority"]), "keep_adapter": m[1] == "LOKO",
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in sets]})
    return sorted(runs, key=lambda r: r["priority"])


def new_sets(registry):
    """A's frozen evaluation sets of the new families, as registered so far."""
    reg = json.load(open(registry))
    return sorted(n for n, v in reg.items()
                  if n.split("/")[0] in NEW_FAMILIES and v.get("frozen") and v.get("split") != "train")


def with_new_sets(runs, registry):
    """Training runs (not folds or diversity curves) also evaluate on the registered new sets and keep their
    adapter, so that sets A registers later are scored by B-NS eval-only runs (FINAL_TASKS_B P0.6)."""
    ns = new_sets(registry)
    for r in runs:
        if r.get("train", True) and not r["run_id"].startswith(("B-FOLD", "B-DIV", "B-C0", "B-T0", "B-AUX")):
            r["eval_sets"] = r["eval_sets"] + [s for s in ns if s not in r["eval_sets"]]
            r["keep_adapter"] = True
    return runs


def ns_eval(registry, adapters):
    """B-NS-<family>-<run>: eval-only runs of kept adapters on each new-set family their run did not evaluate.
    adapters: run_ids with an adapter on the PVC; their specs come from configs/queues."""
    specs = {}
    for p in sorted(glob.glob(f"{ROOT}/configs/queues/**/*.json", recursive=True)):
        specs.update({r["run_id"]: r for r in json.load(open(p))["runs"]})
    fams = {}
    for s in new_sets(registry):
        fams.setdefault(s.split("/")[0], []).append(s)
    runs = []
    for src in sorted(adapters):
        spec = specs.get(src, {})
        meta = f"{ROOT}/results_git/{src}/meta.json"     # what the run did: done runs leave the queue files, and a
        if os.path.exists(meta):                          # runner may have claimed a run before its spec changed
            m = json.load(open(meta))
            spec = spec | {k: m[k] for k in ("format", "seed", "eval_sets")} | {"base_model": m["model"]}
        for fam, sets in sorted(fams.items()):
            if set(sets) <= set(spec.get("eval_sets", [])):
                continue
            rid = f"B-NS-{fam}-{src}"
            runs.append({"run_id": rid, "seed": spec["seed"], "priority": priority(rid, 0), "format": spec["format"],
                         "train": False, "adapter": f"adapters/{src}", "eval": dict(EVAL), "eval_sets": sets}
                        | {k: spec[k] for k in ("base_model", "min_gen", "kind") if k in spec})
    return runs


def case_visible(registry, version):
    """FINAL_TASKS_B P0.4 and NEXT_TASKS_B 2: pipelines whose judge also sees the case (rule, case, record, claim):
    summary2_case (B-SC-summary2-<corpus>-s<seed>) and ledger2_case (B-LC-ledger2-<corpus>-s<seed>); rows and seeds
    from docs/RUN_MATRIX_B.csv."""
    fmts = {"SC": "summary2_case", "LC": "ledger2_case"}
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-(SC|LC)-(summary2|ledger2)-(blocks|triplets)-s(\d)", r["run_id"])
        if not m or r["status"] in ("done", "dropped", "deferred"):
            continue
        runs.append({"run_id": r["run_id"], "seed": int(m[4]), "priority": priority(r["run_id"], int(m[4])),
                     "format": fmts[m[1]], "corpus": f"{version}/train_{m[3]}", "n_examples": 60000,
                     "keep_adapter": True, "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    return runs


# docs/AUX_PROTOCOL.md S1 (secondary analysis, specified 3 Oct after the planned comparisons failed): verdict format
AUX_DS = {"nli4ct": {"train": "clin_v1/nli4ct_train", "dev": "clin_v1/nli4ct_dev", "test": ("clin_v1/nli4ct_test",)},
          "medeinst": {"train": "clin_v1/medeinst_train", "dev": "clin_v1/medeinst_ref_dev",
                       "test": ("clin_v1/medeinst_test", "clin_v1/medeinst_neg")},
          "trialgpt": {"train": "clin_v1/trialgpt_cv", "dev": "clin_v1/trialgpt_dev", "test": ("clin_v1/trialgpt_cv",),
                       "folds": 5}}
AUX = {"2": "rule_v1x/aux_blocks_20k", "3": "rule_v1x/aux_triplets_20k", "4": "clin_v1/medeinst_neg_train"}
AUX_EPOCHS = f"{ROOT}/configs/aux_epochs.json"      # {dataset: epochs}, fixed on dev by scripts/aux_epochs.py


def aux(registry, seeds=(0, 1, 2)):
    """S1 runs whose inputs are frozen in the registry. Epoch selection: B-AUX-<ds>-ep5-s0 (recipe 1, seed 0, five
    epochs, an adapter saved after each) and B-AUX-<ds>-ep5-e<k> (adapter of epoch k on the dataset's dev split).
    Grid, once configs/aux_epochs.json fixes the dataset's epochs E: B-AUX-<ds>[-f<fold>]-r<recipe>-s<seed>,
    recipes 1 (E passes over the in-domain records), 1b (the same plus as many in-domain examples as recipe 3 has
    auxiliary records), 2 and 3 (E passes plus every record of aux_blocks_20k / aux_triplets_20k once), 4 for MedEinst
    (E passes plus every record of medeinst_neg_train once). TrialGPT: one run per held-out fold (fold and
    not-applicable items excluded from training), scored on all of trialgpt_cv; C pools the held-out predictions."""
    reg = json.load(open(registry))
    ok = lambda name: reg.get(name, {}).get("frozen")
    epochs = json.load(open(AUX_EPOCHS)).get("chosen", {}) if os.path.exists(AUX_EPOCHS) else {}
    runs, base = [], {"format": "verdict", "keep_adapter": True, "eval": dict(EVAL), "max_drop": 0.01,
                      "hp": {"per_device": 8}}          # long clinical notes (batch 64 unchanged)
    for ds, c in AUX_DS.items():
        if not ok(c["train"]):
            continue
        excl = lambda f: {"train_meta_exclude": {"fold": [f], "category": ["na"]}} if "folds" in c else {}
        if ok(c["dev"]):                          # epoch selection; TrialGPT trains on folds 1-4 (fold 0 held out)
            ep = f"B-AUX-{ds}-ep5-s0"
            runs.append({**base, "run_id": ep, "seed": 0, "priority": priority(ep, 0), "corpus": c["train"],
                         "passes": 1, "hp": {"per_device": 8, "epochs": 5}, "save_epochs": True, "eval_sets": []} | excl(0))
            for k in range(1, 6):
                runs.append({**base, "run_id": f"{ep}-e{k}", "seed": 0, "priority": priority(ep, 0), "train": False,
                             "keep_adapter": False, "adapter": f"adapters/{ep}-e{k}", "eval_sets": [c["dev"]]})
        if ds not in epochs:
            continue
        tests = [s for s in c["test"] if ok(s)]
        recipes = {"1": {}, "1b": {"pad_examples": reg[AUX["3"]]["n_records"]},
                   "2": {"mix": {"corpus": AUX["2"]}}, "3": {"mix": {"corpus": AUX["3"]}}}
        if ds == "medeinst" and ok(AUX["4"]):
            recipes["4"] = {"mix": {"corpus": AUX["4"]}}
        for rc, extra in recipes.items():
            if rc in ("2", "3", "4") and not ok(AUX[rc]):
                continue
            for sd in seeds:
                for f in range(c.get("folds", 1)):
                    rid = f"B-AUX-{ds}" + (f"-f{f}" if "folds" in c else "") + f"-r{rc}-s{sd}"
                    runs.append({**base, "run_id": rid, "seed": sd, "priority": priority(rid, sd), "corpus": c["train"],
                                 "passes": epochs[ds], "eval_sets": tests} | extra | excl(f))
    return runs


RW_CORPUS = "rule_v1x/train_triplets_rw"     # A's training-side rewrites (NEXT_TASKS_A 4), queued once frozen


def rewritten(registry, version):
    """NEXT_TASKS_B 5: verdict and summary2 trained on A's rewritten-note triplets (B-RW-<format>-triplets-s<seed>);
    scored on dev, L2 and every registered new set (with_new_sets)."""
    if not json.load(open(registry)).get(RW_CORPUS, {}).get("frozen"):
        return []
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-RW-(verdict|summary2)-triplets-s(\d)", r["run_id"])
        if m and r["status"] not in ("done", "dropped", "deferred"):
            runs.append({"run_id": r["run_id"], "seed": int(m[2]), "priority": priority(r["run_id"], int(m[2])),
                         "format": m[1], "corpus": RW_CORPUS, "n_examples": 60000, "keep_adapter": True,
                         "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    return runs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["smoke", "factorial", "transfer", "extras", "backbones", "probe_rw", "critic", "ns",
                                     "newexp", "case_visible", "rewritten", "aux"])
    ap.add_argument("out")
    ap.add_argument("--seeds", default="0")
    ap.add_argument("--registry", default=f"{ROOT}/data/REGISTRY.json")
    ap.add_argument("--version", default="rule_v1")
    ap.add_argument("--key_only", action="store_true", help="factorial: the four key cells only")
    ap.add_argument("--runs", default="", help="keep run_ids matching this regex")
    ap.add_argument("--adapters", default="", help="ns: comma list of run_ids with an adapter on the PVC")
    a = ap.parse_args()
    seeds = {int(s) for s in a.seeds.split(",")}
    gen = {"smoke": lambda: smoke(),
           "factorial": lambda: factorial(seeds, a.registry, a.version, a.key_only),
           "transfer": lambda: transfer(seeds, a.registry, a.version),
           "backbones": lambda: backbones(seeds, a.registry, a.version),
           "extras": lambda: extras(seeds, a.registry, a.version),
           "probe_rw": lambda: probe_rw(a.version),
           "critic": lambda: critic(a.registry, a.version),
           "newexp": lambda: newexp(seeds, a.registry, a.version),
           "case_visible": lambda: case_visible(a.registry, a.version),
           "rewritten": lambda: rewritten(a.registry, a.version),
           "aux": lambda: aux(a.registry),
           "ns": lambda: ns_eval(a.registry, a.adapters.split(","))}
    runs = [r for r in with_new_sets(gen[a.kind](), a.registry) if re.search(a.runs, r["run_id"])]
    newer = [r["run_id"] for r in runs if r.get("min_gen", 0) >= 2]   # runners staged before 2 Oct 13:00 read the top level
    if newer and "v2" not in os.path.normpath(os.path.abspath(a.out)).split(os.sep):
        sys.exit(f"{newer} need runner code from 2 Oct 13:00 UTC on: write them under configs/queues/v2/ (docs/NRP_B.md)")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump({"runs": runs}, open(a.out, "w", newline="\n"), indent=1)
    print(f"{len(runs)} runs -> {a.out}")


if __name__ == "__main__":
    main()
