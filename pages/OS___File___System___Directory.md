logseq-entity:: [[Logseq/Entity/term]]
alias:: [[File System Directory]], [[POSIX Directory]]
see-also:: [[OS/File/System/Inode]], [[OS/File/System/Link/Hard]], [[OS/File/System/Link]]
- # File system directory
	- In the POSIX sense, a **directory** is a special file whose content is a sequence of directory entries (`struct dirent`), each mapping a name to an [[OS/File/System/Inode]] number within the same file system.
	- The directory does not store file content or most metadata — those live in the inode. It is purely a name-to-inode mapping.
	- Every directory contains two automatic [[OS/File/System/Link/Hard]]s: `.` (pointing to itself) and `..` (pointing to the parent directory).
	- ## Contrast with the colloquial sense
		- In everyday use, "directory" and "folder" are synonyms for a container that organizes files.
		- In the POSIX data-structure sense, a directory is the mechanism that gives a file its name: the name lives in the directory entry, not in the file itself.
