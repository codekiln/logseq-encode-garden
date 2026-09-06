logseq-entity:: [[Logseq/Entity/Question]]
- # How does the picker split the phrase from the extra `rg` arguments?
	- ## [[AI Answer]]
		- The [[nvim/Plugin/snacks.nvim/Picker]] grep source parses the picker's input for the literal separator ` -- `. Text before the separator becomes the search pattern; text after it is tokenized (respecting quotes) and appended to the `rg` command as additional arguments, alongside flags such as [[rg/-g]] and `-t` that the picker also sets from its own options.
