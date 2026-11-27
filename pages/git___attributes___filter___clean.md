tags:: [[Term]]
logseq-entity:: [[Logseq/Entity/Term]]
see-also:: [[git/attributes/filter/smudge]]

- # [clean](https://git-scm.com/docs/gitattributes#_filter)
	- The command of a [[git/attributes/filter]] driver that converts a working-tree file into the form [[git]] stores. It is defined as `filter.<driver>.clean` in git configuration.
	- `git add` feeds it the working file on standard input and stores its standard output as the blob.
	- `git status` and `git diff` also run it to compare a working file with the index, so a working file that cleans to the stored blob counts as unchanged.
	- Running clean on its own output should change nothing.
	- [[git/lfs]] cleans a large file into a small pointer file and keeps the content outside the repository.
	- Not the same as `git clean`, which deletes untracked files: [[git/clean]].
