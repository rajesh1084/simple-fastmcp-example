import asyncio
import logging
from mcp.server.fastmcp.server import FastMCP
from mcp.server.sse import SseServerTransport
from mcp.types import TextContent, GetPromptResult

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-server")

# Create SSE transport with explicit endpoint configuration
sse_transport = SseServerTransport(endpoint="/sse")

# Create a FastMCP server
server = FastMCP(
    name="SimpleMCPServer",
    instructions="A simple MCP server with basic tools and resources.",
)


# Define a resource
@server.resource(
    "mcp://hello", name="Hello Resource", description="Returns a hello message."
)
def hello_resource() -> str:
    return "Hello from MCP Server!"


# Define another resource with parameters
@server.resource(
    "mcp://greeting/{name}",
    name="Personalized Greeting",
    description="Returns a personalized greeting.",
)
def greeting_resource(name: str) -> str:
    return f"Welcome to MCP, {name}!"


# Define a simple tool
@server.tool(name="echo", description="Echoes back the input text.")
def echo_tool(text: str) -> str:
    return f"Echo: {text}"


# Define a math tool
@server.tool(name="add", description="Adds two numbers together.")
def add_tool(a: float, b: float) -> float:
    return a + b


# Define a prompt template
@server.prompt(name="introduction", description="Creates an introduction message.")
def introduction_prompt(name: str, role: str) -> GetPromptResult:
    # Return a GetPromptResult object with properly formatted messages
    # Note: Using only 'assistant' and 'user' roles as required by the validation
    return GetPromptResult(
        messages=[
            {
                "role": "assistant",  # Changed from 'system' to 'assistant'
                "content": TextContent(
                    type="text", text="You are a helpful assistant."
                ),
            },
            {
                "role": "user",
                "content": TextContent(
                    type="text",
                    text=f"Please introduce yourself to {name} who is a {role}.",
                ),
            },
        ]
    )


if __name__ == "__main__":
    # Run the server with the explicitly configured SSE transport
    logger.info("Starting MCP server on http://localhost:8000")
    server.run(transport="sse")
