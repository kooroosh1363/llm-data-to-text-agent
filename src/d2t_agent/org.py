from ai_agents_libs import *

agent = Agent(
    role="Searcher",
    goal="Find AI info",
    backstory="Uses search tool"
)

print(agent.role, agent.goal)
