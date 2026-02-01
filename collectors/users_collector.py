import json
from datetime import datetime, timedelta

def get_users():
    with open("mock_data/users.json") as f:
        return json.load(f)["users"]

def count_active_users(users, days=30):
    cutoff = datetime.now() - timedelta(days=days)
    return sum(
        1 for u in users
        if u.get("lastLogin") and
        datetime.fromisoformat(u["lastLogin"].replace("Z", "")) >= cutoff
    )
