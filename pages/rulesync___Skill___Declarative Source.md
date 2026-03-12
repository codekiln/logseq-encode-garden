# [Declarative Skill Sources | Rulesync](https://rulesync.dyoshikawa.com/guide/declarative-sources.html)
	- Rulesync can fetch skills from external repositories using the [[rulesync/install]] command. Instead of manually running `fetch` for each skill source, declare them in your `rulesync.jsonc` and run `rulesync install` to resolve and fetch them. Then [[rulesync/generate]] picks them up as local curated skills. Typical workflow: `rulesync install && rulesync generate`.
	- This lets you import sources from another repository
	- ## Configuration
		- Add a `sources` array to your `rulesync.jsonc`:
			- ```json
			  {
			    "$schema": "https://github.com/dyoshikawa/rulesync/releases/latest/download/config-schema.json",
			    "targets": ["copilot", "claudecode"],
			    "features": ["rules", "skills"],
			    "sources": [
			      // Fetch all skills from a GitHub repository (default transport)
			      { "source": "owner/repo" },
			  
			      // Fetch only specific skills by name
			      { "source": "anthropics/skills", "skills": ["skill-creator"] },
			  
			      // With ref pinning and subdirectory path (same syntax as fetch command)
			      { "source": "owner/repo@v1.0.0:path/to/skills" },
			  
			      // Git transport — works with any git remote (Azure DevOps, Bitbucket, etc.)
			      {
			        "source": "https://dev.azure.com/org/project/_git/repo",
			        "transport": "git",
			        "ref": "main",
			        "path": "exports/skills",
			      },
			  
			      // Git transport with a local repository
			      { "source": "file:///path/to/local/repo", "transport": "git" },
			    ],
			  }
			  ```
	- ## [How it works](https://rulesync.dyoshikawa.com/guide/declarative-sources.html#how-it-works)
		- The `skills/` directory (or the path specified in the source URL) is listed from the remote repository.
	-