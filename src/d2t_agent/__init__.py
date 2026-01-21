from ai_agents_libs import *
from ai_agents_libs import *
from ai_agents_libs import *
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain AI agents in one sentence"
)

print(resp.output[0].content[0].text)

def create_agent(role, goal):
    return Agent(role=role, goal=goal, backstory="AI helper")

agent = create_agent("Analyst", "Analyze data")
print(agent.role)

with DDGS() as ddgs:
    for r in ddgs.text("multi agent ai", max_results=2):
        print(r["title"])