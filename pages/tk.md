alias:: [[ticket]]
tags:: [[Task/Management/Git-Friendly]]

- [wedow/ticket: Fast, powerful, git-native ticket tracking in a single bash script. Dependency graphs, priority levels, zero setup.](https://github.com/wedow/ticket)
  title:: tk
	- The git-backed issue tracker for AI agents. Rooted in the Unix Philosophy, `tk` is inspired by Joe Armstrong's [Minimal Viable Program](https://joearms.github.io/published/2014-06-25-minimal-viable-program.html) with additional quality of life features for managing and querying against complex issue dependency graphs.
	- `tk` was written as a full replacement for  [[Beads]]. It shares many similar commands but without the need for keeping a [[SQLite]] in sync or a rogue background daemon mangling your changes. It ships with a `migrate-beads` command to make this a smooth transition.
	- there's even a "migrating from beads" section with a [[Beads]] [uninstall script](https://gist.github.com/banteg/1a539b88b3c8945cd71e4b958f319d8d)