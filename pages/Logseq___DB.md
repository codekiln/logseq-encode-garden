alias:: [[LogseqDB]]
tags:: [[SQLite]]

- # Database version of Logseq
	- https://github.com/logseq/logseq#-database-version
	- The Database version (DB version) of Logseq introduces DB graphs. [See this page](https://github.com/logseq/docs/blob/master/db-version.md) to get an overview of the main features for DB graphs. If you are an existing user, [see changes with the DB version](https://github.com/logseq/docs/blob/master/db-version-changes.md). The DB version has its own new mobile app (on iOS, with Android coming soon)! To participate in the mobile app alpha, [please complete this brief form](https://forms.gle/nfefJv51jUuULbFB9). The DB version also has a new sync approach, RTC (Real Time Collaboration)! You can use it to sync graphs between multiple devices or collaborate with others. To participate in the RTC alpha, [please fill out this form](https://forms.gle/YSyF4WfKPSDuwyjH6).
	- The DB version is in beta status while the new mobile app and RTC is in alpha. This means that **data loss is possible** so we recommend [automated backups](https://github.com/logseq/docs/blob/master/db-version.md#automated-backup) or [regular SQLite DB backups](https://github.com/logseq/docs/blob/master/db-version.md#graph-export). We recommend you create a dedicated test graph and choose one project that’s not crucial for you.
	- To get started with the DB version:
	- To try the latest web version, go to [https://test.logseq.com/](https://test.logseq.com/).
	- To try the latest desktop version, go to [https://github.com/logseq/logseq/releases/tag/nightly](https://github.com/logseq/logseq/releases/tag/nightly) and download the artifact for your operating system.
	- To try the latest by building from the source code
		- Use `test/db` for stable releases. Fewer bugs and slower updates. Update frequency: days or weeks.
		- Use `master` for the latest updates as they are developed. Expect more bugs and faster changes. Update frequency: hours or days.