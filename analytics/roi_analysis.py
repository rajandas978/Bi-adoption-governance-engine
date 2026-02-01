def calculate_roi_metrics(
    inactive_users,
    unused_dashboards,
    license_cost_per_user=70
):
    """
    license_cost_per_user: monthly cost in USD (can be changed)
    """

    monthly_waste = inactive_users * license_cost_per_user
    annual_waste = monthly_waste * 12

    return {
        "Inactive Users": inactive_users,
        "Unused Dashboards": unused_dashboards,
        "Monthly Cost Leakage ($)": monthly_waste,
        "Annual Cost Leakage ($)": annual_waste
    }
