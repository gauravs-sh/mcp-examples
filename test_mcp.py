#!/usr/bin/env python3
"""
Test script to check MCP client initialization and identify Playwright MCP server issues.
"""

import asyncio
from mcp_use import MCPClient

async def test_mcp_client():
    """Test MCP client initialization to identify Playwright server issues."""
    config_file = "browser_mcp.json"

    print("Testing MCP client initialization...")
    print("Config file:", config_file)

    try:
        # Create MCPClient from config file
        client = MCPClient.from_config_file(config_file)
        print("SUCCESS: MCP client created successfully")
        print(f"MCPClient methods: {[method for method in dir(client) if not method.startswith('_')]}")

        # Check what servers are configured
        print(f"Configured servers: {list(client.config.keys()) if hasattr(client, 'config') else 'No config attribute'}")

        # Try to create individual server sessions to test them one by one
        server_names = list(client.config['mcpServers'].keys())
        print(f"Configured servers: {server_names}")

        for server_name in server_names:
            print(f"\nTesting server '{server_name}'...")
            try:
                await client.create_session(server_name)
                print(f"SUCCESS: Server '{server_name}' started successfully")
            except Exception as e:
                print(f"ERROR: Server '{server_name}' failed: {e}")

        # Check what servers are available
        print(f"\nAvailable servers: {list(client.sessions.keys())}")

        # Check each server status
        for server_name, session in client.sessions.items():
            print(f"Server '{server_name}': Connected")

        # Clean up
        await client.close_all_sessions()
        print("SUCCESS: All sessions closed successfully")

    except Exception as e:
        print(f"ERROR: Error during MCP client initialization: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_mcp_client())
