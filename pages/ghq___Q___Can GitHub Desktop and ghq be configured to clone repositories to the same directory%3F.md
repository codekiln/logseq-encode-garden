logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[git/.gitconfig]]
- # Can [[GitHub Desktop]] and [[ghq]] be configured to clone repositories to the same directory?
	- ## [[AI Answer]]
		- **Short answer:** not automatically — GitHub Desktop has no configurable default clone directory or awareness of `ghq.root`, but the two tools are compatible if bridged manually in each direction.
		- **ghq → GitHub Desktop:** a repo cloned with `ghq get` under ghq's `<ghq root>/<host>/<owner>/<repo>` layout can be opened in GitHub Desktop via **File → Add local repository...**, pointing at that existing folder. Desktop only needs a valid local git repo path, so it works regardless of directory layout.
		- **GitHub Desktop → ghq layout:** Desktop's clone dialog has no persistent "default root" setting — it just remembers the last path used, seeded from `~/Documents/GitHub` (`%USERPROFILE%\Documents\GitHub` on Windows). The **Local Path** field is a plain editable text/browse field, so a `<ghq root>/github.com/<owner>/<repo>` path can be typed or browsed to on each clone, and Desktop will clone there.
		- **No native integration:** Desktop does not read `ghq.root` from [[git/.gitconfig]] or otherwise auto-follow ghq's host/owner/repo convention — every Desktop-initiated clone into the ghq tree requires manually setting the path each time.
		- [[Answer/Official]] from [Cloning and forking repositories from GitHub Desktop](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
		- [Option for changing default directory missing (desktop/desktop#2889)](https://github.com/desktop/desktop/issues/2889)
