alias:: [[Data Definition Language]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Diataxis/Explanation]], [[Logseq/Entity/Term/Acronym]]
- # Data Definition Language (DDL)
	- ## Overview
		- **Data Definition Language** is the part of a database language used to define and change database structures. In [[SQL]], `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE` are DDL statements. They describe the shape and constraints of data rather than individual row values.
	- ## Why it matters
		- DDL turns a [[Database/Schema]] into structures a database system can enforce: tables, columns, data types, keys, and constraints. Changing those definitions changes which data the system accepts and which queries applications can make.
		- A schema change may require existing data to be checked or transformed. The effects of a DDL statement on locks, transactions, and running queries depend on the database engine.
	- ## Place in database systems
		- [[Database/System/Theory]] considers the relationship between the logical data model, queries, transactions, and physical storage. DDL expresses part of that logical model in a language the system can execute.
