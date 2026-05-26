logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[ghq]], [[git/.gitconfig]]
- # In [[ghq]], is there a way to create a repository at a specified location?
- ## Answer
	- [[AI/Response]]
		- **Short answer:** yes, but not with a direct destination-path argument on `ghq create`. `ghq` creates the repository under its managed root layout.
		- **Change the default root:** set `ghq.root` in `[[git/.gitconfig]]`. If multiple `ghq.root` values exist, the last one becomes the primary root and new repositories are created there.
		- **Override for one invocation:** set `GHQ_ROOT=/path/to/root` when running `ghq create ...`. The `GHQ_ROOT` environment variable is used as the only root directory for that command regardless of configured `ghq.root` values.
		- **Use a host- or URL-specific root:** configure `ghq.<url>.root` in git config when repositories matching a URL prefix should go under a different root.
		- **Constraint:** `ghq` still creates repositories under its own host/owner/repo directory structure beneath the chosen root, so it is not an arbitrary full output path argument.
		- **Examples:** `git config --global --add ghq.root ~/src`, `GHQ_ROOT=~/tmp/ghq ghq create github.com/me/project`, or a git-config stanza like `[ghq "https://git.example.com/repos/"]` with `root = ~/myproj`.
		- [ghq manual page](https://man.freebsd.org/cgi/man.cgi?query=ghq&sektion=1&manpath=FreeBSD+13.2-RELEASE+and+Ports)
		- [ghq repository](https://github.com/x-motemen/ghq)
