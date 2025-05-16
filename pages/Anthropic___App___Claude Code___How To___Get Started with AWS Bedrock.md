tags:: [[Diataxis/How To]]

- # How to get started with [[Claude Code]] using [[AWS/Bedrock/Model/Anthropic]]
	- ## Problem
		- Use **Claude Code** with Anthropic models on **AWS Bedrock** while authenticating through an Okta-backed IAM role obtained with **`aws_okta_keyman`**.
	- ## Prerequisites
		- Node 18+ & npm
		- Python 3.8+ and `pip`
		- AWS CLI v2 configured for SSO/Okta federation
		- Bedrock model access for *Claude 3.7 Sonnet* (and optionally *3.5 Haiku*) in your Region
		- An Okta-backed IAM role allowing `bedrock:InvokeModel`
		- Local Git checkout of your monorepo
	- ## Steps
		- ### 1. Install tools
			- ~~~
			  npm install -g @anthropic-ai/claude-code       # Claude Code CLI
			  pip install --user aws-okta-keyman             # Okta → AWS STS helper
			  ~~~
			- `aws_okta_keyman` produces short-lived `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` for any role your Okta account exposes ([aws_okta_keyman GitHub](https://github.com/nathan-v/aws_okta_keyman)).
		- ### 2. Assume the Bedrock-enabled role
			- ~~~
			  aws_okta_keyman --role arn:aws:iam::<acct>:role/BedrockInvokeRole
			  # follow MFA prompts; creds land in ~/.aws/credentials under [default]
			  ~~~
			- *Alternatively*, wrap the entire Claude session:
				- ~~~
				  aws_okta_keyman --command "claude"
				  ~~~
		- ### 3. Verify the temporary credentials
			- ~~~
			  aws sts get-caller-identity
			  aws bedrock list-foundation-models --region us-east-1 | grep claude
			  ~~~
		- ### 4. Tell Claude Code to use Bedrock
			- ~~~
			  export CLAUDE_CODE_USE_BEDROCK=1
			  export AWS_REGION=us-east-1
			  export ANTHROPIC_MODEL=us.anthropic.claude-3-7-sonnet-20250219-v1:0
			  export ANTHROPIC_SMALL_FAST_MODEL=us.anthropic.claude-3-5-haiku-20241022-v1:0
			  ~~~
			- These variables switch the provider and model IDs for the session ([Anthropic Claude Code Bedrock Docs](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex?utm_source=chatgpt.com)).
			- Persist once if you prefer:
				- ~~~
				  claude config set --global env \
				  '{"CLAUDE_CODE_USE_BEDROCK":"true", \
				  "ANTHROPIC_MODEL":"us.anthropic.claude-3-7-sonnet-20250219-v1:0"}'
				  ~~~
		- ### 5. Launch Claude Code in your project
			- ~~~
			  cd /path/to/monorepo
			  claude    # starts the REPL
			  /init     # one-time: generates CLAUDE.md project map
			  /status   # confirms “provider: Bedrock”
			  ~~~
		- ### 6. Optional hygiene
			- ~~~
			  # Ignore large or irrelevant libraries
			  claude config add ignorePatterns "libs/legacy/**"
			  # View token spend
			  /cost
			  ~~~
	- ## Result
		- Claude Code now runs against AWS Bedrock using STS credentials issued by `aws_okta_keyman`; every request is SigV4-signed and billed to your enterprise account.