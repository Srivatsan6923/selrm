# DECISIONS role B

date | decision | rule applied | evidence | effect on paper
---|---|---|---|---
2026-10-02 | Work in a fresh clone of Srivatsan6923/selrm@role-b (D:\NAACL27\selrm-role-b); the opened folder was another repo (Symbolic_PRM_NAACL) | PROMPTS P1 (role-b branch) | git remote of D:\NAACL27 | none
2026-10-02 | GPUs on NRP Nautilus (namespace ecepxie), one GPU per Job, queue runners; Drive not used by B; results leave the cluster through results_git/<run_id>/ on role-b | role-B NRP prompt; COLAB guide fallback channel | docs/NRP_B.md | none
2026-10-02 | Unidentified namespace secrets (e.g. github-token) are not used; code reaches the PVC by kubectl cp until selrm-github-ro exists (COMPUTE REQUEST #1) | integrity, secrets rule | kubectl get secrets (names only) | none
2026-10-02 | Smoke runs are named B-C0-smoke-<format>-<corpus>-s<seed>; timing runs B-T0-<format>; both provisional and never tabled | AUTONOMY integrity (smoke numbers never enter a table) | scripts/make_queue_b.py | none
2026-10-02 | Example selection uses a fixed construction seed (0) shared by all seeds of a cell; the run seed sets data order (Trainer seed/data_seed) and LoRA init (random_state) | ROLE.md "Seeds set data order and LoRA initialisation" | selrm/formats.py, scripts/finetune.py | seed variance = training stochasticity only
2026-10-02 | Two-stage budget: n//2 reader examples, one per (case, condition), cycled with a fresh shuffle per pass when units < n//2; n//2 judge examples as both claims of a (case, claim type), so judge labels are exactly 50/50 | ROLE.md equal budget | selrm/formats.py | all formats see n examples
2026-10-02 | Ledger resampling: with p=0.3 a selected judge pair takes its ledger, claim and label from another case_kind of the same tid and claim type (same rule and condition) | ROLE.md ledger resampling | selrm/formats.py | ablation p=0 = B-AB-noresamp
2026-10-02 | value2 reader uses the frozen ledger reader prompt with targets cut to need/found (no new prompt text) | INTERFACES 2 frozen prompts | selrm/formats.py | value-ledger row reads "same prompt, fewer fields"
2026-10-02 | Malformed rule (u=-20 both claims) applied to ledger2/value2 reader outputs that are unparsable, cut off at the generation limit, or quote a found that is not a substring of the case; summary2 prose is never malformed; rationale is one-stage (rule not applied) | INTERFACES 3 | scripts/eval_local.py | malformed rate reported per set
2026-10-02 | Rationale scoring: greedy generation, u read at the first '+'/'-' token that starts a line; if none, a newline is appended and u is read there (counted as rationale_no_answer) | ROLE.md "generate the ledger, then read the answer logits" | scripts/eval_local.py | none
2026-10-02 | Completions end with the chat end-of-turn token <|im_end|> (in the loss), so generation formats learn to stop | INTERFACES 2 (chat template by caller) | scripts/pretok.py | none
2026-10-02 | Own claims (CLAIMED_B) count as stale after 15 min without heartbeat (runners heartbeat every 30 s); other roles' claims keep the 3 h rule | INTERFACES 7 | selrm/runq.py | none
