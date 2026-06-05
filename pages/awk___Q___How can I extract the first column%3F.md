logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]]
- # How can I extract the first column? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
		- Short answer: use `awk '{print $1}'` — `$1` is the first whitespace-delimited field.
		- `awk` splits each line into fields on whitespace by default. Fields are numbered `$1`, `$2`, … `$NF` (last field).
			- Basic extraction:
				- ~~~bash
				  awk '{print $1}' file.txt
				  ~~~
			- Custom delimiter (e.g. CSV or colon-separated):
				- ~~~bash
				  awk -F',' '{print $1}' file.csv
				  awk -F':' '{print $1}' /etc/passwd
				  ~~~
			- Pipe from another command:
				- ~~~bash
				  ls -l | awk '{print $1}'
				  ~~~
		- The `-F` flag sets the field separator to any character or regex. Without it, `awk` collapses consecutive spaces/tabs into a single separator.
		- Reference: [GNU awk manual — Fields](https://www.gnu.org/software/gawk/manual/gawk.html#Fields)
