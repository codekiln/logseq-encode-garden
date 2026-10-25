logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Rectify slot 217 capture
	- [Download the slot 217 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___217%20Rectify___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 217 over USB on October 25, 2026 with `mise run microfreak:download --slot 217`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `06acda365e886330e87de3e0b41100016061daeb84db51428e3bb692cc370800`.
