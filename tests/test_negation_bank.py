import re

import pytest

from selrm import negation_bank as N
from selrm import phrases as P

FINDINGS = ["fever", "Productive cough", "ECG changes", "a rash on the trunk", "palpitations.",
            "recent travel to West Africa", "3 weeks of night sweats"]


def test_cues_follow_rule_v1_split():
    assert set(N.CUES["train"]) >= set(P.NEG_CUES["train"])
    assert not set(N.CUES["test"]) & set(N.CUES["train"])
    assert set(N.CUES["test"]) <= set(P.NEG_CUES["test"])          # 'never' deliberately unused
    for split, other in (("train", "test"), ("test", "train")):
        for t in N.TEMPLATES[split]:
            text = t.replace("{np}", "x").replace("{NP}", "X")
            assert any(s == split for s, _ in N.cue_words(text)), t   # every template carries its split's cue
            assert not [c for s, c in N.cue_words(text) if s == other], t


def test_lines_name_the_finding_and_rebuild_identically():
    for split in ("train", "test"):
        for i, f in enumerate(FINDINGS):
            line = N.deny(f, split, key=f"pair-{i}")
            assert line == N.deny(f, split, key=f"pair-{i}")
            assert N._np(f).lower() in line.lower()
            assert (line[0].isupper() or line[0].isdigit()) and line.endswith(".") and ".." not in line
            assert not re.search(r"(?i)\b(no|without|of|for|denies) (a|an|the) ", line)
    assert N.deny("ECG changes", "test", key=3).count("ECG") == 1
    used = {N.deny("fever", "test", key=k) for k in range(200)}
    assert len(used) == len(N.TEMPLATES["test"])                     # the hash reaches every template


def test_rejects_bad_input():
    with pytest.raises(ValueError):
        N.deny("fever", "dev", key=1)
    with pytest.raises(ValueError):
        N.deny("  .", "test", key=1)
