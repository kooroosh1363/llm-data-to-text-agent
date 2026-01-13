# --- Vector Memory ---
chroma_client = chromadb.Client()

# --- Tool ---
search = DDGS()

# --- Async check ---
async def run():
    print("AI Agents talk  stack is ready 🚀")

asyncio.run(run())