logseq-entity:: [[Logseq/Entity/Question]]

- # How can we sign in with [[Passkey]]s in [[ChatGPT/Cloud/Browser]]?
	- ## [[AI Answer]]
		- **Short answer:** OpenAI documents no passkey sign-in for websites in the cloud browser, as of [[2026-11-21 Sat]]. Use a password and one-time code in the secure sign-in form, or finish that site yourself.
		- OpenAI's only passkey article covers signing in to the OpenAI account itself ([Passkeys to secure your OpenAI account](https://help.openai.com/en/articles/20001039-passkeys-to-secure-your-openai-account)).
		- 1Password for Agents states that passkeys "aren't yet supported" ([support page](https://support.1password.com/1password-for-agents/), 2026-11-04).
		- Inference, untested: a passkey answers a challenge from the browser on the same device, and the cross-device QR flow needs the phone near the computer over Bluetooth. A remote cloud browser has neither, so expect passkey prompts there to fail.