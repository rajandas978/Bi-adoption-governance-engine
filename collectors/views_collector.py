import json
from datetime import datetime, timedelta

def get_views():
    with open("mock_data/views.json") as f:
        return json.load(f)["views"]

def count_unused_views(views, days=90):
    cutoff = datetime.now() - timedelta(days=days)
    return sum(
        1 for v in views
        if datetime.fromisoformat(v["lastViewedAt"].replace("Z", "")) < cutoff
    )
