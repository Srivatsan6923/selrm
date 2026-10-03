"""Write selrm/phrases.py from the phrase banks in tools/phrase_kit/banks.

  python tools/phrase_kit/gen_time_forms.py   # banks/T.json: value-neutral numeric time forms
  python tools/phrase_kit/gen_phrases.py      # final: refuses any TODO slot
  python tools/phrase_kit/gen_phrases.py --dev  # dev only: fills TODO slots with another template of the same split

Banks: G1-G6 (concept groups), N (concepts and forms added with the rule batches),
T (generated time forms), F (fillers). Later files override earlier ones form by form.
"""
import json
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
OUT = KIT.parents[1] / "selrm" / "phrases.py"
DEV = "--dev" in sys.argv


def fill(L):
    if not DEV:
        assert "TODO" not in L, "unfilled slot"
        return L
    out = list(L)
    for i, t in enumerate(out):
        if t == "TODO":
            same = [x for j, x in enumerate(out) if x != "TODO" and (j % 6 < 4) == (i % 6 < 4)]
            out[i] = same[i % len(same)] if same else "Dev placeholder line."
    return out


banks = {}
# N: concepts and forms of the rule batches; T: value-neutral numeric time forms (gen_time_forms.py)
for g in ("G1", "G2", "G3", "G4", "G5", "G6", "N", "T"):
    for concept, forms in json.load(open(f"{KIT}/banks/{g}.json", encoding="utf-8")).items():
        if g == "T" and concept not in banks:
            continue
        banks.setdefault(concept, {}).update({form: fill(L) for form, L in forms.items()})
fillers = {k: fill(v) for k, v in json.load(open(f"{KIT}/banks/F.json", encoding="utf-8")).items()}


def pylist(name, L, indent=4):
    pad = " " * indent
    return f"{name} = [\n" + "".join(f"{pad}{json.dumps(x)},\n" for x in L) + "]\n"


def pybanks(B):
    out = ["BANKS = {\n"]
    for concept, forms in B.items():
        out.append(f"    {json.dumps(concept)}: {{\n")
        for form, L in forms.items():
            out.append(f"        {json.dumps(form)}: [\n")
            out += [f"            {json.dumps(x)},\n" for x in L]
            out.append("        ],\n")
        out.append("    },\n")
    out.append("}\n")
    return "".join(out)


