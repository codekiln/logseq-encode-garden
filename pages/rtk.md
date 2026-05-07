alias:: [[rtk-ai/rtk]]
logseq-entity:: [[Logseq/Entity/software-project]]
tags:: [[CLI/Tool]]
via:: https://github.com/chriskrycho/dotfiles/blob/main/tasks/setup/rtk.sh

- # [rtk](https://github.com/rtk-ai/rtk)
	- CLI proxy aimed at lowering LLM token use on common development commands (the project cites about 60–90% reduction in typical cases). One Rust binary, no extra runtime dependencies.
	- ## Links
		- [GitHub](https://github.com/rtk-ai/rtk)
	- ## Setup reference
		- [[Person/Chris Krycho/GitHub/dotfiles]] wire this up for Claude Code with mise: once `rtk` is on `PATH`, the setup task runs `rtk init -g` ([tasks/setup/rtk.sh](https://github.com/chriskrycho/dotfiles/blob/main/tasks/setup/rtk.sh)).
