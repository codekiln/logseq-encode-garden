tags:: [[Diataxis/Explanation]]

- # Explanation: Workflows vs Actions for DRY in a Local Repository
	- ## Overview
		- Both **workflows** and **actions** can help reduce duplication in GitHub Actions, but they operate at different levels. Choosing correctly depends on whether you want to DRY **steps inside a job** or **entire jobs across workflows**.
		- ### Important Note on Potentially Confusing "relative path" `uses: ./...` notation
			- Usually in programming languages, a file reference that begins with `./xyz` means "in the current directory, find xyz." Here, it does not! Instead, in github actions, it refers to the **repository root**.
	- ## Context
		- In a single repository, it’s common to repeat build, test, or setup steps across multiple jobs or workflows.
		- GitHub provides two main tools to reduce duplication:
			- **Composite actions** (bundling steps together).
			- **Reusable workflows** (bundling whole jobs or pipelines).
		- YAML anchors also exist, but they are limited to pure YAML duplication removal and lack the semantics of Actions.
	- ## Key Principles
		- **Granularity matters**: Actions DRY out *steps*, workflows DRY out *jobs*.
		- **Scope matters**: Composite actions run inside the caller’s job; reusable workflows run as their own jobs.
		- **Locality matters**: Within one repo, prefer `./.github/...` references, but understand that they are resolved differently for actions vs workflows.
	- ## Mechanism
		- ### Composite Actions
			- Define in `.github/actions/<name>/action.yml`.
			- Encapsulate repeated **step sequences** like “setup Node, install dependencies, lint.”
			- Invoked inside a job step:
			  ~~~yaml
			  steps:
			   - uses: ./.github/actions/setup-node
			  ~~~
				- ==Note: even though this looks like a relative path (`./...`), it is not!==
			- Runs *within* the job that called it.
			- Here, `uses: ./...` really is a filesystem path. GitHub Actions resolves the path relative to the **repository root**, not the workflow file. So `./.github/actions/setup-node` resolves to `.github/actions/setup-node/action.yml` in the repo.
		- ### Reusable Workflows
			- Define in `.github/workflows/<name>.yml` with `on: workflow_call`.
			- Encapsulate repeated **jobs or pipelines** like “run full test matrix” or “deploy to staging.”
			- Invoked as a job:
			  ~~~yaml
			  jobs:
			   tests:
			     uses: ./.github/workflows/test-matrix.yml
			  ~~~
				- ==Note: even though this looks like a relative path (`./...`), it is not!==
			- Runs as a separate job with its own runner and config.
			- Here, `uses: ./...` looks like a relative path, but GitHub interprets it as a **workflow reference**. Just like with composite actions, the resolution is anchored at the **repository root**, not relative to the calling workflow file. That’s why you must put reusable workflows under `.github/workflows/`.
	- ## Examples
		- **Composite Action use case**  
		  You have 10 jobs across workflows that all need the same setup steps: checkout repo, set up Python, install deps. DRY them into a composite action and call it inside each job.
		- **Reusable Workflow use case**  
		  You have multiple workflows that all need to run the same test matrix (e.g., across OSes and Python versions). DRY the whole matrix into a reusable workflow and call it from different workflows.
	- ## Misconceptions
		- *Myth*: “Reusable workflows can replace composite actions.”  
		  → No. Workflows can’t be dropped into the middle of a job; they only run as whole jobs.
		- *Myth*: “Composite actions can orchestrate jobs.”  
		  → No. They’re limited to steps and cannot set `runs-on`, matrices, or job-level config.
		- *Myth*: “Both `uses: ./...` syntaxes mean the same thing.”  
		  → No. For composite actions, `uses: ./...` is a **filesystem path** pointing to a directory with `action.yml`. For reusable workflows, `uses: ./...` is a **workflow reference**, but in both cases resolution is from the repository root, not relative to the calling workflow file.
	- ## Related
		- [Creating composite actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
		- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)