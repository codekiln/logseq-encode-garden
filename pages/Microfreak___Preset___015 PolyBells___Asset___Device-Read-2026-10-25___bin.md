logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # PolyBells slot 15 capture
	- [Download the slot 15 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___015%20PolyBells___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 15 over USB on October 25, 2026 with `mise run microfreak:download --slot 15`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `cbfdbeacaecaf7c0c074f65e3c26932bf67015fa08a15a0b5d153b64c2ab00c8`.
