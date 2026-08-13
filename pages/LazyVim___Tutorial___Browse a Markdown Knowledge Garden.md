tags:: [[Diataxis/Tutorial]]
see-also:: [[LazyVim/Q/In LazyVim, how can I open a Markdown link with a keyboard shortcut?]], [[LazyVim/Keyshort/LSP/Navigation]], [[LazyVim/Keyshort/Search]], [[LazyVim/Keyshort/Explorer]], [[LazyVim/plugins/extras/lang/markdown]]

- # Tutorial: Browse a Markdown Knowledge Garden
	- ## Summary
		- A folder of [[Markdown]] notes becomes a navigable [[Knowledge Garden]] in [[LazyVim]] with five keys and no plugin beyond what [[LazyVim/plugins/extras/lang/markdown]] already installs. The Marksman language server turns every ordinary Markdown link into something `gd` can follow and `gr` can list backwards.
		- Every link here is the ordinary Markdown form, `[text](target)`. Obsidian-style double-bracket wiki links are out of scope here; [[LazyVim/Q/In LazyVim, how can I traverse wiki links in an Obsidian knowledge garden?]] covers those.
	- ## Before You Start
		- LazyVim with the `lang.markdown` extra enabled; `:LazyExtras` confirms it. The extra configures Marksman, and `:Mason` shows the installed version.
		- A folder of Markdown notes that link to each other with relative paths, e.g. `[Coffee](notes/coffee.md)`.
		- Leader is `<Space>`.
	- ## Learning Goals
		- Turn a plain notes folder into something the language server resolves links across.
		- Follow a link to another file, and to one heading inside it.
		- Return to where the reading started, and go forward again.
		- Reach a note by name and by content, with no link to click.
		- Read a note's incoming links.
	- ## Steps
		- ### 1. Make the folder a project
			- Marksman resolves links *across* files only inside a project, which means a [[git]] repository or any directory holding a `.marksman.toml`. Either one is enough:
			- ~~~bash
			  cd ~/notes
			  git init            # if it isn't a repository yet
			  ~~~
			- Or, with no interest in version control:
			- ~~~bash
			  cd ~/notes && touch .marksman.toml
			  ~~~
			- Notice: skipping this looks like a broken editor rather than a missing config. Without a project, Marksman still attaches to the buffer and still follows links *within* the current file — a link to another file resolves to nothing at all, with no error.
		- ### 2. Open the garden from its root
			- ~~~bash
			  cd ~/notes && nvim .
			  ~~~
			- A directory argument opens the [[nvim/Plugin/snacks.nvim]] explorer in a sidebar rather than netrw. Move to any `.md` file and press `<CR>` to open it.
			- Notice: the root is what the *pickers* need — `<leader>ff` and `<leader>/` in step 7 then search the garden instead of whatever directory the shell was sitting in. Marksman finds the project on its own by walking up from the file, so opening a single note from anywhere else still follows links. `nvim .` just gets both right in one move.
		- ### 3. Confirm the server is attached
			- With a `.md` file open, press `<leader>cl`.
			- Marksman appears in the list with the garden's root as its root directory. That root directory is the evidence step 1 worked.
			- If Marksman is missing entirely, `:Mason` shows whether the server is installed — see [[LazyVim/Keyshort/LSP/Navigation]].
		- ### 4. Follow a link with `gd`
			- Put the cursor anywhere on a link to another note — on the label or on the path, either works — and press `gd`. The target opens in the same window.
			- Three shapes worth trying, because each is a place plain `gf` gives up:
				- `[Coffee](notes/coffee.md)` — opens at the top of the file.
				- `[Roasting](notes/coffee.md#roasting)` — lands on the `## Roasting` line, not the top.
				- `[Coffee](notes/coffee)` — no extension, still resolves to `coffee.md`.
			- Notice: `gd` is go-to-definition, the same key that jumps to a function definition in code. On a Markdown buffer, a link is what "definition" means. See [[LazyVim/Keyshort/LSP/Navigation]].
		- ### 5. Come back with `<C-o>`
			- Press `<C-o>` to return to the link that was just followed, and `<C-i>` to go forward again.
			- Follow four or five links, then hold down `<C-o>`: the whole reading path unwinds in order, across files. `:ju` prints the [[vim/jump/list]] with the most recent entry at position `0`.
			- Notice: this pair is what makes `gd` cheap enough to press on any link that looks interesting — nothing is lost by looking. See [[vim/Keyshort/Jump/Back and Forward]].
		- ### 6. Send a URL to the browser with `gx`
			- Put the cursor on a link whose target is an `http` address and press `gx`. It opens in the default browser and the buffer does not move.
			- `gd` does nothing at all on a URL, and that is the entire division of labour between the two keys: `gd` stays inside the garden, `gx` leaves it. [[LazyVim/Q/In LazyVim, how can I open a Markdown link with a keyboard shortcut?]] has the full comparison, including why `gf` is the weakest of the three.
		- ### 7. Reach a note with no link to follow
			- `<leader>ff` opens a fuzzy file picker over the garden. Where the filename *is* the note's title, a few letters of the title is the fastest way in.
			- `<leader>/` greps the garden's contents, for when the title is not the part that was remembered. `<leader>sw` greps the word under the cursor.
			- `<leader>e` reopens the explorer sidebar at the root, and `<leader>sR` resumes the last picker with its query intact. See [[LazyVim/Keyshort/Search]] and [[LazyVim/Keyshort/Explorer]].
		- ### 8. Read the incoming links with `gr`
			- Open a note that other notes link to. Put the cursor on its `#` title line and press `gr`.
			- A picker lists every link in the garden pointing at this file — a backlinks panel, with no plugin involved. All three link shapes from step 4 show up, since all three resolve to the same file.
			- On a subheading line instead, `gr` narrows to the links targeting *that heading*: a `…#roasting` link appears, a bare file link does not.
			- Notice: the cursor has to be on the heading line. From a body line, `gr` returns nothing.
	- ## Verification
		- `<leader>cl` lists Marksman with the garden's root as its root directory.
		- `gd` on a `#heading` link lands on the heading line, not on line 1.
		- `gd` on an extensionless target opens the `.md` file anyway.
		- `gd` on an `http` target does nothing, while `gx` on it opens the browser.
		- `<C-o>` unwinds the last several jumps in order, across files.
		- `gr` on a note's title line lists the links that other files aim at it.
	- ## What You've Learned
		- The four keys that cover ordinary browsing: `gd` in, `<C-o>` back, `gx` out, `gr` backwards.
		- That the one piece of setup is making the folder a project — a `git init` or an empty `.marksman.toml` — and that its absence fails silently rather than loudly.
		- That the pickers (`<leader>ff`, `<leader>/`, `<leader>e`) are the other half of navigation, for the notes nothing links to yet.
	- ## Next Steps
		- Set `suffixesadd=.md` for Markdown buffers if `gf` is a long-standing habit; it is empty by default, which is why extensionless targets fail under `gf` but not under `gd`.
		- Wiki links are the next case: [[LazyVim/Q/In LazyVim, how can I traverse wiki links in an Obsidian knowledge garden?]] covers Marksman's support for them and where an [[Obsidian]]-specific plugin starts to earn its place.
