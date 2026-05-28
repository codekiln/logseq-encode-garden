tags:: [[Claude/Desktop]], [[Q]]
alias:: [[Anthropic/App/Claude Desktop/Q/Is it possible to use AWS Bedrock to power Claude Desktop]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Desktop/How To/Use BYOK with AWS Bedrock]], [[Claude/Code/Bedrock]]
title:: Claude/Desktop/Q/Is it possible to use AWS Bedrock to power Claude Desktop?

- # Is it possible to use [[AWS/Bedrock]] to power [[Claude/Desktop]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer (as of 2026-05-28):** **Yes.** [[Claude/Desktop]] can route **model inference** through **Amazon Bedrock** in your AWS account via **third-party inference** configuration (the same **Cowork / 3P** path used for enterprise Bedrock deployments). This is distinct from the [[Claude/Code]] CLI’s `CLAUDE_CODE_USE_BEDROCK=1` env-var flow, but serves the same goal: use Bedrock instead of Anthropic-hosted inference endpoints.
			- **How to enable (evaluation / single machine):**
				- Update [[Claude/Desktop]] to a current build.
				- **Help → Troubleshooting → Enable Developer Mode**
				- **Developer → Configure Third-Party Inference**
				- In **Connection**, set inference provider to **Bedrock** and supply region plus a credential source (Bedrock API key / bearer token, named AWS profile, or AWS SSO fields). See [Deploy Cowork on 3P with Amazon Bedrock](https://claude.com/docs/cowork/3p/bedrock) and the [configuration reference](https://claude.com/docs/cowork/3p/configuration#bedrock).
				- Apply locally and relaunch. A garden note at [[Claude/Desktop/How To/Use BYOK with AWS Bedrock]] records a successful basic-inference setup (telemetry off, no MCP) using the [3P installation guide](https://claude.com/docs/cowork/3p/installation).
			- **Enterprise rollout:** IT can push the same keys (`inferenceBedrockRegion`, `inferenceBedrockProfile`, `inferenceBedrockBearerToken`, SSO fields, `inferenceModels`, optional gateway URL) via MDM (Jamf, Intune, Group Policy). AWS describes **Claude Cowork in Amazon Bedrock** as inference in **your** account/regions with optional LLM gateway routing ([AWS ML blog, Apr 2026](https://aws.amazon.com/blogs/machine-learning/from-developer-desks-to-the-whole-organization-running-claude-cowork-in-amazon-bedrock/)).
			- **What Bedrock covers vs. not:**
				- **Through Bedrock:** model calls to `bedrock-runtime` in configured regions; billing/audit via AWS (IAM, CloudTrail, VPC endpoints as you design).
				- **Still Anthropic-side or not Bedrock-backed today:** some product surfaces called out in AWS/Anthropic 3P docs as **not** available through Bedrock inference (e.g. certain hosted capabilities, depending on release). MCP connectors can still reach endpoints **you** approve; aggregate telemetry to Anthropic can be reduced/disabled per 3P policy docs.
				- **Compare [[Claude/Code]]:** CLI uses env vars such as `CLAUDE_CODE_USE_BEDROCK` and Bedrock auth refresh settings ([[Claude/Code/Bedrock]]). Desktop uses the in-app **3P inference** JSON/managed config instead.
			- **Prerequisites:** Bedrock model access in the chosen region (`bedrock:InvokeModel`, streaming invoke as needed), valid inference profile IDs in `inferenceModels` for profile/SSO auth, and a Desktop build that includes 3P Bedrock (feature landed in 2026; tracked publicly from [anthropics/claude-code#32668](https://github.com/anthropics/claude-code/issues/32668)).
