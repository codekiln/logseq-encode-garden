logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Unix/Q/What is a named pipe in unix, and how do 1Password Environments use one to mount a .env?]]

- # Can a symlink to a `.env` created with [[1Password/Environment]]s work? Can I create a number of different symlinks to the same `.env` and use it in different places?
	- ## [[AI Answer]]
		- **Short answer:** yes to both, with one catch. A symlink is just another path to the same named pipe, so 1Password cannot tell a read through a symlink from a read of the mount itself. Many symlinks to one mount work as long as two programs don't read at the same moment; when they do, one gets the secrets and the other waits or gets nothing.
		- This is reasoned from how named pipes work and from a test with a plain `mkfifo` pipe on macOS on 2026-10-02. It was not tested against a live 1Password mount.
		- ### Why a symlink works
			- The mounted `.env` is a named pipe (FIFO), per [Local .env files — 1Password Developer](https://www.1password.dev/environments/local-env-file). Opening a symlink opens whatever it points to, so every symlink lands on the same pipe.
			- In the test, a relative symlink (`a/.env -> ../real.env`) and an absolute one (`b/.env -> /…/real.env`) both resolved to the same pipe: `stat -L` gave the same inode and type `Fifo File` for all three paths.
			- The docs say 1Password makes "no distinction … between different processes reading the file," and it has no way to see which path a reader used either.
		- ### Many symlinks to one mount
			- **One at a time works.** When the writer serves each read in turn, `cat a/.env` then `cat b/.env` each got a full copy.
			- **Two at once does not.** With one write and two simultaneous readers, `a` got `K=once` and `b` blocked until the test was killed. The docs warn that mounted files "aren't designed for concurrent access." Several dev servers or agents starting together through different symlinks hit this.
			- **It saves mounts.** All the symlinks share one mount, so they count once against the limit of ten enabled local `.env` files per device. For git worktrees, one mount plus a symlink per worktree avoids the cleanup problem in [[1Password/Environment]] → Experiments: deleting a worktree deletes only its symlink.
			- **Approval is shared too.** Approving the first read unlocks reads through every symlink until 1Password locks.
		- ### Things that change with a symlink
			- **Git tracks it.** Git ignores a FIFO but tracks a symlink as a link (mode `120000` in the test). Add `.env` to `.gitignore` in each place you put one, or the link gets committed.
			- **Use a relative target when the layout is fixed**, e.g. worktrees beside each other; an absolute target breaks on another machine or user.
			- **File-type checks still see a pipe.** Python's `os.path.isfile` returned `False` through the symlink, the same as on the pipe itself, so loaders that need a regular file fail either way. The docs list `python-dotenv` 1.1.2+ as supported.
			- **The agent hook may not know the path.** The hook that validates mounts in supported IDEs and agents might look only at the mount's own path; whether it accepts a symlink is untested.
