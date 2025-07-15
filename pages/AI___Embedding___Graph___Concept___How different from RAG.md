alias:: [[AI/Embedding/Concept/How are Graph Embeddings different than traditional RAG]]
tags:: [[Diataxis/Concept]], [[Writing/Co-Written with AI]], [[o3]]

- # Graph Embeddings in [[Neo4j]] — Conceptual Overview
	- ## Overview
		- Graph embeddings are vectors that encode the structure and attributes of graph elements so that geometric proximity mirrors topological similarity.
	- ## Context
		- Neo4j’s Graph Data Science (GDS) library learns these vectors and stores them on nodes, enabling fast similarity search, link prediction, and hybrid retrieval-augmented generation (RAG) that combines structured and unstructured knowledge.
	- ## Key Principles
		- **Topology-aware representation** — embeddings capture paths, neighborhoods, and community structure rather than raw text.
		- **Algorithmic generation** — vectors come from graph algorithms such as FastRP, Node2Vec, and GraphSAGE, not from large language models.
		- **Native storage & indexing** — Neo4j writes embeddings back as `LIST<FLOAT>` properties and can build vector indexes for k-NN queries.
		- **Complement to text embeddings** — graph embeddings support relationship reasoning, while text embeddings capture semantic content; combining both powers “GraphRAG.”
	- ## Mechanism
		- **FastRP** projects higher-order adjacency information into a low-dimensional space using random projections, delivering production-scale speed.
		- **Node2Vec** performs biased random walks and trains a skip-gram model so nodes that co-occur in walks land near each other.
		- **GraphSAGE** samples neighbors and aggregates their features through a neural network, allowing inductive embeddings for unseen nodes.
		- After computation, embeddings can be indexed:
			- `CALL gds.fastRP.mutate('g', {embeddingDimension:128, mutateProperty:'embedding'});`
			- `CREATE VECTOR INDEX ON :Person(embedding);`
	- ## Examples
		- ~~~cypher
		  // 1. Project a social graph
		  CALL gds.graph.project(
		      'social',
		      'Person',
		      {FRIEND_OF: {orientation:'UNDIRECTED'}}
		  );
		  // 2. Generate FastRP embeddings
		  CALL gds.fastRP.mutate(
		      'social',
		      {embeddingDimension:128, mutateProperty:'embedding'}
		  );
		  // 3. Find nearest neighbours
		  CALL gds.knn.stream(
		      'social',
		      {topK:5, nodeProperties:['embedding']}
		  ) YIELD node1, node2, similarity;
		  ~~~
	- ## Misconceptions
		- *“Graph embeddings are just text embeddings stored in a graph.”*  
		  – They are learned from topology and attributes, independent of language models.
		- *“Embeddings remove the need for Cypher pattern matching.”*  
		  – They approximate similarity but cannot replace exact path queries where relationship semantics matter.
	- ## Related
		- # [[AI/RAG/Graph/Graph Vector]]
		- [[Neo4j/Blog/24/09/Enhancing Hybrid Retrieval with Graph Traversal Using the GraphRAG Python Package]]
		- [Fast Random Projection – Neo4j Graph Data Science](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/fastrp/) ([Graph Database & Analytics](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/fastrp/))
		- [Node2Vec – Neo4j Graph Data Science](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/node2vec/) ([Graph Database & Analytics](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/node2vec/))
		- [GraphSAGE – Neo4j Graph Data Science](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/graph-sage/) ([Graph Database & Analytics](https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/graph-sage/))
		- [Vector indexes – Cypher Manual](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/) ([Graph Database & Analytics](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/))