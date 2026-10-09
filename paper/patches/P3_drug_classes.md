# P3. Drug classes after the amendment of 9 Oct

Status: waits for approval of the wording. The decision itself is taken (docs/DECISIONS_D.md, 9 Oct; appended
line of docs/ANALYSIS_PLAN_STAGE2.md). Until this patch is applied the paper describes the first rule, which is
no longer what `cls_v1` is built with.

## Appendix E, "Class membership from open ontologies"

Now:
> ... it belongs to a class if the ATC fourth-level class and the FDA established pharmacologic class served
> by RxClass both contain it.

Proposed:
> ... it belongs to a class if it is a direct ingredient member of an FDA established pharmacologic class
> served by RxClass. We first required agreement with an ATC fourth-level class; that rule left 28 drug classes,
> 7 of them for test, and was replaced before the class set was built (Appendix~\ref{app:plan}). Classes on
> which both sources agree are marked, and results are also reported on them.

## Limitations, "Sources of criteria"

Now:
> class membership differs between drug classifications, so we keep a membership only where two sources agree

Proposed:
> class membership differs between drug classifications; we take one source, the FDA established
> pharmacologic classes, and report separately the classes on which a second source agrees

## Appendix A, stage-2 paragraph (one sentence added after the list of comparisons)

> The plan was amended once, on 9 October 2026 and before the class set existed: drug classes are taken from one
> source instead of the agreement of two, because the agreement rule left 7 drug classes for test; comparison
> (10) is otherwise unchanged and is also reported on the classes where both sources agree.

## Table of sources (`tab:onto`), row "Drug classes"

"ATC level 4 and FDA class through RxClass" becomes "FDA class through RxClass (direct ingredient members);
ATC level 4 for the agreement flag and for near-misses".

Counts (80 classes, 47 / 12 / 21; number with agreement) are filled from A's `data/onto_v1` manifest by key,
not typed.
