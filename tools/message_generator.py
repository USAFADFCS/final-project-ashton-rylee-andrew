# tools/message_generator.py
class MessageGeneratorTool:
    """Generates a first-draft friendly message based on user intent."""

    def run(self, user_input: str, context: dict) -> str:
        situation = context.get("situation", "")
        if "gym" in user_input.lower():
            return "Hey, it was great meeting you at the gym! How’s your workout routine going lately?"
        elif "class" in user_input.lower():
            return "Hi! I really enjoyed talking with you in class the other day — how’s your week going?"
        elif "coffee" in user_input.lower():
            return "Hi there! Want to grab coffee again sometime soon?"
        else:
            return "Hey, it was nice meeting you! How have you been?"
