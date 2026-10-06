tags:: [[Diataxis/Concept]], [[LangSmith/Deployment]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[LangSmith/Deployment/How To/Set Up Preview Builds]], [[LangSmith/CLI]], [[LangSmith/Deployment/langgraph.json]]

- # LangSmith Deployment Source
	- ## Overview
		- A LangSmith deployment has a source workflow that determines how its code becomes a running revision.
		- The GitHub integration connects a deployment to a repository and branch. LangSmith builds the repository source and can update the deployment when that branch receives a push.
		- The LangGraph CLI treats deployment as an explicit build-and-publish operation. It builds an Agent Server image locally or remotely, pushes it to the appropriate registry, and creates or updates a deployment.
	- ## Context
		- The two workflows converge on the same LangSmith Deployment runtime. They differ mainly in who owns the source-to-revision lifecycle: LangSmith owns more of it in the GitHub workflow, while the caller owns more of it in the CLI workflow.
		- The distinction is operational rather than a permanent compatibility boundary. The current CLI can update deployments that were created through the LangSmith UI or GitHub integration.
	- ## Key Principles
		- **GitHub integration is repository-connected automation.** The repository, branch, push events, and GitHub authorization form part of the deployment configuration.
		- **The CLI is an automation primitive.** It exposes deployment, listing, logs, deletion, and revision operations that can be composed into GitHub Actions, GitLab CI, Bitbucket Pipelines, or another delivery system.
		- **Managed pull-request previews belong to the GitHub-connected lifecycle.** LangSmith Preview Builds currently work on LangSmith Cloud for deployments created through the GitHub integration.
		- **Custom pull-request previews belong to the delivery pipeline.** A team using the CLI can create a preview deployment for a pull request through CI and the Control Plane API, but the team must define the trigger, naming, promotion, cleanup, permissions, and evaluation behavior.
	- ## Mechanism
		- A GitHub-connected parent deployment can be configured to create a temporary preview deployment for every pull request or for pull requests carrying a selected label.
		- LangSmith builds the latest commit from the pull request's source branch as the preview's first revision. Later commits create later revisions of that preview.
		- Preview deployments inherit the parent's secrets when they are created. Existing previews do not receive later changes to the parent's secrets.
		- An idle time-to-live, a concurrency limit, and manual deletion control the lifetime of managed previews.
		- A CLI-based pipeline can reproduce the same broad shape by creating a deployment per pull request, updating it when the branch changes, and deleting it when the pull request closes or merges.
	- ## Trade-offs
		- The GitHub integration reduces pipeline code and gives reviewers a shared preview environment tied directly to the pull request. It is the natural fit when LangSmith Cloud and GitHub are the system of record for source changes.
		- The CLI gives the delivery system control over build timing, tests, offline evaluations, approval rules, image construction, registry choice, deployment type, and hosting environment. That control comes with pipeline work that the managed GitHub workflow performs for you.
		- The CLI also supports deployment workflows that are independent of GitHub and can target self-hosted or hybrid arrangements that use a registry and listener.
	- ## Misconceptions
		- **A CLI deployment cannot have a pull-request preview.** It can have one when CI creates and manages the preview. The CLI does not currently provide the managed Preview Builds settings exposed for GitHub-connected Cloud deployments.
		- **A GitHub-created deployment can only be updated through GitHub.** The current CLI documentation says that `langgraph deploy` can update deployments created through the UI or GitHub integration.
		- **The choice changes the Agent Server capabilities.** Both workflows produce LangSmith Deployments with the same runtime surface; the major difference is the surrounding delivery lifecycle.
	- ## Sources
		- [Create a deployment](https://docs.langchain.com/langsmith/deploy-to-cloud) describes the GitHub and CLI creation paths.
		- [Preview builds](https://docs.langchain.com/langsmith/preview-builds) describes managed pull-request previews and their limits.
		- [LangGraph CLI](https://docs.langchain.com/langsmith/cli#deploy) describes CLI deployment, including updating deployments created through other methods.
		- [Implement a CI/CD pipeline](https://docs.langchain.com/langsmith/cicd-pipeline-example) demonstrates custom preview and production deployment workflows.
