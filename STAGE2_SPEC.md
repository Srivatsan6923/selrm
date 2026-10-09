# Stage-2 spec (shared contracts)

Extends `docs/INTERFACES.md`. Role D files it as one change request and
merges it first. If you need something different, file a change request and
work around it; do not edit a contract locally.

## 1. Pinned sources
| Source | Pin | Licence | Check at download |
|---|---|---|---|
| MedCalc-Bench Verified | github.com/nikhilk7153/MedCalc-Bench-Verified, tag `v1.0.8`, commit `801592132bfd833f049b517a4e013e00a5fc40fa` | CC BY-SA 4.0 (data). Calculator code: no licence, not used | sha256 `test_data.csv` = `9d296b09668d945d7c4ad8136032e984a3a3b8b0a7b046eb0f9f787331d9d97d`; `train_data.csv` = `bd0292576be31e2fa8140c2e9eb456168335a85d1986155f010082d64f497845`; 1,100 test rows, 380 rule-based (230 Extracted, 150 Synthetic), 19 calculators |
| DDXPlus, English release | figshare record 22687585 (patients, `release_conditions.json`, `release_evidences.json`) | CC BY 4.0 | 49 conditions; 223 evidences (110 symptoms, 113 antecedents; 208 binary, 10 categorical, 5 multi-choice); 888 links (605 + 283). Record the sha256 of every file |
| MedEinst | huggingface.co/datasets/zhui711/MedEinst, revision recorded | CC BY 4.0 | test 10,766 rows (5,383 pairs); train 21,218 rows |
| Chia | figshare DOI 10.6084/m9.figshare.11855817.v2, `chia_with_scope.zip` | CC BY 4.0 | 1,000 trials, 12,409 criteria |
| Leaf Clinical Trials corpus | figshare DOI 10.6084/m9.figshare.17209610.v2; repo uw-bionlp/clinical-trials-gov-data, commit `62d54af` | CC BY 4.0 | 1,006 annotated documents |
| HPO, Mondo, Disease Ontology | release tag at download | HPO: free with attribution, no alteration; Mondo CC BY 4.0; DOID CC0 | tag and sha256 in the manifest |
| RxNorm ingredients, RxClass (ATC level 4, FDA EPC, MED-RT) | RxNav API; store `version.json`; cache every response | no licence needed; ATC class names are not redistributed | store ATC codes only; show FDA class names |

The sha256 values above are from a clone made on 8 Oct 2026; a mismatch is
reported, not worked around.

## 2. Sets
| Set | Owner | Portions | Bootstrap cluster |
|---|---|---|---|
| `mcv_v1` | A | `criteria_test`, `natural_band_test`, `edits_test`, `ruleside_test`, `dev`, `adapt_blocks`, `adapt_triplets` | note |
| `kb_v1` | A | `triplets_dev` (DDXPlus validation patients), `triplets_test` (test patients); renderer `selrm/kb_criterion.py` | patient; label pair for MedEinst |
| `onto_v1` | A | snapshot and closure tables, no records | n/a |
| `cls_v1` | A | `dev`, `test`; training classes live inside `rule_v2` | class |
| `reg_v1` | A | `dev` (10% of criteria, for the parser), `test` | trial |
| `rule_v2` | A | `train_blocks`, `train_triplets`, `dev`, `test_L2` | rule |
| `xp_v1` | A | program-preserving paraphrases of the rule text for 300 `rule_v1/test_L2` groups | rule |
| criterion views of `clin_v1/*` | C | `medeinst_test`, `keypairs_medqa`, TrialGPT test portion | as in stage 1 |

