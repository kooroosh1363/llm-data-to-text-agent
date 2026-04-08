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

