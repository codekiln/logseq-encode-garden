logseq-entity:: [[Logseq/Entity/Website]]
created-by:: [[Shiftbrain]]
date-created:: [[2019]]
via:: [[Awwwards]]
see-also:: [[Design/Good/Web]]

- # [Misato Town — みさとと](http://www.town.shimane-misato.lg.jp/misatoto/)
	- The rebranding microsite for Misato, a small town of ~4,600 in Shimane prefecture, Japan, built by the studio [[Shiftbrain]] as the town's rebranding partner.
	- ## Why it is notable
		- The scene is a single continuous, well-produced animation rather than typical jerky parallax: scroll position is mapped to a point along a **pre-designed keyframed timeline** with built-in interpolation, so the [[WebGL]] scene plays like film that the reader scrubs — the scroll drives *time*, not objects directly.
		- Flat 2D illustrations are lifted into a 3D [[WebGL]] scene; an illustrated map doubles as scroll-triggered navigation, with an overlay menu.
	- ## Stack
		- [[Three.js]] over [[WebGL]], [[SVG]] artwork, bundled with [[Webpack]]; responsive.
	- ## Awards
		- [Awwwards — Site of the Day, 2019-11-07](https://www.awwwards.com/sites/misato-town)
