- [servers](https://github.com/modelcontextprotocol/servers)
- ## [[MCP/GitHub/servers/Getting Started]] [Getting Started](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-getting-started)
	- Typescript-based servers in this repository can be used directly with `npx`.
	- For example, this will start the [[MCP/GitHub/servers/memory]] [Memory](https://github.com/modelcontextprotocol/servers/blob/main/src/memory) server:
	- ```
	  npx -y @modelcontextprotocol/server-memory
	  ```
		- #note *to find the exact name, you might need to do `npm search @modelcontextprotocol`*
		- #Example for [[MCP/GitHub/servers/GitHub]]
			- `npx -y @modelcontextprotocol/server-github` will actually **start a server**
	- Python-based servers in this repository can be used directly with [[uv]]'s [`uvx`](https://docs.astral.sh/uv/concepts/tools/) or [`pip`](https://pypi.org/project/pip/). `uvx` is recommended for ease of use and setup.
	- For example, this will start the [Git](https://github.com/modelcontextprotocol/servers/blob/main/src/git) server:
	- ```
	  # With uvx
	  uvx mcp-server-git
	  
	  # With pip
	  pip install mcp-server-git
	  python -m mcp_server_git
	  ```
	- Follow [these](https://docs.astral.sh/uv/getting-started/installation/) instructions to install  [[uv]] and [these](https://pip.pypa.io/en/stable/installation/) to install `pip`.