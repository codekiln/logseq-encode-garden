logseq-entity:: [[Logseq/Entity/Trade-Off/Component]]
see-also:: [[Software/Composition]]
- Choosing composition here means building behavior from collaborators connected through explicit interfaces or delegated calls.
- **Gains** — independent variation and focused tests; a collaborator can often be replaced without changing the containing object's place in a type hierarchy.
- **Costs** — additional interfaces, forwarding methods, and wiring. The flow of behavior may be less obvious when spread across collaborators.
- **Too far** — a web of tiny objects and indirection that makes ordinary behavior hard to trace.
