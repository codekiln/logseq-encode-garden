alias:: [[Git-Friendly Task Management]]
tags:: [[Term]]

- # [[git/Friendly]] Task Management
	- This is a class of software products that
		- represent hierarchies of tasks along with their statuses
		- in such a way that it can be committed to git
		- and used by parallel AI agents on different machines without significant merge conflicts
		- is
			- [[Offline/First]]
			- [[Local/First]]
		- is **NOT**
			- based on a local database in a way that is incompatible with storing it in git in a way that avoids merge conflicts by design
				- e.g. don't rely on [[SQLite]] binary database files put in naively in git or git lfs or tell users they can periodically do a bulk export without explicit guidance on supporting every task landing in git in a flat file
					- for example, [[td]] takes the sqlite approach, and I wouldn't consider it "Git-Friendly"
			- based on a cloud provider like [[Linear]], [[JIRA]], [[GitHub/Issue]]s