tags:: [[npm/lib]]

- # `nbb-logseq`
	- [[AI Notes]]
		- [[2025-05-10 Sat]]
			- This package provides a [[ClojureScript]] scripting environment tailored for Logseq, enabling advanced queries and operations that go beyond the capabilities of the standard [[Logseq/Plugin/API]]. It leverages `nbb`, a ClojureScript runtime for Node.js, and includes support for libraries like [[Datascript]], facilitating powerful interactions with Logseq graphs.
			- For instance, `nbb-logseq` allows you to execute scripts that can query any Logseq graph, making it a valuable tool for tasks such as graph validation, data export, and complex data manipulations [citation](https://www.npmjs.com/package/%40logseq/nbb-logseq).
			- In contrast, **`@logseq/libs`** is the official Logseq SDK, primarily written in [[Typescript]], and is designed for developing Logseq plugins. While it provides a comprehensive set of APIs for plugin development, it may not offer the same level of flexibility for detailed queries as `nbb-logseq`.
	- ### For Logseq users
		- `nbb-logseq` provides [easy CLJS scripting on Node.js](https://github.com/babashka/nbb) for Logseq. Since logseq is primarily written with [ClojureScript](https://clojurescript.org/), this scripting environment has capabilities that are not possible in any other environment. For example, [see here](https://github.com/logseq/nbb-logseq/blob/HEAD/examples/#query.cljs) for a script that queries any logseq graph.
	- ### [](https://www.npmjs.com/package/%40logseq/nbb-logseq?#for-clojure-users) For Clojure users
		- `nbb-logseq` is a custom version of [nbb](https://github.com/babashka/nbb) that bundles support for datascript, datascript-transit and a couple other cljs libraries that are useful to logseq. A good amount of the datascript API is available as [seen by its tests](https://github.com/babashka/nbb-features/blob/main/test/features/datascript/test_runner.cljs). Since nbb only loads features/libraries when they are required, users can write datascript based CLIs without concern of loading the other libraries.