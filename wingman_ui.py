# wingman_ui.py
import asyncio
import gradio as gr

import os
import signal

def shutdown_server():
    os.kill(os.getpid(), signal.SIGTERM)
    return "🛑 Server is shutting down..."


from main import generate_wingman_response  # import the function you just wrote

def sync_wingman(user_input: str) -> str:
    # Gradio expects a sync function, so we bridge to asyncio here
    return asyncio.run(generate_wingman_response(user_input))

with gr.Blocks() as demo:
    gr.Markdown("## 💌 Consent-First Wingman\nType what you want help saying below.")
    inp = gr.Textbox(
        label="What do you want to say?",
        placeholder="E.g., I just met someone and want a low-stress first date idea...",
        lines=3,
    )
    out = gr.Textbox(label="Suggestion", lines=12)

    btn = gr.Button("Generate message")
    btn.click(fn=sync_wingman, inputs=inp, outputs=out)

    shutdown_btn = gr.Button("Stop Server 🛑")
    shutdown_output = gr.Textbox(label="Status")

    shutdown_btn.click(
        fn=shutdown_server,
        outputs=shutdown_output
    )

if __name__ == "__main__":
    demo.launch()
