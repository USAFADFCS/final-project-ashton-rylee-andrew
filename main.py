# main.py
import os
import sys
import asyncio
from dotenv import load_dotenv

from fairlib import (
    settings,
    OpenAIAdapter,      # 👈 same adapter as in the demo
    ToolRegistry,
    ToolExecutor,
    WorkingMemory,
    SimpleAgent,
    SimpleReActPlanner,
    RoleDefinition,
)

# --- Local tools ---
from tools.consent_check import ConsentCheckTool
from tools.tone_adjuster import ToneAdjusterTool
from tools.event_matcher import LocalEventMatcherTool   # your activity matcher (RAG or simple)
from tools.formatter import DialogueFormatterTool
from tools.context_analyzer import ContextAnalyzerTool

load_dotenv()

# =========================
# 1. Model / API config
# =========================
# load API key into fairlib settings (like the demo)
settings.api_keys.openai_api_key = os.getenv("OPENAI_API_KEY")

PREFERRED_MODEL = "gpt-4.1-mini"  # or "gpt-4o", etc.

print("🧠 Preparing language model...\n")

llm = OpenAIAdapter(
    api_key=settings.api_keys.openai_api_key,
    model_name=PREFERRED_MODEL,
)

print(f"✅ Model ready: {PREFERRED_MODEL}\n")

# =========================
# 2. Register tools
# =========================
tool_registry = ToolRegistry()
tool_registry.register_tool(ConsentCheckTool())
tool_registry.register_tool(ToneAdjusterTool())
tool_registry.register_tool(LocalEventMatcherTool())
tool_registry.register_tool(DialogueFormatterTool())
tool_registry.register_tool(ContextAnalyzerTool())

executor = ToolExecutor(tool_registry)
memory = WorkingMemory()

# =========================
# 3. Planner and Agent
# =========================
planner = SimpleReActPlanner(llm, tool_registry)
planner.prompt_builder.role_definition = RoleDefinition(
    "You are the Consent-First Wingman — a friendly assistant who crafts "
    "confident, respectful first messages and suggests local events.\n\n"
    "If you call the 'match_local_events' tool, you MUST:\n"
    " • Look at the returned activities.\n"
    " • Pick one or two that best fit the user's vibe.\n"
    " • Mention them explicitly by name in your Final Answer.\n"
    "For example, instead of saying 'a fun activity', say something like:\n"
    " 'Would you like to check out that live music spot or maybe try karaoke sometime?'\n\n"
    "Follow this reasoning format exactly:\n"
    "Thought: <your reasoning>\n"
    "Action: <one of: analyze_context, match_local_events, Final Answer>\n"
    "Observation: <result of that action>\n\n"
    "Your goal is to produce ONE friendly message for the user to send — "
    "NOT a conversation script."
)




agent = SimpleAgent(
    llm=llm,
    planner=planner,
    tool_executor=executor,
    memory=memory,
    max_steps=8,
)

# main.py (add this near the bottom)

async def generate_wingman_response(user_input: str) -> str:
    """
    One-shot pipeline: take raw user text, run context analysis,
    ReAct agent, post-processing tools, and return a pretty string.
    """
    # 1) Analyze context
    context_tool = tool_registry.get_tool("analyze_context")
    context = context_tool.use(user_input)

    # 2) Run the ReAct agent
    draft = await agent.arun(user_input)

    # 3) Post-processing with context
    msg = draft
    msg = tool_registry.get_tool("check_consent").use(msg, context)
    msg = tool_registry.get_tool("adjust_tone").use(msg, context)

    # 4) Get activities based on same context
    events = tool_registry.get_tool("match_local_events").use(context)

    # 5) Format everything nicely
    final_output = tool_registry.get_tool("format_dialogue").use(msg, events)
    return final_output


# === 4. CLI (Async Interaction Loop) ===
async def main():
    print("=== 🤖 Consent-First Social Wingman ===")
    print("Type 'quit' or 'exit' to end.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in {"quit", "exit"}:
                print("👋 Goodbye!")
                break

            print("\n🤖 Wingman: analyzing your message request...\n")

            # 1️⃣ Analyze context ONCE at the top
            context_tool = tool_registry.get_tool("analyze_context")
            context = context_tool.use(user_input)

            # 2️⃣ Let the ReAct agent think / call tools (no context needed here)
            draft = await agent.arun(user_input)

            # 3️⃣ Post-processing pipeline with context
            msg = draft
            msg = tool_registry.get_tool("check_consent").use(msg, context)
            msg = tool_registry.get_tool("adjust_tone").use(msg, context)

            # Activities based on the same context (energy, social, location)
            events = tool_registry.get_tool("match_local_events").use(context)

            # 4️⃣ Final formatting using message + events
            final_output = tool_registry.get_tool("format_dialogue").use(msg, events)

            print(f"\n✅ Final Wingman Message:\n{final_output}\n")

        except KeyboardInterrupt:
            print("\n👋 Exiting gracefully.")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️ Error: {e}\n")



if __name__ == "__main__":
    asyncio.run(main())