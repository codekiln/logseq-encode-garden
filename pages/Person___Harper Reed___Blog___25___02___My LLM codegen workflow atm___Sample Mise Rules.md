tags:: mise, [[llm-cli]], repomix
created-by:: [[Person/Harper Reed]]
alias:: [[Person/Harper Reed/Sample Mise Rules]]

- # Harper Reed - Sample [[mise/Tasks]] for [[AI/Coding]]
	- #notes
		- See [[Person/Harper Reed/GitHub/dotfiles/mise]] [here](https://github.com/harperreed/dotfiles/blob/560ebda30d1b8cea81acee8d44ebe1cf8be3aa2e/.config/mise/config.toml)
			- To install:
				- ```
				  $ mkdir -p ~/.config/mise
				  $ cd ~/.config/mise
				  $ curl -o config.toml https://raw.githubusercontent.com/harperreed/dotfiles/560ebda30d1b8cea81acee8d44ebe1cf8be3aa2e/.config/mise/config.toml
				  ```
			- Note: Harper hasn't shared his actual [[llm-cli/Prompt template]]s AFAIK, so we'll need to create our own versions of these templates:
				- `readme-gen`
				- `github-issue-gen`
				- `code-review-gen`
				- `missing-tests-gen`
				- `issue-prompts-gen`
		- I'd like to adapt these commands so the files are not in the root of the repo but are instead in `.ai-coding/*`
		  id:: 67bc53e0-115e-4c8b-9fb2-dfbd65c1665e
	- DONE Configure AI coding task collection in `~/.config/mise/config.toml`:
		- ### `LLM:generate_bundle` - Bundle Generation Task
			- Generate LLM bundle using #Repomix
			- #Via [[Person/Harper Reed/GitHub/dotfiles]] [here](https://github.com/harperreed/dotfiles/blob/560ebda30d1b8cea81acee8d44ebe1cf8be3aa2e/.config/mise/config.toml#L33)
			- ```toml
			  [tasks."llm:generate_bundle"]
			  description = 'Generate LLM bundle output file using repomix'
			  hide = true # hide this task from the list
			  run = """
			  #!/usr/bin/env bash
			  npx repomix --style xml --output-show-line-numbers --output output.txt --ignore **/uv.lock,**/package-lock.json,**/.env,**/Cargo.lock,**/node_modules,**/target,**/dist,**/build,**/output.txt,**/yarn.lock
			  """
			  ```
		- ### `LLM:clean_bundles` - Clean Bundles Task
			- Remove all output.txt files
			- ```toml
			  [tasks."llm:clean_bundles"]
			  description = 'Generate LLM bundle output file using repomix'
			  run = """
			  #!/usr/bin/env bash
			  find . -name "output.txt" -print -delete
			  """
			  ```
		- ### `LLM:generate_readme` - README Generation
			- Depends on generate_bundle task
			- #notes
				- this depends on the [[llm-cli/Prompt template]] called `readme-gen`, which Harper hasn't shared, but which can be imagined
			- ```toml
			  [tasks."llm:generate_readme"]
			  depends = ["llm:generate_bundle"]
			  description = 'Generate README.md from repository content stored in output.txt using LLM generation'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | llm -t readme-gen > README.md
			  """
			  ```
		- ### `LLM:copy_buffer_bundle` - Clipboard Operations
			- Depends on generate_bundle task
			- ```toml
			  [tasks."llm:copy_buffer_bundle"]
			  depends = ["llm:generate_bundle"]
			  description = 'Copy generated LLM bundle from output.txt to system clipboard for external use'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | pbcopy
			  echo "Pushed output.txt to the copy buffer"
			  """
			  ```
		- ### `LLM:generate_github_issues` - Issue Generation
			- Depends on generate_bundle task
			- #notes
				- this depends on the [[llm-cli/Prompt template]] called `github-issue-gen`
				- would need to create this template to generate GitHub-formatted issues from codebase
			- ```toml
			  [tasks."llm:generate_github_issues"]
			  depends = ["llm:generate_bundle"]
			  description = 'Generate GitHub issues from repository content stored in output.txt using LLM generation'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | llm -m claude-3.5-sonnet -t github-issue-gen > issues.md
			  """
			  ```
		- ### `LLM:generate_code_review` - Code Review Generation
			- Depends on generate_bundle task
			- #notes
				- this depends on the [[llm-cli/Prompt template]] called `code-review-gen`
				- template should instruct LLM to analyze code for best practices, issues, and improvements
			- ```toml
			  [tasks."llm:generate_code_review"]
			  depends = ["llm:generate_bundle"]
			  description = 'Generate code review output from repository content stored in output.txt using LLM generation'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | llm -m claude-3.5-sonnet -t code-review-gen > code-review.md
			  """
			  ```
		- ### `LLM:generate_missing_tests` - Test Coverage Analysis
			- Depends on generate_bundle task
			- #notes
				- this depends on the [[llm-cli/Prompt template]] called `missing-tests-gen`
				- template should guide LLM to identify untested code paths and suggest test cases
			- ```toml
			  [tasks."llm:generate_missing_tests"]
			  depends = ["llm:generate_bundle"]
			  description = 'Generate missing tests for code in repository content stored in output.txt using LLM generation'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | llm -m claude-3.5-sonnet -t missing-tests-gen > missing-tests.md
			  """
			  ```
		- ### `LLM:generate_issue_prompts` - Prompt Generation
			- Depends on generate_bundle task
			- #notes
				- this depends on the [[llm-cli/Prompt template]] called `issue-prompts-gen`
				- template should help LLM generate useful prompts for common development tasks
			- ```toml
			  [tasks."llm:generate_issue_prompts"]
			  depends = ["llm:generate_bundle"]
			  description = 'Generate issue prompts from repository content stored in output.txt using LLM generation'
			  run = """
			  #!/usr/bin/env bash
			  cat output.txt | llm -m o3-mini -t issue-prompts-gen > issue-prompts.md
			  """
			  ```
	- ## #notes
		- Uses a hidden `llm:generate_bundle` task that other tasks depend on
		- Uses [[llm-cli]] with specific templates (-t flag) and models (-m flag)
		- More specific ignore patterns in the bundle generation
		- Simpler output paths (directly in project root rather than .ai-coding/)
		- Uses Claude 3.5 Sonnet for most generations, O3-mini for prompts
		- Tasks generate files in the project root directory; ((67bc53e0-115e-4c8b-9fb2-dfbd65c1665e))
		- Uses the `llm` CLI tool with specific templates
		- For clipboard operations, uses [[pbcopy]] (macOS) - adjust for your OS
		- ### Prerequisites
			- Requires:
				- repomix (via npx)
				- llm CLI tool
				- Claude API access for some tasks