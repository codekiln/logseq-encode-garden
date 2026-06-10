logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/CLI]], [[Obsidian/Q/What Obsidian keyboard shortcuts are most useful for pointing to pages and headings when working with external agentic coding tools like Claude Code?]]

- # Does a [[CLI]] for [[Obsidian]] exist, and if so, can it quickly generate references like wikilinks to pages and headings? [[card]]
	- ## [[My Answer]]
		- [[Obsidian/CLI/file]] has the ability
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
			- **`rjzxvi/obsidian-vault-cli`** (GitHub) — 100+ commands; includes link operations and note management without needing the Obsidian app running.
			- **`davidpp/obsidian-cli`** — AI-optimized with a REST API mode; designed for agentic tools like [[Claude Code]].
			- **`nightisyang/obsidian-cli`** — headless-first with ripgrep search and a backlink index; no running app required.
		- ### Sources
			- [Obsidian Help — CLI](https://obsidian.md/help/cli)
			- [DEV.to — Obsidian's Official CLI Is Here](https://dev.to/shimo4228/obsidians-official-cli-is-here-no-more-hacking-your-vault-from-the-back-door-3123)
			- [GitHub — rjzxvi/obsidian-vault-cli](https://github.com/rjzxui/obsidian-vault-cli)
			- [GitHub — davidpp/obsidian-cli](https://github.com/davidpp/obsidian-cli)
			- [GitHub — nightisyang/obsidian-cli](https://github.com/nightisyang/obsidian-cli)