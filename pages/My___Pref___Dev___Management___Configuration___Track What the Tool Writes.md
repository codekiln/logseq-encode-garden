see-also:: [[My/Pref/Dev/Tool/Dotfiles]], [[My/Principle/Simplify/Prefer Standards and Defaults]], [[My/Pref/Dev/Management/Configuration/Comment Style]]

- # Track What the Tool Writes
	- When a tool writes its own [[Configuration File]], [[chezmoi]] tracks that file, copied byte for byte from what the tool wrote.
	- Keep the settings whose values match the tool's own defaults. A tracked copy identical to the tool's output leaves the tool nothing to change, so the two stop contending for the file.
	- Which settings I customize is a separate question, and [[My/Principle/Simplify/Prefer Standards and Defaults]] answers it: a customization is driven by "must." That governs what I edit in the file; tracking governs what the file is.
	- ## Comments
		- A tool that writes its config only when the file is missing has no later occasion to rewrite it, so a comment placed there survives and [[My/Pref/Dev/Management/Configuration/Comment Style]] applies as it does anywhere else.
		- A tool that rewrites a file it already has will strip the comment on its next run. For those, the reason for a setting lives in the commit that made the change.
	- ## What it costs
		- A tracked file holds the defaults the tool had on the day it was copied. When an upgrade changes what the tool would write, copy it again and re-apply whatever I had customized on top.
		- The file is long, and a reader cannot tell from it which lines I chose. The record of a deliberate choice is the change that made it.
	- ## Configs a tool writes while it runs
		- An editor that saves window state into the same file that holds a setting I chose keeps only that setting under management, through a script that asserts my keys and passes the rest through. A whole-file copy would go stale on the tool's next save.
	- ## [[Examples]]
		- [[GitHub/CLI/Extension/gh-dash]] writes its full defaults on first run when no config exists, so the dotfiles hold that file as gh-dash wrote it.
		- [[Lazygit]] rewrites its config on startup migrations, so the tracked copy is in the form lazygit writes and carries no comments.
