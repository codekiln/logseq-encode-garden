cgpt-link:: [Idea/langgraph-streamio-aichat - StreamIO Chat API v2](https://chatgpt.com/g/g-p-67f8f6b926a8819192b3b953d0bf4266-idea-langgraph-streamio-aichat/c/6821fbf7-4084-800a-b32f-fe0544c3d96c)

- # Differences from StreamIO Chat REST API v1 vs v2 with respect to the Python and React libraries
	- [[My Notes]]
		- [[2025-05-12 Mon]]
		  id:: 682200ae-9789-4693-abfa-fee47423adba
			- Was surprised that a general [[o3]] query returned results that seemed more like a [[ChatGPT/Deep Research/Response]], even though that was not stipulated.
			- Via this response, I found [[StreamIO/GitHub/protocol]] which is a repository for the Stream public #API and for generating some of the client SDKs. Though o3 came up with [Platform API SDKs · GetStream/protocol · Discussion #177](https://github.com/GetStream/protocol/discussions/177) as a dictation; that's an old thread and there isn't that much recent information in any of the discussions.
			- Some stuff below doesn't quite make sense and might need to be updated. The python library I'm more familiar with is [[Py/Lib/stream-chat]] and exists in github repo [[StreamIO/GitHub/stream-chat-python]], not `stream-py` as indicated. I did end up finding [[StreamIO/GitHub/stream-py]] which, as in the report below, seems to be auto-generated from the [[OpenAPI]] [spec as per the README here](https://github.com/GetStream/stream-py?tab=readme-ov-file#generate-code-from-spec).
	- [[ChatGPT/Response]]
		- Below is what Stream has made public so far about the brand-new **Chat v2 server-side REST API** and what that means for developers who use the current “v1” Chat API.
		- ## TL; DR (one-paragraph executive summary)
			- Stream's v2 Chat API is part of a larger "Platform API" initiative announced on GitHub that unifies Chat, Video and (eventually) Feeds behind a single OpenAPI specification and a single set of language SDKs. Compared with the long-standing `chat-openapi.yaml` ("v1"), the new `v2/chat-serverside-api.yaml` adopts uniform resource naming, makes most request/response bodies strongly-typed objects, removes several legacy query parameters, and introduces brand-new resources for rule-based moderation, S3/Azure/GCS media storage and granular permission scopes. A Python SDK that targets v2 (`getstream`, a.k.a. **stream-py**) reached GA on **6 May 2025 (v 2.1.0)**, while a React SDK is tracking for **Q3 2025**: an RC (v 13.0.0-rc.*) has already shipped. Upgrading is opt-in; Stream will continue to run v1 in parallel and the migration is "schema-only"—tokens, app keys and WebSocket endpoints remain unchanged.
		- ---
		- ## 1 Where to read about the differences
			- Where to look / What you'll find:
				- **OpenAPI specs** – compare [`openapi/chat-openapi.yaml`](https://raw.githubusercontent.com/GetStream/protocol/main/openapi/chat-openapi.yaml) with [`openapi/v2/chat-serverside-api.yaml`](https://raw.githubusercontent.com/GetStream/protocol/main/openapi/v2/chat-serverside-api.yaml):
					- You can diff the files to see renamed/removed paths, new components (e.g. **RuleBuilder**, **S3Request**, unified **custom** object, ISO-8601 `updated_at` fields, etc.)
				- **Platform-API discussion (#177):**
					- Maintainers explain the goal of "one spec, one SDK per language" and confirm Chat is the first product to move.
				- **Permissions v2 docs** (`/node/user_permissions/`):
					- The permission system has been rewritten; the spec exposes the same "v2" grants.
				- **Release notes in the React SDK (v 13 RC):**
					- Highlight breaking prop changes caused by the v2 data model. [stream-chat-react releases](https://github.com/GetStream/stream-chat-react/releases)
				- **stream-py README & CHANGELOG:**
					- Shows the new Python client generated from the v2 spec.
		- ### Headline functional changes
			- **Uniform resources** – endpoints are now grouped under `/chat/…` and use nouns rather than verbs (e.g. `POST /chat/channels` instead of `POST /channels/{type}/{id}`)
			- **Strongly-typed payloads** – every nested object has a schema; ad-hoc `extra_data` fields have been consolidated into a top-level `custom` map
			- **Moderation & storage** – new first-class components such as `RuleBuilderConfig`, `RuleBuilderAction`, `S3Request`, `AzureRequest` let you configure moderation pipelines and external storage purely via API
			- **Consistent timestamps & enums** – all times are RFC 3339 strings; enums are capital-case strings rather than integers (e.g. `default_device: "speaker"`)
			- **Deprecations removed** – legacy push-v1, mixed snake/camel casing, and several list-style query parameters have been dropped (see spec diff)
		- ## 2 Roll-out schedule for SDK support
			- SDK / Status / Milestone:
				- **Python** [stream-chat-python](https://github.com/GetStream/stream-chat-python) [[StreamIO/GitHub/stream-chat-python]]
					- **GA** – v 2.1.0 (6 May 2025) with full Chat & Video namespaces; generated from v2 spec
				- **React** (`stream-chat-react`): [[StreamIO/GitHub/stream-chat-react]]
					- **Release Candidate** – v 13.0.0-rc.2 (30 Apr 2025) introduces breaking changes that mirror v2 schemas. GA is planned "later this summer" per maintainers' release notes [stream-chat-react/releases](https://github.com/GetStream/stream-chat-react/releases)
				- **JS core** (`stream-chat-js`):
					- Back-compat layer ships now; a branch with pure v2 types is targeted for mid-2025 according to roadmap issues
				- **Other server SDKs (Go, Node, Ruby, PHP):**
					- Will migrate as "platform" repos similar to stream-py; timeline not yet public but expected 4-6 weeks after Python GA
		- ## 3 What the update process looks like
			- **Opt-in at the SDK level:**
				- Install the new package (`pip install getstream` or `npm install stream-chat-react@next`). Tokens, API keys and the base URL stay the same. [github.com](https://github.com/GetStream/stream-chat-react/releases)
			- **Verify permission version:**
				- Call `client.get_app_settings()`; if it returns `"permission_version": "v1"`, open a ticket with Stream support to switch your app to the v2 grant engine before deploying.
			- **Map resource & field changes:**
				- Use the two OpenAPI specs side-by-side or run the official diff tool included in stream-py's `generate.sh` script to find renamed properties.
			- **Parallel run / canary:**
				- Because JWTs and WebSockets are unchanged, you can point a staging environment at v2 while production remains on v1; Stream recommends at least 48 hours of canary traffic.
			- **Client updates:**
				- Once server-side calls and permission grants pass tests, bump mobile/React clients to the matching v2-ready versions. React RCs already contain shims that can talk to either backend. [github.com](https://github.com/GetStream/stream-chat-react/releases)
			- **Sunset v1:**
				- Stream has committed to **12 months of overlap support** after the v2 GA of each SDK; you'll receive dashboard and e-mail notices well in advance of any cutoff.
		- ---
		- ### Need more detail?
			- Stream's developer relations team is preparing a full **migration playbook**; watch the Platform-API GitHub discussion for updates.
			- If you use **custom webhooks or signed links**, those endpoints have not changed, but the payload shape has – re-validate your HMAC checks.
			- Video, Feeds and Live Analytics endpoints will join the same spec later in 2025, so adopting the new SDKs early will future-proof your code.
			- Feel free to ask if you need a line-by-line diff or example code for the new SDK calls!