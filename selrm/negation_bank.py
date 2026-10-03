"""Phrases that explicitly deny one finding, for role C's negated-evidence sets (NEXT_TASKS_A item 2;
docs/AUX_PROTOCOL.md S2): clin_v1/medeinst_neg uses the test split on MedEinst test pairs, and the training
version uses the train split on the reference pairs.

The split follows rule_v1's negation cues (selrm.phrases.NEG_CUES): training templates use only the
training cues ('denies', 'no', 'not'), test templates only the test cues ('negative', 'free of', 'without',
'absent', 'ruled out'), so no denial wording of the test set occurs in training. 'never' is left out: it
states a lifetime absence, while MedEinst findings are current presentations. Every template names the
finding, so the line is an explicit denial ('denies X', 'no X'), not a general normal finding.

  deny("productive cough", "test", key="pair-0417")  -> "Presents without productive cough."

The template is chosen by a hash of key, so a set rebuilds identically.
"""
import hashlib
import re

TEMPLATES = {
    "train": ("Denies {np}.", "No {np}.", "No {np} on history or examination.", "{NP}: not present.",
              "Reports no {np}.", "Does not have {np}."),
    "test": ("Negative for {np}.", "Free of {np}.", "Presents without {np}.", "{NP}: absent.",
             "{NP}: ruled out.", "{NP} absent on assessment."),
}
CUES = {"train": ("denies", "no", "not", "does not"),
        "test": ("negative", "free of", "without", "absent", "ruled out")}


def _np(finding):
    """The finding as a noun phrase: no final full stop or leading article ('No a rash' reads wrong), and a
    lower-case first letter unless it starts an abbreviation ('ECG changes' stays as is)."""
    f = re.sub(r"(?i)^(a|an|the)\s+", "", finding.strip().rstrip(".").strip())
    first = f.split(" ", 1)[0]
    if f and not (len(first) > 1 and (first.isupper() or any(c.isdigit() for c in first))):
        f = f[0].lower() + f[1:]
    return f


def deny(finding, split, key):
    """One line that explicitly denies finding, from the given split ('train' or 'test')."""
    if split not in TEMPLATES:
        raise ValueError(f"split must be 'train' or 'test', not {split!r}")
    np = _np(finding)
    if not np:
        raise ValueError("empty finding")
    t = TEMPLATES[split][int(hashlib.sha256(str(key).encode("utf-8")).hexdigest(), 16) % len(TEMPLATES[split])]
    return t.replace("{np}", np).replace("{NP}", np[0].upper() + np[1:])


def cue_words(text):
    """The negation cues of either split that occur in text (for checks on built sets)."""
    found = []
    for split, cues in CUES.items():
        found += [(split, c) for c in cues if re.search(rf"(?i)\b{re.escape(c)}\b", text)]
    return found
