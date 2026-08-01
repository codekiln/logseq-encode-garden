tags:: [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Code/--/enable-auto-mode]], [[Claude/Code/Settings]]

- # How can I make auto mode the default permission mode?
	- ## [[AI Answer]]
		- **Short answer:** Set `defaultMode` to `auto` in **user** settings — `~/.claude/settings.json`. Project and local settings are ignored for this value.
		- ~~~json
		  {
		    "permissions": {
		      "defaultMode": "auto"
		    }
		  }
		  ~~~
		- [[Answer/Official]] from [Choose a permission mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode):
		- **User settings only.** From v2.1.142 on, `defaultMode: "auto"` in `.claude/settings.json` or `.claude/settings.local.json` is ignored "so a repository cannot grant itself auto mode." The symptom is a session that starts in Manual with no error message.
		- **`/doctor` offers to do it.** From v2.1.210 the checkup proposes the user-settings default, including on [[AWS/Bedrock]], Google Cloud's Agent Platform, and Microsoft Foundry.
		- **Per-session instead of default:** `claude --permission-mode auto`, or `Shift+Tab` to cycle — auto slots in last, after `plan`, and switching to it needs no confirmation.
		- **The old enable step is gone.** `CLAUDE_CODE_ENABLE_AUTO_MODE=1` was required on Bedrock, Agent Platform, Foundry, and signed-in Claude apps gateway sessions in v2.1.158–v2.1.206; v2.1.207 removed the requirement and the variable now has no effect. There is no `--enable-auto-mode` flag in current builds.
		- **Prerequisites for the setting to take effect** — auto mode has to be available to the account at all:
			- **Plan:** all plans. On Team and Enterprise it is on by default, but an administrator can set `permissions.disableAutoMode` to `"disable"` in managed settings, which also rejects `--permission-mode auto`.
			- **Model:** on the Anthropic API and Claude Platform on AWS, Claude Opus 4.6 or later, Claude Sonnet 4.6 or later, or [[Anthropic/Model/Claude/Fable/5]]. On [[AWS/Bedrock]], Agent Platform, Foundry, and Claude apps gateway sessions, only Claude Sonnet 5, [[Anthropic/Model/Claude/4.7/Opus]] or later, and [[Anthropic/Model/Claude/Fable/5]]. Haiku and the 4.5-generation models are unsupported on every provider.
		- **Other surfaces:**
			- **VS Code extension:** `claudeCode.initialPermissionMode` does not accept `auto` — the user-settings `defaultMode` is the only way to start there in auto mode.
			- **Desktop:** reads the same settings files, but a mode picked from the mode selector is remembered per folder and takes precedence over `defaultMode` for that folder.
			- **Claude Code on the web:** cloud sessions offer Accept edits, Plan, and Auto in the dropdown; auto appears only when the organization allows it and the model supports it.
