"""Wells' Criteria for Pulmonary Embolism (Calculator ID 8), from the score text of the instances:

1. Clinical signs and symptoms of DVT: No = 0 points, Yes = +3 points
2. PE is #1 diagnosis OR equally likely: No = 0 points, Yes = +3 points
3. Heart rate > 100: No = 0 points, Yes = +1.5 points
4. Immobilization at least 3 days OR surgery in the previous 4 weeks: No = 0 points, Yes = +1.5 points
5. Previous, objectively diagnosed PE or DVT: No = 0 points, Yes = +1.5 points
6. Hemoptysis: No = 0 points, Yes = +1 point
7. Malignancy with treatment within 6 months or palliative: No = 0 points, Yes = +1 point
"""
from selrm.mcv import Item, Score, flag, num

DVT = "Clinical signs and symptoms of Deep Vein Thrombosis"
PE1 = "Pulmonary Embolism is #1 diagnosis OR equally likely"
HR = "Heart Rate or Pulse"
IMMOB, SURG = "Immobilization for at least 3 days", "Surgery in the previous 4 weeks"
PREV_PE, PREV_DVT = "Previously Documented Pulmonary Embolism", "Previously documented Deep Vein Thrombosis"
HEMO = "Hemoptysis"
MALIG = "Malignancy with treatment within 6 months or palliative"
BPM = {"beats per minute": 1, "beats/min": 1, "beats/minute": 1, "bpm": 1, "per min": 1}


def _hr(e):
    v = num(e, HR, BPM)
    return 1.5 * (v is not None and v > 100)


SCORE = Score(8, "Wells' Criteria for Pulmonary Embolism", (
    Item("Clinical signs and symptoms of DVT", (0, 3), lambda e: 3 * flag(e, DVT), (DVT,), "finding"),
    Item("PE is #1 diagnosis OR equally likely", (0, 3), lambda e: 3 * flag(e, PE1), (PE1,), "finding"),
    Item("Heart rate", (0, 1.5), _hr, (HR,), "numeric", {HR: ("beats per minute", (100,))}),
    Item("Immobilization at least 3 days OR surgery in the previous 4 weeks", (0, 1.5),
         lambda e: 1.5 * (flag(e, IMMOB) or flag(e, SURG)), (IMMOB, SURG), "finding",
         support={"window": "in the previous 4 weeks"}),
    Item("Previous, objectively diagnosed PE or DVT", (0, 1.5),
         lambda e: 1.5 * (flag(e, PREV_PE) or flag(e, PREV_DVT)), (PREV_PE, PREV_DVT), "finding",
         time="ever", support={"time": "Previous, objectively diagnosed"}),
    Item("Hemoptysis", (0, 1), lambda e: int(flag(e, HEMO)), (HEMO,), "finding"),
    Item("Malignancy with treatment within 6 months or palliative", (0, 1), lambda e: int(flag(e, MALIG)), (MALIG,),
         "finding", support={"window": "within 6 months"}),
), conventions=(
    "Unmentioned signs of DVT are absent ('not reported and so we assume that this is missing from the patient').",
    "Unmentioned 'PE is #1 diagnosis' is No ('not reported to be the #1 diagnosis and so the total score remains "
    "unchanged').",
    "Unmentioned immobilization or surgery is No ('does not give an indication ... and so we assume this to be "
    "false').",
    "Unmentioned previous PE or previous DVT is No ('does not give an indication ... and so we assume this to be "
    "false').",
    "Unmentioned hemoptysis is absent ('not reported in the patient note and so we assume that it is missing').",
    "Unmentioned malignancy is absent ('not reported in the patient note and so we assume that this is absent').",
))
