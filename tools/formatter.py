# tools/formatter.py
class DialogueFormatterTool:
    """Formats the final conversation suggestion in a clear, friendly layout."""
    name = "format_dialogue"
    description = "Formats final conversation suggestions in a user-friendly way."

    def use(self, message: str, events: list = None) -> str:
        """Combine a suggested message with a short, formatted list of local events."""
        if events is None:
            events = []

        output_lines = [f"💬 Suggested Message:\n➡️ {message}\n"]

        if events:
            output_lines.append("\n📅 Possible Local Events:")
            for e in events:
                if isinstance(e, dict) and "error" in e:
                    output_lines.append(f"❌ Could not fetch events: {e['error']}")
                elif isinstance(e, dict) and "name" in e and "start" in e:
                    output_lines.append(f"• {e['name']} — starts {e['start']}")
                else:
                    output_lines.append("⚠️ Invalid event data.")
        else:
            output_lines.append("\n(No local events available.)")

        return "\n".join(output_lines)
