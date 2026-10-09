"""Glasgow-Blatchford Bleeding Score (GBS) (Calculator ID 27), from the score text of the instances:

1. BUN (mg/dL): <18.2 = 0 points, 18.2-22.3 = +2 points, 22.4-28 = +3 points, 28-70 = +4 points, >70 = +6 points
2. Hemoglobin (g/dL) for men: >=13 = 0 points, <=12-13 = +1 point, <=10-12 = +3 points, <10 = +6 points
3. Hemoglobin (g/dL) for women: >=12 = 0 points, <=10-12 = +1 point, <10 = +6 points
4. Systolic blood pressure (mm Hg): >=110 = 0 points, 100-109 = +1 point, 90-99 = +2 points, <90 = +3 points
5. Pulse >=100 (per minute): No = 0 points, Yes = +1 point
6. Melena present: No = 0 points, Yes = +1 point
7. Recent syncope: No = 0 points, Yes = +2 points
8. Hepatic disease history: No = 0 points, Yes = +2 points
9. Cardiac failure present: No = 0 points, Yes = +2 points

Criteria 2 and 3 are the sex-specific variants of one item (Hemoglobin).
"""
from selrm.mcv import Item, Score, flag, num

BUN, HB, SBP, HR = "Blood Urea Nitrogen (BUN)", "Hemoglobin", "Systolic Blood Pressure", "Heart Rate or Pulse"


def _bun(e):
    v = num(e, BUN, {"mg/dl": 1})
    return 0 if v < 18.2 else 2 if v < 22.4 else 3 if v < 28 else 4 if v <= 70 else 6


def _hb(e):
    v = num(e, HB, {"g/dl": 1})
    if v < 10:
        return 6
    if e["sex"] == "Male":
        return 3 if v < 12 else 1 if v < 13 else 0
    return 1 if v < 12 else 0


def _sbp(e):
    v = num(e, SBP, {"mm hg": 1})
    return 0 if v >= 110 else 1 if v >= 100 else 2 if v >= 90 else 3


def _finding(key, pts):
    return lambda e: pts * int(flag(e, key))


SCORE = Score(27, "Glasgow-Blatchford Bleeding Score (GBS)", (
    Item("BUN", (0, 2, 3, 4, 6), _bun, (BUN,), "numeric", {BUN: ("mg/dL", (18.2, 22.4, 28, 70))}),
    Item("Hemoglobin", (0, 1, 3, 6), _hb, (HB, "sex"), "mixed", {HB: ("g/dL", (10, 12, 13))}),
    Item("Systolic blood pressure", (0, 1, 2, 3), _sbp, (SBP,), "numeric", {SBP: ("mm Hg", (90, 100, 110))}),
    Item("Pulse", (0, 1), lambda e: int(num(e, HR, {"beats per minute": 1}) >= 100), (HR,), "numeric",
         {HR: ("per minute", (100,))}),
    Item("Melena present", (0, 1), _finding("Melena Present", 1), ("Melena Present",), "finding",
         time="current", support={"time": "Melena present"}),
    Item("Recent syncope", (0, 2), _finding("Recent Syncope", 2), ("Recent Syncope",), "finding",
         support={"window": "Recent syncope"}),
    Item("Hepatic disease history", (0, 2), _finding("Hepatic disease history", 2), ("Hepatic disease history",),
         "finding", time="ever", support={"time": "Hepatic disease history"}),
    Item("Cardiac failure present", (0, 2), _finding("Cardiac Failure Present", 2), ("Cardiac Failure Present",),
         "finding", time="current", support={"time": "Cardiac failure present"}),
), conventions=(
    "An unmentioned finding (melena, recent syncope, hepatic disease history, cardiac failure) is absent: "
    "\"The patient's status for recent syncope is missing from the patient note and so we assume it is absent "
    "from the patient.\"",
))
