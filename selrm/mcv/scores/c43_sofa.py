"""Sequential Organ Failure Assessment (SOFA) Score (Calculator ID 43), from the score text of the instances:

1. PaO2/FiO2 ratio (mm Hg): >=400 = 0 points, 300-399 = +1 point, 200-299 = +2 points, < 200 and NOT mechanically
   ventillated = +2 points, 100-199 (with mechanical ventilation) = +3 points, <= 199, <100 (with respiratory
   support) = +4 points
2. Platelets (x10^3/uL): >=150 = 0 points, 100-149 = +1 point, 50-99 = +2 points, 20-49 = +3 points, <20 = +4 points
3. Glasgow Coma Scale (GCS): 15 = 0 points, 13-14 = +1 point, 10-12 = +2 points, 6-9 = +3 points, <6 = +4 points
4. Bilirubin (mg/dL): <1.2 = 0 points, 1.2-1.9 = +1 point, 2.0-5.9 = +2 points, 6.0-11.9 = +3 points,
   >=12.0 = +4 points
5. Mean arterial pressure (MAP) or administration of vasopressors (in mcg): No hypotension = 0 points,
   MAP <70 mmHg = +1 point, Dopamine <=5 or Dobutamine (any dose) = +2 points, Dopamine >5 or Epinephrine <=0.1 or
   norepinephrine <=0.1 = +3 points, Dopamine >15 or Epinephrine >0.1 or norepinephrine >0.1 = +4 points
6. Creatinine (mg/dL) or urine output: <1.2 = 0 points, 1.2-<2.0 = +1 point, 2.0-<3.5 = +2 points, 3.5-<5.0 or
   urine output <500 mL/day = +3 points, >=5.0 or urine output <200 mL/day = +4 points
"""
from selrm.mcv import Item, Score, flag, num

MMHG, MCG = {"mm hg": 1}, {"mcg/kg/min": 1}
DRUGS = ("DOPamine", "DOBUTamine", "EPINEPHrine", "norEPINEPHrine")


def _band(v, cuts):
    """Number of cuts that v lies below (cuts descending): 0 points at or above the first cut."""
    return sum(v < c for c in cuts)


def _resp(e):
    ratio = num(e, "PaO2", MMHG) / (num(e, "FiO2", {"%": 1}) / 100)
    support = flag(e, "On mechanical ventilation") or flag(e, "Continuous positive airway pressure")
    if ratio >= 200 or not support:
        return min(_band(ratio, (400, 300)), 2)
    return 3 if ratio >= 100 else 4


def _platelets(e):
    return _band(num(e, "Platelet count", {"µl": 1e-3}), (150, 100, 50, 20))


def _gcs(e):
    return _band(num(e, "Glasgow Coma Score"), (15, 13, 10, 6))


def _bili(e):
    v = num(e, "Bilirubin", {"mg/dl": 1})
    return sum(v >= c for c in (1.2, 2, 6, 12))


def _cardio(e):
    dop, dob, epi, nor = (num(e, k, MCG) or 0 for k in DRUGS)
    if dop > 15 or epi > 0.1 or nor > 0.1:
        return 4
    if dop > 5 or epi > 0 or nor > 0:
        return 3
    if dop > 0 or dob > 0:
        return 2
    if not flag(e, "Hypotension"):
        return 0
    s, d = num(e, "Systolic Blood Pressure", MMHG), num(e, "Diastolic Blood Pressure", MMHG)
    return int(s is not None and d is not None and (s + 2 * d) / 3 < 70)   # MAP = (systolic + 2 diastolic) / 3


def _renal(e):
    c, u = num(e, "creatinine", {"mg/dl": 1}), num(e, "Urine Output", {"ml/day": 1})
    return max(sum(c >= x for x in (1.2, 2, 3.5, 5)), 4 if u < 200 else 3 if u < 500 else 0)


SCORE = Score(43, "Sequential Organ Failure Assessment (SOFA) Score", (
    Item("PaO2/FiO2 ratio", (0, 1, 2, 3, 4), _resp,
         ("PaO2", "FiO2", "On mechanical ventilation", "Continuous positive airway pressure"), "mixed",
         {"PaO2": ("mm Hg", (400, 300, 200, 100))}),   # cuts of the ratio PaO2 / (FiO2 % / 100)
    Item("Platelets", (0, 1, 2, 3, 4), _platelets, ("Platelet count",), "numeric",
         {"Platelet count": ("x10^3/µL", (150, 100, 50, 20))}),
    Item("Glasgow Coma Scale (GCS)", (0, 1, 2, 3, 4), _gcs, ("Glasgow Coma Score",), "numeric",
         {"Glasgow Coma Score": ("points", (15, 13, 10, 6))}),
    Item("Bilirubin", (0, 1, 2, 3, 4), _bili, ("Bilirubin",), "numeric",
         {"Bilirubin": ("mg/dL", (1.2, 2.0, 6.0, 12.0))}),
    Item("Mean arterial pressure (MAP) or administration of vasopressors", (0, 1, 2, 3, 4), _cardio,
         ("Hypotension", "Systolic Blood Pressure", "Diastolic Blood Pressure") + DRUGS, "mixed",
         {"Systolic Blood Pressure": ("mmHg", (70,)), "Diastolic Blood Pressure": ("mmHg", (70,)),
          "DOPamine": ("mcg/kg/min", (5, 15)), "EPINEPHrine": ("mcg/kg/min", (0.1,)),
          "norEPINEPHrine": ("mcg/kg/min", (0.1,))}),
    Item("Creatinine or urine output", (0, 1, 2, 3, 4), _renal, ("creatinine", "Urine Output"), "mixed",
         {"creatinine": ("mg/dL", (1.2, 2.0, 3.5, 5.0)), "Urine Output": ("mL/day", (500, 200))}),
), conventions=(
    "Unreported mechanical ventilation is absent ('Whether the patient is on mechanical ventillation is not "
    "reported and so we assume this to be false').",
    "Unreported continuous positive airway pressure is absent ('Whether the patient is on continuous positive "
    "airway pressure is not reported and so we assume this to be false').",
    "Unreported hypotension gives 0 points without a vasopressor ('Whether the patient has hypotension is not "
    "reported, and so we do not add any points to the score').",
    "A vasopressor that is not released is not given (the explanations test only the released doses; no "
    "explanation sentence states this).",
))
