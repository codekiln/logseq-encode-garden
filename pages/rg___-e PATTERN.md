- `-e PATTERN, --regexp=PATTERN`
	- A pattern to search for. This option can be provided multiple times, where all patterns given are searched, in addition to any patterns provided by `-f/--file`. Lines matching ==at least one of the provided patterns== are printed.  This flag can also be used when searching for patterns that start with a dash.
	  id:: 69dca805-55f5-4bad-8c83-c81495946547
	- For example, to search for the literal -foo:
		- `rg -e -foo`
	- You can also use the special -- delimiter to indicate that no more flags will be provided. Namely, the fol‐
	           lowing is equivalent to the above:
		- `rg -- -foo`
	- When `-f/--file` or `-e/--regexp` is used, then ripgrep treats all positional arguments as files or directories
	           to search.