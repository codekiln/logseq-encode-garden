logseq-entity:: [[Logseq/Entity/Question]]

- # What [[AWS]] services aid in upgrading OS packages to remediate security vulnerabilities?
	- ## [[AI Answer]]
		- **Short answer:** [[AWS/SSM]] Patch Manager is the primary service; [[AWS/Inspector]] identifies which packages are vulnerable but does not apply patches.
		- **[[AWS/SSM]] Patch Manager** automates OS-level patching across managed instances:
			- Define *patch baselines* — lists of approved/auto-approved patches per OS
			- Schedule patch runs inside *maintenance windows*
			- Executes the `AWS-RunPatchBaseline` SSM document on registered targets
			- Generates patch compliance reports in the SSM console
		- **[[AWS/SSM]] Run Command** — ad-hoc package upgrades via shell commands on one or many instances without SSH/RDP
		- **[[AWS/SSM]] State Manager** — continuously enforces a desired patch state by re-running associations on a schedule
		- **[[AWS/Inspector]]** scans EC2 instances and Lambda functions for CVEs (software package vulnerabilities) and surfaces *what* needs patching, but does not apply patches
		- **[[AWS/Security Hub]]** aggregates Inspector findings and other security signals for centralized visibility and remediation tracking
