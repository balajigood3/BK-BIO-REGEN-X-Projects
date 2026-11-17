import csv
import random
from datetime import datetime, timedelta

SCENARIOS = ("simulated_normal", "simulated_bleeding", "simulated_inflammation")

def generate_sensor_data(scenario="simulated_normal", rows=60, seed=7):
    # Synthetic illustrative values only; not clinical measurements.
    if scenario not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario}")
    rng = random.Random(seed)
    data = []
    start = datetime(2026, 1, 1, 9, 0, 0)
    for i in range(rows):
        temperature = 32.5 + rng.uniform(-0.4, 0.4)
        moisture = 35 + rng.uniform(-5, 5)
        fluid_flag = 0
        stress_proxy = rng.uniform(0.0, 0.25)
        if scenario == "simulated_bleeding" and 18 <= i <= 34:
            moisture += 48 + rng.uniform(-5, 5)
            fluid_flag = 1
        elif scenario == "simulated_inflammation" and 18 <= i <= 44:
            temperature += 3.0 + rng.uniform(-0.5, 0.5)
            moisture += 15 + rng.uniform(-4, 4)
            stress_proxy += 0.55
        data.append({
            "timestamp": (start + timedelta(minutes=5*i)).isoformat(),
            "temperature_c_synthetic": round(temperature, 2),
            "moisture_percent_synthetic": round(max(0, min(100, moisture)), 2),
            "fluid_presence_synthetic": fluid_flag,
            "activity_stress_proxy_synthetic": round(min(1, stress_proxy), 3),
            "scenario": scenario,
        })
    return data

def write_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
