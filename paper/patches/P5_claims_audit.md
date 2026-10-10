# P5. Wording that the statement-level audit contradicts

Status: waits for approval. Source: `docs/CLAIMS_AUDIT_V14.md` (409 statements; 28 contradicted, 82 partly true),
every row with its evidence in `docs/CLAIMS_AUDIT_V14.csv`. Status notes and table cells that were merely stale are
already corrected from the files. The items below change what a sentence claims. They are ordered by how much a
reviewer would care; each gives the current claim, what the files show, and the proposed wording.

## A. Results stated more strongly than the files support

1. **TrialGPT, Section 6.4 and comparison (6a).** "the systems trained on triplets have a higher macro-F1 than
   the backbone (69.1-70.8 against 65.7)". True at seed 0 only. Five seeds exist: Ledger-RM on triplets 69.1,
   69.3, 66.6, 53.4, 63.3 (mean 64.3, below the backbone); summary 66.5; verdict 69.8. Proposed: report the
   five-seed means and say that the sign of the difference for Ledger-RM is not stable across seeds; keep
   "not established". Comparison (6a) stays as registered (seed 0) with the five-seed mean next to it.
2. **"Where the criterion is implicit, training on rules changes nothing or does harm"** (Section 6.4; the
   conclusion's "unchanged on benchmarks that state none"; Limitations, Transfer). True for MedEinst and key
   pairs. On NLI4CT-P, which Tables 1 and 4 list under "no criterion stated", the verdict-only models score
   85.6 and 85.4 against 80.9 (one seed, no test). Proposed: name the two benchmarks, and say that on NLI4CT-P
   the verdict-only models are higher at one seed, untested.
3. **"Near-miss supervision has to cover each condition"** (Section 6.2; Limitations, rule language). Shown
   for the verdict-only model on three kinds at seed 0 (7.0 / 60.2 / 49.8), and the seeds differ widely
   (subject 7.0 / 12.3 / 51.5; boundary 49.8 / 23.0 / 16.8). The prose record largely extends to uncovered
   kinds (subject 84.5-91.8; boundary 99.0 / 99.0 / 70.5), and negation was not run. Proposed: restrict to the
   verdict-only model, give the seed range, and state that the two-stage formats extend further.
4. **"Without near-misses the failures are concentrated where the finding belongs to another person or the
   value sits on the threshold"** (Section 6.2). True for verdict-only; in the other formats past findings are
   as bad or worse (rationale 20.5, summary 27.9, ledger 42.7 on the time kind). Proposed: "for the
   verdict-only model".
5. **"because a field that says 'current' or 'past' cannot carry a date"** (Section 6.3, window items: bit
   reader 91, ledger 68). The explanation is not supported: the prose record, which has no such field, scores
   54-71. Proposed: drop the "because" clause, or mark it as a conjecture.
6. **"the two-stage formats 98.0% and 99.2%"** (Section 6.2). The value ledger, the third two-stage format of
   Section 5, is at 85.7. Proposed: "the prose and typed-ledger formats".
7. **"self-consistency is the best selector"** (Section 6.6). On MedQA, CareQA and key pairs; on the MedEinst
   pool it is the lowest (20.6) and the ledger score the highest (26.2). Proposed: "on exam questions".
8. **Abstract and introduction: "accuracy falls from 88.0% to 38.7%"** for the policy trained against Med-PRM.
   Seed 0; seed 1 is 89.3 to 54.7. Proposed: "at seed 0", or the two-seed range.
9. **"Windows are the weakest clause for every trained system that does not write a decision bit
   (43-76%)"** (Appendix H) and **"the clause on which every current system is weakest"** (Appendix E). True
   for the triplet-trained verdict, prose and ledger runs; false for several blocks-trained runs, the value
   ledger and the released PRMs. Proposed: "for the systems trained on triplets".
10. **"The gain from near-misses is established for items of 19 clinical scores"** (Limitations). 19 scores are
    in the set; comparison (7) covers 14 of them on human-written notes and (9) covers 13, with unadjusted p.
    Proposed: the two counts, and "unadjusted".

## B. Descriptions of the method or data that do not match what was built

11. **Rule derivation** (Section 5, Appendix B): "compiled from public recommendations by the tree-then-program
    procedure ... a model extracts the recommendation, writes it as a decision tree, and compiles the tree". No
    such pipeline exists. The 60 constraint rules were written directly as programs, 54 simplified from a
    source and 6 synthetic; the other rules are grammar-sampled. Proposed: say exactly that.
12. **Gate checks** (Appendix F table): "value: comparison after unit conversion" (the code converts no units);
    "subject, status: not computable when the scope is not stated" (the implemented gate uses defaults: the
    patient, present, current; role B asked for this rewording on 9 Oct). Proposed: B's wording.
13. **Sources table** (Appendix E): RxNorm "prescribable subset" (the general API is used); "openFDA and
    DailyMed label sections" (not used); "MED-RT contraindication assertions used only in the positive
    direction" (not used at all); Disease Ontology "as fallback" (downloaded, never read). Proposed: list only
    what is used.
14. **Clinical-pairs model** (Appendix D): described as trained on 7,807 MedEinst reference pairs and 122 key
    pairs. The held-out-disease runs train on 3,145 MedEinst pairs and no key pairs; three seeds exist (pair
    accuracy 7.8 / 43.5 / 48.7; trap accuracy 97.4 / 95.7 / 94.8). Proposed: the correct corpus, three seeds,
    "about 95%".
15. **"Every case reports the same fields with raw values, so the presence of a field carries no label
    information"** (Appendix B). True for measured inputs. The decisive finding is never named in the base
    case and is named in flip and near-miss (by design: both of those name it, which is what makes the
    near-miss a control). Proposed: state it for measurements, and state the design for findings.
16. **"a past mention carries a year"** (Appendix C). 8,117 of 13,591 do. Proposed: "may carry a year".
17. **"near-misses that differed from the flip in more than one attribute were removed"** (Appendix B). Only
    subject near-misses were aligned; 670 of 2,180 negation near-misses still differ in more than status.
18. **"Most judgments concern one condition of one rule"** (Limitations, Appendix B). One criterion is edited
    per group, but the conclusion needs 1.8 (train) and 2.5 (L2) conditions on average; single-condition
    judgments are 42% and 17%.
19. **"The frozen library has no time windows"** (Limitations, Section 6.4, Appendix C). No program has one; one
    rule text (a falls-risk score, "in the six months before this admission") names one, in 12 L2 groups.
20. **MedCalc-V description** (Appendix E): the two-model fidelity filter (1,636 of 1,787 test triplets kept) is
    not mentioned; strata come from the released entity dictionary, not from the note text; 504 of 1,636 edit
    groups are on model-written notes. Registered criteria: 190 and 331 are candidates, 404 pass the model
    check, 374 are in the test portion.
21. **"All trained models use Qwen3.5-9B ... on 60,000 records"** (Section 5). True for the factorial; the
    exceptions are the 4B backbone runs, the verification-pass run (70,000), the pairwise run, the diversity
    runs and the policy.
22. **"Every number in this paper is produced by a script"** (Appendix K). About 270 verified numbers are still
    typed (intervals recomputed from scores, counts written as words, a few sums). Proposed: "every table and
    1,200 of the numbers in the text are printed from result files by key; the others are listed with their
    source in the repository".

## C. Stage-1 plan, as described

23. **"Stage 1 (fixed before any test set was scored)"** (Appendix A). Comparisons (1)-(5) predate the first
    scores; comparison (6) first appears in the draft after the first seed-0 L2 scores, though before any
    external result. The joint decision rule on (4) and (6) dates from that later version. Proposed: say so.
24. **Development history** (Appendix J): three statements have no repository record (that presentation edits
    were added later; that the "three expectations" were expectations of a first plan; "balanced outcomes would
    teach reversal", where the files show balanced corpora do teach reversal and fail on holding). These are
    the authors' to confirm from their own records or remove (H6).

## D. Statements with data that the paragraph does not yet draw on

- Appendix E, "what would count against us": on MedCalc-V edits the order is triplets 96.0, backbone 88.9,
  blocks 64.6, and comparison (8) includes zero. The paragraph still reads as a prediction.
- Scale (Appendix H): "the other cells are not run, so we draw no conclusion about scale". Three 4B cells are
  done at seed 0 (ledger blocks 50.3 against 75.3 for 9B; ledger triplets 99.2 against 99.2; verdict triplets
  91.3 against 91.3).
- Eligibility slice of NLI4CT-P (Appendix D, red): values exist (critic 80.3, verdict blocks 83.5, verdict
  triplets 81.7, Ledger-RM triplets 71.5).
