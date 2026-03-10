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

events = ["start", "think", "act", "end"]

for e in events:
    print(f"event: {e}")short_memory = []

short_memory.append("User asked about AI agents")
print(short_memory)

result = {
    "task": "summarize",
    "status": "done",
    "output": "Short summary generated"
}

print(result)
MAX_STEPS = 3

for step in range(MAX_STEPS):
    print("step", step)


def route(tool_name):
    return f"Routing to {tool_name}"

print(route("search_tool"))    

chat_history = []

def add_message(role, content):
    chat_history.append({"role": role, "content": content})

add_message("user", "What is AI agent?")
add_message("agent", "AI agent is a system that acts autonomously")

print(chat_history)




def pipeline(task):
    task = task.lower()
    task = task.strip()
    return f"processed: {task}"

print(pipeline(" Analyze AI "))

def plan(task):
    return ["search info", "analyze data", "generate answer"]

steps = plan("Explain AI agents")
print(steps)

for step in steps:
    print("Running:", step)



tools = {
    "search": lambda q: f"results for {q}",
    "calc": lambda x: x * 2
}

print(tools["search"]("AI agents"))


def choose_tool(task):
    if "search" in task:
        return "search"
    return "calc"

print(choose_tool("search about LLM"))


result = {
    "task": "summarize",
    "status": "done",
    "output": "Short summary generated"
}

def generate_answer(task):
    return f"Answer for: {task}"

print(generate_answer("What is LangChain?"))

task = "search AI agents"
tool = choose_tool(task)
result = tools[tool](task)

print("Final:", result)

import uuid

task_id = str(uuid.uuid4())
print("Task ID:", task_id)

from collections import deque

task_queue = deque()
task_queue.append("search ai news")
task_queue.append("summarize article")

print(task_queue.popleft())

def classify_task(text):
    if "search" in text:
        return "tool_search"
    return "analysis"

print(classify_task("search latest AI models"))

