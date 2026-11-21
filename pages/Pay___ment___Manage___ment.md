alias:: [[Payment Management]]
tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Diataxis/Explanation]]
see-also:: [[Credential/Manage/ment]]

- # Payment Management
	- ## Overview
		- Payment management is a feature of software systems that lets a person store, choose, update and remove the payment methods the system may charge, and see what was charged.
		- It appears in online stores, subscription services, app stores, ride-share and food apps, browsers, operating-system wallets, and now in [[AI/Agent]] products that buy things for a person.
	- ## Context
		- Before saved payment methods, a buyer typed a card number into every checkout. Saving the card once made repeat purchases fast, and moved the risk to whoever stores it.
		- Card networks answered that risk with the PCI DSS rules for anyone who stores card numbers, and later with **network tokens**: the merchant stores a token that only works for that merchant, while the real card number stays with the card network or wallet.
		- Wallets such as Apple Pay and Google Pay moved the stored card into the device or the platform account, so a merchant never sees the card number at all and the buyer approves each charge with a fingerprint, face or device passcode.
	- ## Key principles
		- **Who holds the card** — the merchant, a payment processor, a wallet, or a password manager. The fewer parties that hold the real card number, the less there is to leak.
		- **Who approves a charge** — a saved card can be charged with no step from the buyer, or each charge can need an approval step, a biometric check, or a 3-D Secure challenge from the bank.
		- **Limits** — spending caps, single-use or merchant-locked virtual cards, and per-transaction approval bound what a stolen or misused method can cost.
		- **Visibility and revocation** — the buyer can see each charge and remove a method or a token without cancelling the card.
	- ## Mechanism
		- A typical flow: the buyer adds a method once; a processor such as Stripe stores it and returns a token; at checkout the system charges the token; the bank may ask the buyer to approve the charge; the system shows a receipt and keeps a history.
		- Subscription billing, the money a service charges its own user, uses the same parts. It differs from purchases the service makes from *other* merchants on the user's behalf.
	- ## Payment management for [[AI/Agent]]s
		- An agent that pays for things needs a payment method it can use without seeing a card number it could leak or misuse.
		- As of November 2026 the approaches in use are a wallet the agent draws on, with a network token per merchant and the person's biometric approval on each purchase, as in [[ChatGPT/Wallet]]; a checkout the merchant and the AI vendor build together around a payment token scoped to one purchase, as in OpenAI's 2025 Instant Checkout; and a browser agent that reaches the merchant's checkout and pauses for the person to enter or approve the payment, as in [[ChatGPT/Cloud/Browser]].
		- The same split appears in [[Credential/Manage/ment]]: the agent gets a scoped, short-lived grant, and the long-lived secret stays with the person or their wallet.
		- [[ChatGPT/Q/Does ChatGPT have any payment management?]] looks at what [[ChatGPT]] offers.
