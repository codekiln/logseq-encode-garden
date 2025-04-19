tags:: [[Diataxis/How To]]

- # How to use [[mise]] and [[1Password/Dev/op/run]] to inject [[API/Key]] into [[aider]]
	- ## Overview
		- This guide shows you how to securely inject API keys from 1Password into aider using mise's environment management and `op run`
		- For developers who want to use aider with their OpenAI API key stored in 1Password
		- We'll set this up to work with both global defaults and project-specific configurations
		- The approach uses mise's environment variables with 1Password secret references, ensuring no secrets are stored on disk
	- ## Prerequisites
		- [[mise]] installed on your system
		- [[1Password/CLI]] installed and configured
		- [[1Password/Desktop]] app installed (for biometric authentication)
		- A 1Password vault containing your API keys
		- [[aider]] installed on your system
	- ## Steps
		- ### 1. Configure Global Default
			- Edit `~/.config/mise/config.toml` to set your default API keys:
				- ~~~toml
				  # Global environment variables
				  [env]
				  # Default API keys using 1Password references
				  # These match aider's supported environment variables:
				  # https://aider.chat/docs/config/api-keys.html
				  OPENAI_API_KEY = "op://your-vault/default-openai-api-key/credential"
				  ANTHROPIC_API_KEY = "op://your-vault/default-anthropic-api-key/credential"
				  GEMINI_API_KEY = "op://your-vault/default-gemini-api-key/credential"
				  
				  # Simple task that wraps aider with op run
				  [tasks.aider]
				  description = "Run aider with 1Password integration, passing through all arguments"
				  run = "op run -- aider $@"  # Pass all arguments directly to aider
				  alias = "ai"
				  dir = "{{cwd}}"  # Run in the current directory, not mise's config directory
				  ~~~
			- Replace `your-vault` with your actual 1Password vault name
			- Update the item names to match your 1Password items
		- ### 2. Run aider using mise tasks
			- Basic usage:
				- ~~~bash
				  mise run aider  # or mise ai
				  mise run aider --model sonnet  # use Claude 3 Sonnet
				  mise run aider --model gpt-4 --context-size 128k  # use GPT-4 with custom context size
				  mise run aider path/to/file1.py path/to/file2.py  # add specific files
				  ~~~
			- The task will:
				- Use `op run` to securely inject secrets at runtime
				- Load environment variables from mise configuration
				- Run in your current working directory
				- Pass all arguments directly to aider
				- Automatically clean up secrets when aider exits
		- ### 3. Project-Specific Configuration
			- Create a `.mise.toml` in your project directory to use project-specific API keys:
				- ~~~toml
				  # Project-specific environment variables
				  [env]
				  # Override API keys for this project
				  # See https://aider.chat/docs/config/api-keys.html for all supported keys
				  # Each project can have its own set of API keys from different vaults
				  OPENAI_API_KEY = "op://project-vault/project-openai-key/credential"
				  ANTHROPIC_API_KEY = "op://project-vault/project-anthropic-key/credential"
				  GEMINI_API_KEY = "op://project-vault/project-gemini-key/credential"
				  ~~~
			- For project-specific overrides that shouldn't be committed:
				- Create `.mise.local.toml` (add to `.gitignore`):
					- ~~~toml
					  [env]
					  # Project API keys for just this project, not committed to version control
					  OPENAI_API_KEY = "op://vault-name/project-openai-key/credential"
					  ~~~
	- ## Troubleshooting
		- If you get "op not found", ensure 1Password CLI is properly installed
		- If you get "mise not found", ensure mise is properly installed and in your PATH
		- If aider complains about missing API key:
			- Check your mise configuration files
			- Verify the 1Password vault and item names are correct
			- Ensure you're signed into 1Password CLI (`op signin`)
			- Ensure you're signed into the correct 1Password account if using multiple vaults
		- For CI/CD environments:
			- Use platform-specific secret management (e.g., GitHub Actions secrets)
			- Update the task configuration to handle both local and CI environments
	- ## Benefits of this Approach
		- No secrets stored on disk - only references in mise configuration
		- No separate `.env` files needed - everything managed by mise
		- Secrets only available during command execution
		- Seamless authentication via 1Password desktop app
		- Hierarchical configuration with mise (global → project → local)
		- Easy to override API keys per project
		- Integrated with mise's task management system
	- ## Related
		- [[1Password/Dev/op/run]]
		- [[mise]]
		- [[aider]]
		- [[API/Key/OpenAI]]
		- [[1Password/Dev/CLI/Secret Reference]]