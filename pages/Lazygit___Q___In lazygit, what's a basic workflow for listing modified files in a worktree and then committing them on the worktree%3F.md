logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Lazygit/Keyshort]]
- # In [[Lazygit]], what's a basic workflow for listing modified files in a worktree and then committing them on the worktree?
- ## Answer
	- [[AI/Response]]
		- A [[git worktree]] is just another working copy of the same repo; [[Lazygit]] always shows **that checkout's** `git status` in the **Files** panel. The basic loop is the same as in the main repo: see changed paths → stage → commit.
		- **Work directly in the worktree (simplest):** `cd` into the worktree directory and run `lazygit`. The Files panel lists modified/untracked/staged files for that path. Stage with **space** (or **a** for stage all), optionally **enter** on a file for line/hunk staging, then **c** to commit staged changes (see [Keybindings_en.md — Files](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md) and [Main panel (staging)](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md)).
		- **Stay in one lazygit instance (main repo checkout):** use the list-panel tabs — **]** / **[** cycle tabs until **Worktrees** is selected — pick the worktree and **switch** into it (lazygit rebinds the session to that worktree). Then open the **Files** panel again; it now reflects that worktree's working tree. Stage and **c** to commit as above. The dedicated **Worktrees** bindings (e.g. **n** new, remove **d**) are documented in the same [Worktrees](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md) section. Creating a worktree from a branch is also described under [Worktrees in the README](https://github.com/jesseduffield/lazygit#worktrees) (e.g. worktree options from the branches view).
		- **Filter / refresh:** **/** filters the current side panel; **R** refreshes git state if the list looks stale ([global keybindings](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md)).
- ## My Notes
	- *placeholder*
