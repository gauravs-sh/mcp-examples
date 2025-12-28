# mcp-examples

A small collection of Python example code demonstrating how to use MCP (Model Context Protocol) servers and clients.

MCP stands for Model Context Protocol.

## Contents

- app.py — Interactive chat example using MCPAgent with built-in conversation memory (requires GROQ API key and dependencies listed in pyproject.toml).
- test_mcp.py — Test script to initialize MCPClient and attempt to start configured MCP servers (useful for debugging Playwright/other MCP servers).
- browser_mcp.json — MCP server configuration used by MCPClient (includes Playwright and DuckDuckGo search server entries).
- pyproject.toml — Project metadata and runtime dependencies.
- main.py — Small placeholder entrypoint.

## Requirements

- Python 3.11+
- pip
- Recommended: virtual environment (venv or virtualenv)
- Environment variable required for app.py:
  - GROQ_API_KEY — API key for langchain-groq (used by app.py)

## Setup

1. Clone the repository:

   git clone https://github.com/gauravs-sh/mcp-examples.git
   cd mcp-examples

2. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows

3. Install dependencies (from pyproject.toml):

   pip install "langchain-groq>=1.1.1" "langchain-openai>=1.1.6" "mcp-use>=1.5.1"

(If you prefer a requirements.txt, you can generate one from pyproject.toml.)

## Usage

### Interactive chat (app.py)

1. Create a .env file with your GROQ API key:

   GROQ_API_KEY=your_groq_api_key_here

2. Run the chat example:

   python app.py

Notes:
- The script loads browser_mcp.json to create an MCPClient which can launch local MCP servers configured there.
- Commands: type `clear` to clear the conversation history, and `exit` or `quit` to end the session.
- The example uses ChatGroq(model="llama-3.1-8b-instant"). Adjust to an available model as needed.

### Test MCP client & servers (test_mcp.py)

Run the script to validate MCPClient initialization and attempt to start servers listed in browser_mcp.json:

   python test_mcp.py

The script prints configured servers, attempts to create sessions for each, and reports success or errors.

## browser_mcp.json

This file contains mcpServers definitions, e.g.:

{
  "mcpServers": {
    "playwright": { "command": "npx", "args": ["@playwright/mcp@0.0.52"] },
    "duckduckgo-search": { "command": "npx", "args": ["-y", "duckduckgo-mcp-server"] }
  }
}

MCPClient.from_config_file reads this to know which local processes to launch as MCP servers.

## Development

- pyproject.toml declares project metadata and dependencies.
- Add small, self-contained examples under an examples/ directory if you expand the repo.
- Use pytest for tests and standard logging.

## Contributing

Contributions welcome! Fork, branch, add tests and documentation, then open a pull request.

## License

This repository is licensed under the MIT License. See LICENSE for details.

## Contact

Owner: gauravs-sh — https://github.com/gauravs-sh
