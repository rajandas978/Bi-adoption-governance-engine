import csv

from collectors.users_collector import get_users, count_active_users
from collectors.views_collector import get_views, count_unused_views
from analytics.adoption_score import calculate_adoption_score
from analytics.governance_score import calculate_governance_score
from analytics.roi_analysis import calculate_roi_metrics


def main():
    # -----------------------------
    # Data Ingestion (Mock Mode)
    # -----------------------------
    users = get_users()
    views = get_views()

    total_users = len(users)
    total_views = len(views)

    # -----------------------------
    # Usage & Governance Metrics
    # -----------------------------
    active_users = count_active_users(users)
    inactive_users = total_users - active_users

    unused_views = count_unused_views(views)

    # -----------------------------
    # Scoring Logic
    # -----------------------------
    adoption_score = calculate_adoption_score(
        active_users=active_users,
        total_users=total_users,
        total_views=total_views
    )

    governance_score = calculate_governance_score(
        unused_views=unused_views,
        total_views=total_views
    )

    # -----------------------------
    # ROI & Cost Optimization
    # -----------------------------
    roi_metrics = calculate_roi_metrics(
        inactive_users=inactive_users,
        unused_dashboards=unused_views,
        license_cost_per_user=70  # monthly cost (can be adjusted)
    )

    # -----------------------------
    # Output Executive Report
    # -----------------------------
    output_file = "outputs/adoption_report.csv"

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])

        writer.writerow(["Total Users", total_users])
        writer.writerow(["Active Users (30 days)", active_users])
        writer.writerow(["Inactive Users", inactive_users])
        writer.writerow(["Total Dashboards / Views", total_views])
        writer.writerow(["Unused Dashboards (90 days)", unused_views])

        writer.writerow(["Adoption Score (0-100)", adoption_score])
        writer.writerow(["Governance Health Score (0-100)", governance_score])

        for key, value in roi_metrics.items():
            writer.writerow([key, value])

    print("✅ BI Adoption & Governance Executive Report Generated")
    print(f"📄 Output File: {output_file}")


if __name__ == "__main__":
    main()
