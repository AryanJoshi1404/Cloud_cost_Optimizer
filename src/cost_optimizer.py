from src.llm_client import call_llm
import json


def generate_recommendations(analysis_result):
    analysis = analysis_result["analysis"]

    prompt = f"""
You are a cloud cost optimization expert.

STRICT RULES:
- Output ONLY a valid JSON array
- NO explanation text
- NO markdown
- NO comments
- Each item must be an object

Generate 6 to 10 cost optimization recommendations.

Each recommendation MUST include:
service, cost, savings, action

Cost analysis:
{json.dumps(analysis, indent=2)}
"""

    recommendations = call_llm(prompt)

    # ---- Validation ----
    if not isinstance(recommendations, list):
        raise ValueError("Recommendations must be a JSON array")

    for r in recommendations:
        if not isinstance(r, dict):
            raise ValueError("Each recommendation must be a JSON object")

    return recommendations
