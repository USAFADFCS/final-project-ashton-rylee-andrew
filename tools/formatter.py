# tools/formatter.py
class DialogueFormatterTool:
    """Formats final conversation suggestions in a user-friendly way."""

    def run(self, message: str, events: list) -> str:
        output = f"Suggested Message:\n➡️ {message}\n\nPossible Local Events:\n"
        for e in events:
            if "error" in e:
                output += f"❌ Could not fetch events: {e['error']}\n"
            else:
                output += f"• {e['name']} — starts {e['start']}\n"
        return output
