tags:: Q, [[GitHub Personal Access Token]]

- # DONE How to create a [[GitHub/Auth/Personal]] with Fine-Grained permissions
	- there **isn't** currently a command to create Fine-Grained Personal Access Tokens (PATs) through the GitHub CLI #gh ... The closest authentication-related commands available are:- gh auth login - Which handles basic authentication and creates [[GitHub/Auth/Personal/Classic]] tokens
		- [[GitHub/CLI/gh/auth/token]] `gh auth token` - Which displays existing tokens
		- [[GitHub/CLI/gh/auth/refresh]] `gh auth refresh` - Which can modify scopes of existing tokens
	- To create a Fine-Grained PAT, you'll need to:- Visit GitHub's website directly: https://github.com/settings/tokens?type=beta
	- Or use the GitHub API endpoints for token management
	  If you need to use a Fine-Grained PAT with the GitHub CLI, you can create it on the website first and then use it by:
	- ## Setting [[GitHub/CLI/EnvVar/GH_TOKEN]]
		- `export GH_TOKEN=your_fine_grained_pat`
	- ## Or using it during login - [[GitHub/CLI/gh/auth/login]]
		- `gh auth login --with-token < pat_file.txt`