"""APACHE II Score (Calculator ID 28), from the score text of the instances:

1. Age, years: <=44 = 0 points, 45-54 = +2 points, 55-64 = +3 points, 65-74 = +5 points, >=75 = +6 points
2. History of severe organ insufficiency or immunocompromised: Yes, nonoperative or emergency postoperative
   patient = +5 points, Yes, elective postoperative patient = +2 points, No = 0 points
3. Rectal temperature, C: >=41 = +4 points, 39 to <41 = +3 points, 38.5 to <39 = +1 point, 36 to <38.5 = 0 points,
   34 to <36 = +1 point, 32 to <34 = +2 points, 30 to <32 = +3 points, <30 = +4 points
4. Mean arterial pressure, mmHg: >=160 = +4 points, 130-159 = +3 points, 110-129 = +2 points, 70-109 = 0 points,
   50-69 = +2 points, <=49 = +4 points
5. Heart rate, beats per minute: >=180 = +4 points, 140 to <180 = +3 points, 110 to <140 = +2 points,
   70 to <110 = 0 points, 55 to <70 = +2 points, 40 to <55 = +3 points, <40 = +4 points
6. Respiratory rate, breaths per minute: >=50 = +4 points, 35 to <50 = +3 points, 25 to <35 = +1 point,
   12 to <25 = 0 points, 10 to <12 = +1 point, 6 to <10 = +2 points, <6 = +4 points
7. Oxygenation (use PaO2 if FiO2 < 50%, otherwise use A-a gradient): A-a gradient > 499 = +4 points, A-a gradient
   350-499 = +3 points, A-a gradient 200-349 = +2 points, A-a gradient < 200 (if FiO2 >= 50%) or PaO2 > 70 (if
   FiO2 < 50%) = 0 points, PaO2 61-70 = +1 point, PaO2 55-60 = +3 points, PaO2 < 55 = +4 points.
8. Arterial pH: >=7.7 = +4 points, 7.60 to <7.70 = +3 points, 7.50 to <7.60 = +1 point, 7.33 to <7.50 = 0 points,
   7.25 to <7.33 = +2 points, 7.15 to <7.25 = +3 points, <7.15 = +4 points
9. Serum sodium, mmol/L: >=180 = +4 points, 160 to <180 = +3 points, 155 to <160 = +2 points, 150 to <155 = +1
   point, 130 to <150 = 0 points, 120 to <130 = +2 points, 111 to <120 = +3 points, <111 = +4 points
10. Serum potassium, mmol/L: >=7.0 = +4 points, 6.0 to <7.0 = +3 points, 5.5 to <6.0 = +1 point, 3.5 to <5.5 = 0
    points, 3.0 to <3.5 = +1 point, 2.5 to <3.0 = +2 points, <2.5 = +4 points
11. Serum creatinine, mg/100 mL: >=3.5 and ACUTE renal failure = +8 points, 2.0 to <3.5 and ACUTE renal failure =
    +6 points, >=3.5 and CHRONIC renal failure = +4 points, 1.5 to <2.0 and ACUTE renal failure = +4 points,
    2.0 to <3.5 and CHRONIC renal failure = +3 points, 1.5 to <2.0 and CHRONIC renal failure = +2 points,
    0.6 to <1.5 = 0 points, <0.6 = +2 points
12. Hematocrit, %: >=60 = +4 points, 50 to <60 = +2 points, 46 to <50 = +1 point, 30 to <46 = 0 points,
    20 to <30 = +2 points, <20 = +4 points
13. White blood count, total/cubic mm in 10^3: >=40 = +4 points, 20 to <40 = +2 points, 15 to <20 = +1 point,
    3 to <15 = 0 points, 1 to <3 = +2 points, <1 = +4 points
14. Glasgow Coma Scale (GCS): 1-15 points (use 15 - [GCS Score])
"""
from selrm.mcv import Item, Score, flag, num

MMHG = {"mm hg": 1}
MMOL = {"mmol/l": 1, "meq/l": 1}       # valence 1: "141 mEq/(1 mEq/mmol) = 141.0 mmol"


def band(v, cuts, pts):
    """Points of the band holding v: pts[i] for the first cut with v < cuts[i], else pts[-1]."""
    return next((p for c, p in zip(cuts, pts) if v < c), pts[-1])


def _age(e):
    return band(num(e, "age", {"years": 1}), (45, 55, 65, 75), (0, 2, 3, 5, 6))


def _history(e):
    if not flag(e, "History of severe organ failure or immunocompromise"):
        return 0
    # points need the patient category; with no surgery type released the explanations add nothing
    return {"Elective": 2, "Emergency": 5, "Nonoperative": 5}[e["Surgery Type"]] if "Surgery Type" in e else 0


def _temp(e):
    v = num(e, "Temperature", {"degrees celsius": 1, "degrees fahrenheit": lambda f: 5 / 9 * (f - 32)})
    return band(v, (30, 32, 34, 36, 38.5, 39, 41), (4, 3, 2, 1, 0, 1, 3, 4))


def _map(e):
    # "1/3 * (systolic blood pressure) + 2/3 * (diastolic blood pressure)"; a released MAP entity is not used.
    # The bands are whole mmHg (50-69, 70-109); a value between two bands goes to the nearest whole number
    # (69.67 is scored "at least 70" in the one instance that falls in a gap).
    v = 1 / 3 * num(e, "Systolic Blood Pressure", MMHG) + 2 / 3 * num(e, "Diastolic Blood Pressure", MMHG)
    return band(round(v), (50, 70, 110, 130, 160), (4, 2, 0, 2, 3, 4))


