# LLM & Agent Frameworks
import langchain
import langgraph
import autogen
from crewai import Agent, Task, Crew

# OpenAI / LLM Providers
from openai import OpenAI

# Memory & Vector Databases
import chromadb
import faiss

from ai_agents_libs import *
load_dotenv()
client = OpenAI()
agent = Agent(role="Researcher", goal="Collect info", backstory="AI agent")
memory = chromadb.Client()
search = DDGS()
query = "latest AI agents frameworks"
results = list(search.text(query, max_results=3))
print(results[0]["title"])
async def main():
    print("Agent ready")
asyncio.run(main())