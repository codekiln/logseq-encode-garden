logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[Obsidian/CLI]], [[Obsidian/Q/What Obsidian keyboard shortcuts are most useful for pointing to pages and headings when working with external agentic coding tools like Claude Code?]]

- # Can the official [[CLI]] for [[Obsidian]]  generate wikilinks to pages and headings? [[card]]
  card-last-score:: 3
  card-repeats:: 2
  card-next-schedule:: 2026-06-28T05:17:07.465Z
  card-last-interval:: 3.95
  card-ease-factor:: 2.36
  card-last-reviewed:: 2026-06-24T07:17:07.465Z
	- ## [[My Answer]]
		- CLI exists but there's **no** built-in way to generate wikilinks to pages and headings.
		- ### commands that could be scripted to do that
			- [[Obsidian/CLI/file]] lists details for a given page.
			- [[Obsidian/CLI/files]] lists all files in the vault.
			- [[Obsidian/CLI/outline]] lists headings for a file. use `format=md` to get the outline.
				- [[Example]]
					- ```
					   ~/ghq/github.com/albion-house/defend   main  obsidian outline file=2026-06-10 for
					  mat=md
					  # killbox weapons-first playtest
					  ## runs
					  ## useful pressure
					  
					  ```
	- ## [[AI Answer]]
		- **Short answer:** Yes — the official [[Obsidian/CLI]] (requires Obsidian 1.12.4+ running) gets you close, but has no single "output a wikilink" command. You combine two or three of its outputs with a shell alias in your dotfiles to produce `[[Page#Heading]]` strings.
		- ### Official Obsidian CLI (built-in, requires running app)
			- Enabled in **Settings → General → Command line interface**. See [[Obsidian/CLI]] for install notes.
			- Useful commands for generating references:
				- `obsidian file file="NoteName"` — returns file metadata including **vault-relative path**, name, and extension. Pipe with `--copy` to clipboard.
				- `obsidian outline file="NoteName"` — returns the heading tree in tree, markdown, or JSON format. Combined with `--copy`, you get all headings on the clipboard to construct `[[NoteName#Heading]]` manually.
				- `obsidian daily:path` — returns today's daily note path (useful as a reference target).
				- `--copy` — universal flag; adds clipboard output to **any** command (e.g. `obsidian outline file="NoteName" --copy`).
			- **What it cannot do natively:** there is no `obsidian wikilink file="NoteName" heading="Heading"` command that outputs `[[NoteName#Heading]]` in one step. You construct that from `file` + `outline` output in a shell alias.
		- ### Shell alias approach (dotfiles-friendly)
			- A small shell function in your `.zshrc` / `.bashrc` can wrap the CLI output into a wikilink:
				- ~~~bash
				  # copy [[NoteName]] wikilink to clipboard
				  owikilink() { echo "[[${1}]]" | pbcopy; }
				  # copy [[NoteName#Heading]] — requires knowing the heading text
				  owikilink-h() { echo "[[${1}#${2}]]" | pbcopy; }
				  ~~~
			- More robustly: `obsidian file file="$1"` gives the canonical page name; parse it and wrap in `[[ ]]`.
		- ### Community CLI alternatives
			- [`davidpp/obsidian-cli`](https://github.com/davidpp/obsidian-cli) — AI-optimized with a REST API mode; designed for agentic tools like [[Claude Code]].
				- [[My Note]]s 3 stars, typescript, funny. uses an API key to secure the localhost Obsidian server (which might be standard for obsidian)
			- [nightisyang/obsidian-cli](https://github.com/nightisyang/obsidian-cli) — headless-first with ripgrep search and a backlink index; no running app required.
				- [[My Note]] 1 star, go
		- ### Sources
			- [Obsidian Help — CLI](https://obsidian.md/help/cli)
			- [DEV.to — Obsidian's Official CLI Is Here](https://dev.to/shimo4228/obsidians-official-cli-is-here-no-more-hacking-your-vault-from-the-back-door-3123)
			- [GitHub — rjzxvi/obsidian-vault-cli](https://github.com/rjzxui/obsidian-vault-cli)
			- [GitHub — davidpp/obsidian-cli](https://github.com/davidpp/obsidian-cli)
			- [GitHub — nightisyang/obsidian-cli](https://github.com/nightisyang/obsidian-cli)