logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Hollows slot 57 capture
	- [Download the slot 57 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___057%20Hollows___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 57 over USB on October 25, 2026 with `mise run microfreak:download --slot 57`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `a73ac875ed2b10e959456a1c479799587db8ed899d05a7ce86465492b58dfafe`.
