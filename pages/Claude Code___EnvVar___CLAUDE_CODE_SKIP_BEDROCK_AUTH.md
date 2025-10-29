- # CLAUDE_CODE_SKIP_BEDROCK_AUTH
	- ## Purpose
		- Skip AWS authentication for Bedrock when using Claude Code
		- Primarily used when routing Bedrock requests through an [[LLM/Gateway]] or proxy service that handles authentication separately
	- ## Use Cases
		- When using an [[LLM/Gateway]] like [[LiteLLM]] that provides its own authentication layer
		- When using a proxy server that handles AWS credential management
		- When authentication is handled at a network gateway or middleware level
	- ## Configuration
		- ### Environment Variable
			- Set to any non-empty value (typically `1` or `true`) to enable skipping authentication
			- ~~~
			  export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
			  ~~~
		- ### settings.json
			- Can also be configured in Claude Code settings files (see [[Claude Code/Settings]])
			- ~~~
			  {
			    "env": {
			      "CLAUDE_CODE_SKIP_BEDROCK_AUTH": "1"
			    }
			  }
			  ~~~
		- ### Prerequisites
			- Must be used in combination with [[Claude Code/EnvVar/CLAUDE_CODE_USE_BEDROCK]]
			- The LLM gateway or proxy service must handle AWS authentication on your behalf
	- ## Related Environment Variables
		- [[Claude Code/EnvVar/CLAUDE_CODE_USE_BEDROCK]] - Enables Bedrock integration
		- [[Claude Code/EnvVar/CLAUDE_CODE_SKIP_VERTEX_AUTH]] - Similar functionality for Google Vertex AI
		- [[Claude Code/EnvVar/ANTHROPIC_MODEL]] - Model selection when using Bedrock
	- ## References
		- [[Claude Code/Settings]] - Official Claude Code settings documentation
		- [[Claude Code/Bedrock]] - AWS Bedrock integration guide
		- [[LiteLLM]] - Example LLM gateway implementation

