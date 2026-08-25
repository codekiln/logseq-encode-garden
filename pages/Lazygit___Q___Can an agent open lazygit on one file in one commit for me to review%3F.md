logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Lazygit/Keyshort]], [[git/worktree]]

- # Can an agent open [[Lazygit]] on one file in one commit for me to review?
- ## Answer
	- [[AI/Response]]
		- **Yes, and the flags do it. Sending keystrokes to the running program also works and is the weaker method.** Measured against lazygit 0.64.1 in a throwaway repository, never against a real checkout.
		- ### The one command that does most of it
			- ~~~sh
			  lazygit --filter 'pages/Some Page.md'
			  ~~~
			- `--filter` does four things, and `--help` describes only the first. It narrows the commit list to commits touching that path, focuses the Commits panel without being told to, puts the cursor on the newest commit touching the path, and **restricts the diff in the main panel to that path**. Measured on a commit touching three files: the main panel read `pages/Target Page.md | 3 +++` and `1 file changed`, with the other two files absent.
			- So when the commit under review is the newest one touching that file — which it is whenever the agent has just made it — the reader presses nothing. Filenames containing spaces work, given a quoted path.
		- ### For an older commit, check it out in a worktree first
			- `--filter` names a path and never names a commit, so if three commits touch the file the cursor starts on the newest rather than on the one under review. Detaching a [[git/worktree]] at the commit makes the commit under review the newest one there:
			- ~~~sh
			  git worktree add --detach /tmp/reviewwt <sha>
			  lazygit -p /tmp/reviewwt --filter 'pages/Some Page.md'
			  ~~~
			- Measured: the commit list held that one commit, the cursor was on it, and the main panel showed only that file. It also puts the reader in a detached worktree rather than in the working checkout, so a mistaken keystroke cannot reach uncommitted work.
			- `git worktree add` writes a record into the shared `.git`, so it is worth asking before running it against a checkout holding someone's uncommitted work.
		- ### Driving the program with keystrokes works, and fails silently
			- A sequence that searches by SHA rather than counting cursor movements does land on the right commit and the right file: `/` then the short SHA then Enter then Escape in the Commits panel, Enter to open the commit, then `/` and the path in the Diff files panel. Searching by SHA rather than pressing `j` a fixed number of times matters, because a new commit landing on top changes how far down the target sits.
			- **The failure is the reason to prefer the flags.** Run without waiting between keystrokes, every keystroke is swallowed while the program is still starting, and it settles on the newest commit showing a screen that looks completely healthy. Nothing errors and nothing on screen says the keys were lost, so an agent that does not read the screen back reports success while the reader is looking at the wrong commit.
			- `/` also means two different things: a cursor search in the Commits panel, which needs an Escape to leave, and a row filter in the Diff files panel, which does not.
			- In the Commits panel most other keys are live git operations — `d` drops a commit, `e` starts an interactive rebase, `A` amends, `g` opens reset options. A keystroke arriving at the wrong moment rewrites history, which is an argument against keystroke driving whatever the sequence does when it works.
		- ### Other routes, and what each is good for
			- `git show <sha> -- <path>` prints one file from one commit and nothing else, through the same diff renderer lazygit uses, so it reads the same in a pager as in the program.
			- [[nvim/Plugin/snacks.nvim]] already wraps this: its lazygit helper shells out with `--filter` on the current file, and it passes arbitrary flags through, so the worktree form works from inside [[nvim]] too. [[LazyVim]] binds plain lazygit here and does not bind the file-filtered form.
			- [[Lazygit/Command/Custom]] commands are bound to keys, and no startup hook appears in the flags or in the printed default configuration, so a custom command cannot save the first keypress. That is scoped to the flags and the configuration rather than to the program's source, which was not read.
		- ### One thing to say when handing the screen over
			- Filter mode hides the commit's other files. A commit touching three files looks like a one-file commit on that screen, so name what else it touched rather than letting the filtered view imply there was nothing else.
- ## My Notes
	- *placeholder*
