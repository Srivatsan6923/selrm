"""CURB-65 Score for Pneumonia Severity (Calculator ID 45), from the score text of the instances:

1. Confusion: No = 0 points, Yes = +1 point
2. BUN >19 mg/dL (>7 mmol/L urea): No = 0 points, Yes = +1 point
3. Respiratory Rate >=30: No = 0 points, Yes = +1 point
4. Systolic BP <90 mmHg or Diastolic BP <=60 mmHg: No = 0 points, Yes = +1 point
5. Age >=65: No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

MMHG = {"mm hg": 1}


def _bun(e):
    # the score text gives both cuts: >19 mg/dL of BUN, >7 mmol/L of urea
    if "Blood Urea Nitrogen (BUN)" not in e:
        return 0
    v, unit = e["Blood Urea Nitrogen (BUN)"]
    return int(v > 7) if unit.lower() == "mmol/l" else int(num(e, "Blood Urea Nitrogen (BUN)", {"mg/dl": 1}) > 19)


def _rr(e):
    v = num(e, "respiratory rate", {"breaths per minute": 1})
    return int(v is not None and v >= 30)


def _bp(e):
    s, d = num(e, "Systolic Blood Pressure", MMHG), num(e, "Diastolic Blood Pressure", MMHG)
    return int((s is not None and s < 90) or (d is not None and d <= 60))


def _age(e):
    v = num(e, "age", {"years": 1})
    return int(v is not None and v >= 65)


SCORE = Score(45, "CURB-65 Score for Pneumonia Severity", (
    Item("Confusion", (0, 1), lambda e: int(flag(e, "Confusion")), ("Confusion",), "finding"),
    Item("BUN", (0, 1), _bun, ("Blood Urea Nitrogen (BUN)",), "numeric",
         {"Blood Urea Nitrogen (BUN)": ("mg/dL", (19,))}),
    Item("Respiratory Rate", (0, 1), _rr, ("respiratory rate",), "numeric",
         {"respiratory rate": ("breaths per minute", (30,))}),
    Item("Systolic BP or Diastolic BP", (0, 1), _bp, ("Systolic Blood Pressure", "Diastolic Blood Pressure"),
         "numeric", {"Systolic Blood Pressure": ("mmHg", (90,)), "Diastolic Blood Pressure": ("mmHg", (60,))}),
    Item("Age", (0, 1), _age, ("age",), "numeric", {"age": ("years", (65,))}),
), conventions=(
    "An unmentioned finding is absent (the explanations add 0 points where the note does not report confusion).",
))
