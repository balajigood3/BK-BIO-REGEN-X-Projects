import tempfile
import unittest
from pathlib import Path
from bioregen.simulator import generate_sensor_data
from bioregen.assessment import assess
from bioregen.models import illustrative_healing_curve
from bioregen.pipeline import run_pipeline

class BioRegenTests(unittest.TestCase):
    def test_generator_is_deterministic(self):
        self.assertEqual(generate_sensor_data(seed=11), generate_sensor_data(seed=11))

    def test_unknown_scenario_rejected(self):
        with self.assertRaises(ValueError):
            generate_sensor_data("real_patient")

    def test_simulated_fluid_scenario_flagged(self):
        result = assess(generate_sensor_data("simulated_bleeding"))
        self.assertEqual(result["overall_status"], "REVIEW_FLAGGED")
        self.assertIn("SYNTHETIC_FLUID_SIGNAL", result["flags"])

    def test_normal_scenario_no_flags(self):
        result = assess(generate_sensor_data("simulated_normal"))
        self.assertEqual(result["overall_status"], "NO_SIMULATED_FLAG")

    def test_healing_curve_non_negative(self):
        curve = illustrative_healing_curve(days=60)
        self.assertTrue(all(x["illustrative_damage_index"] >= 0 for x in curve))

    def test_pipeline_writes_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_pipeline("all", Path(tmp))
            self.assertEqual(len(result["assessments"]), 3)
            self.assertTrue((Path(tmp) / "latest_assessment.json").exists())
            self.assertTrue((Path(tmp) / "synthetic_sensor_data.csv").exists())

if __name__ == "__main__":
    unittest.main()
