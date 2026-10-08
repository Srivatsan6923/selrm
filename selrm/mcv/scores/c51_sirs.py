"""SIRS Criteria (Calculator ID 51), from the score text of the instances:

1. Temperature >38°C (100.4°F) or <36°C (96.8°F): No = 0 points, Yes = +1 point
2. Heart rate >90: No = 0 points, Yes = +1 point
3. Respiratory rate >20 or PaCO₂ <32 mm Hg: No = 0 points, Yes = +1 point
4. White blood cell count (WBC) >12,000/mm³, <4,000/mm³: No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, num

PER_MIN = {"beats per minute": 1, "beats/min": 1, "beats/minute": 1, "bpm": 1}
BREATHS = {"breaths per minute": 1, "breaths/min": 1, "breaths/minute": 1, "cycles per minute": 1,
           "mid’s breaths per minute": 1}
CELSIUS = {"degrees celsius": 1, "degrees fahrenheit": lambda f: (f - 32) * 5 / 9}
PER_MM3 = {"mm^3": 1, "µl": 1, "ml": 1e-3, "dl": 1e-5, "l": 1e-6}   # released unit is the volume of the count


def _temp(e):
    v = num(e, "Temperature", CELSIUS)
    return int(v is not None and (v > 38 or v < 36))


def _hr(e):
    v = num(e, "Heart Rate or Pulse", PER_MIN)
    return int(v is not None and v > 90)


def _rr(e):
    r, p = num(e, "respiratory rate", BREATHS), num(e, "PaCO2", {"mm hg": 1, "mmhg": 1})
    return int((r is not None and r > 20) or (p is not None and p < 32))


def _wbc(e):
    v = num(e, "White blood cell count", PER_MM3)
    return int(v is not None and (v > 12000 or v < 4000))


SCORE = Score(51, "SIRS Criteria", (
    Item("Temperature", (0, 1), _temp, ("Temperature",), "numeric", {"Temperature": ("°C", (36, 38))}),
    Item("Heart rate", (0, 1), _hr, ("Heart Rate or Pulse",), "numeric",
         {"Heart Rate or Pulse": ("beats per minute", (90,))}),
    Item("Respiratory rate or PaCO₂", (0, 1), _rr, ("respiratory rate", "PaCO2"), "numeric",
         {"respiratory rate": ("breaths per minute", (20,)), "PaCO2": ("mm Hg", (32,))}),
    Item("White blood cell count (WBC)", (0, 1), _wbc, ("White blood cell count",), "numeric",
         {"White blood cell count": ("/mm³", (4000, 12000))}),
), conventions=(
    "An absent PaCO2 does not meet the criterion (\"The patient's PaCO₂ partial pressure is not provided and so we "
    "assume that the patient's partial pressure is greater than or equal to 32 mm Hg\").",
))
