# [Load secrets into scripts | 1Password Developer](https://developer.1password.com/docs/cli/secrets-scripts/)
	- You can use the following methods to load secrets into scripts, separately or in combination:
		- [[1Password/Dev/op/run]]
			- [Use `op run` to load secrets into the environment.](https://developer.1password.com/docs/cli/secrets-scripts/#option-1-use-op-run-to-load-secrets-into-the-environment)
		- [[1Password/Dev/op/read]]
			- [Use `op read` to read secrets.](https://developer.1password.com/docs/cli/secrets-scripts/#option-2-use-op-read-to-read-secrets)
		- [[1Password/Dev/op/inject]]
			- [Use `op inject` to load secrets into a config file.](https://developer.1password.com/docs/cli/secrets-scripts/#option-3-use-op-inject-to-load-secrets-into-a-config-file)
		- [[1Password/Dev/op/plugin/run]]
			- [Use `op plugin run` to load secrets using a shell plugin.](https://developer.1password.com/docs/cli/secrets-scripts/#option-4-use-op-plugin-run-to-load-secrets-using-a-shell-plugin)
	- ## 1Password #Tip recommends using [[1Password Service Account]]s instead of the above methods, but that's only realistic if you're explicitly enabled to do that by an admin on the business tier
		- > We recommend using [1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) to follow the [principle of least privilege](https://developer.1password.com/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose. Service accounts are also useful if your personal account has SSO or MFA requirements.
			- [[My Note]] - #Important - while this page recommends using service accounts over using [[1Password/Dev/op]], only some people can use them
			  id:: 67dfdb5e-9b4f-424a-976d-7bec032c969f
				- {{embed ((67dfdd64-6d97-43dd-96f6-ff28165bafb8))}}
	- ## [Option 1](https://developer.1password.com/docs/cli/secrets-scripts/#option-1-use-op-run-to-load-secrets-into-the-environment) - use [[1Password/Dev/op/run]] to load #Secrets into [[EnvVars]]
		- ### #Example
			- Given a [[.env File]]
				- ```bash
				  AWS_SECRET_ACCESS_KEY=op://prod/aws/secret-key
				  AWS_ACCESS_KEY_ID=op://prod/aws/access-key
				  ```
			- `op run --env-file yourscript.env -- yourscript.sh`
			- This might work well with [[mise/Task]] definitions
	- ## [Option 2](https://developer.1password.com/docs/cli/secrets-scripts/#option-2-use-op-read-to-read-secrets) - use [[1Password/Dev/op/read]] to read secrets in a script
		- ### [[My Notes]]
			- **Not as useful**, because it prevents the application from being used in contexts that don't use one password. Once you have a script that references `op` inline, every person or environment running that script must use `op`. Even so, there may be some use cases.
		- ### Directly in script
			- ##### #Example
				- ```bash
				  #!/bin/bash
				  
				  docker login -u $(op read op://prod/docker/username) -p $(op read op://prod/docker/password)
				  ```
		- ### With environment variables
			- ##### #Example
				- ```bash
				  #!/bin/bash
				  
				  export AWS_SECRET_ACCESS_KEY=$(op read op://prod/aws/secret-key)
				  export AWS_ACCESS_KEY_ID=$(op read op://prod/aws/access-key-id)
				  aws sts get-caller-identity
				  ```
	- ## [Option 3](https://developer.1password.com/docs/cli/secrets-scripts/#option-3-use-op-inject-to-load-secrets-into-a-config-file) - use [[1Password/Dev/op/inject]] to [load secrets into a config file](https://developer.1password.com/docs/cli/secrets-scripts/#option-3-use-op-inject-to-load-secrets-into-a-config-file)
		- If your script uses a configuration file, you can [[Template]] the config file with [[1Password Secret References]], then use [`op inject`](https://developer.1password.com/docs/cli/reference/commands/inject/) to pass the config file with the resolved secrets to your script at runtime.
		- This allows you to check config files into source control and keep them in sync throughout developer workstations, CI, and production servers. And you can include template variables within the secret references to [load different sets of secrets for different environments](https://developer.1password.com/docs/cli/secrets-config-files/#step-3-differentiate-between-environments).
		- [Learn how to load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/).
		- [[My Notes]] on option 3
			- This uses a specific [[Template]] sytax reminiscent of [[Jinja]] - see [[1Password/Dev/CLI/Ref/Concept/Template Syntax]]
				- {{embed ((67dfea45-d135-4607-9190-07c6918ce936))}}
			- of course, now you have the secret sitting around unencrypted on disk, which goes against [[Security/Quest/Zero Secrets on Disk]]
			- rant about this part
				- > keep them in sync throughout developer workstations, CI, and production servers
				- in practice, it seems like this would likely either involve using [[1Password/Dev/Connect Server]] or [[1Password Service Account]], which isn't applicable to all setups
	- ## [Option 4](https://developer.1password.com/docs/cli/secrets-scripts/#option-4-use-op-plugin-run-to-load-secrets-using-a-shell-plugin) - use [[1Password/Dev/op/plugin/run]] to load secrets using a [[1Password/Dev/CLI/Shell Plugin]]
		- [1Password Shell Plugin](https://developer.1password.com/docs/cli/shell-plugins/)s prompt each user to select their credentials when the script is executed.
		- to authenticate an individual command, wrap the command in [`op plugin run`](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-run).
			- ### #Example - use [[1Password/Dev/CLI/Shell Plugin/AWS]] to provide an [[AWS/EnvVar]] AWS Access Key and Secret Key ID
				- to the  [[AWS/CLI/sts/get-caller-identity]] `sts get-caller-identity` command:
					- ```bash
					  #!/bin/bash
					  
					  op plugin run -- aws sts get-caller-identity
					  ```
		- To use a shell plugin throughout a script, you can include an alias for the tool's executable command at the beginning of the script. For example, in this script, the AWS shell plugin would be used to supply secrets for every `aws` command in the script.
			- ```bash
			  #!/bin/bash
			  
			  alias aws="op plugin run -- aws"
			  aws sts get-caller-identity
			  ```
		- If a shell plugin doesn't exist for the tool you're using, you can [build a new plugin](https://developer.1password.com/docs/cli/shell-plugins/contribute/).
		- [[My Notes]]
			- This might work well with [[mise/Task]] definitions