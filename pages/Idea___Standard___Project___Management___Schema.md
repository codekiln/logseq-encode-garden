see-also:: [[Idea/Standard/Project/Vision and Goals]]

- # Project Management Schema
	- Every time I start a repository, I write agent instructions explaining how issues are prioritized, what "blocked by" means, how parent and child work is modeled, and how all of that maps onto whichever tracker the repository uses: [[GitHub/Issue]], [[JIRA]], [[Beads]], or maybe [[Linear]]. The meanings barely change from project to project. Only the tracker mechanics change.
	- What if a small, provider-neutral [[Schema]] defined what the terms mean, and a separate binding per tracker said how each term is represented there? An agent could read the schema and know what priority and dependencies mean without knowing which tracker is in use.
	- ## The schema
		- A handful of concepts: work item, status, priority, blocks / blocked-by, parent / child, and relates-to. Maybe milestone.
		- Each concept carries a short definition a human can read and approve.
		- ~~~yaml
		  priority:
		    high:
		      rank: 1
		      definition: Selected before normal-priority work.
		  relations:
		    blocks:
		      inverse: blocked_by
		      definition: The blocked item is not started until the blocker is done.
		  ~~~
	- ## Provider bindings
		- A binding maps each concept onto one tracker's fields:
		- ~~~yaml
		  provider: github
		  priority:
		    high: { label: "priority:P1" }
		  relations:
		    blocks: { representation: issue-link }
		  hierarchy: sub-issues
		  ~~~
		- In [[JIRA]], `high` maps to the native Priority field and `blocks` to the Blocks link type. In [[Beads]], both are native.
		- A small CLI could read the binding, set up the tracker (create missing labels, check that link types exist), and report mismatches, the way infrastructure-as-code tools treat cloud resources.
		- The repository holds the schema and the bindings. The tracker holds the issues themselves.
		- A repository-specific skill could then shrink to a few lines: read the schema, use the CLI.
	- ## Prior art
		- [OSLC Change Management Version 3.0](https://docs.oasis-open-projects.org/oslc-op/cm/v3.0/os/change-mgt-spec.html) from OASIS defines change requests and their relationships. It is the closest existing standard, but no mainstream tracker uses it as its native model. Its vocabulary could inform the names in the schema.
	- ## Open questions
		- Should priority, severity, and urgency be separate concepts, or should the core carry only priority and leave the others to an optional profile?
		- How should a binding carry tracker-specific fields, such as Jira story points, without adding them to the core?
		- Should backlog maintenance (finding duplicates, missing dependencies, stale or orphaned work) be defined as standard operations alongside the data?
