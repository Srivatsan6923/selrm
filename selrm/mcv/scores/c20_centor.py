"""Centor Score (Modified/McIsaac) for Strep Pharyngitis (Calculator ID 20), from the score text of the instances:

1. Age: 3-14 years = +1 point, 15-44 years = 0 points, >=45 years = -1 point
2. Exudate or swelling on tonsils: No = 0 points, Yes = +1 point
3. Tender/swollen anterior cervical lymph nodes: No = 0 points, Yes = +1 point
4. Temperature >38 C (100.4 F): No = 0 points, Yes = +1 point
5. Cough: Cough present = 0 points, Cough absent = +1 point
"""
from selrm.mcv import Item, Score, flag, num

TONSILS, NODES = "Exudate or swelling on tonsils", "Tender/swollen anterior cervical lymph nodes"


def _age(e):
    # the score text is silent below 3 years; the explanations of such rows leave the score unchanged
    v = num(e, "age", {"years": 1, "months": 1 / 12})
    return 0 if v is None or v < 3 else 1 if v < 15 else 0 if v < 45 else -1


def _temp(e):
    # "To convert to degrees celsius, apply the formula 5/9 * [temperature (degrees fahrenheit) - 32]";
    # rounded so that 100.4 F is exactly the 38 C of the score text
    v = num(e, "Temperature", {"degrees celsius": 1, "degrees fahrenheit": lambda f: round(5 / 9 * (f - 32), 3)})
    return int(v is not None and v > 38)


SCORE = Score(20, "Centor Score (Modified/McIsaac) for Strep Pharyngitis", (
    Item("Age", (-1, 0, 1), _age, ("age",), "numeric", {"age": ("years", (3, 15, 45))}),
    Item("Exudate or swelling on tonsils", (0, 1), lambda e: int(flag(e, TONSILS)), (TONSILS,), "finding"),
    Item("Tender/swollen anterior cervical lymph nodes", (0, 1), lambda e: int(flag(e, NODES)), (NODES,), "finding"),
    Item("Temperature", (0, 1), _temp, ("Temperature",), "numeric", {"Temperature": ("degrees celsius", (38,))}),
    Item("Cough", (0, 1), lambda e: int(flag(e, "Cough Absent", absent=True)), ("Cough Absent",), "finding"),
), conventions=(
    "Unmentioned tonsillar exudate/swelling or cervical nodes are absent, 0 points (\"The patient note does not "
    "mention details about 'exudate or swelling on tonsils' and so we assume it to be absent\").",
    "An unmentioned cough is absent, +1 point (\"The patient note does not mention details about the patient "
    "coughing and so we assume it to be absent. Hence, we add 1 point\").",
    "Age below 3 years gives 0 points (rows with age in months: the explanation converts the age and makes no "
    "change to the score).",
))
