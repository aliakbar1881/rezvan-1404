import asyncio
from fastmcp import Client

client = Client("http://localhost:8002/mcp")
async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)
asyncio.run(call_tool("Ali"))
