created-by:: [[Person/Kazuki Yamada]]
tags:: #LLMs, [[CLI/Tool]], [[AI/LLM/Tool/Repo Summarizer]]

- # Repomix
	- id:: 67b59da6-2954-4c43-8505-60ca22587e1d
	  > 📦 Repomix (formerly Repopack) is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models #LLMs or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.
	- [[Repomix/GitHub]] https://github.com/yamadashy/repomix
	- [[Repomix/Web]] https://repomix.com/
		- This tool can be used online
	- ## Usage
		- ## [[Repomix/Config]]
			- See [[Repomix/repomix.config.json]] for options
			- ### Creating a Config File with [[repomix/--init]]
				- creates a config file in current dir
					- [[repomix/--global]] can be used with `--init` to create a global config file
			- ### Specifying a Config File with [[Repomix/--config]]
				- use with [[repomix/--global]] to utilize global config file
				- To use Repomix with a specific configuration file, use the following command:
				  ~~~bash
				  npx repomix --config path/to/repomix.config.json
				  ~~~
				- This will generate the output based on the settings in your configuration file
				- The config file allows you to customize:
					- Which files to include/exclude
					- Output format
					- Repository metadata
	- ## [[see-also]]
		- [[gitingest]]
		-
-