## 3. Record fields added to the canonical record
| Key | Meaning |
|---|---|
| `crit` | `{source: none|stated|derived|self|wrong, provenance, text_sha}`; `rule_text` holds the text shown, `""` for none |
| `cluster` | id used by the bootstrap (note, class, trial, label pair) |
| `note_type` | `human` (Extracted) or `model` (Synthetic); `mcv_v1` only |
| `stratum` | `stated`, `denied`, `default`; `mcv_v1` only (section 5) |
| `edit_type` | `value` or `sentence`; `mcv_v1/edits_test` only |
| `ref_date` | reference date of the case, ISO; window items only |
| `nm_kind` | adds `window` and `class` to the five existing kinds |
| `ledger` entries | `time` may carry a date, `past (2024-06)`; optional `concept: <ontology id>`; `applies: yes|no` |
| `struct` | reference structure of the criterion (thresholds, window, class id, scopes) from the program or annotation; never shown to a model |

Unchanged: every case carries both claims; `label` comes from code; ledger
and prose never state a decision.

## 4. Claims
| Set | `claim_type` | Wording |
|---|---|---|
| `mcv_v1` | `criterion` | "Under the <score name>, the item '<item name>' scores <k> point(s) for this patient." `s` has the points the rule code gives; `s_prime` the other value (binary items), the level the edit targets (edits), or the nearest other level (untouched notes). The item name is the item heading of the score text without comparators or numbers, so a claim never states a threshold |
| `kb_v1` | `conclusion` | the wording of `clin_v1/medeinst_test`: `s` names diagnosis A, `s_prime` diagnosis B |
| `cls_v1`, `rule_v2` | `conclusion`, `criterion` | as `rule_v1` |
| `reg_v1` | `criterion` | as the TrialGPT protocol: met / not met |

## 5. Criterion conditions
`scripts/crit_views.py --set <name> --cond <c>` writes a view: identical
records, `rule_text` replaced, iid suffix `@<c>`. Nobody edits prompts by
hand.

| Tier | none | stated / derived | self | wrong |
|---|---|---|---|---|
| `mcv_v1` | no score text; the claim names the score | score definition as shipped in the instance | definition written by the frozen backbone from the score name | definition of another score |
| `reg_v1`, TrialGPT | not defined (the claim is the criterion) | criterion text | not used | another criterion of the same trial and type |
| `cls_v1` | rule names the class, no member list (closed book) | rule plus member list from the release (open book) | not used | rule names a sibling class |
| `kb_v1`, MedEinst | no criterion | renderer output for the pair | pairwise criterion written by the backbone from the two diagnosis names | renderer output with the two lists exchanged |
| key pairs | no criterion | not defined | what must hold for each answer, written by the backbone from the option set without the vignette | the self-written text of another pair |
| `rule_v1`, `xr_v1` (controls) | rule text removed | rule text | not used | rule of another group |

Self-written texts are generated once (greedy, frozen backbone, prompt chosen
on the development portion), stored with a sha256 and frozen before scoring.

MedCalc-V strata: `stated` = the input's key is in the released dictionary
with a number or True; `denied` = key present with False; `default` = key
absent, settled by the benchmark's convention. Primary comparisons use
`stated` and `denied`.

## 6. Systems (`configs/adapters.json`)
| Name | What | Owner |
|---|---|---|
| `critic` | untrained backbone, verdict prompt | C |
| `verdict_blocks_s{0..4}`, `verdict_triplets_s{0..4}` | stage-1 adapters on `rule_v1` | B (exist) |
| `summary2_*`, `ledger2_*` | stage-1 two-stage adapters | B (exist) |
| `v2_verdict_blocks_s*`, `v2_verdict_triplets_s*` | verdict-only on `rule_v2` | B |
| `v2_reader_s*` | reader that writes the stage-2 record with the `applies` bit; one adapter with the judge prompts | B |
| `ledger_rm_g_s*` | composite of section 7 | B |
| `mix_blocks_s*`, `mix_triplets_s*` | adaptation arms (plan, secondary 4) | B |

