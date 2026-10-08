"""Child-Pugh Score for Cirrhosis Mortality (Calculator ID 15), from the score text of the instances:

1. Bilirubin (Total): <2 mg/dL (<34.2 umol/L) = +1 point, 2-3 mg/dL (34.2-51.3 umol/L) = +2 points,
   >3 mg/dL (>51.3 umol/L) = +3 points
2. Albumin: >3.5 g/dL (>35 g/L) = +1 point, 2.8-3.5 g/dL (28-35 g/L) = +2 points, <2.8 g/dL (<28 g/L) = +3 points
3. INR: <1.7 = +1 point, 1.7-2.3 = +2 points, >2.3 = +3 points
4. Ascites: Absent = +1 point, Slight = +2 points, Moderate = +3 points
5. Encephalopathy: No Encephalopathy = +1 point, Grade 1-2 = +2 points, Grade 3-4 = +3 points
"""
from selrm.mcv import Item, Score, num

ASCITES = {"absent": 1, "slight": 2, "moderate": 3}
ENCEPH = {"no encephalopathy": 1, "grade 1-2": 2, "grade 3-4": 3}


def _bili(e):
    v = num(e, "Bilirubin", {"mg/dl": 1})
    return 1 if v < 2 else 2 if v <= 3 else 3


def _alb(e):
    v = num(e, "Albumin", {"g/dl": 1})
    return 1 if v > 3.5 else 2 if v >= 2.8 else 3


def _inr(e):
    v = num(e, "international normalized ratio")
    return 1 if v < 1.7 else 2 if v <= 2.3 else 3


def _grade(key, table):
    # an unspecified state takes the lowest grade (1 point); an unlisted released value raises
    return lambda e: table[e[key].strip().lower()] if key in e else 1


SCORE = Score(15, "Child-Pugh Score for Cirrhosis Mortality", (
    Item("Bilirubin (Total)", (1, 2, 3), _bili, ("Bilirubin",), "numeric", {"Bilirubin": ("mg/dL", (2, 3))}),
    Item("Albumin", (1, 2, 3), _alb, ("Albumin",), "numeric", {"Albumin": ("g/dL", (2.8, 3.5))}),
    Item("INR", (1, 2, 3), _inr, ("international normalized ratio",), "numeric",
         {"international normalized ratio": ("", (1.7, 2.3))}),
    Item("Ascites", (1, 2, 3), _grade("Ascites", ASCITES), ("Ascites",), "finding"),
    Item("Encephalopathy", (1, 2, 3), _grade("Encephalopathy", ENCEPH), ("Encephalopathy",), "finding"),
), conventions=(
    "Ascites absent from the entities = Absent, 1 point ('The patient's ascites state is not specified and so we "
    "will assume it to be absent.').",
    "Encephalopathy absent from the entities = No Encephalopathy, 1 point ('The encephalopathy state is not "
    "specified, and so we assume that the patient does not have encephalopathy.').",
    "Band edges are inclusive in the middle band (bilirubin 2.0 mg/dL and albumin 2.8 g/dL are explained as "
    "'between' and give 2 points).",
))
