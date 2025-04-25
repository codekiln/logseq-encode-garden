# [codekiln/logseq-cursor-rules: Cursor project rules for working with logseq graphs](https://github.com/codekiln/logseq-cursor-rules)
	- ## How to install
		- These cursor project rules can be installed as a git submodule in your logseq graph project.
		- ### Prerequisites
			- Your logseq graph must be a git repository
			- You must have git installed
			- You must have SSH access to GitHub configured
		- ### Installation Steps
			- 1. First ensure you have a `.cursor/rules` directory in your logseq graph:
				- ```bash
				  mkdir -p .cursor/rules
				  ```
			- 2. Add the rules as a git submodule:
				- git submodule add git@github.com:codekiln/logseq-cursor-rules.git .cursor/rules/logseq-cursor-rules
			- 3. Commit the changes:
				- ```bash
				  git add .cursor/rules/logseq-cursor-rules .gitmodules
				  git commit -m "feat: add logseq-cursor-rules as submodule"
				  ```
		- ### For Existing Projects
			- If you're cloning a project that already has this submodule, you'll need to:
				- ```bash
				  git submodule update --init --recursive
				  ```
		- ### Updating the Rules
			- To update to the latest version of the rules:
				- ```bash
				  cd .cursor/rules/logseq-cursor-rules
				  git pull origin main
				  cd ../../..
				  git add .cursor/rules/logseq-cursor-rules
				  git commit -m "chore: update logseq-cursor-rules"
				  ```