# Tools
from duckduckgo_search import DDGS

# Data Validation & Structures
from pydantic import BaseModel, Field

# Environment Variables
from dotenv import load_dotenv

# Async & System
import asyncio
import os
import json
import logging

from ai_agents_libs import *

load_dotenv()

# --- LLM ---
client = OpenAI()

# --- Simple Agent (CrewAI) ---
agent = Agent(
    role="Researcher",
    goal="Find useful AI info",
    backstory="An autonomous AI agent"
)

# --- Vector Memory ---
chroma_client = chromadb.Client()

# --- Tool ---
search = DDGS()

# --- Async check ---
async def run():
    print("AI Agents talk  stack is ready 🚀")

asyncio.run(run())