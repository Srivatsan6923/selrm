"""Error-analysis sheets for the authors (FINAL_TASKS_D P0.4; coded in HUMAN_TASKS H4).

Draws 200 rule_v1/test_L2 triplets that trained systems (seed 0) fail, stratified by
system x near-miss kind, and deals them into four parts of 50:
  python scripts/error_sheet.py
writes audit/error_sheet.csv, audit/error_sheet_part1.csv .. part4.csv and
audit/ERROR_CODING.md. Inputs are frozen (records hash checked against
data/REGISTRY.json; finished runs), so every rerun writes the same bytes."""
import collections, csv, hashlib, json, os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from selrm.formats import MALFORMED_U
from selrm.metrics import _flags, decisions          # the triplet definition (TA; ties fail)
from selrm.prompts import ledger_to_text

SET = "rule_v1/test_L2"
RUNS = ("B-F-ledger2-blocks-s0", "B-F-ledger2-triplets-s0", "B-F-summary2-triplets-s0",
        "B-F-verdict-blocks-s0", "B-F-verdict-triplets-s0")
KINDS = ("boundary", "negation", "numeric", "subject", "time")
PER_STRATUM, PARTS = 8, 4
TOTAL = PER_STRATUM * len(RUNS) * len(KINDS)
CASES = ("base", "flip", "near")
CODING = ("category", "subcategory_or_note", "coder", "second_coder_category", "agreed")
OUT = f"{ROOT}/audit"


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def deal(n, keys, room):
    """n units given one at a time, round robin over keys (in order) that still have room."""
    got = dict.fromkeys(keys, 0)
    while n and any(got[k] < room[k] for k in keys):
        for k in keys:
            if n and got[k] < room[k]:
                got[k], n = got[k] + 1, n - 1
    return got


def system(meta):
    return f"{meta['format']} x {meta['corpus'].removeprefix('rule_v1/train_')}"


def write_csv(name, rows):
    with open(f"{OUT}/{name}", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")   # LF, as the repo stores text
        w.writeheader()
        w.writerows(rows)


def table(head, body):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] +
                     ["| " + " | ".join(map(str, r)) + " |" for r in body])


