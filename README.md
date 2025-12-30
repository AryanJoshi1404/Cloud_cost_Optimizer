<<<<<<< HEAD
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
=======
<h1 align="center">Cloud Cost Optimizer</h1>

<p align="center"><strong>AI-powered CLI for generating synthetic cloud bills, analyzing costs, and recommending optimizations.</strong></p>

<p align="center">
	<img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-blue" />
	<img alt="License" src="https://img.shields.io/badge/license-MIT-green" />
</p>

<p>This repository provides a simple, menu-driven CLI that:</p>
<ul>
	<li>Turns a free-form project description into a structured JSON profile (LLM-assisted)</li>
	<li>Generates budget-aware synthetic billing records</li>
	<li>Performs cost analysis and produces actionable optimization recommendations</li>
</ul>

<details>
	<summary><strong>Quicklinks</strong></summary>
	<ul>
		<li><a href="#quick-start">Quick Start</a></li>
		<li><a href="#usage-examples">Usage Examples</a></li>
		<li><a href="#project-structure">Project Structure</a></li>
		<li><a href="#development">Development</a></li>
	</ul>
</details>

<h2 id="quick-start">Quick Start</h2>

<details>
<summary>Install dependencies and run (expand for commands)</summary>

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run the CLI (recommended)
python -m src.cli

# Or run the convenience runner
python run.py
```

</details>

<h2 id="usage-examples">Usage Examples</h2>

<details>
	<summary>Sample interactive session</summary>

	<p>When prompted, paste a short project description. The app produces three core artifacts in <code>data/</code>:</p>

	<ul>
		<li><code>data/project_profile.json</code> — structured project profile extracted by the LLM</li>
		<li><code>data/mock_billing.json</code> — synthetic billing records</li>
		<li><code>data/cost_optimization_report.json</code> — analysis & recommendations</li>
	</ul>

	<pre><code>
> python -m src.cli
1) Provide Project Description
2) Run Complete Cost Analysis
3) View Recommendations
4) Exit
Select an option: 2
Processing... (LLM calls may take a few seconds)
Analysis complete — see data/cost_optimization_report.json
	</code></pre>

</details>

<h2 id="project-structure">Project Structure</h2>

<table>
	<tr><th>Path</th><th>Description</th></tr>
	<tr><td><code>src/</code></td><td>Application modules (CLI, LLM client, generators, analyzers)</td></tr>
	<tr><td><code>data/</code></td><td>Input/output JSON and sample artifacts</td></tr>
	<tr><td><code>run.py</code></td><td>Convenience runner for the CLI</td></tr>
	<tr><td><code>requirements.txt</code></td><td>Python dependencies</td></tr>
</table>

<h3>Source modules</h3>
<ul>
	<li><code>src/cli.py</code> — menu and user interactions</li>
	<li><code>src/llm_client.py</code> — wrapper for LLM calls</li>
	<li><code>src/profile_extractor.py</code> — converts free text → JSON profile</li>
	<li><code>src/bill_generator.py</code> — creates mock billing records</li>
	<li><code>src/cost_analyzer.py</code> — computes totals and variances</li>
	<li><code>src/cost_optimizer.py</code> — formulates recommendations</li>
	<li><code>src/report_builder.py</code> — bundles final report JSON</li>
</ul>

<h2 id="configuration">Configuration</h2>

<p>Create a <code>.env</code> file in the project root and add any provider keys used by your LLM client. Example:</p>

<pre><code>
HF_API_KEY=your_huggingface_api_key
HF_MODEL=meta-llama/Meta-Llama-3-8B-Instruct
# Optionally set local overrides
DEBUG=true
</code></pre>

<h2 id="data-format">Data & Output Formats</h2>

<p>All LLM-generated outputs are validated as JSON. Example artifacts included in <code>data/</code> show expected schemas for:</p>

<ul>
	<li><code>project_profile.json</code> — project meta, budget, services</li>
	<li><code>mock_billing.json</code> — list of billing line items with service, amount, region, provider</li>
	<li><code>cost_optimization_report.json</code> — top-line savings, per-service suggestions</li>
</ul>

<h2 id="development">Development & Contributing</h2>

<p>Contributions are welcome — create issues or PRs for improvements. Local development steps:</p>

<ol>
	<li>Create a new branch.</li>
	<li>Run the CLI and verify outputs in <code>data/</code>.</li>
	<li>Open a PR describing changes and any new assumptions.</li>
</ol>

<h2 id="notes">Notes & Limitations</h2>

<ul>
	<li>This project uses synthetic billing data for demonstration and education.</li>
	<li>LLM-based outputs should be reviewed; they are validated for JSON correctness but not for business accuracy.</li>
	<li>Do not commit secrets — <code>.env</code> is excluded by design.</li>
</ul>

<h2 id="license">License</h2>

<p>MIT — see LICENSE file.</p>

<hr />

<p style="font-size:0.95em">If you'd like, I can also:</p>
<ul>
	<li>add a short GIF or image walkthrough (you provide the media),</li>
	<li>generate a concise badge set for CI / coverage, or</li>
	<li>open a follow-up PR adding a simple HTML export of the report.</li>
</ul>
>>>>>>> 7b19504 (Updated Readme)
