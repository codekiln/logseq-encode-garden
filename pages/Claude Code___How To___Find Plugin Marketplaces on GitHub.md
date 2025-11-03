tags:: [[Claude Code]], [[GitHub]], [[Plugin]]

- # How To Find Plugin Marketplaces on GitHub
	- ## Overview
		- Claude Code plugins that provide marketplace functionality include a `marketplace.json` file in a `.claude-plugin` directory
		- This file structure can be used to discover plugin marketplaces via GitHub search
	- ## GitHub Search Pattern
		- Use the following path pattern to find repositories containing Claude Code plugin marketplaces:
			- [claude-plugin marketplace json query on github](https://github.com/search?q=path%3A**%2F.claude-plugin%2Fmarketplace.json+&type=code)
			- ```bash
			  path:**/.claude-plugin/marketplace.json
			  ```
		- This search pattern will find all GitHub repositories that contain a `marketplace.json` file within a `.claude-plugin` directory
	- ## Usage
		- Navigate to [GitHub Search](https://github.com/search) and use the path pattern in the search box
		- This is useful for discovering:
			- Community-maintained plugin marketplaces
			- Plugin collections and repositories
			- Examples of marketplace.json structure
	- ## Related
		- [[Person/Seth Hobson/GitHub/agents]] - Example plugin marketplace (wshobson/agents)
		- [[Person/Daniel Avila/GitHub/claude-code-templates]] - Another example marketplace (davila7/claude-code-templates)
		- [[Claude Code/How To/Use Essential Commands]] - General Claude Code usage