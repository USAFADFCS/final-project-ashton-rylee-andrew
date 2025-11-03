# tools/tone_adjuster.py
class ToneAdjusterTool:
    """Rewrites the tone of a message to be warm and confident."""
    name = "adjust_tone"
    description = "Rewrites the tone of a message to be warm and confident."

    def use(self, message: str, context: dict = None) -> str:
        """Adjusts message tone to sound warmer and more confident."""
        if context is None:
            context = {}

        # Normalize and enhance tone
        msg = message.replace("hey", "Hi").replace("!", " 🙂")

        # Add warmth for first-meeting scenarios
        if "first_meeting" in context.get("situation", ""):
            msg = f"It was nice meeting you! {msg}"

        return msg
