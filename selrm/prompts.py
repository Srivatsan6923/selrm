"""Frozen prompt builders (INTERFACES.md, section 2). Import these; do not
re-type prompts elsewhere. Chat templating is applied by the caller
(tokenizer.apply_chat_template(..., enable_thinking=False) for local models)."""

VERDICT = ("Rule: {rule}\n\nCase:\n{case}\n\nClaim: {claim}\n\n"
           "Is the claim correct for this case under the stated rule? Answer + or -.")

READER_LEDGER = ("Rule: {rule}\n\nCase:\n{case}\n\nCondition under test: {condition}\n\n"
                 "Write the evidence ledger for this condition: one entry per relevant "
                 "mention in the case, with the fields need, found, subject, status, time. "
                 "Quote the case verbatim in 'found' (or give the value). If nothing is "
                 "mentioned, write found: not mentioned. Record facts only; do not decide "
                 "any claim.")

READER_PROSE = ("Rule: {rule}\n\nCase:\n{case}\n\nCondition under test: {condition}\n\n"
                "Summarise in plain sentences what the case says that bears on this "
                "condition. Record facts only; do not decide any claim.")

JUDGE = ("Rule: {rule}\n\nEvidence record:\n{record}\n\nClaim: {claim}\n\n"
         "Is the claim correct under the stated rule, given only this record? Answer + or -.")

RATIONALE = ("Rule: {rule}\n\nCase:\n{case}\n\nClaim: {claim}\n\n"
             "First write the evidence record for the condition the claim depends on, "
             "then on a new line answer + or - for whether the claim is correct under "
             "the stated rule.")

CHOICE_SYSTEM = ("You check single steps of clinical reasoning against a patient case and a "
                 "stated rule. Apply the rule exactly as stated, even where it differs from "
                 "standard practice.")
CHOICE = ("Rule:\n{rule}\n\nCase:\n{case}\n\nWhich statement is correct for this patient "
          "under the rule?\nA. {a}\nB. {b}\n\nEnd your reply with a line of the form "
          "'Answer: A' or 'Answer: B'.")


def ledger_to_text(ledger: list) -> str:
    return "\n\n".join("\n".join(f"{k}: {e[k]}" for k in ("need", "found", "subject",
                                                           "status", "time"))
                       for e in ledger)


def verdict_prompt(rec):  return VERDICT.format(rule=rec["rule_text"], case=rec["case_text"], claim=rec["claim_text"])
def reader_prompt(rec, prose=False):
    return (READER_PROSE if prose else READER_LEDGER).format(
        rule=rec["rule_text"], case=rec["case_text"], condition=rec["condition"])
def judge_prompt(rec, record_text):
    return JUDGE.format(rule=rec["rule_text"], record=record_text, claim=rec["claim_text"])
def rationale_prompt(rec): return RATIONALE.format(rule=rec["rule_text"], case=rec["case_text"], claim=rec["claim_text"])
def choice_prompt(rule_text, case_text, a, b): return CHOICE.format(rule=rule_text, case=case_text, a=a, b=b)
def answer(rec): return "+" if rec["label"] == 1 else "-"
