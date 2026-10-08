logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LangSmith/Terraform/Q/What is the minimum secure setup for using the LangSmith Terraform provider in GitHub Actions?]], [[LangSmith/Q/What can the LangSmith Remote MCP do that the LangSmith CLI can't, and vice versa?]]

- # Which [[LangChain]] tools manage each part of a [[LangSmith]] setup?
	- The parts: prompts in the Prompt Hub, structured outputs, assistants, deployments, resource tags, tracing projects, datasets and evaluators.
	- ## [[AI Answer]]
		- **Short answer:** no single tool covers everything. The [[LangSmith/CLI]] covers prompts, tracing projects, datasets and evaluators. The [[LangSmith/MCP/Remote]] mostly reads. The Terraform provider covers deployments, resource tags and evaluators, and nothing about prompts or datasets. Assistants are reachable only through the LangGraph SDKs, the Agent Server API and the UI: no LangChain command line tool, MCP server or Terraform resource manages them.
		- Sources read on 2026-10-08, pinned: LangSmith CLI v0.3.0 at [`596db1e`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/root.go#L76-L95), the Terraform provider v0.0.16 at [`0896d0f`](https://github.com/langchain-ai/terraform-provider-langsmith/tree/0896d0f6fa7e882493389c4b3b53acb713fab03f/docs/resources), LangGraph at [`40a2e6d`](https://github.com/langchain-ai/langgraph/tree/40a2e6d845054cc0cc17a6a169ca6e7394e5231c/libs), and the LangChain docs at [`1da22ee`](https://github.com/langchain-ai/docs/tree/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith).
		- ### Prompts in the [[LangSmith/PromptHub]]
			- **LangSmith SDK:** `client.push_prompt` and `client.pull_prompt` ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/manage-prompts-programmatically.mdx#L72)).
			- **LangSmith CLI:** `langsmith prompt` lists, gets, creates, deletes, pulls and pushes Prompt Hub repos, and lists their commits ([`prompt.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/prompt.go#L31-L32)). This group is in v0.3.0 but not yet in the CLI docs page. `langsmith hub` is a different thing: it manages agent and skill repos ([`hub.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/hub.go#L71-L72)).
			- **LangSmith MCP:** `list_prompts` and `get_prompt_by_name` read prompts; `push_prompt` only returns instructions and changes nothing ([standalone server docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/langsmith-mcp-server.mdx#L77)).
			- **UI:** the Playground.
			- **Not covered:** the Terraform provider has no prompt resource.
		- ### Structured outputs
			- A structured output lives inside a prompt as its output schema, so the prompt tools above carry it. No tool manages schemas on their own.
			- **LangSmith SDK:** push a `StructuredPrompt`, a template plus a schema, with `push_prompt`, alone or chained with a model ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/manage-prompts-programmatically.mdx#L147-L149)).
			- **UI:** add an output schema to a prompt in the Playground ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/create-a-prompt.mdx#L75-L77)).
			- **LangSmith CLI:** `langsmith prompt push` sends a whole manifest, so it can carry a schema, but it has no schema-specific options.
			- More in this garden: [[LangSmith/PromptHub/How To/Define Structured Output and Models for PromptHub in Git]].
		- ### [[langgraph/Assistant]]s
			- Assistants live on each deployment's own Agent Server, not on the LangSmith API, so tools that call the LangSmith API do not reach them.
			- **LangGraph SDK** (Python and JavaScript): `create`, `update`, `delete`, `search`, `count`, `get`, `get_versions` and `set_latest`. `create` takes an optional `assistant_id` and an `if_exists` setting, so a re-run can leave an existing assistant alone ([`assistants.py`](https://github.com/langchain-ai/langgraph/blob/40a2e6d845054cc0cc17a6a169ca6e7394e5231c/libs/sdk-py/langgraph_sdk/_async/assistants.py#L314-L376)).
			- **Agent Server API:** `/assistants` on each deployment's hostname, which the SDK wraps.
			- **UI:** create, edit and version assistants by hand ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/assistants.mdx#L37-L39)).
			- **Not covered:** the LangSmith CLI, the LangGraph CLI, the LangSmith MCP servers and the Terraform provider. A deployment's own `/mcp` endpoint exposes its agents as tools to call, not to manage ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/server-mcp.mdx)).
		- ### Deployments
			- **LangGraph CLI:** `langgraph deploy` builds an image and creates or updates a deployment from it; `deploy list`, `deploy delete`, `deploy logs` and `deploy revisions list` round it out. All are marked beta ([`deploy.py`](https://github.com/langchain-ai/langgraph/blob/40a2e6d845054cc0cc17a6a169ca6e7394e5231c/libs/cli/langgraph_cli/deploy.py#L2474-L2695)).
			- **Terraform provider:** `langsmith_deployment` builds from a GitHub repository, with data sources for revisions. Changing `name` replaces the deployment: Terraform deletes it and creates a new one ([`deployment_resource.go`](https://github.com/langchain-ai/terraform-provider-langsmith/blob/0896d0f6fa7e882493389c4b3b53acb713fab03f/internal/provider/deployment_resource.go#L169-L174)).
			- **Control plane API:** `/v2/deployments` on the `api.host` hosts, for CI scripts ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/api-ref-control-plane.mdx)).
			- **UI:** create a deployment and its revisions.
			- **Not covered:** the LangSmith CLI and the LangSmith MCP servers.
		- ### Resource tags
			- **Terraform provider:** `langsmith_tag_key`, `langsmith_tag_value` and `langsmith_tagging`, plus the `langsmith_tag` shortcut that owns one key and one value. A tagging can point at a deployment, prompt, dataset, tracing project, evaluator and several other types ([`tagging_resource.go`](https://github.com/langchain-ai/terraform-provider-langsmith/blob/0896d0f6fa7e882493389c4b3b53acb713fab03f/internal/provider/tagging_resource.go#L29)). Prefer the separate key and value resources when other people add values to the same key, since destroying the shortcut destroys the key ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/manage-with-terraform.mdx#L107-L109)).
			- **REST API:** `/api/v1/workspaces/current/tag-keys` and `/taggings`. The docs show it with plain HTTP calls, not an SDK method ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/set-up-resource-tags.mdx#L65-L130)).
			- **UI:** Settings, then Resource tags.
			- **Not covered:** the LangSmith CLI's typed commands and the LangSmith MCP servers. `langsmith api` can call the tag endpoints directly.
			- Creating keys and applying any key but `Application` takes `workspaces:manage`, which only a Workspace Admin has by default ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/set-up-resource-tags.mdx#L25)).
		- ### Tracing projects
			- **LangSmith CLI:** `langsmith project` lists, inspects and deletes them, and `trace`, `run` and `thread` read what is in them ([`project.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/project.go#L15-L16), [`project_delete.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/project_delete.go#L15-L16)).
			- **LangSmith MCP:** `list_projects`, `fetch_runs` and `get_thread_history` read them ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/langsmith-remote-mcp.mdx#L165-L174)).
			- **LangSmith SDK:** `client.create_project`, and tracing creates a project on first use.
			- **Terraform provider:** only a `langsmith_project` data source that finds a project by name, which is enough to tag it or attach a run rule. No resource creates one ([docs](https://github.com/langchain-ai/terraform-provider-langsmith/blob/0896d0f6fa7e882493389c4b3b53acb713fab03f/docs/data-sources/project.md)).
		- ### Datasets
			- **LangSmith SDK:** `create_dataset`, `create_examples` and the rest ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/manage-datasets-programmatically.mdx#L53-L58)).
			- **LangSmith CLI:** `langsmith dataset` lists, gets, creates, deletes, exports and uploads; `langsmith example` manages examples ([`dataset.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/dataset.go#L17-L18)).
			- **LangSmith MCP:** reads datasets and examples; `create_dataset` and `update_examples` only return instructions ([docs](https://github.com/langchain-ai/docs/blob/1da22ee8525f1a71b17b86974f74f4f28da45347/src/langsmith/langsmith-mcp-server.mdx#L94-L95)).
			- **Terraform provider:** no dataset resource. A `langsmith_run_rule` can add matching runs to a dataset that already exists.
		- ### [[LangSmith/Evaluator]]s
			- **LangSmith CLI:** `langsmith evaluator` lists, gets, deletes, uploads code evaluators and creates LLM-as-judge rules; `evaluator rule` manages what attaches them to projects and datasets ([`evaluator.go`](https://github.com/langchain-ai/langsmith-cli/blob/596db1ef1f320252f9148cc9ed4cd41392d0daee/internal/cmd/evaluator.go#L22-L23)).
			- **Terraform provider:** `langsmith_evaluator` for LLM-as-judge and code evaluators, and `langsmith_run_rule` to attach one to a tracing project or dataset ([evaluator](https://github.com/langchain-ai/terraform-provider-langsmith/blob/0896d0f6fa7e882493389c4b3b53acb713fab03f/docs/resources/evaluator.md), [run rule](https://github.com/langchain-ai/terraform-provider-langsmith/blob/0896d0f6fa7e882493389c4b3b53acb713fab03f/docs/resources/run_rule.md)).
			- **LangSmith SDK:** `evaluate()` runs offline evaluations against a dataset.
			- **LangSmith MCP:** `list_experiments` reads results; `run_experiment` only returns instructions.
		- ### What this sweep left out
			- Community tools outside `langchain-ai`, and the JavaScript SDK beyond the assistants client. The query below covers them.
	- ## Deep research query
		- For handing to a deep research tool to find what this sweep missed, especially for assistants:
		- ```text
		  I run LangGraph graphs as LangSmith Deployments (LangSmith Cloud,
		  formerly "LangGraph Platform"). Each deployment has several
		  "assistants": saved configurations of one graph (graph_id plus
		  config.configurable values such as prompt names and model settings),
		  created through the Agent Server API (/assistants on each
		  deployment's own hostname).
		  
		  When a deployment is replaced by a new one, its assistants must be
		  recreated on the new deployment from configuration kept in Git, then
		  kept in sync afterwards.
		  
		  Research, as of October 2026, every tool that can manage these
		  assistants declaratively or from the command line:
		  
		  1. Any official LangChain tool: LangSmith CLI (langchain-ai/langsmith-cli),
		     LangGraph CLI (langgraph deploy), LangSmith MCP servers, the LangSmith
		     Terraform provider (langchain-ai/terraform-provider-langsmith), Pulumi,
		     or anything announced on the LangChain blog, changelog or forum. Is
		     assistant support planned or in an open pull request or issue?
		  2. Community tools on GitHub, PyPI or npm that export, import, diff or
		     sync LangGraph assistants between deployments, or keep them in Git.
		  3. How other teams handle "assistants as code" across dev, staging and
		     production deployments: copying assistants between deployments,
		     keeping assistant IDs stable, and versioning (get_versions,
		     set_latest).
		  4. Whether the Agent Server API lets you create an assistant with a
		     chosen assistant_id, and what if_exists does, so a re-run makes no
		     changes.
		  5. Whether LangSmith's newer "agent" concept (deployment create accepts
		     agent: {agent_id, environment}) changes how assistants are meant to
		     be managed across environments.
		  
		  For each tool give: link, owner, last release date, what it can do
		  with assistants (list, create, update, delete, diff, export), how it
		  authenticates, and whether it is maintained. Say plainly if nothing
		  exists. Cite sources; do not infer features from names.
		  ```
