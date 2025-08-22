tags:: [[Diataxis/How To]]

- # How to get started with [[Claude Code]] using [[AWS/Bedrock/Model/Anthropic]]
	- ## Problem
		- You, as a software engineer, want to use **Claude Code** with **Anthropic** models served by your enterprise's **AWS Bedrock** access. You are working in an organization where your [[DevOps]] team has already configured your AWS user to be able to utilize AWS Bedrock, as long as you use [[Okta]] to conduct [[MFA]] and then subsequently assume an [[AWS/IAM/Role]].
		- ### After this guide you should be able to:
			- 1 - start [[Claude Code]] and demonstrate that it is able to use your organization's AWS Bedrock connection to utilize [[Anthropic/Model]]s such as [[Claude 3.5 Sonnet]] and [[Claude 3.7 Sonnet]] and [[Anthropic/Model/Claude/3.5/Haiku]].
	- ## Prerequisites
		- ### Your Responsibilities and Prerequisites
			- #### Follow [[AWS/Okta Keyman/How To/Install and Configure for Bedrock]]
				- The above how-to guide is a prerequisite for this one.
			- **Before** starting this how-to guide, you should **already** have these things **available** as [[CLI commands]]:
				- [[NodeJS]] 18+ and [[npm]]
				- [[aws_okta_keyman]] (which was required for the how-to guide above)
			- You should also have a git repository already created which has a project you want to work on with claude code
	- ## Steps
		- ### 1. Install tools - [[Claude Code]]
			- `npm install -g @anthropic-ai/claude-code`
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