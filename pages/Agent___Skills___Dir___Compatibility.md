# Agent Skills Dir Compatibility
	- We really need something like a **feature compatibility matrix**
		- For JavaScript specifically, there were a few adjacent ecosystems:
			- [ECMAScript Compatibility Table (kangax)](https://compat-table.github.io/compat-table/es6/?utm_source=chatgpt.com)
				- Famous for ES6/ES2015+ feature-by-feature support matrices.
				- Covered things like promises, generators, async/await, proxies, etc.
				- Much more granular/spec-oriented than Can I Use.
				- Referenced widely in the JS community.
			- [MDN Browser Compatibility Data](https://github.com/mdn/browser-compat-data?utm_source=chatgpt.com)
				- Eventually became the underlying structured compatibility dataset used by many tools.
				- Covers JS, CSS, HTML, Web APIs, runtimes, etc.
			- [Can I Use: Promises](https://caniuse.com/?search=Promises&utm_source=chatgpt.com)
				- Example of how Can I Use indexed individual JS features too.
	- We need something that has dimensions
		- dimensions like:
			- slash commands
			- MCP
			- skills
			- hooks
			- sandboxing
			- resumability
			- CI mode
			- streaming tool calls
			- multi-agent orchestration
			- structured plans
			- browser control
			- Git worktree awareness
			- offline support
	- ## Estimation of compatibility from ChatGPT for [[Agent/Skills/Dir]] `.agent/skills` specifically
		- | Tool | Project `.agents/skills/` | User `~/.agents/skills/` | Native skill dir | Notes |
		  | ---- | ---- | ---- |
		  | Claude Code / Claude Agent SDK | Not found in current docs | Not found in current docs | `.claude/skills/`, `~/.claude/skills/` | Docs only cite `.claude/skills/` locations and plugin skills. ([Claude Code](https://code.claude.com/docs/en/agent-sdk/skills)) |
		  | OpenAI Codex | Yes | Yes | `.agents/skills/` | Codex appears to use the open path directly rather than a `.codex/skills` authoring path. ([OpenAI Developers](https://developers.openai.com/codex/skills)) |
		  | Gemini CLI | Yes | Yes | `.gemini/skills/`, `~/.gemini/skills/` | `.agents/skills/` is documented as an alias and has same-tier precedence. ([Gemini CLI](https://geminicli.com/docs/cli/skills/)) |
		  | OpenCode | Yes | Yes | `.opencode/skills/`, `~/.config/opencode/skills/` | Also supports Claude-compatible `.claude/skills/`. ([OpenCode](https://opencode.ai/docs/skills/)) |
		  | Warp | Yes | Yes | `.warp/skills/`, `~/.warp/skills/` | Also scans many other vendors’ skill dirs. ([Warp](https://docs.warp.dev/agent-platform/capabilities/skills/)) |
		  | Cursor | Needs deeper verification | Needs deeper verification | Cursor docs exist, but location details need direct extraction | Cursor has official Agent Skills docs, but the fetched page did not expose lines with directory search paths. ([Cursor](https://cursor.com/docs/skills?utm_source=chatgpt.com)) |