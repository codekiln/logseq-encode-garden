- [GitHub Stacked PRs](https://github.github.com/gh-stack/)
	- The TLDR: Break large changes into small, reviewable pull requests that build on each other — with native GitHub support and the `gh stack` CLI.
	- > Stacked PRs is currently in private preview. This feature will not work unless enabled for your repository. Sign up for the waitlist →
		- ```
		  gh extension install github/gh-stack
		  gh stack alias
		  gs init auth-layer
		  gs add api-routes
		  gs add frontend
		  gs push
		  gs submit
		  ```