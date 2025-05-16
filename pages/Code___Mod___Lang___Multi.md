alias:: [[Multi-Language CodeMod Tool]], [[Multi-Language CodeMod Tools]], [[Polyglot Codemod Engine]], [[Polyglot Codemod Engines]]
tags:: [[Programming/Code/Mod]]

- # Polyglot Codemod Engines
	- [[ChatGPT/Response]]
		- Tools that call themselves *language-agnostic codemod engines* (often marketed as “polyglot” or “structural search-and-rewrite” frameworks) sit on top of parsers like Tree-sitter and give you one DSL to query / rewrite many languages. Besides OpenRewrite, the main players are:
		- | Engine | Core idea | Out-of-the-box languages* |
		  | ---- | ---- | ---- |
		  | **Grit (GritQL)** | SQL-ish query language + declarative rewrites, SaaS & CLI | JS/TS, Python, Go, Rust, Java, Terraform, SQL, CSS, Markdown, YAML, … 12+ [GitHub](https://github.com/getgrit/gritql)[Elite AI Tools](https://eliteai.tools/tool/grit?utm_source=chatgpt.com) |
		  | **Comby** | Lightweight templates → structural search/replace; no per-lang boilerplate | “~every language” via heuristics + specific parsers [comby.dev](https://comby.dev/)[comby.dev](https://comby.dev/) |
		  | **AST-grep** | Tree-sitter-based grep/replace with intuitive code-as-pattern DSL | 30+ TS grammars; add your own quickly [GitHub](https://github.com/codemod-com/ast-grep-custom-languages) |
		  | **Semgrep + Autofix** | Pattern-matching rules with optional `fix:` block; same rule file works across all supported parsers | 35+ languages (C, Python, Swift, Kotlin, etc.) [Semgrep](https://semgrep.dev/docs/writing-rules/autofix) |
		  | **Codemod.com Studio** | AI-assisted UI that emits deterministic AST-grep scripts | same list as AST-grep (it’s the engine under the hood) [codemod.com](https://codemod.com/?utm_source=chatgpt.com)[docs.codemod.com](https://docs.codemod.com/codemod-studio?utm_source=chatgpt.com) |
		  | **GitHub CodeQL Autofix** | Semantic security queries + LLM-generated fixes; polyglot IR | C/C++, C#, JS/TS, Java, Kotlin, Python, Ruby, Swift (growing) [The GitHub Blog](https://github.blog/changelog/2024-09-17-now-available-for-free-on-all-public-repositories-copilot-autofix-for-codeql-code-scanning-alerts/?utm_source=chatgpt.com)[The GitHub Blog](https://github.blog/changelog/2024-08-14-copilot-autofix-for-codeql-code-scanning-alerts-is-now-generally-available/?utm_source=chatgpt.com) |
		  | **Code Property Graph (CPG)** | Graph DB over AST+CFG; you can write traversal scripts that mutate code | multi-language IR, research/enterprise focus [GitHub](https://github.com/ShiftLeftSecurity/codepropertygraph) |
			- *Engines inherit new languages whenever Tree-sitter (or an equivalent parser) adds one, so coverage keeps expanding.
		- ### Other honorable mentions
			- **Tree-sitter query + rewrite prototypes** – experimental; you write a matcher and feed edits back to the tree. Good for bespoke tasks but no turnkey CLI. [Tree-sitter](https://tree-sitter.github.io/tree-sitter/creating-parsers/1-getting-started.html)
			- **OpenRewrite** – the widest JVM/ecosystem coverage plus YAML “recipes,” but outside JVM it only touches config formats (YAML/JSON/HCL). [OpenRewrite Docs](https://docs.openrewrite.org/reference/supported-languages)
			- **CLI SSR built into IDEs** – VS Code / IntelliJ structural replace; handy but not scriptable at repo scale. [Tabnine](https://www.tabnine.com/blog/code-refactoring-tools-7-popular-tools-why-you-need-them/?utm_source=chatgpt.com)
		-