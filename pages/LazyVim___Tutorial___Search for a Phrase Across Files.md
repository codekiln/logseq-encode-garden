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
		- ### How do we know that [[rg]] is used for search in [[LazyVim]]?
		  id:: 6a994fbb-4d17-4176-ae71-3bcb558ed04d
		  collapsed:: true
			- LazyVim maps `<leader>/` to `LazyVim.pick("grep")`. This setup registers [[nvim/Plugin/snacks.nvim/Picker]] as LazyVim's picker, and that picker's grep source builds the search command with `cmd = "rg"`.
			- Run `:checkhealth lazyvim` inside Neovim to verify that `rg` is installed and available. [[LazyVim/Q/Does LazyVim integrate with rg?]] links to the source and describes the other searches backed by `rg`.
	- ## Treat Punctuation as Ordinary Text
	  id:: 6a994d3e-1a16-4bab-9a08-ceaee29778da
		- Press `<leader>/` to open another repository search.
		- Press `<Alt-r>` to turn off regular-expression matching, then type `tags:: [[Diataxis/Tutorial]]`.
		- The results include tutorial pages whose frontmatter contains that complete text. With regular expressions turned off, characters such as `[` and `]` are matched literally.
		- Press `<Alt-r>` again when a search needs regular-expression syntax.
		- ### Why does searching for `tags:: [[Diataxis/Tutorial]]` require turning off [[Regex]] matching in [[rg]]? [[Question/My]]
			- [[Answer/AI]]
				- In a regular expression, square brackets delimit a [[Regex/Character Class]], which matches one character from a set. Rust's regex engine permits nested classes, so `[[Diataxis/Tutorial]]` is parsed as an outer class containing the inner class `[Diataxis/Tutorial]`. The brackets are syntax; they consume no text.
				- The nested class consumes one of the letters in `Diataxis/Tutorial`, or `/`. Because `T` is one of those letters, `tags:: ` followed by `T` satisfies the complete regex. `rg` looks for a matching substring, so the rest of the line does not have to match.
				- Pressing `<Alt-r>` turns off regex matching. The [[nvim/Plugin/snacks.nvim/Picker]] then runs `rg` with `--fixed-strings`, so every bracket, slash, and letter in `tags:: [[Diataxis/Tutorial]]` must appear in that order.
		- ### What does the `R` indicate in the title of the `Grep` dialog? [[Question/My]]
			- `<leader>/` opens a grep dialog. By default, there is no `R` in the title. After pressing `<Alt-r>` once, an `R` appears in the dialog title. What's a good way to remember what `R` represents in the dialog title?
			- [[Answer/AI]]
				- `R` marks the regex toggle's non-default state: regex matching is off, so the search is using fixed strings. The [[nvim/Plugin/snacks.nvim/Picker]] is configured to show the badge when its `regex` option is `false`.
				- A useful reminder is **`R` visible → read the text literally**. Press `<Alt-r>` again and the `R` disappears as regex matching returns.
	- ## Search Only the Current Directory
		- Run `:cd pages`, followed by `:pwd`. Neovim's current directory now ends in `/pages` while the Git root remains the garden's top directory.
		- Press `<leader>sG`; the uppercase `G` chooses the current-directory form of the grep picker.
		- Type `Fuzzy file picker scoped to the detected root`.
		- The results include `LazyVim___Keyshort___Search.md` under `pages/`. Files outside `pages/` are outside this search.
		- Run `:cd ..` when you want Neovim's current directory to be the repository root again.
	- ## Include Hidden or Ignored Files
		- Open either grep picker and enter the phrase first.
		- Press `<Alt-h>` to include hidden files. The picker reruns the search with hidden files enabled.
		- Press `<Alt-i>` to include files excluded by ignore rules. The picker reruns the search without applying those rules.
		- Press either key again to return to the usual project search.
	- ## What You've Learned
		- `<leader>/` and `<leader>sg` search the detected project root; in a Git repository, that is the Git root.
		- `<leader>sG` searches Neovim's current working directory, which `:pwd` displays and `:cd` changes.
		- A phrase containing spaces is one contiguous `rg` pattern. `<Alt-r>` makes punctuation literal, while `<Alt-h>` and `<Alt-i>` broaden which files are searched.
		- Enter opens the selected match at the matching line.
