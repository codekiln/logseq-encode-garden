tags:: [[rulesync]], [[Diataxis/Explanation]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[mise/Config/Setting/github.credential_command]], [[mise/Task/File]], [[lefthook]], [[GitHub/CLI/EnvVar/GH_TOKEN]]

- # Rulesync authenticates to GitHub with GITHUB_TOKEN
	- Behaviour read from the [jdx/mise](https://github.com/jdx/mise) docs at `bc1bdc54e` (`docs/dev-tools/github-tokens.md`), and observed with `rulesync 36.0.2`, `mise 2026.10.12` and `gh 2.102.0` on macOS.
	- ## Overview
		- `rulesync install` fetches [[rulesync]] sources, such as the skills in `codekiln/logseq-encode-garden`, through the GitHub contents API. It sends an authenticated request when `GITHUB_TOKEN` or `GH_TOKEN` is set in its environment, and an anonymous request otherwise.
		- A `gh auth login` on macOS keeps the token in the Keychain. Rulesync never asks `gh` for it, so a shell that is signed in to `gh` still runs rulesync anonymously.
		- Anonymous requests share GitHub's limit of 60 per hour. One install of this garden's skills makes more than a hundred requests, so a single run spends the hour's allowance and the rest fail with `403` and `429` errors:
			- ~~~
			  GitHubClientError: GitHub API rate limit exceeded. Consider using a GitHub token.
			  Tip: Set GITHUB_TOKEN or GH_TOKEN environment variable for private repositories or better rate limits.
			  ~~~
	- ## Context
		- ### Why a git hook makes it visible
			- [[lefthook]] runs `rulesync install` after every checkout and merge, so each step of a rebase spends more of the hour's allowance. A hook that exits non-zero stops the rebase.
		- ### Why `gh auth status` succeeds while rulesync fails
			- `gh auth status` reads the keyring. The environment variables are a separate channel, and nothing copies the keyring token into them.
			- `gh auth token` prints the keyring token, so `GITHUB_TOKEN=$(gh auth token) rulesync install` bridges the two.
		- ### What [[mise]] contributes
			- mise has its own token lookup for its own GitHub calls. It reads `GITHUB_TOKEN`, token files, the `gh` `hosts.yml` file, and a `credential_command`. On macOS the `gh` token sits in the Keychain, so mise needs `credential_command = 'gh auth token --hostname "$MISE_CREDENTIAL_HOST"'` to see it. See [[mise/Config/Setting/github.credential_command]].
			- Those sources feed mise only. mise does not export the token to the programs it runs, and it does not read `GH_TOKEN` itself.
			- `credential_command` is global-only. A project's `mise.toml` cannot set it.
	- ## Key Principles
		- A tool authenticates through the credential channel it implements, and a login held by a different tool is invisible to it.
		- A token held in a keyring reaches a child process only when something puts it into that process's environment.
	- ## Mechanism
		- Three ways to put the token into rulesync's environment, from narrowest to widest:
			- 1. A [[mise/Task/File]] that exports `GITHUB_TOKEN` from `gh auth token` and then runs `rulesync install` and `rulesync generate`. The hook calls `mise run <task>`. One repository changes, and no token touches disk. This is the fix `codekiln/logseq-garden` uses, as `rulesync:sync`.
			- 2. `GH_TOKEN` exported from the shell profile, as `export GH_TOKEN=$(gh auth token)`. Every program started from that shell sees it, at the cost of one `gh` call per shell.
			- 3. mise's native GitHub OAuth in the global mise config. With `github.oauth_client_id` set to a GitHub App's client ID and `mise token github --oauth` run once, mise exports `GITHUB_TOKEN` through `mise activate`, `mise hook-env`, `mise env` and `mise exec`. Every program run under mise reads it, including hooks that go through `mise x` or `mise run`. The token is a GitHub App user token, so it reaches only the repositories where the app is installed. It replaces a `GITHUB_TOKEN` already in the shell unless `github.oauth_export_env` names another variable.
	- ## Examples
		- The file task, `mise-tasks/rulesync/sync`:
			- ~~~bash
			  #!/usr/bin/env bash
			  #MISE description="Install rulesync sources and regenerate tool config, authenticated with the gh login"
			  set -euo pipefail
			  if [[ -z "${GITHUB_TOKEN:-}${GH_TOKEN:-}" ]] && command -v gh >/dev/null; then
			    GITHUB_TOKEN="$(gh auth token 2>/dev/null || true)"
			    export GITHUB_TOKEN
			  fi
			  rulesync install
			  rulesync generate
			  ~~~
		- The `lefthook.yml` entries, for both `post-merge` and `post-checkout`:
			- ~~~yaml
			  rulesync:
			    run: mise run rulesync:sync
			  ~~~
	- ## Misconceptions
		- "I'm signed in to `gh`, so every GitHub-calling tool is authenticated." Only tools that read the `gh` keyring or `hosts.yml` are.
		- "mise's GitHub token setting covers the tools it runs." It covers mise's own API calls.
