# MCP No-as-a-Service & Motivation

An MCP (Model Context Protocol) server that provides two useful tools:
1. **No-as-a-Service** - Get creative, polite rejection reasons when you need to decline requests
2. **Motivational Quotes** - Get daily inspiration with a collection of motivational quotes

## Project Overview

This project implements a FastMCP server that serves two tools via the Model Context Protocol. It's perfect for AI assistants, chatbots, or any application that needs to generate thoughtful rejection messages or provide motivational inspiration.

### Tools

#### `get_no_reason()`
Returns a random, creative rejection reason from a curated collection. Perfect for:
- Politely declining requests
- Getting inspiration for how to say "no"
- Humor and entertainment

#### `get_motivational_quote()`
Returns a random motivational quote from a collection of 30+ inspiring quotes. Features authors like:
- Steve Jobs
- Eleanor Roosevelt
- Nelson Mandela
- And many more

## Project Structure

```
mcp_no_and_motovation/
├── mcp_no_and_motovation.py    # Main MCP server code
├── quotes.json                  # Collection of 30+ motivational quotes
├── reasons.json                 # Collection of 100+ creative rejection reasons
└── README.md                    # This file
```

## File Descriptions

### `mcp_no_and_motovation.py`
The main server file containing:
- FastMCP server initialization
- `load_quotes()` - Loads quotes from JSON with fallback defaults
- `load_reasons()` - Loads rejection reasons from JSON with fallback defaults
- Caching mechanism for performance
- Two MCP tools: `get_no_reason()` and `get_motivational_quote()`

### `quotes.json`
A JSON array containing 30+ motivational quotes with attributed authors. Examples:
- "The only way to do great work is to love what you do. - Steve Jobs"
- "Believe you can and you're halfway there. - Theodore Roosevelt"

### `reasons.json`
A JSON array containing 100+ creative rejection reasons. Examples:
- "My future self wrote me a note: 'Please don't do this again.'"
- "Even my coffee said, 'Not today.'"
- "I'd rather say no with honesty than yes with resentment."

## Prerequisites

- Python 3.8+
- `mcp` package with FastMCP support

## Installation

1. **Clone or download the project** to your local machine
2. **Install dependencies:**
   ```bash
   pip install mcp
   ```

## How to Run in VS Code

### Method 1: Using Python Extension (Recommended)

1. **Open the project** in VS Code:
   ```bash
   code /path/to/mcp_no_and_motovation
   ```

2. **Install Python extension** (if not already installed):
   - Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac)
   - Search for "Python"
   - Install the Microsoft Python extension

3. **Run the server**:
   - Open `mcp_no_and_motovation.py`
   - Press `Ctrl+F5` (or `Cmd+F5` on Mac) to run without debugging
   - Or press `F5` to run with debugging

4. The server will start and listen for MCP connections

### Method 2: Using Integrated Terminal

1. **Open the integrated terminal** in VS Code:
   - Press `Ctrl+` ` (backtick) or go to View → Terminal

2. **Navigate to the project directory**:
   ```bash
   cd /path/to/mcp_no_and_motovation
   ```

3. **Run the server**:
   ```bash
   python mcp_no_and_motovation.py
   ```

4. The server will start running

### Method 3: Using VS Code Tasks

1. **Create a task** (optional):
   - Press `Ctrl+Shift+D` to open Run and Debug
   - Click "create a launch.json file"
   - Or press `Ctrl+Shift+P` and search for "Tasks: Create Task"

2. **Add this configuration** to your `.vscode/tasks.json`:
   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Run MCP Server",
         "type": "shell",
         "command": "python",
         "args": ["mcp_no_and_motovation.py"],
         "group": {
           "kind": "build",
           "isDefault": true
         }
       }
     ]
   }
   ```

3. **Run the task**:
   - Press `Ctrl+Shift+B` to run the default build task

## Code Explanation

### Server Initialization
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("MCP Demo")
```
Creates an MCP server with the name "MCP Demo" that can be discovered and called by MCP clients.

### Caching Mechanism
The code uses global caching (`_reasons_cache` and `_quotes_cache`) to:
- Load JSON files only once
- Improve performance on subsequent tool calls
- Provide fallback values if files are missing

### Tool Decoration
```python
@mcp.tool()
def get_no_reason() -> str:
    """Get a random rejection reason from No-as-a-Service"""
    reasons = get_reasons()
    return random.choice(reasons)
```
The `@mcp.tool()` decorator exposes Python functions as MCP tools that can be called by clients.

### Error Handling
- Files are loaded with UTF-8 encoding
- FileNotFoundError and JSONDecodeError are caught
- Fallback hardcoded values are returned if JSON files fail to load

## Usage Examples

When the server is running, clients can call:

```
Tool: get_no_reason()
Response: "My enthusiasm is sincere, but my availability is imaginary."
```

```
Tool: get_motivational_quote()
Response: "You miss 100% of the shots you don't take. - Wayne Gretzky"
```

## Customization

### Add More Quotes
Edit `quotes.json` and add new quote strings to the array:
```json
[
  "Your existing quote...",
  "Your new quote here. - Author Name"
]
```

### Add More Rejection Reasons
Edit `reasons.json` and add new reason strings to the array:
```json
[
  "Your existing reason...",
  "Your new creative reason here."
]
```

## Troubleshooting

### Server won't start
- Ensure Python 3.8+ is installed: `python --version`
- Install the mcp package: `pip install mcp`
- Check that you're in the correct directory

### Files not found
- The code includes fallback hardcoded values
- Ensure `quotes.json` and `reasons.json` are in the same directory as the script
- Check file permissions

### Import errors
- Install the mcp package: `pip install mcp`
- Verify the package is installed: `pip list | grep mcp`

## License

This project is open source and available for educational and personal use.
