logseq-entity:: [[Logseq/Entity/Trade-Off/Component]]
see-also:: [[Software/Inheritance/Multiple]]

- Choosing multiple inheritance means a class may name several parents and inherit members from each.
- **Gains** — an object that is several kinds of thing at once inherits from each kind directly, with no copied code and no wrapper objects.
- **Costs** — two parents can define the same member, and a shared ancestor can be reached by two paths, the diamond problem. Reading the class means knowing the resolution order to see where a member comes from.
- **Too far** — a tangled graph of parents where reordering the list of bases silently changes behavior.
