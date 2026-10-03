# challenge_v1: writing guide (H2)

You write short patient notes from fact lists, in your own words. A program decides the correct
answer from the facts, so a note is correct when it states exactly the listed facts: no more, no
fewer, nothing ambiguous. Do not look at generated cases (`data/`, `docs/SAMPLE_TRIPLETS.md`, the
H1 sheets in `audit/h1/`, `ec_v1/SIGNOFF_CASES.md`) before you have finished writing. **Write your
H2 notes before you start H1 or H3**, which show generated cases.

## What you write for each group

Your form `challenge_v1/form_<authorN>.md` has 40 groups. Save it as
`challenge_v1/notes_<authorN>.md`, with your assigned id (author1 to author4) and not your name,
and fill in the fields after the colons.

| Field | What to write |
|---|---|
| `header` | One line with the patient's age and sex as given, e.g. "Woman, 54.", "54F" or "Boy, 16." (only the sex when the form says "adult"). |
| `reason` | The reason for the visit, in your own words. Keep its medical content and add nothing that a rule could use. |
| `fact N` | One line that states fact N, and only fact N. |
| `extra` | Optional: one unrelated line, such as a hobby or living situation. It must not name any condition or measurement of the rule. Repeat the field for more lines, at most three. |
| `FLIP` | The one line that replaces (or is added to) the base note, as the form says. |
| `NEAR` | The same for the near-miss. |
| `check_ok`, `check_comment` | Left empty by you. Your second author fills them in. |

The note for each case is assembled from your lines:
- **base:** header, reason, the facts, the extras;
- **flip and near-miss:** the base with exactly one line replaced or added.

So FLIP and NEAR must make sense in place of the line they replace.

Some scenarios are clinically odd by design (for example, a request for contraception at 78).
Write them as given.

## Rules

1. **State each fact exactly.**
   - Write values and years exactly as given. "creatinine 2.4 mg/dL" may also read "Creatinine
     today: 2.4 mg/dL".
   - The value is the first number after the name: write "Creatinine 2.4 mg/dL", not "Creatinine
     1.1, up from 2.4".
   - Keep the unit.
2. **Current and past.**
   - "Now" or "the current value" must read as current.
   - A fact that the form marks as over or resolved must say so in words: resolved, no longer,
     outgrown, stopped, in remission. A date or "years ago" alone is not enough.
   - Any other past fact needs its date, or "years ago" when the form gives no date.
   - An earlier measurement must read as earlier than today's value.
3. **Who.** A fact about a relative names that relative ("Her father ..."), and the relative is the
   one with the condition, not the informant: "His wife has new confusion", never "His wife reports
   new confusion". A fact about the patient names no one else ("as a child" is fine).
4. **Denials.** "Explicitly does not have X" must be a clear denial that names X: "No X", "Denies
   X", "Non-X", "X absent".
5. **Not mentioned means absent.** The base note must not mention the condition under test at all,
   not even to deny it, when the form says so. Anything not listed is simply not mentioned.
6. **Required words.** Every line that mentions the condition under test must contain one of the
   words the form lists, as a word or as the start of a longer word: 'diabet' is matched by
   "diabetes" and "diabetic", 'bp' by "BP".
7. **The rule stays out of the note.** Do not mention the rule, a decision, a drug choice or a
   threshold. Do not hint at what matters.
8. **Plain clinical English.** Use short lines, the abbreviations a clinician would use (except in
   lines about the condition under test, which must use one of the form's listed words), and no
   copied phrasing from anywhere else.

## Example (a rule that is not in the set)

> Rule: For a dry cough, prescribe dextromethorphan. If the patient currently has asthma or the
> current respiratory rate is above 24/min, prescribe an inhaled bronchodilator instead.
>
> Patient: 37-year-old male. Reason: dry cough for five days.
> fact 1: respiratory rate: 18/min, the current value
> Do not mention asthma in the base note at all, not even to deny it.
> FLIP: one line that is added to the base note, stating: the patient has asthma now.
> NEAR-MISS: one line that is added to the base note, stating: the patient's uncle has asthma now.

```
header: Man, 37.
reason: Five days of a dry, tickly cough.
fact 1: Respiratory rate 18/min.
extra: Works as a bus driver.
FLIP: Has asthma.
NEAR: His uncle has asthma.
check_ok:
check_comment:
```

Each line states its fact and nothing more. The respiratory rate is named and the unit kept; the
flip names no treatment, since a treatment could hint at the rule's alternative.

## What the assembler checks

The assembler reports any of the following, so fix and re-run.
- **Header:** the age, when the form gives one ("adult" forms take no age), and the sex.
- **Base:** for a finding under test, the base never names it.
- **Each line about the condition under test:** one of the listed words.
- **Values:** the first number after the name is the value (128 does not count as 28), with its
  unit.
- **Dates and people:** years as given; a relative's fact names that relative and does not merely
  report; a patient's fact names no other person.
- **Denials and time:** a denial reads as a denial; a present fact is not denied; a fact marked over
  says so in words; an undated past fact reads as past.
- **No unlisted conditions:** no case names another condition of the rule that the form leaves
  unmentioned; extra lines name no condition or measurement of the rule; the reason names none
  that the form's reason does not.

These checks cannot judge meaning. The second author does that.

## Order of work

1. The writer fills in the group and runs the assembler until the group's line in
   `challenge_v1/ASSEMBLY_REPORT.md` reads "passes the checks; awaiting the second author:
   check_ok: yes <fingerprint>".
2. The second author checks the group (below) and writes `check_ok: yes <fingerprint>`, copied from
   the report, or `check_ok: no` with a reason in `check_comment`.
3. The fingerprint identifies the exact text. Any later edit changes it, and the group goes back to
   step 2. After a no, the writer revises and the same second author checks again.

## Second author (check)

For each group of the author you check, compare every line with its fact. The note must state
exactly the fact: right value, unit, year, person, time and denial, with nothing added.

FLIP and NEAR must differ from the base only in their line. Nothing in the base may name the
condition under test when the form forbids it.

Then write `check_ok: yes <fingerprint>` or `check_ok: no`. Give a reason in `check_comment`
whenever the answer is no, and fix nothing yourself. Only groups approved with the current
fingerprint enter the set.

## Submitting

```
python scripts/challenge_v1.py assemble
```

- Your `.md` file becomes `challenge_v1/notes_<authorN>.jsonl`.
- Every group is checked: values, years, persons, required strings, no unlisted conditions, and
  the second-author approval of the current text.
- `challenge_v1/ASSEMBLY_REPORT.md` lists what to fix and the fingerprint of each group that
  awaits its check.

Labels never come from your text; they come from the program run on the facts. A group that
fails a check is reported, not dropped silently.
