logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Knowledge/Garden]]

- # Graph database
	- ## Overview
		- A **graph database** stores data as **nodes** and **relationships** (edges), with properties on both, so the primary question is *what connects to what* rather than *which row matches this key*.
		- It matters when the interesting fact is the link: a knowledge garden's wikilinks, a social graph, a bill of materials, or a fraud ring are cheaper to traverse as edges than to reconstruct with joins.
	- ## Context
		- Contrasts with a table store (rows and foreign keys) and with a document store (nested trees). A graph engine treats adjacency as a first-class index.
		- This garden already uses the metaphor: journaling is [[Chron/ological/Order]]; knowledge gardening clusters related pages the way a graph clusters neighbors — *what goes where* more than *what happened*.
	- ## Key Principles
		- **Nodes and relationships are data** — the edge is not an afterthought join; it has a type and can carry properties.
		- **Local traversal** — queries walk neighborhoods (friends-of-friends, citation chains) without scanning the whole store.
		- **Index-free adjacency (ideal)** — each node knows its neighbors directly; cost grows with the walk, not with table size.
	- ## Mechanism
		- Two common models: **labeled-property graphs** (nodes/edges with labels and maps of properties) and **RDF triples** (subject–predicate–object).
		- Query languages include Cypher / GQL, Gremlin, SPARQL, and vendor languages such as AQL.
	- ## Examples
		- [[Neo4j]] — native property graph; Cypher; the engine most cited in this garden.
		- [[ArangoDB]] — multi-model (document + graph + key-value).
		- [[Amazon Neptune]] — managed graph on AWS (property graph and RDF).
		- [[JanusGraph]] — distributed open-source graph over Cassandra/HBase, queried with Gremlin.
	- ## Misconceptions
		- "A graph database is a knowledge graph" — **False**; a knowledge graph is a modeled web of meaning; a graph database is one way to store it.
		- "Graphs replace SQL" — **Oversimplified**; they win on relationship-heavy queries and lose on simple tabular aggregates unless the product is multi-model.
