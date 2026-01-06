import sys
from pathlib import Path
import gradio as gr

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from agent.agent import chat

gr.ChatInterface(fn=chat).launch()
