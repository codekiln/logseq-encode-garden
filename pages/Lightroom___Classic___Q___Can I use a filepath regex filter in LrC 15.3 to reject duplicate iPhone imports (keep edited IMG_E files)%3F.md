logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]

- # In [[Lightroom/Classic]], can I use a filepath regex filter in LrC 15.3 to reject duplicate iPhone imports (keep edited `IMG_E…` files)?
	- ## My Notes
		- Observed pairs when importing from iPhone: originals look like `…-IMG_####.HEIC` / `…-IMG_####.MOV`, while on-phone crops/edits look like `…-IMG_E####.HEIC` / `…-IMG_E####.MOV` (Apple Photos commonly keeps an original plus a rendered “edited” asset).
		- [[My Answer]]
			- search for `filename does not contain` with `IMG_E`, then reject all.
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** **No** — [[Lightroom/Classic]] does **not** expose a Library Filter (or Smart Collection rule) that matches **regular expressions** against full **file paths**. Text filtering is **substring / rule-based** (for example **contains**, **starts with**, **is**, **does not contain** depending on the field), not regex.
			- **What you can do instead (usually “easy enough”):** build a **Smart Collection** (or use the **Library Filter bar → Text**) on **Filename** (and optionally combine with **Source** / folder if you only want imports from a specific mount) using rules that approximate your intent:
				- **To isolate likely “originals” (not the `IMG_E…` edit)** for bulk reject/delete: match filenames that **contain** `IMG_` **and** **do not contain** `IMG_E` (important: `IMG_E1234…` **still contains** the substring `IMG_` at the start, so **“contains `IMG_`” alone is not enough**—adding **“doesn’t contain `IMG_E`”** is what separates `IMG_1234…` from `IMG_E1234…`; sanity‑check a few rows in Grid view before bulk operations).
				- **To isolate likely on-phone edits:** **Filename** **contains** `IMG_E` (covers `IMG_E####.HEIC` / `.MOV` style names).
			- **Why duplicates happen:** when you edit in Apple Photos, iOS often keeps **both** the original capture and a **new file** for the edited render; wired import can surface both to Lightroom, which treats them as separate files (community threads discuss this pattern for `IMG_…` vs `IMG_E…` pairs).
			- **Going forward:** if the goal is “only what I saw on the phone,” many people either **cull during Import** (uncheck the `IMG_…` rows when the `IMG_E…` sibling is present) or **avoid pre-editing in Photos** before a Lightroom-first workflow—neither is regex-based, but both reduce the pile-up.
			- **If you truly need regex on paths:** plan on **outside‑Lightroom** tooling (for example a small script against exported file lists, or a **plugin/SDK** workflow), not a built-in 15.3 Library filter.
			- ### Sources
				- [LRC imports both the original & edited version of each image from iPhone — Lightroom Queen forums](https://www.lightroomqueen.com/community/threads/lrc-imports-both-the-original-edited-version-of-each-image-from-iphone.42899/)
				- [LR importing duplicate images from iPhone — Lightroom Queen forums](https://www.lightroomqueen.com/community/threads/lr-importing-duplicate-images-from-iphone.42583/)
				- [How to find photos in a catalog in Lightroom Classic — Adobe Help (Library Filter / text search fields)](https://helpx.adobe.com/lightroom-classic/help/finding-photos-catalog.html)