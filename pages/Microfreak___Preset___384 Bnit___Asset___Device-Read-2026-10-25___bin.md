logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Bnit slot 384 capture
	- [Download the slot 384 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___384%20Bnit___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 384 over USB on October 25, 2026 with `mise run microfreak:download --slot 384`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `0485ad9efaec5f890cb79f0c23aa98fb1bbf8a87040450e89326afc546e1fb7f`.
