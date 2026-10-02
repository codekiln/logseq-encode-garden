logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[logseq-proxy-codeforge-url]]

- # `logseq-proxy-codeforge-url::` — where a proxy's source file lives on a code forge
	- The web URL of the source file of a [[Logseq/Entity/Proxy/Page]] in its repository, carrying the host, owner, repository, branch, the graph's folder inside the repository, and the file under `pages/`. On an instance: `logseq-proxy-codeforge-url:: https://github.com/logseq/docs/blob/master/pages/Queries.md`.
	- A graph in a subfolder of its repository shows that folder between the branch and `pages/`: `https://github.com/<owner>/<repo>/blob/main/<folder>/pages/<file>.md`.
	- ## Rules
		- Set it when the source graph is committed and pushed to a code forge. A source that lives on one machine only carries [[Logseq/Entity/Proxy/Page/Frontmatter/logseq-proxy-url]] alone.
		- The URL takes the forge's own file form: `/blob/<branch>/` on GitHub, `/-/blob/<branch>/` on GitLab.
		- Spaces in the path are `%20`, as on [[Logseq/Frontmatter/github-link]].
		- It names the same page as [[Logseq/Entity/Proxy/Page/Frontmatter/logseq-proxy-url]]. That key opens the source in Logseq; this one opens it on the forge, and it locates the repository for a sync on any machine.
		- A sync writes it together with the other proxy keys.
	- ## Owning entity
		- [[Logseq/Entity/Proxy/Page]]
