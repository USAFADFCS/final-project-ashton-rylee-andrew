# tools/consent_check.py
from tools.base_tool import Tool

class ConsentCheckTool(Tool):
    """Scans text for consent-based phrasing and flags problematic patterns."""

    def __init__(self):
        super().__init__(
            name="check_consent",
            description="Ensures that messages use clear, respectful, and consent-based phrasing."
        )

    def use(self, message: str, context=None) -> str:
        flagged_terms = ["should", "must", "have to", "need to see you"]
        adjusted = False

        # Check for phrases that might imply pressure or lack of consent
        for term in flagged_terms:
            if term in message.lower():
                adjusted = True
                break

        if adjusted:
            if "if you’re comfortable" not in message.lower():
                message = message.strip() + " — if you’re comfortable, of course."

            message += " [⚠️ Adjusted: added consent phrasing]"

        return message
