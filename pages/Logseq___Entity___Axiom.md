logseq-entity:: [[Logseq/Entity/Definition]]

- # Axiom
	- In this garden, **Axiom** pages model statements that hold by **proof or by physical law**—provable with internal consistency within a formal system (mathematical or logical axioms), or established laws of nature with predictive force. This is the contrast class to [[Logseq/Entity/Named Law]]: not a shortcut, and not defeasible by gaming or fashion.
	- ## When we treat something as an axiom entity
		- Strong signals: the statement is **derivable or provable** within a formal system, or it is an **empirically established law of physics** that makes testable predictions and is not expected to be gamed away or to expire with changing incentives.
		- Good fit: mathematical and logical axioms, conservation laws, the laws of thermodynamics.
		- This type is expected to be **sparse**; its job is to make the heuristic-versus-axiom distinction structural rather than to catalog every theorem.
	- ## Relationship to other types
		- [[Logseq/Entity/Named Law]] — the "masquerading as laws" category: eponymous laws, effects, and fallacies that are useful but defeasible. When something is *called* a law but can be gamed, can expire, or admits exceptions, it is a **named law**, not an axiom.
		- [[Logseq/Entity/Concept]] — use when the goal is an understanding-oriented essay rather than anchoring a single provable statement. The distinction itself is explained at [[Epistemics/Concept/Heuristic vs Axiom]].
		- [[Logseq/Entity/Term]] — glossary stubs only.
	- ## Finding and deduplicating
		- Search for an existing page before creating a new axiom entity: exact title, common name of the law, and the field it belongs to. Classify as: **existing**, **similar**, **new**, or **blocked**.
	- ## Frontmatter
		- On instances, set **`logseq-entity:: [[Logseq/Entity/Axiom]]`** so this type page collects backlinks to every axiom entity.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- Logseq Flavored Markdown; lean. Suggested shape: H1 with the name; a one-line **statement**; the **system or domain** it holds in; and **see-also** links.
