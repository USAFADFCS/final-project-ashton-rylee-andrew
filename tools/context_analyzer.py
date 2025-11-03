# tools/context_analyzer.py
class ContextAnalyzerTool:
    """Determines conversation context and location."""
    name = "analyze_context"
    description = "Determines conversation context and location."

    def use(self, user_input: str) -> dict:
        """Analyze input to infer conversation situation and location context."""
        situation = "first_meeting" if "met" in user_input.lower() else "followup"
        location = "Colorado Springs"

        return {
            "situation": situation,
            "location": location
        }
