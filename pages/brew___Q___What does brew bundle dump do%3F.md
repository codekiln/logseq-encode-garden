logseq-entity:: [[Logseq/Entity/Question]]

- # What does `brew bundle dump` do?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Homebrew Bundle README](https://github.com/Homebrew/homebrew-bundle)
		- Short answer: it writes the current machine's installed state (taps, formulae, casks, and other supported package managers) out to a [[brew/file]], so that state can be captured, version-controlled, and diffed over time.
		- By default it writes `./Brewfile` in the current directory, or a custom path via `--file` (`--file=-` pipes to stdout/stdin).
		- What it dumps, by default: taps, formulae (`brew`), and casks (`cask`). Each of these can be toggled independently with `--formula`/`--no-formula`, `--cask`/`--no-cask`, `--tap`/`--no-tap`.
		- It can also dump entries for several other package managers if present, each gated by a `--no-dump-<manager>` flag (or the matching `HOMEBREW_BUNDLE_DUMP_NO_*` env var): `mas` (Mac App Store), `whalebrew`, `vscode` extensions, Flatpak, WinGet, Krew plugins, and npm packages.
		- `--describe` (default on) adds a comment above each entry describing the package; `--no-describe` omits those comments.
		- `-f`/`--force` overwrites an existing Brewfile at the target path instead of erroring.
		- `--global` reads/writes the global Brewfile location (`$HOMEBREW_BUNDLE_FILE_GLOBAL`, `$XDG_CONFIG_HOME/homebrew/Brewfile`, or `~/.Brewfile`) instead of the current directory's.
		- `--install` runs `brew bundle install` first, so the dump reflects the post-install state.
		- It is effectively the inverse of `brew bundle` (a.k.a. `brew bundle install`), which reads a Brewfile and installs/updates the system to match it — `dump` goes system → Brewfile, `install` goes Brewfile → system.
