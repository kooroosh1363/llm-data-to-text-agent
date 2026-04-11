# LLM & Agent Frameworks
import langchain
import langgraph
import autogen
from crewai import Agent, Task, Crew

# OpenAI / LLM Providers
from openai import OpenAI
from ai_agents_libs import *

decision = {
    "task": "search",
    "tool": "browser",
    "status": "ready"
}

print(decision)
# Memory & Vector Databases
import chromadb
import faiss

from ai_agents_libs import *

async def run_agent():
    await asyncio.sleep(1)
    print("Async agent running")

asyncio.run(run_agent())


# memory/shared.py
shared_memory = []

def save(data):
    shared_memory.append(data)

def get_all():
    return shared_memory


# core/orchestrator.py
from memory.shared import save

save(result)


# core/orchestrator.py
from agents.manager import Manager
from agents.researcher import Researcher
from agents.writer import Writer

manager = Manager("Manager")
researcher = Researcher("Researcher")
writer = Writer("Writer")

def run_system(task):
    decision = manager.run(task)

    if decision == "research":
        data = researcher.run(task)
        return writer.run(data)

    return writer.run(task)


# main.py
from core.orchestrator import run_system

task = "search latest AI agent tools"

result = run_system(task)

print(result)

# memory/shared.py
shared_memory = []

def save(data):
    shared_memory.append(data)

def get_all():
    return shared_memory


# utils/logger.py
def log_agent(agent, msg):
    print(f"[{agent}] -> {msg}")



# core/orchestrator.py
from utils.logger import log_agent

log_agent("Manager", decision)

# core/state.py
class AgentState:
    def init(self, task):
        self.task = task
        self.plan = []
        self.data = ""
        self.result = ""


# agents/manager.py
from core.llm import ask_llm

def manager_decide(task):
    prompt = f"""
    Decide what to do:
    Task: {task}
    Options: research, write
    Answer only one word.
    """
    return ask_llm(prompt).strip().lower()



# core/planner.py
from core.llm import ask_llm

def create_plan(task):
    prompt = f"Create 3 steps plan for: {task}"
    steps = ask_llm(prompt)
    return steps.split("\n")


# agents/researcher.py
from tools.search_tool import search_tool

def do_research(step):
    return search_tool(step)