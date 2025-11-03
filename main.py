# main.py
import os
import sys
import asyncio
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# --- Core FairLLM imports ---
from fairlib.modules.mal.huggingface_adapter import HuggingFaceAdapter
from fairlib import (
    ToolRegistry,
    ToolExecutor,
    WorkingMemory,
    SimpleAgent,
    SimpleReActPlanner,
    RoleDefinition
)

# --- Local tools ---
from tools.consent_check import ConsentCheckTool
from tools.tone_adjuster import ToneAdjusterTool
from tools.event_matcher import LocalEventMatcherTool
from tools.formatter import DialogueFormatterTool
from tools.context_analyzer import ContextAnalyzerTool
from tools.message_generator import MessageGeneratorTool

from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig


# === 1. Model Configuration ===
PREFERRED_MODEL = "microsoft/Phi-3-mini-4k-instruct"
FALLBACK_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")


def ensure_model_available(model_name: str) -> bool:
    """
    Check if a Hugging Face model is already downloaded locally.
    Returns True if available, otherwise tries to download metadata.
    """
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    if any(cache_dir.rglob(model_name.split("/")[-1])):
        print(f"📦 Found cached model for '{model_name}'")
        return True

    print(f"🌐 Checking availability for '{model_name}'...")
    try:
        AutoConfig.from_pretrained(model_name, token=hf_token)
        AutoTokenizer.from_pretrained(model_name, token=hf_token)
        AutoModelForCausalLM.from_pretrained(model_name, token=hf_token)
        print(f"✅ Successfully downloaded '{model_name}'")
        return True
    except Exception as e:
        print(f"⚠️ Could not access '{model_name}': {e}")
        return False


# === 2. Choose model ===
print("🧠 Preparing language model...\n")
if ensure_model_available(PREFERRED_MODEL):
    chosen_model = PREFERRED_MODEL
else:
    print(f"🚨 Falling back to safe model: {FALLBACK_MODEL}")
    chosen_model = FALLBACK_MODEL

# Initialize adapter
llm = HuggingFaceAdapter(
    model_name=chosen_model,
    auth_token=hf_token,
)

print(f"✅ Model ready: {chosen_model}\n")


# === 3. Register tools ===
tool_registry = ToolRegistry()
tool_registry.register_tool(ConsentCheckTool())
tool_registry.register_tool(ToneAdjusterTool())
tool_registry.register_tool(LocalEventMatcherTool())
tool_registry.register_tool(DialogueFormatterTool())
tool_registry.register_tool(ContextAnalyzerTool())
tool_registry.register_tool(MessageGeneratorTool())

executor = ToolExecutor(tool_registry)
memory = WorkingMemory()


# === 4. Planner and Agent ===
planner = SimpleReActPlanner(llm, tool_registry)
planner.prompt_builder.role_definition = RoleDefinition(
    "You are the Consent-First Wingman — a friendly assistant who crafts confident, respectful first messages and suggests local events.\n\n"
    "Follow this reasoning format exactly:\n"
    "Thought: <your reasoning>\n"
    "Action: <one of: analyze_context, generate_message, check_consent, adjust_tone, match_local_events, format_dialogue, or Final Answer>\n"
    "Observation: <result of that action>\n\n"
    "Your goal is to produce ONE friendly message for the user to send — NOT a conversation script.\n"
    "If you must output a message, it should be a single text like:\n"
    "\"Hey, it was great meeting you at the gym! How’s your training going lately?\"\n\n"
    "Never simulate both sides of a conversation. When you reach a suitable message, use:\n"
    "Action: Final Answer\n"
    "Observation: <the final single message>"
)



agent = SimpleAgent(
    llm=llm,
    planner=planner,
    tool_executor=executor,
    memory=memory,
    max_steps=8,
)


# === 5. CLI (Async Interaction Loop) ===
async def main():
    print("=== 🤖 Consent-First Social Wingman ===")
    print("Type 'quit' or 'exit' to end.\n")

    while True:
        try:
            # Prompt user for input
            user_input = input("You: ").strip()
            if user_input.lower() in {"quit", "exit"}:
                print("👋 Goodbye!")
                break

            print("\n🤖 Wingman: analyzing your message request...\n")

            # Run the reasoning loop
            draft = await agent.arun(user_input)

            # 🪄 Post-processing pipeline
            msg = draft
            msg = tool_registry.get_tool("check_consent").use(msg)
            msg = tool_registry.get_tool("adjust_tone").use(msg)
            msg = tool_registry.get_tool("format_dialogue").use(msg)

            print(f"\n✅ Final Wingman Message:\n{msg}\n")

        except KeyboardInterrupt:
            print("\n👋 Exiting gracefully.")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️ Error: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())

