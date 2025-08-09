import subprocess
import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

scripts = [
    "clear.py",
    "merge.py",
    "features.py",
    "analysis.py"
]

for script in scripts:
    print(f"\n▶ Uruchamiam: {script}")
    subprocess.run(["python", f"scripts/{script}"])