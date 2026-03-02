tags:: [[Diataxis/Explanation]]
alias:: [[DevContainer Hooks]]

- # DevContainer Hooks Conceptual Overview
	- ## Overview
		- DevContainer hooks are lifecycle entry points that let you run commands at specific moments in the environment's setup, startup, and attachment flow.
		- The main distinction is not just *which* hook exists, but *what event* it is attached to: host-side preparation, first-time container creation, every container start, or every editor attach.
	- ## Context
		- Dev Containers span more than one phase:
			- The host may need to prepare inputs before Docker builds anything.
			- The container may need one-time bootstrap work when it is first created.
			- The running environment may need repeatable tasks each time it starts.
			- The editor or client may need developer-experience setup each time it attaches.
		- Hooks exist to separate those concerns so teams do not overload a single command with conflicting responsibilities.
	- ## Key Principles
		- **Lifecycle matters more than syntax**
			- Choosing the right hook is mostly about choosing the right moment.
		- **Host and container are different execution environments**
			- `initializeCommand` runs on the host, while the other lifecycle hooks run inside the container.
		- **Some hooks are creation-time, others are runtime**
			- `onCreateCommand` and `postCreateCommand` are for first creation.
			- `postStartCommand` and `postAttachCommand` are for ongoing use.
		- **Idempotence becomes more important later in the lifecycle**
			- Commands that run on every start or attach should tolerate repetition.
	- ## Hook Families
		- ### Before the container exists
			- [[DevContainer/Hook/initializeCommand]]
				- Runs on the host before the container is created or built.
				- Best for pre-flight checks, generating files, or preparing local inputs that the build depends on.
		- ### During first-time environment creation
			- [[DevContainer/Hook/onCreateCommand]]
				- Runs inside the container only once, after the container is created and started for the first time.
				- Best for one-time bootstrap tasks.
			- [[DevContainer/Hook/updateContentCommand]]
				- Runs inside the container when workspace content changes during creation workflows.
				- This is mainly relevant in flows like GitHub Codespaces prebuilds, where the image and repository content can arrive in different stages.
			- [[DevContainer/Hook/postCreateCommand]]
				- Runs after creation, when the workspace is mounted and ready.
				- This is often the practical default hook for dependency installation and final project setup.
		- ### During normal runtime
			- [[DevContainer/Hook/postStartCommand]]
				- Runs every time the container starts.
				- Best for idempotent startup tasks and background services.
			- [[DevContainer/Hook/postAttachCommand]]
				- Runs every time a client attaches to the container.
				- Best for interactive or developer-experience tasks that depend on an editor/session attaching.
	- ## Mechanism
		- On first creation, the lifecycle is roughly:
			- ~~~text
			  initializeCommand
			  -> build
			  -> start
			  -> onCreateCommand
			  -> updateContentCommand (if applicable)
			  -> postCreateCommand
			  -> postStartCommand
			  -> postAttachCommand
			  ~~~
		- On a container restart, the creation-time hooks do not rerun:
			- ~~~text
			  start
			  -> postStartCommand
			  -> postAttachCommand
			  ~~~
		- On a window reload or reattach, only the attach-time hook runs:
			- ~~~text
			  postAttachCommand
			  ~~~
	- ## Practical Distinctions
		- **[[DevContainer/Hook/onCreateCommand]] vs [[DevContainer/Hook/postCreateCommand]]**
			- Both are first-creation hooks, but [[DevContainer/Hook/postCreateCommand]] is usually the better fit for project setup because it runs after the workspace is mounted and fully available.
		- **[[DevContainer/Hook/postStartCommand]] vs [[DevContainer/Hook/postAttachCommand]]**
			- [[DevContainer/Hook/postStartCommand]] is about the container becoming live.
			- [[DevContainer/Hook/postAttachCommand]] is about a human-facing tool session attaching to that live container.
		- **[[DevContainer/Hook/initializeCommand]] vs everything else**
			- [[DevContainer/Hook/initializeCommand]] is the only standard lifecycle hook in this group that runs on the host rather than inside the container.
	- ## Mental Model
		- A useful way to think about the hooks is:
			- [[DevContainer/Hook/initializeCommand]]: prepare the inputs
			- [[DevContainer/Hook/onCreateCommand]]: bootstrap the environment once
			- [[DevContainer/Hook/updateContentCommand]]: reconcile creation with changing workspace content
			- [[DevContainer/Hook/postCreateCommand]]: finish project setup
			- [[DevContainer/Hook/postStartCommand]]: re-establish runtime state
			- [[DevContainer/Hook/postAttachCommand]]: re-establish developer session state
	- ## Misconceptions
		- **[[DevContainer/Hook/postCreateCommand]] and [[DevContainer/Hook/postStartCommand]] are interchangeable** -> **False**. One is first-creation setup; the other is every-start behavior.
		- **[[DevContainer/Hook/postAttachCommand]] is a startup hook** -> **False**. It is tied to client attachment, not just container process startup.
		- **[[DevContainer/Hook/updateContentCommand]] is part of every local workflow** -> **False**. It is more relevant in prebuild-oriented workflows than in typical local VS Code usage.
		- **[[DevContainer/Hook/initializeCommand]] can rely on container tools** -> **False**. It runs on the host, before the container exists.
	- ## Quick Reference
		- | Hook | Where it runs | Typical trigger | Best fit |
		  |------|---------------|-----------------|----------|
		  | [[DevContainer/Hook/initializeCommand]] | Host | Recreate or rebuild flow | Host-side preparation |
		  | [[DevContainer/Hook/onCreateCommand]] | Container | First creation only | One-time bootstrap |
		  | [[DevContainer/Hook/updateContentCommand]] | Container | Creation when content changes | Prebuild/content reconciliation |
		  | [[DevContainer/Hook/postCreateCommand]] | Container | First creation only | Final project setup |
		  | [[DevContainer/Hook/postStartCommand]] | Container | Every start | Runtime initialization |
		  | [[DevContainer/Hook/postAttachCommand]] | Container | Every attach | Session UX setup |
	- ## Related
		- [[DevContainer]]
		- [[DevContainer/Ref/Key]]
		- [[DevContainer/Hook/onCreateCommand]]
