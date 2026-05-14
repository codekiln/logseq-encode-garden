logseq-entity:: [[Logseq/Entity/Software/Project]]
tags:: [[CLI/Tool]], [[Go]]
created-by:: [[Person/Shunsuke Suzuki]]

- # [ghtkn](https://github.com/suzuki-shunsuke/ghtkn)
	- CLI that mints **short-lived (about eight-hour) GitHub App user access tokens** through the **device authorization flow**, stores them in the OS secret manager, and prints or injects them for tools such as [[GitHub/CLI]] (`GH_TOKEN`).
	- Intended for **interactive local development** (not CI): only a GitHub App **client ID** is required in config—no client secret or app private key for ordinary use.
	- See [[mise/Tool/GitHub Token]] and [[mise/Tool/GitHub Token/Native GitHub OAuth]] for how **`ghtkn`** fits mise’s GitHub token stack (including **`credential_command`** and mise’s own experimental native OAuth).
