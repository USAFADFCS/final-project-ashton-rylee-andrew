# 🤝 Consent-First Social Wingman
**CS 471 – FairLLM Final Project**

> *An agentic AI system designed to promote respectful, consent-based social interactions through ethical communication guidance and context-aware event suggestions.*

---

## 📘 Overview
The **Consent-First Social Wingman** is an agentic AI assistant built using the **FairLLM framework**.  
Its mission is to help users navigate social interactions ethically — generating respectful, confident messages while ensuring all communication upholds principles of **mutual consent**, **tone sensitivity**, and **contextual appropriateness**.

Unlike typical “AI dating” or “conversation” tools that prioritize persuasion or humor, this system focuses on **empathy and autonomy**, reinforcing positive social norms while supporting the user’s confidence and self-awareness.

---

## 🎯 Objectives
- Promote **ethical and transparent AI-assisted communication**.
- Generate messages that balance friendliness, confidence, and consent.
- Detect and correct **non-consensual or manipulative phrasing**.
- Suggest **local events** that align with user interests and availability.
- Encourage user agency by offering structured, opt-in dialogue options.
- Demonstrate how multiple small models can work together through **agentic reasoning**.

---

## 🧩 System Architecture
The system uses a modular agentic design where each agent or tool performs a specialized ethical or contextual reasoning function.  
A coordinating agent manages communication between all modules to ensure balanced, responsible behavior.

| Agent / Tool | Role |
|---------------|------|
| **MessageGeneratorAgent** | Creates candidate social messages based on user input. |
| **ConsentCheckTool** | Scans messages for implied pressure or missing consent language. |
| **ToneAdjusterTool** | Refines text for warmth, confidence, and emotional awareness. |
| **ContextAnalyzerTool** | Evaluates the relationship stage and environment context (e.g., first meeting vs. established friendship). |
| **LocalEventMatcherTool** | Retrieves local events that match user interests and schedule. |
| **CalendarAvailabilityTool** | Checks calendar availability to prevent scheduling conflicts. |
| **InterestProfilerTool** | Tracks and ranks user interests (e.g., music, art, fitness) to tailor event suggestions. |
| **ConsentPromptBuilderTool** | Generates opt-in phrasing for invitations (e.g., “if you’d like to join…”). |
| **StructuredDialogueFormatterTool** | Presents final safe, confidence-balanced conversation options for the user. |

---

## 🧠 Model & Data
- **Foundational Model:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (Hugging Face)  
- **Why This Model:**  
  - Lightweight and deployable on edge devices.  
  - Supports conversational reasoning and context adaptation.  
  - Requires additional agents to handle consent, tone, and personalization — aligning perfectly with FairLLM’s agentic approach.

- **Data Inputs:**  
  - User message requests (free text).  
  - User interest profiles (JSON file).  
  - Schedule availability data (simulated calendar).  
  - Event feeds (from APIs like Eventbrite, Ticketmaster, or a static dataset).

- **Outputs:**  
  - Polished message drafts with transparent consent validation.  
  - Structured event recommendations that align with interests and schedule.  
  - Safe, respectful invitation phrasing for each event.

---

## 🧭 Ethical Design Principles
The Consent-First Social Wingman strictly follows **FairLLM’s ethical communication standards**, including:

- **Consent-First:** Always ensures messages contain voluntary, non-pressuring phrasing.  
- **Transparency:** Clearly communicates reasoning steps and message modifications.  
- **Fairness:** Avoids gendered stereotypes, manipulative tactics, or overgeneralization.  
- **Safety:** Rejects prompts that encourage deceit, harassment, or non-consensual behavior.  
- **Explainability:** Provides reasoning for why certain suggestions or rewrites were made.

---

## ⚙️ FairLLM Integration
FairLLM enables this system to operate as a **coordinated network of small, transparent agents**, rather than a single monolithic model.  
This approach enhances interpretability, ensures ethical alignment, and supports deployment on lightweight hardware (such as edge devices or mobile systems).

The Wingman’s architecture demonstrates:
- **Orchestration:** The ability to chain multiple reasoning steps together.  
- **Transparency:** Traceable reasoning for each tool’s contribution.  
- **Adaptability:** Support for replacing or updating individual tools independently.

---

## 📍 Workflow Example
1. **User Input:**  
   “Help me start a conversation with someone I met at a coffee shop this weekend.”

2. **MessageGeneratorAgent:**  
   Produces 2–3 possible message drafts.

3. **ConsentCheckTool:**  
   Flags overly direct or assumptive lines; keeps only messages with explicit consent cues.

4. **ToneAdjusterTool:**  
   Rewrites text for warmth, confidence, and respect.

5. **LocalEventMatcherTool:**  
   Finds nearby weekend events that match user interests and schedule.

6. **ConsentPromptBuilderTool:**  
   Adds opt-in invitation phrasing such as:  
   *“If you’re free and would like to, maybe we could check out this art fair?”*

7. **StructuredDialogueFormatterTool:**  
   Presents final safe message options for the user to select or edit.

---

## 🌐 Local Event Matching
A key feature of the Wingman is the **LocalEventMatcherTool**, which combines personalization and practicality.

### Its Core Functions:
- Retrieves nearby events from an API or dataset.  
- Filters by user interests (music, fitness, food, etc.).  
- Compares against the user’s availability to avoid conflicts.  
- Ranks suggestions based on interest fit, accessibility, and novelty.  
- Generates respectful invitation prompts for the top event options.

Example output:
| Event | Time | Match % | Suggested Invitation |
|--------|-------|----------|----------------------|
| Jazz in the Park | Sat 1800–2100 | 0.91 | “There’s a jazz event Saturday evening — if you’d like to go, it could be fun!” |
| Local Art Walk | Sun 1300–1600 | 0.85 | “There’s an art walk this Sunday afternoon — only if you’re interested!” |

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/<your-repo-name>.git
cd consent-first-social-wingman

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Prototype
python main.py

### 4. Example Prompt
“Help me write a friendly message to someone I met at the gym and suggest a casual activity.”

Expected output:
A structured, context-aware message with event-based opt-in phrasing.

## 🧾 Documentation Statement
Authorized assistance from ChatGPT (Level 5 FairLLM usage) was used to help structure this project’s documentation and planning.
All coding, implementation, and testing will be completed by the project team members.

## 👥 Team Members
| Name | GitHub Username |
|------|-----------------|
| Ashton Blair | @c26ashtonblair |
| [Partner Name] | @github-username |



## 📜 License
This project is for academic and research purposes under the USAFA FairLLM policy.
Commercial use, reproduction, or unethical deployment is strictly prohibited.

### “Respect is the foundation of communication — AI should never forget that.”

---