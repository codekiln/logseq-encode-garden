logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Math/Projection]], [[Palimpsest]]
- # Database View
	- ## Overview
		- A database view is a named presentation of selected or transformed data. It lets a reader work with a useful projection of underlying records without confusing that presentation with the records themselves.
		- In relational databases, a view commonly names a query and exposes its result like a table. A view can join, filter, or reshape data from one or more source tables.
	- ## In a knowledge garden
		- A page can act as a view when it gathers linked or embedded source material and commentary into one readable surface. The source pages remain separately addressable; the view determines how they are presented together.
		- For a source garden and a local discussion, the view can place the upstream page alongside local annotations. This makes the combined reading resemble a [[Palimpsest]] while preserving the distinction between source and response.
	- ## Context
		- A view is not necessarily a copy of its source. In SQL, a regular view is defined by a query; the database evaluates that query when the view is used. A materialized view instead stores query results and must be refreshed.
		- [PostgreSQL's tutorial on views](https://www.postgresql.org/docs/17/tutorial-views.html) describes a view as a named query usable like an ordinary table.
