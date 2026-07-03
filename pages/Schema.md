logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Interface]], [[JSON Schema]], [[GraphQL]], [[Programming/Language/Concept/Type/Structural]]

- # Schema
	- ## Overview
		- A **schema** is a declared **shape**: the expected structure, fields, types, and constraints something must satisfy to count as valid. It says *what a thing looks like*, not *what it does*.
		- The word carries two registers that share one idea. Generally, a schema is a **mental or organizing pattern**—a blueprint, template, or framework for how information is arranged or understood. In software, a schema is a **formal, often machine-checkable description** of the structure of data.
	- ## General-purpose sense
		- Outside computing, *schema* names a **pattern for organizing knowledge**: in cognitive psychology, a mental framework that shapes how new experience is interpreted; in ordinary use, an outline, blueprint, or plan that a concrete instance is measured against.
		- The common thread: the schema is the **expectation**, and any particular case either **conforms** to it or **violates** it.
	- ## Software sense
		- A **database schema** declares tables, columns, types, keys, and relationships—the structure rows must fit.
		- **Data-format schemas** ([[JSON Schema]], XML Schema, Avro, Protobuf) describe the fields and types a document or message must carry, so it can be **validated** and so tools can **generate code** from it.
		- A **[[GraphQL]] schema** declares the types, fields, and operations a service exposes—serving at once as documentation and as the contract clients query against.
		- In each case the schema is **separate from the data**: it is the specification, and instances are checked against it.
	- ## Schema and interface
		- A schema and an [[Interface]] are both **contracts**, but over different things: a schema describes the **shape of data** (fields, types, constraints), while an interface describes the **behavior** an implementation must provide (operations callers may rely on).
		- They meet at **structural typing** ([[Programming/Language/Concept/Type/Structural]]): "conforms to the schema" and "matches the interface's shape" are the same style of judgment—validity by fitting the expected shape, not by declared identity.
	- ## Misconceptions
		- A schema is not the data—it is the **template the data is judged against**.
		- A schema need not be rigid: schema-on-read systems apply the expected shape when data is *used* rather than when it is stored.
