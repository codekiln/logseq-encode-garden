# TODO is it possible to scope the `gh` command so that the permissions it has in one directory are different than the permissions it has in another directory?
	- ## Impetus
		- [[CursorAI/Agent Mode]] can invoke the [[GitHub/CLI]] when instructed to do so in a [[CursorAI/Project Rule]]. It would be great if the `gh` cli permissions could be locked down to modifying just the assets associated with a certain repo.
	- ## Follow-up #Questions
		- TODO Is it possible that the GitHub CLI access token could source an [[EnvVar/.env]] file in the current repo to obtain a [[GitHub Personal Access Token]] that's scoped to the current repository?
		- TODO how might we quickly provision scoped, temporary [[GitHub Personal Access Token]]s?