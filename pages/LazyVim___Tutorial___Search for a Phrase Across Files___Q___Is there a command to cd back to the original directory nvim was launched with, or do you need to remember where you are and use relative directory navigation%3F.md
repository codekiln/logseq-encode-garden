logseq-entity:: [[Logseq/Entity/Question]]
- # Is there a command to cd back to the original directory [[nvim]] was launched with, or do you need to remember where you are and use relative directory navigation?
	- ## [[AI Answer]]
		- **Short answer:** `:cd -` toggles back to the previously set directory, the same way `cd -` works in a shell, so you don't need to track relative paths yourself for a single hop.
		- `:cd -` swaps between only the **last two** directories, like a toggle rather than a stack. After one `:cd`, pressing it again returns to wherever you started.
		- After two or more `:cd` calls, `:cd -` only swaps with the immediately previous directory, not necessarily the directory Neovim launched in. Repeated presses bounce back and forth between the last two, never reaching an earlier one.
		- To reliably return to the launch directory regardless of how many times you've changed it, note it yourself at startup, for example `:let g:launch_dir = getcwd()`, then `:cd g:launch_dir` later. There is no built-in command that remembers the original launch directory beyond that one-step toggle.
