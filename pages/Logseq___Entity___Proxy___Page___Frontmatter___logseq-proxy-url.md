logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[logseq-proxy-url]]

- # `logseq-proxy-url::` — the page a proxy mirrors
	- The source page of a [[Logseq/Entity/Proxy/Page]], given as that page's [[logseq-url]]: `logseq://graph/<graph_name>?page=<Page Name>`. On an instance: `logseq-proxy-url:: logseq://graph/logseq-garden?page=rulesync`.
	- ## Rules
		- Required on every proxy page. It is the one property that marks a page as a proxy.
		- One canonical spelling per source page, with `%2F` for a `/` inside `page=`, as on [[Logseq/Docs/term/block]].
		- Every sync rewrites it, along with [[Logseq/Entity/Proxy/Page/Frontmatter/logseq-proxy-last-sync-date]]. The page's other properties stay as they are.
	- ## Owning entity
		- [[Logseq/Entity/Proxy/Page]]
