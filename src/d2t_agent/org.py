from ai_agents_libs import *
# runner.py
from agent import SimpleAgent
# task.py
import logging


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

if name == "main":
    print("AI Agent Project Running...")


agent_state = {
    "mood": "idle",
    "current_task": None,
    "memory_size": 0
}

print(agent_state)
def pipeline(task):
    task = task.lower()
    task = task.strip()
    return f"processed: {task}"

print(pipeline(" Analyze AI "))
tasks = [
    {"name": "search", "priority": 2},
    {"name": "summarize", "priority": 1}
]

tasks.sort(key=lambda x: x["priority"])
print(tasks)

def decide(task_type):
    if task_type == "search":
        return "use_tool"
    return "think"

print(decide("search"))