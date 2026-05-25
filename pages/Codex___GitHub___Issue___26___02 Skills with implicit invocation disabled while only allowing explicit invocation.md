- [Skills with implicit invocation disabled while only allowing explicit invocation #10585](https://github.com/openai/codex/issues/10585)
	- body
		- ### What feature would you like to see?
		  
		  This issue is preceded by this question:
		- [Specify that a skill cannot be invoked implicitly #10573](https://github.com/openai/codex/issues/10573)
		  
		  ---
		  
		  Currently, there is no way to disable implicit invocation of skills while allowing explicit invocation via `$<name>`; we can only instruct `codex` in natural languages not to invoke skills implicitly, which may or may not be respected by `codex`.
		  
		  Given that [custom prompts](https://developers.openai.com/codex/custom-prompts/), which is similar to skills but can only be invoked explicitly (via `/prompts:<name>`), [is deprecated in favor of skills](https://github.com/openai/codex/issues/4734#issuecomment-3786166437), there should be a way to define skills with implicit invocations disabled; otherwise skills cannot be a complete alternative to custom prompts.
	- [your-diary](https://github.com/your-diary) [on Feb 3](https://github.com/openai/codex/issues/10585#issuecomment-3845192069)
		- to Author [@etraut-openai](https://github.com/etraut-openai)
		  It's a theoretical concern.
		- I have many custom prompts which perform destructive operations such as deleting AWS resources, so I want to be 100% (not 99%) sure they are invoked only when I explicitly request so.
	- [wsmoak](https://github.com/wsmoak) [on Feb 14](https://github.com/openai/codex/issues/10585#issuecomment-3902544135)
		- Some tools use `disable-model-invocation: true` in the frontmatter for this -- then the skill will not be auto-invoked, only if you specifically ask for it. I thought it was in the agent skills spec but apparently not.
		- Cursor defines it like this:
		- > By default, skills are automatically applied when the agent determines they are relevant. Set disable-model-invocation: true to make a skill behave like a traditional slash command, where it is only included in context when you explicitly type /skill-name in chat.
	- [lattwood](https://github.com/lattwood) [on Mar 23](https://github.com/openai/codex/issues/10585#issuecomment-4110626198)
		- One potential use-case for this functionality are ==skills that the agent might not be able to invoke in all environments== the repository is being modified in.
		- [[Good point]]
			- For instance, an infrastructure type repo could have a skill for planning/previewing the changes (ie [[Terraform/Plan]]), but it requires SRE type credentials to be discoverable in the environment. This is *not* a skill you would want the model to automatically try to invoke if it's running somewhere like Codex Cloud, but it **is** a skill you would want to manually invoke from Codex CLI running on your laptop.
	- [etraut-openai](https://github.com/etraut-openai) [on Mar 30](https://github.com/openai/codex/issues/10585#issuecomment-4155714608)
		- This feature is already supported. See [[Codex/Skill/Optional metadata]] for details.
	- [ignatremizov](https://github.com/ignatremizov) [on Apr 3](https://github.com/openai/codex/issues/10585#issuecomment-4183067933)
		- For anyone landing here from search: this is configured in the skill metadata file `agents/openai.yaml`, not in `SKILL.md`.
		- Example:
		- ```
		  policy:
		    allow_implicit_invocation: false
		  ```
		- Typical layout:
		- ```
		  my-skill/
		  ├── SKILL.md
		  └── agents/
		    └── openai.yaml
		  ```
		- With that setting, the skill is not injected implicitly, but it can still be invoked explicitly via `$skill-name`.
	- [MichaelYochpaz](https://github.com/MichaelYochpaz) [last week](https://github.com/openai/codex/issues/10585#issuecomment-4463258550)
		- I'd love it if Codex just supported the `disable-model-invocation` Frontmatter flag, as it's somewhat conventional and would work across other harnesses (from what I've found, this flag is currently supported on Claude Code, Gemini CLI, Cursor and Pi).
		- [[Good point]]
			- Forcing a custom `openai.yaml` file convention and making it Codex-specific is as-annoying as Anthropic not adopting the `AGENTS.md` file convention on Claude Code and forcing everyone to symlink `CLAUDE.md`.