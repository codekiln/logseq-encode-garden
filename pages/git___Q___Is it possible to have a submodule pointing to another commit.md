tags:: [[Question]]

- # Is it possible to have a [[git/submodule]] which points to a different commit of the same git repo?
	- Use case: [[langgraph/Platform]] allows deploying more than one AI graph at once, as long as there are separately addressable python applications. If it was possible to have a submodule in a `<ai-app-name>-prod` folder which pointed to a specific commit, then two versions of the same application could be accessed in one [[langgraph/Platform/Deployment]].
	- ## Answer - Not possible with a single repo; must use two repos
		- It's possible to accomplish this with **two** repos:
			- `ai-app-impl`
				- `v1` tag
				- `v2` tag
			- `ai-app` - this is a single deployment
				- `ai-app-prod/` (`graph_id` `ai-app-prod`)
					- git submodule that points to `ai-app-impl@v1`
				- `ai-app-stage/` (`graph_id` `ai-app-stage`)
					- git submodule that points to `ai-app-impl@v2`
			-