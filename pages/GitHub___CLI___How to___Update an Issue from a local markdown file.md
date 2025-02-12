- Basic idea
	- 1. Using `gh issue edit`:
	  ~~~bash
	  # Edit issue content from a file
	  gh issue edit <issue-number> --body-file path/to/file.md
	  ~~~
	  
	  2. Using `gh issue comment` to add the file content as a comment:
	  ~~~bash
	  # Add file content as a comment
	  gh issue comment <issue-number> --body-file path/to/file.md
	  ~~~
	  
	  Additional useful options:
	- Use `-t` or `--title` to update the issue title at the same time
	- Use `-` as the filename to read from stdin
	- Use `--editor` to open your default editor with the current content
	- Examples:
	  ~~~bash
	  # Update issue #123 with content from update.md
	  gh issue edit 123 --body-file update.md
	  
	  # Update both title and body
	  gh issue edit 123 --title "New Title" --body-file update.md
	  
	  # Add markdown file content as a comment
	  gh issue comment 123 --body-file comment.md
	  ~~~