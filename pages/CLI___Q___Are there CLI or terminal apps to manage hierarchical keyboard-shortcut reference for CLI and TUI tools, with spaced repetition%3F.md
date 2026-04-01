logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Learning/Idea/26/03/Terminal toolbelt learning and Readwise-like CLI/Proto Session/26/03/25 Wed]], [[CLI/Craftsperson]], [[dotfiles]]
via:: [[2026-04-01 Wed]]

- # Are there CLI or terminal apps to manage hierarchical keyboard-shortcut reference for CLI and TUI tools, with spaced repetition?
	- Context (from [[CLI/Craftsperson|CLI craftspeople]] workflow): tools like [[Lazygit]] expose different bindings per pane and inside modals; [[nvim]] adds many custom maps in [[dotfiles]]. Looking for something versioned with dotfiles, not only [[Logseq]] Keyshort + flashcards.
	- ## Answer
		- [[AI/Response]]
			- **No single mainstream tool** appears to cover “every CLI/TUI app + hierarchical contexts + built-in SRS + auto-sync from live configs (e.g. Neovim)” end-to-end. Practical setups combine **lookup** layers (cheatsheets, generated docs) with **SRS** layers (markdown decks, Anki, or terminal drill CLIs), all kept under git in your dotfiles.
			- **Terminal-native spaced repetition (SRS)** — good when you are fine storing cards as text in the repo:
				- [[repeater]] — Rust CLI, **Markdown-first** cards (Q/A and cloze), **FSRS** scheduling, SQLite progress; cards can live beside notes so decks are git-friendly.
				- [**rep**](https://sr.ht/~reticular-flux/rep/) — minimal CLI SRS (Zig), edits in `$EDITOR`; good for plain-text cards, less “structured doc” oriented.
				- [**fla.sh**](https://github.com/tallguyjenks/fla.sh) — Bash + **fzf**, colon-separated fields in text files; lighter SRS than FSRS/Anki but very terminal-native.
			- **Hierarchical reference / execution (usually not SRS)** — strong for “pane → modal → action” style docs if you maintain the structure yourself:
				- [[navi]] — interactive cheatsheets (`.cheat` files), fzf/skim, can **pull cheats from git repos** and shell widgets; hierarchy comes from how you **split files, tags, and sections**, not from reading lazygit/nvim automatically.
				- [[cheat.sh]] / [[tldr-pages/tldr]] / [[navi]] integrations — fast lookup for **public** command docs; **won’t reflect your private Neovim maps** unless you generate or mirror content.
			- **Anki-centric path (strongest SRS ecosystem)** — keep **markdown or CSV decks in git**, sync into Anki via **AnkiConnect** and tools such as [**AnkiOps**](https://github.com/visserle/AnkiOps) (markdown ↔ Anki, optional git hooks), [**markdown-anki-decks**](https://pypi.org/project/markdown-anki-decks/), or [**@anki.md/cli**](https://www.npmjs.com/package/@anki.md/cli). Subdecks/tags give **hierarchy**; you still **author** shortcut cards (or generate stubs) yourself.
			- **Closing the “knows my Neovim config” gap** — products rarely parse your full config for flashcards. Typical pattern: **generate** reference text on demand (`:map`, `:verbose map`, help tags, or a small Lua/`nvim --headless` script that dumps bindings) and pipe that into markdown/cheat files or a deck import. Same idea for TUIs: maintain cards from each app’s **upstream keybinding doc** (e.g. lazygit’s published tables) plus **your overrides** if you wrap or alias the binary.
			- **Compared to Logseq Keyshort** — terminal tools trade graph linking for **git-native, scriptable** plain text; you gain dotfiles integration and automation at the cost of building your own hierarchy and import pipeline.
	- ## My Notes
		- Prior art in this graph: [[Learning/Idea/26/03/Terminal toolbelt learning and Readwise-like CLI/Proto Session/26/03/25 Wed]] (Readwise-like CLI learning thread); [[Lazygit/Keyshort]] style pages for per-app structure.