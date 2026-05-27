see-also:: [[GitHub/CLI]], [[GitHub/App]]

- # GitHub Auth
	- Umbrella for how this garden documents **authenticating to GitHub**: personal access tokens, OAuth scopes used by [[GitHub/CLI]], and related how-tos.
	- ## Personal access tokens
		- [[GitHub/Auth/Personal]] — classic PAT (deprecated in favor of fine-grained)
		- [[GitHub/Auth/Personal/Fine-Grained]] — fine-grained PAT (repository + permission checkboxes; not the same strings as OAuth scopes)
	- ## OAuth scopes
		- [[GitHub/Auth/OAuth]] — what OAuth scopes are, normalization, inspection
		- [[GitHub/Auth/OAuth/Scope]] — catalog of scope names (`workflow`, `repo:status`, …) used by `gh auth refresh -s`
	- ## How-tos
		- [[GitHub/CLI/How to create a Fine Grained Personal Access Token]] — create a fine-grained PAT (no `gh` subcommand today)
