# Paper context (read before writing any code)

Working title: **Learning When to Change: Symbolic Supervision for Selective
Evidence Sensitivity in Medical Reward Models**
Venue: NAACL/COLING 2027 main conference via ARR. Deadline 12 Oct 2026
(submit 11 Oct; check the AoE time on the ARR call).
Track: Safety and Alignment in LLMs (secondary: Interpretability).

The LaTeX draft in `paper/` (v10) has the full text, related work and
bibliography. **Every number in it is a red placeholder; no experiment has
been run.** Its experimental scope (6,000 GPU-hours) has been cut to the
plan below. Use the draft for definitions, wording and related work; use
this file and `CLAUDE.md` for what to run.

---

## 1. Problem

Reward models (RMs, PRMs, LLM judges) decide which medical reasoning traces
are kept, reranked and reinforced. A claim is often right for one patient and
wrong for another. A useful reward must:

- **reverse** its preference when a decisive patient input changes (flip);
- **hold** its preference when similar-looking evidence does not apply
  (near-miss): a penicillin allergy in the patient's *mother*, a *denied*
  allergy, an ulcer *healed in 2015*, an eGFR of 24 *last year* when today's
  is 52, a value *close to* but not across a threshold.

Two failures: **under-reaction** (never reverses; typical of step-error PRMs)
and **over-triggering** (reverses whenever the concept appears; typical of
judges and of models trained on flip pairs only).

## 2. Test: symbolic triplets

- Executable rules with typed inputs. Each criterion has an **applicability
  predicate** saying which mentions count (patient vs relative, current vs
  past, present vs absent). Applicability is per criterion: CHA2DS2-VASc
  counts a stroke at any time; a contraception rule counts VTE in a
  first-degree relative.
- A patient state is a set of mentions (concept, value, subject, status,
  time). Labels come from executing the rule on the state.
- Triplet = base x, flip x^f, near-miss x^n, crossed with claims s, s'.
  s correct for x and x^n; s' correct for x^f. Plus a presentation edit x^p
  (same state, other wording/order) as the "should not matter" control.
- Constraint rules: claims are two orders ("Prescribe amoxicillin." /
  "Prescribe azithromycin."). Score rules: "The urea criterion contributes 0
  points." / "... 1 point."
- Labels are **exact relative to the rule text shown in the prompt**. They do
  not claim clinical optimality. No clinician validated anything.

