logseq-entity:: [[Logseq/Entity/Keyshort]], [[Logseq/Entity/Card]]

- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]]
	- **Open Lazygit** [[Card]]
		- Description:
			- Open **[[Lazygit]]** in a floating window rooted at the **git root**. The uppercase variant opens it at the **current working directory**. The mappings are available when the `lazygit` binary is on `PATH`.
		- Shortcut:
			- `<leader>gg` — git root
				- [[Mnemonic]]
					- git GUI
					- ==g==it ==g==UI
					- `<leader>gg`
			- `<leader>gG` — current working directory
				- [[Mnemonic]]
					- git GUI, current working directory variant
					- ==g==it ==G==UI — uppercase for the current working directory
					- `<leader>gG`
	- **Git Status Picker** [[Card]]
		- Description:
			- Pick from **changed files**, with a **diff preview** for each file.
		- Shortcut: `<leader>gs`
			- [[Mnemonic]]
				- git status
				- ==g==it ==s==tatus
				- `<leader>gs`
	- **History of the Current File** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T09:53:46.027Z
	  card-last-score:: 1
		- Description:
			- Open the git commit log filtered to the **file** in the current buffer — the "how did this line get here" view.
		- Shortcut: `<leader>gf`
			- [[Mnemonic]]
				- git file
				- ==g==it ==f==ile
				- `<leader>gf`
	- How to 1.) Git Log for the repository, and 2.) open the [[git/log]] for the current directory? [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T09:57:16.272Z
	  card-last-score:: 1
		- Description:
			- Open the **commit log** for the repository. The uppercase variant scopes the log to the **current working directory**.
		- Shortcut:
			- `<leader>gl` — repository
				- [[Mnemonic]]
					- git log
					- ==g==it ==l==og
					- `<leader>gl`
			- `<leader>gL` — current working directory
				- [[Mnemonic]]
					- git log, current working directory variant
					- ==g==it ==L==og — uppercase for the current working directory
						- [[LazyVim/Keyshort/Git/Q/Is <leader>gL's current working directory the internal :pwd, or the directory LazyVim was started in?]]
						  id:: 6a9d387e-e656-49ac-aa99-b1a61ba23b30
					- `<leader>gL`
	- **Blame the Current Line** [[Card]]
		- Description:
			- Show the **commit that last touched the current line**, with an option to open the **full diff**.
		- Shortcut: `<leader>gb`
			- [[Mnemonic]]
				- git blame
				- ==g==it ==b==lame
				- `<leader>gb`
	- **1. Open in browser or 2. Copy the Remote URL to the Forge (GitLab, GitHub, etc) for the current file and line range** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:46:17.979Z
	  card-last-score:: 1
		- Description:
			- Build the **remote forge URL** aka GitHub or GitLab for the **current file and line range**, then **open it in the browser** or **copy it to the clipboard**. Visual mode pins the selected line range.
		- Shortcut:
			- `<leader>gB` — open in the browser
				- [[Mnemonic]]
					- git browse
					- ==g==it ==B==rowse
					- `<leader>gB`
			- `<leader>gY` — copy to the clipboard
				- [[Mnemonic]]
					- git yank
					- ==g==it ==Y==ank
					- `<leader>gY`
		- [[My Notes]]
			- Very useful! unfortunately, `<leader>gB` opens markdown files with a link like https://github.com/codekiln/logseq-encode-garden/blob/main/pages/LazyVim___Keyshort___Git.md#L6-L6, which doesn't activate the "code" mode needed to highlight the range. It would need to be something like https://github.com/codekiln/logseq-encode-garden/blob/main/pages/LazyVim___Keyshort___Git.md?plain=1#L6-L7 to work "correctly.
				- TODO consider filing an issue in my dotfiles to fix this for me - all md file visual selections should link to the version that's going to highlight correctly.
	- [[My Note]]
		- These are pickers over git data; the interactive staging and committing workflow lives in [[Lazygit]] behind `<leader>gg`.
		- Hunk-level staging inside the buffer comes from [[nvim/Plugin/gitsigns.nvim]] on the `<leader>gh` group, not from these keys.
		- A general LazyVim cheat sheet may list `<leader>gc` for commit search and `<leader>ge` for a Neotree git explorer; neither exists here — those belong to the fzf-lua and neo-tree extras (see [[LazyVim/Keyshort/Explorer]]).