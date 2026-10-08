"""PERC Rule for Pulmonary Embolism (Calculator ID 48), from the score text of the instances:

1. Age ≥50: No = 0 points, Yes = +1 point
2. Heart Rate (HR) ≥100: No = 0 points, Yes = +1 point
3. O₂ saturation on room air <95%: No = 0 points, Yes = +1 point
4. Unilateral leg swelling: No = 0 points, Yes = +1 point
5. Hemoptysis: No = 0 points, Yes = +1 point
6. Recent surgery or trauma (within 4 weeks, requiring treatment with general anesthesia): No = 0 points, Yes = +1 point
7. Prior pulmonary embolism (PE) or deep vein thrombosis (DVT): No = 0 points, Yes = +1 point
8. Hormone use (oral contraceptives, hormone replacement, or estrogenic hormone use in males or females):
   No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

HR, SPO2 = "Heart Rate or Pulse", "O₂ saturation percentage"
PE, DVT = "Previously Documented Pulmonary Embolism", "Previously documented Deep Vein Thrombosis"


def _age(e):
    v = num(e, "age", {"years": 1})
    return int(v is not None and v >= 50)


def _hr(e):
    v = num(e, HR, {"beats per minute": 1, "beats/minute": 1})
    return int(v is not None and v >= 100)


def _spo2(e):
    v = num(e, SPO2, {"%": 1})
    return int(v is not None and v < 95)


def _finding(key):
    return lambda e: int(flag(e, key))


SCORE = Score(48, "PERC Rule for Pulmonary Embolism", (
    Item("Age", (0, 1), _age, ("age",), "numeric", {"age": ("years", (50,))}),
    Item("Heart Rate (HR)", (0, 1), _hr, (HR,), "numeric", {HR: ("beats per minute", (100,))}),
    Item("O₂ saturation on room air", (0, 1), _spo2, (SPO2,), "numeric", {SPO2: ("%", (95,))}),
    Item("Unilateral leg swelling", (0, 1), _finding("Unilateral Leg Swelling"), ("Unilateral Leg Swelling",),
         "finding"),
    Item("Hemoptysis", (0, 1), _finding("Hemoptysis"), ("Hemoptysis",), "finding"),
    Item("Recent surgery or trauma", (0, 1), _finding("Recent surgery or trauma"), ("Recent surgery or trauma",),
         "finding", support={"window": "Recent surgery or trauma (within 4 weeks"}),
    Item("Prior pulmonary embolism (PE) or deep vein thrombosis (DVT)", (0, 1),
         lambda e: int(flag(e, PE) or flag(e, DVT)), (PE, DVT), "finding",
         time="ever", support={"time": "Prior pulmonary embolism (PE) or deep vein thrombosis (DVT)"}),
    Item("Hormone use", (0, 1), _finding("Hormone use"), ("Hormone use",), "finding"),
), conventions=(
    "An unmentioned finding is absent (\"The patient note does not report a status on 'unilateral leg swelling'. "
    "Hence, we assume it to be absent, and so we do not increment the criteria count.\").",
))