HEAD = '''"""Phrase banks: concept x mention form -> sentence templates.

Every list is laid out in blocks of 6: index % 6 in 0-3 is the train split,
4-5 the test split (templates, header frames, filler lines, person names).
The words that mark negation, past time and current time are split the same
way (NEG_CUES, TIME_CUES, CURRENT_CUES); tests check that every template other
than a generic absence uses only its own split's cues, that present and
other-person forms carry no negation or past-time cue, and that every current
value carries a current cue of its split.

Slots: {v} value, {dia} diastolic pressure (sbp only), {year}, {Poss} the
patient's possessive pronoun (Her/His), {rel} another person.

Finding forms (status, time) and their use:
  generic     absent, current   absence that does not name the concept (base)
  present     present, current  flip
  past        present, past     flip if the criterion counts past, else time near-miss
  absent      absent, current   named absence (negation near-miss)
  rel         present, current  another person: subject near-miss, or a flip by a
                                first-degree relative where the criterion counts family
  rel_past    present, past     another person, past (used only where past counts)
  delabelled  present, past     allergy label removed after testing (tier "delabelled")
Numeric forms:
  current     present, current  base, flip, numeric and boundary near-misses (one template)
  past        present, past     flip-side value in an earlier year (time near-miss)
  superseded  present, past     recent value replaced by today's (tier "superseded")
Fillers: FILLERS (neutral), FILLERS_OTHER (another person's unrelated condition),
FILLERS_LAB (an old value of an unrelated lab); the long tier mixes all three.
"""

FORMS = {
    "generic": ("absent", "current"),
    "present": ("present", "current"),
    "past": ("present", "past"),
    "absent": ("absent", "current"),
    "rel": ("present", "current"),
    "rel_past": ("present", "past"),
    "delabelled": ("present", "past"),
    "current": ("present", "current"),
    "superseded": ("present", "past"),
}

# Cue words, matched as whole words in lower case.
NEG_CUES = {"train": ("denies", "no", "not"),
            "test": ("never", "negative", "ruled out", "absent", "free of", "without")}
TIME_CUES = {"train": ("resolved", "healed", "previously", "completed", "stopped",
                       "yesterday", "on admission", "removed"),
             "test": ("formerly", "outgrown", "ago", "recovered", "earlier", "last month",
                      "de-labeled", "delabeled")}
CURRENT_CUES = {"train": ("today", "this morning", "at this assessment"),
                "test": ("current", "currently", "now", "latest", "at this visit")}


def split_of(i):
    return "train" if i % 6 < 4 else "test"


def ids(items, split):
    """Indices of the items in this split."""
    if split not in ("train", "test"):
        raise ValueError(f"split must be train or test, got {split!r}")
    return [i for i in range(len(items)) if split_of(i) == split]


def by_split(items, split):
    return [items[i] for i in ids(items, split)]


# Header frames; HEADER_NO_AGE is used when the rule has an age criterion.
HEADER = ["{age}-year-old {noun}.", "Patient: {sex}, {age} years.", "{Sex}, {age} years.",
          "{age} years old, {sex}.",
          "{Noun} of {age} years.", "{Sex} patient of {age} years."]
HEADER_NO_AGE = ["Patient: {sex}.", "Sex: {sex}.", "Adult {noun}.", "{Sex} patient.",
                 "An adult {noun}.", "{Noun}, adult."]

# Other people, in blocks of 6 (0-3 train, 4-5 test).
PERSONS = ["mother", "brother", "aunt", "husband", "father", "sister",
           "cousin", "partner", "coworker", "grandmother", "uncle", "wife",
           "neighbor", "brother-in-law", "housemate", "grandfather", "roommate", "friend"]
FIRST_DEGREE_SHOWN = {"mother", "father", "brother", "sister"}
PERSON_OK = {   # who can plausibly carry the concept (default: anyone)
    "pregnancy": frozenset({"cousin", "partner", "coworker", "neighbor", "housemate",
                            "sister", "wife", "roommate", "friend"}),
}


def persons(concept, split, age=None):
    """Other people who can plausibly carry the concept, for a patient of this age:
    grandparents only under 40, no parents' generation from 65, no spouse under 18."""
    ok = set(PERSON_OK.get(concept, PERSONS))
    if age is None or age >= 40:
        ok -= {"grandmother", "grandfather"}
    if age is not None and age >= 65:
        ok -= {"mother", "father", "aunt", "uncle"}
    if age is not None and age < 18:
        ok -= {"husband", "wife"}
    if age is not None and age >= 70:
        ok -= {"coworker"}
    return [p for p in by_split(PERSONS, split) if p in ok]


# Concepts whose generic absence lines may deny one another (e.g. "No known drug
# allergies" and a sulfonamide allergy). The engine omits a generic line when
# another concept of its group is present in the group's cases.
OVERLAP = (
    {"pen_allergy", "sulfa_allergy", "contrast_allergy", "angioedema", "hit"},
    {"aspirin", "warfarin", "vte", "hit", "mech_valve", "inr"},
    {"clarithromycin", "methotrexate", "lithium", "aspirin", "warfarin"},
    {"bleeding", "peptic_ulcer", "crc", "hemoptysis", "hemoglobin"},
    {"cancer", "crc"},
    {"stroke", "confusion"},
    {"cad", "vascular", "chf", "hypertension"},
    {"vascular", "calf_swelling"},
    {"hypertension", "sbp", "map"},
    {"warfarin", "inr"},
    {"supp_oxygen", "spo2"},
    {"peptic_ulcer", "crc", "ascites", "rlq_tenderness"},
)


# Missing-input lines for a finding whose status is unknown ({What}/{what}: the
# criterion label). Measured inputs are unknown when omitted and need no line.
MISSING = [
    "{What}: could not be determined from the information available.",
    "{What}: not yet assessed.",
    "Information on {what} was not obtained.",
    "{What}: still to be established.",
    "{What}: unknown.",
    "{What}: status unclear from the records at hand.",
]


'''

src = (HEAD + "# Neutral lines: one attribute each, no medications, no medical history, no\n"
       "# people and no criterion keyword of any rule (tests enforce the last).\n"
       + pylist("FILLERS", fillers["neutral"])
       + "\n# Another person's unrelated condition (subject distractors for the long tier).\n"
       + pylist("FILLERS_OTHER", fillers["other_person"])
       + "\n# An old value of an unrelated lab (time distractors for the long tier).\n"
       + pylist("FILLERS_LAB", fillers["old_lab"]) + "\n" + pybanks(banks))
open(OUT, "w", encoding="utf-8").write(src)
print(f"wrote {OUT}: {len(banks)} concepts, "
      f"{sum(len(L) for b in banks.values() for L in b.values())} templates{' (DEV FILL)' if DEV else ''}")
