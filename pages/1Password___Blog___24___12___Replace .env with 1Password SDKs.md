created-by:: [[Person/Phil Johnston]]
date-created:: [[2024/12]]
month-created:: [[2024/12]]

- # [How to Replace .env Files with 1Password | 1Password](https://blog.1password.com/env-file-migration-secure-programming-best-practices/)
	- ## [[My Notes]]
	  id:: 67dbde70-e7cb-4b5a-a5e6-a15a761a4ccb
		- how to migrate from [[EnvVar/.env]] files to 1Password's secure tooling
		- 1 - how to use [[op/run]] and a [[1Password Shared Vault]] to share secrets with other members on the dev team and inject them in to the [[EnvVar/.env]] file
		- 2 - how a remotely running automated script can use a [[1Password Service Account]] and the [[1Password/Dev/SDK/python]] to access secrets
		- **comments** - after this article, I have a better sense of how 1Password aims to cover the whole dev lifecycle.
			- I have an active #Question about the trade-offs of using this vs or with cloud-focused tools like [[HashiCorp/Vault]] or [[AWS/Secrets Manager]]. Duplication of secrets isn't fun, but convincing #DevOps to to use a tool that's convenient for development instead of [[HashiCorp Vault]] or an AWS-specific tool sounds even less fun. Maybe someone has made an integration ... ?
			- This article doesn't mention [[1Password/Dev/Connect Server]], which is the next level up from using a [[1Password Service Account]], and offers low latency and self-managed rate limits at the expense of self-hosting, etc. See [[1Password/Dev/Doc/secrets-automation/Overview/Comparison]]
	- ## Migration Steps
		- ### Install [[VSCode/Extension/1Password]]
			- Select a secret in [[EnvVar/.env]] file and use [[VSCode/Extension/1Password/Command/Save in 1Password]] [[VSCode/Command]] to swap it for a secret reference
			  id:: 67dbdeb9-817b-4dac-8674-649b1cba9d67
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
			- Plugin automatically converts secrets to references
		- ### Step 2: Vault Setup
			- Create dedicated vault for application secrets
			- Example vault name: "ENV_Demo_Secrets"
			- next, they move the secret reference to use `ENV_DEMO_Secrets`
				- ![ENV_Demo_SECRETS vault](https://blog.1password.com/posts/2024/env-file-migration-secure-programming-best-practices/app_secret_token_2.png)
			- Share vault access with team members
			- Supports multiple environments (dev/staging/prod)
		- ### Step 3: [[1Password/Dev/SDK]] Implementation
			- Use 1Password SDKs for **cloud-based secret access**
			- > For this step, let’s **assume you’re running a remote automated job** that **kicks off a Python script**. **Due to hosting limitations** you are **unable to install the 1Password CLI**. The desktop client does not allow programmatic access to secrets. In this scenario, your **only option is to use the 1Password SDKs** to access your application secrets.
			- #### When to use which [[1Password]] Tool
				- [[1Password/Desktop]] - intended to be used as a desktop client
				- [[OP]] - Intended to be run from command line to inject secrets into your environment (may be limited due to hosting configuration).
				- [[1Password SDKs]] - Intended for direct secret access from within applications and scripts.
					- [[My Notes]]
						- It's still unclear to me whether 1P is advising when to use `op` vs `sdk` for devs **locally**. It sounds like they are saying that the SDKs are a last resort for remote scenarios. If I've instrumented my application to use .env files and [[1Password/Dev/CLI/Secret Reference]]s
			- Implementation steps:
				- 1. Create [[1Password Service Account]] token
					- See also [[1Password/YouTube/23/11/Getting started with 1Password Service Accounts]]
				- 2. Configure `OP_SERVICE_ACCOUNT_TOKEN`
				- 3. Update application code
			- Example Python remote script using [[1Password Service Account]]
			  id:: 67dbdeb9-75a2-4113-9d2c-4a01bdb43c5f
				- ~~~python
				  import asyncio
				  import os
				  from onepassword import Client
				  
				  async def main():
				    # You still need to load your Service Account Token from the OS, 
				    # but let's do it without an additional package.  
				    token = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")
				    client = await Client.authenticate(auth=token, 
				                                     integration_name="DevRel Demo",
				                                     integration_version="v0.0.1")
				    
				    app_name = await client.secrets.resolve("op://ENV_Demo_Secrets/Demo App Name/text")
				    app_secret_token = await client.secrets.resolve("op://ENV_Demo_Secrets/Blog 1 ENV App_Secret_Token/Section_ty4kl2xveagt5wxcz4yzfzloia/token")
				  ~~~
				- [[My Note]] *If we've instrumented this so it can run as a remote job and use a [[1Password Service Account]], I think the assumption that locally, I'll then use [[1Password/Dev/CLI]] `op` to get a [[1Password/Dev/CLI/Secret Reference]] to load the `OP_SERVICE_ACCOUNT_TOKEN` ... is that right?*
		- ### Step 4: Key Rotation
			- Optional but recommended step
			- Edit secrets directly in 1Password
			- Changes automatically reflected on application restart
	-