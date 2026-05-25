logseq-entity:: [[Logseq/Entity/term]]
alias:: [[Hard Link]], [[Hard Links]]
see-also:: [[OS/File/System/Link/Soft]], [[OS/File/System/Link/Concept/Comparison of Different Types]], [[OS/File/System/Link]]
- # Hard link
	- A **hard link** is another directory entry for the same underlying file object. On Unix-like file systems, multiple hard links can name the same inode, so each name reaches the same file content and metadata.
	- Deleting one hard link removes that directory entry, not necessarily the file data. The file data remains available until the last hard link is removed and no process still has it open.
	- ## Advantages
		- **Same-object identity** - Each hard link is an equal name for the same file, rather than a pointer to a preferred target path.
		- **Rename and deletion resilience** - Other hard links keep working when one name is renamed or removed.
		- **No dangling path** - A hard link does not store a target pathname, so it cannot become broken merely because a target path moved.
	- ## Disadvantages
		- **Same-file-system limit** - Hard links normally cannot cross file-system boundaries because they refer to an object within one file system.
		- **Directory restrictions** - Ordinary users generally cannot hard-link directories, because directory hard links can create cycles and confuse traversal.
		- **Surprising aliasing** - Editing through any hard link changes the same underlying file, which can surprise readers who expected a copy.
