# How to use [[1Password/Dev/op/run]] only in dev environments when using [[mise/Tasks]]
	- ## Impetus
		- In [[CICD]] you want to use [[GitHub Actions]] with their own [[GitHub/Repo/Setting/Security/Secrets]] defined; see also [[GitHub/Docs/Actions/Security/Guides/Using Secrets]] and [[GitHub/Repo/Setting/Security/Secrets]]
		- Locally, you want to use [[op/run]] to pull the secret from [[1Password]]
		- Assumption - you want to use `mise run <XYZ>` and have it prepend an alias of `op run` if we are in dev but not if we are in CI
	- ## Using [[mise/config/Environment]] to optionally prepend `op run`
		-