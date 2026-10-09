"""Charlson Comorbidity Index (CCI) (Calculator ID 32), from the score text of the instances:

1. Age: <50 years = 0 points, 50-59 years = +1 point, 60-69 years = +2 points, 70-79 years = +3 points,
   >=80 years = +4 points
2. Myocardial infarction (history of definite or probable MI with EKG changes and/or enzyme changes):
   No = 0 points, Yes = +1 point
3. Congestive heart failure (CHF) (exertional or paroxysmal nocturnal dyspnea, responsive to digitalis, diuretics,
   or afterload reducing agents): No = 0 points, Yes = +1 point
4. Peripheral vascular disease (intermittent claudication, past bypass for chronic arterial insufficiency, history
   of gangrene or acute arterial insufficiency, untreated thoracic or abdominal aneurysm >=6 cm):
   No = 0 points, Yes = +1 point
5. Cerebrovascular accident (CVA) or transient ischemic attack (TIA): No = 0 points, Yes = +1 point
6. Dementia (chronic cognitive deficit): No = 0 points, Yes = +1 point
7. Chronic pulmonary disease (CPD): No = 0 points, Yes = +1 point
8. Connective tissue disease: No = 0 points, Yes = +1 point
9. Peptic ulcer disease (any history of treatment for ulcer disease or ulcer bleeding): No = 0 points, Yes = +1 point
10. Liver disease: None = 0 points, Mild = +1 point, Moderate to severe = +3 points
11. Diabetes mellitus: None or diet-controlled = 0 points, Uncomplicated = +1 point, End-organ damage = +2 points
12. Hemiplegia: No = 0 points, Yes = +2 points
13. Moderate to severe chronic kidney disease (CKD): No = 0 points, Yes = +2 points
14. Solid tumor: None = 0 points, Localized = +2 points, Metastatic = +6 points
15. Leukemia: No = 0 points, Yes = +2 points
16. Lymphoma: No = 0 points, Yes = +2 points
17. AIDS: No = 0 points, Yes = +6 points
"""
from selrm.mcv import Item, Score, flag, num

CVA, TIA = "Cerebrovascular Accident", "Transient Ischemic Attacks History"
LIVER = {"none": 0, "mild": 1, "moderate to severe": 3}
DM = {"none or diet-controlled": 0, "uncomplicated": 1, "end-organ damage": 2}
TUMOR = {"none": 0, "localized": 2, "metastatic": 6}


def _age(e):
    v = num(e, "age", {"years": 1})
    return 0 if v is None else sum(v >= c for c in (50, 60, 70, 80))


def _yes(key, pts, name=None, **kw):
    return Item(name or key, (0, pts), lambda e: pts * flag(e, key), (key,), "finding", **kw)


def _graded(key, table, name):
    # an undetermined grade takes the 0-point level of the score text
    return Item(name, tuple(table.values()), lambda e: table[str(e.get(key, next(iter(table)))).strip().lower()],
                (key,), "finding")


SCORE = Score(32, "Charlson Comorbidity Index (CCI)", (
    Item("Age", (0, 1, 2, 3, 4), _age, ("age",), "numeric", {"age": ("years", (50, 60, 70, 80))}),
    _yes("Myocardial infarction", 1, time="ever", support={"time": "history of definite or probable MI"}),
    _yes("Congestive Heart Failure", 1, "Congestive heart failure"),
    _yes("Peripheral vascular disease", 1,
         support={"time": "past bypass for chronic arterial insufficiency, history of gangrene or acute arterial "
                          "insufficiency"}),
    Item("Cerebrovascular accident or transient ischemic attack", (0, 1), lambda e: int(flag(e, CVA) or flag(e, TIA)),
         (CVA, TIA), "finding"),
    _yes("Dementia", 1),
    _yes("Chronic Pulmonary Disease", 1, "Chronic pulmonary disease"),
    _yes("Connective tissue disease", 1),
    _yes("Peptic ulcer disease", 1, time="ever",
         support={"time": "any history of treatment for ulcer disease or ulcer bleeding"}),
    _graded("Liver disease severity", LIVER, "Liver disease"),
    _graded("Diabetes mellitus", DM, "Diabetes mellitus"),
    _yes("Hemiplegia", 2),
    _yes("Moderate to severe Chronic Kidney Disease", 2, "Moderate to severe chronic kidney disease"),
    _graded("Solid tumor", TUMOR, "Solid tumor"),
    _yes("Leukemia", 2),
    _yes("Lymphoma", 2),
    _yes("AIDS", 6),
), conventions=(
    "An unmentioned issue is absent (\"is not mentioned in the patient note and so we assume it to be absent for "
    "the patient. We do not add any points\").",
    "CVA or TIA: an unmentioned one of the two is absent (\"Transient ischemic attacks is not mentioned for the "
    "patient and so we assume it to be absent\"); one present is enough for the point.",
    "Undetermined diabetes status is 'none or diet-controlled' (\"is not determined and so we assume the value to "
    "be 'none or diet-controlled.' No points are added\").",
    "Undetermined solid tumor is 'none' (\"status is not determined and so we assume that it is 'none.' Hence, do "
    "not add any points\").",
    "Undetermined liver disease gives 0 points, i.e. 'none' (\"The patient's liver disease status is not determined "
    "... No points are added\"; the explanation names the default 'none or diet-controlled', the diabetes wording).",
))
