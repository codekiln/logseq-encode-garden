# [Claude Code on Amazon Bedrock - Claude Docs](https://docs.claude.com/en/docs/claude-code/amazon-bedrock)
	- #### Advanced credential configuration
		- Claude Code supports automatic credential refresh for AWS SSO and corporate identity providers. Add these settings to your Claude Code settings file (see [Settings](https://docs.claude.com/en/docs/claude-code/settings) for file locations).When Claude Code detects that your AWS credentials are expired (either locally based on their timestamp or when Bedrock returns a credential error), it will automatically run your configured `awsAuthRefresh` and/or `awsCredentialExport` commands to obtain new credentials before retrying the request.##### Example configuration
			- ```
			  {
			  "awsAuthRefresh": "aws sso login --profile myprofile",
			  "env": {
			    "AWS_PROFILE": "myprofile"
			  }
			  }
			  ```
	- ##### Configuration settings explained
		- **`awsAuthRefresh`**: Use this for commands that modify the `.aws` directory (e.g., updating credentials, SSO cache, or config files). Output is shown to the user (but user input is not supported), making it suitable for browser-based authentication flows where the CLI displays a code to enter in the browser.**`awsCredentialExport`**: Only use this if you cannot modify `.aws` and must directly return credentials. Output is captured silently (not shown to the user). The command must output JSON in this format:
			- ```
			  {
			  "Credentials": {
			    "AccessKeyId": "value",
			    "SecretAccessKey": "value",
			    "SessionToken": "value"
			  }
			  }
			  ```