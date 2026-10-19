see-also:: [[rulesync/Explanation/Rulesync authenticates to GitHub with GITHUB_TOKEN]], [[mise/Config/Setting]]

- # [github.credential_command mise setting](https://mise.jdx.dev/dev-tools/github-tokens.html#credential-command)
	- Type: `string` (optional)
	- Scope: global config only (`~/.config/mise/config.toml`). A project `mise.toml` cannot set it.
	- A shell command that prints a GitHub token on stdout. mise uses the token for its own GitHub API calls.
	- The command receives `MISE_CREDENTIAL_HOST` and `MISE_CREDENTIAL_PROVIDER`. It runs once per host per mise command, with mise's shims removed from `PATH`.
	- ## Example for a `gh` login kept in the macOS Keychain
		- ~~~toml
		  [settings.github]
		  credential_command = 'gh auth token --hostname "$MISE_CREDENTIAL_HOST"'
		  ~~~
		- `mise token github` shows which source mise picked, with the token masked.
	- ## Reach
		- The token goes to mise. mise does not export it to the programs it runs, so a tool such as [[rulesync]] needs its own `GITHUB_TOKEN`. See [[rulesync/Explanation/Rulesync authenticates to GitHub with GITHUB_TOKEN]].
	- Sibling settings: `gitlab.credential_command`, `forgejo.credential_command`.
