tags:: [[Idea]]
alias:: [[1P/Idea/Populate EnvVars]]

- # Populate [[EnvVar]]s using [[1Password/Dev]]
	- Ideally, we wouldn't even store passwords in [[.env Files]]. Instead, we'd use an integration with a dedicated password manager like [[1Password]], so secrets are never stored unencrypted on disk.
	- [[1Password/Environment]] is the product form of this: project [[EnvVar]]s live in 1Password and can be mounted without writing credentials to disk.
	-