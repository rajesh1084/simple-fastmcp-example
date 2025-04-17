# Simple FastMCP Example

This project demonstrates a simple implementation of a FastMCP server and client. The server provides resources, tools, and prompts, while the client interacts with the server using HTTP and Server-Sent Events (SSE).

## Project Structure

- **`src/fastmcp_server/remote_server.py`**: Contains the FastMCP server implementation with resources, tools and prompts.
- **`src/client.py`**: Contains the client implementation to interact with the FastMCP server.

## Features
Server Components

 - ### Resources:
   - `mcp://hello`: Returns a simple greeting message
   - `mcp://greeting/{name}`: Returns a personalized greeting with the provided name
 - ### Tools:
   - `echo`: Echoes back the input text
   - `add`: Adds two numbers together
 - ### Prompts:
   - `introduction`: Creates an introduction message using the specified name and role

Client Capabilities
 - Connect to the server via SSE
 - List available resources and tools
 - Read content from resources
 - Call tools with parameters
 - Get prompt templates and results


## Requirements

- Python `>=3.13`
- Dependencies:
  - `mcp`
  - `fastapi`
  - `uvicorn`
  - `pydantic`
  - `starlette`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple-fastmcp-example
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Server
To run the FastMCP server:

```bash
python src/fastmcp_server/remote_server.py
```

The server will start and listen on `http://localhost:8000` with an SSE endpoint at `/sse`.


## Running the Client

To run the client:

```bash
python src/client.py
```

## Example Interaction
When running the client, you should see output similar to:
```bash
INFO:mcp-client:Connecting to MCP server at http://localhost:8000/sse
INFO:mcp-client:Connection initialized
INFO:mcp-client:Listing resources...

Available Resources:
- Hello Resource (mcp://hello)
- Personalized Greeting (mcp://greeting/{name})

Hello Resource Content: Hello from MCP Server!
Greeting Resource Content: Welcome to MCP, User!

Available Tools:
- echo: Echoes back the input text.
- add: Adds two numbers together.

Echo Tool Result: Echo: Hello, Server!
Add Tool Result: 8.0

Available Prompts:
- introduction: Creates an introduction message.

Introduction Prompt:
[assistant] You are a helpful assistant.
[user] Please introduce yourself to Developer who is a Software Engineer.
```

## License
