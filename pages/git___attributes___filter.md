logseq-entity:: [[Logseq/Entity/Software/Feature]]
see-also:: [[git/attributes]]

- # [gitattributes: filter](https://git-scm.com/docs/gitattributes#_filter)
	- The `filter` attribute names a filter driver that converts a file between its form in the working tree and the form [[git]] stores.
	- The driver's [[git/attributes/filter/clean]] command runs on check-in. `git add` feeds it the working file on standard input and stores its standard output as the blob.
	- The driver's [[git/attributes/filter/smudge]] command runs on checkout. Git feeds it the blob and writes its output to the working tree.
	- Either command can be left out.
	- ## Configuration
		- [[git/attributes]] assigns a driver to paths, such as `*.als filter=als`. The commands are defined in git configuration, which each clone sets for itself:
		  ~~~
		  [filter "als"]
		  	clean = gzip -dcf
		  	smudge = gzip -9cn
		  ~~~
		- A clone whose configuration doesn't define the driver passes content through unchanged, and so does a command that exits with a non-zero status. `filter.<driver>.required = true` makes both an error, for content that is unusable without the filter, such as encrypted files.
		- `%f` in a command is replaced with the path being filtered. The file on disk may not exist or may hold other content, so a filter reads only standard input.
		- `filter.<driver>.process` runs one long-lived command for a whole git command instead of one per file, and takes precedence over `clean` and `smudge`. [[git/lfs]] uses it. [Long Running Filter Process](https://git-scm.com/docs/gitattributes#_long_running_filter_process)
	- ## How a filter should behave
		- Running clean on its own output changes nothing. Smudge followed by clean gives the same result as clean alone.
		- After changing the clean command, `git add --renormalize .` stores existing files again through the new command.
		- `merge.renormalize = true` runs a virtual checkout and check-in on all three versions in a merge, so a file stored before the filter existed merges cleanly with one stored after. [Merging branches with differing checkin/checkout attributes](https://git-scm.com/docs/gitattributes#_merging_branches_with_differing_checkincheckout_attributes)
		- Git compares a working file with the index by running clean on it. A working file that differs from smudge's output, but cleans to the stored blob, counts as unchanged.
	- ## gzip as a filter
		- `gzip -dc` decompresses on clean. With `-f`, gzip passes input that isn't gzip through unchanged, so clean accepts its own output.
		- A gzip header records the original file name and modification time, so compressing the same data twice gives two different files. `gzip -n` leaves both out, and smudge then writes the same file in every clone. [RFC 1952: Member format](https://www.rfc-editor.org/rfc/rfc1952#section-2.3)
	- ## Filter or textconv
		- A filter changes what the repository stores, and `git diff` then compares the stored form directly.
		- `diff.<driver>.textconv` leaves the repository storing the original file and changes only what `git diff` and `git log -p` show, as [[git/attributes]] describes.
	- ## In this garden
		- [[Ableton/Live/Idea/Store-Ableton-in-the-Garden]] weighs a filter that stores Ableton Live Sets as XML.
