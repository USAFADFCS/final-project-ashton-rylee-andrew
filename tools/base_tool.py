# tools/base_tool.py
class Tool:
    """Minimal fallback Tool class compatible with FairLib ToolRegistry."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def use(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the 'use' method.")
