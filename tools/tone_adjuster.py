# tools/tone_adjuster.py

class ToneAdjusterTool:
    name = "adjust_tone"
    description = "Lightly adjusts the tone of the message based on context (situation, energy)."

    def use(self, message: str, context: dict | None = None) -> str:
        context = context or {}
        msg = message

        # Example: tweak for first meeting
        situation = context.get("situation")
        if situation == "first_meeting" and "nice meeting you" not in msg.lower():
            msg = f"It was nice meeting you! {msg}"

        # Example: gentle emoji for low-energy invites
        energy = context.get("energy")
        if energy == "low":
            msg = msg.replace("!", " 🙂")

        return msg
