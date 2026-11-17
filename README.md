# BIO-REGEN X — Integrated Biomedical Healing-Support Research Simulator

**தமிழ்:** ஒருங்கிணைந்த உயிரியல் காயக் கண்காணிப்பு மற்றும் குணமடைதல் ஆராய்ச்சி சிமுலேட்டர்.

This is an offline, CPU-only educational simulation combining the proposed research workstreams: synthetic sensor data, signal screening, illustrative healing trends, bone/tissue research notes, safety flags, and reports.

## Safety boundary
This is NOT a medical device, diagnostic system, treatment recommendation, injectable chip, or human-body control system. All data are synthetic. Do not connect it to a person, inject materials, stimulate tissue, or use outputs for clinical decisions. It cannot identify blood, diagnose infection/fracture, accelerate healing, or grow body parts. Emergencies require immediate professional medical care.

## Requirements
- Python 3.10+
- CPU only
- No paid API keys
- No internet required
- Standard library only

## Run
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python run.py --scenario all --output reports
python -m unittest discover -s tests -v
```

Scenarios: `all`, `simulated_normal`, `simulated_bleeding`, `simulated_inflammation`.

Outputs: `reports/latest_assessment.json`, `reports/synthetic_sensor_data.csv`, `reports/research_summary.md`.

## Tamil quick start
1. Python 3.10+ நிறுவவும்.
2. Terminal-ல் `pip install -r requirements.txt` இயக்கவும்.
3. `python run.py --scenario all --output reports` இயக்கவும்.
4. `reports/` கோப்புறையில் உருவான முடிவுகளைப் பார்க்கவும்.

## Integrated workstreams
1. Research review (human-led literature work)
2. Healing-process mathematical simulation
3. Synthetic dataset generation
4. Transparent injury-signal screening
5. Simulated sensor interface
6. Synthetic fluid-signal flagging (not blood identification)
7. Illustrative healing trend
8. Smart dressing interface concept only
9. Bone regeneration research notes
10. Soft-tissue regeneration research notes
11. Liquid biochip feasibility checklist
12. Integrated local reporting and tests

No biological activation, autonomous treatment, injectable-device instructions, or patient-specific predictions are implemented.
