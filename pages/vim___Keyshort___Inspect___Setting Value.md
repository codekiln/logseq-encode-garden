- [[Keyshort]] [[vim/Keyshort]] [[vim/Keyshort/Inspect]]
	- **Given a Vim setting named `<option>`, inspect its current value** #card
	  card-last-score:: 5
	  card-repeats:: 4
	  card-next-schedule:: 2026-05-11T12:37:49.680Z
	  card-last-interval:: 26.21
	  card-ease-factor:: 2.56
	  card-last-reviewed:: 2026-04-15T07:37:49.680Z
		- Shortcut: `:set <option>?` (example: `:set runtimepath?`, `:set number?`)
		- **`set`** is the Ex command for **options** (Vim's internal configuration variables).
		- **`?`** means "query": always **print the option's current value**, including when it matches the default.
		- Contrast for the same option name:
			- `:set <option>=...` → **assign** a value
			- `:set <option>` alone → show only if **non-default** (for boolean options, often **toggle**)
			- `:set <option>?` → **always** show the current value
		- Boolean-style pattern: `:set number` on, `:set nonumber` off, `:set number?` reports on/off