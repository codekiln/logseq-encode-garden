logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Corrosion slot 34 capture
	- [Download the slot 34 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___034%20Corrosion___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 34 over USB on October 25, 2026 with `mise run microfreak:download --slot 34`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `1e1a244e18235ce523efb9a3eccb050c92ef850ef232d9c4b9e22523f10086cd`.
