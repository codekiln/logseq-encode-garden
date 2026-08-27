# Can [[CursorAI/CLI]] (cursor-agent) accept image input? If so, how?
	- ## My Notes
		- Tested it this morning in my beans log entry (see the garden for [[Person/codekiln/GitHub/beans]]); it worked just fine. I pointed the CLI to a path to the image on my machine prepended with the `@` symbol.
		- One of the [[Frustrations]] I've encountered with it is the friction with using [[MacOS/Screenshot]]s, which, these days, seem to save to the Documents folder with a long filename that contains spaces, including a non-standard narrow space utf character at the end of the filename. [[CursorAI]] struggled to find an image whose absolute path had been copied from [[yazi]], and said that the image was not on disk until it wrote a python program on the fly to find it.
			- I really just wish I could paste in to the terminal the way I do with [[Claude/Code]].
				- This morning, Cursor itself told me I could drag and drop images into the cursor-agent terminal, which I haven't tested.
					- TODO try dragging images into [[CursorAI/CLI]]
	- ## Answer
		- [[AI/Response]]
			- Yes. The Cursor Agent CLI accepts image input via file paths / `@`, headless prompt paths, and (on macOS/Linux) clipboard paste.
			- **Interactive mode:** Use `@` to select files and folders (including images) to include in context. Same behavior as in the editor.
			- **Headless/print mode:** Put image file paths in the prompt. The agent reads files (including images) via tool calling and uses vision-capable models when needed.
			- **Example (headless):**
				- ~~~
				  agent -p "Analyze this image and describe what you see: ./screenshot.png"
				  ~~~
			- **Example (multiple images):**
				- ~~~
				  agent -p "Compare these two images: ./before.png ./after.png"
				  ~~~
			- Paths can be relative to the current working directory or absolute. Supported image formats include `.png`, `.jpg`, `.gif`, `.webp`, `.svg`. The agent can also read other binary/media files when you reference them in the prompt.
			- **Paste image from clipboard? (as of [[2026-08-26 Wed]])** Yes on **macOS** and **Linux**; not yet on **Windows**.
				- **How:** In an interactive `agent` / `cursor-agent` session, press **Ctrl+V** (not Cmd+V on macOS) to attach a clipboard image. Pasting a copied image *file* also resolves to the actual image.
				- **When it landed:** [Cursor CLI changelog – April 2026](https://cursor.com/docs/cli/changelog) added “Image paste shortcuts” (`Ctrl+V`); [May 7, 2026](https://cursor.com/docs/cli/changelog) added Linux clipboard paste on Wayland and X11; later entries fix drag-and-drop / macOS paste edge cases.
				- **Caveats:** Use **Ctrl+V**, not the terminal’s usual paste (Cmd+V / right-click). Some terminals or setups (Windows Terminal, WSL, SSH, tmux) may still fail or dump raw bytes — then fall back to a file path. Cursor staff (Aug 2026 forum): paste works on macOS/Linux; Windows remains a known gap with `@path` or drag-and-drop as workarounds.
				- **Other image paths still work:** `@` / file paths in interactive mode; paths in `-p` prompts; `--image` in any session (changelog, March 2026).
			- Sources:
				- [[Answer/Official]] from [Cursor CLI changelog](https://cursor.com/docs/cli/changelog) (April 2026 image paste shortcuts; May 2026 Linux clipboard; later paste/DnD fixes; March 2026 `--image`)
				- [Using Agent in CLI – Selecting context](https://cursor.com/docs/cli/using) (`@` for files; Input shortcuts page still omits Ctrl+V image paste)
				- [Pasting images from clipboard doesn’t work](https://forum.cursor.com/t/pasting-images-from-clipboard-doesnt-work/156943) (staff: Ctrl+V handler on macOS; user confirmed after update)
				- [Pasting images not work on Window cursor cli](https://forum.cursor.com/t/pasting-images-not-work-on-window-cursor-cli/154665) (staff: works on macOS/Linux; Windows not yet)
				- [Claude Code – Interactive mode](https://code.claude.com/docs/en/interactive-mode) (Ctrl+V / Alt+V image paste; similar gesture)
	- ## Related
		- [[CursorAI/CLI]]
		- [[AI/Coding/Tool/Q/How can I do fire and forget tasks in each CLI AI coding tool like Claude Code cursor-agent and codex?]]