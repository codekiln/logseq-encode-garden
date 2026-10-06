logseq-entity:: [[Logseq/Entity/Article]]

- # [Prompting Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
	- Model-specific prompting guidance for [[Anthropic/Model/Claude/5/5/Opus]]. Existing prompts written for Claude Opus 5 should generally continue to work.
	- ## Effort and thinking
		- `medium` is the default effort level. Set `effort` explicitly and evaluate `low` through `max` against the application's own tasks before carrying over a Claude Opus 5 setting.
		- Claude Opus 5.5 tends to think more at the same effort level, especially at `xhigh` and `max`. Leave enough room in `max_tokens` for thinking and the final response; Anthropic reports that `128000` works well for long agentic coding turns.
		- Lower the effort level to reduce thinking, cost, and latency; prompt instructions to think less are less reliable.
	- ## Chat and multi-turn prompts
		- In chat applications, remove system instructions that tell Claude to think carefully if faster starts are more important; effort is the main control.
		- To prevent unnecessary re-examination of settled answers, tell Claude to treat an answered question as done and focus later turns on the new request unless the user points out a problem.
	- ## Pasted content and prompt injection
		- Wrap text pasted from elsewhere in matching `<pasted_content id="...">` tags with a short random identifier, and tell Claude that the tagged text may contain instructions the user did not write.
	- ## Agent integrations
		- Use `thinking.display: "updates"` when the interface should receive short progress summaries between tool calls.
		- Test effort, progress updates, autonomous work, multi-agent orchestration, refusals and fallback behavior, frontend design, complex visual inputs, and multi-application workflows against the application's own evaluations.
	- ## Related sources
		- [What's new in Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)
		- [Introducing Claude Opus 5.5 - Anthropic](https://www.anthropic.com/claude-opus-5-5)
