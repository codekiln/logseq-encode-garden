tags:: [[Claude Code]], [[Mise]], [[AWS/Bedrock]], [[Okta]], [[Diataxis/How To]]

- # How To Bootstrap [[Claude Code]] with [[mise]] + [[uv]] -Powered #Okta [[AWS/IAM/Role]] Assumption
	- ## Overview
		- Pin Node LTS, Claude Code, **aws_okta_keyman**, and UV in **mise**; add a `claude` task whose scoped env-vars point the CLI at Bedrock. `aws_okta_keyman` fetches STS creds (installed via mise’s Python/UV pipeline), and `AWS_PROFILE` makes Claude pick them up automatically—no extra role-switch inside the REPL.
	- ## Time Estimate
		- 10 minutes
	- ## Prerequisites
		- [[mise]] v2024.10+ on `PATH`
		- Okta-backed IAM role with `bedrock:InvokeModel`
		- AWS CLI v2
		- Bedrock access to *Claude 3.7 Sonnet* in your target Region
	- ## Steps
		- ### 1  Edit the global mise config
			- Append to *~/.config/mise/config.toml* (keep `[settings] experimental = true`):
				- ~~~toml
				  [tools]                                   # language & CLI pinning
				  node = "lts"
				  uv   = "latest"                           # UV installer/runtime
				  "npm:@anthropic-ai/claude-code" = "latest"
				  "pipx:aws-okta-keyman"        = "latest"  # pipx uses UV under the hood
				  
				  [tasks.bedrock-login]                     # STS helper (optional)
				  run = "uvx aws_okta_keyman --role arn:aws:iam::<acct>:role/BedrockInvokeRole --profile bedrock"
				  
				  [tasks.claude]                            # main entry point
				  run = "claude $@"                         # forward args
				  
				  [tasks.claude.env]                        # vars ONLY for Claude
				  CLAUDE_CODE_USE_BEDROCK    = "true"
				  AWS_PROFILE                = "bedrock"
				  AWS_REGION                 = "us-east-1"
				  ANTHROPIC_MODEL            = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
				  ANTHROPIC_SMALL_FAST_MODEL = "us.anthropic.claude-3-5-haiku-20241022-v1:0"
				  ~~~
			- **Why UV not pipx?** With `experimental = true`, mise installs Python packages using **UV** and exposes them via **`uvx`**—fast, isolated, and no extra venvs.
		- ### 2  Install & reshim the toolchain
		  ~~~bash
		  mise install
		  mise reshim
		  mise run claude -- --version    # sanity-check shim
		  ~~~
		- ### 3  Obtain STS credentials
		  ~~~bash
		  mise run bedrock-login          # runs uvx aws_okta_keyman …
		  ~~~
			- Credentials land in *~/.aws/credentials* under `[bedrock]`.
		- ### 4  Launch Claude Code
		  ~~~bash
		  cd /path/to/monorepo
		  mise run claude                 # or: mise r claude
		  /init                           # one-time scan
		  /status                         # should show “provider: Bedrock”
		  ~~~
		- ### 5  Verify & tidy
		  ~~~bash
		  aws sts get-caller-identity --profile bedrock
		  aws bedrock list-foundation-models --region us-east-1 | grep claude
		  claude config add ignorePatterns "libs/legacy/**"
		  /cost
		  ~~~
	- ## Troubleshooting
		- **403 “Model access denied”** → enable *Claude 3* in the Bedrock console for `us-east-1`.
		- **TOML parse error** → ensure `[tasks.claude.env]` is a nested table, not inline `{…}`.
		- **Expired creds** → rerun `mise r bedrock-login`; STS tokens last ≈1 h.
	- ## Related
		- A less opinionated guide is available at [[Anthropic/App/Claude Code/How To/Get Started with AWS Bedrock]]
		- Claude Code Bedrock settings docs