readwise-link:: https://readwise.io/reader/shared/01kgwcjp3kxgxpyxpzkx3eawsr
created-by:: [[Person/Simon Willison]]

- # [How StrongDM's AI team build serious software without even looking at the code](https://simonwillison.net/2026/Feb/7/strongdm-ai/)
	- ## [[My Notes]]
		- StrongDM describes a "software factory" workflow where humans focus on specs, scenarios, harnesses, and system constraints instead of manually writing implementation code.
		- The sharpest claim is the [[AI/Coding/Dark Factory]] principle: ==code is neither written nor reviewed by humans==, and quality is enforced through scenario coverage and empirical "satisfaction" metrics.
		- Their [[StrongDM/Digital Twin Universe]] idea is especially interesting: build high-fidelity local clones of third-party systems (like [[Okta]], [[JIRA]], and [[Slack]]) to safely run thousands of scenario checks per hour.
		- The release strategy for [[StrongDM/GitHub/attractor]] is a notable spec-first pattern: publish the complete markdown spec and let coding agents generate the implementation.
		- [[StrongDM/GitHub/cxdb]] looks like a practical "context substrate" for agentic work, with immutable DAG-based storage for tool outputs and conversation history.
	- ## Highlights
		- "Code must not be written by humans"
		- "Code must not be reviewed by humans"
		- "If you haven’t spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement"
		- "We repurposed the word scenario to represent an end-to-end ‘user story’, often stored outside the codebase (similar to a ‘holdout’ set in model training)."
		- "With the DTU, we can validate at volumes and rates far exceeding production limits... run thousands of scenarios per hour without hitting rate limits."
