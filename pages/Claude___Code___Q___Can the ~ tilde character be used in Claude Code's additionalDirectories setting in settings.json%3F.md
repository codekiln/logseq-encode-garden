tags:: [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Code/Settings]]

- # Can the `~` tilde character be used in [[Claude/Code]]'s `additionalDirectories` setting in settings.json?
	- ## [[My Notes]]
		- if we are using [[ghq]] for everything then we should be able to use relative directories pretty easily
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** No — `~` is not expanded in `additionalDirectories`. Use a full absolute path instead.
			- `~` is a shell expansion feature; Node.js treats it as a relative path (`path.isAbsolute('~')` returns `false`), not as the home directory.
			- There is a [known bug](https://github.com/anthropics/claude-code/issues/17354) where using `~` causes Claude Code to create a literal `~/` directory inside the working directory.
			- **Use an absolute path:**
				- ~~~json
				  {
				    "permissions": {
				      "additionalDirectories": ["/Users/pnore/other-repo"]
				    }
				  }
				  ~~~
			- **Session-only alternative:** `/add-dir` in-session also requires an absolute path (shell expansion of `~` does not happen inside Claude Code).
