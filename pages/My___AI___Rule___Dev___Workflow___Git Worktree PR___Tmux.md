# [[git/worktree]] and [[tmux/session/Picker]] workflow
	- This workflow inherits [[My/AI/Rule/Dev/Workflow/Git Worktree PR]] standards and adds tmux-related items.
	- AI agents should be organized in [[tmux]] such that when I open [[tmux/session/Picker/Window Expanded]], I see a list of everything my agents are working on:
		- [[tmux/session]] names should describe an area of responsibility - either a full repository or an area of responsibility within a particular repository.
		- There should be at most one [[AI/Agent]] per [[tmux/Window]], and the first pane in the group should be for the agent. The [[tmux/Window]] name should convey what the agent is for.
		- The first [[tmux/Window]] should be a primary [[AI/Agent/Manager]] which "wakes up" and "puts to sleep" other agents, by which I mean that an appropriately named [[tmux/Window]] is created with an [[AI/Coding/Tool]] initiated with an appropriately named [[AI/Coding/Session]] that matches the name in the [[tmux/Pane]].
-