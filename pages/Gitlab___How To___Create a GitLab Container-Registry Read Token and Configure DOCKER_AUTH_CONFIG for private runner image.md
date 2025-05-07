- # How To Create a GitLab Container-Registry Read Token and Configure DOCKER_AUTH_CONFIG for Private Runner Image
	- ## Overview
		- This guide shows you how to create a GitLab Project Access Token with read_registry scope, securely capture it, build and export a DOCKER_AUTH_CONFIG JSON blob, and configure your GitLab CI/CD pipeline to use private Docker images with a custom runner.
		- For DevOps engineers or project maintainers who need to pull private images in GitLab CI/CD jobs using the Docker executor.
	- ## Prerequisites
		- Maintainer (or Owner) access to your GitLab project
		- Your project uses the Docker Machine (docker+machine) or Docker executor
		- CI_REGISTRY and CI_REGISTRY_USER are set (GitLab provides these automatically)
	- ## Steps
		- 1. Create a Project Access Token
			- Navigate to **Your Project ▸ Settings ▸ Access Tokens**
			- Name your token, e.g. `registry-read-token`
			- Under **Scopes**, check **read_registry**
			- Click **Create project access token**
			- **Copy** the resulting token value and store it securely (you'll only see it once)
		- 2. Securely Read the Token in Zsh
			- Open a terminal on your local machine (or CI runner) and run:
				- ~~~zsh
				read -sr "REGISTRY_TOKEN?Enter your registry read token: "
				echo
				# -s hides input
				# -r prevents backslashes from being interpreted
				# The trailing echo prints a newline
				~~~
		- 3. Build and Export DOCKER_AUTH_CONFIG
			- Use your token to create the JSON structure that Docker and GitLab Runner understand:
				- ~~~sh
				AUTH_B64=$(printf '%s:%s' "$CI_REGISTRY_USER" "$REGISTRY_TOKEN" | base64 | tr -d '\n')
				export DOCKER_AUTH_CONFIG=$(printf '{"auths":{"%s":{"auth":"%s"}}}' "$CI_REGISTRY" "$AUTH_B64")
				~~~
			- On macOS, base64 wraps lines by default, so pipe through `tr -d '\n'`
			- `$CI_REGISTRY_USER` is typically `gitlab-ci-token` or your project's read-only username
		- 4. Store DOCKER_AUTH_CONFIG in GitLab CI/CD Settings
			- In your project, go to **Settings ▸ CI/CD ▸ Variables**
			- Click **Add variable**:
				- Key: `DOCKER_AUTH_CONFIG`
				- Type: File
				- Value: (paste the JSON you just exported)
				- Check Protected and Masked if desired
			- Save the variable
		- 5. Reference in .gitlab-ci.yml
			- GitLab Runner will automatically pick up `DOCKER_AUTH_CONFIG` and use it when pulling images. In your `.gitlab-ci.yml`, you do NOT need to explicitly docker login—just ensure the variable is available:
				- ~~~yaml
				image:
				  name: registry.gitlab.com/your-group/your-private-image:latest
				  # (optional) force fresh pull
				  pull_policy: always
				variables:
				  # If you're overriding, ensure DOCKER_AUTH_CONFIG is inherited
				  DOCKER_AUTH_CONFIG: $DOCKER_AUTH_CONFIG
				stages:
				  - build
				build-job:
				  stage: build
				  script:
				    - echo "Building with private image..."
				    # GitLab Runner uses DOCKER_AUTH_CONFIG to authenticate automatically
				    - docker info
				~~~
			- Tip: You can verify that your runner is using the correct credentials by inspecting the job log for `Authenticating with credentials from DOCKER_AUTH_CONFIG`
	- ## Troubleshooting
		- Permission denied pulling image
			- Double-check your token has read_registry scope
			- Ensure the CI/CD variable is of File type and your JSON is valid
		- Base64 line-wrap issues
			- Always strip newlines: `base64 | tr -d '\n'`
	- ## Related
		- [[GitLab/How To/Configure GitLab Runner]]
		- [[GitLab/How To/Use Private Container Registry]]