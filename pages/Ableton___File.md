alias:: [[Ableton/File Types]], [[Ableton File Types]], [[Ableton/File/Concept/Storing in Git]] 
tags:: [[Diataxis/Explanation]]

- # Ableton File Types – Conceptual Overview
	- ## Overview
		- Ableton Live uses a variety of proprietary file types to represent sets, clips, presets, and metadata. Some are human-readable (XML or JSON), others are binary. Understanding these formats is essential for workflows involving version control (e.g., Git).
	- ## Context
		- Many Ableton users want to store projects in Git for collaboration, history, and diffs. The challenge is that some file types are opaque binaries, while others can be normalized for text-based diffs. Knowing which is which helps decide what to commit, ignore, or preprocess.
	- ## Key Principles
		- **Textual formats** (XML/JSON) are git-friendly with proper filters.
		- **Binary formats** (analysis files, waveforms, grooves) are not useful to version and can be regenerated.
		- **Archive formats** (packs) should be treated as immutable binaries.
		- **Programmatically generated files** (e.g., `.asd`) should be excluded since Live will recreate them.
	- ## File Types & Internal Structure
		- {{embed [[Ableton/File/.als]]}}
		- {{embed [[Ableton/File/.alc]]}}
		- {{embed [[Ableton/File/.adg]]}}
		- {{embed [[Ableton/File/.adv]]}}
		- {{embed [[Ableton/File/.amxd]]}}
		- {{embed [[Ableton/File/.ask]]}}
		- {{embed [[Ableton/File/.alp]]}}
		- {{embed [[Ableton/File/.asd]]}}
		- {{embed [[Ableton/File/.ams]]}}
		- {{embed [[Ableton/File/.agr]]}}
	- ## Misconceptions
		- **Myth**: All Ableton files are binary and unsuitable for Git.  
		  **Reality**: Many are gzipped XML or JSON and can be made git-friendly with filters.
		- **Myth**: `.asd` files must be backed up.  
		  **Reality**: They’re metadata caches and should be ignored in source control.
	- ## Recommendations for Git
		- **Store with filters**: `.als`, `.alc`, `.adg`, `.adv`, `.amxd`, `.ask`.
		- **Ignore**: `.asd` (auto-regenerated).
		- **Store as binary**: `.alp`, `.ams`, `.agr` (no useful diffs).
		- **Use custom diff drivers**:
			- `.als`/`.alc`/`.adg`/`.adv`: `gzip -cd`.
			- `.amxd`: strip header, parse JSON.
			- `.ask`: plain XML diff.
	- ## See Also
		- [[Person/Zack Steinkamp/blog/posts/2022-02-15-git-diff-amxd-max]]
		- [[GitHub/codekiln/ableton-live-git-hooks]]