import asyncio
import logging
from mcp import ClientSession
from mcp.client.sse import sse_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-client")

SERVER_URL = "http://localhost:8000/sse"


async def main():
    # Connect to the remote server via SSE
    logger.info(f"Connecting to MCP server at {SERVER_URL}")

    async with sse_client(SERVER_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            logger.info("Connection initialized")

            # List available resources
            logger.info("Listing resources...")
            resources = await session.list_resources()
            print("\nAvailable Resources:")

            # Handle resources as a list of objects or tuples
            for resource in resources:
                if hasattr(resource, "name") and hasattr(resource, "uri"):
                    # Handle as object with attributes
                    print(f"- {resource.name} ({resource.uri})")
                elif isinstance(resource, (list, tuple)) and len(resource) >= 2:
                    # Handle as tuple (name, uri, ...)
                    print(f"- {resource[0]} ({resource[1]})")
                else:
                    # Just print the raw resource
                    print(f"- {resource}")

            # Read the hello resource
            logger.info("Reading 'hello' resource...")
            hello_content = await session.read_resource("mcp://hello")
            print(f"\nHello Resource Content: {hello_content}")

            # Read the greeting resource with a parameter
            logger.info("Reading 'greeting' resource with parameter...")
            greeting_content = await session.read_resource("mcp://greeting/User")
            print(f"\nGreeting Resource Content: {greeting_content}")

            # List available tools
            logger.info("Listing tools...")
            tools = await session.list_tools()
            print("\nAvailable Tools:")
            for tool in tools:
                if hasattr(tool, "name") and hasattr(tool, "description"):
                    # Handle as object with attributes
                    print(f"- {tool.name}: {tool.description}")
                elif isinstance(tool, (list, tuple)) and len(tool) >= 2:
                    # Handle as tuple (name, description, ...)
                    print(f"- {tool[0]}: {tool[1]}")
                else:
                    # Just print the raw tool
                    print(f"- {tool}")

            # Call the echo tool
            logger.info("Calling 'echo' tool...")
            echo_result = await session.call_tool("echo", {"text": "Hello, Server!"})
            print(f"\nEcho Tool Result: {echo_result}")

            # Call the add tool
            logger.info("Calling 'add' tool...")
            add_result = await session.call_tool("add", {"a": 5, "b": 3})
            print(f"\nAdd Tool Result: {add_result}")

            # List available prompts
            logger.info("Listing prompts...")
            prompts = await session.list_prompts()
            print("\nAvailable Prompts:")
            for prompt in prompts:
                if hasattr(prompt, "name") and hasattr(prompt, "description"):
                    print(f"- {prompt.name}: {prompt.description}")
                elif isinstance(prompt, (list, tuple)) and len(prompt) >= 2:
                    print(f"- {prompt[0]}: {prompt[1]}")
                else:
                    print(f"- {prompt}")

            # Get prompt result
            logger.info("Getting 'introduction' prompt...")
            try:
                intro_prompt = await session.get_prompt(
                    "introduction", {"name": "Developer", "role": "Software Engineer"}
                )
                print("\nIntroduction Prompt:")

                # Handle different response formats
                try:
                    if hasattr(intro_prompt, "messages"):
                        messages = intro_prompt.messages
                    elif isinstance(intro_prompt, dict) and "messages" in intro_prompt:
                        messages = intro_prompt["messages"]
                    else:
                        messages = intro_prompt

                    for message in messages:
                        if hasattr(message, "role") and hasattr(message, "content"):
                            print(f"[{message.role}] {message.content}")
                        elif (
                            isinstance(message, dict)
                            and "role" in message
                            and "content" in message
                        ):
                            content = message["content"]
                            if hasattr(content, "text"):
                                print(f"[{message['role']}] {content.text}")
                            elif isinstance(content, dict) and "text" in content:
                                print(f"[{message['role']}] {content['text']}")
                            else:
                                print(f"[{message['role']}] {content}")
                        else:
                            print(f"- {message}")
                except Exception as e:
                    print(f"Could not parse prompt messages: {e}")
                    print(f"Raw prompt data: {intro_prompt}")
            except Exception as e:
                print(f"Error getting prompt: {e}")


if __name__ == "__main__":
    asyncio.run(main())
