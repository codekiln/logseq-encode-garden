logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Zsh/Init/File]]

- # What is the idiomatic way to add the [[Obsidian]] CLI to [[PATH]] via [[chezmoi]] dotfiles, and install [[Obsidian]] in a [[Brewfile]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Add `cask "obsidian"` to a `run_onchange_before_install-packages-darwin.sh.tmpl` heredoc script (the chezmoi-idiomatic package-install pattern), and export the [[PATH]] entry in `dot_zprofile.tmpl` with a macOS template guard.
			- **Brewfile / package installation:**
				- The idiomatic [[chezmoi]] pattern for [[Homebrew]] is an inline heredoc inside a `run_onchange_` script, not a standalone `Brewfile`. chezmoi only re-runs the script when its content changes, avoiding redundant `brew bundle` runs on every `chezmoi apply`.
				- File: `~/.local/share/chezmoi/run_onchange_before_install-packages-darwin.sh.tmpl`
					- ~~~bash
					  {{- if eq .chezmoi.os "darwin" -}}
					  #!/bin/bash
					  brew bundle --no-lock --file=/dev/stdin <<EOF
					  cask "obsidian"
					  EOF
					  {{- end }}
					  ~~~
				- [[Obsidian]] is a **cask** (GUI macOS app), not a formula — `cask "obsidian"` is the correct entry.
			- **PATH addition:**
				- [[Obsidian]]'s settings can add `/Applications/Obsidian.app/Contents/MacOS` to [[PATH]] to expose the `obsidian` CLI binary. To manage this in [[chezmoi]], add the export to `dot_zprofile.tmpl`.
				- Prefer `dot_zprofile` over `dot_zshrc` for macOS [[PATH]] additions: `.zprofile` loads after `/etc/zprofile` (which runs `path_helper`), so additions here survive macOS's built-in path reordering; `.zshrc` is for interactive aliases, not login-shell [[PATH]].
				- File: `~/.local/share/chezmoi/dot_zprofile.tmpl`
					- ~~~zsh
					  {{- if eq .chezmoi.os "darwin" }}
					  export PATH="/Applications/Obsidian.app/Contents/MacOS:$PATH"
					  {{- end }}
					  ~~~
				- Use `.tmpl` only if the file has machine- or OS-varying content. If macOS-only, a plain `dot_zprofile` with a hardcoded export line works equally well.
			- Sources: [chezmoi macOS guide](https://www.chezmoi.io/user-guide/machines/macos/) · [chezmoi: use scripts](https://www.chezmoi.io/user-guide/use-scripts-to-perform-actions/) · [Homebrew cask: obsidian](https://formulae.brew.sh/cask/obsidian)
