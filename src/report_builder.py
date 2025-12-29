import json
from src.cost_analyzer import analyze_costs
from src.cost_optimizer import generate_recommendations


def build_report():
    analysis_result = analyze_costs()
    recommendations_result = generate_recommendations(analysis_result)

    # ---- validate BEFORE writing ----
    if not isinstance(recommendations_result, list):
        raise ValueError("Recommendations must be a list")

    report = {
        "project_name": analysis_result["project_name"],
        "analysis": analysis_result["analysis"],
        "recommendations": recommendations_result,
        "summary": {
            "total_potential_savings": sum(
                r.get("savings", 0)
                for r in recommendations_result
                if isinstance(r, dict)
            ),
            "recommendations_count": len(recommendations_result)
        }
    }

    # ---- write only after everything is ready ----
    with open(
        "data/cost_optimization_report.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(report, f, indent=2)

    print("cost_optimization_report.json generated successfully")
