logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[mise/Environment]], [[mise/Config/mise.toml/env]]

- # In [[TOML]], is `false` a first-class primitive?
- ## Answer
	- [[AI/Response]]
		- **Yes.** The [TOML v1.0.0](https://toml.io/en/v1.0.0#boolean) spec defines **Boolean** as one of the allowed value types. Booleans are the lowercase tokens `true` and `false` (not quoted strings). A parser maps them to a boolean type in the host language, not to the string `"false"`.
		- **What is not a boolean in TOML:** Quoted values such as `'false'` or `"false"` are **strings**. Integers like `0`, empty strings, and omitted keys are separate types or absences; TOML has no general “falsey” coercion like JavaScript or the shell.
		- **Example host semantics ([[mise/Environment]]):** In `mise.toml` `[env]`, mise documents that assigning `false` **unsets** a variable (for example `NODE_ENV = false` removes a previously set `NODE_ENV`). That behavior is **mise’s interpretation** of a TOML boolean in the env table, not a universal TOML rule. See [Environments | mise](https://mise.jdx.dev/environments/) (“To clear an env var, set it to `false`”).
		- **Contrast with setting a value:** `NODE_ENV = 'production'` uses a TOML string; the shell receives the string `production`. Only the bare boolean `false` triggers unset semantics in mise env config—not the string `'false'`.
		- **Takeaway:** `false` is a first-class TOML boolean primitive; tools such as mise may assign extra meaning to that type in specific config sections.
