# tools/event_matcher.py
import os, requests

class LocalEventMatcherTool:
    """Fetches local events using the Eventbrite API and filters by context."""

    def run(self, context: dict) -> list:
        api_key = os.getenv("EVENT_API_KEY")
        url = os.getenv("EVENT_API_URL", "https://www.eventbriteapi.com/v3/events/search/")
        params = {"location.address": context.get("location", "Colorado Springs"), "location.within": "25km"}
        headers = {"Authorization": f"Bearer {api_key}"}

        print(f"🔍 Fetching events from {url} for {params['location.address']}...")
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            if resp.status_code != 200:
                print(f"⚠️ API Error {resp.status_code}: {resp.text[:200]}")
                return []
            data = resp.json()
            events = data.get("events", [])
            if not events:
                print("⚠️ No events found.")
                return []
            return [{"name": e["name"]["text"], "start": e["start"]["local"]} for e in events[:3]]
        except Exception as e:
            print(f"❌ Exception: {e}")
            return []
