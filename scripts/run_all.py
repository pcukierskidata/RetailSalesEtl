import subprocess
import os

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Scripts for the pipeline
full_pipeline = ["clear.py", "merge.py", "features.py", "analysis.py"]
only_visualization = ["analysis.py"]

print("=== Retail Sales ETL Pipeline ===")
print("1. Run the full pipeline (data cleaning + preparation + visualization)")
print("2. Run only visualization")
choice = input("Select an option (1/2): ").strip()

if choice == "1":
    scripts = full_pipeline
elif choice == "2":
    scripts = only_visualization
else:
    print("Invalid choice. Exiting program.")
    exit(1)

# Run the selected scripts
for script in scripts:
    print(f"\n▶ Running: {script}")
    subprocess.run(["python", f"scripts/{script}"])