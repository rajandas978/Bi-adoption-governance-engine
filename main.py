import csv
from collectors.users_collector import get_users, count_active_users
from collectors.views_collector import get_views, count_unused_views
from analytics.adoption_score import calculate_adoption_score
from analytics.governance_score import calculate_governance_score

def main():
    users = get_users()
    views = get_views()

    active_users = count_active_users(users)
    unused_views = count_unused_views(views)

    adoption_score = calculate_adoption_score(
        active_users, len(users), len(views)
    )
    governance_score = calculate_governance_score(
        unused_views, len(views)
    )

    with open("outputs/adoption_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Users", len(users)])
        writer.writerow(["Active Users", active_users])
        writer.writerow(["Total Views", len(views)])
        writer.writerow(["Unused Views", unused_views])
        writer.writerow(["Adoption Score", adoption_score])
        writer.writerow(["Governance Score", governance_score])

    print("Report generated successfully")

if __name__ == "__main__":
    main()
