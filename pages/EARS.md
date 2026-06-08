logseq-entity:: [[Logseq/Entity/concept]]
alias:: [[Easy Approach to Requirements Syntax]]
see-also:: [[Product Requirements Document]], [[OpenSpec]], [[AI/Coding/Technique/Spec-Driven Dev]]

- # EARS — Easy Approach to Requirements Syntax
	- Lightweight requirements-writing notation developed by [[Person/Alistair Mavin]] and colleagues at Rolls-Royce PLC (first published 2009) to help teams write requirements that are unambiguous, testable, and consistent — without a full formal specification language.
	- Popular in systems engineering, safety-critical systems, and [[AI/Coding/Technique/Spec-Driven Dev]] workflows.
	- ## Core Patterns
		- ### Ubiquitous
			- Always-true requirements.
			- Pattern: `The <system> shall <response>.`
			- Example: *The system shall display the user's account balance.*
		- ### Event-Driven
			- Pattern: `When <trigger>, the <system> shall <response>.`
			- Example: *When the user clicks "Save", the system shall persist the document.*
		- ### State-Driven
			- Pattern: `While <state>, the <system> shall <response>.`
			- Example: *While the user is authenticated, the system shall allow profile updates.*
		- ### Optional Feature
			- Pattern: `Where <feature>, the <system> shall <response>.`
			- Example: *Where two-factor authentication is enabled, the system shall require a verification code.*
		- ### Unwanted Behavior (Error Handling)
			- Pattern: `If <error condition>, the <system> shall <response>.`
			- Example: *If payment processing fails, the system shall display an error message and preserve the shopping cart.*
		- ### Complex (Combined)
			- Patterns can be combined freely.
			- Example: *While a user is logged in, when they upload a file, the system shall scan it for malware.*
	- ## Why AI Coding Workflows Prefer EARS
		- AI coding assistants perform better when requirements are explicit, atomic, testable, and structured.
		- Each EARS requirement maps to one behavior, one trigger/condition, and one response — making it straightforward to derive implementation tasks and acceptance tests from.
		- Vague: *Users should be able to upload files securely.*
		- EARS: *When a user uploads a file, the system shall scan the file for malware before storing it.*
	- ## Relationship to Spec-Driven Dev
		- EARS fits into [[AI/Coding/Technique/Spec-Driven Dev]] pipelines: Idea → EARS Requirements → Design → Tasks → Implementation → Tests.
		- [[OpenSpec]] and [[Person/forztf/GitHub/open-skilled-sdd]] both use EARS in their proposal/specification workflows.
