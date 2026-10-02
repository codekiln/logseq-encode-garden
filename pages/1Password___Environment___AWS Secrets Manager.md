tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[1Password/Environment]]

- # [Sync secrets from 1Password to AWS Secrets Manager (beta)](https://www.1password.dev/environments/aws-secrets-manager)
	- ## Overview
		- A beta integration that copies the variables of a [[1Password/Environment]] into a single secret in AWS Secrets Manager and keeps it current. [[1Password]] stays the place where the values are edited; AWS holds a copy that workloads on AWS can load with any of AWS's own methods.
		- Source: the [1Password Developer page](https://www.1password.dev/environments/aws-secrets-manager), read on 2026-10-02.
	- ## Context
		- It is the opposite end of the Environment's other outputs. A [[1Password/Environment]] can be mounted as a local `.env` file or read through the CLI, SDKs and [[1Password/Environment/MCP]] on a developer machine. This integration pushes it to a cloud secret store instead.
		- Requirements: the desktop app, an Environment, and an AWS account where you can create IAM resources.
	- ## Key Principles
		- One-way. Changes made in AWS Secrets Manager are never synced back to 1Password.
		- One definitive copy. 1Password recommends keeping a single authoritative copy of each secret, either as an item or as an Environment variable, since several copies drift.
		- Set up once per Environment. Only the person creating the IAM resources needs AWS credentials. Afterwards, teammates invited to edit the Environment can change variables without any AWS access.
		- Anything that auto-rotates in AWS should stay managed there, otherwise the two sides disagree. See [[AWS/Secrets Manager/Secret/Rotation]].
	- ## Mechanism
		- 1Password does the syncing from its Confidential Computing platform, built on AWS Nitro Enclaves, so the sync runs always-on and not from anyone's laptop.
		- It authenticates to AWS with SAML federation, not with stored access keys. Setup creates these pieces:
			- 1. A SAML identity provider in AWS IAM, registered from a `saml-metadata.xml` file downloaded from 1Password.
			- 2. An IAM policy that allows `secretsmanager:DescribeSecret`, `RestoreSecret`, `PutSecretValue`, `CreateSecret`, `DeleteSecret`, `TagResource` and `UpdateSecret`.
			- 3. An IAM role that trusts the SAML provider, constrained by a `SAML:sub` `StringEquals` condition holding the subject 1Password shows on its configuration page.
		- In 1Password the role and provider ARNs are pasted into the Environment's AWS Secrets Manager card, along with a target region and a target secret name. The name defaults to the Environment's name and must be unique within AWS. An optional KMS key ID or ARN makes AWS encrypt with that key; the role then needs KMS permissions too.
		- **Test connection** creates and immediately deletes a placeholder secret, to confirm the permissions work. Then the toggle enables syncing.
		- After that, saving a change to the Environment triggers another sync.
		- The Environment's variables land together in one AWS secret, so the Environment, not each variable, is the unit that maps to a secret.
	- ## Examples
		- Stopping: toggle the integration to Disabled to pause it, or use the ellipsis menu and Delete integration to remove it.
		- Size: a 64 KB limit applies. A large Environment can be split into several, each with its own integration and its own target secret.
		- Common failures the page lists: missing role permissions, a failed role assumption (SAML provider or trust policy wrong), a SAML subject that doesn't match the trust policy, a target name already used in AWS, an invalid KMS key, and an exceeded Secrets Manager quota.
	- ## Misconceptions
		- It does not keep AWS as a source of truth. Edits made in AWS are never copied back to 1Password. The page doesn't say what a later sync does to them, so treat them as unsafe.
		- Deleting the integration is how you stop syncing. The page doesn't say whether the AWS secret is removed when you do.
		- It is not part of the local `.env` mount feature, so the ten-mount limit per device does not apply to it.
