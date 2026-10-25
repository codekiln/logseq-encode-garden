logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Padel slot 103 capture
	- [Download the slot 103 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___103%20Padel___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 103 over USB on October 25, 2026 with `mise run microfreak:download --slot 103`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `678d5d43bf109b327e4e5c9d387f61a87fc13d65e855985f4ae6f39bb5f78257`.
