# Build Prompt: MCP No-as-a-Service & Motivation Server

## Project Overview
Build an MCP (Model Context Protocol) server called "MCP No-as-a-Service & Motivation" that provides two tools:
1. **get_no_reason()** - Returns a random creative rejection reason
2. **get_motivational_quote()** - Returns a random motivational quote

## Tech Stack
- Python 3.8+
- FastMCP library (part of the `mcp` package)
- JSON data files for storing quotes and reasons

## Project Structure
Create the following file structure:
```
mcp_no_and_motovation/
├── mcp_no_and_motovation.py    # Main MCP server
├── quotes.json                  # 30+ motivational quotes
├── reasons.json                 # 100+ rejection reasons
├── requirements.txt             # Dependencies
├── README.md                    # Documentation
└── BUILD_PROMPT.md              # This file
```

## Step 1: Create Main Server File (mcp_no_and_motovation.py)

Create a FastMCP server with the following features:
- Initialize FastMCP with server name "MCP Demo"
- Implement global caching for quotes and reasons (`_quotes_cache`, `_reasons_cache`)
- Create `load_quotes()` function that:
  - Loads from `quotes.json`
  - Handles FileNotFoundError with fallback values
  - Handles JSONDecodeError with fallback values
  - Returns a list of quote strings
- Create `load_reasons()` function that:
  - Loads from `reasons.json`
  - Handles FileNotFoundError with fallback values
  - Handles JSONDecodeError with fallback values
  - Returns a list of reason strings
- Create `get_quotes()` function that uses cache
- Create `get_reasons()` function that uses cache
- Create two MCP tools using `@mcp.tool()` decorator:
  - `get_no_reason()`: Returns random rejection reason, includes docstring
  - `get_motivational_quote()`: Returns random motivational quote, includes docstring
- Include `mcp.run()` to start the server

## Step 2: Create quotes.json

Create a JSON array with 30+ motivational quotes. Include quotes from:
- Steve Jobs
- Eleanor Roosevelt
- Nelson Mandela
- Theodore Roosevelt
- Wayne Gretzky
- Martin Luther King Jr.
- Maya Angelou
- Albert Einstein
- And others

Format: `"Quote text. - Author Name"`

Minimum content: 30 diverse, inspiring quotes.

## Step 3: Create reasons.json

Create a JSON array with 100+ creative rejection reasons. Include variety like:
- Humorous rejections
- Metaphorical responses
- Self-aware humor
- Poetic declines
- Honest but witty reasons

Examples to inspire:
- "My future self wrote me a note: 'Please don't do this again.'"
- "Even my coffee said, 'Not today.'"
- "I'd rather say no with honesty than yes with resentment."

Minimum content: 100+ unique rejection reasons.

## Step 4: Create requirements.txt

List all Python dependencies:
- `mcp>=0.1.0` (for FastMCP and MCP protocol support)

## Step 5: Create README.md

Document the project with:
- Project title and description
- Overview of the two tools
- Project structure explanation
- File descriptions for each component
- Prerequisites (Python 3.8+, mcp package)
- Installation instructions
- Three methods to run the server:
  1. Using Python Extension (F5/Ctrl+F5)
  2. Using Integrated Terminal
  3. Using VS Code Tasks
- Code explanation section covering:
  - Server initialization
  - Caching mechanism
  - Tool decoration
  - Error handling
- Usage examples showing tool responses
- Customization guide for adding quotes/reasons
- Troubleshooting section
- License statement

## Key Requirements

### Code Requirements:
- Use `import random`, `import json`, `from pathlib import Path`
- Import FastMCP: `from mcp.server.fastmcp import FastMCP`
- UTF-8 encoding for file operations
- Proper error handling for missing files and invalid JSON
- Fallback data for both quotes and reasons
- Global cache variables to avoid reloading files

### Data Requirements:
- At least 30 motivational quotes in quotes.json
- At least 100 rejection reasons in reasons.json
- All JSON data in proper array format

### Documentation Requirements:
- Clear README with multiple setup methods
- Code comments explaining caching and error handling
- Usage examples in documentation
- Troubleshooting section

## Success Criteria

✓ Server starts without errors: `python mcp_no_and_motovation.py`
✓ Both tools return random values from their respective JSON files
✓ Caching prevents repeated file loading
✓ Fallback values work if JSON files are missing
✓ All code is properly commented
✓ README provides complete setup and usage instructions
✓ Project runs successfully with `pip install -r requirements.txt && python mcp_no_and_motovation.py`

## Notes

- Ensure cross-platform compatibility (works on Windows, macOS, Linux)
- Use relative paths with Path for file operations
- Tools should have descriptive docstrings for MCP discovery
- Server should handle UTF-8 encoded JSON properly
- Fallback data should be meaningful and useful
