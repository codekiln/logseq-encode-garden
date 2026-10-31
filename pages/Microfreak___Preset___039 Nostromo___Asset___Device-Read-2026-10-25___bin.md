logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Nostromo slot 39 capture
	- [Download the slot 39 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___039%20Nostromo___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 39 over USB on October 25, 2026 with `mise run microfreak:download --slot 39`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `bcb190e820c84cb5db4c16dfa5247349cd60d4696e6a350d77bb019fa88f0e98`.
