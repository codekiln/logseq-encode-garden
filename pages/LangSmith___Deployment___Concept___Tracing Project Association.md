tags:: [[Diataxis/Concept]], [[LangSmith/Deployment]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[LangSmith/Deployment/Concept/Deployment Source]], [[LangSmith/CLI]], [[LangSmith/Engine]]

- # LangSmith Deployment Tracing Project Association
	- ## Overview
		- A LangSmith Deployment has an associated LangSmith tracing project that receives the deployment's built-in Agent Server traces.
		- On LangSmith Cloud, the tracing project is conventionally created with the same name as the deployment. The association is part of the deployment resource's identity and lifecycle.
		- The GitHub integration and the LangGraph CLI create or update the same kind of LangSmith Deployment resource. The CLI therefore does not provide a separate tracing-project namespace that bypasses the deployment association.
	- ## Context
		- The project name is more than a display label for a collection of traces. LangSmith uses the deployment-to-project association to decide where hosted runs appear and which project-level capabilities, including LangSmith Engine, operate on those traces.
		- Renaming the tracing project directly can break the association. LangSmith may then create a new project under the deployment's original name when the deployment sends another run.
		- Renaming the deployment through its deployment settings changes the deployment identity and its associated project relationship. Renaming the tracing project is a different operation with different consequences.
	- ## Key Principles
		- **Deployment identity controls built-in trace placement.** A new deployment normally receives a new associated tracing project based on its deployment name.
		- **The deployment method does not change that identity model.** Creating a deployment with `langgraph deploy` does not make it possible to attach the deployment to an arbitrary existing Cloud tracing project through a documented CLI option.
		- **Application tracing and Agent Server tracing are distinct concerns.** The LangSmith SDK can route application-created traces to a named project with `LANGSMITH_PROJECT` or `LANGCHAIN_PROJECT`, but that general SDK setting is not documented as a supported override for the Agent Server's managed deployment project.
		- **Engine follows the tracing project.** To have LangSmith Engine analyze the historical traces and the new deployment's built-in traces together, both sets of traces need to live in the same tracing project.
	- ## Mechanism
		- A Cloud deployment provisions or associates a tracing project using the deployment's name.
		- A deployment revision continues using the deployment's associated project, so changing the build source or using the CLI to update the deployment does not change the project identity.
		- Setting `LANGSMITH_PROJECT` is useful for custom traces emitted by code inside the application. It may create or select a project when the named project does not exist, but it does not establish a supported replacement for the deployment's own project association.
		- If a new deployment must replace an old one while preserving Engine's historical context, the supported conceptual choices are to keep the original deployment/project association or migrate project configuration and historical data into the new operational arrangement.
	- ## Trade-offs
		- Keeping the original deployment identity preserves the existing tracing project and its Engine history, but may constrain how the replacement deployment is named or introduced.
		- Creating a new deployment gives a clean operational identity and can support a migration workflow, but it creates a separate tracing project unless the deployment remains associated with the original resource.
		- Custom application-level traces can provide continuity for selected instrumentation, but splitting them from Agent Server traces makes a single Engine view harder to maintain.
	- ## Misconceptions
		- **The CLI can point a new Cloud deployment at any existing tracing project.** The current deployment documentation exposes deployment name, type, image, registry, listener, and build options, but no supported tracing-project selector.
		- **Setting `LANGSMITH_PROJECT` makes the whole deployment use that project.** The variable controls SDK tracing destinations; the managed Agent Server's deployment association remains a separate platform concern.
		- **Renaming the tracing project is equivalent to renaming the deployment.** LangSmith documents these as different operations, and renaming the tracing project can cause the deployment to recreate a project under its original name.
	- ## Sources
		- [Create a deployment](https://docs.langchain.com/langsmith/deploy-to-cloud) describes the GitHub and CLI deployment paths and the automatic tracing-project creation.
		- [Log traces to a specific project](https://docs.langchain.com/langsmith/log-traces-to-project) describes `LANGSMITH_PROJECT` and SDK-level project routing.
		- [LangGraph CLI](https://docs.langchain.com/langsmith/cli#deploy) lists the CLI deployment options and does not expose a tracing-project selector.
		- [Renaming a deployment's tracing project breaks the deployment link](https://kb.langchain.com/articles/2266685764-renaming-a-deployment-s-tracing-project-breaks-the-deployment-link-and-reserves-the-name) explains the platform's deployment-to-project coupling and recovery constraints.
		- [LangSmith Engine overview](https://docs.langchain.com/langsmith/engine-overview) describes Engine's analysis of connected tracing projects.