## 7. Ledger-RM-G (composite) and the gate
```
if rule_text == "":                          # no criterion
    return v2_verdict_triplets(case, claim)  # abstain -> fallback
record = reader(case, rule_text, condition)
if malformed(record):                        # unparsable, or quotation not in the case
    return v2_verdict_triplets(case, rule_text, claim)
constraints = parse_criterion(rule_text, condition)
g = gate(record, constraints, case, ref_date, onto)
if g.applies is not None:                    # every constraint kind computable
    record.applies = g.applies
    return judge_blind(record, rule_text, claim)
return judge_case(record, rule_text, claim, case)   # bit stands, judge sees the case
```
- `parse_criterion(text, condition) -> list[Constraint]`, deterministic (no
  model): numbers with comparator and unit; windows ("within N
  days/months/years before <reference>"), scope words (ever, current,
  history of); class names by lookup in `onto_v1` labels; subject scope
  (patient; patient or first-degree relative); status scope.
- `gate(...)` returns `checks: {quotation, value, time, concept, subject,
  status}`, each `1`, `0` or `None` (not computable), and `applies`: the
  conjunction when every constraint kind found in the criterion has a check
  that is not `None`, otherwise `None`.
- Checks: quotation = string occurs in the case; value = comparison after
  unit conversion; time = date arithmetic against `ref_date`, boundary day
  as the criterion states; concept = mention linked to an `onto_v1` term and
  the term in the closure of the class; subject, status = set membership.
- Linking: retrieval over labels and synonyms of the snapshot (exact and
  normalised match, then an encoder), top 10, then the reader chooses one or
  abstains. Identifiers are never generated freely.
- Two reference variants are always reported next to the system:
  `gate_struct` (constraints taken from `struct` instead of the parser) and
  `reader_bit` (no gate).
- The stage-1 behaviour (a malformed record rejects both claims) stays the
  behaviour of the stage-1 systems. The fallback is part of Ledger-RM-G only.

## 8. Metrics (`selrm/metrics.py`, owner C)
Accuracy of the preferred claim, and for `mcv_v1/criteria_test` its balanced
form (mean over items that score points and items that score none); TA,
Rev, Hold; pair accuracy; XA; macro-F1
(TrialGPT); interaction contrasts for (8) and (11); non-inferiority for (12);
Holm over the family. New diagnostics: parser coverage and precision against
`struct`; gate coverage (share of items with `applies` computed); linking
accuracy and abstention; fallback rate; malformed rate. All with the cluster
of section 2.

## 9. Results
Layout unchanged: `results/<run_id>/{meta.json, scores_<set>.jsonl,
summary_<set>.json, DONE}`. Run ids: `<role>-S2-<set>-<system>-<cond>[-s<seed>]`.
Scores of a composite run also store `route` (`fallback_none`,
`fallback_malformed`, `gate`, `judge_case`) and the gate checks per item.
Summaries add the keys `note_type=`, `stratum=`, `edit_type=`, `cond=`,
`route=`.

## Amendment of 9 Oct 2026 (section 1, RxClass row; section 2, `cls_v1`)
Drug classes of `onto_v1` / `cls_v1` (comparison 10 and secondary analysis 10). Requested by role A
(docs/CHANGE_REQUESTS.md, 8 Oct) and accepted by the lead on the human lead's word, before `cls_v1` exists and
before any model has seen a class. The rule first written (a class is an ATC level-4 code and an FDA
established pharmacologic class that agree) gives 28 usable drug classes, 7 of them held out for test,
against 56 phenotype and 54 disease test classes. Amended rule: a drug class is an FDA established
pharmacologic class by its direct ingredient members, with at least 4 single ingredients that belong to no
other such class and at least 2 near-miss ingredients under role A's near-miss rule of 8 Oct
(docs/DECISIONS_A.md); 80 classes, 47 / 12 / 21 train / dev / test. Every class carries
`agreement = true|false` (its members also match one ATC level-4 code under the first rule).
Consequences, fixed now: comparison (10) is computed on all held-out test classes under the amended rule;
its metric, contrast, cluster and decision rule are unchanged. The same contrast on the classes with
`agreement = true` (the definition first written) is reported next to it as a secondary analysis, and the
paper states both definitions and that the amendment preceded the data. No new source or licence; ATC names
are still not redistributed.
