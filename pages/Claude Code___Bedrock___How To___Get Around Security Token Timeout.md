tags:: [[Diataxis/How To]], [[Claude Code]], [[AWS/Bedrock]]
alias:: [[Anthropic/App/Claude Code/Bedrock/How To/Get Around Security Token Timeout]]

- # How To Handle Security Token Expiration Errors with Claude Code and AWS Bedrock
	- ## Problem
		- When using [[Claude Code]] with [[AWS/Bedrock]], you may encounter the error:
			- ```
			  API Error: The security token included in the request is expired
			  ```
		- This occurs when AWS credentials (STS tokens, SSO sessions, etc.) have expired and Claude Code needs to refresh them.
	- ## Expected Behavior
		- According to the [official documentation](https://code.claude.com/docs/en/amazon-bedrock), Claude Code should automatically detect expired credentials and run your configured `awsAuthRefresh` command before retrying the request.
		- Detection happens in two ways:
			- **Local detection**: Based on credential timestamp in `~/.aws/credentials` or SSO cache
			- **Remote detection**: When Bedrock returns a credential error (like the expired token error)
	- ## Configuration
		- ### Basic Setup
			- Add `awsAuthRefresh` to your Claude Code settings file (`~/.claude/settings.json`):
				- ```json
				  {
				    "awsAuthRefresh": "aws sso login --profile myprofile",
				    "env": {
				      "AWS_PROFILE": "myprofile",
				    }
				  }
				  ```
		- ### Command Types
			- **`awsAuthRefresh`**: For commands that modify the `.aws` directory (credentials, SSO cache, config files)
				- Output is shown to the user
				- User input is NOT supported (see [GitHub Issue #11264](https://github.com/anthropics/claude-code/issues/11264) for feature request to support interactive authentication)
				- Suitable for browser-based authentication flows
				- **Limitation**: Interactive authentication tools (like `gimme-aws-creds` with password/MFA prompts) cannot be used with `awsAuthRefresh` currently
			- **`awsCredentialExport`**: For commands that output credentials directly as JSON
				- Output is captured silently (not shown)
				- Must output JSON in this format:
					- ```json
					  {
					    "Credentials": {
					      "AccessKeyId": "value",
					      "SecretAccessKey": "value",
					      "SessionToken": "value"
					    }
					  }
					  ```
				- **Example Commands**:
					- **Using AWS STS assume-role with jq** (most common):
						- ```json
						  "awsCredentialExport": "aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name mysession | jq '{Credentials: .Credentials | {AccessKeyId, SecretAccessKey, SessionToken}}'"
						  ```
						- Reference: [AWS CLI Command Reference: assume-role](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html)
					- **Using AWS STS get-session-token with jq**:
						- ```json
						  "awsCredentialExport": "aws sts get-session-token | jq '{Credentials: .Credentials | {AccessKeyId, SecretAccessKey, SessionToken}}'"
						  ```
						- Reference: [AWS CLI Command Reference: get-session-token](https://docs.aws.amazon.com/cli/latest/reference/sts/get-session-token.html)
					- **Using a custom script**:
						- ```json
						  "awsCredentialExport": "/path/to/generate_aws_grant.sh"
						  ```
						- The script should output the JSON format shown above to stdout
						- Reference: [Claude Code Settings Documentation](https://code.claude.com/docs/en/settings) - See `awsCredentialExport` setting
					- **Using AWS CLI export-credentials** (if your AWS CLI version supports it):
						- ```json
						  "awsCredentialExport": "aws configure export-credentials --profile myprofile --format json | jq '{Credentials: {AccessKeyId: .AccessKeyId, SecretAccessKey: .SecretAccessKey, SessionToken: .SessionToken}}'"
						  ```
						- Reference: [AWS CLI Command Reference: configure export-credentials](https://docs.aws.amazon.com/cli/latest/reference/configure/export-credentials.html)
					- **Using a wrapper script with environment variables**:
						- ```json
						  "awsCredentialExport": "bash -c 'aws sts assume-role --role-arn $AWS_ROLE_ARN --role-session-name $SESSION_NAME | jq \"{Credentials: .Credentials | {AccessKeyId, SecretAccessKey, SessionToken}}\"'"
						  ```
						- References:
							- [AWS CLI Command Reference: assume-role](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html)
							- [jq Manual](https://stedolan.github.io/jq/manual/) - For [[jq]] filter syntax
				- **Important Notes**:
					- The command must output **only** valid JSON to stdout (no error messages or other output)
					- Use `jq` to filter AWS STS output, as it includes additional fields (`Expiration`, `AssumedRoleUser`, etc.) that Claude Code doesn't need
					- Ensure `jq` is available in Claude Code's PATH if your command uses it
					- For commands with pipes, you may need to wrap them in `bash -c` or `sh -c`
					- Test your command manually first to ensure it outputs the correct JSON format
	- ## Troubleshooting: When Automatic Refresh Doesn't Work
		- ### Issue: Command Not Triggering
			- If you see the expired token error but no indication that `awsAuthRefresh` ran:
				- **Check command path**: Ensure your command is in your PATH when Claude Code runs
					- Claude Code may not have access to the same PATH as your shell
					- Try using the full path: `"/usr/local/bin/aws sso login --profile myprofile"`
				- **Check command syntax**: Verify the command works when run manually
					- ```bash
					  aws sso login --profile myprofile
					  ```
				- **Check permissions**: Ensure Claude Code has permission to execute the command
					- Check your `permissions` settings in `settings.json`
					- May need to add: `"Bash(aws:*)"` to allowed commands
			- **Workaround**: Manually refresh credentials before using Claude Code
				- ```bash
				  aws sso login --profile myprofile
				  ```
				- Then retry your Claude Code request
		- ### Issue: Credentials Refreshed But Not Used (Known Bug)
			- **Symptom**: `awsAuthRefresh` runs successfully and credentials are updated in `~/.aws/credentials`, but Claude Code still fails with expired token errors
			- **Cause**: This is a [known bug in Claude Code](https://github.com/anthropics/claude-code/issues/3823) where the refreshed credentials aren't always picked up after `awsAuthRefresh` completes
			- **Workaround**: Exit and resume Claude Code to force it to reload credentials
				- Exit Claude Code: `Ctrl+C` or `exit`
				- Resume with: `claude -r` (resume last session)
				- This forces Claude Code to reload credentials from `~/.aws/credentials`
			- **Alternative Workaround**: Use `awsCredentialExport` instead of `awsAuthRefresh`
				- `awsCredentialExport` directly provides credentials to Claude Code, bypassing the credential file reload issue
				- See the `awsCredentialExport` examples above
			- **Note**: The issue tracker includes a request for a `/refresh-credential` command to manually trigger credential reload without exiting
		- ### Issue: Command Not Found
			- If your refresh command isn't available in Claude Code's environment:
				- **Option 1**: Use full path to the command
					- Find command location: `which aws` or `command -v aws`
					- Use full path in `awsAuthRefresh`: `"/usr/local/bin/aws sso login --profile myprofile"`
				- **Option 2**: Use direct script path
					- If you have a custom refresh script, reference it directly:
						- ```json
						  "awsAuthRefresh": "/path/to/refresh_credentials.sh"
						  ```
				- **Option 3**: Use `awsCredentialExport` with a wrapper script
					- Create a script that outputs credentials in the required JSON format
					- See examples in the `awsCredentialExport` section above
		- ### Issue: Interactive Commands
			- If your refresh command requires user interaction (like password entry, MFA approval, Touch ID):
				- Claude Code's `awsAuthRefresh` shows output but doesn't support user input
				- This may cause the command to hang or fail
				- **Current Workaround**: Use `awsCredentialExport` instead, or ensure your command can run non-interactively
				- **Future Enhancement**: [GitHub Issue #11264](https://github.com/anthropics/claude-code/issues/11264) requests support for interactive `awsAuthRefresh` to enable enterprise authentication flows (gimme-aws-creds, saml2aws, etc.)
				- **Alternative**: For now, manually refresh credentials in a separate terminal before using Claude Code
		- ### Issue: Environment Variables Not Available
			- If your refresh command needs specific environment variables:
				- Add them to the `env` section of your settings.json
			- Example:
				- ```json
				  {
				    "awsAuthRefresh": "aws sso login --profile myprofile",
				    "env": {
				      "AWS_PROFILE": "myprofile",
				      "OP_SESSION_myorg": "your-session-token",
				      "PATH": "/custom/path:$PATH"
				    }
				  }
				  ```
	- ## Manual Refresh Workflow
		- When automatic refresh fails, use this workflow:
		  1. **Check current credentials**:
			- ```bash
			  aws sts get-caller-identity --profile myprofile
			  ```
			  2. **Refresh credentials**:
			- ```bash
			  aws sso login --profile myprofile
			  ```
			  3. **Verify new credentials**:
			- ```bash
			  aws sts get-caller-identity --profile myprofile
			  ```
			  4. **Retry Claude Code request**
	- ## Related Pages
		- [[Claude Code/Bedrock]] - Main Bedrock integration guide
		- [[mise/Task/How To/invoke aws_okta_keyman from mise with a configuration that references a default AWS account]] - Example of setting up credential refresh scripts
		- [[Claude Code/Settings]] - Claude Code settings documentation
	- ## References
		- [Claude Code on Amazon Bedrock - Advanced Credential Configuration](https://code.claude.com/docs/en/amazon-bedrock#advanced-credential-configuration)
		- [Claude Code Settings Documentation](https://code.claude.com/docs/en/settings)
		- [GitHub Issue #3823: CC not taking the updated credentials with awsAuthRefresh](https://github.com/anthropics/claude-code/issues/3823) - Known bug where refreshed credentials aren't always used
		- [GitHub Issue #11264: Interactive awsAuthRefresh](https://github.com/anthropics/claude-code/issues/11264) - Feature request to support interactive authentication flows (password/MFA prompts) within Claude Code