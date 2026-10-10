# G4, outcome "holds": comparisons (7)-(12) meet the expectations of the plan

Prepared before any stage-2 result exists. Applied only after approval (H-S2-5). Keys: `cmp/p7` ... `cmp/p12`
(fields `diff`, `lo`, `hi`, `padj`), filled from C's comparison file. Wording is plain on purpose; the authors
polish it (H6) without changing what it claims.

## 1. Abstract

Replace
> ... execute the parts of applicability that are executable, and report transfer over absent, stated, derived
> and wrong criteria (not yet run).

with
> ... and execute the parts of applicability that are executable. On clinical notes with a published score
> definition, the verifier trained with near-misses is \res{cmp/p7/diff} points above the one trained on
> decisive edits alone on criterion claims and \res{cmp/p9/diff} points above it on edited notes, and its
> advantage over the untrained backbone depends on the criterion being stated (\res{cmp/p8/diff} points).

Length: about one line longer. Proposed removal in the abstract: "taken from published score definitions,
registered eligibility criteria, a diagnostic knowledge base and open ontologies," (the list is in Section 3).

## 2. Introduction, contribution (3), last sentence

Replace
> ... to be evaluated on real clinical text with stated rules and released labels (Section 6.5; not yet run).

with
> On real clinical notes with stated score definitions and released labels, the ordering of the rule tier
> reappears, and removing or exchanging the criterion lowers the trained verifier more than the backbone
> (Section 6.5).

## 3. Section 6.5 (replaces the whole subsection body)

> If selectivity is relative to a criterion, three things should hold, and each could have failed.
>
> **Stated criterion, clinical notes.** On \mcv{} criterion claims over human-written notes the verifier
> trained on triplets is above the one trained on blocks by \res{cmp/p7/diff} points of balanced accuracy
> [\res{cmp/p7/lo}, \res{cmp/p7/hi}], and by \res{cmp/p9/diff} points of triplet accuracy on edited notes
> [\res{cmp/p9/lo}, \res{cmp/p9/hi}] (Table~\ref{tab:mcv}). The ordering of the rule tier on criterion claims
> reappears: triplets above the backbone, blocks below it.
>
> **The criterion is read.** Stating the score definition helps the trained verifier by
> \res{cmp/p8/diff} points more than it helps the backbone [\res{cmp/p8/lo}, \res{cmp/p8/hi}], and a wrong
> definition lowers it (Table~\ref{tab:ground}).
>
> **Derived criterion.** [if G2 passed] The symbolic executor decides
> \res{sum/C-S2-executor/test.both_decided} of the MedEinst pairs and is right on
> \res{sum/C-S2-executor/test.pair}; with the derived criterion the trained verifier gains
> \res{cmp/p11/diff} points more than the backbone [\res{cmp/p11/lo}, \res{cmp/p11/hi}].
> [if G2 failed: the block "(11) dropped" of `G4_fails.md`.]
>
> **Executable parts.** On classes held out from training the gate is \res{cmp/p10/diff} points above the
> learned verdict [\res{cmp/p10/lo}, \res{cmp/p10/hi}]. With no criterion the composite abstains and falls
> back to its verdict-only score; on key pairs it is within the margin of the verdict-only verifier
> (\res{cmp/p12/diff} [\res{cmp/p12/lo}, \res{cmp/p12/hi}]; margin $-2$).
>
> All six comparisons are Holm-corrected as one family (Table~\ref{tab:stage2}).

Length: the current subsection is 20 lines; this text is about 26. Proposed removal: the paragraph
"By the decision rule fixed in advance ... unchanged where none does." at the end of Section 6.4 shortens to
its first sentence (the second is now shown by Section 6.5).

## 4. Conclusion, last sentence

Replace
> Whether this carries onto clinical text is the experiment of Section 6.5 (not yet run).

with
> On clinical notes with a published score definition the same ordering holds, and it depends on the
> criterion being stated.

## 5. Limitations, "Transfer"

Replace the paragraph with
> The verifiers trained on rules do not improve agreement with any clinical benchmark that leaves its
> criterion implicit. Where a criterion is stated on clinical text the gain is established on score items
> from \res{sum/A-S2-mcv_v1/n_scores@int} calculators and \res{sum/A-S2-mcv_v1/n_human_notes@int}
> human-written notes; it is a result about single criteria with numeric or categorical inputs, not about
> clinical reasoning at large.
