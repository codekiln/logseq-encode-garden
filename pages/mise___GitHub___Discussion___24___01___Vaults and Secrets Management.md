# [vaults/secrets management · jdx/mise · Discussion #3712](https://github.com/jdx/mise/discussions/3712)
	- ## [[My Notes]]
		- open discussion on how the team can add add [[Secrets Management]] to [[mise]]. as of [[2025-03-23 Sun]] there are no proposals on the table and discussion hasn't been active since last year.
	- ## Summary
		- ### Initial Proposal by [[@jdx]]
			- Two main approaches suggested:
				- #### Built-in Encryption
					- Allow committing encrypted config into repo
					- Single env var for decryption
					- Potential integrations:
						- macOS keychain
						- YubiKeys
				- #### Backend Support
					- Integration with various secret management systems:
						- [[HashiCorp/Vault]]
						- macOS keychain
						- Heroku/Vercel env vars
						- [[dotenv-org/vault]]
		- ### Community Feedback
			- #### [[chezmoi]] Integration Suggestion
				- Already supports multiple password managers
				- Preference for referencing secrets over storing encrypted copies
				- Easier secret rotation when not storing copies
			- #### [[1Password/Dev/op]] Integration Considerations
				- Recommendation to use secret references with `op inject`
				- Example usage:
					- ~~~bash
					  # .env file with references
					  AWS_SECRET_ACCESS_KEY="op://dev/credentials/aws_secret_access_key"
					  
					  # Usage methods
					  cat .env | op inject  # output resolved .env
					  source <(cat .env | op inject)  # load into shell
					  ~~~
			- #### [[sops]] Integration
				- Currently used with [[direnv]] plugin successfully
				- Benefits:
					- Single YAML file for configuration
					- Flexible output (shell env vars, JSON, YAML)
					- PGP key support
				- [[mise/plugin/mise-sops]] plugin development in progress
					- Based on asdf-sops
					- Includes caching for improved performance
			- #### Alternative Approaches
				- [[rops]] suggested as alternative to [[sops]] for teams using KMS
				- Command-based secret resolution (like weechat/aerc)
				- [[keybase]] for personal use
				- [[AWS/SSM]] for AWS environments
				- [[Person/Vincent Prouillet/GitHub/tera]] templates for command execution
					- ~~~toml
					  [env]
					  USR="{{exec(command='./vault kv get -address=http://localhost:8200 -mount test -field=usr myapp')}}"
					  ~~~
		- ### Key Discussion Points
			- Preference for managing secrets outside of mise
			- Need for efficient secret resolution mechanism
			- Focus on workspace-specific secret management
			- Related to task management discussion in #3542
		- ### Current Status
			- Discussion ongoing
			- Multiple integration paths being explored:
				- Direct tool integration ([[1Password/Dev/op]], [[sops]])
				- Template-based approach ([[Person/Vincent Prouillet/GitHub/tera]])
				- Command-based resolution
			- See related issue: [[mise/GitHub/Issue/24/02/Struggles with integrating 1Password op]] for specific [[1Password/Dev/op]] integration challenges