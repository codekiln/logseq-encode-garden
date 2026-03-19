alias:: [[BIP-39 bitcoin improvement proposal to make human-readable mnemonic phrase for random entropy]]

- # BIP-39 bitcoin improvement proposal to make human-readable mnemonic phrase for random entropy
	- **BIP-39** (Bitcoin Improvement Proposal 39) is a standard for encoding random entropy into a **human-readable mnemonic phrase**—typically used to back up and recover cryptocurrency wallets.
	- ## Core idea
		- It converts a binary seed (random bits) into a sequence of **common English words** like:
		- ~~~
		  abandon ability able about above absent absorb abstract absurd abuse access accident
		  ~~~
		- This phrase can later be converted back into the exact same seed.
	- ## How it works (simplified)
		- **Generate entropy**
			- 128–256 bits of randomness
		- **Add checksum**
			- A few bits derived from a hash of the entropy
		- **Split into chunks**
			- Each chunk is 11 bits
		- **Map to words**
			- Each 11-bit value indexes into a fixed list of **2048 words**
	- ## Key properties
		- **Deterministic**
			- Same phrase → same seed → same wallet
		- **Word list (2048 words)**
			- Carefully designed:
				- No ambiguous words
				- No homophones
				- First 4 letters uniquely identify each word
		- **Error resistance**
			- Checksum helps detect mistakes
		- **Human-friendly**
			- Easier to write down, say aloud, and remember than hex strings
	- ## Typical sizes
		- | Words | Entropy |
		  | ---- | ---- |
		  | 12 | 128-bit |
		  | 15 | 160-bit |
		  | 18 | 192-bit |
		  | 21 | 224-bit |
		  | 24 | 256-bit |
	- ## Where it's used
		- Bitcoin, Ethereum, and most crypto wallets
		- Hardware wallets (Ledger, Trezor)
		- Any system needing **portable, human-readable secrets**
	- ## Why it shows up in that GitHub issue
		- The proposal is repurposing BIP-39 for **ID generation**:
		- Instead of: `bd-x7q`
		- Use: `bd-calm-fox`
		- Because the word list is:
			- easy to dictate
			- easy to remember
			- globally standardized
			- already optimized for human communication
	- ## Important distinction
		- BIP-39 is:
			- **not encryption**
			- **not a wallet format itself**
		- It's just a **mapping layer**:
		- ~~~
		  entropy ↔ mnemonic words ↔ seed (via PBKDF2)
		  ~~~