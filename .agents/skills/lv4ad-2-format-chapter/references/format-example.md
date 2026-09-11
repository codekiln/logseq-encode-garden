# Worked example: Chapter 1 after formatting (before link enrichment)

This is the target shape produced by `lv4ad-2-format-chapter`, using LV4AD
Chapter 1 as the concrete example. Note there are **no entity wikilinks yet**
beyond what was already in the raw highlight text (e.g. inline code like
`ed`) — those come from `lv4ad-3-enrich-links`.

```
readwise-link:: https://read.readwise.io/read/01m207ez76jh7f9fb9z5q1wq6a

- # [Chapter 1: Introduction and Installation - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/)
	- ## 1.1 Why Vim
		- > You may also be familiar with another iteration of `ed` called `sed`, the "stream editor." To this day it is still used for modifying text in a shell pipeline.
			- [[My Note]] *Wow, I didn't know the ed -> sed history. Cool.*
		- > The `ed` command was also **ex**tended to create another line editor called `ex`, which isn't really used anymore, except (extensively) as a submode of Vim.
			- [[My Note]] *I love the historical roots of vim.*
		- > This is the big one for me. I used Vim a lot through my early career...
			- [[My Note]] *I never thought about modal editing as a way to prevent RSI before...*
	- ## [1.3 Introducing LazyVim](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/#_introducing_lazyvim)
		- > To be clear, LazyVim is Vim. The editing experience is identical...
			- [[My Note]] *I'm heartened to hear this pain-point acknowledged...*
		- > you will find that it's extremely well thought-out
			- [[My Note]] *Yes, this is exactly what I want to hear.*
	- ## [1.6 Install Neovim](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/#_install_neovim)
		- > Neovim development happens at a super fast pace compared to their release cycle...
		- > If you want to live on the edge, `brew install --HEAD neovim` will install the latest nightly version of Neovim...
		- > If you want to, you can run the command `<Escape>:Tutor<Enter>` to open an interactive text file...
		- #### [1.8.2. Install Other Recommended Dependencies](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/#_install_other_recommended_dependencies)
			- > I strongly recommend installing `lazygit`, `ripgrep` and `fd`...
		- > You may see it compile and install a bunch of treesitter grammars...
			- [[My Note]] *This is discussing the LazyVim menu*
		- > You can access this UI from the dashboard simply by pressing the `l` key...
		- > Typically, the only Lazy.nvim keybinding I use is `S`, for `Sync`...
		- id:: 6aa19602-3f9f-42cf-a7f9-1b41a8fd0aaf
		  > you can find my own dot files on GitHub in the dusty-phillips/dotfiles repository.
```

## Notes on this shape

- Heading numbers/titles come straight from the site's own TOC; headings that
  have their own URL anchor become links, others stay plain text.
- Sub-headings (`####`) nest under their parent `##`/`###` exactly as they do
  on the source site — don't flatten or renumber them.
- A highlight with no personal annotation has no child bullet at all.
- Multi-paragraph highlights keep their original paragraph breaks inside the
  same blockquote bullet (a blank line inside the bullet's block, still
  indented, per LFM quoting conventions) rather than being split into
  separate highlight bullets.
- The `id::` line stays glued to the bullet it was already on; it is not
  something this skill invents — it only gets preserved if the source page
  already had one.
