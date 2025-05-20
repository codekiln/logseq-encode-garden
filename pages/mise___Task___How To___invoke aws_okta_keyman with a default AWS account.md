tags:: [[Diataxis/How To]]

- # How To invoke aws_okta_keyman with a default AWS account using mise
	- ## Goal
		- Use `mise run` to execute `aws_okta_keyman`, automatically setting a specific AWS account as the default to avoid manual account selection.
	- ## Preconditions
		- `mise` is installed and activated in your shell (e.g., Zsh or Bash).
		- `aws_okta_keyman` is installed and configured with your Okta tenant.
		- You have an AWS Okta Keyman profile named `my-account` in your Okta configuration.
		- Your project directory contains a `mise.toml` file.
	- ## Procedure
		- ### 1. Define the AWS account environment variable in `mise.toml`
			- Open or create `mise.toml` at the root of your project.
			- Under the `[env]` section, add:
			  ~~~toml
			  [env]
			  AWS_OKTA_KEYMAN_ACCOUNT = "my-account"
			  ~~~
			- This sets `AWS_OKTA_KEYMAN_ACCOUNT` to your default account.
		- ### 2. Create a `mise` task for invoking `aws_okta_keyman`
			- In the same `mise.toml`, add under `[tasks]`:
			  ~~~toml
			  [tasks]
			  keyman = "aws_okta_keyman --account {{env.AWS_OKTA_KEYMAN_ACCOUNT}}"
			  ~~~
			- This task uses the environment variable to pass the account flag.
		- ### 3. Run the task
			- Execute:
			  ~~~sh
			  mise run keyman
			  ~~~
			- `aws_okta_keyman` will run using the default account specified.
		- ### 4. Verify the default account
			- Check that your AWS CLI environment variable is set:
			  ~~~sh
			  echo $AWS_PROFILE
			  ~~~
			- It should output `my-account`, confirming the default.
	- ## Troubleshooting
		- **Wrong account selected**
			- Ensure `AWS_OKTA_KEYMAN_ACCOUNT` matches the profile name in your Okta configuration.
		- **`aws_okta_keyman` not found**
			- Install it or add its location to your PATH, or manage it via `mise` if supported.
		- **Environment variable not applied**
			- Run `mise config ls` to confirm which `mise.toml` file is active.
	- ## References
		- [Mise configuration environments](https://mise.jdx.dev/configuration/environments.html)
		- [Mise tasks documentation](https://mise.jdx.dev/tasks/)