# main.py
# --------------------------------------------
# Consent-First Social Wingman Orchestrator
# (local version, works without FairLLM classes)
# --------------------------------------------

from tools.consent_check import ConsentCheckTool
from tools.tone_adjuster import ToneAdjusterTool
from tools.event_matcher import LocalEventMatcherTool
from tools.formatter import DialogueFormatterTool
from tools.context_analyzer import ContextAnalyzerTool
from tools.message_generator import MessageGeneratorTool
from dotenv import load_dotenv
load_dotenv()



class SocialWingmanAgent:
    """Main orchestrator for Consent-First Social Wingman."""

    def __init__(self):
        self.consent_tool = ConsentCheckTool()
        self.tone_tool = ToneAdjusterTool()
        self.context_tool = ContextAnalyzerTool()
        self.event_tool = LocalEventMatcherTool()
        self.formatter_tool = DialogueFormatterTool()
        self.generator_tool = MessageGeneratorTool()


    def handle(self, user_input: str):
        print("\n🤖 Wingman: analyzing your message request...")

        # 1️⃣ Analyze context
        context = self.context_tool.run(user_input)

        # 2️⃣ Generate base message
        base_message = self.generator_tool.run(user_input, context)

        # 3️⃣ Adjust tone
        toned_message = self.tone_tool.run(base_message, context)

        # 4️⃣ Check for consent
        checked_message = self.consent_tool.run(toned_message)

        # 5️⃣ Suggest events
        events = self.event_tool.run(context)

        # 6️⃣ Format output
        final_output = self.formatter_tool.run(checked_message, events)
        return final_output


if __name__ == "__main__":
    agent = SocialWingmanAgent()
    print("=== Consent-First Social Wingman ===")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"quit", "exit"}:
            break

        response = agent.handle(user_input)
        print("\n" + response + "\n")
