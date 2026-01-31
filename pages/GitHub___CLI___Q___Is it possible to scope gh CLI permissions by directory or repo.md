# DOING is it possible to scope the `gh` command so that the permissions it has in one directory are different than the permissions it has in another directory?
:LOGBOOK:
CLOCK: [2025-02-21 Fri 05:19:05]
:END:
	- ## Impetus
		- [[CursorAI/Agent]] can invoke the #gh when instructed to do so in a [[CursorAI/Project Rule]]. It would be great if the `gh` cli permissions could be locked down to modifying just the assets associated with a certain repo.
	- ## Follow-up #Questions
		- ### DOING Is it possible that the GitHub CLI access token could source an [[EnvVar/.env]] file in the current repo to obtain a [[GitHub Personal Access Token]] that's scoped to the current repository?
		  :LOGBOOK:
		  CLOCK: [2025-02-21 Fri 05:19:16]
		  :END:
			- #Theoretical - this could be possible with [[GitHub/CLI/EnvVar/GH_TOKEN]]
				- we could create a wrapper script that implements behavior akin to [[Pyenv/.python-version]]
		- TODO how might we quickly provision scoped, temporary [[GitHub Personal Access Token]]s?
			-