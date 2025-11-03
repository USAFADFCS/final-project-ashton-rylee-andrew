# 🛠️ Setup Instructions
**Project:** Consent-First Social Wingman  
**Course:** CS 471 – FairLLM Final Project  
**Authors:** Ashton Blair & [Partner Name]  
**Last Updated:** October 2025

---

## 📦 1. Overview
This document explains how to install, configure, and verify the development environment for the **Consent-First Social Wingman** project.  
It ensures that the **FairLLM framework** and all required dependencies for the agentic AI system are correctly installed and functional.

---

## 🧩 2. System Requirements
**Recommended Environment**
- **OS:** macOS 13 / Windows 11 / Ubuntu 22.04 LTS  
- **Python:** 3.10 or 3.11  
- **Disk Space:** ≥ 10 GB (fair-llm + TinyLlama weights + dependencies)  
- **RAM:** 8 GB (minimum), 16 GB recommended  
- **GPU (optional):** CUDA-capable NVIDIA GPU for Torch acceleration  

---

## ⚙️ 3. Environment Setup

### Step 1 — Clone the Repository
```bash
git clone https://github.com/USAFADFCS/final-project-ashton-rylee-andrew.git
cd final-project-ashton-rylee-andrew
```

### Step 2 — Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
# or
.venv\Scripts\activate       # Windows PowerShell
```

### Step 3 — Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4 — Verify Installations

Confirm that all core modules import successfully:

```bash
python -c "import torch, transformers, fairlib, numpy; print('✅ Environment OK')"
```

## 🤖 4. Model Setup & Verification
### Step 1 — Download Base Model

The project uses a small, edge-deployable model:

Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
Source: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0

When you first run the program, the model will download automatically to ~/.cache/huggingface/.

### Step 2 — Test Model Response
```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
>>> tok = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
>>> model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
>>> print("✅ Model loaded successfully")
```

## 🔗 5. Environment Variables

Create a .env file in the project root to store API keys and local paths for any external tools.

Example .env:

### Event data source (API or file path)
EVENT_API_KEY=your_api_key_here
EVENT_API_URL=https://www.eventbriteapi.com/v3/events/search/

### Optional: Hugging Face token (for authenticated downloads)
HUGGINGFACE_TOKEN=your_token_here

## 🧠 6. Running the Prototype

After setup, you can run the main agent loop:

python main.py


Example interaction:

User: Help me start a friendly conversation and suggest something fun this weekend.
System: [Generates 3 consent-first messages + event suggestions]

## 🧪 7. Testing the Pipeline

Use the built-in test script to verify all tools communicate correctly:

python tests/test_pipeline.py


Expected output:

✅ MessageGeneratorAgent OK  
✅ ConsentCheckTool OK  
✅ LocalEventMatcherTool OK  
✅ All tests passed!

## 🧰 8. Troubleshooting
Issue	Possible Cause	Fix
torch.cuda.is_available() → False	No GPU or CUDA drivers missing	Install CUDA 11.8+ or run CPU mode
fair_llm not found	Not installed or venv inactive	Re-activate virtual env and re-install requirements
Model download fails	No Hugging Face auth token	Add HUGGINGFACE_TOKEN to .env
ImportError: pydantic.v2	Old Python version	Upgrade to Python ≥ 3.10

## 🧾 9. Documentation Statement

Authorized assistance from ChatGPT (Level 5 FairLLM usage) was used for project setup and documentation.
All implementation and testing code will be developed by the project team.

## ✅ 10. Next Steps

Begin developing core agents (MessageGenerator, ConsentCheck, LocalEventMatcher).

Integrate FairLLM tool calls into main.py.

Document test results in /docs/progress_report.md.

Prepare demo for CS 471 progress checkpoint.