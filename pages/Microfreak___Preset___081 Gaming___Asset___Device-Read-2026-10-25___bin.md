logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Gaming slot 81 capture
	- [Download the slot 81 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___081%20Gaming___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 81 over USB on October 25, 2026 with `mise run microfreak:download --slot 81`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `a03a1bbec5b2b6831ff282e436f6d281274f32ae41c66de34454e967d6569cf4`.
