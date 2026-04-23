tags:: [[CLI/Tool]]
created-by:: [[Person/Jeff Dickey]]

- [fnox — Fort Knox for your secrets](https://fnox.jdx.dev/) [^1]
	- **fnox** is a secrets manager CLI from [[Person/Jeff Dickey]] (same author as [[mise]]), aimed at developer workflows around a checked-in `fnox.toml`.
- Repo: [[Person/Jeff Dickey/GitHub/fnox]]
- ## What it does
	- Manages secrets with **encryption**, **cloud / vault providers**, or **both** in one config file you can keep in version control.
	- Each secret picks a **provider** (for example age ciphertext in the file, or a reference resolved from AWS, GCP, Azure, [[1Password]], Bitwarden, Infisical, Doppler, HashiCorp Vault, Unix `pass`, OS keychain, and others). [^1]
	- **Shell integration** can auto-load secrets when you `cd` into a directory that contains `fnox.toml` (`fnox activate` for bash, zsh, fish; see upstream docs for Nushell). [^1]
	- **Profiles** support different secret sets for dev, staging, production, and custom environments. [^1]
- ## Typical commands
	- `fnox init` — scaffold config in a repo
	- `fnox set` / `fnox get` — write or read a secret through configured providers
	- `fnox exec -- <command>` — run a subprocess with secrets injected as environment variables (similar ergonomics to other “run with secrets” CLIs)
- ## Comparison in this graph
	- [[fnox/vs/secretspec]] — detailed contrast with [[secretspec]]
- ## Footnotes
	- [^1]: https://fnox.jdx.dev/