def main():
    reg = json.load(open(f"{ROOT}/data/REGISTRY.json", encoding="utf-8"))[SET]
    src = {SET: f"data/{reg['path']}"} | {r: f"results_git/{r}/scores_{SET.replace('/', '~')}.jsonl" for r in RUNS}
    sha = {k: sha256(f"{ROOT}/{p}") for k, p in src.items()}
    assert sha[SET] == reg["sha256"], "records differ from data/REGISTRY.json"
    recs = [json.loads(l) for l in open(f"{ROOT}/{src[SET]}", encoding="utf-8")]
    conc = {(r["tid"], r["case_kind"], r["claim_role"]): r for r in recs if r["claim_type"] == "conclusion"}

    S, T, meta, avail = {}, {}, {}, {}
    for run in RUNS:
        assert os.path.exists(f"{ROOT}/results_git/{run}/DONE"), run
        meta[run] = json.load(open(f"{ROOT}/results_git/{run}/meta.json", encoding="utf-8"))
        S[run] = {x["iid"]: x for x in map(json.loads, open(f"{ROOT}/{src[run]}", encoding="utf-8"))}
        T[run] = decisions(recs, [S[run][r["iid"]]["u"] for r in recs])
        assert {t["nm_kind"] for t in T[run].values()} == set(KINDS)
        for k in KINDS:
            avail[run, k] = sorted(i for i, t in T[run].items() if t["nm_kind"] == k and not _flags(t)["TA"])

    # Allocation: 8 per stratum; a system's shortfall goes round robin to its other kinds, what it
    # cannot fill goes round robin to the other systems (and inside each, round robin over kinds).
    n_fail = {r: sum(len(avail[r, k]) for k in KINDS) for r in RUNS}
    quota = {r: min(PER_STRATUM * len(KINDS), n_fail[r]) for r in RUNS}
    more = deal(TOTAL - sum(quota.values()), RUNS, {r: n_fail[r] - quota[r] for r in RUNS})
    take = {}
    for r in RUNS:
        first = {k: min(PER_STRATUM, len(avail[r, k])) for k in KINDS}
        extra = deal(quota[r] + more[r] - sum(first.values()), KINDS, {k: len(avail[r, k]) - first[k] for k in KINDS})
        take |= {(r, k): first[k] + extra[k] for k in KINDS}
    rng = random.Random("error-sheet-v1")
    picked = [(r, k, tid) for r in RUNS for k in KINDS for tid in sorted(rng.sample(avail[r, k], take[r, k]))]
    assert len(picked) == TOTAL
    order = [(p + 1, x) for p in range(PARTS) for x in picked[p::PARTS]]       # dealt round robin into parts

    rows = []
    for n, (part, (run, kind, tid)) in enumerate(order, 1):
        t, d = T[run][tid], T[run][tid]["d"]
        failed = [c + (" (tie)" if d[c] == 0 else "") for c, ok in
                  (("base", d["base"] > 0), ("flip", d["flip"] < 0), ("near", d["near"] > 0)) if not ok]
        assert failed and not _flags(t)["TA"], (run, tid)
        rec = {c: conc[tid, c, "s"] for c in CASES}
        row = {"sheet_id": f"E{n:03d}", "part": part, "system": system(meta[run]), "run_id": run, "tid": tid,
               **{k: t[k] for k in ("rid", "family", "nm_kind", "tier", "level")},
               "failed_conditions": "; ".join(failed),
               **{f"d_{c}": d.get(c, "") for c in CASES + ("pres",)},
               "rule_text": rec["base"]["rule_text"], "condition": rec["base"]["condition"],
               "claim_s": rec["base"]["claim_text"], "claim_s_prime": conc[tid, "base", "s_prime"]["claim_text"],
               **{f"case_text_{c}": rec[c]["case_text"] for c in CASES},
               **{f"gold_ledger_{c}": ledger_to_text(rec[c]["ledger"]) for c in CASES},
               **{f"reader_output_{c}": S[run][rec[c]["iid"]].get("reader_output", "") for c in CASES},
               "near_meta": json.dumps(rec["near"]["meta"], sort_keys=True, ensure_ascii=False),
               **dict.fromkeys(CODING, "")}
        # a text cell starting with = + - @ would be read as a formula by Excel
        assert not any(isinstance(v, str) and v.startswith(("=", "+", "-", "@")) for v in row.values()), row["sheet_id"]
        rows.append(row)

    os.makedirs(OUT, exist_ok=True)
    write_csv("error_sheet.csv", rows)
    for p in range(1, PARTS + 1):
        part_rows = [r for r in rows if r["part"] == p]
        assert len(part_rows) == TOTAL // PARTS
        write_csv(f"error_sheet_part{p}.csv", part_rows)

    sysname = {r: system(meta[r]) for r in RUNS}
    n_kind = collections.Counter(t["nm_kind"] for t in T[RUNS[0]].values())
    systems_table = table(
        ["system", "run_id", "format", "training corpus", "base model", "failed triplets", "triplets"],
        [[sysname[r], r, meta[r]["format"], meta[r]["corpus"], meta[r]["model"], n_fail[r], len(T[r])] for r in RUNS])
    strata_table = table(
        ["system"] + list(KINDS) + ["all"],
        [[sysname[r]] + [f"{take[r, k]} / {len(avail[r, k])}" for k in KINDS] +
         [f"{sum(take[r, k] for k in KINDS)} / {n_fail[r]}"] for r in RUNS] +
        [["all"] + [f"{sum(take[r, k] for r in RUNS)} / {sum(len(avail[r, k]) for r in RUNS)}" for k in KINDS] +
         [f"{len(picked)} / {sum(n_fail.values())}"]])
    per_part = collections.Counter((p, x) for p, (r, k, _) in order for x in (sysname[r], k))
    parts_table = table(["part", "rows"] + [sysname[r] for r in RUNS] + list(KINDS),
                        [[p, sum(q == p for q, _ in order)] + [per_part[p, sysname[r]] for r in RUNS] +
                         [per_part[p, k] for k in KINDS] for p in range(1, PARTS + 1)])
    files_table = table(["input", "path", "sha256"],
                        [["records" if k == SET else f"scores, {k}", f"`{p}`", f"`{sha[k]}`"] for k, p in src.items()])
    kinds_n = ", ".join(f"{k} {n_kind[k]}" for k in KINDS)
    with open(f"{OUT}/ERROR_CODING.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(DOC.format(TOTAL=TOTAL, PARTS=PARTS, PER_PART=TOTAL // PARTS, N_SYS=len(RUNS), N_KINDS=len(KINDS),
                           PER_STRATUM=PER_STRATUM, N_TRIP=len(T[RUNS[0]]), KINDS_N=kinds_n, MALFORMED_U=MALFORMED_U,
                           N_DISTINCT=len({tid for _, _, tid in picked}),
                           LAST_P1=f"E{TOTAL // PARTS:03d}", LAST=f"E{TOTAL:03d}", SET=SET,
                           systems_table=systems_table, strata_table=strata_table, parts_table=parts_table,
                           files_table=files_table))
    print(strata_table)


