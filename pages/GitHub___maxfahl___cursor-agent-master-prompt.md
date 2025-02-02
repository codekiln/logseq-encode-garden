created-by:: [[Person/Max Fahl]]

- [maxfahl/cursor-agent-master-prompt: Cursor Agent - Master Prompt](https://github.com/maxfahl/cursor-agent-master-prompt/tree/main?tab=readme-ov-file)
	- The Task Master Prompt is a systematic way to guide an agent through a project from start to finish. It creates a clear record of every decision and milestone along the way, so you can always see what was done and why.
	- **Key Features:**
		- **Automated Task Documentation**
		  Helps the agent set up and maintain a single “task file” that covers everything from the initial analysis all the way to final implementation.
		- **Git Workflow Integration**
		  Gives the agent precise instructions on how to create branches, merge changes, and clean up repositories, ensuring a smooth and consistent version control process.
		- **Checkpoint-Based Progress**
		  Sets up strategic pause points so the agent can confirm progress with you before moving forward, cutting down on wasted effort or heading off in the wrong direction.
		- **Detailed Task Analysis**
		  Encourages thorough problem-solving before jumping into code changes, preventing rushed solutions and promoting a deeper understanding of the task.
		- **Progress Tracking**
		  Keeps a chronological log of every attempt, success, and failure, making it easy to review what’s been tried and how it worked out.
		- **Reusable Documentation**
		  Each task file can double as a standalone prompt for future collaboration on the task.
		- **Source of Truth Management**
		  Centralizes all project decisions and progress notes in one place so there’s no confusion about what happened or why certain choices were made.
		- **Final Review Process**
		  Walks the agent through a structured review to verify that every step is completed and documented properly before wrapping up the task.
	- > **Power User Tip**: Install [[Raycast]] if you're on Mac, then create a snippet for this that auto expands when a specific keyword is entered. I use `!utf` for "Update Task File".
	- ## Example output file
		- #Cool
			- https://raw.githubusercontent.com/maxfahl/cursor-agent-master-prompt/refs/heads/main/example-task-file-when-done.md