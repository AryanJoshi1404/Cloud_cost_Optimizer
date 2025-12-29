import json
from collections import defaultdict


def analyze_costs():
    with open("data/project_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    with open("data/mock_billing.json", "r", encoding="utf-8") as f:
        billing = json.load(f)

    total_costs = 0
    service_costs = defaultdict(int)

    for item in billing:
        cost = item.get("cost_inr", 0)
        service = item.get("service", "Unknown")

        total_costs += cost
        service_costs[service] += cost

    budget = profile["budget_inr_per_month"]
    project_name = profile.get("name", "Unnamed Project")

    analysis = {
        "total_monthly_cost": total_costs,
        "budget": budget,
        "budget_variance": total_costs - budget,
        "service_costs": dict(service_costs),
        "is_over_budget": total_costs > budget
    }

    return {
        "project_name": project_name,
        "analysis": analysis
    }
