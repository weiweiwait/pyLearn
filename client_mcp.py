#client_demo.py
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, types
import asyncio
#Client会使用这里的配置来启动本地 MCP Server
server_params = StdioServerParameters(
   command="python",
   args=["./server_macp.py"],
    env=None
 )

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=None) as session:
            await session.initialize()
            print('\n正在调用工具...')
            result = await session.call_tool("calculate",{ "expression": "188*23-34" })
            print(result.content)

asyncio.run(main())