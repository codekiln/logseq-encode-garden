# [Look for custom prompts in {project root}/.codex/prompts/ first   - 4734](https://github.com/openai/codex/issues/4734)
	- [your-diary](https://github.com/your-diary) [on Feb 3](https://github.com/openai/codex/issues/4734#issuecomment-3845063487)
		- >  We have decided to deprecate support for custom prompts. We recommend switching to skills, which provide all of the functionality of custom prompts and more.
		  
		  There is no way to disable implicit invocation of skills ([#10573](https://github.com/openai/codex/issues/10573)).
		  
		  So skills cannot always be used in place of custom prompts.
		  
		  I opened a feature request related to this situation:
			- [[Codex/GitHub/Issue/26/02 Skills with implicit invocation disabled while only allowing explicit invocation]]
	- [rahuls360](https://github.com/rahuls360) [on Feb 9](https://github.com/openai/codex/issues/4734#issuecomment-3875273018)
		- > There is currently no option to turn off the implicit invocation of skills ([#10573](https://github.com/openai/codex/issues/10573)).
		- [@etraut-openai](https://github.com/etraut-openai) This accurately highlights the core distinction between custom slash commands and skills. Skills are designed to be triggered automatically by the LLM whenever a particular task needs to be performed. In contrast, custom slash commands are manually triggered by developers when necessary, providing a convenient way to execute predefined prompts.
		- Deprecating stash commands creates inconvenience when trying to store `.md` files and attach them only when required. This flexibility should remain with the developer.