# H1: rendering fidelity (authors)

Each of you reads 75 groups: `sheet_authorN.csv`, or the same rows in `sheets_authorN.md`. Save your
answers as `audit/h1/answers_<your name>.csv`: a copy of your sheet with the answer columns filled in.
No script ever writes that file. Do not open `key.csv` until you have finished; it holds the program's
answers. Afterwards, `python scripts/h1_aggregate.py` compares your answers with the key.

## Conventions the labels follow
- A history item (a finding) that is not mentioned is absent. A measurement that is not mentioned is
  unknown. A line saying a condition is unknown, not obtained or unclear makes it unknown.
- Only the patient counts, unless the rule says that relatives (parent, sibling, child) count.
- Only current findings and values count, unless the rule says that past ones count. A value given
  with a year, or described as earlier, replaced or yesterday, is not current.
- Numbers are compared with the stated operator: "above"/"below" are strict, "or more"/"or less"
  are inclusive.
- General lines such as "Steady on feet; balance normal." never name the condition. They are
  listed as "not named; counts as absent". Do not report them as a missing fact.

## Questions (one row per case; the cases of a group appear in random order)
- **q1_facts_ok (y/n).** Do the quoted lines state exactly the listed facts about the rule's
  conditions: value, unit, person, current or past, denial? And does no other line of the case bear
  on a condition of the rule? The header, the setting and unrelated lines are out of scope unless
  they bear on a condition. An empty facts list means that no condition of the rule is mentioned.
- **q2_conclusion (s / s' / neither).** Under the rule as stated, which conclusion claim is
  correct? Answer "neither" when the case does not decide it, for example when a needed value is
  unknown.
- **q3_criterion (s / s' / neither, or blank).** The same for the criterion claim. Constraint rules
  only.
- **problem_type** when q1 is n or an answer is unclear: dropped negation, wrong subject, ambiguous
  time, conflicting measurement, omitted exception, wording, other. Add a note.
