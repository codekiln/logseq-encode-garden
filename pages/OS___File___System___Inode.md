logseq-entity:: [[Logseq/Entity/Term]]
alias:: [[Inode]], [[Inodes]], [[Index Node]]
see-also:: [[OS/File/System/Directory]], [[OS/File/System/Link/Hard]], [[OS/File/System/Link]]
- # Inode
	- An **inode** (index node) is the data structure in a Unix-like file system that stores a file's metadata and data-block pointers.
	- Each inode has a unique number within its file system. The [[OS/File/System/Directory]] stores the mapping from names to inode numbers; the inode itself does not store the filename.
	- ## What an inode stores
		- File type (regular file, directory, symlink, device, …)
		- Permissions and owner (UID, GID)
		- Timestamps: atime (last access), mtime (last modification), ctime (last status change)
		- File size
		- Link count — the number of [[OS/File/System/Link/Hard]]s pointing to this inode
		- Pointers to the data blocks that hold the file's content
	- ## What an inode does not store
		- The filename — that lives in the [[OS/File/System/Directory]] entry
		- The full path — a file can be reached by multiple paths if multiple hard links exist
	- ## Lifecycle
		- The file's data is freed only when the link count reaches zero **and** no process holds the file open.
		- Hard links share one inode; each new hard link increments the link count.
