logseq-entity:: [[Logseq/Entity/Forum/Post]]
date-created:: [[2019-10-24 Thu]]
logseq-created-time-year:: [[20/1/9]]
created-by:: [[StackOverflow/User/Jakub Vonšovský]]

- # [Difference between git-lfs and dvc - Stack Overflow 58541260](https://stackoverflow.com/questions/58541260/difference-between-git-lfs-and-dvc)
	- ## [[Original Poster]]
		- [[StackOverflow/User/Jakub Vonšovský]]
			- Both [[git/lfs]] and [[dvc]] replace large files with an index and fetch on demand. What does DVC add?
	- ## [[Response]]
		- [[StackOverflow/User/LuVu]] (accepted, 14)
			- DVC can use ordinary remotes — NAS, SSH, S3, GCS, Azure — instead of a dedicated LFS server.
		- [[StackOverflow/User/RodolfoAP]] (62)
			- Different tools. git-lfs is transparent to git and needs a custom server; DVC gitignores the large files, adds `.dvc` sidecars, and also runs Makefile-style pipelines for generated data and models.
	- ## [[Related/Post]]
		- [[dvc/vs/git-lfs]]
