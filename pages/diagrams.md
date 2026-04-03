logseq-entity:: [[Logseq/Entity/software-project]]
tags:: [[Software/Library]]
see-also:: [[D2]], [[Graphviz]], [[Structurizr]], [[Diagram/Mermaid]]
- # [mingrammer/diagrams](https://github.com/mingrammer/diagrams)
	- Python **diagram-as-code** library aimed at **cloud and system architecture** (not dependency extraction from source): labeled nodes, edges, **clusters** (subgraphs), and large built-in **provider/icon sets** (AWS, SaaS, on-prem, common frameworks).
	- Renders via **[[Graphviz]]** (Graphviz/dot under the hood), so output is compiled from code rather than hand-drawn; supports **custom icons** when built-ins miss a vendor (e.g. AI or niche APIs).
	- **Tradeoffs**: layout and visual language stay Graphviz-like (“competent but stiff” without spacing, labels, clustering, and icon choices); elaborate diagrams can hit **cluster/edge limitations** ([GitHub issue #17](https://github.com/mingrammer/diagrams/issues/17)).
