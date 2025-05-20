tags:: [[Diataxis/How To]], [[mise/Tool]], [[AWS/CLI/Tool]]

- # How To invoke [aws_okta_keyman](https://github.com/nathan-v/aws_okta_keyman) with a default [[AWS/IAM/Role]] with [[mise]]
	- ## Goal
		- Use `mise run aok` to execute `aws_okta_keyman`, automatically setting a specific AWS account as the default to avoid manual account selection.
	- ## Preconditions
		- `mise` is installed and activated in your shell (e.g., Zsh or Bash).
		- `aws_okta_keyman` is installed and configured with your Okta tenant.
		- You have an [[AWS/IAM/Role]] named `my-account` in your Okta configuration.
		- Your project directory contains a `mise.toml` file.
	- ## Procedure
		- ### 1. Set up aws_okta_keyman in `mise.toml`
			- Open or create `mise.toml` at the root of your project.
			- Under the `[tools]` section, declare a dependency on aws-okta-keyman:
				- ~~~toml
				  [tools]
				  # pipx uses UV under the hood - run mise install to get these
				  "pipx:aws-okta-keyman"           = "latest"
				  ~~~
		- ### 2. Create a `mise` task for invoking `aws_okta_keyman`
			- In the same `mise.toml`, add under `[tasks]`:
			- ~~~toml
			  [tasks.aok]
			  # pass any arguments to aws_okta_keyman
			  description = "Call aws_okta_keyman"
			  run = "uvx aws_okta_keyman $@"
			  
			  [tasks.aok-config]
			  # replace cursor with the editor of your choice below
			  description = "open aws_okta_keyman config in editor"
			  run = "cursor ~/.config/aws_okta_keyman.yml"
			  ~~~
		- ### 3. Run [[mise/install]] to install aws_okta_keyman
			- `mise install`
		- ### 4. Set up [[AWS/Okta Keyman/aws_okta_keyman.yml]] config file in `~/.config/aws_okta_keyman.yml`
			- **Note**: alternatively, run [[AWS/Okta Keyman/config]] with `mise run aok config` for [interactive configuration](https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#interactive-configuration)
			- In an editor, add
				- ~~~yml
				  # corresponds to `--console` flag, which allows one to log in through the AWS console
				  # (on the web)
				  # https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#aws-console-logins
				  console: null
				  duo_factor: null
				  # default duration is one hour, 
				  # duration: 3600
				  org: https://mycompany.okta.com
				  # https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#keyring-password-cache
				  # uses [jaraco/keyring](https://github.com/jaraco/keyring) 
				  password_cache: true
				  region: null
				  # [reup mode](https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#re-up-mode--automatic-credential-re-generation) 
				  # see the --reup command line option for help - 
				  # this will run the application in a loop, periodically reaching out to okta, 
				  # generating a new SAML assertion, then generating updated AWS credentials
				  reup: true
				  # if you would like an AWS role to be activated upon running AWS Okta Keyman
				  # put the name of that account here
				  role: my-account
				  screen: null
				  username: myAWS_username
				  ~~~
			- `aws_okta_keyman` will run using the default account specified.
	- ## Troubleshooting
		- **`aws_okta_keyman` not found**
			- Install it or add its location to your PATH, or manage it via `mise` if supported.
		- **Environment variable not applied**
			- Run `mise config ls` to confirm which `mise.toml` file is active.
	- ## References
		- [Mise configuration environments](https://mise.jdx.dev/configuration/environments.html)
		- [Mise tasks documentation](https://mise.jdx.dev/tasks/)