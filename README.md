# Simple FastMCP Example

This project demonstrates a simple implementation of a FastMCP server and client. The server provides resources and tools, while the client interacts with the server using HTTP and Server-Sent Events (SSE).

## Project Structure

- **`src/fastmcp_server/remote_server.py`**: Contains the FastMCP server implementation.
- **`src/client.py`**: Contains the client implementation to interact with the FastMCP server.

## Requirements

- Python `>=3.13`
- Dependencies:
  - `mcp`
  - `requests`
  - `sseclient-py`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple-fastmcp-example
   ```

2. Install dependencies:
   ```bash
   pip install .
   or 
   uv sync
   ```

## Running the Server

The server is implemented in `remote_server.py`. It provides the following:

- **Resource**: `mcp://hello`  
  Returns a simple "Hello from FastMCP!" message.

- **Tool**: `greet`  
  Accepts a `name` parameter and returns a greeting message.

To run the server:

```bash
python src/fastmcp_server/remote_server.py
```

The server will start and listen for incoming requests.

## Running the Client

The client is implemented in `client.py`. It interacts with the server to:

1. Initialize an SSE session.
2. List available resources and tools.
3. Read a resource.
4. Call a tool (e.g., `greet`).
5. Listen for SSE events.

To run the client:

```bash
python src/client.py
```

## Example Usage

1. Start the server:
   ```bash
   python src/fastmcp_server/remote_server.py
   ```

2. In a separate terminal, run the client:
   ```bash
   python src/client.py
   ```

3. The client will:
   - List available resources and tools.
   - Read the `mcp://hello` resource.
   - Call the `greet` tool with the name "World".
   - Listen for SSE events.

## License
