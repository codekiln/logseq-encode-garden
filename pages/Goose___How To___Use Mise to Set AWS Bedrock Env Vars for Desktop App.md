cgpt-link:: [Diataxis/mise - Goose/How To/Set AWS EnvVars](https://chatgpt.com/c/686fb3e7-e60c-800a-80c8-8c6a3e4bc22a) 
tags:: [[Mise]], [[Diataxis/How To]]

- # How To Launch [[Goose/Desktop]] with an [[AWS/Profile]] Using a [[mise/Task]]
	- ## Goal
		- Launch Goose Desktop with an `AWS_PROFILE` env var set so that Bedrock models are accessible.
	- ## Preconditions
		- Goose Desktop is installed in `/Applications/Goose.app`
		- `AWS_PROFILE` is configured in `~/.aws/config` and credentials are valid
		- Mise is installed and properly configured for task execution
	- ## Procedure
		- ### 1. Define the task in `mise.toml`
			- Add this to your `mise.toml` (project or global):
			- ~~~toml
			  [tasks.goose]
			  env = { AWS_PROFILE = "my-bedrock-profile" }
			  run = "/Applications/Goose.app/Contents/MacOS/Goose"
			  description = "Launch Goose Desktop with AWS_PROFILE set"
			  ~~~
			- Replace `"my-bedrock-profile"` with your actual profile name.
		- ### 2. Run the task
			- From your shell:
			- ~~~bash
			  mise run goose
			  ~~~
			- This will start Goose with the correct AWS environment in scope.
	- ## Troubleshooting
		- If Goose fails to connect to Bedrock:
			- Make sure `aws sts get-caller-identity` works with the same profile.
			- Confirm Goose Desktop is closed before launching via Mise.
			- Check that Goose sees the profile by viewing the "provider" tab.
	- ## References
		- [AWS SDK credential resolution](https://docs.aws.amazon.com/sdkref/latest/guide/creds.html)
		- [Goose provider documentation](https://block.github.io/goose/docs/getting-started/providers/)
		- [[Mise/Task]]