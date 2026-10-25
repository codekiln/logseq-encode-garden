logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Lowride slot 226 capture
	- [Download the slot 226 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___226%20Lowride___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 226 over USB on October 25, 2026 with `mise run microfreak:download --slot 226`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4f139fc68637c5241370b8703b6dea41e1c516f13297a567677840e7e30cb4ee`.
