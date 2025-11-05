alias:: [[Anthropic/App/Claude Code/How To/Install]]

- # Claude Code Installation
	- Claude Code now has a new native installer that is "much more stable and does not require Node.js," replacing the old npm-based global install.
	- ## Fresh Installation
		- You can install Claude Code fresh via:
			- Homebrew: `brew install --cask claude-code`
			- Install script: `curl -fsSL https://claude.ai/install.sh | bash`
	- ## Upgrading from npm Installation
		- For existing npm users, the recommended way to switch to the native version is to run:
			- ~~~bash
			  npm install -g @anthropic-ai/claude-code@latest
			  claude --help | grep install
			  claude install latest
			  ~~~
	- ## References
		- [Claude Code CHANGELOG v2.0.33](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2033)
		- [Claude Code overview - Claude Docs](https://docs.claude.com/en/docs/claude-code/overview)

