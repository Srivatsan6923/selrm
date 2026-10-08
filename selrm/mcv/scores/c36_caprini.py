"""Caprini Score for Venous Thromboembolism (2005) (Calculator ID 36), from the score text of the instances:

1. Age, years: <=40 = 0 points, 41-60 = +1 point, 61-74 = +2 points, >=75 = +3 points
2. Type of surgery: None = 0 points, Minor = +1 point, Major >45 min (laparoscopic or arthroscopic) = +2 points,
   Elective major lower extremity arthroplasty = +5 points
3. Recent (<=1 month) event: Major surgery = +1 point, Congestive heart failure (CHF) = +1 point, Sepsis = +1 point,
   Pneumonia = +1 point, Immobilizing plaster cast = +2 points, Hip, pelvis, or leg fracture = +5 points,
   Stroke = +5 points, Multiple trauma = +5 points, Acute spinal cord injury causing paralysis = +5 points
4. Venous disease or clotting disorder: Varicose veins = +1 point, Current swollen legs = +1 point,
   Current central venous access = +2 points, History of deep vein thrombosis (DVT) or pulmonary embolism (PE) =
   +3 points, Family history of thrombosis = +3 points, Positive Factor V Leiden = +3 points,
   Positive prothrombin 20210A = +3 points, Elevated serum homocysteine = +3 points, Positive lupus anticoagulant =
   +3 points, Elevated anticardiolipin antibody = +3 points, Heparin-induced thrombocytopenia = +3 points,
   Other congenital or acquired thrombophilia = +3 points
5. Mobility: Normal, out of bed = 0 points, Medical patient currently on bed rest = +1 point,
   Patient confined to bed >72 hours = +2 points
6. Other present and past history: History of inflammatory bowel disease = +1 point, BMI > 25 = +1 point,
   Acute myocardial infarction = +1 point, Chronic obstructive pulmonary disease (COPD) = +1 point,
   Present or previous malignancy = +2 points

Criteria 3, 4 and 6 score each listed entry separately, so each entry is one item.
"""
from selrm.mcv import Item, Score, flag, num

SURGERY = {"minor": 1, "major": 2, "laparoscopic": 2, "arthroscopic": 2,
           "elective major lower extremity arthroplasty": 5}
MOBILITY = {"normal": 0, "on bed rest": 1, "confined to bed >72 hours": 2}
RECENT = {"window": "Recent (<=1 month) event"}
PAST = {"time": "Other present and past history"}
DVT, PE = "Previously documented Deep Vein Thrombosis", "Previously Documented Pulmonary Embolism"


def _age(e):
    v = num(e, "age", {"years": 1})
    return 0 if v is None or v <= 40 else 1 if v <= 60 else 2 if v <= 74 else 3


def _bmi(e):
    v = num(e, "Body Mass Index (BMI)", {"kg/m^2": 1})
    return int(v is not None and v > 25)


def _finding(name, pts, key, time="unstated", support=None):
    return Item(name, (0, pts), lambda e: pts * flag(e, key), (key,), "finding", time=time, support=support or {})


SCORE = Score(36, "Caprini Score for Venous Thromboembolism (2005)", (
    Item("Age", (0, 1, 2, 3), _age, ("age",), "numeric", {"age": ("years", (40, 60, 74))}),
    Item("Type of surgery", (0, 1, 2, 5), lambda e: SURGERY.get(e.get("Surgery Type"), 0), ("Surgery Type",),
         "finding"),
    _finding("Major surgery", 1, "Major Surgery in the last month", "unstated", RECENT),
    _finding("Congestive heart failure (CHF)", 1, "Congestive Heart Failure in the last month", "unstated", RECENT),
    _finding("Sepsis", 1, "Sepsis in the last month", "unstated", RECENT),
    _finding("Pneumonia", 1, "Pneumonia in the last month", "unstated", RECENT),
    _finding("Immobilizing plaster cast", 2, "Immobilizing plaster cast in the last month", "unstated", RECENT),
    _finding("Hip, pelvis, or leg fracture", 5, "Hip, pelvis, or leg fracture in the last month", "unstated", RECENT),
    _finding("Stroke", 5, "Stroke in the last month", "unstated", RECENT),
    _finding("Multiple trauma", 5, "Multiple trauma in the last month", "unstated", RECENT),
    _finding("Acute spinal cord injury causing paralysis", 5,
             "Acute spinal cord injury causing paralysis in the last month", "unstated", RECENT),
    _finding("Varicose veins", 1, "Varicose veins"),
    _finding("Current swollen legs", 1, "Current swollen legs", "current", {"time": "Current swollen legs"}),
    _finding("Current central venous access", 2, "Current central venous access", "current",
             {"time": "Current central venous access"}),
    Item("History of deep vein thrombosis (DVT) or pulmonary embolism (PE)", (0, 3),
         lambda e: 3 * (flag(e, DVT) or flag(e, PE)), (DVT, PE), "finding", time="ever",
         support={"time": "History of deep vein thrombosis (DVT) or pulmonary embolism (PE)"}),
    Item("Family history of thrombosis", (0, 3), lambda e: 3 * flag(e, "Family history of thrombosis"),
         ("Family history of thrombosis",), "finding", subject="family", time="ever",
         support={"time": "Family history of thrombosis", "subject": "Family history of thrombosis"}),
    _finding("Positive Factor V Leiden", 3, "Positive Factor V Leiden"),
    _finding("Positive prothrombin 20210A", 3, "Positive prothrombin 20210A"),
    _finding("Elevated serum homocysteine", 3, "Elevated serum homocysteine"),
    _finding("Positive lupus anticoagulant", 3, "Positive lupus anticoagulant"),
    _finding("Elevated anticardiolipin antibody", 3, "Elevated anticardiolipin antibody"),
    _finding("Heparin-induced thrombocytopenia", 3, "Heparin-induced thrombocytopenia"),
    _finding("Other congenital or acquired thrombophilia", 3, "Other congenital or acquired thrombophilia"),
    Item("Mobility", (0, 1, 2), lambda e: MOBILITY.get(e.get("Mobility"), 0), ("Mobility",), "finding", time="current",
         support={"time": "Medical patient currently on bed rest"}),
    _finding("History of inflammatory bowel disease", 1, "History of inflammatory bowel disease", "ever",
             {"time": "History of inflammatory bowel disease"}),
    Item("BMI", (0, 1), _bmi, ("Body Mass Index (BMI)",), "numeric", {"Body Mass Index (BMI)": ("kg/m^2", (25,))},
         support=PAST),
    _finding("Acute myocardial infarction", 1, "Acute Myocardial infarction", "ever", PAST),
    _finding("Chronic obstructive pulmonary disease (COPD)", 1, "Chronic Obstructive Pulmonary Disease", "ever", PAST),
    _finding("Present or previous malignancy", 2, "Present or previous malignancy", "ever",
             {"time": "Present or previous malignancy"}),
), conventions=(
    "An unmentioned finding is absent ('The patient does not report anything about stroke in the last month and so "
    "we assume this to be false. Hence, 0 points are added').",
    "An unreported BMI gives 0 points ('The patient does not report anything about b[mi] and so we assume this to be "
    "false. Hence, 0 points are added').",
    "Surgery type 'major' scores as Major >45 min ('surgery type is determined to be 'major'. Hence, we add 2 "
    "points').",
))
