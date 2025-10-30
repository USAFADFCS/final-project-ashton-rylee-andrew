# tools/context_analyzer.py
class ContextAnalyzerTool:
    """Determines conversation context and location."""

    def run(self, user_input: str) -> dict:
        context = {"situation": "first_meeting" if "met" in user_input.lower() else "followup"}
        context["location"] = "Colorado Springs"
        return context
