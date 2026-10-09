"""Glasgow Coma Score (GCS) (Calculator ID 21), from the score text of the instances:

1. Best Eye Response: Spontaneously = +4 points, To verbal command = +3 points, To pain = +2 points,
   No eye opening = +1 point
2. Best Verbal Response: Oriented = +5 points, Confused = +4 points, Inappropriate words = +3 points,
   Incomprehensible sounds = +2 points, No verbal response = +1 point
3. Best Motor Response: Obeys commands = +6 points, Localizes pain = +5 points, Withdrawal from pain = +4 points,
   Flexion to pain = +3 points, Extension to pain = +2 points, No motor response = +1 point

For each criteria, if a patient's value is not mentioned/not testable in the note, we assume that it gets the full
score for that attribute.
"""
from selrm.mcv import Item, Score

EYE = {"eyes open spontaneously": 4, "eye opening to verbal command": 3, "eye opening to pain": 2,
       "no eye opening": 1}
VERBAL = {"oriented": 5, "confused": 4, "inappropriate words": 3, "incomprehensible sounds": 2,
          "no verbal response": 1}
MOTOR = {"obeys commands": 6, "localizes pain": 5, "withdrawal from pain": 4, "flexion to pain": 3,
         "extension to pain": 2, "no motor response": 1}


def _level(key, table):
    # an absent key gets the full score of the component; a released value outside the table raises
    full = max(table.values())
    return lambda e: table[str(e[key]).strip().lower()] if key in e else full


SCORE = Score(21, "Glasgow Coma Score (GCS)", (
    Item("Best Eye Response", (1, 2, 3, 4), _level("Best eye response", EYE), ("Best eye response",), "finding"),
    Item("Best Verbal Response", (1, 2, 3, 4, 5), _level("Best verbal response", VERBAL), ("Best verbal response",),
         "finding"),
    Item("Best Motor Response", (1, 2, 3, 4, 5, 6), _level("Best motor response", MOTOR), ("Best motor response",),
         "finding"),
), conventions=(
    "An absent component gets its full score (score text: \"if a patient's value is not mentioned/not testable in "
    "the note, we assume that it gets the full score for that attribute\").",
))
