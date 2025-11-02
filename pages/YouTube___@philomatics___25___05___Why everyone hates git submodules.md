readwise-link:: [Why everyone hates git submodules | Readwise](https://read.readwise.io/new/read/01k91vdy4mm9wz23x89acfymgh)

- [Why everyone hates git submodules - YouTube](https://www.youtube.com/watch?v=JESI498HSMA)
	- ## [[My Notes]]
		- In old versions of git, you had to run `git submodule update --recursive` after changing a branch, running git pull, merging and rebase, etc. In recent versions of git, you can run these two commands once, which will make it so that when you switch branches or run a git pull or git push, all submodules will be updated automatically as necessary.
			- ~~~
			  git config --global submodule.recurse true
			  git config --global push.recurseSubmodules on-demand
			  ~~~
		- Some recommended aliases for submodules
			- ~~~
			  git config --global alias.smu "submodule update --init --recursive"
			  git config --global alias.sms "submodule status"
			  git config --global alias.sma "submodule add"
			  ~~~
		- One alternative to using git submodules is using a package manager like [[npm]] or [[pip]] and keeping the two repos separate, but including the child repo in the parent repo's package.json or whatever is the equivalent. Most package managers allow you to include a custom URL to a repo. So even if your library is private, you can still use this method. This might actually be less confusing for some teams.
			- ~~~
			  { 
			    "dependencies": {
			      "library1": "git+ssh://git@github.com/User/library1.git#v1.2.3"
			    }
			  }
			  ~~~
	- ## [[Video]]
		- {{video https://www.youtube.com/watch?v=JESI498HSMA}}
			- ### {{youtube-timestamp 0}} Introduction to Git Submodules
				- #### What Are Submodules?
					- Git submodules are a way to put one Git repository inside another, allowing you to have nested Git repos
					- Common use case: when your team has written a library that is shared among multiple different applications
					- Each submodule is **pinned to a specific commit**
				- #### Cloning Repositories with Submodules
					- When you clone a repo that includes submodules, the code in the submodule will **not be downloaded automatically**
					- To download everything, add the `--recursive` flag when cloning:
						- `git clone --recursive <repo-url>`
					- This ensures all submodules, including entire git history, are downloaded
					- Alternatively, if you've already cloned the repo, run from the parent repo's directory:
						- `git submodule update --init --recursive`
				- #### How Submodules Work
					- When you run `git submodule update --init --recursive`, Git:
						- Looks at the `.gitmodules` file (created automatically when submodule was first added)
						- Goes through added submodules in this file
						- Clones each submodule from the specified URL
						- Checks out the specific commit the submodule is pinned to
					- To see which commit hash the submodule is currently pinned to:
						- `git ls-tree HEAD <submodule-path>`
					- The commit hash is stored in the hidden `.git` folder of the parent repo (not in `.gitmodules`)
				- #### Recursive Flag
					- Sometimes a submodule can have another submodule nested in it
					- The `--recursive` flag ensures nested submodules are all downloaded as well
				- #### Submodule Behavior
					- Once downloaded, submodule behaves like a regular git repository
					- It doesn't have its own hidden `.git` folder like the parent repo
					- Instead has a `.git` file that points at the parent repo
					- Git commands from the submodule directory only affect that specific repo, not the parent repo
			- ### {{youtube-timestamp 136}} Making Changes to Submodules
				- #### The Detached Head Problem
					- Making changes to submodules is one of the **most confusing aspects** when working with submodules
					- Parent repo always pins the submodule to a specific commit hash
					- When Git downloads a submodule, it's put into a **detached HEAD state**
					- Detached HEAD means you've checked out a specific commit without any branch checked out
				- #### Switching to a Branch
					- To make changes properly, switch to the main branch (or appropriate branch):
						- `cd <submodule-directory>`
						- `git checkout main`
					- This switch doesn't change files since the commit is already the latest on main
					- The purpose is so when you commit changes, they get added to a new commit on the branch
				- #### Updating the Parent Repo
					- After committing changes in submodule, the parent repo doesn't know about the new commit yet
					- Running `git status` in the parent repo shows the submodule has changed
					- Another way this happens: running `git pull` in the submodule directory to get latest changes
					- To update the pinned commit in the parent repo:
						- Run `git add <submodule-path>` in the parent directory (like any other change)
						- Commit this change to the parent repo
						- You're telling the parent repo: change submodule from old commit hash to new commit hash
					- After pushing parent repo, the pinned commit changes on GitHub as well
			- ### {{youtube-timestamp 244}} Branching and Auto-Update Configuration
				- #### Switching Branches with Submodules
					- When switching branches in the parent repo, by default Git will **not automatically update the submodule**
					- Example: main branch has submodule pinned to commit A, older branch has it pinned to commit B
					- After switching branches, submodule should have old commit checked out, but Git won't do this automatically
					- Running `git status` in parent repo shows Git thinks there are newer commits in submodule
				- #### Manual Update Required (Old Git Versions)
					- To fix this, run: `git submodule update`
					- This moves the submodule state to the pinned commit
					- Also necessary when:
						- Switching to a branch where submodule didn't exist yet
						- Running `git pull` in the parent repo
					- In older versions of Git, you had to run `git submodule update` after all these operations, which was extremely annoying
				- #### Auto-Update Configuration (Newer Git Versions)
					- In newer versions of Git, you can configure automatic updates
					- Run these two commands once to enable in your global git config:
						- `git config --global submodule.recurse true`
						- `git config --global push.recurseSubmodules on-demand`
					- This makes submodules update automatically when you:
						- Switch branches
						- Run `git pull`
						- Run `git push`
					- **Highly recommended**: Update Git to latest version before working with submodules
				- #### Useful Aliases
					- Setting up aliases for common operations makes things easier:
						- `git config --global alias.smu "submodule update --init --recursive"`
						- `git config --global alias.sms "submodule status"`
						- `git config --global alias.sma "submodule add"`
			- ### {{youtube-timestamp 336}} Adding and Removing Submodules
				- #### Adding a Submodule
					- Run: `git submodule add <repo-url> <path>`
					- This will:
						- Download the submodule repo to the specified directory
						- Create the `.gitmodules` file if necessary
						- Add the new submodule to it
					- By default, submodule will be on the latest commit of the default branch (usually main)
					- To pin it to a different commit:
						- Switch to that commit or branch in the submodule directory
						- Then commit the change to the parent repo
				- #### Removing a Submodule
					- Run: `git rm <submodule-path>` and commit your changes
					- In older versions of Git, this required a few more steps, but latest version handles it automatically
			- ### {{youtube-timestamp 383}} Alternatives and Conclusion
				- #### Evaluation of Submodules
					- Under the hood, submodules are **really elegant and powerful**
					- Unfortunately, the user experience is **really confusing and awful**
					- Recent versions of Git have made working with them easier (thanks to auto-update settings)
				- #### Alternative 1: Package Managers
					- Use a package manager like [[npm]] or [[pip]] instead
					- Keep the two repos completely separate
					- Include the child repo in the parent repo's `package.json` (or equivalent)
					- Most package managers allow custom URLs to repos, even private ones
					- Example format:
						- ~~~
						  {
						    "dependencies": {
						      "library1": "git+ssh://git@github.com/User/library1.git#v1.2.3"
						    }
						  }
						  ~~~
					- **Recommendation**: Use this method over submodules if you're not already using them
					- Benefits:
						- Saves team from potential headaches
						- Uses tools team is already comfortable with
					- Limitation: Not always possible depending on package manager setup and programming language
				- #### Alternative 2: Monorepo Approach
					- Put all code in a single repo in separate modules
					- Comes with its own set of trade-offs