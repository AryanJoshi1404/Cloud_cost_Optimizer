#  AI-Powered Cloud Cost Optimizer (LLM-Driven)

An intelligent, menu-driven CLI tool that analyzes cloud project requirements, generates realistic synthetic billing data, and provides actionable **multi-cloud cost optimization recommendations** using Large Language Models (LLMs).

This project is developed as part of an academic assignment to demonstrate proficiency in **backend development, LLM integration, structured JSON generation, and cloud cost analysis**.

---

## 📌 Features Overview

- ✔ Plain-English project requirement analysis  
- ✔ LLM-based structured project profile extraction  
- ✔ Budget-aware synthetic cloud billing generation  
- ✔ Cost analysis with budget variance detection  
- ✔ Actionable cost optimization recommendations  
- ✔ Menu-driven CLI (Windows-friendly)  
- ✔ Strict JSON-only LLM outputs with validation  

---

## 🏗️ Project Structure

cloud_cost_optimizer/
│
├── src/
│ ├── main.py
│ ├── cli.py
│ ├── llm_client.py
│ ├── profile_extractor.py
│ ├── bill_generator.py
│ ├── cost_analyzer.py
│ ├── cost_optimizer.py
│ └── report_builder.py
│
├── data/
│ ├── project_description.txt
│ ├── project_profile.json
│ ├── mock_billing.json
│ └── cost_optimization_report.json
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

> ⚠️ The `.env` file is intentionally excluded from version control for security reasons.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+  
- **LLM Provider:** Hugging Face Inference API  
- **Model Used:** `meta-llama/Meta-Llama-3-8B-Instruct`  
- **CLI Interface:** Python Console  
- **Validation:** Strict JSON validation  
- **Environment Management:** `python-dotenv`  

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

From the project root directory, run:

```bash
pip install -r requirements.txt
2️⃣ Configure Environment Variables
Create a .env file in the root directory:

env
Copy code
HF_API_KEY=your_huggingface_api_key
HF_MODEL=meta-llama/Meta-Llama-3-8B-Instruct
🔐 Ensure .env is listed in .gitignore.

▶️ How to Run the Application
✅ Recommended (Simple & Demo-Friendly)
bash
Copy code
python run.py
🔁 Alternative (Module-Based Execution)
bash
Copy code
python -m src.main
Both commands start the same CLI interface.

🧭 CLI Menu Options
markdown
Copy code
1. Provide Project Description
2. Run Complete Cost Analysis
3. View Recommendations
4. Exit
🔄 Application Workflow
Step 1: Project Description (User Input)
User enters a free-form project description via CLI

Saved to:

bash
Copy code
data/project_description.txt
Step 2: Project Profile Extraction (LLM)
LLM extracts structured information:

Project name

Monthly budget

Tech stack

Non-functional requirements

Output:

bash
Copy code
data/project_profile.json
Step 3: Synthetic Billing Generation (LLM)
Generates 12–20 realistic billing records

Covers:

Compute

Database

Storage

Networking

Monitoring

Budget-aware and cloud-agnostic

Output:

bash
Copy code
data/mock_billing.json
Step 4: Cost Analysis & Optimization
Calculates:

Total monthly cost

Budget variance

Service-wise cost breakdown

Generates multi-cloud cost optimization recommendations

Output:

bash
Copy code
data/cost_optimization_report.json
📄 Sample Artifacts Included
project_description.txt

project_profile.json

mock_billing.json

cost_optimization_report.json

These files demonstrate the expected input and output formats.

⚠️ Error Handling & Validation
Strict JSON-only enforcement for all LLM outputs

File existence and size checks before reading

Clear CLI error messages (no silent failures)

Defensive handling of malformed or partial responses

🤖 AI Usage Disclosure
This project uses Large Language Models via the Hugging Face Inference API
(specifically meta-llama/Meta-Llama-3-8B-Instruct) for:

Project profile extraction

Synthetic billing generation

Cost optimization recommendation generation

All AI-generated outputs are strictly validated as JSON.
The developer fully understands and owns all submitted code.

📌 Known Limitations
Uses synthetic (mock) billing data

Not connected to real cloud billing APIs

Free-tier LLM rate limits may introduce latency

🚀 Future Enhancements
HTML report export

Azure and GCP-specific billing formats

Cost visualization dashboards

Real cloud billing ingestion
