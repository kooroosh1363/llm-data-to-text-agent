from ai_agents_libs import *
from ai_agents_libs import *

results = col.query(query_texts=["What did agent learn?"], n_results=1)
print(results)

agent = Agent(
    role="Searcher",
    goal="Find AI info",
    backstory="Uses search tool"
)

print(agent.role, agent.goal)
