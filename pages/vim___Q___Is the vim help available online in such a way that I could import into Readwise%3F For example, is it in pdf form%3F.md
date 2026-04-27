logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-04-27 Mon]]
see-also:: [[Readwise]]

- # Is the [[vim]] help available online in such a way that I could import into [[Readwise]]? For example, is it in PDF form?
	- ## My Notes
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** What ships with Vim as `:help` is **vimdoc** (tagged text files), not one official “full help as PDF” product from the Vim project. For [[Readwise]], the smoothest path is usually **HTML mirrors** (open in the browser → save to **Readwise Reader** → highlight). **PDF** works if you import a **compiled user manual or third-party PDF** via Readwise’s PDF import ([docs](https://docs.readwise.io/readwise/docs/importing-highlights/pdf)); those snapshots often **lag** the help that matches your exact Vim build.
			- **Web / HTML (best fit for Reader):** [Vim’s documentation hub](https://www.vim.org/docs.php) points to **[vimhelp.org](https://vimhelp.org/)** as an up-to-date, hyperlinked copy of the help files—ordinary web pages, so they behave like other long articles in Reader. For [[nvim]], the project publishes HTML docs at **[Neovim user documentation](https://neovim.io/doc/user/)**.
			- **PDF:** The same vim.org page emphasizes online help and books; it does **not** position a single canonical PDF of the entire `:help` tree as the primary distribution. Community compilations of the *Vim user manual* and older “printable help” PDFs exist here and there, but treat them as **optional snapshots**, not the live reference.
			- **Practical takeaway:** Use **vimhelp.org** (or Neovim’s doc site) for import-friendly, version-reasonable reading in Readwise’s web stack; use **PDF** only when you already have a PDF you trust and are okay maintaining versioning yourself.
