AI-Powered Cloud Cost Optimizer (LLM-Driven)

An intelligent, menu-driven CLI tool that analyzes cloud project requirements, generates realistic synthetic billing data, and provides actionable multi-cloud cost optimization recommendations using Large Language Models (LLMs).

This project is developed as part of an academic assignment to demonstrate proficiency in backend development, LLM integration, structured JSON generation, and cloud cost analysis.

📌 Features Overview

✔ Plain-English project requirement analysis
✔ LLM-based structured project profile extraction
✔ Budget-aware synthetic cloud billing generation
✔ Cost analysis with budget variance detection
✔ Actionable cost optimization recommendations
✔ Menu-driven CLI (Windows-friendly)
✔ Strict JSON-only LLM outputs with validation

🏗️ Project Structure
cloud_cost_optimizer/
│
├── src/
│   ├── cli.py
│   ├── llm_client.py
│   ├── profile_extractor.py
│   ├── bill_generator.py
│   ├── cost_analyzer.py
│   ├── cost_optimizer.py
│   └── report_builder.py
│
├── data/
│   ├── project_description.txt
│   ├── project_profile.json
│   ├── mock_billing.json
│   └── cost_optimization_report.json
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore


⚠️ The .env file is intentionally excluded from version control for security reasons.

🛠️ Tech Stack

Language: Python 3.10+

LLM Provider: Hugging Face Inference API

Model Used: meta-llama/Meta-Llama-3-8B-Instruct

CLI Interface: Python Console

Validation: JSON schema checks + defensive parsing

Environment Management: python-dotenv

⚙️ Setup Instructions
1️⃣ Install Dependencies

From the project root directory:

pip install -r requirements.txt

2️⃣ Create Environment File

Create a .env file in the root directory:

HF_API_KEY=your_huggingface_api_key
HF_MODEL=meta-llama/Meta-Llama-3-8B-Instruct


🔐 Make sure .env is listed in .gitignore.

▶️ How to Run the Application
✅ Recommended (Simple & Demo-Friendly)
python run.py


🧭 CLI Menu Options
1. Provide Project Description
2. Run Complete Cost Analysis
3. View Recommendations
4. Exit

🔄 Application Workflow
Step 1: Project Description (User Input)

User enters a free-form project description

Saved to:
data/project_description.txt

Step 2: Project Profile Extraction (LLM)

LLM converts text into structured JSON

Includes project name, budget, tech stack, and requirements

Output:
data/project_profile.json

Step 3: Synthetic Billing Generation (LLM)

Generates 12–20 realistic billing records

Covers compute, database, storage, networking, monitoring

Budget-aware and cloud-agnostic

Output:
data/mock_billing.json

Step 4: Cost Analysis & Recommendations

Calculates total cost, budget variance, and service-wise costs

Generates optimization recommendations (multi-cloud & open-source)

Output:
data/cost_optimization_report.json

📄 Sample Artifacts Included

✔ project_description.txt
✔ project_profile.json
✔ mock_billing.json
✔ cost_optimization_report.json

These are included to demonstrate expected input/output formats.

⚠️ Error Handling & Validation

Strict JSON-only enforcement for LLM outputs

File existence and size checks before reading

Clear CLI error messages (no silent failures)

Defensive handling of malformed or partial LLM responses

🤖 AI Usage Disclosure

This project uses Large Language Models via the Hugging Face Inference API
(specifically meta-llama/Meta-Llama-3-8B-Instruct) for:

Project profile extraction

Synthetic billing data generation

Cost optimization recommendation generation

All AI-generated outputs are strictly validated as JSON and reviewed for correctness.
Also ChatGPT is used to take help for this project generation.
The developer fully understands and owns all submitted code.

📌 Known Limitations

Uses synthetic (mock) billing data, not real cloud invoices

Hugging Face free-tier rate limits may cause minor latency

Cost estimates are illustrative, not production-accurate

🚀 Future Enhancements (Optional)

HTML report export

Azure & GCP-specific billing formats

Visualization dashboards

Real cloud billing ingestion
