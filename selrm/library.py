"""The rule library: pilot rules (rules.py) plus the extensions in rules_*.py.
Use LIBRARY / LIBRARY_BY_ID for data generation; rules.py RULES stays the
11-rule pilot that the smoke generator uses."""
from selrm import rules_constraint, rules_grammar, rules_score
from selrm.rules import RULES as PILOT

LIBRARY = (PILOT + rules_constraint.RULES + rules_score.RULES + rules_grammar.RULES
           + rules_grammar.SAMPLED)
LIBRARY_BY_ID = {r.rid: r for r in LIBRARY}
assert len(LIBRARY_BY_ID) == len(LIBRARY), "duplicate rule ids"
