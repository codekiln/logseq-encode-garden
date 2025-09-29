# [dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync?tab=readme-ov-file#supported-tools-and-features)
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
	- ## [[My Notes]]
		- [[2025-09-29 Mon]]
			- I tried running it in [[Person/codekiln/GitHub/logseq-cursor-rules]] in the root directory with ` rulesync import --targets cursor` and it didn't load any, because they were in the root of the directory. There's a [[GitHub/Issue]] for this here: [rulesync import ignores subdirectories in .cursor/rules · Issue #56 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/56).
			- I also tried running it in [[GitHub/codekiln/logseq-encode-garden]], which did have non-nested [[CursorAI/Project Rules]], but it did not import any rules, as far as I can tell, nor did it output any debug information.
			- As a result, I think this project is of limited utility at this time.
			- I filed [[GitHub/Issue]] [rulesync import --targets cursor does not import .cursor/rules/*.mdc · Issue #328 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/328)
			- result of running `rulesync generate --targets "*" --features "*" after importing` - ALL the [[AI/Coding/Tool]]s had rules imported!
				- ![image.png](../assets/image_1759154003791_0.png)
			- Again, this made me think that we need [[Package Management]] for [[Knowledge Gardens]], because what if we wanted to share some rules in multiple repositories. It does make me wonder if I need to just make my own MCP server which would be a gateway MCP server.
				- #Filed [[GitHub/Issue/My]]
					- [Brainstorm needed - how to share some rules across repos, but not all · Issue #329 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/329)
						- Each project usually requires a combination of shared and project-specific rules.
						- For example, some of my projects use rules and commands that are specific to the context of FastAPI. Others, use rules and commands specific to the context of typescript CLIs. I don't need all of my rules and commands in each project.
						- Ideally, it would be possible to define my rules for technology A, e.g. FastAPI, in one repo, my rules for technology B, e.g. TypeScript in another repo, and my rules for technology C, e.g. EnterprisePrivateTechnology in another private repo, and just marshal those rules into the current repo and then use `rulesync` to spread those out to the various providers.
						- One possible solution could be to use git submodules, but those may have problems:
						- in CI, if you have private repos, authentication permissions can get tricky with git submodules.
						- it's not clear that rulesync would support subdirectories needed for git submodules
						- So, let's talk about what possible solutions are out there for this use case.
					- [Feature request: pre-made rules for how AI can use rulesync · Issue #330 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/330)
						- In order for AI to aid in updating rules, AI needs the context of how `rulesync` works. It would be great if there was an [llms.txt with docs for AI](https://llmstxt.org/) or some other facility for instruction AI on how to update rulesync rules, and what the syntax is for the frontmatter.
						- Is it expected that a rulesync user will edit rules in the AI tool of their choice, then re-import them? Or is the target use case for those who wish to import and thereafter maintain `.rulesync/rules/*.md`?
	-