# Can [[CursorAI/CLI]] (cursor-agent) accept image input? If so, how?
	- ## My Notes
		- Tested it this morning in my beans log entry (see the garden for [[Person/codekiln/GitHub/beans]]); it worked just fine. I pointed the CLI to a path to the image on my machine prepended with the `@` symbol.
		- One of the [[Frustrations]] I've encountered with it is the friction with using [[MacOS/Screenshot]]s, which, these days, seem to save to the Documents folder with a long filename that contains spaces, including a non-standard narrow space utf character at the end of the filename. [[CursorAI]] struggled to find an image whose absolute path had been copied from [[yazi]], and said that the image was not on disk until it wrote a python program on the fly to find it.
			- I really just wish I could paste in to the terminal the way I do with [[Claude Code]].
				- This morning, Cursor itself told me I could drag and drop images into the cursor-agent terminal, which I haven't tested.
					- TODO try dragging images into [[CursorAI/CLI]]
	- ## Answer
		- [[AI/Response]]
			- Yes. The Cursor Agent CLI accepts image input in two ways:
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
			- **Paste image from clipboard?** No. The Cursor Agent CLI does not support pasting an image directly from the clipboard (unlike the Cursor GUI, and unlike [[Claude Code]] CLI, which supports e.g. Ctrl+V on macOS / Alt+V on Windows to paste an image). For cursor-agent at the terminal you have to put the image in a file and reference it (e.g. `@/path/to/image.png` in interactive mode, or include the path in your prompt in headless mode). There is no documented shortcut or paste action for images in the CLI.
			- Sources:
				- [Using Agent in CLI – Selecting context](https://cursor.com/docs/cli/using) (interactive `@`; input shortcuts do not mention image paste)
				- [Using Headless CLI – Working with images](https://cursor.com/docs/cli/headless) (file paths in prompts, examples)
				- [Claude Code – Interactive mode](https://code.claude.com/docs/en/interactive-mode) (image paste via Ctrl+V / Alt+V; contrast with cursor-agent)
	- ## Related
		- [[CursorAI/CLI]]
		- [[AI/Coding/Tool/Q/How can I do fire and forget tasks in each CLI AI coding tool like Claude Code cursor-agent and codex?]]