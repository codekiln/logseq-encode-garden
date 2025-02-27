# [[GitHub/Gist]] [[CursorAI/Project Rule]] auto-updater technique
	- ## Overview
	  id:: 67c04111-e634-477d-9d5f-7b29daf0e0aa
		- This technique can be used to publish a **Cursor Project Rule** to a **GitHub Gist** with an installation script that **can also update the project rule** if it gets out of date.
		- ### #Example - [[CursorAI/Project Rule/cursor-project-rule-editor.mdc]]
			- The gist contains three files:
				- `cursor-project-rule-editor.mdc` - The main rule file
				- `#Cursor Project Rule Editor Rule.md` - Installation and usage instructions
				- `update.sh` - Auto-update script for macOS
			- ### How to Use example
				- 1. Visit https://gist.github.com/codekiln/242b572c64c1097277fd4c831db91c10
				- 2. Run the one-liner in your project root:
					- ~~~bash
					  curl -s https://gist.githubusercontent.com/codekiln/242b572c64c1097277fd4c831db91c10/raw/update.sh | bash
					  ~~~
				- 3. The script will:
					- Create `.cursor/rules` directory if needed
					- Install or update the rule file
					- Add version tracking using gist commit hashes
					- Show status messages for install/update/current
	- ## Future variations
		- could consider making a generic script that would detect any .mdc files in the gist and apply to all of them, so that installer could be reused
		- it would probably be better if there was a standard [[Package Manager]] for cursor rules though
		- could also consider a [[GitHub Repo Template]] as a way to create one's own **stdlib**, as per [[Person/Geoffrey Huntley/Blog/25/02/You are using Cursor AI incorrectly...]]
	- ### Benefits for Sharing Cursor Rules
		- Version control through GitHub Gists
		- Easy one-line installation for other users
		- Automatic version tracking using gist commit hashes
		- Clear update path for rule modifications
		- Maintains proper file structure in `.cursor/rules`