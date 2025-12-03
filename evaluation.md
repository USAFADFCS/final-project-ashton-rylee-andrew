# 📝 Qualitative Evaluation — *Consent-First Social Wingman*

## **1. Evaluation Overview**
The purpose of this qualitative evaluation is to determine whether the **Consent-First Social Wingman** system reliably produces:

- Respectful, consent-aware communication  
- Tone-appropriate first messages  
- Accurate context interpretations  
- Meaningful activity suggestions via RAG  
- Coherent tool-chaining using FairLLM’s agentic reasoning  

The evaluation examines real prompts and judges correctness, appropriateness, and tool performance.

---

## **2. Methodology**
A set of representative prompts was selected to test the following dimensions:

1. **Consent sensitivity**  
2. **Tone adjustment** (warm, confident, low-pressure)  
3. **Context analyzer correctness**  
4. **RAG event retrieval quality**  
5. **ReAct agent loop cohesion**  

Each prompt was run through the full pipeline (context → consent → tone → events → formatting).

Outputs were documented and assessed qualitatively.

---

## **3. Test Scenarios and Observations**

### **Scenario 1 — First-time outreach after meeting at the gym**
**Prompt:**  
`I just met someone high-energy at the gym. Help me send a friendly first message.`

**Expected Behavior**
- Upbeat tone  
- Consent-aware phrasing  
- Optional high-energy activity suggestions  

**System Output Summary**
- Message included opt-in phrasing (“No pressure…”).  
- Tone matched a fitness/high-energy vibe.  
- RAG surfaced appropriate activities (bowling, walking trail, picnic).  

**Evaluation:**  
✔ *Meets expectations — strong consent and tone alignment.*

---

### **Scenario 2 — Low-stress invitation**
**Prompt:**  
`I want to suggest a low-stress, non-demanding activity for someone I just met.`

**Expected Behavior**
- Gentle, low-energy tone  
- Appropriate activity suggestions  

**System Output Summary**
- Produced soft, low-pressure language.  
- RAG provided low-energy ideas (museum, dessert, coffee).  

**Evaluation:**  
✔ *Strong performance — tone and activities aligned correctly.*

---

### **Scenario 3 — Correcting a wrong assumption**
**Prompt:**  
`I never went out to coffee with them.`

**Expected Behavior**
- Remove incorrect assumption  
- Adjust invitation phrasing  

**System Output Summary**
- Corrected message (“would you like to grab coffee sometime?”).  
- No inaccurate references remained.  

**Evaluation:**  
✔ *Excellent responsiveness to user correction.*

---

### **Scenario 4 — Brainstorming non-coffee alternatives**
**Prompt:**  
`What are some other activities we could do that aren't too intense?`

**Expected Behavior**
- Avoid repeatedly suggesting coffee  
- Provide a variety of valid options  

**System Output Summary**
- RAG surfaced balanced, appropriate ideas (museum, workshop, walking trail).  
- Activity diversity improved after tuning.  

**Evaluation:**  
✔ *Shows functional RAG-based activity matching.*

---

## **4. Strengths Observed**

### ⭐ 1. **Consent-Aware Messaging**
All messages contained voluntary, autonomy-respecting phrasing:
- “If you’re up for it…”  
- “No pressure at all…”  
- “Only if you’d like to…”  

### ⭐ 2. **Tone Adaptation**
The system responded well to:
- High-energy prompts  
- Low-stress prompts  
- First-meeting scenarios  

### ⭐ 3. **Context Analyzer Accuracy**
Correctly detected:
- Meeting stage  
- Energy level  
- Location  

### ⭐ 4. **RAG Event Suggestions**
FAISS-powered RAG produced:
- Consistent activity labels  
- Matching metadata (energy/social level)  
- Usable, friendly suggestions  

### ⭐ 5. **Agentic Tool Coordination**
ReAct loop correctly invoked:
- `analyze_context`  
- `check_consent`  
- `match_local_events`  
- `format_dialogue`  

Outputs were coherent and aligned with goals.

---

## **5. Limitations Identified**

### ⚠️ 1. Occasional Over-Reliance on Coffee
At times, the system defaulted to café-style invitations (mitigated after tuning).

### ⚠️ 2. Sometimes Events Don’t Insert into Final Answer
Due to agent choosing Final Answer early.

### ⚠️ 3. Prompt Sensitivity
More complex prompts occasionally require refinement.

---

## **6. Overall Assessment**

| Category | Result |
|---------|--------|
| **Completeness** | ✔ End-to-end agentic pipeline with tools + RAG |
| **Correctness** | ✔ Messages are safe, consent-aware, context-driven |
| **Complexity** | ✔ Multi-step reasoning + FAISS RAG + tool refinement |
| **Documentation** | ✔ README + comments + evaluation |
| **Evaluation Requirement** | ✔ Satisfied with systematic qualitative review |

---

## **7. Final Evaluation Statement**

**The Consent-First Social Wingman reliably produces respectful, consent-aware, and context-sensitive communication. The agentic pipeline—including context analysis, consent detection, tone refinement, and RAG event retrieval—functions cohesively and meets CS 471 project requirements.**
