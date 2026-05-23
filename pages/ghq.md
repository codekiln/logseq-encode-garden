logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Hironao OTSUBO]]
alias:: [[Person/Hironao OTSUBO/GitHub/ghq]]
tags:: [[CLI/Tool]], [[Go]]

- # [ghq](https://github.com/x-motemen/ghq)
	- Go CLI that clones and organizes remote Git repositories under a predictable directory layout (“remote repository management made easy”).
	- Configuration lives in [[git/.gitconfig]] (`ghq.root`, host-specific paths, etc.) rather than a separate project config file.
	- Installable via [[Brew]] (`brew "ghq"`); listed in [[Person/lv416e/GitHub/dotfiles]] [dot_Brewfile.tmpl](https://github.com/lv416e/dotfiles/blob/main/dot_Brewfile.tmpl#L79).
	- ## Related
		- [[Person/codekiln/GitHub/sourcer]] — similar problem space (canonical clone paths, `get` / list workflows); sourcer was not published after finding ghq. ghq is Go and git-config-driven; sourcer sketches were Rust with an explicit allow-list config file.