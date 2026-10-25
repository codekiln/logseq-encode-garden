logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Init slot 401 capture
	- [Download the slot 401 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___401%20Init___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 401 over USB on October 25, 2026 with `mise run microfreak:download --slot 401`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `d08d563d245a4922f388bbfbf508f5ab23db1a44deba91ed139d2ee9afbae80f`.
