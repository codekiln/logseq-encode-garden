logseq-entity:: [[Logseq/Entity/Concept]]
alias:: [[File System Link Comparison]]
see-also:: [[OS/File/System/Link]], [[OS/File/System/Link/Hard]], [[OS/File/System/Link/Soft]], [[System/Operating]]

- # Different Types of File System Links
	- ## Overview
		- [[POSIX]]-style file-system links let one file-system location reach content through more than one name, but the main link types do this in different ways.
		- A [[OS/File/System/Link/Hard]] is a direct name-to-[[OS/File/System/Inode]] mapping: the name *is* the file object. No path resolution happens; the OS reaches the file directly by inode number.
		- A [[OS/File/System/Link/Soft]] stores a path string as its payload. Each time it is followed, the OS walks the [[OS/File/System/Directory]] tree to resolve that string. If the target has moved or been deleted, the stored string leads nowhere — the link is dangling.
		- The practical difference: hard links cannot go stale because there is no path to become wrong; symlinks can go stale because the stored path may stop resolving.
	- ## Context
		- File systems separate several ideas that are easy to blur together: bytes on storage, file metadata, directory entries, and pathnames. Links are where those layers become visible.
		- A pathname such as `notes/today.md` is resolved by walking directory entries. A hard link adds another directory entry to the same file object; a symbolic link inserts a path-redirection step into that walk.
		- The POSIX core is only part of the wider landscape. Windows shortcuts, Windows junctions, macOS Finder aliases, bind mounts, and reflinks are adjacent mechanisms, but they are not the focus of this overview.
	- ## Key Principles
		- **Object link vs path link** - Hard links connect another name to the same file object; symbolic links connect one path to another path.
		- **Equal name vs pointer** - Hard-linked names are peers. A symbolic link is visibly a link that points elsewhere.
		- **Lifetime follows the model** - A hard-linked file survives until the final hard link is removed; a symbolic link can survive after its target path stops resolving.
		- **Scope differs** - Hard links usually stay within one file system and usually apply to regular files; symbolic links can point across file systems and often point to directories.
	- ## Mechanism
		- ### Hard links
			- A directory entry maps a name to a file object. Creating a hard link adds another directory entry to that same object and increments its link count.
			- When one hard-linked path is removed, the file system removes only that directory entry and decrements the link count. The underlying file is reclaimed only after the last link is gone and the file is no longer open.
		- ### Symbolic links
			- A symbolic link is a small file-like object whose payload is a target path. When a program opens the symlink normally, the OS resolves that stored path.
			- If the target path does not exist, the symlink is dangling. The link object still exists, but following it fails.
		- ### Comparison at a glance
			- **Target model** - Hard link: file object. Symbolic link: pathname.
			- **Rename behavior** - Hard link: other names keep working. Symbolic link: may break if the referenced path changes.
			- **Deletion behavior** - Hard link: content remains until the last link disappears. Symbolic link: target deletion leaves a dangling link.
			- **File-system boundary** - Hard link: normally cannot cross. Symbolic link: can point across boundaries.
			- **Directories** - Hard link: usually restricted. Symbolic link: commonly used for directories.
	- ## Examples
		- **Shared file name**: `ln report.md archive-report.md` creates a hard link. Editing either path edits the same file object.
		- **Config indirection**: `ln -s ~/dotfiles/zshrc ~/.zshrc` creates a symbolic link. The home-directory path points to the dotfiles path.
		- **Tool shims**: A version manager may put commands on `PATH` as symlinks to a dispatcher binary, letting many command names route through one implementation.
		- **Project-local references**: A repository may symlink local rules or assets into a standard directory, but those symlinks can break when collaborators use a different directory layout.
	- ## Investigation
		- The tools below let you observe the inode/path distinction directly in a terminal.
		- ### See inode numbers with `ls -li`
			- The first column is the [[OS/File/System/Inode]] number. Two names with the same inode number are hard links to the same file object. The second numeric column is the link count.
			- ~~~sh
			  ls -li report.md archive.md
			  # 1234567 -rw-r--r-- 2 user group 42 Jun 10 report.md
			  # 1234567 -rw-r--r-- 2 user group 42 Jun 10 archive.md
			  ~~~
			- Both names share inode `1234567` and link count `2`. A symlink would show a different inode number and an `l` in the permission field.
		- ### Deep-inspect a single file with `stat`
			- `stat <file>` shows the inode number, link count, permissions, owner, and all three timestamps in one view.
			- ~~~sh
			  stat report.md
			  # Inode: 1234567   Links: 2
			  ~~~
		- ### Read a symlink's stored path with `readlink`
			- `readlink <link>` prints the raw path string stored inside the symlink — the thing that can go stale.
			- `readlink -f <link>` resolves the full chain to a canonical absolute path, or exits non-zero if any step in the chain is broken.
			- ~~~sh
			  readlink ~/.zshrc
			  # /home/user/dotfiles/zshrc
			  readlink -f ~/.zshrc
			  # /home/user/dotfiles/zshrc
			  ~~~
		- ### Find all hard links that share an inode
			- Once you know an inode number (from `ls -li` or `stat`), `find -inum` locates every hard link to it.
			- ~~~sh
			  find . -inum 1234567
			  # ./report.md
			  # ./archive.md
			  ~~~
		- ### Find dangling symlinks with `find -xtype l`
			- `-type l` matches any symlink. `-xtype l` matches symlinks whose target cannot be resolved — the practical definition of a dangling link.
			- ~~~sh
			  find . -xtype l
			  # ./broken-link
			  ~~~
	- ## Misconceptions
		- **"A hard link is a shortcut."** Not quite. A hard link is another real name for the same file object; there is no special shortcut file to follow.
		- **"Deleting the original deletes the hard-linked file."** False. After a hard link is created, no pathname is technically the original; each hard link is an equal directory entry for the same file object. The content remains while any hard link remains.
		- **"A symlink contains the target file."** False. It contains a path string; the target content lives elsewhere.
		- **"Symlinks are always portable."** False. Relative and absolute target paths both depend on the layout of the machine or repository where they are resolved.
		- **"All file-system links are the same kind of indirection."** Too broad. Hard links, symlinks, shortcuts, aliases, mounts, and reflinks each have distinct semantics.
