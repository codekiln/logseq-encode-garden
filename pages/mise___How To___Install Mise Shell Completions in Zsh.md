tags:: [[Diataxis/How To]]

- # How To Install [[mise]] [[Shell/Completion]] in [[zsh]]
	- ## Goal
		- Enable tab-completion for the `mise` command in Zsh.
	- ## Preconditions
		- Zsh shell installed and configured.
		- `mise` installed via [mise.run](https://mise.jdx.dev/installing-mise.html).
	- ## Procedure
		- ### 1. Install [[usageCLI]]
			- `mise` relies on the `usage` CLI to generate shell completions.
			- Install it globally:
				- `mise use --global usage@latest`
		- ### 2. Generate the [[zsh/Completion]] Script
			- Create a directory for custom completions:
				- `mkdir -p ~/.zsh/completions`
			- Generate and save the completion script:
				- `mise completion zsh > ~/.zsh/completions/_mise`
		- ### 3. Configure [[zsh/.zshrc]] to Use the Completion Script
			- Edit your `.zshrc` file to include the completions directory:
				- Add the following lines:
					- ```zsh
					  fpath=(~/.zsh/completions $fpath)
					  autoload -Uz compinit
					  compinit
					  ```
			- Source your `.zshrc` to apply changes:
				- `source ~/.zshrc`
		- ### 4. Optional: Use the `zsh-mise` Plugin for [[zsh/Zap]]
			- For easier setup, consider using the `zsh-mise` plugin:
				- Add the plugin using your Zsh plugin manager, e.g., for [Zap](https://github.com/zap-zsh/zap):
					- `plug "wintermi/zsh-mise"`
				- The plugin handles installation and configuration of completions.
	- ## Troubleshooting
		- **Issue**: Autocompletion not working.
			- **Solution**:
				- Ensure `usage` is installed and up to date:
					- `usage --version`
				- Regenerate the completion script:
					- `mise completion zsh > ~/.zsh/completions/_mise`
				- Restart your terminal session.
		- **Issue**: Errors like `(eval):61: unmatched '` when using completions.
			- **Solution**:
				- Update `usage` to the latest version:
					- `mise use --global usage@latest`
				- Regenerate the completion script as above.
	- ## References
		- [Installing Mise](https://mise.jdx.dev/installing-mise.html)
		- [Mise Completion Command](https://mise.jdx.dev/cli/completion.html)
		- [zsh-mise Plugin Repository](https://github.com/wintermi/zsh-mise) for [[zsh/Zap]]