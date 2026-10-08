"""HEART Score for Major Cardiac Events (Calculator ID 18), from the score text of the instances:

1. History: Slightly suspicious = 0 points, Moderately suspicious = +1 point, Highly suspicious = +2 points
2. EKG: Normal = 0 points, Non-specific repolarization disturbance = +1 point, Significant ST deviation = +2 points
3. Age: <45 years = 0 points, 45-64 years = +1 point, >=65 years = +2 points
4. Risk factors (HTN, hypercholesterolemia, DM, obesity (BMI >30 kg/m2), smoking (current or cessation within
   3 months), positive family history of cardiovascular disease before age 65, atherosclerotic disease such as
   prior MI, PCI/CABG, CVA/TIA, or peripheral arterial disease): No known risk factors = 0 points,
   1-2 risk factors = +1 point, >=3 risk factors or history of atherosclerotic disease = +2 points
5. Initial troponin level: <=normal limit = 0 points, 1-3x normal limit = +1 point, >3x normal limit = +2 points
"""
from selrm.mcv import Item, Score, flag, num

HISTORY = {"slightly suspicious": 0, "moderately suspicious": 1, "highly suspicious": 2}
EKG = {"normal": 0, "non-specific repolarization disturbance": 1, "significant st deviation": 2}
TROPONIN = {"less than or equal to normal limit": 0,
            "between the normal limit or up to three times the normal limit": 1,
            "greater than three times normal limit": 2}
ATHERO = "atherosclerotic disease"
RISK = ("Hypertension history", "hypercholesterolemia", "Diabetes mellitus", "obesity", "smoking",
        "parent or sibling with Cardiovascular disease before age 65", ATHERO)


def _level(table, key):
    return lambda e: table[e[key].strip().lower()] if key in e else 0


def _age(e):
    v = num(e, "age", {"years": 1})
    return 0 if v is None or v < 45 else 1 if v < 65 else 2


def _risk(e):
    n = sum(flag(e, k) for k in RISK)
    return 2 if n >= 3 or flag(e, ATHERO) else int(n >= 1)


SCORE = Score(18, "HEART Score for Major Cardiac Events", (
    Item("History", (0, 1, 2), _level(HISTORY, "Suspicion History"), ("Suspicion History",), "finding"),
    Item("EKG", (0, 1, 2), _level(EKG, "Electrocardiogram Test"), ("Electrocardiogram Test",), "finding"),
    Item("Age", (0, 1, 2), _age, ("age",), "numeric", {"age": ("years", (45, 65))}),
    Item("Risk factors", (0, 1, 2), _risk, RISK, "finding", time="ever",
         support={"time": "history of atherosclerotic disease"}),
    Item("Initial troponin level", (0, 1, 2), _level(TROPONIN, "Initial troponin"), ("Initial troponin",),
         "finding", support={"window": "Initial troponin level"}),
), conventions=(
    "An unmentioned risk factor is absent (\"The following risk factor(s) are missing from the patient's data: ... "
    "We will assume that these are all absent from the patient.\").",
    "An unmentioned EKG is Normal (\"'electrocardiogram' is missing from the patient's data and so we assume it's "
    "value is Normal\").",
    "An unmentioned initial troponin is at or below the normal limit (\"'initial troponin' is missing from the "
    "patient's data and so we assume it's value is less than or equal to normal limit\").",
    "The released key 'Transient Ischemic Attacks History' is not read: the explanations list seven risk factors "
    "and take atherosclerotic disease only from the 'atherosclerotic disease' key.",
))
