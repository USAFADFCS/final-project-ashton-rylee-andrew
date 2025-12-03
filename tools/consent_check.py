# tools/consent_check.py

class ConsentCheckTool:
    name = "check_consent"
    description = "Ensures the message respects consent and gives an easy opt-out."

    def use(self, message: str, context: dict | None = None) -> str:
        context = context or {}
        msg = message

        flagged_terms = ["should", "must", "have to", "need to see you"]
        lower = msg.lower()

        if any(term in lower for term in flagged_terms) and "if you're comfortable" not in lower:
            msg = msg.rstrip(".") + " — if you're comfortable, of course."

        return msg