def _hr(e):
    return band(num(e, "Heart Rate or Pulse", {"beats per minute": 1}), (40, 55, 70, 110, 140, 180),
                (4, 3, 2, 0, 2, 3, 4))


def _rr(e):
    return band(num(e, "respiratory rate", {"breaths per minute": 1}), (6, 10, 12, 25, 35, 50), (4, 2, 1, 0, 1, 3, 4))


def _oxy(e):
    if num(e, "FiO2", {"%": 1}) >= 50:
        return band(num(e, "A-a gradient"), (200, 350, 500), (0, 2, 3, 4))
    return band(num(e, "PaO2", MMHG), (55, 61, 71), (4, 3, 1, 0))


def _ph(e):
    return band(num(e, "pH"), (7.15, 7.25, 7.33, 7.5, 7.6, 7.7), (4, 3, 2, 0, 1, 3, 4))


def _na(e):
    return band(num(e, "Sodium", MMOL), (111, 120, 130, 150, 155, 160, 180), (4, 3, 2, 0, 1, 2, 3, 4))


def _k(e):
    return band(num(e, "Potassium", MMOL), (2.5, 3, 3.5, 5.5, 6, 7), (4, 2, 1, 0, 1, 3, 4))


def _creat(e):
    v = num(e, "creatinine", {"mg/dl": 1})
    if v < 0.6:
        return 2
    if flag(e, "Acute renal failure"):
        return band(v, (1.5, 2, 3.5), (0, 4, 6, 8))
    if flag(e, "Chronic renal failure"):
        return band(v, (1.5, 2, 3.5), (0, 2, 3, 4))
    # explanations: "at least 1.5 mg/dL, but less than 2.0 mg/dL (without acute and chronic renal failure), 2 points";
    # the score text and the instances give nothing for >=2.0 without renal failure
    return 2 if 1.5 <= v < 2 else 0


def _hct(e):
    return band(num(e, "Hematocrit", {"%": 1}), (20, 30, 46, 50, 60), (4, 2, 0, 1, 2, 4))


def _wbc(e):
    return band(num(e, "White blood cell count", {"mm^3": 1e-3}), (1, 3, 15, 20, 40), (4, 2, 0, 1, 2, 4))


SCORE = Score(28, "APACHE II Score", (
    Item("Age", (0, 2, 3, 5, 6), _age, ("age",), "numeric", {"age": ("years", (45, 55, 65, 75))}),
    Item("History of severe organ insufficiency or immunocompromised", (0, 2, 5), _history,
         ("History of severe organ failure or immunocompromise", "Surgery Type"), "finding",
         time="ever", support={"time": "History of"}),
    Item("Rectal temperature", (0, 1, 2, 3, 4), _temp, ("Temperature",), "numeric",
         {"Temperature": ("degrees celsius", (30, 32, 34, 36, 38.5, 39, 41))}),
    Item("Mean arterial pressure", (0, 2, 3, 4), _map, ("Systolic Blood Pressure", "Diastolic Blood Pressure"),
         "numeric"),
    Item("Heart rate", (0, 2, 3, 4), _hr, ("Heart Rate or Pulse",), "numeric",
         {"Heart Rate or Pulse": ("beats per minute", (40, 55, 70, 110, 140, 180))}),
    Item("Respiratory rate", (0, 1, 2, 3, 4), _rr, ("respiratory rate",), "numeric",
         {"respiratory rate": ("breaths per minute", (6, 10, 12, 25, 35, 50))}),
    Item("Oxygenation", (0, 1, 2, 3, 4), _oxy, ("FiO2", "PaO2", "A-a gradient"), "numeric",
         {"FiO2": ("%", (50,)), "PaO2": ("mmHg", (55, 61, 71)), "A-a gradient": ("mmHg", (200, 350, 500))}),
    Item("Arterial pH", (0, 1, 2, 3, 4), _ph, ("pH",), "numeric", {"pH": ("", (7.15, 7.25, 7.33, 7.5, 7.6, 7.7))}),
    Item("Serum sodium", (0, 1, 2, 3, 4), _na, ("Sodium",), "numeric",
         {"Sodium": ("mmol/L", (111, 120, 130, 150, 155, 160, 180))}),
    Item("Serum potassium", (0, 1, 2, 3, 4), _k, ("Potassium",), "numeric",
         {"Potassium": ("mmol/L", (2.5, 3, 3.5, 5.5, 6, 7))}),
    Item("Serum creatinine", (0, 2, 3, 4, 6, 8), _creat,
         ("creatinine", "Acute renal failure", "Chronic renal failure"), "mixed",
         {"creatinine": ("mg/100 mL", (0.6, 1.5, 2, 3.5))}),
    Item("Hematocrit", (0, 1, 2, 4), _hct, ("Hematocrit",), "numeric", {"Hematocrit": ("%", (20, 30, 46, 50, 60))}),
    Item("White blood count", (0, 1, 2, 4), _wbc, ("White blood cell count",), "numeric",
         {"White blood cell count": ("10^3/mm^3", (1, 3, 15, 20, 40))}),
    Item("Glasgow Coma Scale (GCS)", tuple(range(13)), lambda e: 15 - int(num(e, "Glasgow Coma Score")),
         ("Glasgow Coma Score",), "numeric"),
), conventions=(
    "Chronic renal failure absent from the entities = no chronic renal failure (the explanation of such a row says "
    "'The patient is determined to not have a chronic renal failure').",
    "History of severe organ insufficiency = Yes with no Surgery Type released gives 0 points (the explanation says "
    "'surgery type being classified as None' and adds nothing to the total).",
    "PaO2 is released only when FiO2 < 50% and A-a gradient when FiO2 >= 50% (one row has both at FiO2 = 50% and "
    "uses the A-a gradient); neither is ever needed and absent.",
))
