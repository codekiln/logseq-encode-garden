alias:: [[Codemod]]
tags:: [[Term]]

- # Codemod
	- a piece of code meant to modify another bit of code, typically used as part of a [[Software/Library/Upgrade]]
	- These can be multi-language [[Polyglot Codemod Engines]]
	- Or they can be single language, many of which are in this [[ChatGPT/Response]]
		- Codemod ecosystems cluster around language-specific [[Programming/Abstract/Syntax/Tree]] toolkits, but a handful are becoming de-facto standards across many codebases:
		- ## Snapshot
			- #Examples
				- [[OpenRewrite]] (Java → Groovy/Kotlin/XML/JSON & more)
				- [[jscodeshift]] (JavaScript/TypeScript), LibCST + Bowler (Python)
				- clang-tidy (C/C++)
				- Scalafix (Scala)
				- Coccinelle (C)
				- Roslyn analyzers (C#/VB)
				- Spoon (Java)
				- rustfix (Rust)
				- Rector (PHP)
			- These frameworks all expose reusable visitors, pattern-matching [[DSL]]s, and [[CLI]] runners that let you ship repeatable codemods at scale. ([OpenRewrite Docs](https://docs.openrewrite.org/reference/supported-languages), [GitHub](https://github.com/facebook/jscodeshift), [LibCST](https://libcst.readthedocs.io/en/latest/codemods.html), [GitHub](https://github.com/facebookincubator/Bowler), [CommandMasters](https://commandmasters.com/commands/clang-tidy-common/), [GitHub](https://github.com/scalacenter/scalafix), [GitLab](https://coccinelle.gitlabpages.inria.fr/website/), [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/tutorials/how-to-write-csharp-analyzer-code-fix), [Spoon](https://spoon.gforge.inria.fr/?utm_source=chatgpt.com), [Docs.rs](https://docs.rs/rustfix/latest/rustfix/), [GitHub](https://github.com/rectorphp/rector))
		- ## Poly-language & Enterprise Scale - see also [[Polyglot Codemod Engines]]
			- ### OpenRewrite
				- Recipe-based engine that rewrites Java, Kotlin, Groovy, XML, YAML, JSON and even Terraform/HCL through a common visitor API. ([OpenRewrite Docs](https://docs.openrewrite.org/reference/supported-languages))
				- Moderne’s SaaS runner layers org-wide scanning and security policies on top. ([OpenRewrite Docs](https://docs.openrewrite.org/reference/supported-languages))
		- ## [[JavaScript]] / [[Typescript]]
			- | Framework | Highlights |
			  | ---- | ---- | ---- |
			  | [[jscodeshift]] | Facebook-maintained CLI + recast backend; pattern helpers, VS Code debugger. [GitHub](https://github.com/facebook/jscodeshift) |
			  | **Babel codemod (via @babel/traverse)** | Write transforms directly on Babel AST; often wrapped by jscodeshift. |
			  | **TS-Morph** | Typed TypeScript AST with project-wide manipulation (not strictly a codemod runner but often used as one). |
		- ## #Python
			- [[Py/Lib/LibCST]] – lossless concrete syntax tree + “CodemodCommand” scaffolding and parallel runner. ([LibCST](https://libcst.readthedocs.io/en/latest/codemods.html))
				- [[My Note]]
					- [[2025-05-16 Fri]]
					  id:: 68271081-8f21-48fb-9540-6ccd21d7b6f2
						- used by [[Person/Eugene Yurtsev]] for [[LangChain/v/0/2]] release; [Upcoming 0.2 release (week of 05/20) · langchain-ai/langchain · Discussion #21437 · GitHub](https://github.com/langchain-ai/langchain/discussions/21437#discussioncomment-9423668) [[2024/05]]
							- someone suggested [[GritQL]] in this thread, and in [[LangChain/v/0/3/Migrate using langchain-cli]] they migrationed [that as of 0.3, they are using gritQL for the codemod engine](https://github.com/langchain-ai/langchain/discussions/21437#discussioncomment-9423668)
						- used by [[Person/Sebastian Ramirez]] for the [[Pydantic/v/1]] to [[Pydantic/v/2]] translator, [[Py/Lib/bump-pydantic]]; see [bump-pydantic/bump_pydantic/codemods/add_annotations.py at main · pydantic/bump-pydantic · GitHub](https://github.com/pydantic/bump-pydantic/blob/main/bump_pydantic/codemods/add_annotations.py)
			- **Bowler** – fluent query DSL built on fissix, good for large-scale refactors. ([GitHub](https://github.com/facebookincubator/Bowler))
		- ## #Java & JVM languages
			- **Spoon** – programmatic Java AST with code generation and transformation; integrates with Maven/Gradle. ([Spoon](https://spoon.gforge.inria.fr/?utm_source=chatgpt.com))
			- **OpenRewrite** (above) – brings codemods into build pipelines via Maven/Gradle plugins. ([OpenRewrite Docs](https://docs.openrewrite.org/reference/supported-languages))
		- ## C / C++
			- **clang-tidy/clang-tooling** – part of LLVM; custom checks double as codemods, fix-it hints can be auto-applied. ([CommandMasters](https://commandmasters.com/commands/clang-tidy-common/))
			- **Coccinelle** – SmPL semantic-patch language designed for Linux-kernel-scale collateral evolutions. ([GitLab](https://coccinelle.gitlabpages.inria.fr/website/))
		- ## C# / .NET
			- **Roslyn analyzers + CodeFix providers** – first-class in Visual Studio; write analyzers that emit diagnostics and auto-fixes. ([Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/tutorials/how-to-write-csharp-analyzer-code-fix))
		- ## Scala
			- **Scalafix** – integrates with sbt/mill; supports semantic rewrites using SemanticDB. ([GitHub](https://github.com/scalacenter/scalafix))
		- ## #Rust
			- **rustfix / cargo fix** – consumes `rustc` JSON suggestions to apply automated fixes, built into Cargo workflows. ([Docs.rs](https://docs.rs/rustfix/latest/rustfix/))
		- ## #PHP
			- **Rector** – rule-based refactoring engine covering PHP 5.3-8.x and frameworks like Symfony and PHPUnit. ([GitHub](https://github.com/rectorphp/rector))
		- ### Choosing a framework
			- **Language support & [[AST]] fidelity** – pick the one that preserves formatting (LibCST, Spoon) if diff minimalism matters.
			- **Ecosystem integration** – build-tool plugins (OpenRewrite, Scalafix, clang-tidy) ease CI rollout.
			- **Declarative vs imperative** – SmPL (Coccinelle) and OpenRewrite [[yaml]] recipes favor pattern matching; Bowler/jscodeshift give imperative control.
			- **Scale & parallelization** – [[Py/Lib/LibCST]], jscodeshift and OpenRewrite offer built-in parallel runners for monorepos.
		- These frameworks let you codify large-scale migrations—API changes, language upgrades, security fixes—into repeatable, review-friendly scripts instead of one-off search-and-replace.