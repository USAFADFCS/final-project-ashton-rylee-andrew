# 🤝 Consent-First Social Wingman  
**CS 471 – FairLLM Final Project**

> *An agentic AI system for generating respectful, consent-aware messages and suggesting activities using a local RAG-based recommendation system.*

---

## 📘 Overview
The **Consent-First Social Wingman** is an agentic AI assistant built with the **FairLLM framework** and **OpenAI’s GPT-4.1-mini**.  

It helps users communicate confidently and respectfully by:

- Analyzing conversational context  
- Generating consent-forward message drafts  
- Ensuring tone is warm, balanced, and non-pressuring  
- Suggesting activity ideas using a **local RAG index** instead of external APIs  
- Formatting the final output into a clean, user-friendly message

This system prioritizes **ethics, autonomy, and tone sensitivity**, not persuasion or manipulation.

---

## 🎯 Objectives
- Promote ethical, consent-respecting communication  
- Support confidence and clarity in social or romantic outreach  
- Avoid manipulative or coercive phrasing  
- Suggest low-stress or high-energy activities using semantic search  
- Demonstrate FairLLM’s ReAct planning and tool execution pipeline  
- Provide an optional UI for ease of use  

---

## 🧩 System Architecture
The system uses a **single ReAct agent** powered by GPT-4.1-mini, orchestrating several tools.

### Active Tools (Used in This Version)

| Tool | Function |
|------|----------|
| **ContextAnalyzerTool** | Interprets social context (first meeting, energy level, location). |
| **MessageGeneratorTool** | Produces raw message drafts. |
| **ConsentCheckTool** | Ensures messages include opt-in, pressure-free phrasing. |
| **ToneAdjusterTool** | Adds warmth, friendliness, and confidence. |
| **LocalEventMatcherTool** *(RAG)* | Suggests activities using a FAISS vector store from `activities_catalog_tagged.md`. |
| **DialogueFormatterTool** | Builds the final combined message + activity suggestions. |

### Model
- **OpenAI GPT-4.1-mini (Responses API)**  
- Accessed using a custom adapter to integrate with FairLLM

### RAG Components
- **DocumentProcessor** for semantic text chunking  
- **SentenceTransformerEmbedder** (MiniLM-L6-v2)  
- **FaissVectorStore** for activity embeddings  
- **SimpleRetriever** for top-k activity recommendations  

The activity library lives in:
```
activities_catalog_tagged.md
```

---

## 🧠 Model & Data Sources

### LLM
- **Model:** `gpt-4.1-mini`  
- **Why:**  
  - Fast  
  - Low cost  
  - Strong reasoning for ReAct chains  
  - Excellent at natural, polite message generation

### Data Inputs
- User prompt text  
- Automatically generated social context metadata  
- Embedded activity chunks from the local catalog

### Outputs
- One carefully crafted, consent-forward message  
- 1–3 matched activity suggestions displayed below it  

---

## 🧭 Ethical Design Principles  

The Wingman follows FairLLM’s ethical standards:

- **Consent-first** phrasing (always optional, non-pressuring)  
- **Safety** — no manipulation, coercion, or sexual content  
- **Empathy** — warm tone, clear boundaries  
- **Transparency** — user-visible reasoning steps via ReAct  
- **Autonomy** — user chooses how to proceed; AI does not decide for them  

---

## 📍 Workflow Example  

1. **User Input:**  
   “I met someone at the gym and I want to ask them to hang out.”

2. **ContextAnalyzerTool:**  
   Detects: first meeting, high energy, location = Colorado Springs

3. **LocalEventMatcherTool:**  
   Uses RAG to return activities such such as:  
   - Bowling  
   - Picnic  
   - Walk on a local trail  

4. **MessageGeneratorTool:**  
   Drafts an opening line

5. **ConsentCheckTool:**  
   Ensures phrases include things like:  
   *“No pressure at all — only if you want to!”*

6. **ToneAdjusterTool:**  
   Adds warmth + friendliness  

7. **DialogueFormatterTool:**  
   Produces final message + bullet list of suggested activities  

---

## 🌐 Local Activity Matching (RAG)

Instead of calling APIs (like Eventbrite), this system uses a **local FAISS vector store**.

### Input File:
```
activities_catalog_tagged.md
```

### On first run:
- The file is chunked into semantic sections  
- Embedded using MiniLM-L6-v2  
- Stored at:  
  ```
  out/event_activities_index/
  ```
- Future runs reuse the index  
- Querying returns the top-k most relevant activities  

### Output Format:
```
📅 Possible Activities:
• Bowling — Colorado Springs
• Walk along a local trail — Colorado Springs
• Dessert spot — Colorado Springs
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```
git clone https://github.com/USAFADFCS/final-project-ashton-rylee-andrew.git
cd final-project-ashton-rylee-andrew
```

### 2. Install Dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Your API Keys to `.env`
```
OPENAI_API_KEY=your_key_here
```

### 4. Run the Core Agent
```
python main.py
```

### 5. Optional — Launch the UI
```
python wingman_ui.py
```

UI opens at:
```
http://127.0.0.1:7860
```

---

## 🧪 Testing
Run the pipeline test:  
```
python tests/test_pipeline.py
```

Expected:
```
MessageGenerator OK
ConsentCheck OK
ToneAdjuster OK
LocalEventMatcher OK
All systems operational
```

---

## 🧾 Documentation Statement
Authorized ChatGPT assistance (FairLLM level 5) was used for documentation refinement, debugging strategy, and architectural explanation.  
All implementation and testing was completed by the project team.

---

## 👥 Team Members

| Name | GitHub |
|------|--------|
| **Ashton Blair** | @c26ashtonblair |
| **[Partner Name]** | @github-username |

---

## 📜 License
This project is for educational and research purposes under USAFA FairLLM policies.  
Commercial or unethical use is prohibited.
