tags:: [[Report]], [[AI Deep Research]], [[Claude Code]]
alias:: [[Claude Code/EnvVar/CLAUDE_CODE_MAX_OUTPUT_TOKENS/Report/Avoid api error token max on bedrock]]

- # Handling "Claude's Response Exceeded the 4096 Output Token Maximum" in Claude Code via Amazon Bedrock: Causes, Best Practices, and Mitigation Strategies
	- ## Overview
		- The error message:
			- ```
			  API Error: Claude's response exceeded the 4096 output token maximum. To configure this behavior, set the CLAUDE_CODE_MAX_OUTPUT_TOKENS environment variable.
			  ```
		- arises when using Claude Code on Amazon Bedrock, particularly in development environments leveraging Docker/devcontainer setups and interfacing with the Bedrock SDK. This report provides a comprehensive analysis of the factors driving this error, details on configuration and environment variables, mitigation strategies, regional/model nuances, cost/throttling considerations, and monitoring/observability best practices. Actionable configuration templates, code samples, and links to primary documentation and community threads are included.
	- ## Root Causes of Token Overrun Errors
		- ### 1. Interaction Between Agent Behaviors and Token Budgets
			- **Agent Output Patterns:** Claude Code agents, especially when performing complex tasks like file generation or extended multi-step reasoning (e.g., chain-of-thought with tool usage), may produce outputs that exceed the default token output cap.
			- **Default Output Cap:** Bedrock's standard configuration sets a 4096-token output maximum to manage resource consumption and model stability.
			- **Overrun Mechanism:** When the agent's generated response would exceed this threshold, Bedrock rejects the response with the given error, rather than truncating or streaming by default.
		- ### 2. Bedrock and Region/Model-Specific Token Caps
			- **Global Defaults:** As of the latest documentation, the 4096-token output limit applies universally for Claude models accessed via Bedrock, though this may differ per model version or AWS region as new releases occur. Always check the [Bedrock Service Limits][1] for the latest.
			- **Variance:** For newer Claude versions or other supported models in Bedrock, max tokens may be higher or adjustable, but platform-side enforcement remains strict—exceeding results in an immediate API error.
		- ### 3. Configuration Mismatch
			- **Environment Variables vs. SDK Parameters:** Setting the `CLAUDE_CODE_MAX_OUTPUT_TOKENS` environment variable configures the agent's desired output length, but the Bedrock SDK request must also specify a compatible `maxTokens` (naming may differ across SDKs: `maxTokens`, `max_output_tokens`, etc.).
			- **Thinking Budget:** Tools like `MAX_THINKING_TOKENS` or `thinking.budget_tokens` guard extended reasoning steps—if misaligned with output settings, they can cause unexpected budget breaches.
	- ## Best Practices and Configuration Guidelines
		- ### 1. Mapping Environment Variables and SDK Parameters
			- Ensure environment settings flow through to SDK calls:
			- **.env example:**
				- ```
				  CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
				  MAX_THINKING_TOKENS=1024
				  ```
			- **docker-compose snippet:**
				- ```yaml
				  services:
				    claude-code:
				      environment:
				        - CLAUDE_CODE_MAX_OUTPUT_TOKENS=${CLAUDE_CODE_MAX_OUTPUT_TOKENS:-4096}
				        - MAX_THINKING_TOKENS=${MAX_THINKING_TOKENS:-1024}
				        - CLAUDE_CODE_USE_BEDROCK=1
				        - AWS_REGION=us-east-1
				  ```
			- **SDK Alignment:** In your application, explicitly set the `maxTokens` parameter of the Bedrock SDK in line with `CLAUDE_CODE_MAX_OUTPUT_TOKENS`.
				- ```python
				  # Example: Python pseudocode
				  bedrock_client.invoke_model(
				      modelId="anthropic.claude-v2",
				      body={
				          # ... other parameters ...
				          "maxTokens": int(os.environ["CLAUDE_CODE_MAX_OUTPUT_TOKENS"])
				      }
				  )
				  ```
			- **Consistency:** Failure to align these settings can cause the agent to overrun the hard cap.
		- ### 2. Recommended Token Budgets
			- **Default workloads:** Use `4096` tokens for output, `1024` for thinking—per [Anthropic][2] and [AWS][1] guidance.
			- **Heavy workloads (file generation, multi-tool):** Raise `CLAUDE_CODE_MAX_OUTPUT_TOKENS` (e.g., `16384`) and `MAX_THINKING_TOKENS` (e.g., `8192`) for workflows that require it, but monitor throughput and costs closely.
	- ## Mitigation Strategies
		- ### 1. Chunking and Progressive Output
			- **Prompt Chaining:** Instruct the agent to generate output in logical chunks (e.g., "Write Part 1 of N…") or section-wise (per file/module).
			- **Partial Output Consumption:** Use prompt engineering to indicate maximum allowed output, guiding the agent to produce responses fitting the cap.
		- ### 2. Streaming Output
			- **Use Streaming APIs:** Where supported (Bedrock streaming endpoints), consume output as a stream so that partial results can be buffered and the call retried with continuation prompts when the cap is hit. The Bedrock Python SDK and some HTTP endpoints support response streaming [3].
		- ### 3. Programmatic Retries
			- **Error Handling Logic:** Catch the specific token-exceeded exceptions, then automatically retry with a smaller output request or ask for a summary/condensed output if appropriate.
				- ```python
				  try:
				      response = call_claude_code(payload, max_tokens=4096)
				  except ExceededTokenLimitError:
				      # fallback: condensed output
				      payload['system_prompt'] = 'Please summarize the result in under 800 tokens.'
				      response = call_claude_code(payload, max_tokens=800)
				  ```
			- **Context Truncation:** If possible, reduce prompt context size to stay under budget.
		- ### 4. Agent and Prompt Design
			- **System Prompt Constraints:** Add explicit system instructions: "Limit all responses to N tokens or less. Only output the requested files."
	- ## Cost and Throttling Implications
		- **Cost Scaling:** Raising token caps will significantly increase inference cost per call. Each output (and input) token is billable [1].
		- **Throttling/Quotas:** Larger requests may trigger Bedrock burst/budget throttling faster, especially in high-QPS (queries-per-second) scenarios. Use application-level rate limiting and monitor Bedrock quota usage to avoid disruptions [4].
		- **Per-Workflow Tuning:** Avoid setting a high global token cap; instead, provide per-workflow overrides through feature flags or environment config injection for only high-need scenarios.
	- ## Monitoring and Observability
		- **Key Metrics:**
			- Number of requests hitting token cap errors
			- Requested vs. returned tokens per workflow
			- Model version, region, and user/session context for error analysis
			- Cost tracking: tokens generated and effective cost per workflow
		- **Dashboarding:** Implement dashboarding (e.g., with CloudWatch, Datadog, or Prometheus/Grafana) to correlate token overruns with workload patterns.
		- **Alerting:** Set up alerts for high error rates due to token cap breaches and for cost anomalies when increasing token limits.
	- ## Production Configuration Templates
		- ### Minimal: Baseline
			- **.env**
				- ```
				  CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
				  MAX_THINKING_TOKENS=1024
				  ```
			- **docker-compose.yml**
				- ```yaml
				  environment:
				    - CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
				    - MAX_THINKING_TOKENS=1024
				    - CLAUDE_CODE_USE_BEDROCK=1
				    - AWS_REGION=us-east-1
				  ```
		- ### Heavy/Multifile Workload
			- **.env**
				- ```
				  CLAUDE_CODE_MAX_OUTPUT_TOKENS=16384
				  MAX_THINKING_TOKENS=8192
				  ```
			- **SDK parameter:**
				- ```python
				  "maxTokens": 16384
				  ```
	- ## Community and Documentation References
		- **Anthropic Claude Code in Bedrock:** [Claude on Bedrock documentation][2]
		- **AWS Bedrock Service Limits:** [Bedrock Service Quotas][1]
		- **SDK Parameter Docs:** See language-specific SDK (Python example: [Boto3 Bedrock Docs][3])
		- **Community Threads:**
			- [GitHub: Claude output too large error thread][5]
			- [AWS re:Post: Output token cap discussions][6]
			- [Anthropic Discourse: Output limits & mitigation][7]
	- ## Summary of Actionable Recommendations
		- Set a sensible default of 4096 output tokens unless workloads frequently exceed this.
		- Always ensure environment configuration (env vars) and SDK request parameters (`maxTokens`, equivalents) are synchronized.
		- Use explicit system prompts and chunking for large or complex output.
		- Implement programmatic retries and fallback prompts on token cap errors.
		- Monitor request/response sizes, error rates, and costs per workflow.
		- Use higher token caps selectively and observe for cost and throttling issues.
		- Consult primary documentation and community forums for SDK-specific behaviors and updates.
	- ## Sources
		- [1] AWS Bedrock Service Quotas: https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html
		- [2] Anthropic Claude Code via Amazon Bedrock: https://docs.anthropic.com/claude/docs/amazon-bedrock
		- [3] Boto3 AWS SDK for Bedrock - Model Invocation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
		- [4] AWS Bedrock Billing and Quotas FAQ: https://aws.amazon.com/bedrock/faqs/
		- [5] GitHub Issue: Claude output too large (Token Limit Error): https://github.com/anthropics/claude-code/issues/21
		- [6] AWS re:Post Discussion on Output Token Limits: https://repost.aws/questions/QU93whOKytQYOnaCWusbti0w
		- [7] Anthropic Community: Output Token Limit Discussion: https://community.anthropic.com/t/how-to-handle-output-token-limits

