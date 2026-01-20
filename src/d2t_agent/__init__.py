from ai_agents_libs import *
from ai_agents_libs import *

def create_agent(role, goal):
    return Agent(role=role, goal=goal, backstory="AI helper")

agent = create_agent("Analyst", "Analyze data")
print(agent.role)

with DDGS() as ddgs:
    for r in ddgs.text("multi agent ai", max_results=2):
        print(r["title"])