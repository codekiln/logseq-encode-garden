tags:: [[Diataxis/How To]]

- # How to Install and Configure [[aws_okta_keyman]] for [[AWS/Bedrock/Model/Anthropic]] access
	- ## Problem
		- You, as a software engineer, want to use **Anthropic** LLM models served by your enterprise's **AWS Bedrock** access. You are working in an organization where your [[DevOps]] team has already configured your AWS user to be able to utilize AWS Bedrock, as long as you use [[Okta]] to conduct [[MFA]] and then subsequently assume an [[AWS/IAM/Role]].
		- After this guide you should be able to:
			- 1 - invoke the [[aws_okta_keyman]] [[CLI/Tool]] to authenticate with AWS via [[Okta]]
			- 2 - test out bedrock access using the AWS CLI
				- 2.1 - list foundation models
				- 2.2 - execute a test query against bedrock
	- ## Prerequisites
		- ### Your DevOps Team's Responsibilities and Prerequisites
			- Set up an Okta-backed IAM role allowing `bedrock:InvokeModel` as well as being able to list models
				- Should include at least Bedrock model access for *Claude 3.7 Sonnet* and *3.5 Haiku* in your region
			- Document developer authentication instructions for Okta with Bedrock, including how the software engineer can find their username, password, and any relevant IAM roles
				- #### Information you need from your DevOps Team
				  id:: 68a875cc-1e1e-4d2a-b945-ec4594240bc3
					- `$OKTA_USERNAME` - your username in okta
					- `$OKTA_ORG` - your Okta domain, for example, `https://myorganization.okta.com`
					- `$AWS_REGION` - your [[AWS/Region]], for example, `us-east-1`
					- `$AWS_ROLE_GATEWAY` - name of the [[AWS/IAM/Role]] that developers should use when logging into [[AWS/Okta Keyman]], for example, `my-developer-gateway-role`
					- `$AWS_ROLE_ASSUMED_ARN` - the [[AWS/IAM/Role]] [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) that should be assumed **after** using Okta to log into `$AWS_ROLE_GATEWAY`, which will give you the ability to use Bedrock, for example, `arn:aws:iam::123456789010:role/my-bedrock-role`
		- ### Your Responsibilities and Prerequisites
			- You should have a linux-like shell available ([[MacOS]] terminal should be fine).
			- **Before** starting this how-to guide, you should **already** have these things **available** as [[CLI commands]] on the path in your linux-like shell:
				- [[Python]] 3.8+ and [[pip]] installed.
				- [[AWS/CLI]] v2 already installed. If you do not have this installed, you will need to follow AWS's instructions for your machine.
				- [[jq]] installed
			- #### Information you need to decide before beginning
				- `$AWS_PROFILE` - typically it's up to you to decide on the name of an [[AWS/Profile]] you will use for Amazon Bedrock requests. The name of AWS profiles is a convenience that you decide and configure on your own computer(s).
	- ## Steps
		- ### 0. Ensure your [[AWS/CLI/config]] has the appropriate [[AWS/Profile]]
			- You should have already configured the AWS CLI.
				- See [Configuration and credential file settings in the AWS CLI - AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for the exhaustive documentation.
			- At the very least, `~/.aws/config` should have something like this:
				- ==IMPORTANT NOTE - you should substitute the dollar sign variables for the actual values below== - if you have literal `$AWS_PROFILE` in your config, it won't work ;)
				- ```toml
				  [default]
				  region = us-east-1
				  output = json
				  
				  [profile $AWS_PROFILE]
				  role_arn = $AWS_ROLE_ASSUMED_ARN
				  source_profile = default
				  region = $AWS_REGION
				  ```
				- Note 2: it may have a lot more stuff in it; for our purposes here we only need a single profile with a single `role_arn` with the permissions to execute AWS Bedrock commands.
		- ### 1. Install [[aws_okta_keyman]]
			- `aws_okta_keyman` lets you use [[Okta]] to authenticate with [[AWS/CLI]]. It produces short-lived `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` for any role your Okta account exposes ([aws_okta_keyman GitHub](https://github.com/nathan-v/aws_okta_keyman)).
			- Install with `pip install --user aws-okta-keyman`; see the [Client Setup instructions here](https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#client-setup) for more info.
			- Test with: `aws_okta_keyman --help`.
			- At this point, if you don't have `aws_okta_keyman` installed, you'll need to debug that before proceeding.
		- ### 2. Configure [[aws_okta_keyman]], which will set up [[AWS/Okta Keyman/config]]
			- See the [section on Interactive Configuration in the aws_okta_keyman's README here](https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#interactive-configuration).
			- Use `$> aws_okta_keyman config` or directly create and edit `~/.config/aws_okta_keyman.yml`
				- You should fill in the values you obtained from your [[DevOps]] team in the prerequisites:
					- {{embed ((68a875cc-1e1e-4d2a-b945-ec4594240bc3))}}
				- This will end up defining [[AWS/Okta Keyman/aws_okta_keyman.yml]], which defaults to `~/.config/aws_okta_keyman.yml`. Using the variables above, a sample [[yaml]] config file would be the following. ==IMPORTANT NOTE - you will need to substitute all dollar sign variables for the real values for your enterprise for this to work==:
					- ```yml
					  console: null
					  duo_factor: null
					  org: $OKTA_ORG
					  password_cache: true
					  region: us-east-1
					  reup: null
					  role: $AWS_ROLE_GATEWAY
					  screen: null
					  username: $OKTA_USERNAME
					  ```
		- ### 3. Export the value of your [[AWS/Profile]] [[AWS/EnvVar]]
			- For the following steps, export the `AWS_PROFILE` [[EnvVar]] value corresponding to the name of the AWS profile you set up in step 0. Substitute `my-aws-profile` for whatever the real value of `$AWS_PROFILE` is in your `~/.aws/config`:
				- `export AWS_PROFILE=my-aws-profile`
		- ### 4. Verify that AWS Okta Keyman and the roles are working by listing the models
			- Then test it out. Note that `aws` command will read from `AWS_PROFILE` [[EnvVar]]:
				- `aws_okta_keyman && aws bedrock list-foundation-models --no-cli-pager | jq -r '.modelSummaries[].modelId' | grep claude`
			- You should see a list of models including `claude`.
				- ```
				  aws_okta_keyman && aws bedrock list-foundation-models --no-cli-pager | jq -r '.modelSummaries[].modelId' | grep claude
				  10:35:13 (INFO) AWS Okta Keyman 🔐 v0.9.0
				  10:35:13 (INFO) Successfully authed REDACTED
				  10:35:14 (INFO) Using account: REDACTED
				  10:35:14 (INFO) Getting SAML Assertion from $OKTA_ORG
				  10:35:14 (WARNING) Application-level MFA present; re-authenticating Okta
				  10:35:15 (WARNING) MFA Requirement Detected - Enter your GOOGLE code here
				  MFA Passcode: 123456
				  10:35:23 (INFO) Getting SAML Assertion from $OKTA_ORG
				  10:35:24 (INFO) Starting AWS session for $AWS_REGION
				  10:35:24 (INFO) Assuming role: $AWS_ROLE_GATEWAY
				  10:35:24 (INFO) Wrote profile "default" to ~/.aws/credentials 💾
				  10:35:24 (INFO) Current time is 2025-08-22 14:35:24.466510
				  10:35:24 (INFO) Session expires at 2025-08-22 15:35:24+00:00 ⏳
				  10:35:24 (INFO) All done! 👍
				  ...
				  anthropic.claude-3-5-sonnet-20241022-v2:0
				  anthropic.claude-3-7-sonnet-20250219-v1:0
				  anthropic.claude-3-5-haiku-20241022-v1:0
				  ...
				  ```
			- If you don't, contact your DevOps team and let them know what you did.
		- ### 4. Verify that Okta will let you execute one of the models
			- You may need to substitute the `--model-id` parameter for one of the ones you had in the list-out above.
			- ```
			  aws bedrock-runtime invoke-model \
			    --model-id us.anthropic.claude-3-5-sonnet-20241022-v2:0 \
			    --body '{
			      "anthropic_version": "bedrock-2023-05-31",
			      "max_tokens": 200,
			      "messages": [
			        {"role": "user", "content": "What is the capital of Georgia?"}
			      ]
			    }' \
			    --cli-binary-format raw-in-base64-out \
			    --no-cli-pager \
			    output.json && jq -r '.content[0].text' output.json
			  
			  ```
			- You should see:
				- ```
				  {
				      "contentType": "application/json"
				  }
				  The capital of Georgia is Atlanta. It is the most populous city in Georgia and serves as the state's economic and cultural center.
				  ```