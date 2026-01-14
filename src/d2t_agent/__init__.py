from ai_agents_libs import *

with DDGS() as ddgs:
    for r in ddgs.text("multi agent ai", max_results=2):
        print(r["title"])