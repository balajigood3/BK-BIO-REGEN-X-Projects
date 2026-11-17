def assess(rows):
    # Transparent synthetic-data screening, not diagnosis or validated thresholds.
    if not rows:
        raise ValueError("At least one synthetic reading is required.")
    fluid_events = sum(int(r["fluid_presence_synthetic"]) for r in rows)
    high_moisture = sum(float(r["moisture_percent_synthetic"]) > 75 for r in rows)
    warm_readings = sum(float(r["temperature_c_synthetic"]) > 35.5 for r in rows)
    proxy_elevations = sum(float(r["activity_stress_proxy_synthetic"]) > 0.6 for r in rows)
    flags = []
    if fluid_events:
        flags.append("SYNTHETIC_FLUID_SIGNAL")
    if high_moisture >= 3:
        flags.append("SYNTHETIC_HIGH_MOISTURE_TREND")
    if warm_readings >= 3:
        flags.append("SYNTHETIC_WARM_TREND")
    if proxy_elevations >= 3:
        flags.append("SYNTHETIC_ACTIVITY_STRESS_PROXY")
    return {
        "overall_status": "REVIEW_FLAGGED" if flags else "NO_SIMULATED_FLAG",
        "flags": flags,
        "counts": {
            "synthetic_fluid_events": fluid_events,
            "high_moisture_readings": high_moisture,
            "warm_readings": warm_readings,
            "elevated_activity_stress_proxy_readings": proxy_elevations,
        },
        "interpretation": (
            "Synthetic scenario contains signals for review; it does not establish bleeding, infection, pain, injury, or disease."
            if flags else
            "No configured synthetic flags were triggered; this does not establish health or absence of injury."
        ),
        "safety_notice": "Not for diagnosis, treatment, triage, or real patient monitoring."
    }
