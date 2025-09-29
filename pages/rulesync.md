# [dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync?tab=readme-ov-file#supported-tools-and-features)
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