DOC = """# Error coding of trained-system failures (HUMAN_TASKS H4)

Generated by `python scripts/error_sheet.py`, which rewrites this file and the sheets
byte for byte from the inputs listed at the end. Change the script, not these files.

## What the sheet is

Each of the {TOTAL} rows of `audit/error_sheet.csv` is a triplet of `{SET}` that one
of {N_SYS} trained systems failed ({N_DISTINCT} distinct triplets; a triplet can appear once
per system). `{SET}` holds rules of signature classes held out from training
(level L2). A triplet is solved when the system prefers the correct conclusion claim
in all three cases: d(base) > 0, d(flip) < 0 and d(near) > 0, where
d = u(s) - u(s_prime), u = logit("+") - logit("-") at the answer position, s is the
claim that is correct on base and near and s_prime the claim that is correct on flip.
A tie (d = 0) is a failure. Every failure is recomputed from the per-example scores
with `selrm.metrics.decisions` (conclusion claim). `audit/error_sheet_part1.csv` to
`audit/error_sheet_part{PARTS}.csv` hold the same rows in {PARTS} parts of {PER_PART}, one part per
author.

Systems (seed 0; each scored on the same {N_TRIP} triplets, by near-miss kind: {KINDS_N}):

{systems_table}

- verdict: one stage. The model reads the rule, the case and one claim and answers + or -.
- ledger2: two stages. A reader writes an evidence ledger for the condition under test
  (one entry per relevant mention, fields need, found, subject, status, time); a judge
  sees the rule and this ledger, not the case, and answers + or - for each claim.
- summary2: the same two stages, with a plain-prose summary in place of the ledger.
- blocks corpus: base and flip cases of every training group (some groups also give a
  presentation edit or a missing-input case), no near-miss cases. triplets corpus: as
  blocks, but 7 of every 14 groups give the near-miss case in place of the base case
  (`docs/DATA_A.md`).
- ledger2 only: a reader output that was cut off or is not a well-formed ledger (entries
  without exactly the five fields in order, or a found that is neither "not mentioned"
  nor a verbatim substring of the case; `selrm/formats.py`, `well_formed`) is not shown
  to the judge. Both claims then get u = {MALFORMED_U}, so d = 0, a tie.

The flip and near cases each differ from the base case in one line (`selrm/engine.py`).
Near-miss kinds (the near case keeps the label of the base case):
- numeric: the target value is close to the threshold, on the side that does not count.
- boundary: the target value is exactly at a strict threshold (50 under "below 50"),
  so it does not count.
- subject: the finding is stated for a person whose history the rule does not count.
- negation: the case names the finding and states that it is absent.
- time: the finding is past or resolved where the rule needs it current (tier
  delabelled: an allergy label removed after testing); for a measured value, an earlier
  value lies on the counting side while the current value does not count.

Tiers: easy; long (15 to 20 filler lines); superseded (an earlier measurement replaced
by today's); delabelled (an allergy label removed after testing).

## Sampling

1. The failed triplets of a system are those with TA false in `selrm.metrics`.
2. Strata are system x near-miss kind ({N_SYS} x {N_KINDS}); the target is {PER_STRATUM} triplets per
   stratum, {TOTAL} in all.
3. A stratum with fewer failures gives all it has. The system's shortfall goes, one
   triplet at a time, round robin to its kinds that have failures left (kinds in
   alphabetical order). What a system cannot fill goes the same way to the other
   systems that have failures left (run ids in alphabetical order), and inside each
   of them round robin over its kinds.
4. Within each stratum the triplets are drawn with
   `random.Random("error-sheet-v1").sample` from the sorted list of failed triplet ids;
   one generator, strata in sorted order (run id, kind).
5. Parts: the rows, sorted by (run id, kind, tid), are dealt round robin (row 1 to
   part 1, row 2 to part 2, ...). sheet_id numbers the rows part by part (E001 to
   {LAST_P1} are part 1, up to {LAST}).

Sampled / failed triplets per stratum:

{strata_table}

Rows per part, by system and by near-miss kind:

{parts_table}

## Columns

| column | content |
|---|---|
| sheet_id | row key; keep it unchanged, it is used to merge the coded files |
| part | part 1 to {PARTS} |
| system, run_id | format x training corpus; the run directory in `results_git/` |
| tid, rid, family | triplet id, rule id, structural family of the rule (not the signature class: the held-out unit of L2 is the signature class, which this sheet does not show, and every test_L2 family also occurs in training) |
| nm_kind, tier, level | near-miss kind, tier, ladder level |
| failed_conditions | the cases with a wrong preference: base if d_base is not above 0, flip if d_flip is not below 0, near if d_near is not above 0; "(tie)" marks d = 0 |
| d_base, d_flip, d_near, d_pres | d on the conclusion claim in each case; pres is the presentation edit of the base case (same state: numeric lines re-templated, a new header, lines reordered; finding lines keep their text; not part of the triplet test) |
| rule_text, condition | the stated rule; the condition under test (what the reader is asked about) |
| claim_s, claim_s_prime | the two conclusion claims |
| case_text_base, case_text_flip, case_text_near | the case notes |
| gold_ledger_base, gold_ledger_flip, gold_ledger_near | the program's evidence ledger for the condition (`selrm.prompts.ledger_to_text`); the ledger2 reader is trained to write it, the summary2 reader states the same evidence in sentences |
| reader_output_base, reader_output_flip, reader_output_near | what the system's reader wrote (ledger2, summary2); empty for verdict |
| near_meta | record meta of the near case: templates used (meta.tpl, bank/form/index), keywords, seed |
| category, subcategory_or_note, coder, second_coder_category, agreed | coding columns, empty |

## Categories

Code one category per row: the main reason the system failed the triplet. If several
conditions failed for different reasons, code the first one listed in
failed_conditions and describe the others in subcategory_or_note. Check in this order:
was a fact of the case misread (extraction error or unseen wording)? If not, was a
correctly read mention wrongly counted or not counted (applicability error)? If not,
was the rule itself applied wrongly (rule misread)? Otherwise, other. The examples
below were written for this guide; they are not taken from the sheet.

- **extraction error**: a fact of the case was read wrongly although it is worded in
  an ordinary way. The system missed the target mention, found one that is not there,
  or took the wrong value, person (subject), status (present or absent) or time from
  the text. In ledger2 and summary2 this shows as a reader output that disagrees with
  the gold ledger. Example: the case says "Platelet count this morning: 30" and the
  reader writes "found: not mentioned" although the case gives the platelet count.
- **applicability error**: the facts were read correctly, but the system misjudged
  whether the mention counts for this patient under the rule. It counted a finding of
  a person the rule does not cover (or ignored a relative the rule covers), counted a
  past or resolved finding where the rule needs a current one (or ignored a past
  finding the rule counts), or counted a finding the case states as absent. Example:
  the ledger correctly gives "subject: brother" for a stroke, the rule counts only the
  patient's own strokes, and the system still treats the stroke as counting.
- **unseen wording**: a fact was misread because of how the case words it: a phrasing,
  cue word or person name. In `selrm/phrases.py` every list of templates and of
  negation and time cue words and person names is split four to two within each
  block of six entries: training corpora use the four (`templates: train` in their
  MANIFEST.json), test cases the two, so no test wording occurs in training. Use
  this category only when you judge that the same fact in plainer wording would
  probably have been read correctly, and quote the wording in subcategory_or_note.
  Example: a past finding is marked with a time cue that training never used, and
  the reader records the finding as current.
- **rule misread**: the facts and their applicability are right, but the system applies
  a different rule from the stated one: a wrong threshold or direction, a strict
  threshold read as inclusive, the wrong combination of criteria (any of, all of, two
  of three), wrong points or cut-off in a score rule, or usual clinical practice in
  place of the stated rule. Example: the rule says "below 50", the case gives exactly
  50, and the system treats the value as below 50.
- **other**: none of the above, or the cause cannot be told from the row (say why).
  Use it also when you think the gold label or the case text is wrong or ambiguous,
  and begin the note with "data problem:" so these rows can be found and checked.

The verdict systems show no reader output, so the step that failed cannot be seen.
Code the most likely cause from the case texts, the gold ledgers and the failed
condition; when you cannot choose, code other and say so in the note.

## How to code

1. The lead assigns one part to each author. Open `audit/error_sheet_part<k>.csv` in
   Excel or LibreOffice (UTF-8 with a byte-order mark, which Excel detects). Wrapping
   text in the long columns helps.
2. For each row read rule_text, condition, claim_s and claim_s_prime and
   failed_conditions; then the case texts and gold ledgers of the failed condition and
   of a condition the system got right; for ledger2 and summary2 also the reader
   output (the judge saw only that text and the rule).
3. Fill category with exactly one of: extraction error, applicability error, unseen
   wording, rule misread, other. Write a short reason in subcategory_or_note (the field
   that was misread, the wording, the rule clause). Write your name in coder.
4. Change no other column, and do not add, remove or reorder rows.
5. Save as CSV UTF-8 (comma delimited) under `audit/errors_<name>.csv`, with your name
   in place of `<name>` (HUMAN_TASKS H4).
6. second_coder_category and agreed are for rows coded twice, chosen by the lead. To
   code blind, the second author works on a copy of the part made before the first
   coder starts (or with category, subcategory_or_note and coder cleared); the lead
   then copies the second category into second_coder_category and sets agreed to y
   when the two categories match, n otherwise.

## Inputs

{files_table}

The records hash equals the `{SET}` entry of `data/REGISTRY.json` (the script stops
otherwise). The records file is not in git: on a fresh clone rebuild it first
(`python scripts/build_rule_v1.py --out <dir>`, then copy `<dir>/rule_v1/test_L2/records.jsonl`
to `data/rule_v1/test_L2/`). Regenerate with `python scripts/error_sheet.py` (Python 3.11 or later).
"""


if __name__ == "__main__":
    main()
