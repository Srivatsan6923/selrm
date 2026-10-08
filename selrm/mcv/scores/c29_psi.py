"""PSI Score: Pneumonia Severity Index for CAP (Calculator ID 29), from the score text of the instances:

1. Age: Enter age in years (age score will be equal to age in years)
2. Sex: Female = -10 points, Male = 0 points
3. Nursing home resident: No = 0 points, Yes = +10 points
4. Neoplastic disease: No = 0 points, Yes = +30 points
5. Liver disease history: No = 0 points, Yes = +20 points
6. Congestive heart failure (CHF) history: No = 0 points, Yes = +10 points
7. Cerebrovascular disease history: No = 0 points, Yes = +10 points
8. Renal disease history: No = 0 points, Yes = +10 points
9. Altered mental status: No = 0 points, Yes = +20 points
10. Respiratory rate >=30 breaths/min: No = 0 points, Yes = +20 points
11. Systolic blood pressure <90 mmHg: No = 0 points, Yes = +20 points
12. Temperature <35 C (95 F) or >39.9 C (103.8 F): No = 0 points, Yes = +15 points
13. Pulse >=125 beats/min: No = 0 points, Yes = +10 points
14. pH <7.35: No = 0 points, Yes = +30 points
15. BUN >=30 mg/dL or >=11 mmol/L: No = 0 points, Yes = +20 points
16. Sodium <130 mmol/L: No = 0 points, Yes = +20 points
17. Glucose >=250 mg/dL or >=14 mmol/L: No = 0 points, Yes = +10 points
18. Hematocrit <30%: No = 0 points, Yes = +10 points
19. Partial pressure of oxygen <60 mmHg or <8 kPa: No = 0 points, Yes = +10 points
20. Pleural effusion on x-ray: No = 0 points, Yes = +10 points
"""
from selrm.mcv import Item, Score, flag, num

TEMP = {"degrees celsius": 1, "degrees fahrenheit": lambda f: (f - 32) * 5 / 9}


def _lt(key, to, cut, pts):
    return lambda e: pts * int((v := num(e, key, to)) is not None and v < cut)


def _ge(key, to, cut, pts):
    return lambda e: pts * int((v := num(e, key, to)) is not None and v >= cut)


def _temp(e):
    v = num(e, "Temperature", TEMP)
    return 15 * int(v is not None and (v < 35 or v > 39.9))


def _find(name, key, pts, **kw):
    return Item(name, (0, pts), lambda e: pts * int(flag(e, key)), (key,), "finding", **kw)


def _numeric(name, key, pts, f, to, unit, cut):
    return Item(name, (0, pts), f(key, to, cut, pts), (key,), "numeric", {key: (unit, (cut,))})


HIST = {"time": "ever", "support": {"time": "history"}}

SCORE = Score(29, "PSI Score: Pneumonia Severity Index for CAP", (
    Item("Age", ("age in years",), lambda e: num(e, "age", {"years": 1}), ("age",), "numeric"),
    Item("Sex", (-10, 0), lambda e: -10 * int(e["sex"] == "Female"), ("sex",), "finding"),
    _find("Nursing home resident", "Nursing home resident", 10),
    _find("Neoplastic disease", "Neoplastic disease", 30),
    _find("Liver disease history", "Liver disease history", 20, **HIST),
    _find("Congestive heart failure (CHF) history", "Congestive Heart Failure", 10, **HIST),
    _find("Cerebrovascular disease history", "Cerebrovascular disease history", 10, **HIST),
    _find("Renal disease history", "Renal disease history", 10, **HIST),
    _find("Altered mental status", "Altered mental status", 20),
    _numeric("Respiratory rate", "respiratory rate", 20, _ge, {"breaths per minute": 1}, "breaths/min", 30),
    _numeric("Systolic blood pressure", "Systolic Blood Pressure", 20, _lt, {"mm hg": 1}, "mmHg", 90),
    Item("Temperature", (0, 15), _temp, ("Temperature",), "numeric", {"Temperature": ("degrees celsius", (35, 39.9))}),
    _numeric("Pulse", "Heart Rate or Pulse", 10, _ge, {"beats per minute": 1}, "beats/min", 125),
    _numeric("pH", "pH", 30, _lt, None, "", 7.35),
    _numeric("BUN", "Blood Urea Nitrogen (BUN)", 20, _ge, {"mg/dl": 1}, "mg/dL", 30),
    _numeric("Sodium", "Sodium", 20, _lt, {"meq/l": 1}, "mmol/L", 130),
    _numeric("Glucose", "Glucose", 10, _ge, {"mg/dl": 1}, "mg/dL", 250),
    _numeric("Hematocrit", "Hematocrit", 10, _lt, {"%": 1}, "%", 30),
    _numeric("Partial pressure of oxygen", "Partial pressure of oxygen", 10, _lt, {"mm hg": 1}, "mmHg", 60),
    _find("Pleural effusion on x-ray", "Pleural effusion on x-ray", 10),
), conventions=(
    "An unmentioned finding is absent ('Neoplastic disease is not reported for the patient and so we assume it to be"
    " false. Hence, we do not add any points').",
    "Sodium in mEq/L equals mmol/L ('The compound ... has a valence of 1 ... 140 mEq sodium/L converts to 140.0 mmol"
    " sodium/L').",
))
