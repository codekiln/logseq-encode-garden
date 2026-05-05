logseq-entity:: [[Logseq/Entity/question]]

- # What is the difference between [[GitHub]] Direct Access, Organization Access, and Enterprise Access for a repository, and what changes when adding a [[GitHub/Team]] at the organization vs direct level?
	- ## Answer
		- [[AI/Response]]
			- ### The three access tiers
				- **Direct access** — Collaborators (individual users or teams) added explicitly to a specific repository. Managed from the repo's *Settings → Collaborators and teams* page. Any **repository admin** can add or remove direct collaborators. Shows under the "Direct access" tab.
				- **Organization access** — Access granted by an **organization owner** at the org level, usually by giving a team permission on a repository through the team's own *Repositories* settings. Shows under the "Organization access" tab on the repo. Repository admins **cannot** manage these entries; only org owners or team maintainers with appropriate rights can.
				- **Enterprise access** (preview) — Enterprise-level grants made by an **enterprise admin** that flow down to a repository. Visible on the "Enterprise access" tab. Intended for cross-org or enterprise-wide policies.
			- ### What changes when you add a GitHub Team at the organization level vs at the direct level
				- **Direct level (repo Settings → Add teams)**
					- The team entry appears in the **Direct access** tab.
					- Any repository admin can add/remove the team.
					- Access is scoped to this one repository; the team has no implied access to other repos.
					- Useful when a cross-functional team needs access to a repo but the org-wide team permissions are not (or should not be) the vehicle for it.
				- **Organization level (Org → Teams → [team] → Repositories)**
					- The team entry appears in the **Organization access** tab on the repo.
					- Only an org owner (or team maintainer with appropriate rights) can grant or revoke this access.
					- Granting at this level can cascade: if the org team has sub-teams, child teams inherit the permission.
					- Better for managing access at scale — changing the team's org-level repo list affects all repos at once rather than repo-by-repo.
			- ### Summary comparison
				- | Dimension | Direct access | Organization access |
				  |---|---|---|
				  | Who can grant | Repo admin | Org owner / team maintainer |
				  | Where it appears | Direct access tab | Organization access tab |
				  | Scope | Single repo | Configurable from team side |
				  | Sub-team inheritance | No | Yes (team hierarchy) |
				  | Typical use | Ad-hoc / per-repo grants | Structured, scalable team permissions |
			- ### References
				- [Managing teams and people with access to your repository — GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
				- [Adding or removing a team from a repository — GitHub Docs](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/managing-team-access-to-an-organization-repository)
