- [Codex Skills - Optional Metadata](https://developers.openai.com/codex/skills#optional-metadata)
	- Add `agents/openai.yaml` to configure UI metadata in the [Codex app](https://developers.openai.com/codex/app), to set invocation policy, and to declare tool dependencies for a more seamless experience with using the skill.
	  
	  ```yaml
	  interface:
	    display_name: "Optional user-facing name"
	    short_description: "Optional user-facing description"
	    icon_small: "./assets/small-logo.svg"
	    icon_large: "./assets/large-logo.png"
	    brand_color: "#3B82F6"
	    default_prompt: "Optional surrounding prompt to use the skill with"
	  
	  policy:
	    allow_implicit_invocation: false
	  
	  dependencies:
	    tools:
	      - type: "mcp"
	        value: "openaiDeveloperDocs"
	        description: "OpenAI Docs MCP server"
	        transport: "streamable_http"
	        url: "https://developers.openai.com/mcp"
	  ```
	  
	  `allow_implicit_invocation` (default: `true`): When `false`, Codex won’t implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works.