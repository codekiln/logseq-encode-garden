logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Press So slot 84 capture
	- [Download the slot 84 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___084%20Press%20So___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 84 over USB on October 25, 2026 with `mise run microfreak:download --slot 84`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `846e1ee3c17d60f029df9e6ff6bd8b0a1e86c555cdb18a3e2c56e5a7117871f2`.
