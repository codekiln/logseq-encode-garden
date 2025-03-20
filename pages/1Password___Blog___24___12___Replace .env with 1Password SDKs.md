created-by:: [[Person/Phil Johnston]]
date-created:: [[2024/12]]
month-created:: [[2024/12]]

- # [How to Replace .env Files with 1Password | 1Password](https://blog.1password.com/env-file-migration-secure-programming-best-practices/)
	- ## Summary
		- Article by Phil Johnston explains how to migrate from [[EnvVar/.env]] files to 1Password's secure tooling
		- Focus on using [[op]] CLI and SDKs for secure secret management
	- ## When to use which [[1Password]] Tool
		- [[My Notes]]
			- Unclear on when 1P is advising to use `op` vs `sdk` for devs locally
		- [[1Password/Desktop]] - intended to be used as a desktop client
		- [[OP]] - Intended to be run from command line to inject secrets into your environment (may be limited due to hosting configuration).
		- [[1Password SDKs]] - Intended for secret access from within applications and scripts.
	- ## Migration Steps
		- ### Install [[VSCode/Extension/1Password]]
			- Select a secret in [[EnvVar/.env]] file and use [[VSCode/Extension/1Password/Command/Save in 1Password]] [[VSCode/Command]] to swap it for a secret reference
				- Before
					- ```bash
					  # This is an example .env file that we will use to migrate  
					  # from hosting the actual configurations of an environment  
					  # over to a 1Password-managed environment. 
					  
					  # Environment Configuration  
					  # options include  
					  #         - development  
					  #         - staging  
					  #         - production  
					  APP_ENV=development
					  
					  # Application Configuration  
					  APP_NAME=OP SDJ ENV Demo Application
					  
					  APP_SECRET_TOKEN=QAZWSXEDCrfvtgbyhn 
					  ```
				- highlight line 15, then use VSCode `Save in 1Password`
				- After, it's replaced with [[1Password/Dev/CLI/Secret Reference]]
					- first, they move it to a generic vault named "Vault"
						- ![moving it to Vault](https://blog.1password.com/posts/2024/env-file-migration-secure-programming-best-practices/app_secret_token.png)
					- next, they move it to `ENV_DEMO_Secrets`
						- ![ENV_Demo_SECRETS vault](https://blog.1password.com/posts/2024/env-file-migration-secure-programming-best-practices/app_secret_token_2.png)
			- Plugin automatically converts secrets to references
		- ### Step 2: Vault Setup
			- Create dedicated vault for application secrets
			- Example vault name: "ENV_Demo_Secrets"
			- Share vault access with team members
			- Supports multiple environments (dev/staging/prod)
		- ### Step 3: SDK Implementation
			- Use 1Password SDKs for cloud-based secret access
			- Tool comparison:
				- Desktop app: Local client usage
				- [[op]]: CLI-based environment injection
				- SDKs: Direct secret access in applications
			- Implementation steps:
				- 1. Create Service Account token
					- See also [[1Password/YouTube/23/11/Getting started with 1Password Service Accounts]]
				- 2. Configure OP_SERVICE_ACCOUNT_TOKEN
				- 3. Update application code
			- Example Python implementation:
				- ~~~python
				  import asyncio
				  import os
				  from onepassword import Client
				  
				  async def main():
				    token = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")
				    client = await Client.authenticate(auth=token, 
				                                     integration_name="DevRel Demo",
				                                     integration_version="v0.0.1")
				    
				    app_name = await client.secrets.resolve("op://ENV_Demo_Secrets/Demo App Name/text")
				    app_secret_token = await client.secrets.resolve("op://ENV_Demo_Secrets/Blog 1 ENV App_Secret_Token/Section_ty4kl2xveagt5wxcz4yzfzloia/token")
				  ~~~
		- ### Step 4: Key Rotation
			- Optional but recommended step
			- Edit secrets directly in 1Password
			- Changes automatically reflected on application restart