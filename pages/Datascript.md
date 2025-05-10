alias:: [[Programming/Language/Query/Datascript]]

- # DataScript
	- See [[Person/Nikita Prokopov/GitHub/datascript]]
	- DataScript is a ClojureScript implementation of [[Datalog]], a declarative logic programming language originally derived from Prolog.
	- It is an in-memory database that runs entirely in the browser (or any JavaScript environment), making it suitable for client-side applications, offline-first apps, and reactive UIs.
	- Unlike SQL, DataScript is based on *facts* and *rules*, allowing for expressive and composable queries over relational-style data.
	- Querying in DataScript resembles logic programming: instead of specifying procedures, you describe the shape of the data you want, and the engine figures out how to get it.
	- It is often used in reactive frameworks (e.g., re-frame) to manage app state in a normalized and queryable way, akin to how GraphQL treats data access.
	- DataScript enables time-travel debugging, immutable histories, and derived data views — powerful tools in modern frontend architecture.
	- Compared to [[Logseq/Plugin/API]], DataScript queries provide more precise and composable access to the underlying graph, making it a key tool for power users and internal tool builders.
	- Similar technologies: [[Datalog]], [[SQL]], [[GraphQL]]