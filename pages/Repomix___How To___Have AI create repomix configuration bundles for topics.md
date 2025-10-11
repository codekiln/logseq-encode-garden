- This morning I used a new technique - I used an [[AI/Coding/Tool]] to update the `bundles.json` based on a query in the repo, e.g.
	- >  configuration called aws-okta-login and put files in it that are related to whether I could replace my usage of `aws_okta_keyman` with `aws sso login`.
- This ended up adding the following to my `bundles.json` for repomix, which I then generated and used in [[ChatGPT]]. This was cool because I essentially used [[CursorAI]]'s vector indexing to quickly integrate with a chatgpt deep research query.
	- ```json
	  "aws-okta-login-001": {
	        "name": "aws-okta-login",
	        "created": "2025-01-27T00:00:00.000Z",
	        "lastUsed": "2025-10-11T10:57:22.731Z",
	        "tags": [],
	        "files": [
	          "pages/AWS___Okta Keyman.md",
	          "pages/AWS___Okta Keyman___How To___Install and Configure for Bedrock.md",
	          "pages/mise___Task___How To___invoke aws_okta_keyman from mise with a configuration that references a default AWS account.md",
	          "pages/Anthropic___App___Claude Code___Bedrock.md",
	          "pages/Anthropic___App___Claude Code___Settings.md",
	          "pages/AWS___Profile.md",
	          "pages/AWS___CLI___config.md",
	          "pages/AWS___CLI.md",
	          "pages/AWS___IAM___How To___Use Temporary Access Keys.md",
	          "pages/Anthropic___App___Claude Code___How To___Bootstrap Claude Code with Mise + UV-Powered Okta Role Assumption.md",
	          "pages/Anthropic___App___Claude Code___How To___Get Started with AWS Bedrock.md",
	          "pages/Anthropic___App___Claude Code___Tutorial___Dev Team Quickstart with Vue and AWS Bedrock.md",
	          "pages/Anthropic___App___Claude Code___Bedrock___How To___Enable Prompt Caching.md",
	          "pages/Goose___How To___Use Mise to Set AWS Bedrock Env Vars for Desktop App.md",
	          "pages/aider___docs___llms___bedrock.md",
	          "pages/AWS___Bedrock___API Key.md",
	          "pages/AWS___Blog___25___05___Introducing Claude 4 in Amazon Bedrock.md",
	          "pages/Person___Han Lee___Blog___25___03___Walkthrough%3A Setting Up Claude Code on Amazon Bedrock.md",
	          "pages/langgraph___Studio___issue___24___11___Dynamic AWS Creds in LangGraph Studio.md",
	          "pages/Okta___GitHub___okta-aws-cli.md",
	          "journals/2025_10_11.md"
	        ]
	      }
	  ```