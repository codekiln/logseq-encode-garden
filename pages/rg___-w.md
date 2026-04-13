alias:: [[rg/--word-regexp]]

- `-w, --word-regexp`
	- When enabled, ripgrep will only show matches surrounded by word boundaries. This is equivalent to surrounding every pattern with `\b{start-half}` and `\b{end-half}`.
	- This overrides the `-x/--line-regexp` flag.
	- Option text matches `rg --help` / `man rg` (see [[rg/manpage]]).
