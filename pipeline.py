import json
from pathlib import Path
from .simulator import generate_sensor_data, write_csv
from .assessment import assess
from .models import illustrative_healing_curve, regeneration_research_status

def run_pipeline(scenario, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    scenarios = ["simulated_normal", "simulated_bleeding", "simulated_inflammation"] if scenario == "all" else [scenario]
    assessments = []
    all_rows = []
    for name in scenarios:
        rows = generate_sensor_data(name)
        all_rows.extend(rows)
        assessments.append({"scenario": name, **assess(rows)})
    write_csv(all_rows, output_dir / "synthetic_sensor_data.csv")
    result = {
        "project": "BIO-REGEN X",
        "project_type": "offline educational biomedical research simulation",
        "overall_status": "COMPLETED_WITH_RESEARCH_FLAGS" if any(a["overall_status"] == "REVIEW_FLAGGED" for a in assessments) else "SIMULATION_COMPLETED",
        "assessments": assessments,
        "illustrative_healing_curve": illustrative_healing_curve(),
        "regeneration_research": regeneration_research_status(),
        "limitations": [
            "All inputs are synthetic.",
            "No validated clinical thresholds or clinical model.",
            "Cannot identify blood from fluid presence.",
            "Cannot diagnose injury, infection, fracture, or pain.",
            "Cannot accelerate healing or grow body parts.",
            "No autonomous treatment or bodily activation."
        ]
    }
    (output_dir / "latest_assessment.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_summary(result, output_dir / "research_summary.md")
    return result

def write_summary(result, path):
    lines = [
        "# BIO-REGEN X — Simulation Summary",
        "",
        "> Educational simulation only. Not a medical device or clinical advice.",
        "",
        f"**Overall:** {result['overall_status']}",
        "",
        "## Scenario assessments",
    ]
    for item in result["assessments"]:
        lines += [f"### {item['scenario']}", f"- Status: {item['overall_status']}", f"- Flags: {', '.join(item['flags']) or 'None'}", f"- Interpretation: {item['interpretation']}", ""]
    lines += ["## Research workstreams",
              "- Bone regeneration: research topics only; no patient outcome prediction.",
              "- Soft tissue regeneration: research topics only; no biological activation.",
              "- Liquid biochip: feasibility review only; no injectable design.",
              "", "## Limitations"]
    lines += [f"- {x}" for x in result["limitations"]]
    path.write_text("\\n".join(lines), encoding="utf-8")
