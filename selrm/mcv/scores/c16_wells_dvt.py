"""Wells' Criteria for DVT (Calculator ID 16), from the score text of the instances:

1. Active cancer (treatment or palliation within 6 months): No = 0 points, Yes = +1 point
2. Bedridden recently >3 days or major surgery within 12 weeks: No = 0 points, Yes = +1 point
3. Calf swelling >3 cm compared to the other leg (measured 10 cm below tibial tuberosity): No = 0 points, Yes = +1 point
4. Collateral (nonvaricose) superficial veins present: No = 0 points, Yes = +1 point
5. Entire leg swollen: No = 0 points, Yes = +1 point
6. Localized tenderness along the deep venous system: No = 0 points, Yes = +1 point
7. Pitting edema, confined to symptomatic leg: No = 0 points, Yes = +1 point
8. Paralysis, paresis, or recent plaster immobilization of the lower extremity: No = 0 points, Yes = +1 point
9. Previously documented DVT: No = 0 points, Yes = +1 point
10. Alternative diagnosis to DVT as likely or more likely: No = 0 points, Yes = -2 points
"""
from selrm.mcv import Item, Score, flag

BED, SURGERY = "Bedridden recently >3 days", "Major surgery within 12 weeks"
ALT = "Alternative diagnosis to Deep Vein Thrombosis as likely or more likely"


def _finding(name, key, time="unstated", phrase=None):
    return Item(name, (0, 1), lambda e: int(flag(e, key)), (key,), "finding",
                time=time, support={"time": phrase} if phrase else {})


SCORE = Score(16, "Wells' Criteria for DVT", (
    _finding("Active cancer", "Active cancer", "unstated", "Active cancer (treatment or palliation within 6 months)"),
    Item("Bedridden recently or major surgery", (0, 1), lambda e: int(flag(e, BED) or flag(e, SURGERY)),
         (BED, SURGERY), "finding", support={"window": "Bedridden recently >3 days or major surgery within 12 weeks"}),
    # the released entity is the finding itself (True/False); no calf measurement is released
    _finding("Calf swelling compared to the other leg", "Calf swelling >3 centimeters compared to the other leg"),
    _finding("Collateral (nonvaricose) superficial veins present", "Collateral (nonvaricose) superficial veins present",
             "current", "present"),
    _finding("Entire leg swollen", "Entire Leg Swollen"),
    _finding("Localized tenderness along the deep venous system", "Localized tenderness along the deep venous system"),
    _finding("Pitting edema, confined to symptomatic leg", "Pitting edema, confined to symptomatic leg"),
    _finding("Paralysis, paresis, or recent plaster immobilization of the lower extremity",
             "Paralysis, paresis, or recent plaster immobilization of the lower extremity",
             "unstated", "recent plaster immobilization"),
    _finding("Previously documented DVT", "Previously documented Deep Vein Thrombosis", "ever", "Previously documented"),
    Item("Alternative diagnosis to DVT as likely or more likely", (0, -2), lambda e: -2 * flag(e, ALT), (ALT,),
         "finding"),
), conventions=(
    "An unmentioned finding is absent (\"The issue,'active cancer,' is missing from the patient note and so the "
    "value is assumed to be absent from the patient. Hence, a point should not be given\").",
    "Item 2 needs only one of its two findings; an unmentioned one is absent (\"'major surgery within 12 weeks,' is "
    "missing from the patient note and so the value is assumed to be absent ... at least one of the criteria ... "
    "must be true for this criteria to be met\").",
))
