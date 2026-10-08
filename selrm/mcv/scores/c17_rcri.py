"""Revised Cardiac Risk Index for Pre-Operative Risk (Calculator ID 17), from the score text of the instances:

1. Elevated-risk surgery (intraperitoneal, intrathoracic, or suprainguinal vascular): No = 0 points, Yes = +1 point
2. History of ischemic heart disease (history of myocardial infarction, positive exercise test, current chest pain
   due to myocardial ischemia, use of nitrate therapy, or ECG with pathological Q waves): No = 0 points, Yes = +1 point
3. History of congestive heart failure (pulmonary edema, bilateral rales or S3 gallop, paroxysmal nocturnal dyspnea,
   or chest x-ray showing pulmonary vascular redistribution): No = 0 points, Yes = +1 point
4. History of cerebrovascular disease (prior transient ischemic attack or stroke): No = 0 points, Yes = +1 point
5. Pre-operative treatment with insulin: No = 0 points, Yes = +1 point
6. Pre-operative creatinine >2 mg/dL (176.8 umol/L): No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

SURGERY = "Elevated-risk surgery"
IHD = "History of ischemic heart disease"
CHF = "Congestive Heart Failure criteria for the Cardiac Risk Index rule"
CVD = "History of cerebrovascular disease"
INSULIN = "Pre-operative treatment with insulin"
CREAT = "Pre-operative creatinine"
# the explanations convert umol/L to mg/dL with the molar mass 113.12 g/mol: umol * 1e-06 * 113.12 * 1000 / 10
UMOL = 113.12 / 10000
CREAT_UNITS = {"mg/dl": 1, "µmol/l": UMOL, "μmol/l": UMOL}   # micro sign and Greek mu


def _creat(e):
    v = num(e, CREAT, CREAT_UNITS)
    # released on every row; the explanations state no convention for an absent creatinine (0 points here)
    return int(v is not None and v > 2)


def _finding(name, key, support=None):
    return Item(name, (0, 1), lambda e: int(flag(e, key)), (key,), "finding",
                time="ever" if support else "unstated", support={"time": support} if support else {})


SCORE = Score(17, "Revised Cardiac Risk Index for Pre-Operative Risk", (
    _finding("Elevated-risk surgery", SURGERY),
    _finding("History of ischemic heart disease", IHD, "History of"),
    _finding("History of congestive heart failure", CHF, "History of"),
    _finding("History of cerebrovascular disease", CVD, "History of"),
    _finding("Pre-operative treatment with insulin", INSULIN),
    Item("Pre-operative creatinine", (0, 1), _creat, (CREAT,), "numeric", {CREAT: ("mg/dL", (2,))}),
), conventions=(
    "An unmentioned finding is absent, for each of the five findings (\"The patient note does not mention anything "
    "about a history of congestive heart failure and is assumed to be absent. This means that the total score "
    "remains unchanged\").",
))
