logseq-entity:: [[Logseq/Entity/Trade-Off/Component]]
see-also:: [[Software/Inheritance]]
- Choosing inheritance here means specializing a parent class or prototype to reuse behavior and, where justified, express an [[Software/Inheritance/Is-A]] relationship.
- **Gains** — shared implementation and a direct extension point when the specialization preserves the parent's contract.
- **Costs** — tighter coupling to the parent and its method-resolution rules; a change in shared behavior can affect every descendant.
- **Too far** — a deep hierarchy built for code reuse, even when some descendants cannot honor the behavior their parent promises. [[Software/Subtyping]] explains the resulting substitution problem.
