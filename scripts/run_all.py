import subprocess
import os

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Paths to scripts
data_processing_path = "scripts/data_processing"
viz_path = "scripts/visualizations/matplotlib"

# Scripts for the pipeline (in order)
full_pipeline = ["clear.py", "merge.py", "features.py"]

print("\n=== Retail Sales ETL Pipeline ===")
print("1. Run the full pipeline (data cleaning + preparation + visualization)")
print("2. Run only visualization (technical version)")
print("3. Run only visualization (business version)")

choice = input("Select an option (1-3): ").strip()

if choice == "1":
    # Run ETL scripts
    for script in full_pipeline:
        print(f"\n▶ Running: {script}") 
        subprocess.run(["python", f"{data_processing_path}/{script}"])
    
    # Visualization mode
    viz_mode = input("\nChoose visualization mode (technical/business): ").strip().lower()
    if viz_mode not in ["technical", "business"]:
        viz_mode = "technical"  # default mode is technical
    subprocess.run(["python", f"{viz_path}/analysis.py", viz_mode])

elif choice == "2":
    subprocess.run(["python", f"{viz_path}/analysis.py", "technical"])

elif choice == "3":
    subprocess.run(["python", f"{viz_path}/analysis.py", "business"])

else:
    print("Invalid choice. Exiting program.")
    exit(1)