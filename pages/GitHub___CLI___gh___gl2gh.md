logseq-entity:: [[Logseq/Entity/CLI/Command]]
see-also:: [[GitHub/CLI/gh]], [[GitHub/CLI/Extension]]
- # [gh gl2gh](https://github.com/github/gh-gl2gh)
	- **Usage:** `gh gl2gh <command> [flags]`
	- GitHub CLI extension for migrating repositories from GitLab to GitHub Enterprise Cloud through GitHub Enterprise Importer.
	- ## Commands
		- `inventory-report` — produce CSV reports of GitLab groups and projects to help plan a migration.
		- `migrate-repo` — migrate one GitLab project and its repository data to a GitHub repository.
		- `generate-script` — generate a script for migrating multiple GitLab projects.
		- `generate-mannequin-csv` — generate a CSV of imported GitLab users represented as mannequins.
		- `reclaim-mannequin` — associate imported content with its corresponding GitHub users.
		- ## Migration data
			- Git history, repository wiki, commit comments, issues and comments, merge requests converted to pull requests, reviewers and approvers, milestones, timeline events, emoji reactions, uploads, releases, release assets, and project members represented as mannequins.
			- Merge-request review comments become review comments when diff data is present; only the latest diff is included in the export. Threaded discussions become flat comments with context about the original thread.
		- ## Limits
			- The destination is an organization on GitHub Enterprise Cloud at github.com or ghe.com. GitLab-to-GitHub Enterprise Server migrations are not supported.
			- Git LFS pointer files migrate with the history, but the binary objects need a follow-up push. Repository policies, group settings, snippets, issue boards, time tracking, design-management data, CI/CD pipelines, vulnerability reports, webhooks, and job artifacts are not migrated.
		- ## Setup
			- Install or update the extension:
			- ~~~bash
			  gh extension install github/gh-gl2gh
			  gh extension upgrade github/gh-gl2gh
			  ~~~
			- The extension needs credentials for both GitLab and GitHub. It stages the GitLab export archive in GitHub-owned blob storage or an AWS S3/Azure Blob Storage account.
		- ## Source
			- [Migrate from GitLab to GitHub with GitHub Enterprise Importer — GitHub Changelog, August 3, 2026](https://github.blog/changelog/2026-08-03-migrate-from-gitlab-to-github-with-github-enterprise-importer/)
			- [Understand migrations from GitLab to GitHub — GitHub Docs](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrate-from-gitlab/understand-migrations)
