alias:: [[Obsidian CLI]], [[obsidian-cli]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
- # [Obsidian CLI](https://obsidian.md/help/cli#Install+Obsidian+CLI)
	- Official `obsidian` [[CLI/Tool]] for scripting, automation, and integration with external tools from the terminal.
	- Supports both one-shot commands and an interactive terminal interface with help, autocomplete, command history, and reverse search.
	- Requires the Obsidian 1.12.7+ installer and a running Obsidian app; installation starts by enabling **Command line interface** in **Settings -> General**.
	- ## Key commands for generating references
		- `obsidian file file="NoteName"` — returns vault-relative path, name, and extension; useful for handing a file reference to external tools like [[Claude Code]].
		- `obsidian outline file="NoteName"` — returns the heading tree (tree / markdown / JSON format); use to identify heading anchors for `[[NoteName#Heading]]` links.
		- `--copy` — universal flag; copies the output of **any** command to the system clipboard (e.g. `obsidian outline file="NoteName" --copy`).
		- `obsidian daily:path` — returns the expected path for today's daily note.
		- `obsidian links file="NoteName"` / `obsidian backlinks file="NoteName"` — outgoing and incoming link lists.
	- ## Community / headless alternatives
		- These work without a running Obsidian app:
		- **[nightisyang/obsidian-cli](https://github.com/nightisyang/obsidian-cli)** — headless-first; ripgrep search, backlink index, optional REST API mode.
		- **[davidpp/obsidian-cli](https://github.com/davidpp/obsidian-cli)** — AI-optimized with REST API; designed for agentic tools like [[Claude Code]].
		- **[rjzxui/obsidian-vault-cli](https://github.com/rjzxui/obsidian-vault-cli)** — 100+ commands covering note lifecycle and link operations.
