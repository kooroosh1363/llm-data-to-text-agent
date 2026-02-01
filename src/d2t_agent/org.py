from ai_agents_libs import *
# runner.py
from agent import SimpleAgent
# task.py
class Task:
    def init(self, title):
        self.title = title
        self.done = False
agent = SimpleAgent("CoreAgent")
result = agent.act("Analyze data")

print(result)
import os
# tools.py
def calculator(a, b):
    return a + b
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
