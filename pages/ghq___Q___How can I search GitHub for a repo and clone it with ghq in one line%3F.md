logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]]
see-also:: [[awk/Q/How can I extract the first column?]]
- # How can I search GitHub for a repo and clone it with ghq in one line? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
		- Short answer: pipe `gh search repos` → `head -n 1` → `awk '{print $1}'` → `ghq get`.
		- ~~~bash
		  gh search repos rulesync | head -n 1 | awk '{print $1}' | ghq get
		  ~~~
		- Steps in the pipeline:
			- `gh search repos <name>` — queries GitHub and prints results, first column is `OWNER/REPO`
			- `head -n 1` — takes the top result
			- `awk '{print $1}'` — extracts the first whitespace-delimited field (the `OWNER/REPO` slug); see [[awk/Q/How can I extract the first column?]]
			- `ghq get` — clones the repo under your `ghq` root
