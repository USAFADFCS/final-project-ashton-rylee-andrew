# tools/formatter.py

class DialogueFormatterTool:
    name = "format_dialogue"
    description = "Formats the final message and optional events for user display."

    def use(self, message: str, events: list | None = None) -> str:
        events = events or []

        lines = []
        lines.append("💬 Suggested Message:")
        lines.append(f"➡️ {message}")

        if events:
            lines.append("\n📅 Possible Activities:")
            for e in events:
                lines.append(f"• {e.get('name')} — {e.get('venue', '')}")
        else:
            lines.append("\n(No local events available.)")

        return "\n".join(lines)
