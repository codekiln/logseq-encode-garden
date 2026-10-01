logseq-entity:: [[Logseq/Entity/Trade-Off/Component]]
see-also:: [[Software/Inheritance]]

- Choosing single inheritance means each class has one parent; other reuse goes through interfaces, mixins, or [[Software/Composition]].
- **Gains** — one chain to read, no diamond, and member lookup that anyone can follow by walking up the chain.
- **Costs** — an object that is two kinds of thing must pick one parent and reach the other through an interface, a collaborator, or copied code.
- **Too far** — unrelated capabilities forced into one chain, producing base classes that collect everything any descendant might need.
