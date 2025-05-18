tags:: [[Diataxis/How To]]

- # How To get started with OpenAI Codex CLI using [[mise/Tasks]] and [[1Password/Dev/op/run]]
	- ## Goal
		- Provide a minimal, secure workflow to install and run the OpenAI Codex CLI, with API credentials managed via 1Password and injected at runtime using `op run`.
	- ## Preconditions
		- macOS with 1Password CLI (`op`) installed and authenticated.
		- `mise` installed and activated in your shell.
	- ## Procedure
		- ### 1. Configure global `~/.config/mise/config.toml`
			- Create or update to include:
			  ~~~toml
			  # ~/.config/mise/config.toml
			  [tools]
			  node = "lts"
			  npm = "latest"  # Ensure we have latest npm for package management
			  
			  [tasks.codex]
			  description = "Run Codex CLI with OPENAI_API_KEY from 1Password"
			  run = "op run -- npx @openai/codex $@"
			  alias = "cx"
			  dir = "{{cwd}}"  # Run in current directory
			  env = { OPENAI_API_KEY = "op://vault/default-openai-key/credential" }
			  ~~~
			- This configuration:
				- Pins Node.js to the LTS release
				- Makes the codex task available globally
				- Scopes the API key to the codex task only
		- ### 2. (Optional) Override at project level
			- In your project's `.mise.toml`, you can override the API key or other settings:
			  ~~~toml
			  [tasks.codex]
			  # Override with a different API key for this project
			  env = { OPENAI_API_KEY = "op://vault/project-specific-openai-key/credential" }
			  # Or add project-specific arguments
			  run = "op run -- npx @openai/codex --model=gpt-4 $@"
			  ~~~
			- Project-level settings will take precedence over global settings
			- You can override any task property: `env`, `run`, `description`, etc.
		- ### 3. Install dependencies
			- Run:
			  ~~~bash
			  mise install
			  ~~~
			- This will install Node.js and npm at the specified versions
		- ### 4. Try a sample prompt
			- Run:
			  ~~~bash
			  mise run codex "Explain how the HTTP status code 418 came to be."
			  ~~~
			- Or use the alias:
			  ~~~bash
			  cx "Explain how the HTTP status code 418 came to be."
			  ~~~
	- ## Troubleshooting
		- **`codex: command not found`**
			- Ensure mise is properly activated in your shell
			- Try running with explicit `mise run codex` instead of the alias
		- **Missing API key**
			- Verify retrieval:
			  ~~~bash
			  op run -- printenv OPENAI_API_KEY
			  ~~~
			- Check if a project-level override is interfering with the global config
	- ## References
		- [Configuration | mise-en-place](https://mise.jdx.dev/configuration.html)
		- [mise use | mise-en-place](https://mise.jdx.dev/cli/use.html)
		- [TOML-based Tasks | mise-en-place](https://mise.jdx.dev/tasks/toml-tasks.html)
		- [OpenAI Codex CLI repository](https://github.com/openai/codex)
		- [1Password CLI op run documentation](https://developer.1password.com/docs/cli/reference/commands/run/)