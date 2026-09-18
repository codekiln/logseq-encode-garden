# Worked examples: target shape after formatting (before link enrichment)

These are the target shapes produced by `lv4ad-2-format-chapter`. Entity
wikilinks beyond inline code in the raw highlight text come from
`lv4ad-3-enrich-links`.

## Chapter 1 (basic shape)

```
readwise-link:: https://read.readwise.io/read/01m207ez76jh7f9fb9z5q1wq6a

- # [Chapter 1: Introduction and Installation - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/)
	- ## 1.1 Why Vim
		- > You may also be familiar with another iteration of `ed` called `sed`, the "stream editor." To this day it is still used for modifying text in a shell pipeline.
			- [[My Note]] *Wow, I didn't know the ed -> sed history. Cool.*
		- > The `ed` command was also **ex**tended to create another line editor called `ex`, which isn't really used anymore, except (extensively) as a submode of Vim.
			- [[My Note]] *I love the historical roots of vim.*
	- ## [1.3 Introducing LazyVim](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/#_introducing_lazyvim)
		- > To be clear, LazyVim is Vim. The editing experience is identical...
			- [[My Note]] *I'm heartened to hear this pain-point acknowledged...*
	- ## [1.6 Install Neovim](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/#_install_neovim)
		- > Neovim development happens at a super fast pace compared to their release cycle...
		- > If you want to live on the edge, `brew install --HEAD neovim` will install the latest nightly version of Neovim...
		- id:: 6aa19602-3f9f-42cf-a7f9-1b41a8fd0aaf
		  > you can find my own dot files on GitHub in the dusty-phillips/dotfiles repository.
```

## Chapter 5 (notes, splits, and reconstructions)

```
- # [Chapter 5: Plugin Basics - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-5/)
	- ## [5.1 Three Categories](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-5/#_the_three_categories_of_plugins_in_lazyvim)
		- > Others, such as flash.nvim and which-key.nvim provide new commands or modes to work with.
			- [[AI Notes]] *The document identifies flash.nvim as a pre-installed plugin… it generally enables:*
				- Rapid Navigation: Jumping to any visible text by typing labels.
				- Enhanced Search: Instant jumping to / search results.
				- treesitter Integration: Quickly selecting logical code blocks.
		- > As some specific examples consider these three nvim plugins for file management…
			- [[My Note]] *Some text is missing in Readwise:*
				- ### snacks.nvim Explorer
					- Snacks explorer ships with LazyVim and is active by default…
				- ### mini.files
					- ships as a Lazy Extra, and is basically a "one click" install…
	- ## [5.2 Lazy Extras](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-5/#_lazy_extras)
		- > The Lazy Extras mode can be accessed by pressing `x` from the Dashboard…
		- > ![](https://lazyvim-ambitious-devs.phillips.codes/images/book/chapter-5/lazy-extras-dark.png)
		  > lazy extras dark
		- > I've installed over a dozen extras at the moment…
		- > No matter how you get there, once your cursor is on the extra you want to install…
			- [[My Note]] *Ok so this is the answer to my question at the end of the previous chapter…*
		- > While we're in the `LazyExtras` screen, I recommend enabling the `lang.*` extras…
		- > I wouldn't install any other non-recommended extras until…
		- > You can find more information on each extra by visiting https://lazyvim.org…
	- ## [5.3 Disabling Built-in Plugin](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-5/#_disabling_a_built_in_plugin)
		- > The only LazyVim plugin I have disabled is the bufferline.nvim…
		- > First I want to give an introduction to the LazyVim configuration directory…
			- [[AI Notes]] *Yes, the dashboard is the interface you see when you first launch the editor…*
				- Specifically, the Dashboard allows you to:
					- Open the configuration directory by simply pressing the `c` key.
					- Access the Lazy Extras mode… by pressing `x`.
				- If you are already working in a file… you can show the Dashboard at any time…
		- > In reality, it's a fairly short list. To disable a plugin simply set `enabled = false`:
		  >
		  > If there are any other plugins that LazyVim enables by default…
			- [[My Note]] *Missing text:*
				- ```
				  return {
				  { "akinsho/bufferline.nvim", enabled = false },
				  }
				  ```
		- > In Lua, a table is like a combination of an array and a record or dictionary…
```

(After `lv4ad-3-enrich-links`, the `###` headings and inline mentions above
become `[[nvim/Plugin/…]]` wikilinks, and section 5.3's heading may gain a
`- [[nvim/Plugin/bufferline.nvim]]` suffix.)

## Notes on this shape

- Heading numbers/titles come straight from the site's own TOC; headings that
  have their own URL anchor become links, others stay plain text.
- Sub-headings (`###`/`####`) nest under their parent `##` exactly as they do
  on the source site — don't flatten or renumber them.
- A highlight with no personal annotation has no child bullet at all.
- **Multi-paragraph highlights become sibling blockquote bullets** — one `- >`
  per paragraph. Do not join them with blank continuation lines inside one
  bullet.
- A single blockquote bullet may still contain a **figure + caption** on
  continuation lines (`  > `) when they are one visual unit (image URL then
  alt/caption text).
- **`[[My Note]]` vs `[[AI Notes]]`:** personal reader notes (from Readwise or
  added later in Logseq) use `[[My Note]]`; Readwise built-in AI answers use
  `[[AI Notes]]` (see `readwise-note-labels.md`). Lists, sub-headings, and code
  under either label are **children** of that note bullet (one extra indent),
  not siblings of the parent highlight.
- **Readwise `---` splits:** import emits one plain child per `\n---\n`
  segment; formatting labels each (e.g. Ch. 5 `vim.uv.cwd()` → `[[My Note]]`
  then `[[AI Notes]]`; Ch. 5 `disabled.lua` → `[[My Note]]` with code, then
  book text promoted to a sibling blockquote).
- **`###` inside a note** names the missing sub-section; after link enrichment
  the heading text is the primary entity wikilink.
- The `id::` line stays glued to the bullet it was already on; it is not
  something this skill invents — it only gets preserved if the source page
  already had one.
