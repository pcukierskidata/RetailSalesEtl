import subprocess
import os

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Scripts for the pipeline
full_pipeline = ["clear.py", "merge.py", "features.py"]

print("\n=== Retail Sales ETL Pipeline ===")
print("1. Run the full pipeline (data cleaning + preparation + visualization)")
print("2. Run only visualization (technical version)")
print("3. Run only visualization (business version)")

choice = input("Select an option (1-3): ").strip()

if choice == "1":
    scripts = full_pipeline

    for script in scripts:
        print(f"\n▶ Running: {script}") 
        subprocess.run(["python", f"scripts/{script}"])

    # added question about type of visualizations
    viz_mode = input("\nChoose visualization mode (technical/business): ").strip().lower()
    if viz_mode not in ["technical", "business"]:
        viz_mode = "technical" # default mode is technical
    subprocess.run(["python", "scripts/analysis.py", viz_mode])

elif choice == "2":
    subprocess.run(["python", "scripts/analysis.py", "technical"])

elif choice == "3":
    subprocess.run(["python", "scripts/analysis.py", "business"])

else:
    print("Invalid choice. Exiting program.")
    exit(1)

# Run the selected scripts
for script in scripts:
    print(f"\n▶ Running: {script}")
    subprocess.run(["python", f"scripts/{script}"])