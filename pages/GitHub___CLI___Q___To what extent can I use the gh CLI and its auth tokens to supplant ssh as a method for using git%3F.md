logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[GitHub/Auth/OAuth]]

- # To what extent can I use the `gh` CLI and its auth tokens to supplant SSH as a method for using git?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [GitHub CLI manual: gh auth setup-git](https://cli.github.com/manual/gh_auth_setup-git)
		- **Short answer:** almost entirely, for GitHub-hosted repos — `gh auth setup-git` wires git's credential helper to the token from `gh auth login`, so any HTTPS-protocol git command (`clone`, `fetch`, `push`, `pull`, submodules) authenticates without touching an SSH key.
		- How it works:
			- `gh auth login` stores an OAuth token (or PAT) per authenticated host.
			- `gh auth setup-git` (all authenticated hosts) or `gh auth setup-git --hostname <host>` sets `credential.https://<host>.helper` to `gh auth git-credential`, which implements the git credential-helper protocol and hands git the stored token on request.
			- `gh config set git_protocol https` makes `gh repo clone` and similar default to HTTPS remotes instead of `git@github.com:...` SSH URLs.
		- Where it falls short of a full SSH replacement:
			- Only covers hosts authenticated via `gh auth login` (`github.com` or a configured GHES hostname) — no help for GitLab, Bitbucket, or bare self-hosted git remotes.
			- Existing SSH-style remotes (`git@github.com:org/repo.git`) bypass the credential helper entirely; a repo needs an HTTPS remote (or a `url.insteadOf` rewrite) to benefit.
			- Requires the `gh` binary on `PATH` wherever git runs — CI runners or other tools that shell out to git without `gh` installed won't authenticate this way.
			- Commit/tag signing via SSH keys (`gpg.format = ssh`) is unrelated to `gh auth` — that's a separate git config, not something the `gh` token replaces.
			- Orgs that enforce SSH-only access or IP-allowlisted SSH still require SSH; HTTPS+token access is instead subject to whatever policy applies to OAuth/PAT tokens.
		- **Net:** for day-to-day git-over-GitHub, `gh auth setup-git` removes the need to manage an SSH keypair or agent. It doesn't extend to non-GitHub remotes or to SSH-based commit signing.
