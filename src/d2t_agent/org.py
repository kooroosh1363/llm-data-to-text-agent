from ai_agents_libs import *

# config.py
import os
# agent.py
class SimpleAgent:
    def init(self, name):
        self.name = name

    def act(self, task):
        return f"{self.name} is working on: {task}"
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4.1-mini"
