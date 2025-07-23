tags:: [[Diataxis/How To]]

- # How To use [[mise]] home-directory config to drive [[opencommit]] with [[OpenAI/API]] delivered through [[Azure]] for [[Conventional Commits]]
	- ## Goal
		- One-line command (`mise run oco`) that reads *staged* Git changes and writes a Conventional Commit message via OpenAI models running on Azure OpenAI Service.
	- ## Preconditions
		- **mise** ≥ 2025.5 installed and initialised in your shell.
		- Azure OpenAI Service endpoint and API key configured.
		- Git repo with changes staged (`git add …`).
		- Node ≥ 18 and OpenCommit CLI (installed below).
	- ## Procedure
		- ### 1. Install tools globally with mise
			- ```bash
			  mise use -g node@lts         # install Node runtime
			  mise use -g npm:opencommit   # install the CLI from NPM
			  ```
		- ### 2. Create or open `~/.config/mise/config.toml`
			- The following **global** config makes the task available in every repo:
				- ~~~toml
				  [tasks.oco]
				  description = "opencommit - AI-generated Conventional Commit on staged files"
				  run = "opencommit"
				  
				  [tasks.oco.env]
				  OCO_AI_PROVIDER = "azure"
				  OCO_API_URL     = "https://your-resource.openai.azure.com/"
				  OCO_API_KEY     = "your-azure-openai-api-key"
				  OCO_MODEL       = "gpt-4o-mini"  # your Azure deployment name
				  OCO_EMOJI       = true
				  OCO_DESCRIPTION = false
				  ~~~
			- Save and exit. `mise` auto-reloads configs on next run.
		- ### 3. (Optional) keep secrets in 1Password
			- Replace literal values with secret references, e.g.  
			  `OCO_API_KEY = "op://AI/AzureOpenAI/api-key"` and `OCO_API_URL = "op://AI/AzureOpenAI/endpoint-url"` – these resolve at runtime when you wrap the task with `op run -- mise run oco`. The pattern is identical to other mise examples that embed API secrets inside `env` blocks.
		- ### 4. Commit with a single command
		  1. Stage your work: `git add -A`
		  2. Run: `mise run oco --type feat --scope auth`  
		    *OpenCommit* streams the generated message, then executes `git commit -m "<msg>"`.
	- ## Troubleshooting
		- **"Provider not found"** → ensure `OCO_AI_PROVIDER` is set to `"azure"`.
		- **Azure auth errors** → verify your `OCO_API_URL` and `OCO_API_KEY` are correct in the Azure OpenAI Service.
		- **Model not found** → ensure `OCO_MODEL` matches your Azure deployment name (not the model name).
		- **Unexpected commit style** → adjust `OCO_EMOJI` and `OCO_DESCRIPTION` settings in the env block.
	- ## References
		- [OpenCommit Documentation](https://github.com/di-sukharev/opencommit/tree/master) - Official OpenCommit repository with Azure OpenAI configuration examples
		- Template of `env` in task blocks
		- `mise config` and `mise use -g` for editing global configs