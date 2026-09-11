logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Almog Gavra]]
date-created:: [[2026/01/08]]
see-also:: [[UI/Text-based]], [[Lazygit]], [[gh-dash]], [[PiAI]]

- # [tuicr](https://tuicr.dev/)
	- Code review TUI with [[vim]] keybindings: scroll a GitHub-style continuous diff, leave line/range/file/review comments, then push a real review to GitHub, GitLab, Gitea, Bitbucket, Azure DevOps, or Gerrit — or export structured Markdown to the clipboard / stdout for an agent.
	- Pronounced "tweaker."
	- [agavra/tuicr](https://github.com/agavra/tuicr) — [[GitHub/Star]]: 3,088 (checked 2026-09-10). MIT.
	- Written in [[Rust]].
	- Works with [[git]], [[jj-vcs]], and [[mercurial]]; reviews uncommitted changes, commit ranges, or remote PRs/MRs.
	- Ships an agent skill so tools like [[PiAI]] can discover active review sessions, read human comments, and add agent-authored inline comments rather than a free-floating summary.
	- wishlist
		- [[tuicr/Wishlist]]
	- ## Coverage
		- [[Person/Omer Hamerman/YouTube/26/07/The Holy Grail of Code Review TUIs]] — DevOps Toolbox walkthrough of local review, GitHub submit, [[gh-dash]] integration, and the [[PiAI]] skill.