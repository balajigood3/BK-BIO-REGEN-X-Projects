import argparse
from pathlib import Path
from bioregen.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="BIO-REGEN X research simulator")
    parser.add_argument("--scenario", choices=["all", "simulated_normal", "simulated_bleeding", "simulated_inflammation"], default="all")
    parser.add_argument("--output", default="reports")
    args = parser.parse_args()
    result = run_pipeline(args.scenario, Path(args.output))
    print("BIO-REGEN X simulation completed.")
    print("Assessment:", result["overall_status"])
    print("Report folder:", Path(args.output).resolve())

if __name__ == "__main__":
    main()
