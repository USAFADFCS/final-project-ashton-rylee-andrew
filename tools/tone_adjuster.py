# tools/tone_adjuster.py
class ToneAdjusterTool:
    """Rewrites the tone of a message to be warm and confident."""

    def run(self, message: str, context: dict) -> str:
        message = message.replace("hey", "Hi").replace("!", " 🙂")
        if "first_meeting" in context.get("situation", ""):
            message = "It was nice meeting you! " + message
        return message
