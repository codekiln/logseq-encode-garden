tags:: [[Diataxis/How To]]

- # How To use [[mise]] home-directory config to drive [[opencommit]] with [[AWS/Bedrock/Model/Anthropic]] model for Conventional Commits
	- ## Goal
		- One-line command (`mise commit`) that reads *staged* Git changes and writes a Conventional Commit message via Anthropic Claude running on AWS Bedrock.
	- ## Preconditions
		- **mise** ≥ 2025.5 installed and initialised in your shell.
		- AWS CLI v2 configured; role with `bedrock:InvokeModel` in your default profile.
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
				  [tasks.commit]
				  description = "AI-generated Conventional Commit"
				  run = "opencommit --provider anthropic"   # OpenCommit reads staged files
				  env = {                                   # passed only to this task
				    OCO_AI_PROVIDER = "anthropic-bedrock",
				    AWS_REGION      = "us-east-1",
				    OCO_MODEL       = "claude-3-sonnet-20250219-v1:0",
				    # optional if you proxy Bedrock via an OpenAI-compatible endpoint
				    # OPENAI_API_BASE_URL = "https://bedrock-runtime.$AWS_REGION.amazonaws.com/openai/v1"
				  }
				  ~~~
			- Save and exit. `mise` auto-reloads configs on next run.
		- ### 3. (Optional) keep secrets in 1Password
			- Replace literal values with secret references, e.g.  
			  `OCO_MODEL = "op://AI/Bedrock/claude-sonnet-model-id"` – these resolve at runtime when you wrap the task with `op run -- mise commit`. The pattern is identical to other mise examples that embed `ANTHROPIC_API_KEY` secrets inside `env` blocks.
		- ### 4. Commit with a single command
		  1. Stage your work: `git add -A`
		  2. Run: `mise commit --type feat --scope auth`  
		    *OpenCommit* streams the generated message, then executes `git commit -m "<msg>"`.
	- ## Troubleshooting
		- **“Provider not found”** → ensure `OCO_AI_PROVIDER` matches `anthropic-bedrock`.
		- **AWS auth errors** → run `aws sts get-caller-identity` to confirm your Bedrock role is active.
		- **Unexpected commit style** → pass `--emoji false --style conventional` to the `run` line.
	- ## References
		- Template of `env` in task blocks
		- `mise config` and `mise use -g` for editing global configs