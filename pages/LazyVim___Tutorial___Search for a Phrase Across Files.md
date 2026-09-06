tags:: [[Diataxis/Tutorial]]
see-also:: [[LazyVim/Keyshort/Search]], [[nvim/Plugin/snacks.nvim/Picker]], [[rg]]

- # Tutorial: Search for a Phrase Across Files in [[LazyVim]]
	- ## What You'll Do
		- We will search this garden for a phrase that appears on one line of a file. We will search the whole Git repository, narrow the search to Neovim's current directory, treat punctuation as ordinary text, and include hidden or ignored files when needed.
	- ## Before You Start
		- Use this garden's current [[LazyVim]] setup, where the [[nvim/Plugin/snacks.nvim/Picker]] runs searches with [[rg]].
		- `<leader>` is the Space key.
		- Run `:checkhealth lazyvim` if the picker reports that `rg` is unavailable.
	- ## Open the Garden at Its Git Root
		- From a shell, open the garden from the path registered with `ghq`:
			- ~~~bash
			  cd "$(ghq list --full-path --exact github.com/codekiln/logseq-encode-garden)"
			  nvim .
			  ~~~
		- Run `:pwd` in LazyVim. You will see the garden's repository root.
	- ## Search the Whole Repository
		- Press `<leader>/`. `<leader>sg` opens the same repository-root search on a mnemonic key sequence.
		- Type `the garden's rulesync targets` into the picker without quotation marks.
		- The results update while you type. The list includes `README.md`, where the complete phrase occurs on one line. This tutorial also appears because it contains the exercise phrase.
		- Move to the `README.md` result with `<C-j>` and `<C-k>` or the arrow keys, then press Enter. LazyVim opens the file **with the cursor on the match**.
		- Notice that the spaces stay inside one search pattern. Quotation marks are unnecessary; typing them would ask `rg` to find quotation-mark characters in the file.
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/How do we know that rg is used for search in LazyVim?]]
		  id:: 6a994fbb-4d17-4176-ae71-3bcb558ed04d
	- ## Treat Punctuation as Ordinary Text
	  id:: 6a994d3e-1a16-4bab-9a08-ceaee29778da
		- Press `<leader>/` to open another repository search.
		- Press `<Alt-r>` to turn off regular-expression matching, then type `tags:: [[Diataxis/Tutorial]]`.
		- The results include tutorial pages whose frontmatter contains that complete text. With regular expressions turned off, characters such as `[` and `]` are matched literally.
		- Press `<Alt-r>` again when a search needs regular-expression syntax.
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/Why does searching for the tags line for Diataxis Tutorial require turning off Regex matching in rg?]]
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/What does the R indicate in the title of the Grep dialog?]]
	- ## Search Only the Current Directory
		- Run `:cd pages`. Neovim's current directory now ends in `/pages` while the Git root remains the garden's top directory. A floating `Messages` notification reports the new path.
		  id:: 6a994d3e-fabf-4abb-a27e-6e8aacbc0e45
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/Why does cd pages show a Messages notification but pwd shows nothing visible?]]
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/Are cd and pwd built-in vim commands that do something different than the shell version of cd and pwd?]]
		  id:: 6a9c2a08-7019-4504-a4ca-c05f7a810902
		- Press `<leader>sG`; the uppercase `G` chooses the current-directory form of the grep picker.
		- Type `Fuzzy file picker scoped to the detected root`.
		- The results include `LazyVim___Keyshort___Search.md` under `pages/`. Files outside `pages/` are outside this search.
		- Run `:cd ..` when you want Neovim's current directory to be the repository root again.
		  id:: 6a994d3e-12ff-4233-a32d-dfb810b7175c
			- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/Is there a command to cd back to the original directory nvim was launched with, or do you need to remember where you are and use relative directory navigation?]]
	- ## Restrict the Search to One File Extension
		- Press `<leader>/` to open a repository search.
		- Type `garden -- -g=*.md`. Everything before ` -- ` is the search phrase; everything after it is passed to `rg` as extra arguments, here the [[rg/-g]] flag.
		- The results are limited to files whose name matches `*.md`, so files such as `mise.toml` or `.gitignore` no longer appear even if they contain the word `garden`.
		- `-t md` works the same way: `garden -- -t md` restricts the search to `rg`'s built-in Markdown file type, which already covers `.md`, `.markdown`, `.mdx`, and related extensions.
		- [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/How does the picker split the phrase from the extra rg arguments?]]
	- ## Include Hidden or Ignored Files
		- Open either grep picker and enter the phrase first.
		- Press `<Alt-h>` to include hidden files. The picker reruns the search with hidden files enabled.
		- Press `<Alt-i>` to include files excluded by ignore rules. The picker reruns the search without applying those rules.
		- Press either key again to return to the usual project search.
	- ## What You've Learned
		- `<leader>/` and `<leader>sg` search the detected project root; in a Git repository, that is the Git root.
		- `<leader>sG` searches Neovim's current working directory, which `:pwd` displays and `:cd` changes.
		- A phrase containing spaces is one contiguous `rg` pattern. `<Alt-r>` makes punctuation literal, while `<Alt-h>` and `<Alt-i>` broaden which files are searched.
		- Typing ` -- ` after the phrase, followed by flags such as `-g=*.md` or `-t md`, restricts a search to one file extension or type.
		- Enter opens the selected match at the matching line.