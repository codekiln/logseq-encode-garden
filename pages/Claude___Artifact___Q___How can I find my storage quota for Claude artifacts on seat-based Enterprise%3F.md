logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Artifact/Q/How much storage comes with Claude artifacts?]]

- # How can I find my storage quota for Claude artifacts on seat-based Enterprise?
	- ## [[AI Answer]]
		- **Short answer:** I found no page that shows an artifact storage quota, because Anthropic publishes none for Enterprise. What you can see are usage limits and spend. For a stored-bytes figure, ask your Anthropic account team.
		- [[Answer/Official]] from [Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans).
			- The guide describes no storage quota and no page where storage is shown.
			- **Organization settings > Artifacts** turns artifacts, templates, and sharing on or off. It shows no usage figures.
			- Artifact activity draws from each user's seat session and weekly limits, shared with the rest of Claude. There is no separate allowance.
			- [Usage analytics](https://support.claude.com/en/articles/12883420) cover only claude.ai/design, not artifacts made in conversations.
			- The Compliance API lists artifacts and retrieves a version's content, so it can be used to inventory them. It reports no quota.
		- **Where to look for usage**
			- **Organization settings > Usage** shows who is blocked or near a limit and, per [Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans), lets Owners set spend limits for the organization, per seat tier, or per member. Labels may differ in your console.
			- **Organization settings > Data and privacy** sets how long artifacts are kept before deletion.
		- **Unverified:** Whether an organization-wide cap on uploaded assets exists. I found none published.
