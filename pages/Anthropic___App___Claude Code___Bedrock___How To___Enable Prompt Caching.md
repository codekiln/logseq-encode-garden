tags:: [[Diataxis/How To]]

- # How To Enable Prompt Caching for Anthropic Models in AWS Bedrock
	- ## Goal
		- Ensure prompt caching is active for Anthropic Claude models on AWS Bedrock to reduce latency and token costs.
	- ## Preconditions
		- AWS account with Bedrock access and Anthropic Claude models enabled.
		- AWS CLI v2 configured (`aws configure`).
		- (Optional) Claude Code CLI installed and configured.
	- ## Procedure
		- ### 1. Configure Claude Code for Bedrock with caching enabled
			- Set the Bedrock backend:
			  ~~~bash
			  export CLAUDE_CODE_USE_BEDROCK=1
			  ~~~
			- Ensure prompt caching isn't disabled:
			  ~~~bash
			  unset DISABLE_PROMPT_CACHING
			  ~~~
			- (Alternative) Persist in global Claude Code config:
			  ~~~bash
			  claude config set --global env '{"CLAUDE_CODE_USE_BEDROCK":"true"}'
			  ~~~
		- ### 2. Verify prompt caching via AWS CLI
			- Create a `payload.json`:
			  ~~~json
			  {
			   "prompt": "Human: Test for caching.\n\nAssistant:",
			   "cache_control": {"type":"default"},
			   "max_tokens": 10
			  }
			  ~~~
			- Invoke the model and specify an output file (required positional `outfile`):
				- ~~~bash
				  aws bedrock-runtime invoke-model \
				   --model-id us.anthropic.claude-3-7-sonnet-20250219-v1:0 \
				   --body fileb://payload.json \
				   --content-type application/json \
				   --region us-east-1 \
				   --profile bedrock \
				   response.json
				  ~~~
				- **Note:** Use `fileb://` (not `file://`) for the `--body` parameter to avoid base64 errors.
			- Inspect the response for caching metrics:
			  ~~~bash
			  jq '.CacheReadInputTokens, .CacheWriteInputTokens' response.json
			  ~~~
			  Presence of numeric values confirms prompt caching is operational.
		- ### 3. Enable caching in the Bedrock console
			- Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home).
			- In **Playground**, select an Anthropic Claude model.
			- Toggle **Prompt caching** to **On** (default for supported models).
	- ## Troubleshooting
		- *Invalid base64 error* → Use `fileb://` instead of `file://` for the `--body` parameter in your AWS CLI command.
		- *Missing cache fields* → Verify your account's prompt caching entitlement; contact AWS Support if unavailable.
		- *`cache_control` not recognized* → Upgrade AWS CLI/SDK to the latest version that supports cache control.
		- *Console toggle absent* → Confirm your region and console version support prompt caching.
	- ## References
		- [Bedrock & Vertex · Anthropic Documentation](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex)
		- [Prompt caching for faster model inference · Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
		- [AWS Prompt Engineering: A Developer's Guide to CLI Usage](https://paiml.com/blog/2024-11-22-aws-prompt-engineering-guide/)