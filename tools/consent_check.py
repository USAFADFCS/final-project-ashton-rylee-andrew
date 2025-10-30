# tools/consent_check.py
class ConsentCheckTool:
    """Scans text for consent-based phrasing and flags problematic patterns."""

    def run(self, message: str) -> str:
        flagged_terms = ["should", "must", "have to", "need to see you"]
        if any(term in message.lower() for term in flagged_terms):
            message += " [⚠️ Adjusted: added consent phrasing]"
            if "if you’re comfortable" not in message.lower():
                message = message.strip() + " — if you’re comfortable, of course."
        return message