**Proposition 1 (in the draft).** Let d(x)=u(s,x)-u(s',x). A deterministic
scorer that depends only on the claim, only on the case, or on the case only
through a feature h with h(x^f)=h(x^n) cannot solve the triplet. The engine
builds near-misses so that h_k (is concept k named anywhere?) collides:
h_k(x)=0, h_k(x^f)=h_k(x^n)=1 for findings; numerics name k everywhere.

**Metrics.** Rev = P(d(x)>0 and d(x^f)<0). Hold = P(d(x^n)>0).
TA (triplet accuracy, primary) = P(all three right). Ties count as failures.
Also: presentation hold, tie rate, per near-miss kind, per tier.

## 3. Method: the ledger (two stages)

- **Reader**: given rule, case and the condition under test (not a candidate
  claim), writes a typed record per relevant finding:
  `need, found (value or verbatim quote or missing), subject, status, time`.
  Facts only, no decision field.
- **Judge**: sees rule + ledger + claims, **never the case**. Decides whether
  the recorded finding counts under the rule and which claim is correct.
- Training targets on rules come from the program. A quote that does not occur
  in the case makes the ledger malformed (string check).
- Comparisons that isolate the design: one-stage verdict; one-stage rationale;
  two-stage **free-text summary** (same interface, same token budget);
  two-stage value ledger (no subject/status/time); oracle ledger (program's
  ledger → measures reader vs judge error).

## 4. The full v10 paper, item by item (what must be produced, and by whom)

The three contributions in the draft:
(1) **A test**: triplets separate under-reaction from over-triggering; audit
of existing reward signals. (2) **A controlled comparison** of training
distributions and intermediate representations under one interface and
budget. (3) **Transfer with confounds removed**: a model trained on rules
alone, tested on held-out rule structure and zero-shot on MedEinst.

| Paper item | Content | Owner | Run IDs |
|---|---|---|---|
| Sec. 3, App. B, C | Rule library, splits, triplet construction, invariants, text tiers | A | A-D0..D15 |
| Table 1 | Sources and what each measures (rule triplets, MedEinst, key pairs, NLI4CT-P) | C (data), D (text) | C-CL-* |
| Table 2 | Audit of reward signals: trained PRMs, open judges, closed judges; Rev/Hold/TA/MR on rules, MedEinst, key pairs | C | C-AUD-* |
| Table 3 | Factorial: {verdict, rationale, evidence summary, value ledger, applicability ledger} x {natural, balanced, blocks, triplets}, TA on L2, 5 seeds | B | B-F-*, B-FOLD* |
| Table 4 | Transfer: training-free rows, trained-without-medical-data rows, with-medical-data rows, references; columns L2, L3-alt, Hold, MR, MedEinst, key pairs, NLI-F, NLI-C | B, C | B-F-*, B-TR-*, C-TF-*, C-REF-* |
| Sec. 7.4, Table 9 | Decision bit, reader bottleneck (program-supplied ledger, verification pass), one-stage variant, field interventions, ablations | B | B-AB-*, B-AE-* |
| Fig. 3 left | Rule-diversity curves | B (sets: A) | B-DIV-* |
| Sec. 7.4 | Other backbones | B | B-BB-* |
| Table 5, Fig. 3 right | Answer selection on MedQA and CareQA, key pairs, MedEinst; step check, combined reward, swapped vignette, no-near-misses, closed judge, oracle; selection pressure | D | D-POOL-*, D-CAL, D-SEL-*, D-SELN |
| App. F | Shortcut scorers (Table 7), composition gap (Table 8), shift analysis (Fig. 4), sampling noise, input ablations, probe | A, C | A-D14, C-DG-* |
| App. D | MedEinst details incl. disease-held-out, key pairs, CondMedQA, NLI4CT-P, overlap; claim-side test on real notes (conditional) | C, B | C-CL-*, B-DIS-* |
| App. G | Rule ladder (Table 10), training details, resources, policy training (GRPO), selection protocol | B, D | B-F-*, D-RL-*, D-RES |

Definitions the tables rely on (details in the draft, Sections 3-6):
- **Corpora.** natural: patient states sampled with flip-side conditions at
  low prevalence (15%), each case with both claims; balanced: each criterion
  outcome equally frequent, cases independent; blocks: balanced, with cases
  in base-flip pairs; triplets: blocks in which near-misses replace half of
  the base cases. All share 15% presentation and 15% missing-input instances
  and the same size.
- **Representations.** verdict only; rationale then verdict (one-stage, sees
  the case); evidence summary (two-stage, prose); value ledger (two-stage,
  need and found only); applicability ledger (two-stage, adds subject,
  status, time). Two-stage = the judge never sees the case.
- **Ledger-RM** = applicability ledger trained on triplets (the headline
  system). **Step check** = injected-error PRM; **combined reward** = minimum
  of the two calibrated scores.
- **Levels.** L0 trained rules, new patients; L1 unseen rules of a seen
  signature class; L2 held-out signature classes (primary); L3-inv invented
  rules; L3-alt trained rules with thresholds altered in the prompt, kept
  where the original and the altered rule disagree.

**Primary pre-declared comparisons** (paired bootstrap over rules, Holm):
(1) triplets vs blocks on triplet accuracy (ledger and verdict rows);
(2) blocks vs triplets on unnecessary reversal on near-misses;
(3) applicability ledger vs evidence summary on triplets (TA);
(4) rule-only Ledger-RM vs the critic on MedEinst reversal, zero-shot.
Decision rules if they fail are in the draft's Appendix A and must be
followed: report as found, change the claim.

**Beyond v10 (optional, P2):** step-level claim metrics, change-loss arm,
conclusion-only labels, in-context data effect, scale curve.

## 5. What the paper may and may not claim

- MAY: behaviour on stated executable rules; transfer to held-out rule
  structures and altered thresholds; agreement with MedEinst labels;
  reranking effects on MedQA.
- MAY NOT: clinical correctness; that a model "uses" or "ignores" evidence
  internally (describe behaviour only); selectivity on real clinical notes
  (no benchmark has case-side near-misses).
- Every number must come from a script that writes it; never type numbers
  into the paper by hand.

## 6. Related work you must know (positioning, one line each)

- **MedGuideX** (Shen et al., 2605.26567): compiles guidelines into executable
  functions, trains a *policy* on factual + counterfactual QA, keeps only
  interventions that change the outcome (= flip-only data). We add
  near-misses and target reward models.
- **DynaCF** (2606.09043): rewrites responses without changing content and
  down-weights shortcut-sensitive preference pairs; response-side, probes
  only. We edit the case both ways and train on exact labels.
- **CSR** (2509.01544): trains a solver to change its answer when its trace is
  broken; rewards change only.
- **FoVer** (Kamoi et al.): formal-verifier step labels transfer to informal
  tasks; transfer itself is not our novelty.
- **GenPRM** (2504.00891), **ThinkPRM**: generative verifiers; included as
  audited signals.
- **Med-PRM**, **MedS3**, **MedPRMBench**: medical PRMs/benchmarks; none
  changes the case under a fixed claim.
- **MedEinst** (ACL 2026): control/trap diagnostic pairs, 5,383 test pairs.
- **CondMedQA/CGR** (2602.17911): 100 questions whose answer changes with a
  stated condition; no version without the condition.
- **EHRNote-ChatQA**: expert-reviewed distractors on MIMIC-IV notes,
  credentialed access (optional, likely out of scope).
- **EVPV**, concept bottlenecks, **VeNRA** (typed fact ledger), **FinCARDS**,
  **DeepEra**: structured records / similar-but-irrelevant evidence in other
  domains. **NegEx / ConText / i2b2 2010 assertions**: origin of the
  subject/status/time attributes.
- **Compared to What?** (Yang et al. 2605.01048): targeted edits must be
  compared with meaning-preserving edits → our presentation control.

## 7. Known reviewer concerns already designed in

Confounded transfer (no medical data in the rule-only adapter); decision-bit
shortcut (reader writes facts only; bit-only ablation); one-stage vs two-stage
(matched summary baseline); template leakage (held-out templates and cue
phrases); model selection on test (dev only, frozen before test); ties count
as failures; label scope (stated rules only). See `docs/REVIEW_HISTORY.md`.

## 8. How the paper text is finished (owner D, everyone contributes appendix text)

- The structure of v10 stays. Replace every placeholder with a measured
  number through `scripts/update_paper.py`; never by hand.
- Update names that were placeholders: backbone (Qwen3.5-9B), audited models
  with exact IDs, providers, access dates and reasoning settings (appendix).
- Rule-library counts, fold counts, seeds, set sizes: report what was built.
- Rewrite abstract, contribution list, Section 7 prose and conclusion from
  `docs/RESULTS_SUMMARY.md`. One sentence per primary comparison, including
  negative results, plus the scope sentence (stated rules; no clinical
  validation; selectivity on real notes tested only indirectly or untested).
- Remove any paragraph, row or figure whose result file does not exist
  (for example EHRNote-ChatQA, CondMedQA, step-error-data row), and remove
  its mention from abstract and limitations.
- API scoring differs from the draft (two-order choice instead of 32
  samples): update Appendix F "Readouts".
- Switch to `\placeholdersfalse` only when no `\ph{` remains; main text at
  most 8 pages; Limitations and Ethical Considerations after the conclusion.
