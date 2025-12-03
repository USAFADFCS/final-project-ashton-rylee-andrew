"""
LocalEventMatcherTool (tag/keyword version, no FAISS)

Instead of calling the Eventbrite API or using FAISS, this tool:
  - Loads a local Markdown file (activities_catalog_tagged.md)
  - Parses activities and their **Tags:** lines
  - Uses simple tag + keyword scoring to retrieve best-matching activities
  - Returns them in an Event-like shape: [{name, start, venue, ...}, ...]

This makes 'match_local_events' effectively a "match local activities"
tool that your Consent-First Wingman can call in the ReAct loop, without
any heavy dependencies (FAISS, sentence-transformers, etc.).
"""

from pathlib import Path
from typing import List, Dict, Any

# Path to your tagged activities catalog
ACTIVITIES_DOC_PATH = Path("activities_catalog_tagged.md")

# How many activities to return
DEFAULT_TOP_K = 3

_activities: List[Dict[str, Any]] = []
_loaded = False


def _parse_tags_line(line: str) -> Dict[str, str]:
    """
    Parse a line like:
      **Tags:** duration=medium, cost=low, setting=indoor, energy=low, social=one-on-one
    into a dict: {"duration": "medium", "cost": "low", ...}
    """
    line = line.strip()
    if not line.lower().startswith("**tags:**"):
        return {}

    # Remove the '**Tags:**' prefix
    tag_part = line.split("**Tags:**", 1)[1].strip()
    # Split on commas
    pieces = [p.strip() for p in tag_part.split(",") if p.strip()]
    tags: Dict[str, str] = {}
    for p in pieces:
        if "=" in p:
            k, v = p.split("=", 1)
            tags[k.strip()] = v.strip()
    return tags


def _load_activities_if_needed():
    """
    Load and parse activities from the markdown file once.
    Each activity is keyed by its '### Activity Name' heading.
    """
    global _loaded, _activities

    if _loaded:
        return

    if not ACTIVITIES_DOC_PATH.exists():
        raise FileNotFoundError(
            f"Activities file not found at {ACTIVITIES_DOC_PATH}. "
            "Make sure activities_catalog_tagged.md is there."
        )

    text = ACTIVITIES_DOC_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    current: Dict[str, Any] = {}
    buffer: List[str] = []

    for line in lines:
        stripped = line.strip()

        # New activity starts at a "### " heading
        if stripped.startswith("### "):
            # Commit previous one
            if current:
                current["text"] = "\n".join(buffer).strip()
                _activities.append(current)

            # Start new
            name = stripped[4:].strip()
            current = {
                "name": name,
                "tags": {},
                "text": "",
            }
            buffer = []
            continue

        # Inside an activity block
        if not current:
            continue

        # Capture tags line
        if stripped.lower().startswith("**tags:**"):
            tags = _parse_tags_line(stripped)
            current["tags"] = tags
        else:
            buffer.append(line)

    # Commit last activity
    if current:
        current["text"] = "\n".join(buffer).strip()
        _activities.append(current)

    _loaded = True


def _score_activity(act: Dict[str, Any], query: str, context: Dict[str, Any]) -> float:
    score = 0.0
    tags = act.get("tags", {})
    name = act.get("name", "") or ""
    text = act.get("text", "") or ""
    name_l = name.lower()
    text_l = text.lower()

    # Tag-based scoring (as you already do)
    energy = context.get("energy")
    if energy and tags.get("energy") == str(energy):
        score += 3.0

    social = context.get("social")
    if social and tags.get("social") == str(social):
        score += 2.0

    # Simple keyword scoring
    for kw in ["low stress", "non-demanding", "chill", "relaxed"]:
        if kw in text_l or kw in name_l:
            score += 1.5

    # ⚠️ Small penalty for coffee so it isn't always first
    if "coffee" in name_l:
        score -= 1.0

    return score



def _choose_activities(query: str, context: Dict[str, Any], top_k: int) -> List[Dict[str, Any]]:
    _load_activities_if_needed()

    if not _activities:
        return []

    scored = []
    for act in _activities:
        s = _score_activity(act, query, context)
        scored.append((s, act))

    # Sort descending by score
    scored.sort(key=lambda x: x[0], reverse=True)

    # If everything scores at 0, just take the first few low-energy ones as a fallback
    if scored and scored[0][0] <= 0:
        low_energy = [a for (_, a) in scored if a.get("tags", {}).get("energy") == "low"]
        if low_energy:
            scored = [(1.0, a) for a in low_energy]
        # else leave scored as-is (they're all 0 but sorted)

    return [act for (_, act) in scored[:top_k]]


# tools/event_matcher.py (tag-based version)

class LocalEventMatcherTool:
    name = "match_local_events"
    description = (
        "Fetches activity suggestions using a local markdown catalog "
        "activities_catalog_tagged.md and filters by context."
    )

    def use(self, context) -> List[Dict[str, Any]]:
        # Normalize context
        if isinstance(context, str):
            context = {"location": "Colorado Springs", "query": context}
        elif not isinstance(context, dict):
            context = {"location": "Colorado Springs"}

        location = context.get("location", "Colorado Springs")
        query = context.get("query", "")

        # We keep energy/social in context for scoring
        activities = _choose_activities(query, context, top_k=DEFAULT_TOP_K)

        if not activities:
            return [
                {
                    "name": "Grab coffee at a local café",
                    "start": "Flexible time",
                    "venue": location,
                },
                {
                    "name": "Take a walk in a nearby park",
                    "start": "Flexible time",
                    "venue": location,
                },
            ]

        formatted: List[Dict[str, Any]] = []
        for act in activities:
            formatted.append(
                {
                    "name": act.get("name", "Suggested Activity"),
                    "start": "Flexible time",
                    "venue": location or "Any convenient place",
                    "raw_chunk": act.get("text", ""),
                    "metadata": act.get("tags", {}),
                }
            )

        return formatted

