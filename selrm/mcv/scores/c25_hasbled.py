"""HAS-BLED Score for Major Bleeding Risk (Calculator ID 25), from the score text of the instances:

1. Hypertension (Uncontrolled, >160 mmHg systolic): No = 0 points, Yes = +1 point
2. Renal disease (Dialysis, transplant, Cr >2.26 mg/dL or >200 umol/L): No = 0 points, Yes = +1 point
3. Liver disease (Cirrhosis or bilirubin >2x normal with AST/ALT/AP >3x normal): No = 0 points, Yes = +1 point
4. Stroke history: No = 0 points, Yes = +1 point
5. Prior major bleeding or predisposition to bleeding: No = 0 points, Yes = +1 point
6. Labile INR (Unstable/high INRs, time in therapeutic range <60%): No = 0 points, Yes = +1 point
7. Age >65: No = 0 points, Yes = +1 point
8. Medication usage predisposing to bleeding (Aspirin, clopidogrel, NSAIDs): No = 0 points, Yes = +1 point
9. Alcohol use (>=8 drinks/week): No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

HTN, STROKE = "Hypertension", "Stroke"
RENAL = "Renal disease criteria for the HAS-BLED rule"
LIVER = "Liver disease criteria for the HAS-BLED rule"
BLEED = "Prior major bleeding or predisposition to bleeding"
INR = "Labile international normalized ratio"
MEDS = "Medication usage predisposing to bleeding"
DRINKS = "Number of Alcoholic Drinks Per Week"


def _finding(name, key, **kw):
    return Item(name, (0, 1), lambda e: int(flag(e, key)), (key,), "finding", **kw)


def _age(e):
    v = num(e, "age", {"years": 1})
    return int(v is not None and v > 65)


def _alcohol(e):
    v = num(e, DRINKS)
    return int(v is not None and v >= 8)


SCORE = Score(25, "HAS-BLED Score for Major Bleeding Risk", (
    _finding("Hypertension", HTN),
    _finding("Renal disease", RENAL),
    _finding("Liver disease", LIVER),
    _finding("Stroke history", STROKE, time="ever", support={"time": "Stroke history"}),
    _finding("Prior major bleeding or predisposition to bleeding", BLEED, time="ever",
             support={"time": "Prior major bleeding"}),
    _finding("Labile INR", INR),
    Item("Age", (0, 1), _age, ("age",), "numeric", {"age": ("years", (65,))}),
    _finding("Medication usage predisposing to bleeding", MEDS),
    Item("Alcohol use", (0, 1), _alcohol, (DRINKS,), "numeric", {DRINKS: ("drinks/week", (8,))}),
), conventions=(
    "An unmentioned finding is absent, for each of the seven findings: 'The issue, renal disease, is missing from "
    "the patient note and so we assume it to be absent and so we do not change the score'.",
    "age and Number of Alcoholic Drinks Per Week are released on every row; no absent-key convention is stated "
    "for them (the items give 0 points if the key is absent).",
))
