import json
import os
import re
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL = os.getenv("HF_MODEL")

if not HF_API_KEY or not MODEL:
    raise RuntimeError("HF_API_KEY or HF_MODEL missing from .env")

endpoint = HuggingFaceEndpoint(
    repo_id=MODEL,
    huggingfacehub_api_token=HF_API_KEY,
    temperature=0.2,
    max_new_tokens=1500,
)

llm = ChatHuggingFace(llm=endpoint)

def call_llm(prompt: str):
    response = llm.invoke([HumanMessage(content=prompt)])
    raw = response.content.strip()

    # Try direct JSON
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Extract JSON inside ```json fences (BEST for LLaMA-3) since llama3 gives code fences
    fence_match = re.search(r"```json\s*([\s\S]*?)\s*```", raw)
    if fence_match:
        try:
            return json.loads(fence_match.group(1))
        except json.JSONDecodeError:
            pass

    # raise an error if all parsing attempts fail
    raise ValueError(
        "LLM did not return valid JSON.\n"
        "----- RAW OUTPUT -----\n"
        f"{raw}"
    )