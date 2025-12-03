# 🛠️ Setup Instructions  
**Project:** Consent-First Social Wingman  
**Course:** CS 471 – FairLLM Final Project  
**Authors:** Ashton Blair & [Partner Name]  
**Last Updated:** December 2025

---

## 📦 1. Overview
This project implements the **Consent-First Social Wingman**, an agentic AI system that:

- Crafts respectful, confident first messages  
- Analyzes social, romantic, and conversational context  
- Suggests activities using a **local RAG activity catalog**  
- Runs a **ReAct-style tool agent** using the FairLLM framework  
- Presents results through a **Gradio UI**  

Core components used:

- **FairLLM tools & ReAct planner**  
- **OpenAI GPT-4.1-mini (Responses API)**  
- **SentenceTransformer embedding model (MiniLM-L6-v2)**  
- **Local FAISS vector store for activity suggestions**  
- **Gradio** for a simple user-facing application

---

## 🧩 2. System Requirements

**Recommended Environment**
- macOS 12+ / Windows 11 / Ubuntu 22.04  
- Python 3.10–3.12  
- Disk: ~3 GB free (models + vector index + deps)  
- RAM: 8 GB minimum, 16 GB recommended  
- GPU: Optional (CPU works fine for this project)

---

## ⚙️ 3. Environment Setup

### Step 1 — Clone the Repository
git clone https://github.com/USAFADFCS/final-project-ashton-rylee-andrew.git
cd final-project-ashton-rylee-andrew

### Step 2 — Create a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate # macOS / Linux
.venv\Scripts\activate # Windows

### Step 3 — Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

### Step 4 — Verify Installations
python - << 'EOF'
import fairlib, openai, gradio
print("✅ Environment OK")
EOF

---

## 🤖 4. Model Setup & Verification

This project uses **OpenAI GPT-4.1-mini** through the **Responses API**.

### Test the LLM Connection
python3 - << 'EOF'
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
resp = client.responses.create(
model="gpt-4.1-mini",
input="Say hello!"
)
print(resp.output_text)
EOF


Expected output:
Hello!

yaml
Copy code

---

## 🔗 5. Environment Variables

Create a `.env` file in the project root:

OPENAI_API_KEY=your_openai_key_here

## 🧠 6. Local RAG System (Activity Recommendations)

The Wingman uses a **local retrieval-augmented system**:

- `activities_catalog_tagged.md` — your activity library  
- `DocumentProcessor` — semantic chunking  
- `SentenceTransformerEmbedder` — embeddings  
- `FaissVectorStore` — persistent vector index  
- `SimpleRetriever` — top-k search  

### On first run:
1. The file is chunked automatically  
2. Embeddings are generated  
3. A FAISS index is created at:  
out/event_activities_index/
4. Future runs reuse cached embeddings + index  
5. Queries return **top 3 recommended activities**  

No external calls or internet access are needed.

---

## ▶️ 7. Running the Wingman

### Option A — Terminal (ReAct Loop)
python main.py

Example:
You: I met someone at the gym—help me ask them out.
System: [Generates message + activity suggestions]

---

### Option B — Gradio UI
python wingman_ui.py

Then visit:

http://127.0.0.1:7860


The UI includes:
- Input box  
- Suggested message output  
- Activity suggestions  
- A “Stop Server” button

---

## 🧪 8. Testing the Pipeline

Run the tests:

python tests/test_pipeline.py


Expected output:
✅ MessageGeneratorTool OK
✅ ConsentCheckTool OK
✅ LocalEventMatcherTool OK
🎉 All systems operational


---

## 🧰 9. Troubleshooting

| Issue | Cause | Fix |
|-------|--------|------|
| `'str' object has no attribute content'` | Using old OpenAI response format | Use GPT-4.1-mini + Responses API adapter |
| Missing FAISS | Dependency not installed | `pip install faiss-cpu` |
| Tools not found | Running from wrong directory | Run from project root |
| UI stuck on local only | Default Gradio behavior | Use `launch(share=True)` |
| Vec store rebuilds every run | File missing or path incorrect | Ensure `activities_catalog_tagged.md` exists |

---

## 🧾 10. Documentation Statement

This project used authorized assistance from ChatGPT (FairLLM Level 5 guidelines) for:

- Architecture guidance  
- Debugging tool integration  
- Documentation creation  


---