# [dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync?tab=readme-ov-file#supported-tools-and-features)
	- ## [[My Notes]]
		- [[2025-09-29 Mon]]
			- I tried running it in [[Person/codekiln/GitHub/logseq-cursor-rules]] in the root directory with ` rulesync import --targets cursor` and it didn't load any, because they were in the root of the directory. There's a [[GitHub/Issue]] for this here: [rulesync import ignores subdirectories in .cursor/rules · Issue #56 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/56).
			- I also tried running it in [[GitHub/codekiln/logseq-encode-garden]], which did have non-nested [[CursorAI/Project Rules]], but it did not import any rules, as far as I can tell, nor did it output any debug information.
			- As a result, I think this project is of limited utility at this time.
			- I filed [[GitHub/Issue]] [rulesync import --targets cursor does not import .cursor/rules/*.mdc · Issue #328 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/328)
			- result of running `rulesync generate --targets "*" --features "*" after importing` - ALL the [[AI/Coding/Tool]]s had rules imported!
				- ![image.png](../assets/image_1759154003791_0.png)
			-
	- ## Docs
		- > A Node.js CLI tool that automatically generates configuration files for various AI development tools from unified AI rule files. Features selective generation, comprehensive import/export capabilities, and supports major AI development tools with rules, commands, MCP, ignore files, and subagents. Uses the recommended `.rulesync/rules/*.md` structure, with full backward compatibility for legacy `.rulesync/*.md` layouts.
		- Rulesync supports both **generation** and **import** for All of the major AI coding tools:
		  | Tool | rules | ignore | mcp | commands | subagents |
		  | ---- | ---- | ---- |
		  | AGENTS.md | ✅ |  |  |  |  |
		  | Claude Code | ✅ | ✅ | ✅ | ✅ | ✅ |
		  | Codex CLI | ✅ | ✅ |  | 🎮 | 🎮 |
		  | Gemini CLI | ✅ | ✅ |  | ✅ | 🎮 |
		  | GitHub Copilot | ✅ |  | ✅ | 🎮 | 🎮 |
		  | Cursor | ✅ | ✅ | ✅ | ✅ | 🎮 |
		  | OpenCode | ✅ |  |  |  |  |
		  | Cline | ✅ | ✅ | ✅ |  |  |
		  | Roo Code | ✅ | ✅ | ✅ | ✅ | 🎮 |
		  | Qwen Code | ✅ | ✅ |  |  |  |
		  | Kiro IDE | ✅ | ✅ |  |  |  |
		  | Amazon Q Developer CLI | ✅ |  | ✅ |  |  |
		  | JetBrains Junie | ✅ | ✅ |  |  |  |
		  | AugmentCode | ✅ | ✅ |  |  |  |
		  | Windsurf | ✅ | ✅ |  |  |  |
		  | Warp | ✅ |  |  |  |  |
		- 🎮: Simulated Commands/Subagents (Experimental Feature)
	-