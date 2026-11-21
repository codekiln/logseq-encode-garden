alias:: [[Credential Management]]
tags:: [[Term]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Term]]
see-also:: [[Password/Manage/ment]], [[Secret/Management]]

- # Credential Management
	- [[Definition/My]]
		- The practice of storing, issuing, using, rotating and revoking the things that prove an identity to a system: [[Password]]s, [[Passkey]]s, API keys, tokens, certificates and one-time codes.
	- ## Overview
		- [[Password/Manage/ment]] covers one kind of credential. Credential management covers all of them, including the ones a person never types, such as an OAuth token a site hands back after sign-in, or a passkey held in a device's secure hardware.
		- Tools in this space include password managers such as [[1Password]], platform keychains, and [[Secret/Manager]]s for software.
	- ## Key principles
		- **Least privilege** — a credential grants only the access its holder needs.
		- **Short lifetime** — a credential that expires soon limits the damage when it leaks.
		- **Separation** — the credential stays with the holder that uses it; it is handed over only as a reference or a scoped grant.
		- **Revocation** — the owner can cancel a credential without changing every other one.
	- ## Mechanism
		- A credential has a lifecycle: it is created or enrolled, stored, presented at sign-in, refreshed or rotated, and finally revoked.
		- A *secret* credential, such as a password, works by the holder knowing something the system can check. A *key pair* credential, such as a passkey, works by the holder proving possession of a private key that never leaves the device.
	- ## Credentials and [[AI/Agent]]s
		- An agent acting for a person needs a way to sign in without the person pasting a password into the agent. The options in use are: the person signs in and hands over the session, the agent receives a scoped token, or a password manager fills the field without revealing the secret to the agent.
		- Payments raise the same question; see [[Pay/ment/Manage/ment]].
