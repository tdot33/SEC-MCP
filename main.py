import asyncio
from fastmcp import FastMCP

# 1. Import the existing server objects from the Luis Rincon suite
from sec_mcp.scraper.server import mcp as scraper_mcp
from sec_mcp.edgar_core.server import mcp as edgar_mcp

# 2. Create the Master Server
mcp = FastMCP("SEC-Master-Suite")

async def initialize():
    # Use import_server to bundle them. 
    # Prefixing helps n8n/AI identify which module a tool belongs to.
    await mcp.import_server(scraper_mcp, prefix="scraper")
    await mcp.import_server(edgar_mcp, prefix="edgar")

if __name__ == "__main__":
    # We run the initialization to actually copy the tools
    asyncio.run(initialize())
    
    # Start the server (FastMCP Cloud/GCP will handle the port)
    mcp.run(transport="sse", port=8080)
