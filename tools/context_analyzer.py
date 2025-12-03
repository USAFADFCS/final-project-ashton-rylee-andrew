# tools/context_analyzer.py

class ContextAnalyzerTool:
    name = "analyze_context"
    description = "Analyzes the user's message to infer situation, energy, and social vibe."

    def use(self, user_input: str) -> dict:
        text = user_input.lower()

        # First time meeting vs followup
        if "just met" in text or "just met someone" in text or "met someone new" in text:
            situation = "first_meeting"
        else:
            situation = "followup"

        # Rough energy guess
        if "low energy" in text or "not too energy intensive" in text or "chill" in text:
            energy = "low"
        elif "hype" in text or "high energy" in text or "active" in text:
            energy = "high"
        else:
            energy = "medium"

        # Social preference (if mentioned)
        if "just us" in text or "one-on-one" in text or "just the two of us" in text:
            social = "one-on-one"
        elif "friends" in text or "group" in text:
            social = "small-group"
        else:
            social = "unspecified"

        # You can later make this dynamic (user’s city)
        location = "Colorado Springs"

        return {
            "situation": situation,
            "energy": energy,
            "social": social,
            "location": location,
        }
