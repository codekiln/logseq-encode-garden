logseq-entity:: [[Logseq/Entity/Question]]

- # Which providers support global mode rules in [[rulesync]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [rulesync global-mode docs](https://rulesync.dyoshikawa.com/guide/global-mode.html)
		- ### Short answer
			- Yes. **Rules** work in global mode for many providers; **commands** only work for Claude Code. The flag is `"global": true` in `rulesync.jsonc` (or `--global` CLI).
		- ### Setup
			- 1. Create a dedicated directory (e.g. `~/.aiglobal`)
				- ~~~bash
				  mkdir -p ~/.aiglobal
				  ~~~
			- 2. Initialize rulesync in it
				- ~~~bash
				  cd ~/.aiglobal && rulesync init
				  ~~~
			- 3. Edit `~/.aiglobal/rulesync.jsonc` — in global mode only `global`, `features`, `delete`, and `verbose` are honoured; other keys are ignored. `features` accepts `"rules"` and `"commands"`.
				- ~~~jsonc
				  { "global": true }
				  ~~~
			- 4. Edit `~/.aiglobal/.rulesync/rules/overview.md` — only a single `root: true` file per target is supported in global mode.
				- ~~~md
				  ---
				  root: true
				  ---
				  
				  # The Project Overview
				  ...
				  ~~~
			- 5. Generate
				- ~~~bash
				  rulesync generate
				  ~~~
		- ### Which providers support global rules (from source)
			- The authoritative list is [`toolRuleFactories` in `rules-processor.ts`](https://github.com/dyoshikawa/rulesync/blob/7cc1f0771fabe0c3e1f4f81bd7dea4490e6c967a/src/features/rules/rules-processor.ts#L253), each entry with `meta.supportsGlobal`.
			- **`supportsGlobal: true`** — `amp`, `antigravity-cli`, `antigravity-ide`, `augmentcode`, `claudecode`, `claudecode-legacy`, `cline`, `codexcli`, `copilot`, `copilotcli`, `deepagents`, `factorydroid`, `geminicli`, `goose`, `junie`, `kilo`, `opencode`, `pi`, `qwencode`, `rovodev`, `takt`, `vibe`, `devin`, `zed` (24 total)
			- **`supportsGlobal: false`** — `agentsmd`, `antigravity`, `augmentcode-legacy`, `cursor`, `kiro`, `kiro-cli`, `kiro-ide`, `replit`, `roo`, `warp`
			- The docs list only Claude Code, Copilot, and OpenCode — the source covers more. The filtered list is derived at runtime via [`rulesProcessorToolTargetsGlobal`](https://github.com/dyoshikawa/rulesync/blob/7cc1f0771fabe0c3e1f4f81bd7dea4490e6c967a/src/features/rules/rules-processor.ts#L683).
		- ### How global mode changes output paths
			- When `global=true`, [`getOutputRootsInLightOfGlobal()`](https://github.com/dyoshikawa/rulesync/blob/7cc1f0771fabe0c3e1f4f81bd7dea4490e6c967a/src/config/config-resolver.ts#L332) sets `outputRoot` to `~` (home directory). For Claude Code specifically, [`ClaudecodeRule.getSettablePaths({ global: true })`](https://github.com/dyoshikawa/rulesync/blob/7cc1f0771fabe0c3e1f4f81bd7dea4490e6c967a/src/features/rules/claudecode-rule.ts#L81) emits to `~/.claude/CLAUDE.md`.
		- ### Commands: Claude Code only
			- Per docs and source, command generation in global mode is Claude Code only. The commands processor also has `supportsGlobal` per tool, but only `claudecode` maps to a real global commands path (`~/.claude/commands/`).
