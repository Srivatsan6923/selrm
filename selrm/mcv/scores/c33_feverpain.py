"""FeverPAIN Score for Strep Pharyngitis (Calculator ID 33), from the score text of the instances:

1. Fever in past 24 hours: No = 0 points, Yes = +1 point
2. Absence of cough or coryza: No = 0 points, Yes = +1 point
3. Symptom onset <=3 days: No = 0 points, Yes = +1 point
4. Purulent tonsils: No = 0 points, Yes = +1 point
5. Severe tonsil inflammation: No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag


def _item(name, key, absent=False, **kw):
    return Item(name, (0, 1), lambda e: int(flag(e, key, absent)), (key,), "finding", **kw)


SCORE = Score(33, "FeverPAIN Score for Strep Pharyngitis", (
    _item("Fever in past 24 hours", "Fever in past 24 hours", support={"window": "in past 24 hours"}),
    # the entity is the criterion itself (True = no cough or coryza); an unmentioned one scores the point
    _item("Absence of cough or coryza", "Absence of cough or coryza", absent=True),
    _item("Symptom onset", "Symptom onset <=3 days"),
    _item("Purulent tonsils", "Purulent tonsils"),
    _item("Severe tonsil inflammation", "Severe tonsil inflammation"),
), conventions=(
    "An unmentioned fever, purulent tonsils or severe tonsil inflammation is absent, 0 points ('is not reported and "
    "so we assume that it is absent for the patient. Because of this, we do not increment the score').",
    "An unmentioned 'Absence of cough or coryza' gives +1: cough and coryza are taken as absent ('Whether the "
    "patient has an absence of cough or coryza is not reported and so we assume that it is absent for the patient. "
    "Because of this, we add one point to the score').",
    "'Symptom onset <=3 days' is released in every row; no absent-key text exists, the default (0 points) is unused.",
))
