tags:: [[Prompts]]

- # [Prompt templates - LLM](https://llm.datasette.io/en/stable/templates.html#prompt-templates)
	- Prompt templates can be created to reuse useful prompts with different input data.
	- ## Where are prompt templates stored?
		- Templates are stored as YAML files in a templates directory
		- To find the directory location, run:
		  ```bash
		  llm templates path
		  ```
		- On macOS, typically at: `~/Library/Application Support/io.datasette.llm/templates/`
		- On Linux, typically at: `~/.config/io.datasette.llm/templates/`
		- Each template is a separate YAML file, NOT stored in SQLite
		- Example template format:
		  ```yaml
		  prompt: |
		    Please review this code and suggest improvements:
		    $input
		  ```
	- ## How to manage templates?
		- Create with --save:
		  ```bash
		  llm 'Summarize this: $input' --save summarize
		  ```
		- List templates: `llm templates list`
		- Show template: `llm templates show <name>`
		- Edit template: `llm templates edit <name>`
		- Use template:
		  ```bash
		  cat myfile.py | llm -t code-review
		  ```
	-