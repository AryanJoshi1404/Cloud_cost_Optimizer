import os
import json
from src.profile_extractor import extract_project_profile
from src.bill_generator import generate_billing
from src.report_builder import build_report

REPORT_PATH = "data/cost_optimization_report.json"

def get_multiline_input():
    print("\nEnter project description (type END on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)



def start_cli():
    while True:
        print("\n1. Provide Project Description : ")
        print("2. Run complete cost analysis")
        print("3. View recommendations")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            project_description = get_multiline_input()

            file_path = "data/project_description.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(project_description)

            print(f"\nProject description saved to {file_path}")


        elif choice == "2":
            
            if not os.path.exists("data/project_profile.json"):
                print(" project_profile.json not found. Running extractor first...")
                extract_project_profile()

            generate_billing()
            build_report()

        elif choice == "3":
            report_path = "data/cost_optimization_report.json"

            if not os.path.exists(report_path):
                print("No report found. Run cost analysis first.")
                continue

            if os.path.getsize(report_path) == 0:
                print("Report file is empty. Please rerun cost analysis.")
                continue

            with open(report_path, "r", encoding="utf-8") as f:
                report = json.load(f)

            print("\n--- Cost Optimization Recommendations ---\n")
            print(json.dumps(report.get("recommendations", []), indent=2))

        elif choice == "4":
            break