logseq-entity:: [[Logseq/Entity/concept]]

- # Auth/M2M
	- Machine-to-Machine (M2M) authentication covers server-to-server and service-to-service communication flows where no human user is present to authorize the request
	- ## Common approach
		- Typically implemented via the [[OAuth2]] Client Credentials flow (RFC 6749 §4.4)
		- The client presents its `client_id` and `client_secret` directly to the authorization server and receives a short-lived access token — usually a [[JWT]]
		- No user redirect or consent screen; the token represents the service itself, not a delegated user
	- ## Relevance for async agents and MCP servers
		- Async server-side agents that call protected APIs on behalf of the system (not a specific user) need M2M tokens
		- [[MCP/Server]] deployments that run as background services — including those that scale to zero — rely on M2M auth to authenticate outbound calls without a user session
		- Token caching is essential: short-lived JWTs should be stored in a shared layer (e.g. Redis, KV, DynamoDB, [[Cloudflare/DurableObjects]]) so that scale-to-zero cold starts do not hit the token endpoint on every invocation
	- ## See also
		- [[JWT]]
		- [[OAuth2]]
