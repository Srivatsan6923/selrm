# H1: rendering fidelity (authors)

Each of you reads 75 groups: `sheet_authorN.csv`, or the same rows in `sheets_authorN.md`. Save your
answers as `audit/h1/answers_authorN.csv`, with your assigned id and not your name: a copy of your
sheet with the answer columns filled in. No script ever writes that file. Do not open `key.csv`
until you have finished; it holds the program's answers. Afterwards, `python scripts/h1_aggregate.py`
compares your answers with the key.

## How to read a row
- Read the case text and answer q2 and q3 first. Only then read Facts and answer q1. Facts are the
  program's reading of the case, so reading them first would steer your answers.
- The cases of a group share most lines: two cases differ in one line (replaced or added), and one
  case rewords and reorders another. Check the shared lines once per group.

## Conventions the labels follow
- A history item (a finding) that is not mentioned is absent. A measurement that is not mentioned is
  unknown. A line saying a condition is unknown, not obtained or unclear makes it unknown.
- Only the patient counts, unless the rule says that relatives (parent, sibling, child) count.
- Only current findings and values count, unless the rule says that past ones count. A value given
  with a year, or described as earlier, replaced or yesterday, is not current.
- Numbers are compared with the stated operator: "above"/"below" are strict, "or more"/"or less"
  are inclusive.
- General lines such as "Steady on feet; balance normal." never name the condition. Facts lists
  them as "not named; a general line implies absence (counts as absent)". Do not report them as a
  missing fact.
- Conditions that the case does not mention are listed as "not mentioned", with "(counts as
  absent)" for a finding and "(unknown)" for a measurement.
- "Denied by name" covers whatever the quoted line covers, for example "never" or "now".
- The condition in a criterion claim is the rule's condition with the rule's time and person
  scope: in a rule that counts past heart failure, "heart failure" holds for a patient who had it
  years ago.

## Questions (one row per case; the cases of a group appear in random order)
- **q2_conclusion (s / s' / neither).** Under the rule as stated, which conclusion claim is
  correct? Answer "neither" when the case does not decide it, for example when a needed value is
  unknown.
- **q3_criterion (s / s' / neither, or blank).** The same for the criterion claim. Answer q3
  whenever the row has criterion claims (criterion_s is filled); leave it blank when criterion_s
  is empty.
- **q1_facts_ok (y/n).** Do the quoted lines state exactly the listed facts about the rule's
  conditions: value (in the rule's unit), person, current or past, denial? And does no other line
  of the case bear on a condition of the rule? The header, the setting and unrelated lines are out
  of scope unless they bear on a condition.
- **problem_type** when q1 is n or an answer is unclear: dropped negation, wrong subject, ambiguous
  time, conflicting measurement, wording, other. Add a note.

Write the answers exactly as shown: y or n for q1; s, s' or neither for q2 and q3. The script
refuses any other value and lists the rows to correct.

## Known issue in these sheets
Cases A4-G25-C2, A4-G25-C4 contain the general line "Face and neck without swelling on examination.", which contradicts their swollen neck lymph nodes. Report it as 'conflicting measurement'.
