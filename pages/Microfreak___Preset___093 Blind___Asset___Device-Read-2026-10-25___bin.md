logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Blind slot 93 capture
	- [Download the slot 93 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___093%20Blind___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 93 over USB on October 25, 2026 with `mise run microfreak:download --slot 93`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `8cc204cc52b276aaf7c0cac90686c3b807203b4c1fca8a8898ab0ae7c3ea45a8`.
