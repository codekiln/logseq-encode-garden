logseq-entity:: [[Logseq/Entity/Question]]
- # How do I authenticate [[glab]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** `glab` needs a **GitLab Personal Access Token (PAT)** for API calls — SSH handles git operations only.
		- SSH is configured for *git protocol* (clone/push/pull), but commands like `glab repo view --web` call the **GitLab REST API**, which requires a separate token.
		- To authenticate, run:
		- ~~~bash
		  glab auth login
		  ~~~
		- This starts an interactive flow that asks for:
			- 1. The GitLab hostname (defaults to `gitlab.com`)
			- 2. Your preferred git protocol (keep SSH if desired)
			- 3. A Personal Access Token
		- **Create a PAT** at [https://gitlab.com/-/user_settings/personal_access_tokens](https://gitlab.com/-/user_settings/personal_access_tokens) with at minimum these scopes:
			- `api`
			- `write_repository`
		- **Non-interactive** (paste token directly):
		- ~~~bash
		  glab auth login --token glpat-<your-token>
		  ~~~
		- Credentials are stored in `~/.config/glab-cli/config.yml` (or OS keyring with `--use-keyring`).
		- Verify with:
		- ~~~bash
		  glab auth status
		  ~~~
