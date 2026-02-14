from mcp.server.fastmcp import FastMCP
import json
import random
import os

# Create a named MCP server
mcp = FastMCP("MCP Demo")

# Load rejection reasons for No-as-a-Service
def load_reasons():
    """Load rejection reasons from JSON file"""
    reasons_file = os.path.join(os.path.dirname(__file__), '../reasons.json')
    try:
        with open(reasons_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback reasons if file not found
        return [
            "I appreciate the thought, but I'll have to pass.",
            "That's not something I can commit to right now.",
            "I'm going to respectfully decline.",
            "My schedule doesn't allow for that.",
            "Not today, thanks for asking though!"
        ]

# Cache reasons
_reasons_cache = None

def get_reasons():
    """Get cached reasons or load them"""
    global _reasons_cache
    if _reasons_cache is None:
        _reasons_cache = load_reasons()
    return _reasons_cache

# Load motivational quotes from JSON
def load_quotes():
    """Load motivational quotes from JSON file"""
    quotes_file = os.path.join(os.path.dirname(__file__), './quotes.json')
    try:
        with open(quotes_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback quotes if file not found
        return [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
        ]

# Cache quotes
_quotes_cache = None

def get_quotes():
    """Get cached quotes or load them"""
    global _quotes_cache
    if _quotes_cache is None:
        _quotes_cache = load_quotes()
    return _quotes_cache

# Add a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add No-as-a-Service tool
@mcp.tool()
def get_no_reason() -> str:
    """Get a random rejection reason from No-as-a-Service"""
    reasons = get_reasons()
    return random.choice(reasons)

# Add Motivational Quote tool
@mcp.tool()
def get_motivational_quote() -> str:
    """Get a random motivational quote for inspiration"""
    quotes = get_quotes()
    return random.choice(quotes)
 
# Add a message resource
@mcp.resource("greeting://{name}")
def get_message(name: str) -> str:
    """Get a customised welcome message"""
    return f"Welcome, {name}!"

# Pre-defined prompt template
@mcp.prompt()
def ask_code_review(code_snippet: str) -> str:
    """Generates a code review request"""
    return f"Please review the following code: {code_snippet}"

if __name__ == "__main__":
    mcp.run()