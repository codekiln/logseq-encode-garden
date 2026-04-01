logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-03-28 Sat]]

- # How can I preview PDFs in [[yazi]]?
	- ## Answer
		- [[AI/Response]]
			- [[yazi]] ships a built-in **`pdf` previewer** in the `[plugin]` section: it renders PDFs via **`pdftoppm`** (Poppler) and shows pages in the preview column through the same image pipeline as other previews.
			- **Prerequisites:** install **Poppler** so `pdftoppm` is on your `PATH` (on macOS, common options are **Homebrew** `brew install poppler` or a Poppler build your package manager provides). If the preview is empty or errors, missing Poppler is the first thing to check.
			- **Terminal / emulator:** inline image previews need a terminal that supports Yazi’s image protocols (see notes in this graph on [[Ghostty]], [[Kitty]], [[WezTerm]], etc.). Without that, you may still get text fallbacks or blank previews depending on the file type.
			- **Configuration references:** built-in previewers are listed under **`[plugin]` → previewers** in [yazi.toml | Yazi](https://yazi-rs.github.io/docs/configuration/yazi/#plugin); the **`pdf`** plugin is described there as bridging **`pdftoppm`** and the preview. **`[preview] max_width` / `max_height`** cap decoded image size (run `yazi --clear-cache` after changing them).
			- **Open externally:** use **`open`** (or your `[opener]` rules) if you prefer a dedicated PDF app regardless of preview.
	- ## My Notes
		- *placeholder*
