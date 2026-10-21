logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [Cloudflare R2](https://developers.cloudflare.com/r2/)
	- S3-compatible object storage for unstructured files such as images, documents, audio, and video.
	- Objects are stored in buckets. Applications can access R2 through Cloudflare Workers bindings or its S3-compatible API, among other interfaces.
	- Cloudflare documents R2 as having no egress fees; storage and operations are subject to its pricing and usage terms.
	- R2 stores file contents, while a relational database such as [[Cloudflare/D1]] can store searchable metadata about those files.
	- [[ChatGPT/Sites]] documents R2 as its storage choice for uploaded files.
	- See [[Cloudflare/R2/Concept/Pricing Compared with Backblaze B2]] for a current comparison of storage, request, and download costs.
	- See [[Logseq/Publish/Explanation/Options for Hosting Larger Files]] for the garden's earlier R2 and media-hosting notes.
