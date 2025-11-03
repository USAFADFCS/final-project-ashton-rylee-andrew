# tools/message_generator.py
from tools.base_tool import Tool

class MessageGeneratorTool(Tool):
    """Generates a first-draft friendly message based on user intent."""

    def __init__(self):
        super().__init__(
            name="message_generate",
            description="Generates a first-draft friendly message based on user intent."
        )

    def use(self, user_input: str, context=None) -> str:
        text = user_input.lower()
        if "gym" in text or "workout" in text:
            return "Hey, it was great meeting you at the gym! How’s your training going lately?"
        elif "class" in text:
            return "Hi! I really enjoyed talking with you in class the other day — how’s your week going?"
        elif "coffee" in text:
            return "Hi there! Want to grab coffee again sometime soon?"
        else:
            return "Hey, it was nice meeting you! How have you been?"
