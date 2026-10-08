- # LangGraph Assistants as Code in LangSmith Deployments
	- ## Executive finding
		- As of **October 8, 2026**, there is **no official LangChain CLI command, Terraform resource, Pulumi resource, MCP tool, or known community package that declaratively manages Agent Server assistants across LangSmith Deployments**. I also found **no dedicated public `assistants-as-code` tool** on GitHub, PyPI, or npm that exports/imports/diffs/reconciles assistants between LangSmith deployment hostnames. The only first-party automation surface with complete assistant lifecycle support is the **Agent Server `/assistants` REST API and the official Python/TypeScript LangGraph SDKs**.  [^1]
		- That distinction matters because LangSmith now has three separate layers that use similar vocabulary:
		- 1. A **graph** is the deployed code/blueprint registered through `langgraph.json`.
		- 2. An Agent Server **assistant** is a versioned binding of that graph to `config`, `context`, metadata, name, etc. It is persisted as Agent Server data and managed under `/assistants`.  [^2]
		- 3. A newer LangSmith **agent** is a workspace/control-plane identity used to organize tracing and deployment environments such as development, staging, and production. Binding a deployment to an `agent_id` and environment **does not replace the Agent Server assistant abstraction**: LangChain's current deployment documentation explicitly says that after deployment, execution still uses “assistants for configuration, threads for state, and runs for workloads.”  [^3]
		- For your use case, the practical answer is therefore:
		- **Keep assistant specifications and fixed UUIDs in Git and run your own small reconciler against each deployment's Agent Server API.**
		- That is not merely a workaround around a better declarative product that I found; **today it is the missing product layer**. The official API has nearly everything needed to implement it cleanly, including caller-selected `assistant_id`, idempotent create with `if_exists: "do_nothing"`, updates that create versions, version listing, and `set_latest`. What it lacks is a native desired-state/diff/import/export abstraction.  [^4]
		- ### Tool landscape at a glance
			- **Agent Server REST API / `curl`**
				- **Owner / current release:** LangChain; API is part of Agent Server rather than independently released
				- **Assistant list:** **Yes**
				- **Create:** **Yes**
				- **Update:** **Yes**
				- **Delete:** **Yes**
				- **Diff:** No
				- **Export/import:** No native facility
				- **Auth:** Deployment URL + LangSmith API key, normally `X-Api-Key`
				- **Status:** **The canonical management interface**.  [^5]
			- **Python `langgraph-sdk`**
				- **Owner / current release:** LangChain; **0.4.6, Oct. 6, 2026**
				- **Assistant list:** **Yes**
				- **Create:** **Yes**
				- **Update:** **Yes**
				- **Delete:** **Yes**
				- **Diff:** No
				- **Export/import:** No native facility
				- **Auth:** `url=` + `api_key=`
				- **Status:** **Actively maintained**.  [^6]
			- **JS/TS `@langchain/langgraph-sdk`**
				- **Owner / current release:** LangChain; current npm result **1.9.28**, published ~Oct. 5, 2026
				- **Assistant list:** **Yes**
				- **Create:** **Yes**
				- **Update:** **Yes**
				- **Delete:** **Yes**
				- **Diff:** No
				- **Export/import:** No native facility
				- **Auth:** `apiUrl` + `apiKey`
				- **Status:** **Actively maintained**.  [^7]
			- **LangSmith CLI `langchain-ai/langsmith-cli`**
				- **Owner / current release:** LangChain; **v0.3.0, Oct. 6, 2026**
				- **Assistant list:** No
				- **Create:** No
				- **Update:** No
				- **Delete:** No
				- **Diff:** No
				- **Export/import:** No
				- **Auth:** API key or `langsmith auth login`/profiles
				- **Status:** **Actively maintained, but no Agent Server assistant commands**.  [^8]
			- **LangGraph CLI `langgraph deploy`**
				- **Owner / current release:** LangChain; Python **0.4.33, Oct. 7, 2026**
				- **Assistant list:** No
				- **Create:** No
				- **Update:** No
				- **Delete:** No
				- **Diff:** No
				- **Export/import:** No
				- **Auth:** `LANGSMITH_API_KEY`; deployment-specific workspace/tenant settings as needed
				- **Status:** **Actively maintained; deploys Agent Servers, does not reconcile assistants**.  [^9]
			- **LangSmith Remote MCP server**
				- **Owner / current release:** LangChain hosted service; no separate package release cadence
				- **Assistant list:** No
				- **Create:** No
				- **Update:** No
				- **Delete:** No
				- **Diff:** No
				- **Export/import:** No
				- **Auth:** OAuth interactively; LangSmith API key programmatically
				- **Status:** **Maintained; its LangSmith tools do not include Agent Server assistant CRUD**.  [^10]
			- **Standalone `langsmith-mcp-server`**
				- **Owner / current release:** LangChain; **0.1.1, Feb. 25, 2026**
				- **Assistant list:** No
				- **Create:** No
				- **Update:** No
				- **Delete:** No
				- **Diff:** No
				- **Export/import:** No
				- **Auth:** LangSmith API key/workspace configuration
				- **Status:** **Archived Aug. 14, 2026; deprecated in favor of Remote MCP**.  [^11]
			- **LangSmith Terraform provider**
				- **Owner / current release:** LangChain; **v0.0.16, Sept. 19, 2026**
				- **Assistant list:** No
				- **Create:** No
				- **Update:** No
				- **Delete:** No
				- **Diff:** No
				- **Export/import:** No
				- **Auth:** LangSmith API key/endpoint/workspace/profile through LangSmith Go SDK
				- **Status:** **Actively maintained; no assistant resource/data source**.  [^12]
			- **Pulumi native LangSmith provider**
				- **Owner / current release:** —
				- **Assistant list:** —
				- **Create:** —
				- **Update:** —
				- **Delete:** —
				- **Diff:** —
				- **Export/import:** —
				- **Auth:** —
				- **Status:** **Does not exist in the Pulumi Registry as a dedicated LangSmith package**; Pulumi can dynamically consume Terraform providers, but the LangSmith Terraform schema has no assistants.  [^13]
			- **Community assistant sync/import/export tool**
				- **Owner / current release:** —
				- **Assistant list:** —
				- **Create:** —
				- **Update:** —
				- **Delete:** —
				- **Diff:** —
				- **Export/import:** —
				- **Auth:** —
				- **Status:** **I found none** in targeted GitHub, PyPI, and npm searches; relevant hits were SDK examples or unrelated projects.  [^14]
			- The important nuance in the first three rows is that the SDKs expose **CRUD and versions**, not desired-state semantics. There is no built-in `diff`, `export`, `import`, `sync`, `plan`, or Terraform-style reconciliation method in the documented assistants clients. The JS API, for example, explicitly documents `get`, `create`, `update`, `delete`, `search`, `count`, `getVersions`, and `setLatest`; diff/export are absent.  [^2]
	- ## Official LangChain tooling
		- ### Agent Server API and SDKs
			- This is the one official surface that fully manages the objects you mean by “assistants.”
			- Agent Server describes assistants as a core runtime resource alongside threads, runs, and cron jobs. A deployment contains one or more graphs plus a database and task queue, and core resource data including assistants is persisted in PostgreSQL.  [^1]
			- The current REST assistant surface includes:
			- `POST /assistants`
			- `POST /assistants/search`
			- `GET /assistants/{assistant_id}`
			- `PATCH /assistants/{assistant_id}`
			- `DELETE /assistants/{assistant_id}`
			- `GET /assistants/{assistant_id}/graph`
			- schema/subgraph endpoints
			- `POST /assistants/{assistant_id}/versions`
			- `POST /assistants/{assistant_id}/latest`  [^5]
			- The official TypeScript SDK documents equivalent operations: `get`, `create`, `update`, `delete`, `search`, `count`, `getVersions`, and `setLatest`; `update` produces another assistant version.  [^2] The Python SDK is explicitly described by LangChain as an SDK for connecting to a LangGraph API server and **managing assistants and threads**; version 0.4.6 was uploaded October 6, 2026.  [^6]
			- For LangSmith Cloud, the normal authentication form is the deployment hostname plus your LangSmith API key. LangChain's production deployment example initializes the SDK with `url="<deployment>"` and `api_key=...`, while its direct REST example supplies `X-Api-Key`.  [^18]
			- **This is therefore the right substrate for an assistants-as-code reconciler.**
		- ### LangSmith CLI
			- The official CLI is the Go project **`langchain-ai/langsmith-cli`**. Its current README identifies supported domains including projects, traces, runs, datasets, evaluators, experiments, and threads; it does not expose Agent Server assistant management. Authentication supports `LANGSMITH_API_KEY`, endpoint/workspace defaults, profiles, and `langsmith auth login` OAuth.  [^19]
			- Its latest release when checked was **v0.3.0**, released October 6, 2026. The repository remained under active development hours before this research.  [^8]
			- I found **no documented `assistant` command and no public assistant-specific open issue or PR** in targeted searches. The current open-PR list does include two potentially confusing developments:
			- **#353, `feat (deploy): add langsmith deploy commands`**
			- **#352, `feat: generate commands from the operation catalog`**  [^20]
			- Neither is described as adding Agent Server `/assistants` CRUD, so it would be unjustified to treat either as planned assistant support. As of October 8, there is **no public commitment I found to put assistant reconciliation into the LangSmith CLI**.  [^20]
			- There is also a naming trap: **the PyPI package named `langsmith-cli` is not this official CLI**. The PyPI package currently at 0.12.1 is maintained by `gigaverse-app` and explicitly distinguishes itself from LangChain's `langsmith` executable. It was released September 28, 2026.  [^22] It has extensive trace/archive functionality but I found no Agent Server assistant management in its documented command set or relevant open issues.  [^23]
		- ### LangGraph CLI
			- The Python LangGraph CLI is actively maintained; **`langgraph-cli` 0.4.33 was published October 7, 2026**. Its documented job is creating, developing, building, running, and deploying LangGraph/Agent Server applications.  [^9]
			- `langgraph deploy` now also understands LangSmith's new agent/environment identity. Python CLI 0.4.32+ supports:
			- ~~~bash
			  langgraph deploy \
			    --agent-id my-agent \
			    --agent-environment staging \
			    --remote
			  ~~~
			- Both options must be supplied together, and that addressing mode cannot be combined with `--name` or `--deployment-id`. The command requires a LangSmith API key; org-scoped API keys can additionally require `LANGSMITH_TENANT_ID`, whereas workspace-scoped keys do not.  [^3]
			- But these are **deployment/control-plane commands**. The CLI does not document commands such as:
			- ~~~text
			  langgraph assistants list
			  langgraph assistants apply
			  langgraph assistants export
			  ~~~
			- and therefore does not solve post-deployment assistant recreation. The fact that the server *created by the CLI* exposes `/assistants` does not imply the CLI itself manages those resources. LangChain's architecture documentation explicitly separates deployment from the Agent Server's assistant/thread/run execution model.  [^26]
		- ### Terraform and Pulumi
			- The official **`langchain-ai/langsmith` Terraform provider** is active and reached **v0.0.16 on September 19, 2026**.  [^12] It manages LangSmith control-plane resources; the current provider documentation includes resources such as workspaces, alerts/run rules, evaluators, model configurations, and deployments.  [^28]
			- Authentication is delegated to the official LangSmith Go SDK. The provider documents `LANGSMITH_API_KEY`, `LANGSMITH_ENDPOINT`, `LANGSMITH_WORKSPACE_ID` or `LANGSMITH_TENANT_ID`, plus `LANGSMITH_PROFILE`.  [^28]
			- I found **no `langsmith_assistant` resource or assistant data source in the current provider documentation/source, and no public assistant-specific issue surfaced in targeted searches**. Thus Terraform can provision/manage the **deployment that hosts the Agent Server**, but not the assistant rows inside that server.  [^12]
			- Pulumi has **no dedicated LangSmith provider in its Registry**. Pulumi's registry does offer **Any Terraform Provider**, currently listed at v1.4.0 from August 14, 2026, which can consume a Terraform provider dynamically.  [^13] That means you can use LangChain's Terraform provider through Pulumi infrastructure code, but this cannot manufacture an assistant resource that is absent from the upstream provider schema. It therefore adds **zero additional assistant capability**.  [^28]
		- ### MCP servers
			- There are three things that can be confused here.
			- The original standalone **LangSmith MCP Server** exposed LangSmith conversation history, prompt management, traces/runs, datasets/examples, experiments/evaluations, and billing. Version **0.1.1 shipped February 25, 2026**.  [^11] LangChain subsequently archived the GitHub repository on **August 14, 2026** and directs users toward the hosted Remote MCP service.  [^33] It had no documented Agent Server assistant CRUD.
			- The newer **LangSmith Remote MCP** similarly exposes LangSmith management/observability tools, not a deployment's `/assistants` resource. It supports interactive OAuth and programmatic API-key authentication.  [^10]
			- Finally, an **Agent Server itself can expose an MCP endpoint**, but that endpoint is for presenting the deployed agent as an MCP-accessible tool; it is not an assistant administration protocol. LangChain's current Managed Deep Agents documentation, for example, describes deployment as producing an Agent Server including its API and MCP endpoint, while assistant lifecycle remains part of Agent Server's normal API.  [^34]
			- So **none of LangChain's MCP options is an assistants-as-code manager**.
	- ## Community ecosystem and public plans
		- My searches across GitHub, PyPI, npm, LangChain's sample repositories, forum material, and the official CLI/provider repositories found **no maintained third-party project whose advertised purpose is to export, import, diff, promote, or reconcile LangSmith Deployment assistants**. The search results were dominated by the official SDKs, general LangGraph frameworks, or projects using “sync” in a different sense.  [^35]
		- Several near-misses are worth distinguishing.
		- The official **`langchain-samples/lsd-deep-agent-assistants`** repository is highly relevant technically. It demonstrates exactly the “one deployed graph, many assistants” model and creates assistant configurations through `client.assistants.create(...)`, connecting to a deployment with its URL and `LANGSMITH_API_KEY`.  [^14] It even keeps assistant-related memory files under `src/assistants/` in source control. But the assistant records themselves are created from a notebook: the project does **not** implement manifest export, diff, cross-deployment copying, or continuous reconciliation.  [^37]
		- The community **`kammeows/langgraph-sync`** repository sounds promising by name but is unrelated: it bidirectionally synchronizes **graph Python source and a visual graph editor** using LibCST. It does not manage Agent Server assistant records.  [^38]
		- The community PyPI **`langgraph-agent-toolkit`** is another general agent-serving stack; its documented functionality is its own FastAPI service, persistence, model configuration, integrations, and LangSmith observability. It is not an assistant migration/sync utility for LangSmith Deployment `/assistants`.  [^39]
		- The similarly named community **`gigaverse-app/langsmith-cli`** actively manages LangSmith traces and archival workflows, but its documented CLI does not provide the deployment-host assistant lifecycle requested here.  [^23]
		- On the LangChain Forum, I found material discussing deployment topology and assistants, including advice that multiple graphs in one Agent Server each receive a default assistant and can be addressed independently. I did **not** find a published production pattern or customer case study for Git-driven promotion/copying of custom assistant records across dev/staging/prod.  [^41] A June 2026 thread goes into the semantics of assistant `config` versus `context`, but likewise does not provide an assistant deployment/sync product.  [^42]
		- Therefore, I would not claim that there is a known community-standard tool or “what teams generally use.” The strongest public evidence is simply that LangChain itself shows **SDK-created assistants after deployment**, while the reusable deployment/configuration layer around them remains application-specific.  [^14]
		- I also found **no LangChain blog/changelog announcement establishing assistants-as-code, no public assistant-specific Terraform feature, and no assistant-specific open LangSmith CLI issue/PR**. The most relevant currently open CLI PR is the broader deployment-command work in #353, which should not be conflated with assistant support.  [^20]
	- ## Agent Server idempotency and version semantics
		- The API is much better suited to your desired workflow than it may first appear.
		- ### Caller-selected assistant IDs are supported
			- `POST /assistants` accepts an optional:
			- ~~~json
			  {
			    "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
			    "graph_id": "my_graph",
			    "config": {
			      "configurable": {
			        "prompt_name": "support-v7",
			        "model": "..."
			      }
			    }
			  }
			  ~~~
			- The current API schema identifies `assistant_id` as a **UUID** and says that if it is omitted, Agent Server generates a random UUID.  [^5]
			- That means you can commit a fixed valid UUID to Git for every logical assistant and reuse that UUID in dev, staging, and production. Because each Agent Server deployment has its own persisted resource database, using the same UUID on different deployment hosts does not make the underlying records one global object; it simply gives your logical assistant a stable cross-environment identifier. The separate-data-plane part follows from LangChain's documentation that each deployment contains its Agent Server and persistence layer.  [^1]
			- For your use case, **committing the UUID is materially better than discovering an assistant by mutable name**.
		- ### `if_exists: "do_nothing"` is genuinely idempotent create
			- The create API defines:
			- ~~~json
			  "if_exists": "raise"
			  ~~~
			- as the default and accepts exactly two conflict behaviors:
			- ~~~text
			  raise
			  do_nothing
			  ~~~
			- `raise` raises on duplicate creation; `do_nothing` **returns the existing assistant**.  [^4]
			- Thus this operation is safe to rerun:
			- ~~~python
			  await client.assistants.create(
			      graph_id="support",
			      assistant_id="123e4567-e89b-12d3-a456-426614174000",
			      config=desired_config,
			      name="support-prod",
			      if_exists="do_nothing",
			  )
			  ~~~
			- If that UUID already exists, Agent Server does not create another assistant.  [^4]
			- There is one crucial consequence:
			- **`do_nothing` is idempotent bootstrap, not reconciliation.**
			- The API documentation says it returns the existing assistant. It does **not** say that it compares the supplied `graph_id`, `config`, `context`, metadata, or name and updates differences.  [^4]
			- So this sequence:
			- ~~~text
			  desired Git config = A
			  server has config = B
			  create(id=X, config=A, if_exists=do_nothing)
			  ~~~
			- leaves the existing assistant at **B**, not A. A real `apply` implementation therefore needs:
			- ~~~text
			  GET/search existing
			          │
			          ├── absent ──► CREATE with fixed UUID
			          │
			          └── present
			                │
			                ├── normalized desired == actual ──► no operation
			                │
			                └── different ──► UPDATE
			  ~~~
			- That last comparison/update layer is exactly what none of the researched official tools currently provides.
		- ### Updates are versions
			- Assistants are versioned resources. LangChain's SDK documents `update` as creating a new version; the API exposes `getVersions` and `setLatest`, and the initial create creates the first version and makes it current.  [^2]
			- The official TypeScript API is explicit:
			- ~~~text
			  update(...)      -> patch assistant; creates a new version
			  getVersions(...) -> list version history
			  setLatest(...)   -> point the assistant's latest/current pointer at a version
			  ~~~
			- [^2]
			- `set_latest` in Python takes an `assistant_id` and integer `version` and POSTs to `/assistants/{assistant_id}/latest`.  [^48]
			- The older but still useful official versioning guide also documents that deleting an assistant deletes its complete version history; it does not provide a way to delete a single version.  [^49]
			- This has an important cross-deployment implication. **Version numbers are not a global release identity.** A brand-new target deployment on which you create assistant `X` starts with that assistant's new initial version; its historical sequence comes from actions performed against that particular Agent Server.  [^49]
			- So if staging has:
			- ~~~text
			  assistant X
			  v1
			  v2
			  v3  <- current
			  v4
			  ~~~
			- and production is a newly created deployment, creating X there from your desired configuration gives you a fresh history. `set_latest(X, 3)` is meaningful only if production has already accumulated a corresponding version 3. It is **not a cross-deployment promotion command**. This conclusion follows from the documented per-assistant version endpoints and each deployment's separate Agent Server persistence.  [^2]
			- If preserving the entire history really matters, your automation would need to replay the historical configurations in order and then call `set_latest`. For most GitOps-style systems, a cleaner design is to treat **Git commits/tags as the environment-independent version identity**, while Agent Server version integers are runtime-local audit/history information.
	- ## A workable assistants-as-code design
		- Because there is no packaged reconciler, the smallest robust solution is a thin CLI of your own over `langgraph-sdk`. It does not need to become another platform.
		- A Git representation could look conceptually like:
		- ~~~yaml
		  assistants:
		    - key: customer-support
		      assistant_id: "0a8c86a3-6faa-4bbb-90ea-7f698fe41111"
		      graph_id: support
		      name: Customer Support
		      config:
		        configurable:
		          prompt_name: customer-support
		          prompt_version: production
		          model: anthropic:claude-sonnet-5
		          temperature: 0.2
		      context: {}
		      metadata:
		        managed_by: git
		        manifest_key: customer-support
		    - key: internal-research
		      assistant_id: "66dfdb82-508f-472c-964e-a4a148fc2222"
		      graph_id: research
		      name: Internal Research
		      config:
		        configurable:
		          prompt_name: internal-research
		          model: openai:gpt-5.5
		      metadata:
		        managed_by: git
		        manifest_key: internal-research
		  ~~~
		- The API supports the fields represented here—graph binding, UUID, configuration, context, metadata, name, and description—although the exact manifest schema above is a recommended layer, not a LangChain-defined file format.  [^4]
		- An `apply` operation should first fetch the target assistant by its committed UUID. For a missing assistant it should create with that same UUID; for an existing assistant it should canonicalize and compare only managed fields; if they differ it should call `update`, thereby intentionally creating another Agent Server version. The documented SDK exposes all of those primitives.  [^2]
		- A `plan` operation needs no special API: it is simply the same comparison without mutations. Likewise, an `export` command can serialize the fields returned by `search`/`get`, but that would be **your serialization format**, because no official assistant export format is defined in the surfaced API or SDK documentation.  [^2]
		- For deletion, I would use an explicit ownership marker such as:
		- ~~~yaml
		  metadata:
		    managed_by: my-assistant-manifest
		  ~~~
		- and only prune target assistants carrying that marker. Agent Server supports metadata filtering in assistant search, while assistant deletion is destructive to its whole assistant/version record.  [^2]
		- A production pipeline can then have the shape:
		- ~~~text
		  Git manifest
		      │
		      ├── CI validation
		      │     UUID valid?
		      │     graph_id allowed?
		      │     config schema valid?
		      │
		      ├── deploy graph
		      │
		      ├── wait for new Agent Server deployment URL
		      │
		      └── assistant apply
		            │
		            ├── GET fixed UUID
		            ├── CREATE if missing
		            ├── DIFF managed fields
		            ├── UPDATE if changed
		            └── optionally prune managed extras
		  ~~~
		- That sequencing fits LangChain's architecture: deployment establishes the graph/Agent Server; assistants are subsequently configured against that running server.  [^52]
		- ### Stable IDs across dev, staging, and production
			- There are three sensible ID strategies.
			- **Best for your stated requirement: one committed UUID per logical assistant, reused in every environment.** The create API explicitly permits a supplied UUID, making this technically supported rather than an undocumented database trick.  [^5]
			- You might therefore have:
			- ~~~text
			  Git key              UUID
			  customer-support     0a8c86a3-...
			  research             66dfdb82-...
			  ~~~
			- and apply exactly those values to:
			- ~~~text
			  https://dev-....langgraph.app
			  https://staging-....langgraph.app
			  https://prod-....langgraph.app
			  ~~~
			- The UUID means “this logical assistant” in your organization; the deployment URL supplies the resource namespace.
			- A second approach is one UUID per logical-assistant/environment pair. That gives stronger isolation but loses the useful property that an application can carry one assistant ID across endpoint switches.
			- A third approach—discover by name after every deployment—is weakest because name is mutable while `assistant_id` is the API's primary identity.
		- ### Copying from one deployment to another
			- For one-off migration, two SDK clients are sufficient:
			- ~~~text
			  source client -> /assistants/search
			                      │
			                      ▼
			                normalize record
			                      │
			                      ▼
			  target client -> create/update
			  ~~~
			- The official SDK accepts a server URL and API key and exposes both search and CRUD, so there is no technical blocker to writing this copier.  [^53]
			- For ongoing operation, however, **source-deployment → target-deployment copying is inferior to Git → both deployments**. Otherwise staging silently becomes the configuration source of truth and changes made through Studio can reach production without passing through code review.
			- That is particularly relevant because Studio itself supports editing assistants and assistant versions interactively. LangChain's assistant-versioning material shows creating assistants, saving new versions, viewing history, and setting an earlier version current through Studio.  [^49] A Git reconciler therefore also serves as drift control against manual Studio edits.
		- ### What to do with Agent Server versions
			- A useful separation is:
			- ~~~text
			  Git commit/tag = portable release identity
			  Assistant UUID = portable logical object identity
			  Agent Server version integer = per-deployment mutation/history identity
			  ~~~
			- That model fits the documented API significantly better than trying to make Agent Server `version == 17` mean the same immutable release in three separate databases.  [^2]
			- You can include a Git identifier in assistant metadata:
			- ~~~json
			  {
			    "managed_by": "assistant-sync",
			    "git_sha": "abc123...",
			    "release": "2026-10-08.1"
			  }
			  ~~~
			- Metadata is a supported assistant field, so this provides an environment-independent mapping from a runtime version back to source control.  [^2]
			- Then:
			- ~~~text
			  get_versions()
			  ~~~
			- is useful for **runtime rollback/audit inside that deployment**, while:
			- ~~~text
			  git revert / promote manifest
			  ~~~
			- is the authoritative **cross-environment promotion operation**.
			- After applying the desired configuration, `set_latest` only needs to be called when intentionally selecting a pre-existing non-latest version on that deployment. A normal `update` already creates the new version you intend to use.  [^2]
	- ## The new LangSmith “agent” concept does not replace assistants
		- LangSmith's newest agent-based workspace model is significant, but it solves a different identity problem.
		- An **agent** is now a stable LangSmith workspace entity. Its ID is used in URLs and API calls and, once chosen, cannot be changed. Depending on how it is created, it can have the standard environments **Production, Staging, Development, and Local**. Deploying a project can create or attach to an agent, and an agent created from deployment starts with the environment structure described by LangSmith.  [^55]
		- The v2 deployment API now explicitly accepts:
		- ~~~json
		  {
		    "agent": {
		      "agent_id": "...",
		      "environment": "..."
		    }
		  }
		  ~~~
		- and documents both child fields as required when the `agent` object is supplied.  [^56]
		- The corresponding LangGraph CLI uses:
		- ~~~bash
		  --agent-id...
		  --agent-environment development|staging|production
		  ~~~
		- A deployment cannot target the `local` environment.  [^3]
		- This makes a very useful control-plane hierarchy:
		- ~~~text
		  LangSmith Agent: "customer-support"
		  │
		  ├── Development
		  │    └── Deployment A
		  │         ├── assistant UUID 1
		  │         ├── assistant UUID 2
		  │         └──...
		  │
		  ├── Staging
		  │    └── Deployment B
		  │         ├── assistant UUID 1
		  │         ├── assistant UUID 2
		  │         └──...
		  │
		  └── Production
		       └── Deployment C
		            ├── assistant UUID 1
		            ├── assistant UUID 2
		            └──...
		  ~~~
		- That diagram is an interpretation of the documented layers rather than an official LangChain diagram, but the separation itself is explicit: agent/environment binding occurs at deployment/tracing level, while after deployment the runtime still uses assistants, threads, and runs.  [^3]
		- Crucially, I found **no documentation saying that binding Development, Staging, and Production deployments to the same LangSmith agent replicates their Agent Server assistants, assigns shared assistant IDs, copies versions, or changes `/assistants` persistence semantics**. Current documentation instead continues to instruct users to interact with deployed configurations through Agent Server's assistant model.  [^26]
		- So the new model should change your naming/topology, but **not your assistant synchronization mechanism**:
		- ~~~text
		  agent_id
		      = stable identity of the overall application in LangSmith
		  agent environment
		      = dev / staging / prod observability+deployment partition
		  deployment
		      = one running Agent Server/data plane for that environment
		  assistant_id
		      = stable configured variant inside that Agent Server
		  ~~~
		- The new `agent` abstraction actually strengthens the case for keeping stable assistant UUIDs in Git: you can now have a stable **application identity** above deployments while retaining stable **configuration identities** below each deployment.
	- ## Bottom line
		- The ecosystem as of **October 8, 2026** has an obvious gap:
		- **LangChain has first-class deployment-as-code tooling and a first-class assistant CRUD/versioning API, but no first-class assistants-as-code layer connecting the two.**
		- The official LangSmith CLI does not manage them; `langgraph deploy` does not manage them; the LangSmith Terraform provider does not model them; Pulumi has no additional LangSmith assistant provider; neither hosted nor archived LangSmith MCP exposes assistant administration; and targeted community searches found no assistant export/import/diff/reconciliation project.  [^58]
		- The cleanest supported implementation today is therefore:
		- ~~~text
		  Git
		    assistant_id: fixed valid UUID
		    graph_id
		    name
		    config
		    context
		    metadata
		          │
		          ▼
		  small reconciler using langgraph-sdk
		          │
		          ├── GET/search
		          ├── CREATE(id, if_exists="do_nothing")
		          ├── semantic DIFF
		          ├── UPDATE on drift
		          ├── optional DELETE of owned extras
		          ├── get_versions for audit/rollback
		          └── set_latest for local version rollback
		          │
		          ├────────────┬────────────┐
		          ▼            ▼            ▼
		        dev          staging       prod
		     deployment     deployment   deployment
		  ~~~
		- Every primitive in the center column is officially supported today; only the **declarative reconciliation policy around those primitives** is missing.  [^2]
		- In particular, your replacement-deployment bootstrap can be safely built around a committed UUID and:
		- ~~~python
		  create(
		      assistant_id=FIXED_UUID,
		      graph_id=GRAPH_ID,
		      config=CONFIG,
		      if_exists="do_nothing",
		  )
		  ~~~
		- because caller-selected assistant IDs and `do_nothing` are documented. But subsequent runs must separately compare and update drift, because `do_nothing` deliberately returns an already-existing assistant rather than applying the supplied desired configuration.  [^4]
		- And LangSmith's new `agent: {agent_id, environment}` deployment association does **not** remove that need: it gives the overall application a durable cross-environment control-plane identity, while Agent Server assistants remain the deployed runtime's versioned configuration objects.  [^56]
	- ## Footnotes
		- [^1]: https://docs.langchain.com/langsmith/agent-server?utm_source=chatgpt.com
		- [^2]: https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk/docs/assistants.md?utm_source=chatgpt.com
		- [^3]: https://docs.langchain.com/langsmith/deploy-to-agent-environment?utm_source=chatgpt.com
		- [^4]: https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/create?utm_source=chatgpt.com
		- [^5]: https://woniu9524.github.io/langgraph/cloud/reference/api/api_ref.html?utm_source=chatgpt.com
		- [^6]: https://pypi.org/project/langgraph-sdk/?utm_source=chatgpt.com
		- [^7]: https://www.npmjs.com/package/%40langchain/langgraph-sdk?utm_source=chatgpt.com
		- [^8]: https://github.com/langchain-ai/langsmith-cli/releases?utm_source=chatgpt.com
		- [^9]: https://pypi.org/project/langgraph-cli/?utm_source=chatgpt.com
		- [^10]: https://docs.langchain.com/langsmith/langsmith-remote-mcp?utm_source=chatgpt.com
		- [^11]: https://pypi.org/project/langsmith-mcp-server/?utm_source=chatgpt.com
		- [^12]: https://registry.terraform.io/providers/langchain-ai/langsmith/latest?utm_source=chatgpt.com
		- [^13]: https://www.pulumi.com/registry/packages/?utm_source=chatgpt.com
		- [^14]: https://github.com/langchain-samples/lsd-deep-agent-assistants/blob/main/?utm_source=chatgpt.com
		- [^18]: https://docs.langchain.com/oss/python/langgraph/deploy?utm_source=chatgpt.com
		- [^19]: https://github.com/langchain-ai/langsmith-cli/blob/main/?utm_source=chatgpt.com
		- [^20]: https://github.com/langchain-ai/langsmith-cli/pulls?utm_source=chatgpt.com
		- [^22]: https://pypi.org/project/langsmith-cli/?utm_source=chatgpt.com
		- [^23]: https://github.com/gigaverse-app/langsmith-cli?utm_source=chatgpt.com
		- [^26]: https://docs.langchain.com/langsmith/deployment?utm_source=chatgpt.com
		- [^28]: https://github.com/langchain-ai/terraform-provider-langsmith/blob/main/README.md?utm_source=chatgpt.com
		- [^33]: https://github.com/langchain-ai/langsmith-mcp-server?utm_source=chatgpt.com
		- [^34]: https://docs.langchain.com/langsmith/python/managed-deep-agents-deploy?utm_source=chatgpt.com
		- [^35]: https://pypi.org/project/langgraph/?utm_source=chatgpt.com
		- [^37]: https://github.com/langchain-samples/lsd-deep-agent-assistants/blob/main/README.md?utm_source=chatgpt.com
		- [^38]: https://github.com/kammeows/langgraph-sync
		- [^39]: https://pypi.org/project/langgraph-agent-toolkit/?utm_source=chatgpt.com
		- [^41]: https://forum.langchain.com/t/how-should-i-deploy-a-self-hosted-multi-agent-system/3413?utm_source=chatgpt.com
		- [^42]: https://forum.langchain.com/t/clarification-needed-assistant-config-vs-context-and-graph-initialization/3902?utm_source=chatgpt.com
		- [^48]: https://github.com/langchain-ai/langgraph/blob/main/libs/sdk-py/langgraph_sdk/_async/assistants.py?utm_source=chatgpt.com
		- [^49]: https://github.com/langchain-ai/langgraph/blob/main/docs/docs/cloud/how-tos/assistant_versioning.md?utm_source=chatgpt.com
		- [^52]: https://docs.langchain.com/langsmith/deploy-to-cloud?utm_source=chatgpt.com
		- [^53]: https://github.com/langchain-ai/langgraph/blob/main/libs/sdk-py/README.md?utm_source=chatgpt.com
		- [^55]: https://docs.langchain.com/langsmith/create-an-agent?utm_source=chatgpt.com
		- [^56]: https://docs.langchain.com/api-reference/deployments-v2/create-deployment?utm_source=chatgpt.com
		- [^58]: https://github.com/langchain-ai/langsmith-cli/blob/main/README.md?utm_source=chatgpt.com
