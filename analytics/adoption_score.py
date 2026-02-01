def calculate_adoption_score(active_users, total_users, total_views):
    if total_users == 0:
        return 0
    return round(
        (active_users / total_users) * 60 +
        min((total_views / total_users) * 5, 40),
        2
    )
