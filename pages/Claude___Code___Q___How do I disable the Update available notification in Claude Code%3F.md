tags:: [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Code/Settings]]

- # How do I disable the Update available notification in [[Claude/Code]]?
	- ## [[AI Answer]]
		- **Short answer:** Set `DISABLE_AUTOUPDATER=1` in `~/.claude/settings.json` under the `env` key.
		- Add to `~/.claude/settings.json`:
			- ~~~json
			  {
			    "env": {
			      "DISABLE_AUTOUPDATER": "1"
			    }
			  }
			  ~~~
		- This suppresses the yellow "Update available! Run: mise upgrade claude" banner that [[Claude/Code]] shows when it detects a newer version.
		- The `env` key in `settings.json` injects environment variables into the [[Claude/Code]] process; `DISABLE_AUTOUPDATER` is the variable that controls the built-in autoupdater.
		- If the file already has content, merge the `"env"` key into the existing JSON object rather than replacing the whole file.