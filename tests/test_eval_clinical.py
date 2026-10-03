"""Evidence quotes of TrialGPT reader outputs (scripts/eval_clinical.py). python tests/test_eval_clinical.py"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
from eval_clinical import evidence, quotes, sentence_ids

NOTE = "0. A 5-year-old girl.\n1. She states she has asthma.\n2. No smoking.\n4. Her family tells her to rest.\n5. Seen in clinic."

ledger = ("need: asthma\nfound: 1. She states she has asthma.\n4. Her family tells her to rest.\nsubject: patient\n"
          "status: present\ntime: current\n\nneed: smoking\nfound: not mentioned\nsubject: patient\nstatus: absent\ntime: current")
q = quotes(ledger, "ledger2")
assert q == ["1. She states she has asthma.", "Her family tells her to rest."], q        # continuation line kept
assert sentence_ids(NOTE, q) == {1, 4}
assert quotes("| need | found |\n|---|---|\n| asthma | x |", "ledger2") == []                # no key lines, no quotes
assert sentence_ids(NOTE, ["5"]) == {0}             # '5' inside label '5. ' does not count; '5-year-old' does
assert sentence_ids(NOTE, ["5. Seen"]) == {5}       # a quote that reaches past the label counts
assert quotes('It says "No smoking." and “Seen in clinic.”', "summary2") == ["No smoking.", "Seen in clinic."]

items = [{"quoted": set(), "expert": {1}, "malformed": False}]
assert evidence(items)["precision"] is None and evidence(items)["recall"] == 0.0               # 0/0 precision -> None
items = [{"quoted": {1, 4}, "expert": {1}, "malformed": True}, {"quoted": {2}, "expert": {2}, "malformed": False}]
assert (evidence(items)["precision"], evidence(items)["recall"]) == (200 / 3, 100.0)
assert (evidence(items, True)["precision"], evidence(items, True)["recall"]) == (100.0, 50.0)
print("ok")
