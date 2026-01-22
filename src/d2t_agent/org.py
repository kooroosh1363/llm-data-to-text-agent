from ai_agents_libs import *


db = chromadb.Client()
mem = db.create_collection("agent_mem")

mem.add(
    documents=["Agent can use tools"],
    ids=["001"]
)

print(mem.query(query_texts=["tools"], n_results=1))

state = {"step": "start", "data": None}
print(state)

results = col.query(query_texts=["What did agent learn?"], n_results=1)
print(results)

agent = Agent(
    role="Searcher",
    goal="Find AI info",
    backstory="Uses search tool"
)

print(agent.role, agent.goal)
