tags:: [[Term]]
logseq-entity:: [[Logseq/Entity/Term]]
see-also:: [[git/attributes/filter/clean]]

- # [smudge](https://git-scm.com/docs/gitattributes#_filter)
	- The command of a [[git/attributes/filter]] driver that converts a stored blob into the file written to the working tree. It is defined as `filter.<driver>.smudge` in git configuration.
	- On checkout, [[git]] feeds it the blob on standard input and writes its standard output to the working tree. Clone, switch and `git reset --hard` write files the same way.
	- Smudge followed by [[git/attributes/filter/clean]] should give the same result as clean alone.
	- [[git/lfs]] smudges a pointer file back into the large file it names, downloading the content when the clone doesn't have it.
