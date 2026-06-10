logseq-entity:: [[Logseq/Entity/CLI/Flag]]
see-also:: [[Claude/Code/Settings]]

- # [claude --add-dir](https://docs.claude.com/en/docs/claude-code/cli-reference#cli-flags)
	- Flag for [[Claude/Code]] that adds one or more additional working directories for the session.
	- ## Usage
		- ~~~bash
		  claude --add-dir <path> [<path> ...]
		  ~~~
		- Validates each path exists as a directory. Multiple paths can be given in one invocation.
		- Paths must be absolute; `~` tilde is **not** expanded (see [[Claude/Code/Q/Can the ~ tilde character be used in Claude Code's additionalDirectories setting in settings.json?]]).
	- ## What it does
		- Grants Claude file read and write access to the specified directories (same as `permissions.additionalDirectories` in [[Claude/Code/Settings]]).
		- Also discovers and loads `.claude/skills/` from each added path — this skill-loading step does **not** occur with `permissions.additionalDirectories`.
		- An in-session equivalent exists: `/add-dir` slash command.
	- ## Relationship to `permissions.additionalDirectories`
		- Both grant file access to additional directories; the settings key persists across sessions while `--add-dir` applies only for the current invocation.
		- Key difference: `permissions.additionalDirectories` grants file access **only**. `--add-dir` (and `/add-dir`) also load skills from `.claude/skills/` inside each added path.
		- See [[Claude/Code/Q/In Claude Code settings, is it possible to declare additional directories that should be checked for the directories that skills are loaded from?]]
	- ## Pre-authorizing directories via settings
		- To grant persistent file access without using the flag each time, add to `permissions.additionalDirectories` in `~/.claude/settings.json` (user-global) or `.claude/settings.json` (project-level):
			- ~~~json
			  {
			    "permissions": {
			      "additionalDirectories": ["/absolute/path/to/dir"]
			    }
			  }
			  ~~~
		- This covers file read/write access but **not** skill discovery. Use `--add-dir` at startup or `/add-dir` in-session when the target directory's `.claude/skills/` should also be loaded.
		- `~` is not supported in the settings value either; always use absolute paths.
