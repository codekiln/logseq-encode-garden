- I installed and tried [[GitHub/CLI/Extension/gh-dash]] and [[tuicr]] for doing a pull request review today for the first time. It was a PR opened by an agent. Unfortunately, the "Merge without waiting for requirements to be met (bypass rules)" checkbox was not accessible by gh-dash when I used its `m` to merge. `tuicr` worked okay, but it took a bit to learn. The key was the cheat sheet at https://tuicr.dev/, then using `?` for the rest. Most valuable keyshorts: `;h`, `;j`, `;l`, `;k` for navigation; `;` is the leader within `tuicr`. also `r` for toggle reviewed and `[` and `]` for prev and next hunk, as well as `CTRL-d` and `CTRL-u` for down and up half screen. I did wish that it was easier to copy from the PR description. I see the pr description  in the "Overview" but I'm not able to really copy from it. I really do wish that all programs that offered in-app help also offered in app fuzzy find and grep over keyshorts the way [[tmux]] and [[yazi]] do. this one does, but I can't do it in a case-insensitive way. I did see in the console related to [[GitHub/CLI/Extension/gh-dash]], but I didn't see how to apply the flag.
	- To have the pull request merged after all the requirements have been met, add the `--auto` flag.
	  To use administrator privileges to immediately merge the pull request, add the `--admin` flag.
	- TODO file a question: how do I do the equivalent of `Merge without waiting for requirements to be met (bypass rules)` or use `--admin` flag for [[GitHub/CLI/Extension/gh-dash]]?
	  id:: 6aa2f42e-a7ad-4d49-9aa5-e8e1607cccbf
- in [[tuicr]] - learned
	- [[tuicr/Diff View/Toggle line wrap]]
		- [[tuicr/Keyshort/:wrap]]
	- `:set noreviewed` hides files already marked reviewed.
		- the repo has good docs on keyshorts that are helpful to have up.
