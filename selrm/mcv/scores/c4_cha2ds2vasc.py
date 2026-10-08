"""CHA2DS2-VASc Score for Atrial Fibrillation Stroke Risk (Calculator ID 4), from the score text of the instances:

1. Age: < 65 years = 0 points, 65-74 years = +1 point, >= 75 years = +2 points
2. Sex: Female = +1 point, Male = 0 points
3. Congestive Heart Failure (CHF) history: No = 0 points, Yes = +1 point
4. Hypertension history: No = 0 points, Yes = +1 point
5. Stroke, Transient Ischemic Attack (TIA), or Thromboembolism history: No = 0 points, Yes = +2 points
6. Vascular disease history (previous myocardial infarction, peripheral artery disease, or aortic plaque):
   No = 0 points, Yes = +1 point
7. Diabetes history: No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

STT = ("Stroke", "Transient Ischemic Attacks History", "Thromboembolism history")
HIST = {"time": "history"}


def _age(e):
    v = num(e, "age", {"years": 1})
    return 0 if v is None or v < 65 else 1 if v < 75 else 2


def _one(key):
    return lambda e: int(flag(e, key))


SCORE = Score(4, "CHA2DS2-VASc Score for Atrial Fibrillation Stroke Risk", (
    Item("Age", (0, 1, 2), _age, ("age",), "numeric", {"age": ("years", (65, 75))}),
    Item("Sex", (0, 1), lambda e: int(str(e.get("sex", "")).lower() == "female"), ("sex",), "finding"),
    Item("Congestive Heart Failure (CHF) history", (0, 1), _one("Congestive Heart Failure"),
         ("Congestive Heart Failure",), "finding", time="ever", support=HIST),
    Item("Hypertension history", (0, 1), _one("Hypertension history"), ("Hypertension history",), "finding",
         time="ever", support=HIST),
    Item("Stroke, Transient Ischemic Attack (TIA), or Thromboembolism history", (0, 2),
         lambda e: 2 * int(any(flag(e, k) for k in STT)), STT, "finding", time="ever", support=HIST),
    Item("Vascular disease history", (0, 1), _one("Vascular disease history"), ("Vascular disease history",),
         "finding", time="ever", support={"time": "history (previous myocardial infarction"}),
    Item("Diabetes history", (0, 1), _one("Diabetes history"), ("Diabetes history",), "finding",
         time="ever", support=HIST),
), conventions=(
    "An unmentioned history item is absent ('Because the congestive heart failure history is not specified in the "
    "patient note, we assume it is absent from the patient'; likewise hypertension, stroke, tia, thromboembolism, "
    "vascular disease, diabetes).",
))
