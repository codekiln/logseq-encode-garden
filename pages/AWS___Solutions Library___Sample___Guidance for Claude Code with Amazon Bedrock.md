- # [Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
	- Repository: [aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
	- This Guidance demonstrates how organizations can implement secure enterprise authentication for [[AWS/Bedrock]] using industry-standard protocols and AWS services.
	- ## Key Features
		- ### [[OIDC]] Identity Provider Integration
			- Seamless authentication through providers like [[Okta]], Azure AD, and Auth0
		- ### Temporary AWS Credentials
			- Eliminates long-lived credentials by providing session-based access to Amazon Bedrock
		- ### Centralized Access Control
			- Manage access through existing identity provider groups and policies
		- ### Comprehensive Audit Logging
			- Full [[AWS/CloudTrail]] integration for compliance and security monitoring
		- ### Optional Usage Monitoring
			- [[AWS/CloudWatch]] dashboards for tracking usage, costs, and performance
	- ## Quick Start Guide
		- ### Prerequisites
			- Set up supported OIDC providers
		- ### Deployment
			- Clone the repository:
				- ~~~bash
				  git clone https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock
				  cd guidance-for-claude-code-with-amazon-bedrock/source
				  ~~~
			- Install dependencies:
				- ~~~bash
				  poetry install
				  ~~~
			- Run interactive setup wizard:
				- ~~~bash
				  poetry run ccwb init
				  ~~~
			- Deploy infrastructure:
				- ~~~bash
				  poetry run ccwb deploy
				  ~~~
			- Create distribution package:
				- ~~~bash
				  poetry run ccwb package --target-platform=all
				  ~~~
			- (Optional) Distribute package via secure URL:
				- ~~~bash
				  poetry run ccwb distribute
				  ~~~
		- ### Testing
			- Test package locally:
				- ~~~bash
				  poetry run ccwb test
				  ~~~
		- ### Cleanup
			- To remove infrastructure resources:
				- ~~~bash
				  poetry run ccwb destroy
				  ~~~
	- ## Related Pages
		- [[Claude Code]]
		- [[Claude Code/Bedrock]]
		- [[AWS/Bedrock]]
		- [[AWS/Bedrock/Model/Anthropic]]
		- [[GitHub/Codespace/Q/Can OIDC Grant Access to AWS Bedrock as in GitHub Actions for Claude Code]]
		- [[Okta]]
		- [[AWS/IAM/Role]]

