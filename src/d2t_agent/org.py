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

def run_tool(name, query):
    return f"{name} executed with query: {query}"

print(run_tool("search_tool", "AI agents"))

steps = 0

for i in range(3):
    steps += 1

print("Total steps:", steps)


results = []

results.append({"task": "search", "output": "AI news found"})
print(results)

def is_success(result):
    return "found" in result

print(is_success("AI news found"))

import time

start = time.time()
time.sleep(1)
print("Execution time:", time.time() - start)

def retry(task, attempts=3):
    for i in range(attempts):
        print("Trying:", task)

retry("fetch data")

status = "running"

if status == "running":
    print("Agent is processing tasks")

# settings.py
PROJECT_NAME = "ai-agent-system"
VERSION = "0.1"
DEBUG = True

# config_loader.py
from settings import PROJECT_NAME, VERSION

def load_config():
    return {"name": PROJECT_NAME, "version": VERSION}

# registry.py
agents = {}

def register_agent(name, agent):
    agents[name] = agent


# registry.py
def get_agent(name):
    return agents.get(name)


# task_factory.py
def create_task(name, data):
    return {"task": name, "data": data}

# task_runner.py
def run_task(task):
    print("Running task:", task["task"])
    

# storage.py
def read_all():
    return data_store

# main.py
from config_loader import load_config

config = load_config()
print("Project:", config["name"])

# agents/agent_core.py
class Agent:
    def init(self, name):
        self.name = name
        self.state = "idle"
        self.memory = []

    def think(self, task):
        self.state = "thinking"
        return f"{self.name} thinking about {task}"
    

# agents/agent_core.py
    def act(self, decision):
        self.state = "acting"
        return f"{self.name} executes {decision}"
    

# agents/agent_core.py
    def remember(self, info):
        self.memory.append(info)

# tasks/planner.py
def plan(task):
    return [
        f"analyze {task}",
        f"search {task}",
        f"generate result for {task}"
    ]


# main.py
from core.runner import run_agent

result = run_agent("AI agents")

for r in result:
    print(r)


# utils/logger.py
import datetime

def log(msg):
    print(f"[{datetime.datetime.now()}] {msg}")


# core/runner.py
from utils.logger import log

log("Agent started")
