import json
from src.llm_client import call_llm


def generate_billing():
    with open("data/project_profile.json", "r", encoding="utf-8") as fi:
        profile = json.load(fi)

    prompt = f"""
You are a cloud billing simulator.

STRICT RULES (MUST FOLLOW):
- Output ONLY a valid JSON array
- NO explanation text
- NO markdown
- NO comments
- JSON must be COMPLETE and parseable
- Do NOT include anything outside the JSON array

Generate EXACTLY 12 realistic cloud billing records.

Each record MUST include:
month, service, resource_id, region,
usage_quantity, unit, cost_inr, desc

Budget (monthly): {profile['budget_inr_per_month']} INR

Project profile:
{json.dumps(profile, indent=2)}
"""

    billing = call_llm(prompt)

    # ---- Validation ----
    if not isinstance(billing, list):
        raise ValueError("Billing data is not a JSON array")

    if not (12 <= len(billing) <= 20):
        raise ValueError(
            f"Expected 12–20 billing records, got {len(billing)}"
        )

    with open("data/mock_billing.json", "w", encoding="utf-8") as f:
        json.dump(billing, f, indent=2)

    print("mock_billing.json generated successfully")
