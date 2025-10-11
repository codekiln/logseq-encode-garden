# [langchain-ai/langsmith-mcp-server](https://github.com/langchain-ai/langsmith-mcp-server)
	- [langchain-ai/langsmith-mcp-server | DeepWiki](https://deepwiki.com/langchain-ai/langsmith-mcp-server) #DeepWiki - [[LangSmith/MCP/Server/DeepWiki]]
		- | Category | Tools | Purpose |
		  | ---- | ---- | ---- |
		  | **Dataset Management** | [list_datasets](https://github.com/langchain-ai/langsmith-mcp-server/blob/main/langsmith_mcp_server/services/tools/datasets.py), `read_dataset`, `list_examples`, `read_example` | Access and manage [[LangSmith/Dataset]]s and their examples |
		  | **Trace Analysis** | [fetch_trace](https://github.com/langchain-ai/langsmith-mcp-server/blob/main/langsmith_mcp_server/services/tools/traces.py#L6), `get_thread_history`, [get_project_runs_stats_tool](https://github.com/langchain-ai/langsmith-mcp-server/blob/4f09b26be4fc32225bbb163ad46ea04881eaaee6/langsmith_mcp_server/services/tools/traces.py) | Analyze conversation traces and project statistics |
		  | **Prompt Management** | [list_prompts](https://github.com/langchain-ai/langsmith-mcp-server/blob/main/langsmith_mcp_server/services/tools/prompts.py#L6), `get_prompt_by_name` | Retrieve and manage [[LangSmith/PromptHub]] [[AI/Prompt]]s |
	- I did a bit of AI-assisted [[Requirement/Elicitation]] on possible other tools. AI is not great at this yet. To be fair, [[MCP]] is a new protocol and most humans haven't even figured out that the best MCP servers are actually not API-shaped wrappers. So it is perhaps not that interesting how bad AI is at this at this time ( [[2025-10-11 Sat]] ).
		- ## [Tool analysis suggestions](https://chatgpt.com/c/68ea299d-19a4-832c-95d1-1a7736a8563e) [[ChatGPT/Response]]
			- ## Dataset Management
			- **dataset_versions** — list versions for a dataset
			  
			  Purpose: show versions, created_at, author, changelog.
			  
			  Inputs: `dataset_id`
			  
			  Output: list of `{version_id, created_at, changelog, size}`
			  
			  Why: makes rollbacks, diffs and reproducible evals easier.
			  
			  Example: `dataset_versions(dataset_id="cust-support-v1")`
			  
			  Priority: high. Complexity: low.
			- **diff_dataset_versions** — show diff between two dataset versions
			  
			  Purpose: added/removed/changed examples and metadata.
			  
			  Inputs: `dataset_id, base_version, compare_version`
			  
			  Output: `{added:[...], removed:[...], changed:[{id, before, after}]}`
			  
			  Why: audit changes, spot accidental edits.
			  
			  Example: `diff_dataset_versions("d", "v1","v2")`
			  
			  Priority: high. Complexity: medium.
			- **dataset_stats** — compute coverage / label distribution / token stats
			  
			  Purpose: quick EDA on dataset health.
			  
			  Inputs: `dataset_id, sample=false`
			  
			  Output: `{n_examples, labels: {label:count}, avg_tokens, token_histogram}`
			  
			  Why: surface class imbalance and tokenization costs.
			  
			  Priority: high. Complexity: low.
			- **search_examples** — fuzzy / semantic search over examples
			  
			  Purpose: find similar examples by text or embedding.
			  
			  Inputs: `dataset_id, query, method["text","embedding"], top_k`
			  
			  Output: list of matching examples with score and metadata
			  
			  Why: accelerate prompt engineering and few-shot example selection.
			  
			  Priority: high. Complexity: medium.
			- ## Prompt Management
			- **prompt_versions** — list prompt revisions and owners
			  
			  Inputs: `prompt_name`
			  
			  Output: versions with diff, tags, test coverage flag
			  
			  Why: promotes reproducible prompt experiments.
			  
			  Priority: high. Complexity: low.
			- **prompt_diff_and_perf** — show diff + historical eval performance after change
			  
			  Inputs: `prompt_name, version_a, version_b, metric`
			  
			  Output: text diff + metric deltas on selected eval sets
			  
			  Why: directly connects prompt edits to impact on metrics.
			  
			  Priority: high. Complexity: medium.
			- **prompt_similarity_search** — find similar prompts in project or org
			  
			  Inputs: `prompt_text, top_k`
			  
			  Output: matching prompts with similarity score
			  
			  Why: avoid duplicate prompts, reuse good patterns.
			  
			  Priority: medium. Complexity: low.
			- **bulk_update_prompts** — apply templated edits to many prompts
			  
			  Inputs: `selector_query, edit_patch`
			  
			  Output: preview + dry-run + apply result
			  
			  Why: fix or add boilerplate across many prompts safely.
			  
			  Priority: medium. Complexity: medium.
			- ## Trace & Run Analysis
			- **compare_runs** — compare two runs side-by-side (messages, tool calls, metadata)
			  
			  Inputs: `run_id_a, run_id_b`
			  
			  Output: aligned transcript, divergences, timing breakdown
			  
			  Why: root-cause behavioral differences after model or prompt changes.
			  
			  Priority: high. Complexity: medium.
			- **run_visualize** — render run timeline + tool-call waterfall
			  
			  Inputs: `run_id`
			  
			  Output: structured timeline JSON + optional SVG/mermaid
			  
			  Why: fast visual debugging of long traces.
			  
			  Priority: high. Complexity: medium.
			- **anomaly_detection_on_runs** — flag unusual runs by latency, token spike, or errors
			  
			  Inputs: `project_id, window_days, threshold_rules`
			  
			  Output: list of anomalous run_ids with reason and example excerpts
			  
			  Why: proactively catch regressions or attacks.
			  
			  Priority: high. Complexity: high.
			- **filter_runs_by_metric** — query runs by metrics (accuracy, safety score, cost)
			  
			  Inputs: `project_id, metric, comparator, value, time_range`
			  
			  Output: matching runs sorted by metric
			  
			  Why: find best/worst runs for analysis and curation.
			  
			  Priority: high. Complexity: low.
			- ## Evaluation & Metrics
			- **run_batch_evaluation** — evaluate a model/prompt against a dataset (with metrics)
			  
			  Inputs: `dataset_id, prompt_version, model_spec, eval_config`
			  
			  Output: metrics, per-example fails, confusion matrix
			  
			  Why: centralize evaluation and record results in LangSmith.
			  
			  Priority: high. Complexity: medium.
			- **per_example_feedback** — attach human feedback / annotations to specific trace steps
			  
			  Inputs: `run_id, step_id, annotation{label,comment}`
			  
			  Output: updated run with feedback metadata
			  
			  Why: builds training signals and improves dataset curation.
			  
			  Priority: high. Complexity: low.
			- **auto_eval_report** — generate human-readable report with graphs and top failures
			  
			  Inputs: `eval_run_id`
			  
			  Output: PDF/markdown summary + top-N failing examples
			  
			  Why: shareable artifacts for stakeholders.
			  
			  Priority: medium. Complexity: medium.
			- ## Model & Deployment Management
			- **list_registered_models** — catalog models used in project with provider metadata
			  
			  Inputs: `project_id`
			  
			  Output: `{model_id, provider, version, last_used, avg_cost}`
			  
			  Why: governance and cost tracking.
			  
			  Priority: high. Complexity: low.
			- **compare_model_responses** — side-by-side compare responses from different model providers for same input
			  
			  Inputs: `input, models[]`
			  
			  Output: aligned responses, token/cost estimate, safety flags
			  
			  Why: helps pick model and detect provider-specific differences.
			  
			  Priority: high. Complexity: medium.
			- **model_health_metrics** — daily aggregates: latency, error-rate, token-cost, safety incidents
			  
			  Inputs: `model_id, date_range`
			  
			  Output: time-series metrics
			  
			  Why: SRE-style monitoring for LLMs.
			  
			  Priority: medium. Complexity: medium.
			- ## Observability & Debugging
			- **replay_run** — re-run a stored trace against a different model / prompt / config
			  
			  Inputs: `run_id, override_config{model,prompt,limit}`
			  
			  Output: new run id, diff to original
			  
			  Why: deterministic repro and regression checks.
			  
			  Priority: high. Complexity: high.
			- **step_inspect** — fetch full context for a single step including tool inputs/outputs and embeddings
			  
			  Inputs: `run_id, step_index`
			  
			  Output: rich object for debugger UI
			  
			  Why: targeted inspection without loading entire trace.
			  
			  Priority: medium. Complexity: low.
			- ## Cost & Token Analysis
			- **token_breakdown** — per-run token usage with model/provider breakdown
			  
			  Inputs: `run_id` or `runs[]`
			  
			  Output: token counts by role, cost estimate by provider and pricing model
			  
			  Why: control cloud costs and optimize prompts.
			  
			  Priority: high. Complexity: low.
			- **project_cost_trends** — rolling window cost analysis and anomaly alerts
			  
			  Inputs: `project_id, window_days`
			  
			  Output: trends, spikes, top-cost contributors
			  
			  Why: budgeting and forecasting.
			  
			  Priority: medium. Complexity: medium.
			- ## Safety, Governance & QA
			- **prompt_safety_scan** — scan prompts for PII, disallowed content, jailbreak patterns
			  
			  Inputs: `prompt_text` or `prompt_id`
			  
			  Output: flagged_issues with severity and suggested edits
			  
			  Why: safety guardrails before deployment.
			  
			  Priority: high. Complexity: medium.
			- **pii_detector_on_dataset** — run PII detection across dataset examples
			  
			  Inputs: `dataset_id, pii_rules`
			  
			  Output: list of examples with PII spans and redaction suggestions
			  
			  Why: compliance and data privacy.
			  
			  Priority: high. Complexity: high.
			- **access_audit** — list who accessed what (datasets, prompts, runs) with timestamps
			  
			  Inputs: `project_id, date_range`
			  
			  Output: access log entries for audit and compliance
			  
			  Why: governance and incident investigation.
			  
			  Priority: high. Complexity: low.
			- ## Integrations & Automation
			- **register_webhook** — webhooks for run-complete, eval-complete, anomalous-run
			  
			  Inputs: `event_type, url, secret, filters`
			  
			  Output: webhook_id, test-delivery result
			  
			  Why: integrate CI, alerting and downstream automation.
			  
			  Priority: medium. Complexity: low.
			- **cron_batch_runs** — schedule periodic evaluation or monitoring checks
			  
			  Inputs: `cron_spec, task{eval,metric_snapshot}, targets`
			  
			  Output: scheduled_job_id, history
			  
			  Why: automated health checks and regression guards.
			  
			  Priority: medium. Complexity: medium.
			- ## Experimentation / Research
			- **ablation_runner** — run controlled ablations across prompt components or retrieval k
			  
			  Inputs: `base_config, ablation_matrix`
			  
			  Output: per-condition metrics, heatmap summary
			  
			  Why: fast scientific-style evaluation of design choices.
			  
			  Priority: medium. Complexity: high.
			- **compare_prompt_family** — test multiple prompt variants (A/B/n) on held-out eval set
			  
			  Inputs: `prompt_versions[], eval_dataset`
			  
			  Output: per-prompt metrics, significance tests, recommended winner
			  
			  Why: rigorous prompt selection before rollout.
			  
			  Priority: medium. Complexity: medium.