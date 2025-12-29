AI-Powered Cloud Cost Optimizer (LLM-Driven)

An intelligent, menu-driven CLI tool that analyzes cloud project requirements, generates realistic synthetic billing data, and provides actionable multi-cloud cost optimization recommendations using Large Language Models (LLMs).

This project is built as part of an academic assignment to demonstrate proficiency in backend development, LLM integration, structured JSON generation, and cost optimization analysis.

📌 Features Overview

✔ Plain-English project requirement analysis
✔ LLM-based structured project profile extraction
✔ Budget-aware synthetic cloud billing generation
✔ Cost analysis with budget variance detection
✔ Menu-driven CLI (Windows-friendly)
✔ Strict JSON-only LLM outputs with validation

Tech Stack

Language: Python 3.10+

LLM Provider: Hugging Face Inference API

Model Used: meta-llama/Meta-Llama-3-8B-Instruct

CLI Interface: Python Console

Validation: jsonschema

Environment Management: python-dotenv

Setup Instructions: 
1) first install all the required dependencies
-> pip install -r requirements.txt

2) Make a .env file in the root directory 
-> HF_API_KEY=your_huggingface_api_key
-> HF_MODEL=meta-llama/Meta-Llama-3-8B-Instruct

